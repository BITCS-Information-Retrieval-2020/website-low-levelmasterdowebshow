<template>
    <div>
      <!--
      <video :src="videoSrc" :poster="videoImg" :autoplay="playStatus" height="421" width="700" :muted="muteStatus">
        your browser does not support the video tag
      </video>
      <button @click="playClick" :class="{hide: isPlay}">点击播放</button> -->
      <!--class="video-js vjs-default-skin vjs-big-play-centered" -->
      
      <span class='set_size' style="margin-left:3%">{{ publisher }}</span>
      <span class='set_size'>{{ publish_year }}{{ "  " }}</span>
      <el-divider></el-divider>

      <h2 align='center'>
        {{ paper_title }}
      </h2>

      <div class='author_style'>
          {{authors}}
      </div>
      <p></p>
      <el-divider></el-divider>
      <div class="abstract" style="margin-left:3%;margin-right:3%">
        <b>Abstract:</b>
        {{ abstract }}
      </div>
      
      

      <h3></h3>
      <video :preload="preload" class="video_adjust" 
        fluid="true"
        playbackRates="[0.5, 1.0, 1.5, 2.0]"
        :height="height" 
        :width="width" 
        align="center" 
        :controls="controls"  
        :autoplay="autoplay"
      >
        <source :src="videoSrc" type="video/mp4">
      </video>
      <el-divider style="margin : 10px, 0;"></el-divider>  

      <div class="Resource">
        <el-table
          :data="tableData"
          style="width: 100%"
          align="center">
          <el-table-column
            prop="resource"
            label="Resource"
            width="300">
          </el-table-column>
          <el-table-column
            prop="url"
            label="Link"
            width="300">
               <template slot-scope="scope">
                <el-link icon="el-icon-position" :underline="false" :href="scope.row.url" target="_blank">url
                </el-link>
              </template>
          </el-table-column>
          <el-table-column
            prop="describe"
            label="Describe"
            width="300">
          </el-table-column>
        </el-table>
      </div>      
    </div>
</template>

<script>
import Vue from 'vue'

export default {
  data () {
    return {
      videoSrc: '',
      playStatus: '',
      muteStatus: '',
      isMute: true,
      isPlay: false,
      width: '820', // 设置视频播放器的显示宽度（以像素为单位）
      height: '500', // 设置视频播放器的显示高度（以像素为单位）
      preload: 'auto', //  建议浏览器是否应在<video>加载元素后立即开始下载视频数据。
      controls: true, // 确定播放器是否具有用户可以与之交互的控件。没有控件，启动视频播放的唯一方法是使用autoplay属性或通过Player API。
      autoplay: 'false',
      

      paper_title: '',
      authors: '',
      pdf_url: '',
      code_url: '',
      publisher: '',
      publish_year: '',
      abstract: '',
      dataset: '',
      
      tableData:[],
    }
  },
  // 自动播放属性,muted:静音播放
  // autoplay: 'muted',

  methods: {
    getPaperInfo(){
      //获取页面跳转参数 : JSON字符串 >= JSON 对象
      var data = JSON.parse(localStorage.getItem("data"))
      // get Values
      this.paper_title = data["title"]
      this.publish_year = data["year"]
      this.abstract = data["abstract"]

      var author_str=""
      for(var j=0; j<data["authors"].length; j++){
        if(j == data["authors"].length-1){
          author_str = author_str + data["authors"][j]["firstName"] + ' ' + data["authors"][j]["lastName"]
        }
        else{
          author_str = author_str + data["authors"][j]["firstName"] + ' ' + data["authors"][j]["lastName"]
          author_str = author_str + ", "
        }
      }
      this.authors = author_str

      if("publisher" in data) {
        this.publisher = data["publisher"]
      }
      else {
        this.publisher = "unknown publisher"
      }
      if("videoSrc" in data) {
        this.videoSrc = data["videoSrc"]
      }
      else {
        this.videoSrc = ""
         this.$notify.error({
          title: 'Error',
          message: 'Not Find Video',
          duration: 3000,
        });
        console.log("Unknown Video")
      }
      if("paperPdfUrl" in data) {
        this.pdf_url = data["paperPdfUrl"]
      }
      else {
        this.pdf_url = ""
      }
      if("codeUrl" in data) {
        this.code_url = data["codeUrl"]
      }
      else {
        this.code_url = ""
      }
      if("datasetUrl" in data) {
        this.dataset = data["datasetUrl"]
      }
      else {
        this.dataset = ""
      }
      console.log(data)
      //dict 
      var NameMap = {1 : "PDF", 2 : "Code", 3 : "DataSet"}
      var UrlMap = {1: this.pdf_url, 2 : this.code_url, 3 : this.dataset}
      //fill the LINK table
      for(var i=1; i<=3 ; i++){
        console.log(" Map ", NameMap[i], UrlMap[i])
        var describe = UrlMap[i] ? "Official" : "Unkonwn"
          Vue.set(this.tableData, i,{
            resource: NameMap[i],
            url: UrlMap[i],
            describe: describe
          })
      }
    }
  },

  created(){
    this.getPaperInfo()
  }

}


</script>

<style scoped >

.el-table{
  font-size: 16px;
  font-family: Georgia, 'Times New Roman', Times, serif;
}

.el-divider{
  margin: 8px 0;
  background: 0 0;

  border-top: 1px solid #E6EBF5;
}

.set_size{
  font-size: 15px
}

.author_style{
  text-align: center;
}

.video_adjust{
  display: block;
  margin: auto;
  /* width : 80%; */
}
.abstract{
  font-family:"Microsoft YaHei";
  font-size: 14px;
  line-height: 1.5em;
}
</style>




