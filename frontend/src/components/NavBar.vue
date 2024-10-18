<template>
  <div>
    <!-- Navbar -->
    <nav class="bg-gray-900 text-gray-300 p-4 flex justify-between items-center">
      <!-- Title on the left -->
      <div class="text-lg font-bold text-white">
        WebSiteName
      </div>

      <!-- Center links -->
      <div class="flex space-x-6">
        <router-link to="/chatapp" class="hover:text-white" v-if="isLoggedIn">Chat App</router-link>
        <router-link to="/sticky_note" class="hover:text-white" v-if="isLoggedIn">Note Board</router-link>
        <router-link to="/map" class="hover:text-white" v-if="isLoggedIn">Map</router-link>
      </div>

      <!-- Login or Username on the right -->
      <div class="flex items-center space-x-4">
        <button v-if="!isLoggedIn" @click="login" class="flex items-center space-x-1 hover:text-white">
          <span>&#128274;</span> <span>Login</span>
        </button>
        <span v-else class="flex items-center space-x-1 text-white">
          <span>{{ username }}</span>
        </span>
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
  data() {
    return {
      isLoggedIn: false,
      username: '',
      currentPage: 'LoginComponent',
    };
  },
  methods: {
    login() {
      // Simulate login process
      this.isLoggedIn = true;
      this.username = 'JohnDoe'; // Replace with actual username logic
      this.currentPage = 'HomeComponent'; // Switch to home page after login
    },
  },
  components: {
    LoginComponent: {
      template: `<div>Please login to access the website.</div>`,
    },
    HomeComponent: {
      template: `<div>Welcome to the Home Page!</div>`,
    },
    Page1Component: {
      template: `<div>Page 1 Content</div>`,
    },
    Page2Component: {
      template: `<div>Page 2 Content</div>`,
    },
  },
};
</script>

<style scoped>
/* Navbar Styles to match your image */
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
</style>
