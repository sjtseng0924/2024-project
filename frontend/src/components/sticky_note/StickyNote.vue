<template>
  <div class="message-board">
    <!-- 顯示所有留言 -->
    <div v-for="(note, index) in sortedNotes" :key="index" class="message-card">
      <p class="message-content">{{ note.content }} </p>
      <p class="message-time">{{ formatTime(note.time) }}</p>
      
      <!-- 按讚功能 -->
      <div class="like-section">
        <button @click="likeNote(note.note_id)">👍 {{ note.likes }} Likes</button>
      </div>
    </div>
    
    <!-- 右下角圓形加號按鈕 -->
    <button class="add-note-button" @click="showModal = true">+</button>
    
    <!-- 模態視窗 (Modal) -->
    <div v-if="showModal" class="modal-overlay">
      <div class="modal">
        <textarea v-model="newNoteContent" placeholder="輸入留言內容"></textarea>
        <button @click="submitNote">新增</button>
        <button @click="showModal = false">取消</button>
      </div>
    </div>
  </div>
</template>

<script>
import { createNote, getAllNotes, updateLikes } from "@/services/noteboard/noteboardService";

export default {
  data() {
    return {
      notes: [
      ],              // 從後端獲取的留言
      showModal: false,        // 控制模態視窗顯示與否
      newNoteContent: '',      // 新留言的內容
    };
  },
  computed: {
    sortedNotes() {
      return [...this.notes].sort((a, b) => {
        if (b.likes === a.likes) {
          // 如果按讚數一樣，按照時間排序，新的在上
          return new Date(b.time).getTime() - new Date(a.time).getTime();
        }
        // 按讚數由高到低排序
        return b.likes - a.likes;
      });
    },
  },
  methods: {
    async fetchNotes() {
      try {
        const response = await getAllNotes();
        this.notes = response.notes;  // 從後端取得所有便條
      } catch (error) {
        console.error(error);
      }
    },
    async submitNote() {
      if (!this.newNoteContent.trim()) {
        alert("請輸入留言內容");
        return;
      }
      const newNote = {
        content: this.newNoteContent,
      };
      try {
        // 發送到後端新增留言
        await createNote(newNote.content);
        this.newNoteContent = ''; 
        this.showModal = false;   
        this.fetchNotes();      
      } catch (error) {
        alert(error.message || "新增留言失敗");
      }
    },
    async likeNote(noteId) {
      // 找到對應的留言並增加讚數
      const note = this.notes.find((n) => n.note_id === noteId);
      if (note) {
        note.likes += 1;
        try {
          // 發送請求到後端更新按讚數
          await updateLikes(noteId, note.likes);
        } catch (error) {
          console.error("更新按讚數失敗", error);
        }
      }
    },
    formatTime(timestamp) {
      const date = new Date(timestamp);
      return date.toLocaleString();
    },
  },
  mounted() {
    this.fetchNotes();
  },
};
</script>

<style scoped>
/* 留言板容器 */
.message-board {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 5% 3% 3% 5%;
  gap: 1.5vw;
}

/* 留言卡片 */
.message-card {
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  width: 90vw;   /* 固定寬度 */
  max-width: 500px;
  padding: 1.5vw;
  border-radius: 10px; /* 圓角 */
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  word-wrap: break-word;  /* 讓內容自動換行 */
}

/* 留言內容 */
.message-content {
  font-size: 1.1em;
  margin-bottom: 10px;
}

/* 留言時間 */
.message-time {
  font-size: 0.9em;
  color: #888;
  text-align: right;
}

/* 按讚區塊 */
.like-section {
  margin-top: 10px;
  text-align: right;
}

/* 按讚按鈕 */
.like-section button {
  background-color: transparent;
  border: none;
  color: #f39c12;
  font-size: 1.1em;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
}

.like-section button:hover {
  color: #e67e22;
}

/* 新增留言按鈕 */
.add-note-button {
  position: fixed;
  bottom: 2vw;
  right: 2vw;
  background-color: #f39c12;
  border: none;
  color: white;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  font-size: 24px;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

/* 模態視窗背景 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

/* 模態視窗 */
.modal {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  width: 300px;
  text-align: center;
}

textarea {
  width: 100%;
  height: 100px;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}
</style>
