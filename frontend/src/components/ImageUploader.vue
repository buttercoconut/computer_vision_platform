<template>
  <div class="uploader">
    <input type="file" accept="image/*" @change="onFileChange" />
  </div>
</template>

<script setup lang="ts">
import { defineEmits } from 'vue'

const emit = defineEmits(['image-uploaded'])

function onFileChange(event: Event) {
  const target = event.target as HTMLInputElement
  if (target.files && target.files[0]) {
    emit('image-uploaded', target.files[0])
  }
}
</script>

<style scoped>
.uploader {
  margin: 20px 0;
}
</style>
