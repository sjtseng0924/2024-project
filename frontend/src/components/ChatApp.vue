<template>
  <div class="chat-app container mt-5" :class="{ 'center-room': !inRoom }">
    <div v-if="!inRoom" class="room-container d-flex justify-content-center align-items-center">
      <div class="w-100 text-center">
        <h2 class="mb-4">聊天室</h2>

        <!-- Main Chatroom and Dropdown Section -->
        <div class="row justify-content-center mb-4">
          <div class="col-12 col-md-6 mb-3">
            <button
              class="btn btn-dark btn-sm w-100"
              @click="roomName = '歡樂聊天室'; joinRoom()"
            >
              歡樂聊天室
            </button>
          </div>

          <div class="col-12 col-md-6 mb-3">
            <div class="input-group input-group-sm justify-content-center">
              <select v-model="selectedRoom" class="form-select form-select-sm">
                <option disabled value="">選擇企業聊天室</option>
                <option value="恩智浦半導體">恩智浦半導體</option>
                <option value="LINE台灣">LINE台灣</option>
                <option value="Google">Google</option>
                <option value="台積電">台積電</option>
                <option value="羅技">羅技</option>
                <option value="中華電信">中華電信</option>
                <option value="創客交流組">創客交流組</option>
              </select>
              <button
                class="btn btn-secondary btn-sm"
                @click="confirmRoomSelection"
              >
                確認
              </button>
            </div>
          </div>
        </div>

        <!-- Custom Room Creation Section -->
        <div class="custom-room mt-4">
          <h4 class="mb-3">私人聊天室</h4>
          <div class="d-flex justify-content-center">
            <div class="input-group input-group-sm custom-input-group">
              <input
                v-model="roomName"
                type="text"
                class="form-control form-control-sm"
                placeholder="聊天室名稱"
              />
              <button class="btn btn-secondary btn-sm" @click="joinRoom">加入</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-else>
      <div class="card">
        <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center">
          <h5 class="mb-0">{{ roomName }}</h5>
          <button class="btn btn-outline-light btn-sm" @click="handleRoomExit">離開</button>
        </div>
        <div class="card-body p-0">
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
      selectedRoom: "",
      inRoom: false,
    };
  },
  methods: {
    async joinRoom() {
      if (!this.roomName.trim()) {
        alert("Please select or enter a room name.");
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
    confirmRoomSelection() {
      if (!this.selectedRoom) {
        alert("Please select a room from the dropdown.");
        return;
      }
      this.roomName = this.selectedRoom;
      this.joinRoom();
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
.chat-app {
  max-width: 900px; /* Maintains maximum width */
  margin: auto;
  padding: 15px; /* Added padding for better spacing on mobile */
}

.center-room {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
}

.room-container {
  /* Flexbox centering */
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.w-100 {
  max-width: 600px; /* Limits content width */
  margin: auto;
}

button {
  cursor: pointer;
}

.custom-room h4 {
  font-size: 1.1rem;
}

.card-header h5 {
  margin: 0;
}

/* Ensure input-group elements stay in the same line */
.input-group {
  display: flex;
  flex-wrap: nowrap;
}

/* Adjust main chatroom dropdown and button */
.input-group .form-select {
  flex: 2 1 auto;
  min-width: 150px; /* Prevents from being too narrow */
}

.input-group .btn {
  flex: 0 0 auto;
  width: 80px; /* Reduced width for buttons */
}

/* Adjust custom room creation input and button */
.custom-input-group {
  max-width: 300px; /* Controls the max width of input-group */
}

.custom-input-group .form-control {
  flex: 1 1 auto;
  max-width: 200px; /* Sets max width for input */
}

.custom-input-group .btn {
  flex: 0 0 auto;
  width: 80px; /* Reduced width for button */
}

/* Consistent button styling */
.btn-secondary {
  background-color: #6c757d;
  border-color: #6c757d;
}

.btn-secondary:hover {
  background-color: #5a6268;
  border-color: #545b62;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .input-group {
    flex-wrap: nowrap; /* Prevent wrapping */
    justify-content: center; /* Center the input-group */
  }

  .custom-input-group {
    flex-wrap: nowrap;
    max-width: 100%;
    justify-content: center; /* Center the custom-input-group */
  }

  /* Adjust heading sizes for better readability */
  h2 {
    font-size: 1.3rem;
  }

  h4 {
    font-size: 1rem;
  }

  /* Adjust button sizes */
  .btn {
    padding: 0.25rem 0.5rem;
    font-size: 0.875rem;
  }

  /* Adjust card header for better spacing */
  .card-header {
    padding: 0.5rem 0.75rem;
  }

  .card-body {
    padding: 0.5rem;
  }

  /* Center input-group and custom-input-group */
  .input-group,
  .custom-input-group {
    margin: 0 auto; /* Center horizontally */
  }
}
</style>
