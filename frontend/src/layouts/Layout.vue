<script setup>
import {
  User,
  Menu as IconMenu,
  House,
  Setting,
} from '@element-plus/icons-vue'

import router from "@/router/index.js";

const logout=() => {
  router.push('/login')
}
</script>

<template>
  <div>
    <el-container style="min-height: 100vh">
      <el-header style="display: flex; align-items: center; border-bottom: 1px solid #eee ; background-color: #ffffff">
        <div style="flex:1;display: flex ;align-items: center; font-size: 24px; font-weight: bold">
          <img style="width: 40px" src="@/assets/imgs/logo.png">
          <div style="margin-left: 10px"></div>
        </div>
        <div>
            <el-dropdown>
              <!--头像-->
              <div>
                <img src="@/assets/imgs/管理员.jpg" alt="" style="width: 90px; border-radius: 50%">
                <div>管理员</div>
              </div>
              <template #dropdown>
              <!--下拉菜单-->
                <el-dropdown-menu>
                  <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
                </el-dropdown-menu>
              </template>
            </el-dropdown>
        </div>
      </el-header>

      <el-container>
        <el-aside width="220px">
          <el-menu router style="height: 100vh" default-active="/home">
            <el-menu-item index="/manager/home">
              <el-icon>
                <icon-menu/>
              </el-icon>
              <span>系统首页</span>
            </el-menu-item>
            <el-menu-item index="/manager/lab">
              <el-icon>
                <House/>
              </el-icon>
              <span>lab</span>
            </el-menu-item>
            <el-menu-item index="/manager/User">
              <el-icon>
                <User/>
              </el-icon>
              <span>User</span>
            </el-menu-item>
            <el-menu-item index="/manager/device">
              <el-icon>
                <Setting/>
              </el-icon>
              <span>device</span>
            </el-menu-item>
          </el-menu>
        </el-aside>
        <el-main>
          <router-view/>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
