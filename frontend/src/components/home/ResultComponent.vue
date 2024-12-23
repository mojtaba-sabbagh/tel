<script setup>
import TableHeadComponent from '@/components/home/result/TableHeadComponent.vue'
import TableBodyComponent from '@/components/home/result/TableBodyComponent.vue'
import TableFootComponent from './result/TableFootComponent.vue'

import { ref } from 'vue'
const items = ref([])
for (let i = 0; i < 10; i++) {
  items.value[i] = i + 1
}
const resultTableData = ref({
  profile: 'https://picsum.photos/300/400',
  fullName: 'فاطمه چاقوساز رفسنجانی',
  extensionNumber: '2188',
  phoneNumber: '03431312188',
  organizationalPosition: 'معاون',
  organizationalUnit: 'معاونت آموزشی و تحصیلات تکمیلی',
  responsibility: 'کارشناس آموزش دانشکده ایران شناسی، کارشناس دانشجویان شهریه پرداز',
  description: 'آبدارخانه',
})
</script>

<template>
  <section>
    <div class="mt-4">
      <div class="bg-white dark:bg-gray-800 relative shadow-md sm:rounded-lg overflow-hidden">
        <div class="overflow-x-auto">
          <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
            <TableHeadComponent></TableHeadComponent>
            <TableBodyComponent
              v-for="(item, index) in items"
              v-bind:key="index"
              v-bind:result-table-data="resultTableData"
            ></TableBodyComponent>
          </table>
        </div>
        <TableFootComponent></TableFootComponent>
      </div>
    </div>
  </section>
</template>
