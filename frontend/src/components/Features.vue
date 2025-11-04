<template>
  <section class="features">
    <div class="container">
      <h2>Why LinkSnip?</h2>
      <div class="features-grid">
        <div class="feature">
          <div class="icon">⚡</div>
          <h3>Fast</h3>
          <p>Shortened instantly</p>
        </div>
        <div class="feature">
          <div class="icon">📊</div>
          <h3>Track Clicks</h3>
          <p>See how many times your link is clicked</p>
        </div>
        <div class="feature">
          <div class="icon">🔗</div>
          <h3>Simple</h3>
          <p>Just paste and click</p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.features {
  background: #0f172a;
  padding: 4rem 2rem;
  border-bottom: 1px solid rgba(102, 126, 234, 0.2);
}

.container {
  max-width: 1000px;
  margin: 0 auto;
}

h2 {
  font-size: 2rem;
  text-align: center;
  margin-bottom: 3rem;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.feature {
  background: rgba(102, 126, 234, 0.05);
  border: 1px solid rgba(102, 126, 234, 0.2);
  border-radius: 10px;
  padding: 2rem;
  text-align: center;
  transition: all 0.3s ease;
}

.feature:hover {
  background: rgba(102, 126, 234, 0.1);
  border-color: rgba(102, 126, 234, 0.4);
  transform: translateY(-4px);
}

.icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.feature h3 {
  color: #667eea;
  margin-bottom: 0.5rem;
}

.feature p {
  color: #a0a0a0;
  font-size: 0.95rem;
}

@media (max-width: 768px) {
  h2 {
    font-size: 1.5rem;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }
}
</style>
