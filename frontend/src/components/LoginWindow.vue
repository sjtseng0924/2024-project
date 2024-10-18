<!-- LoginWindow.vue -->
<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <input
        v-model="username"
        type="text"
        placeholder="Enter your name"
        class="input-field"
        required
      />
      <button type="submit" class="login-button">Login</button>
    </form>
  </div>
</template>

<script>
import { loginUser } from "@/services/chatroom/chatroomService";

export default {
  name: "LoginWindow",
  data() {
    return {
      username: "",
    };
  },
  methods: {
    async handleLogin() {
      if (this.username.trim()) {
        try {
          const result = await loginUser(this.username);
          if (result.status === "User already exists") {
            alert("Welcome back! Logging in...");
          } else {
            alert("User created successfully!");
          }
          // Set userName in localStorage
          localStorage.setItem("userName", this.username);
          // Redirect to chatapp
          this.$router.push("/chatapp");
        } catch (error) {
          alert(error.message || "Login failed.");
        }
      } else {
        alert("Please enter a username.");
      }
    },
  },
};
</script>

<style scoped>
.login-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 300px;
  width: 300px;
  margin: 100px auto;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h2 {
  margin-bottom: 20px;
  font-size: 1.5em;
  color: #333;
}

.input-field {
  width: 90%;
  padding: 8px;
  margin-bottom: 15px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.login-button {
  width: 90%;
  padding: 10px;
  background-color: #333;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.login-button:hover {
  background-color: #444;
}
</style>
