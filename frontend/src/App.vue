<!-- App.vue -->
<template>
  <div>
    <!-- Navbar Component -->
    <AppNavbar :isLoggedIn="isLoggedIn" :userName="userName" @logout="handleLogout" />

    <!-- Main Content -->
    <router-view></router-view>
  </div>
</template>

<script>
import AppNavbar from './components/AppNavbar.vue'; // Updated import path and name

export default {
  name: 'App',
  components: {
    AppNavbar, // Updated component registration
  },
  data() {
    return {
      isLoggedIn: !!localStorage.getItem('userName'),
      userName: localStorage.getItem('userName') || '',
    };
  },
  methods: {
    handleLogout() {
      localStorage.removeItem('userName');
      this.isLoggedIn = false;
      this.userName = '';
      this.$router.push('/login');
    },
    checkLoginStatus() {
      this.isLoggedIn = !!localStorage.getItem('userName');
      this.userName = localStorage.getItem('userName') || '';
    },
  },
  watch: {
    // Watch for route changes to update login status
    '$route'() {
      this.checkLoginStatus();
    },
  },
  mounted() {
    // Update state if localStorage changes from other tabs/windows
    window.addEventListener('storage', () => {
      this.checkLoginStatus();
    });
  },
};
</script>

<style>
/* Global styles if needed */
</style>
