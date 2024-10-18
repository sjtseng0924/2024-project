<template>
    <div class="login-wrapper">
      <div class="login-container">
        <h2>梅竹小天地</h2>
        <form @submit.prevent="handleLogin">
          <input
            v-model="username"
            type="text"
            placeholder="使用者名稱"
            class="input-field"
            required
          />
          <button type="submit" class="login-button">登入</button>
        </form>
      </div>
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
              alert("歡迎回到梅竹小天地！");
            } else {
              alert("歡迎加入梅竹小天地！");
            }
            // Set userName in localStorage
            localStorage.setItem("userName", this.username);
            // Redirect to chatapp
            this.$router.push("/chatapp");
          } catch (error) {
            alert(error.message || "Login failed.");
          }
        } else {
          alert("請輸入使用者名稱！");
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Full-height wrapper to center the login container */
  .login-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100vw;
    margin: 0;
    background-color: #e0e0e0;
  }
  
  /* Styling for login container */
  .login-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 300px;
    padding: 20px;
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
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border-radius: 5px;
    border: 1px solid #ccc;
  }
  
  .login-button {
    width: 100%;
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
  