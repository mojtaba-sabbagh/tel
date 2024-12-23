<script setup>
import SearchComponent from '@/components/home/SearchComponent.vue'
import ResultComponent from '@/components/home/ResultComponent.vue'
</script>

<template>
  <div class="container mx-auto p-5">
    <h2
      class="text-gray-900 dark:text-white text-xl md:text-2xl font-bold my-4 md:my-10 border-s-8 border-s-gray-900 dark:border-s-white rounded-s-lg ps-2 leading-tight tracking-tight"
    >
      سامانه تلفن دانشگاه
    </h2>

    <SearchComponent></SearchComponent>
    <ResultComponent></ResultComponent>
  </div>
</template>
