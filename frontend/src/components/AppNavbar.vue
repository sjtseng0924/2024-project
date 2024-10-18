<!-- AppNavbar.vue -->
<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark">
    <div class="container-fluid">
      <!-- Brand -->
      <router-link class="navbar-brand" to="/">梅竹小天地</router-link>

      <!-- Toggler/collapsible Button -->
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Navbar links -->
      <div class="collapse navbar-collapse" id="navbarNav">
        <!-- Center links -->
        <ul class="navbar-nav me-auto mb-2 mb-lg-0" v-if="isLoggedIn">
          <li class="nav-item">
            <router-link class="nav-link" to="/chatapp">聊天室</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/sticky_note">留言板</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/map">地圖與時程</router-link>
          </li>
        </ul>

        <!-- Right side -->
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
          <!-- Login button -->
          <li class="nav-item" v-if="!isLoggedIn">
            <router-link class="nav-link" to="/login">登入</router-link>
          </li>

          <!-- Username and Logout -->
          <li class="nav-item d-flex align-items-center" v-else>
            <span class="nav-link text-white">{{ userName }}</span>
            <button @click="logout" class="btn btn-outline-light ms-2">登出</button>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'AppNavbar',
  props: ['isLoggedIn', 'userName'],
  methods: {
    logout() {
      this.$emit('logout');
    },
  },
};
</script>

<style scoped>
/* Add any custom styles if needed */
</style>
