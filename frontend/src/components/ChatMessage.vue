<template>
  <div :class="['message', isOwnMessage ? 'own' : '']">
    <div class="message-info">
      <span class="sender">{{ message.sender_name }}</span>
      <span class="time">{{ formattedTime }}</span>
    </div>
    <div class="message-content">{{ message.content }}</div>
  </div>
</template>

<script>
export default {
  name: "ChatMessage", // Change to a multi-word name
  props: {
    message: Object,
    isOwnMessage: Boolean,
  },
  computed: {
    formattedTime() {
      const date = new Date(this.message.time);
      return date.toLocaleTimeString();
    },
  },
};
</script>

<style scoped>
.message {
  margin-bottom: 15px;
  padding: 10px;
  border-radius: 5px;
  max-width: 70%;
}
.message.own {
  background-color: #d1ffd6;
  margin-left: auto;
}
.message:not(.own) {
  background-color: #fff;
}
.message-info {
  display: flex;
  justify-content: space-between;
  margin-bottom: 5px;
}
.sender {
  font-weight: bold;
}
.time {
  font-size: 0.8em;
  color: #666;
}
.message-content {
  word-wrap: break-word;
}
</style>
