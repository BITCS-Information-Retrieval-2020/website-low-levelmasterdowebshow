<template>
<div class="index">
  <!-- <background></background> -->
    <el-container>
      <el-aside>
        <navigate></navigate>
      </el-aside>

      <el-container>
      <el-header>
        <el-col><div 
          class="" style="font-weight:700;font-size:50px;text-align:center;margin-top:3%">
          Low-level Master Search
          </div>
        </el-col>
      </el-header>
      <el-main>
        <el-card class="card" style="margin-top:5%">
        <el-row>
            <el-col><div class="" style="margin-left:10%;margin-right:10%">高级检索</div></el-col>
        </el-row>
      
        <el-form ref="queryForm" :model="queryForm" :rules="rules" style="margin-top:3%;margin-left:10%;margin-right:10%">
          <el-form-item
              v-for="(item, index) in queryForm.items"
              :label="'查询项' + (index+1)"
              :key="item.key"
              :prop="'items.' + index + '.value'"
              :rules="{
              required: true, message: '此处不能有空', trigger: 'blur'
              }"
              
          >
              <el-input v-model="item.content" style="width:80%;float:left" placeholder="请输入查询内容">
                  <el-select v-model="item.value" slot="prepend" style="float:right" placeholder="请选择">
                      <el-option label="title" value="title"></el-option>
                      <el-option label="abstract" value="abstract"></el-option>
                      <el-option label="paper_content" value="paper_content"></el-option>
                      <el-option label="video_content" value="video_content"></el-option>
                      <el-option label="authors" value="authors"></el-option>
                  </el-select>
              </el-input>
              <i class="el-icon-remove-outline" style="font-size:20px" @click.prevent="removeItem(item)"></i>
              <i class="el-icon-circle-plus-outline" style="font-size:20px" @click.prevent="addItem()"></i>
          </el-form-item>
              


          <el-form-item label="起始时间">
              <el-date-picker type="date" placeholder="选择日期" v-model="queryForm.startDate" value-format='yyyy-MM-dd' style="width: 80%;float:left"></el-date-picker>
          </el-form-item>
          <el-form-item label="结束时间">
              <el-date-picker type="date" placeholder="选择日期" v-model="queryForm.endDate" value-format='yyyy-MM-dd' style="width: 80%;float:left"></el-date-picker>
          </el-form-item>

          <el-form-item label="排序方式" prop="arrangeMethod">
              <el-radio-group v-model="queryForm.arrangeMethod" style="margin-top:2%;">
                  <el-radio :label="1">年份</el-radio>
                  <el-radio :label="2">相关度</el-radio>
              </el-radio-group>
          </el-form-item>
          
          <el-form-item>
              <el-button type="primary" style="margin-left:10%;margin-right:20%" @click="submitForm('queryForm')">检索</el-button>
          </el-form-item>
        </el-form>
        </el-card>
      </el-main>
      </el-container>
    </el-container>
</div>
</template>

<script>
import navigate from '../components/navigate'
import background from '../components/background'

import Vue from 'vue'
export default {
    data() {
      return {
        queryForm: {
          queryField: '',
          queryContent: '',
          items: [{
             value: ''
           }],
          startDate: '',
          endDate: '',
          arrangeMethod: '',
        },
        rules: {
          queryField: [
            { required: true, message: '请选择查询字段', trigger: 'change' },
          ],
          queryContent: [
            { required: true, message: '请输入查询内容', trigger: 'blur' }
          ],
          arrangeMethod: [
            { required: true, message: '请选择排序方式', trigger: 'change' }
          ],
        },        
      }
		},
		components:{
    	navigate//, background
  	},
    mounted() {
    },
    methods: {
        addItem() {
            this.queryForm.items.push({
                value: '',
                key: Date.now()+2
            });
        },
        removeItem(item) {
            var index1 = this.queryForm.items.indexOf(item)
            if (index1 !== 0) {
            this.queryForm.items.splice(index1, 1)
            }
        },
        
        submitForm(formName) {
            var sort_value = ""
            var item_dict ={}
            this.$refs[formName].validate((valid) => {
              if (valid) {            
                if(this.queryForm.arrangeMethod == 1){
                  sort_value = "year"
                } else if(this.queryForm.arrangeMethod == 2){
                  sort_value = "relevance"
                }

                console.log(this.queryForm.items)
                for(let item of this.queryForm.items) {
                   var item_key = item.value
                   var item_value = item.content
                   if(item_dict.hasOwnProperty(item_key)){
                     item_value = item_value + ","+item_dict[item_key]
                   }
                   item_dict[item_key] = item_value
                }
                console.log(item_dict)

                console.log(this.queryForm.items)
                let postData = this.$qs.stringify({
                  query_type: 'advanced_search',
                  query: this.queryForm.queryContent,
                  match: item_dict,
                  yearfrom: this.queryForm.startDate,
                  yearbefore: this.queryForm.endDate,
                  sort: sort_value
                });
                
                this.axios({
                    method: 'post',
                    url:'/advanced_search/',
                    data:postData
                }).then((res)=>{
                  console.log('get response')
                  var user_id=res.data[0]["user_id"]
                  console.log("user id:", user_id)
                  this.$router.push({
                    name:"search-list",
                    params:{
                      user_id : user_id,
                      res : res
                    }
                  })


                    
                });
              } else {
                console.log('error submit!!');
                return false;
              }
          });
        },
    }
}
</script>


<style>

.card {
    background-color: rgba(170, 196, 236, 0);
}

.el-select {
    width: 150px;
}
.input-with-select .el-input-group__prepend {
background-color: #fff;
}
.highlight{
    background-color: yellow
}
.search-row {
    margin-bottom: 10px;
    margin-top: 10px
}
.table-expand-form label {
    width: 90px;
    color: #99a9bf;
}
.index{
  text-align: center
}
</style>