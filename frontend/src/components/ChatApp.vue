<template>
  <div class="chat-app container mt-5" :class="{ 'center-room': !inRoom }">
    <div v-if="!inRoom" class="text-center">
      <h2>Select or Create a Room</h2>
      <div class="input-group mb-3 mt-4">
        <input v-model="roomName" type="text" class="form-control" placeholder="Enter room name" aria-label="Room Name" />
        <button class="btn btn-dark" @click="joinRoom">Join Room</button>
      </div>
    </div>

    <div v-else>
      <div class="card">
        <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center">
          <h5>Room: {{ roomName }}</h5>
          <button class="btn btn-outline-light" @click="handleRoomExit">Exit Room</button>
        </div>
        <div class="card-body">
          <ChatWindow
            :userName="userName"
            :roomName="roomName"
            @left-room="handleRoomExit"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { createChatRoom } from "@/services/chatroom/chatroomService";
import ChatWindow from "./ChatWindow.vue";

export default {
  name: "ChatApp",
  components: {
    ChatWindow,
  },
  data() {
    return {
      userName: localStorage.getItem("userName") || "",
      roomName: "",
      inRoom: false,
    };
  },
  methods: {
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
      localStorage.removeItem("userName");
      localStorage.removeItem("roomName");
      this.$router.push("/login");
    },
  },
  mounted() {
    const savedRoomName = localStorage.getItem("roomName");
    if (savedRoomName) {
      this.roomName = savedRoomName;
      this.inRoom = true;
    }
  },
};
</script>

<style scoped>
/* Adjust layout to center the room selection when not in a room */
.chat-app {
  max-width: 600px;
  margin: auto;
}

.center-room {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
}

.card-header h5 {
  margin: 0;
}

.input-group {
  max-width: 400px;
  margin: auto;
}

button {
  cursor: pointer;
}
</style>
