<template>
  <div>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-md navbar-dark bg-dark">
      <div class="container-fluid">
        <!-- Brand -->
        <router-link class="navbar-brand" to="/">WebSiteName</router-link>

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
              <router-link class="nav-link" to="/chatapp">Chat App</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/sticky_note">Note Board</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/map">Map</router-link>
            </li>
          </ul>

          <!-- Right side -->
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <!-- Login button -->
            <li class="nav-item" v-if="!isLoggedIn">
              <button @click="login" class="btn btn-link nav-link">Login</button>
            </li>

            <!-- Username and Logout -->
            <li class="nav-item d-flex align-items-center" v-else>
              <span class="nav-link text-white">{{ userName }}</span>
              <button @click="logout" class="btn btn-outline-light ms-2">Logout</button>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Main content -->
    <div class="container mt-4">
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
    };
  },
  methods: {
    logout() {
      this.$emit('logout');
    },
    login() {
      // Implement your login logic here
    },
  },
  watch: {
    isLoggedIn(newVal) {
      if (!newVal) {
        this.$router.push('/chatapp');
      }
    },
  },
  mounted() {
    if (!this.userName) {
      this.$router.push('/chatapp');
    }
  },
};
</script>

<style scoped>
/* Custom styles if needed */
</style>
