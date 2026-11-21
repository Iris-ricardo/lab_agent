<script setup>
import {reactive,ref} from "vue";
import {ElMessage} from "element-plus";
import router from "@/router/index.js";
import {User} from "@element-plus/icons-vue";

const form = reactive({
      Username: '',
      Password: ''
    })
const loadingValue = ref(false);

const login = () => {
  loadingValue.value = true;
  setTimeout(()=>{
    loadingValue.value = false;
    ElMessage.success('登陆成功')
    router.push('/manager/home')
  },2000)
}

</script>

<template>
  <div class="login-container">
    <div class="login-box">
      <h1 class="login-title">实验室预约系统</h1>
      <div class="login-title-second">基于Agent智能预约系统</div>
       <el-form :model="form" label-width="auto" style="max-width: 600px">
          <!--账号输入-->
          <el-form-item >
             <el-input
                 size="large"
                 v-model="form.Username"
                 placeholder="请输入账号"
                 :prefix-icon="User" />
          </el-form-item>
          <!--密码输入-->
          <el-form-item >
              <el-input type="password"
                        show-password
                        v-model="form.Password"
                        placeholder="请输入密码"
                        :prefix-icon="Lock" />
          </el-form-item>
         <div>
           <el-button round type="primary"  style="width: 100%" @click="login" :loading="loadingValue">登陆</el-button>
           <div style="text-align: right; margin-top: 10px">还没有账号？请<a style="color: var(--el-color-primary)" href="/register">注册</a></div>
         </div>
       </el-form>
    </div>
  </div>
</template>

<style scoped>

.login-container{
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center
}

.login-box{
  width: 390px;
  border-radius: 8px;
  box-shadow: 0 8px 12px rgba(0,0,0,0.1);
  padding: 20px;
  text-align: center;
  background: white;
}

.login-title{
  text-align: center; font-size: 28px
}

.login-title-second{
  text-align: center;
  margin-top: 5px;
  margin-bottom: 30px;
  font-size: 15px
}
</style>
