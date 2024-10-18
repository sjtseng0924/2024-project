<template>
  <div id="app">
    <Navbar/>
    <router-view class="pb-[75px]"/>
  </div>
</template>

<script>
import Navbar from '@/components/NavBar.vue'
export default {
  components: {
    Navbar,
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
