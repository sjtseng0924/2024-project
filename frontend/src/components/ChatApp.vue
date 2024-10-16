<template>
  <div class="chat-app">
    <nav class="navbar">
      <h1 v-if="inRoom">Room: {{ roomName }}</h1>
      <h1 v-else>Chat Application</h1>
      <div v-if="isRegistered" class="navbar-right">
        <p>Logged in as: <strong>{{ userName }}</strong></p>
        <button @click="logout">Logout</button>
      </div>
    </nav>

    <div v-if="!isRegistered" class="register-container">
      <h2>Login</h2>
      <input v-model="userName" placeholder="Enter your name" />
      <button @click="login">Login</button>
    </div>

    <div v-else>
      <div v-if="!inRoom" class="room-container">
        <h2>Select or Create a Room</h2>
        <input v-model="roomName" placeholder="Enter room name" />
        <button @click="joinRoom">Join Room</button>
      </div>

      <div v-else>
        <ChatWindow 
          :userName="userName" 
          :roomName="roomName" 
          @left-room="handleRoomExit" 
        />
      </div>
    </div>
  </div>
</template>

<script>
import { loginUser, createChatRoom } from "@/services/chatroomService";
import ChatWindow from "./ChatWindow.vue";

export default {
  components: {
    ChatWindow,
  },
  data() {
    return {
      userName: "",
      roomName: "",
      isRegistered: false,
      inRoom: false,
    };
  },
  methods: {
    async login() {
      if (!this.userName.trim()) {
        alert("Please enter a username.");
        return;
      }
      try {
        const result = await loginUser(this.userName);
        if (result.status === "User already exists") {
          alert("Welcome back! Logging in...");
        } else {
          alert("User created successfully!");
        }
        this.isRegistered = true;
        localStorage.setItem("userName", this.userName);
      } catch (error) {
        alert(error.message || "Login failed.");
      }
    },
    async joinRoom() {
      if (!this.roomName.trim()) {
        alert("Please enter a room name.");
        return;
      }
      try {
        await createChatRoom(this.roomName);
        this.inRoom = true;
        localStorage.setItem("roomName", this.roomName);
      } catch (error) {
        alert(error.message || "Failed to join or create room.");
      }
    },
    handleRoomExit() {
      this.roomName = "";
      this.inRoom = false;
      localStorage.removeItem("roomName");
    },
    logout() {
      this.userName = "";
      this.roomName = "";
      this.isRegistered = false;
      this.inRoom = false;
      localStorage.removeItem("userName");
      localStorage.removeItem("roomName");
    },
  },
  mounted() {
    const savedUserName = localStorage.getItem("userName");
    const savedRoomName = localStorage.getItem("roomName");
    if (savedUserName) {
      this.userName = savedUserName;
      this.isRegistered = true;
    }
    if (savedRoomName) {
      this.roomName = savedRoomName;
      this.inRoom = true;
    }
  },
};
</script>

<style scoped>
body {
  background-color: #f3f4f6;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 0;
  padding: 0;
}

.navbar {
  background-color: #333;
  color: white;
  padding: 15px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.navbar h1 {
  margin: 0;
  font-size: 22px;
  font-weight: 600;
  color: #f3f4f6;
}

.navbar-right {
  display: flex;
  align-items: center;
}

.navbar-right p {
  margin: 0 15px 0 0;
  font-size: 14px;
}

.navbar-right button {
  padding: 8px 15px;
  background-color: #f3f4f6;
  color: #333;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.navbar-right button:hover {
  background-color: #ddd;
}

.chat-app {
  max-width: 650px;
  margin: 30px auto;
  text-align: center;
  padding: 20px;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
}

.register-container, .room-container {
  margin-top: 30px;
  color: #555;
}

.register-container h2, .room-container h2 {
  margin-bottom: 20px;
  color: #333;
  font-size: 20px;
  font-weight: 600;
}

input {
  padding: 12px;
  width: 80%;
  margin-bottom: 15px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
}

button {
  padding: 12px 20px;
  background-color: #333;
  color: #f3f4f6;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s;
  font-size: 14px;
}

button:hover {
  background-color: #555;
}

.room-header {
  margin: 20px 0;
  font-size: 22px;
  color: #333;
  font-weight: bold;
}
</style>
