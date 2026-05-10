<template>
  <div class="app-container">
    <h1>Computer Vision Platform</h1>
    <ImageUploader @image-uploaded="handleImageUploaded" />
    <ResultViewer v-if="result" :result="result" />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import ImageUploader from './components/ImageUploader.vue'
import ResultViewer from './components/ResultViewer.vue'
import { uploadImage } from './services/api'

const result = ref<any>(null)

async function handleImageUploaded(file: File) {
  try {
    const res = await uploadImage(file)
    result.value = res
  } catch (e) {
    console.error('Upload failed', e)
  }
}
</script>

<style scoped>
.app-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}
</style>
