<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script setup lang="ts">
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app')
</script>

<style>
  body { margin: 0; font-family: Avenir, Helvetica, Arial, sans-serif; }
</style>
