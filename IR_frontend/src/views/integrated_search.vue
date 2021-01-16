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
            <el-col><div class="" style="margin-left:10%;margin-right:10%;font-weight:700">综合检索</div></el-col>
        </el-row>

        <el-form ref="queryForm" :model="queryForm" :rules="rules" style="margin-top:3%;margin-left:10%;margin-right:10%">
            <el-form-item label="查询字段" prop="queryField">
                <el-select v-model="queryForm.queryField" placeholder="请选择" multiple style="width:80%;float:right">
                    <el-option label="title" value="title"></el-option>
                    <el-option label="abstract" value="abstract"></el-option>
                    <el-option label="paper_content" value="paper_content"></el-option>
                    <el-option label="video_content" value="video_content"></el-option>
                    <el-option label="authors" value="authors"></el-option>
                </el-select>
            </el-form-item>

            <el-form-item label="查询内容" prop="queryContent">
                <el-input v-model="queryForm.queryContent" style="width:80%;float:right"></el-input>
            </el-form-item>
             <el-form-item label="起始时间">
                <el-date-picker type="date" placeholder="选择日期" v-model="queryForm.startDate" value-format='yyyy-MM-dd' style="width: 80%;float:right"></el-date-picker>
            </el-form-item>
            <el-form-item label="结束时间">
                <el-date-picker type="date" placeholder="选择日期" v-model="queryForm.endDate" value-format='yyyy-MM-dd' style="width: 80%;float:right"></el-date-picker>
            </el-form-item>

            <el-form-item label="排序方式" prop="arrangeMethod" style="color:#ffffff">
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

import Vue from "vue"
export default {
  data() {
    return {
      queryForm: {
          queryField: '',
          queryContent: '',
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
  mounted() {},
  methods: {
    submitForm(formName) {
        var sort_value = ""
        // var match_list = []
        this.$refs[formName].validate((valid) => {
          if (valid) {            
            if(this.queryForm.arrangeMethod == 1){
              sort_value = "year"
            } else if(this.queryForm.arrangeMethod == 2){
              sort_value = "relevance"
            }
            // for (var i = 0; i < this.queryForm.queryField.length; i++) {
            //   match_list = match_list.concat(this.queryForm.queryField[i])
            // }
            // console.log(match_list)
            let postData = this.$qs.stringify({
              query_type: 'integrated_search',
              query: this.queryForm.queryContent,
              match: this.queryForm.queryField,
              yearfrom: this.queryForm.startDate,
              yearbefore: this.queryForm.endDate,
              sort: sort_value
            });
            this.axios({
                method: 'post',
                url:'/integrated_search/',
                data:postData
            }).then((res)=>{
            console.log('get response')
            console.log(res)
            // const options = {name:"search-list", query:this.queryForm.queryContent, params: {query_result: res}}
            // this.$router.push({
            //     options
            //   })
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
};
</script>


<style>

.card {
  background-color: rgba(170, 196, 236, 0);
  font-weight: 900;
}

.el-select {
    width: 80%;
}
.input-with-select .el-input-group__prepend {
    background-color: #fff;
}
.highlight {
  background-color: yellow;
}
.search-row {
  margin-bottom: 10px;
  margin-top: 10px;
}
.table-expand-form label {
  width: 90px;
  color: #99a9bf;
}
.index {
  text-align: center;
}

</style>
