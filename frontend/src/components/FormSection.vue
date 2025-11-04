<template>
  <section class="form-section">
    <div class="container">
      <h2>Shorten Your Link</h2>
      
      <div class="form-wrapper">
        <div class="input-group">
          <input 
            type="url" 
            placeholder="Enter your long URL..." 
            class="url-input"
            v-model="urlInput"
            @keyup.enter="shortenUrl"
            :disabled="loading"
          >
          <button 
            class="btn btn-primary" 
            @click="shortenUrl"
            :disabled="loading"
          >
            {{ loading ? 'Shortening...' : 'Shorten' }}
          </button>
        </div>
        
        <div v-if="error" class="error-box">
          <p>❌ {{ error }}</p>
        </div>
        
        <div v-if="shortened" class="result">
          <p class="result-label">Your shortened link:</p>
          <div class="result-display">
            <code>{{ shortened }}</code>
            <button class="btn-copy" @click="copyToClipboard">📋 Copy</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useUrlShortener } from '../composables/useUrlShortener'

const { urlInput, shortened, error, loading, shortenUrl, copyToClipboard } = useUrlShortener()
</script>

<style scoped>
.form-section {
  background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #16213e 100%);
  padding: 6rem 2rem;
  min-height: 50vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.container {
  max-width: 600px;
  width: 100%;
}

h2 {
  font-size: 2rem;
  text-align: center;
  margin-bottom: 2rem;
}

.form-wrapper {
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(102, 126, 234, 0.2);
  border-radius: 12px;
  padding: 2rem;
}

.input-group {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
}

.url-input {
  flex: 1;
  background: rgba(102, 126, 234, 0.1);
  border: 2px solid rgba(102, 126, 234, 0.3);
  border-radius: 8px;
  padding: 1rem;
  color: #e0e0e0;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.url-input:focus {
  outline: none;
  border-color: #667eea;
  background: rgba(102, 126, 234, 0.2);
}

.url-input::placeholder {
  color: #666;
}

.url-input:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn {
  padding: 1rem 2rem;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}

.btn-primary:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.error-box {
  background: rgba(244, 67, 54, 0.1);
  border: 1px solid rgba(244, 67, 54, 0.3);
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 1rem;
  color: #ff6b6b;
}

.result {
  background: rgba(76, 175, 80, 0.1);
  border: 1px solid rgba(76, 175, 80, 0.3);
  border-radius: 8px;
  padding: 1.5rem;
}

.result-label {
  color: #a0a0a0;
  margin-bottom: 1rem;
  font-size: 0.9rem;
}

.result-display {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: rgba(76, 175, 80, 0.15);
  padding: 1rem;
  border-radius: 6px;
}

.result-display code {
  color: #4caf50;
  font-weight: 600;
  font-size: 1.1rem;
  word-break: break-all;
}

.btn-copy {
  background: transparent;
  border: none;
  color: #4caf50;
  cursor: pointer;
  padding: 0.5rem 1rem;
  transition: all 0.3s ease;
}

.btn-copy:hover {
  transform: scale(1.1);
}

@media (max-width: 768px) {
  .input-group {
    flex-direction: column;
  }

  h2 {
    font-size: 1.5rem;
  }

  .result-display {
    flex-direction: column;
    gap: 1rem;
    align-items: flex-start;
  }
}
</style>
