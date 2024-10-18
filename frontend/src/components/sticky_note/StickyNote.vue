<!-- StickyNote.vue -->
<template>
  <div class="message-board">
    <!-- Display All Notes -->
    <div v-for="note in sortedNotes" :key="note.id" class="message-card">
      <p class="message-content">{{ note.content }}</p>
      <p class="message-time">{{ formatTime(note.time) }}</p>
      
      <!-- Like Feature -->
      <div class="like-section">
        <button @click="likeNote(note.id)" class="btn btn-light">
          👍 {{ note.likes }} Likes
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
import { createNote, getAllNotes } from "@/services/noteboard/noteboardService";

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
      return [...(this.notes || [])].sort((a, b) => {
        if (b.likes === a.likes) {
          // If likes are equal, sort by time (newer first)
          return b.time - a.time;
        }
        // Sort by likes descending
        return b.likes - a.likes;
      });
    },
  },
  methods: {
    async fetchNotes() {
      try {
        const fetchedData = await getAllNotes();
        console.log("Fetched Data:", fetchedData); // Debugging line

        if (fetchedData && Array.isArray(fetchedData.notes)) {
          // Map the fetched notes to match the component's expected structure
          this.notes = fetchedData.notes.map(note => ({
            id: Date.now() + Math.random(), // Generate a unique ID
            content: note.content,
            time: new Date(note.time).getTime(), // Convert ISO string to timestamp
            likes: 0, // Initialize likes to 0 since backend doesn't provide it
          }));
        } else {
          console.error("Fetched data is not an array:", fetchedData);
          alert("獲取留言時發生錯誤。");
          this.notes = []; // Fallback to an empty array
        }
      } catch (error) {
        console.error("Failed to fetch notes:", error);
        alert("無法獲取留言。");
        this.notes = []; // Fallback to an empty array
      }
    },
    async submitNote() {
      if (!this.newNoteContent.trim()) {
        alert("請輸入留言內容");
        return;
      }
      
      // Create a new note object
      const newNote = {
        id: Date.now() + Math.random(), // Generate a more unique ID
        content: this.newNoteContent,
        time: Date.now(),               // Record current time as timestamp
        likes: 0,                       // Initial likes
      };
      
      try {
        // Persist the note to the backend
        const response = await createNote(newNote.content);
        
        console.log("Create Note Response:", response); // Debugging line
        
        // Adjust the condition based on the actual response structure
        // Assuming response.status is case-insensitive "success"
        if (response.status && response.status.toLowerCase() === "note added successfully") {
          // Optionally, you can fetch the newly created note's ID from response.uuid
          newNote.id = response.uuid || newNote.id; // Update ID if backend provides one
          
          // Update the local notes array for immediate feedback
          this.notes.unshift(newNote);
          
          // Clear the textarea
          this.newNoteContent = '';
          
          // Close the Bootstrap modal
          this.closeModal();
        } else {
          throw new Error("Backend responded with an error.");
        }
        
      } catch (error) {
        console.error("Failed to add note:", error);
        alert(error.message || "新增留言失敗");
      }
    },
    likeNote(noteId) {
      // Find the corresponding note and increment likes
      const note = this.notes.find((n) => n.id === noteId);
      if (note) {
        note.likes += 1;
        // Optionally, persist the like to the backend here
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
