<!-- StickyNote.vue -->
<template>
  <div class="message-board">
    <!-- Display All Notes -->
    <div v-for="note in sortedNotes" :key="note.note_id" class="message-card">
      <p class="message-content">{{ note.content }}</p>
      <p class="message-time">{{ formatTime(note.time) }}</p>
      
      <!-- Like Feature -->
      <div class="like-section">
        <button @click="likeNote(note.note_id)" class="btn btn-light">
          👍 {{ note.likes }} 個讚
        </button>
      </div>
    </div>
    
    <!-- Floating Add Note Button -->
    <button
      class="add-note-button btn btn-primary rounded-circle"
      data-bs-toggle="modal"
      data-bs-target="#addNoteModal"
    >
      +
    </button>
    
    <!-- Bootstrap Modal for Adding Notes -->
    <div
      class="modal fade"
      id="addNoteModal"
      tabindex="-1"
      aria-labelledby="addNoteModalLabel"
      aria-hidden="true"
      ref="addNoteModal"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <!-- Modal Header -->
          <div class="modal-header">
            <h5 class="modal-title" id="addNoteModalLabel">新增留言</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          
          <!-- Modal Body -->
          <div class="modal-body">
            <textarea
              v-model="newNoteContent"
              class="form-control"
              placeholder="輸入留言內容"
              rows="4"
            ></textarea>
          </div>
          
          <!-- Modal Footer -->
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              取消
            </button>
            <button
              type="button"
              class="btn btn-primary"
              @click="submitNote"
            >
              新增
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// Import Bootstrap's Modal JS
import { Modal } from 'bootstrap';
import { createNote, getAllNotes, updateLikes } from "@/services/noteboard/noteboardService";

export default {
  name: 'StickyNote',
  // Removed unused props to fix ESLint error
  // props: ['isLoggedIn', 'userName'],
  data() {
    return {
      notes: [], // Initialize as empty array
      newNoteContent: '', // Content of the new note
    };
  },
  computed: {
    sortedNotes() {
      return [...this.notes].sort((a, b) => {
        if (b.likes === a.likes) {
          return new Date(b.time).getTime() - new Date(a.time).getTime();
        }
        return b.likes - a.likes;
      });
    },
  },
  methods: {
    async fetchNotes() {
      try {
        const response = await getAllNotes();
        this.notes = response.notes;  
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
    closeModal() {
      // Get the modal element via ref
      const modalElement = this.$refs.addNoteModal;
      
      // Initialize a Bootstrap modal instance
      const modalInstance = Modal.getInstance(modalElement) || new Modal(modalElement);
      
      // Hide the modal
      modalInstance.hide();
    },
  },
  mounted() {
    // Authentication is handled via route guards; no need to check here
    this.fetchNotes();
  },
};
</script>

<style scoped>
/* Message Board Container */
.message-board {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 5% 3% 3% 5%;
  gap: 1.5vw;
}

/* Message Card */
.message-card {
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  width: 90vw;   /* Fixed width */
  max-width: 500px;
  padding: 1.5vw;
  border-radius: 10px; /* Rounded corners */
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  word-wrap: break-word;  /* Allow content to wrap */
}

/* Message Content */
.message-content {
  font-size: 1.1em;
  margin-bottom: 10px;
}

/* Message Time */
.message-time {
  font-size: 0.9em;
  color: #888;
  text-align: right;
}

/* Like Section */
.like-section {
  margin-top: 10px;
  text-align: right;
}

/* Like Button */
.like-section button {
  background-color: #f8f9fa; /* Light background */
  border: 1px solid #ced4da; /* Border similar to Bootstrap's input */
  color: #f39c12;
  font-size: 1.1em;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  padding: 0.375rem 0.75rem;
  border-radius: 0.25rem;
}

.like-section button:hover {
  background-color: #e2e6ea;
  color: #e67e22;
}

/* Add Note Button */
.add-note-button {
  position: fixed;
  bottom: 2vw;
  right: 2vw;
  /* background-color: #f39c12; */ /* Already using btn-primary */
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
</style>