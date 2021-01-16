<template>
  <el-container>
    <el-header>
      <el-col>
      <div 
        class="result" style="font-weight:700;font-size:50px;text-align:center;margin-top:3%">
        Search Result
      </div>
      </el-col>
    </el-header>
    <el-main>  
    <el-table
      v-loading="loading"
      :data="paper_list_data"

      style="width: 100%;margin-left:8%;margin-top:3%">
      <el-table-column prop="id" label="序号" align="center" width="180"></el-table-column>
      <el-table-column prop="title" label="标题" align="center" width="300">
        <template slot-scope="scope">
         <router-link tag="a" @click.native="detail( scope.$index )" to="">
           {{ scope.row.title }}</router-link>
        </template>
      </el-table-column>
      <el-table-column prop="authors" label="作者" align="center" width="240"></el-table-column>
      <el-table-column prop="publisher" label="发表机构" align="center" width="180"></el-table-column>
      <el-table-column prop="year" label="出版年份" align="center" width="180"></el-table-column>
    </el-table>
    </el-main>
  </el-container>
</template>

<script>
import Vue from 'vue'
    export default {
      data() {
        return {

          paper_list_data: [],
          loading: true
        }
      },
      created() {
        this.get_paper_list()
      },
      methods: {
          
          detail(key){
            console.log(this.$route.params.user_id)
            let postData = this.$qs.stringify({
              user_id: this.$route.params.user_id,
              paper_id: this.$route.params.res.data[key+1].paper_id,
            });
            console.log(this.$route.params.res.data[key+1].paper_id),
            this.axios({
                method: 'post',
                url:'/paper_details/',
                data:postData
            }).then((res)=>{
              console.log(this.paper_list_data[key+1]["authors"])
              
            var {href} = this.$router.resolve({
              name:"paper-details",
/*               params:{
                data : res.data,
              } */
            });
            
            localStorage.setItem("data", JSON.stringify(res.data))
            window.open(href) 
            })

          },

          get_paper_list(){

              var user_id = this.$route.params.user_id
              var res = this.$route.params.res
              for(var i=1; i<res.data.length; i++)
              {
                  var author_str = ""

                  for(var j=0; j<res.data[i]["authors"].length; j++)
                  {
                    if(j == res.data[i]["authors"].length-1)
                    {
                      author_str = author_str + res.data[i]["authors"][j]["firstName"] + ' ' + res.data[i]["authors"][j]["lastName"]
                    }
                    else
                    {
                      author_str = author_str + res.data[i]["authors"][j]["firstName"] + ' ' + res.data[i]["authors"][j]["lastName"]
                      author_str = author_str + ", "
                    }
                  }
                  Vue.set(this.paper_list_data,i,{
                      id: i,
                      title: res.data[i]["title"],
                      authors: author_str,
                      publisher: res.data[i]["publisher"],
                      year: res.data[i]["year"]
                  })

              }
                this.loading = false
          }
      }
    }
</script>


<style scoped>

.result{
  color:rgb(32, 104, 236)
}


</style>