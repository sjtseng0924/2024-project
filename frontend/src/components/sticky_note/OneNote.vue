<template>
    <div
      class="note"
      :style="noteStyle" 
    >
      <p>{{ content }}</p>
      <button class="like-button" @click="likeNote" >:thumbsup: {{ likes }}</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      content: String,
      likes: Number,
    },
    computed: {
      noteStyle() {
        const randomX = Math.random() * 3; // 隨機 X 位移 1% 到 4%
        const randomY = Math.random() * 3; // 隨機 Y 位移 1% 到 4%
        return {
          transform: `translate(${randomX}vw, ${randomY}vw)`,
        };
      },
    },
    methods: {
      likeNote() {
        this.$emit('like');
      },
    },
  };
  </script>
  
  <style scoped>
  button {
    cursor: pointer;
  }
  .like-button {
    position: absolute;
    bottom: 5px;
    right: 5px;
    padding: 5px 20px; 
    background-color: #ffffff; 
    color: #546e7a; 
    border: 2px dashed #b0bec5; 
    border-radius: 4px; 
    cursor: pointer;
    font-size: 1rem; 
  }
  
  .like-button:hover {
    background-color: #f0f0f0; 
    color: #37474f; 
  }
  </style>