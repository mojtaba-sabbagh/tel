<script setup>
const tableHeaders = [
  // 'پروفایل',
  'نام و نام‌ خانوادگی',
  'شماره داخلی',
  'شماره تلفن',
  'پست سازمانی',
  'واحد سازمانی',
  'مسئولیت',
  'توضیحات',
]
</script>

<template>
  <thead class="text-xs text-gray-700 bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
    <tr>
      <th
        scope="col"
        class="px-4 py-3 text-center text-nowrap"
        v-for="(tableHeader, index) in tableHeaders"
        v-bind:key="index"
      >
        {{ tableHeader }}
      </th>
    </tr>
  </thead>
</template>
