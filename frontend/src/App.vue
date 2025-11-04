<template>
  <div class="app">
    <Hero />
    <Features />
    <FormSection />
  </div>
</template>

<script setup>
import Hero from './components/Hero.vue'
import Features from './components/Features.vue'
import FormSection from './components/FormSection.vue'
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body, #app {
  height: 100%;
  width: 100%;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', sans-serif;
  background: #0a0e27;
  color: #e0e0e0;
  line-height: 1.6;
}

html {
  scroll-behavior: smooth;
}
</style>
