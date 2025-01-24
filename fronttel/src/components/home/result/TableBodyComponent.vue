<script setup>
import { useTelLink } from '@/composables/useTelLink'

defineProps({
  resultTableData: Object,
})
</script>

<template>
  <tr class="border-b dark:border-gray-700">
    <!-- <th scope="row" class="px-4 py-3">
        <img
          class="w-8 h-8 rounded-xl"
          v-if="resultTableData.profile"
          v-bind:src="resultTableData.profile"
        />
      </th> -->
    <th scope="row" class="px-4 py-3 text-nowrap font-medium text-gray-900 dark:text-white">
      {{ resultTableData.full_name }}
    </th>
    <td class="px-4 py-3 text-start text-nowrap">{{ resultTableData.extension }}</td>
    <td class="px-4 py-3 text-start text-nowrap">
      <a :href="useTelLink(resultTableData.complete_number)">
        {{ resultTableData.complete_number }}
      </a>
    </td>
    <td class="px-4 py-3 text-start text-nowrap">
      {{ resultTableData.position }}
    </td>
    <td class="px-4 py-3 text-start text-nowrap">
      {{ resultTableData.dep }}
    </td>
    <td
      class="px-4 py-3 text-start overflow-hidden text-ellipsis break-words whitespace-normal line-clamp-2"
    >
      {{ resultTableData.duties }}
    </td>
    <td class="px-4 py-3 text-start text-nowrap">{{ resultTableData.description }}</td>
  </tr>
</template>
