<script setup>
import SearchComponent from '@/components/home/SearchComponent.vue'
import ResultComponent from '@/components/home/ResultComponent.vue'
import TitleComponent from '@/components/home/TitleComponent.vue'
import { ref, watch } from 'vue'

const isLightMode = ref(true)
const darkModeStatus = ref('')

watch(isLightMode, () => {
  if (isLightMode.value) {
    darkModeStatus.value = ''
  } else {
    darkModeStatus.value = 'dark'
  }
})
</script>

<template>
  <div v-bind:class="darkModeStatus">
    <div class="min-h-svh bg-neutral-100 dark:bg-gray-900 font-persian">
      <div class="container mx-auto p-5">
        <div class="flex flex-row justify-between items-center">
          <TitleComponent></TitleComponent>

          <label class="inline-flex items-center me-2 cursor-pointer">
            <input type="checkbox" class="sr-only peer" v-model="isLightMode" />
            <div
              class="relative w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-focus:ring-4 peer-focus:ring-yellow-300 dark:peer-focus:ring-yellow-800 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-yellow-400"
            ></div>
            <span
              class="ms-3 text-sm font-medium text-gray-900 dark:text-gray-300"
              v-if="isLightMode"
            >
              روشن
            </span>
            <span class="ms-3 text-sm font-medium text-gray-900 dark:text-gray-300" v-else>
              تیره
            </span>
          </label>
        </div>

        <SearchComponent></SearchComponent>
        <ResultComponent></ResultComponent>
      </div>
    </div>
  </div>
</template>
