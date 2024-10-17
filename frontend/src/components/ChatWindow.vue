<template>
    <div class="chat-window">
      <div class="messages" ref="messagesContainer">
        <Message
          v-for="message in messages"
          :key="message.time"
          :message="message"
          :isOwnMessage="message.sender_name === userName"
        />
      </div>
      <div class="message-input">
        <input
          v-model="newMessage"
          @keyup.enter="send"
          placeholder="Type your message..."
        />
        <button @click="send" :disabled="sending">Send</button>
      </div>
      <div class="chat-footer">
        <button @click="leaveRoom" class="leave-btn">Leave Room</button>
      </div>
    </div>
  </template>
  
  <script>
  import { getAllMessages, sendMessage } from '@/services/chatroomService';
  import Message from './ChatMessage.vue';
  
  export default {
    components: {
      Message,
    },
    props: {
      userName: String,
      roomName: String,
    },
    data() {
      return {
        messages: [],
        newMessage: '',
        sending: false, 
        intervalId: null,
      };
    },
    methods: {
      async fetchMessages() {
        try {
          this.messages = await getAllMessages(this.roomName);
          this.$nextTick(() => {
            this.scrollToBottom();
          });
        } catch (error) {
          console.error(error);
        }
      },
      async send() {
        if (!this.newMessage.trim() || this.sending) {
          return;
        }
        this.sending = true;
        try {
          await sendMessage(this.roomName, this.userName, this.newMessage);
          this.newMessage = '';
          this.fetchMessages();
        } catch (error) {
          console.error(error);
        } finally {
          this.sending = false; 
        }
      },
      scrollToBottom() {
        const container = this.$refs.messagesContainer;
        container.scrollTop = container.scrollHeight;
      },
      leaveRoom() {
        localStorage.removeItem('roomName');
        this.$emit('left-room');
      },
    },
    mounted() {
      this.fetchMessages();
      this.intervalId = setInterval(this.fetchMessages, 3000); // Poll every 3 seconds
    },
    beforeUnmount() {
      clearInterval(this.intervalId);
    },
  };
  </script>
  
  <style scoped>
  .chat-window {
    display: flex;
    flex-direction: column;
    height: 80vh;
    width: 100%;
    max-width: 600px;
    margin: 0 auto;
    border-radius: 8px;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    background-color: #ffffff;
  }
  
  .messages {
    flex: 1;
    overflow-y: auto;
    padding: 15px;
    background-color: #f9f9f9;
  }
  
  .message-input {
    display: flex;
    align-items: center;
    padding: 15px;
    background-color: #f3f4f6;
    border-top: 1px solid #e0e0e0;
  }
  
  .message-input input {
    flex: 1;
    padding: 12px;
    margin-right: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 14px;
  }
  
  .message-input button {
    padding: 12px 20px;
    background-color: #2e3b4e;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    font-size: 14px;
    transition: background-color 0.3s;
  }
  
  .message-input button:disabled {
    background-color: #999;
    cursor: not-allowed;
  }
  
  .message-input button:hover:enabled {
    background-color: #40577c;
  }
  
  .chat-footer {
    padding: 15px;
    background-color: #f3f4f6;
    border-top: 1px solid #e0e0e0;
    text-align: center;
  }
  
  .leave-btn {
    padding: 10px 20px;
    background-color: #e74c3c;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 14px;
    font-weight: bold;
    transition: background-color 0.3s;
  }
  
  .leave-btn:hover {
    background-color: #c0392b;
  }
  </style>
  