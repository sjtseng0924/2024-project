<template>
  <div id="app">
    <Navbar :isLoggedIn="isRegistered" :username="userName" @logout="handleLogout" />
    <router-view :isLoggedIn="isRegistered" :userName="userName" @login="handleLogin" class="pb-[75px]"/>
  </div>
</template>

<script>
import Navbar from '@/components/NavBar.vue'
export default {
  components: {
    Navbar,
  },
  data() {
    return {
      userName: "",
      isRegistered: false,
    };
  },
  methods: {
    handleLogin(username) {
      this.userName = username;
      this.isRegistered = true; // 更新为已登录
      localStorage.setItem("userName", this.userName);
    },
    handleLogout() {
      this.userName = "";
      this.isRegistered = false; // 更新为未登录
    }
  },
  mounted() {
    const savedUserName = localStorage.getItem("userName");
    if (savedUserName) {
      this.userName  = savedUserName;
      this.isRegistered = true;
    }
    
  },
};
</script>

<style>
body {
  margin: 0;
  font-family: 'Arial', sans-serif;
}
#app {
  height: 90vh;
}
</style>
