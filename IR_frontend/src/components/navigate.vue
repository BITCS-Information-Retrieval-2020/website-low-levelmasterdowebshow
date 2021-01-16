<template>
  <div>
    <el-col :span="12">
      <el-menu
        default-active="activeIndex"
        class="el-menu-vertical-demo"
        
        text-color="#000"
        active-text-color="#000000"
        default-openeds=[2]>
        <!-- <el-menu-item index="1" @click="gotoPage(1)"> -->
        <el-menu-item index="1">
          <template slot="title">
            <i class="el-icon-location" style="color:blue"></i>
            <span style="color:white;font-size:17px">Low-level Master</span>
          </template>
        </el-menu-item>
        <el-submenu index="2" unique-opened="true" >
          <template slot="title">
            <i class="el-icon-menu" style="color:blue"></i>
            <span style="color:white">首页</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="3" @click="gotoPage(2)">综合检索</el-menu-item>
            <el-menu-item index="4" @click="gotoPage(3)">高级检索</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
    </el-col>
    <router-view/>
    <!-- <foot ></foot> -->
  </div>
</template>

<script>
export default {
  data() {
      return {
        activeIndex: '',
        page_index: 2,
      }
  },
  methods:{
    gotoPage(i){
      // if(i==1)
      // {
      //   window.location.href
      //   this.$router.push({path:"/"})
      // }
      if(i==2)
      {
        this.$router.push({path:"/integrated-search"})
        // this.$router.push({path:"/"})
      }
      else if(i==3)
      {
        this.$router.push({path:"/advanced-search"})
      }
      this.page_index = i
    }
  },
}
</script>

<style>

.el-menu-vertical-demo {
  width: 200px;
  min-height: 800px;
  background-color: rgb(0, 0, 0);
}


</style>
