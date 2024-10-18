<template>
  <div>
    <!-- Navbar -->
    <nav class="bg-gray-900 text-gray-300 p-4 flex justify-between items-center">
      <!-- Title on the left -->
      <div class="text-lg font-bold text-white">
        WebSiteName
      </div>

      <!-- Center links, hide on mobile if not logged in -->
      <div class="hidden md:flex space-x-6" v-if="isLoggedIn">
        <router-link to="/chatapp" class="hover:text-white">Chat App</router-link>
        <router-link to="/sticky_note" class="hover:text-white">Note Board</router-link>
        <router-link to="/map" class="hover:text-white">Map</router-link>
      </div>

      <!-- Login/Username/Logout on the right -->
      <div class="flex items-center space-x-4">
        <button v-if="!isLoggedIn" @click="login" class="flex items-center space-x-1 hover:text-white">
          <!-- <span>&#128274;</span> <span>Login</span> -->
        </button>
        <div v-else class="flex items-center space-x-4">
          <span class="flex items-center space-x-1 text-white">
            <span>{{ username }}</span>
          </span>
          <button @click="logout" class="hover:text-white">
            Logout
          </button>
        </div>
      </div>
    </nav>

    <!-- Main content -->
    <div class="p-4 text-white">
      <component :is="currentPage"></component>
    </div>
  </div>
</template>

<script>
export default {
  props: ['isLoggedIn', 'userName'],
  data() {
    return {
      currentPage: 'LoginComponent',
      // localUserName: this.userName, // Create a local variable for username
      // isRegistered: this.isLoggedIn,
    };
  },
  methods: {
    // login() {
    //   // 模擬登入過程
    //   this.isLoggedIn = true;
    //   this.username = 'JohnDoe'; // 替換為真實的登入邏輯
    //   this.currentPage = 'HomeComponent'; // 登入後顯示首頁
    // },
    logout() {
      this.$emit('logout'); // 触发登出事件
    },
  },
  watch: {
    isLoggedIn(newVal) {
      // 當未登入時自動跳轉到 /chatapp 頁面
      if (!newVal) {
        this.$router.push('/chatapp');

      }
    },
    
  },
  mounted() {
    if (!this.username) {
      this.$router.push('/chatapp'); // 頁面載入時檢查登入狀態
    }
  },
  components: {
  },
};
</script>

<style scoped>
/* Navbar Styles */
nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #1f1f1f;
  padding: 1rem;
  color: #b0b0b0;
}

nav .text-white {
  color: #b0b0b0;
}

nav a {
  text-decoration: none;
  color: inherit;
  font-size: 16px;
}

nav a:hover {
  color: white;
}

button {
  background: none;
  border: none;
  color: inherit;
  cursor: pointer;
}

button:hover {
  color: white;
}

nav .flex {
  display: flex;
}

nav .space-x-6 > * + * {
  margin-left: 1.5rem; /* Adds space between center links */
}

nav .space-x-4 > * + * {
  margin-left: 1rem; /* Adds space between login buttons */
}

/* Mobile styles: Stack items vertically and hide center links */
@media (max-width: 768px) {
  nav {
    flex-direction: column;
    align-items: flex-start;
  }

  .space-x-6 {
    flex-direction: column;
    margin-top: 1rem;
  }

  .space-x-6 > * + * {
    margin-left: 0; /* Remove horizontal spacing */
    margin-top: 1rem; /* Add vertical spacing */
  }
}
</style>
