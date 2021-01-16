from searcher import *

S = Searcher(index_name='paperdb', doc_type='papers')

search_info = {
    'query_type': 'integrated_search',
    'query': 'pose',  # 用户查询的内容
    'match': {
        'title': True,  # True/False表示是否检索这个字段的内容
        'abstract': True,
        'paperContent': True,
        'videoContent': True,
    },
    'filter': {
        'yearfrom': 1000,  # paper的年份限制
        'yearbefore': 3000,
    },
    # 'sort': 'relevance',
    'sort': 'year',  # 排序方式：year/cited/relevance
    'is_filter': False,  # 是否先过滤后排序，建议True，提升检索效率
    'is_rescore': False,  # 是否采用重排序，依据relevance排序时建议True，增强排序效果
    'is_cited': False  # 是否使用引用量参与排序，由于未爬取引用量字段，只能为False
}

paper, paper_id, paper_num = S.search_paper_by_name(search_info)
print(paper_id)

print(len(dict.fromkeys(paper_id)))

# print(f'{paper[0]['title'], paper[0]['authors'], paper[0]['publisher'], paper[0]['year']}')
# print('{}'.format(paper[0]['title']))


# if __name__ == '__main__':
#     a=[1, 2, 3, 4]
#     res = {}
#     for it in range(len(a)):
#         res[a[it]]=it
#     print(res)


# a = {'title': 'Continuous Wasserstein-2 Barycenter Estimation without Minimax Optimization', 'arxiv_id': None, 'authors': [{'firstName': 'Anonymous', 'lastName': ''}], 'year': '2021', 'publisher': 'ICLR 2021 1', 'abstract': 'Wasserstein barycenters provide a geometric notion of the weighted average of probability measures based on optimal transport. In this paper, we present a scalable algorithm to compute Wasserstein-2 barycenters given sample access to the input measures, which are not restricted to being discrete. While past approaches rely on entropic or quadratic regularization, we employ input convex neural networks and cycle-consistency regularization to avoid introducing bias. As a result, our approach does not resort to minimax optimization. We provide theoretical analysis on error bounds as well as empirical evidence of the effectiveness of the proposed approach in low-dimensional qualitative scenarios and high-dimensional quantitative experiments.', 'paperUrl': 'https://paperswithcode.com/paper/continuous-wasserstein-2-barycenter', 'paperPdfUrl': 'https://openreview.net/pdf?id=3tFAs5E-Pe', 'codeUrl': ''}

# a = 'match[title]'
#
# print(a[6:-1])
