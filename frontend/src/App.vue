<template>
  <div id="app">
    <ChatApp />
  </div>
</template>

<script>
import ChatApp from './components/ChatApp.vue';

export default {
  name: 'App',
  components: {
    ChatApp,
  },
};
</script>

<style>
body {
  margin: 0;
  font-family: 'Arial', sans-serif;
}
#app {
  height: 90vh;
}
</style>
