import { ref } from 'vue'

const API_URL = 'http://localhost:5000'

export function useUrlShortener() {
  const urlInput = ref('')
  const shortened = ref('')
  const error = ref('')
  const loading = ref(false)

  const shortenUrl = async () => {
    if (!urlInput.value) return
    
    error.value = ''
    loading.value = true

    try {
      const response = await fetch(`${API_URL}/shorten`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          url: urlInput.value
        })
      })

      if (!response.ok) {
        const data = await response.json()
        error.value = data.error || 'Failed to shorten URL'
        return
      }

      const data = await response.json()
      shortened.value = `${API_URL}/${data.short_code}`
    } catch (err) {
      error.value = 'Network error. Make sure backend is running.'
      console.error(err)
    } finally {
      loading.value = false
    }
  }

  const copyToClipboard = async () => {
    try {
      await navigator.clipboard.writeText(shortened.value)
    } catch (err) {
      console.error('Failed to copy:', err)
    }
  }

  return {
    urlInput,
    shortened,
    error,
    loading,
    shortenUrl,
    copyToClipboard
  }
}
