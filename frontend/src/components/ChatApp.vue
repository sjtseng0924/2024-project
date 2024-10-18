<template>
  <div class="chat-app container mt-5" :class="{ 'center-room': !inRoom }">
    <div v-if="!inRoom" class="room-container d-flex justify-content-center align-items-center">
      <div class="w-100 text-center">
        <h2 class="mb-4">聊天室</h2>

        <!-- Main Chatroom and Dropdown Section -->
        <div class="row justify-content-center mb-4">
          <div class="col-12 col-md-6 mb-3">
            <button class="btn btn-dark w-75" @click="roomName = '歡樂聊天室'; joinRoom()">歡樂聊天室</button>
          </div>

          <div class="col-12 col-md-6 mb-3">
            <div class="input-group">
              <select v-model="selectedRoom" class="form-select">
                <option disabled value="">選擇企業聊天室</option>
                <option value="恩智浦半導體">恩智浦半導體</option>
                <option value="LINE台灣">LINE台灣</option>
                <option value="Google">Google</option>
                <option value="台積電">台積電</option>
                <option value="羅技">羅技</option>
                <option value="中華電信">中華電信</option>
                <option value="創客交流組">創客交流組</option>
              </select>
              <button class="btn btn-secondary" @click="confirmRoomSelection">確認</button>
            </div>
          </div>
        </div>

        <!-- Custom Room Creation Section -->
        <div class="custom-room mt-4">
          <h4>私人聊天室</h4>
          <div class="d-flex justify-content-center mt-3">
            <div class="input-group custom-input-group">
              <input v-model="roomName" type="text" class="form-control" placeholder="聊天室名稱" />
              <button class="btn btn-secondary" @click="joinRoom">加入</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-else>
      <div class="card">
        <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center">
          <h5>{{ roomName }}</h5>
          <button class="btn btn-outline-light" @click="handleRoomExit">離開</button>
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
  max-width: 900px; /* 保持最大寬度 */
  margin: auto;
}

.center-room {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
}

.room-container {
  /* 使用 Flexbox 來置中內容 */
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.w-100 {
  max-width: 600px; /* 限制內容的最大寬度 */
  margin: auto;
}

button {
  cursor: pointer;
}

.custom-room h4 {
  font-size: 1.3rem;
}

.card-header h5 {
  margin: 0;
}

/* 確保 input-group 元素保持在同一行 */
.input-group {
  display: flex;
  flex-wrap: nowrap;
}

/* 調整主聊天室下拉選單和按鈕 */
.input-group .form-select {
  flex: 2 1 auto;
  min-width: 200px; /* 設置最小寬度以防止過窄 */
}

.input-group .btn {
  flex: 0 0 auto;
  width: 100px; /* 設置固定寬度 */
}

/* 調整自定義房間創建部分的輸入框和按鈕 */
.custom-input-group {
  max-width: 350px; /* 控制整個 input-group 的最大寬度 */
}

.custom-input-group .form-control {
  flex: 1 1 auto;
  max-width: 250px; /* 設置輸入框的最大寬度 */
}

.custom-input-group .btn {
  flex: 0 0 auto;
  width: 100px; /* 設置固定寬度 */
}

/* 調整按鈕大小和間距以保持一致 */
.btn-secondary {
  background-color: #6c757d;
  border-color: #6c757d;
}

.btn-secondary:hover {
  background-color: #5a6268;
  border-color: #545b62;
}

/* 響應式調整 */
@media (max-width: 768px) {
  .input-group {
    flex-direction: column;
  }

  .input-group .form-select,
  .input-group .form-control {
    width: 100%;
    flex: none;
  }

  .input-group .btn,
  .custom-room .btn {
    margin-top: 10px;
    width: 100%;
  }

  .custom-room .btn {
    width: 100%;
    margin-top: 10px;
  }

  .custom-input-group {
    flex-direction: column;
    align-items: center;
    max-width: 100%; /* 允許在小屏幕上擴展 */
  }

  .custom-input-group .form-control,
  .custom-input-group .btn {
    width: 100%;
    margin-top: 10px;
  }
}
</style>
