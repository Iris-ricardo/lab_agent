<script setup>
import {reactive} from "vue";
import {User,Lock} from "@element-plus/icons-vue";
const form = reactive({
      Username: '',
      Password: '',
      PasswordConfirm: '',
    })
</script>

<template>
  <div class="login-register">
    <div class="register-box">
      <h1 class="register-title">欢迎注册预约系统</h1>
       <el-form :model="form" label-width="auto" style="max-width: 600px">
          <!--账号输入-->
          <el-form-item >
             <el-input
                 size="large"
                 v-model="form.Username"
                 placeholder="请输入账号"
                 prefix-icon="User" />
          </el-form-item>
          <!--密码输入-->
          <el-form-item >
              <el-input type="password"
                        show-password
                        v-model="form.Password"
                        placeholder="请输入密码"
                        :prefix-icon="Lock" />
          </el-form-item>
          <!--确认密码-->
         <el-form-item >
              <el-input type="password"
                        show-password
                        v-model="form.PasswordConfirm"
                        placeholder="请确认密码"
                        :prefix-icon="Lock" />
          </el-form-item>
         <div>
           <el-button round type="primary" style="width: 100%">登陆</el-button>
           <div style="text-align: right; margin-top: 10px">已有账号？请<a style="color: var(--el-color-primary)" href="/login">登陆</a></div>
         </div>
       </el-form>
    </div>
  </div>
</template>

<style scoped>

.login-register{
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center
}

.register-box{
  width: 390px;
  border-radius: 8px;
  box-shadow: 0 8px 12px rgba(0,0,0,0.1);
  padding: 20px;
  text-align: center;
  background: white;
}

.register-title{
  text-align: center; font-size: 28px
}

</style>
