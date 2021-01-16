from django.views.generic import View
# from searcher import *
from mdsearch import Searcher
from django.shortcuts import HttpResponse
import json
from utils import *
import os, sys

# 并发访问字典
# {user_id:[paper, {paper_id:num}]}
users = {}


# Create your views here.
# 综合查询
class Integrated_search(View):
    # def get(self, request):
    #
    #     return render(request, 'index.html')

    def post(self, request):
        # 获取检索所需参数
        query_type = request.POST.get('query_type')
        query = request.POST.get('query')
        yearfrom = request.POST.get('yearfrom')
        yearfrom = yearfrom[:yearfrom.find('-')]
        yearbefore = request.POST.get('yearbefore')
        yearbefore = yearbefore[:yearbefore.find('-')]
        sort = request.POST.get('sort')
        # 配置match参数
        bool_match = {
            'title':False,
            'abstract':False,
            'paperContent':False,
            'videoContent':False
        }
        for it in dict(request.POST).keys():
            if it[:5] == 'match':
                bool_match[request.POST.get(it)] = True
        # 构造结果
        search_info = {
            'query_type': query_type,
            'query':query,
            'match':{
                'title':bool_match['title'],
                'abstract':bool_match['abstract'],
                'paperContent':bool_match['paperContent'],
                'videoContent':bool_match['videoContent']
            },
            'filter':{
                'yearfrom':yearfrom,
                'yearbefore':yearbefore
            },
            'sort':sort,
            'is_filter':True,
            'is_rescore':True if sort == 'relevance' else False,
            'is_cited':False
        }
        # 获取数据
        S = Searcher(index_name='paperdb', doc_type='papers')
        paper, paper_id, paper_num = S.search_paper_by_name(search_info)
        # 以下用于并发访问
        global users
        # 获取用户唯一标识符
        user_id = UID()
        # 构造paper_id字典，便于查询
        paper_id_dict = {}
        for it in range(len(paper_id)):
            paper_id_dict[paper_id[it]] = it
        users[user_id] = [paper, paper_id_dict]
        # 构造返回数据
        res = []
        i = 0
        for it in paper:
            # print(it['authors'])
            res.append(
                {
                    'paper_id':paper_id[i],
                    'title':it['title'],
                    'authors':it['authors'],
                    'publisher':it['publisher'] if 'publisher' in it.keys() else '',
                    'year':it['year'] if 'year' in it.keys() else '',
                    # 用于并发访问，标识这一用户
                }
            )
            i += 1
        res.insert(0, {'user_id':user_id})
        return HttpResponse(json.dumps(res))


# 高级查询
class Advanced_search(View):
    # def get(self, request):
    #
    #     return render(request, 'index.html')

    def post(self, request):
        # 获取检索所需参数
        query_type = request.POST.get('query_type')
        yearfrom = request.POST.get('yearfrom')
        yearfrom = yearfrom[:yearfrom.find('-')]
        yearbefore = request.POST.get('yearbefore')
        yearbefore = yearbefore[:yearbefore.find('-')]
        sort = request.POST.get('sort')
        # 配置match参数
        string_match = {
            'title':None,
            'abstract':None,
            'paperContent':None,
            'videoContent':None
        }
        for it in dict(request.POST).keys():
            if it[:5] == 'match':
                # 抽取出key值
                key = it[6:-1]
                string_match[key] = request.POST.get(it)
        # 构造结果
        search_info = {
            'query_type': query_type,
            # 'query':query,
            'match':{
                'title':string_match['title'],
                'abstract':string_match['abstract'],
                'paperContent':string_match['paperContent'],
                'videoContent':string_match['videoContent']
            },
            'filter':{
                'yearfrom':yearfrom,
                'yearbefore':yearbefore
            },
            'sort':sort,
            'is_filter':False,
            'is_rescore':True if sort == 'relevance' else False,
            'is_cited':False
        }
        # 获取数据
        S = Searcher(index_name='paperdb', doc_type='papers')
        paper, paper_id, paper_num = S.search_paper_by_name(search_info)
        # 以下用于并发访问
        global users
        # 获取用户唯一标识符
        user_id = UID()
        # 构造paper_id字典，便于查询
        paper_id_dict = {}
        for it in range(len(paper_id)):
            paper_id_dict[paper_id[it]] = it
        users[user_id] = [paper, paper_id_dict]
        # 构造返回数据
        res = []
        i = 0
        for it in paper:
            res.append(
                {
                    'paper_id':paper_id[i],
                    'title':it['title'],
                    'authors':it['authors'],
                    'publisher':it['publisher']  if 'publisher' in it.keys() else '',
                    'year':it['year']  if 'year' in it.keys() else '',
                    # 用于并发访问，标识这一用户
                    'user_id':user_id
                }
            )
            i += 1
        return HttpResponse(json.dumps(res))


# 详情
class Paper_details(View):
    def post(self, request):
        # 标识用户
        user_id = request.POST.get('user_id')
        # 标识paper
        paper_id = request.POST.get('paper_id')
        # 查询所选paper的详情
        global users
        select_paper = users[user_id][0][users[user_id][1][paper_id]]
        return HttpResponse(json.dumps(select_paper))


class Test(View):
    def post(self, request):
        print(request.POST)
        return HttpResponse(json.dumps([]))