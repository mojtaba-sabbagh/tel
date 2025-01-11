import { defineStore } from 'pinia'

export const useDarkModeStore = defineStore('storeId', {
  state: () => {
    return {
      darkModeStatus: localStorage.getItem('darkModeStatus') || '',
    }
  },
  actions: {
    toggleDarkMode() {
      if (this.darkModeStatus == 'dark') {
        this.darkModeStatus = ''
        localStorage.setItem('darkModeStatus', '')
      } else {
        this.darkModeStatus = 'dark'
        localStorage.setItem('darkModeStatus', 'dark')
      }
    },
  },
})
