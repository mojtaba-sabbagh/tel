<script setup>
import TableHeadComponent from '@/components/home/result/TableHeadComponent.vue'
import TableBodyComponent from '@/components/home/result/TableBodyComponent.vue'

defineProps({ itemsRow: Array })
</script>

<template>
  <section>
    <div class="overflow-x-auto">
      <table class="w-full text-sm text-start text-gray-500 dark:text-gray-400">
        <TableHeadComponent></TableHeadComponent>
        <tbody>
          <TableBodyComponent
            v-for="(item, index) in itemsRow"
            v-bind:key="index"
            v-bind:result-table-data="item"
          ></TableBodyComponent>
        </tbody>
      </table>
    </div>
  </section>
</template>
