<template>
  <section class="hero">
    <div class="hero-content">
      <h1>LinkSnip</h1>
      <p>Shorten your URLs instantly</p>
    </div>
  </section>
</template>

<style scoped>
.hero {
  background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #16213e 100%);
  min-height: 50vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  border-bottom: 1px solid rgba(102, 126, 234, 0.2);
}

.hero-content {
  text-align: center;
}

h1 {
  font-size: 3rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 1rem;
}

p {
  font-size: 1.3rem;
  color: #a0a0a0;
}

@media (max-width: 768px) {
  h1 {
    font-size: 2rem;
  }
}
</style>
