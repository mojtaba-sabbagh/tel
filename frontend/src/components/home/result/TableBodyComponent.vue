<script setup>
const props = defineProps({
  resultTableData: String,
})
</script>

<template>
  <tbody>
    <tr class="border-b dark:border-gray-700">
      <th scope="row" class="px-4 py-3">
        <img
          class="w-8 h-8 rounded-xl"
          v-if="props.resultTableData.profile"
          v-bind:src="props.resultTableData.profile"
        />
      </th>
      <th scope="row" class="px-4 py-3 text-nowrap font-medium text-gray-900 dark:text-white">
        {{ props.resultTableData.fullName }}
      </th>
      <td class="px-4 py-3 text-start text-nowrap">{{ props.resultTableData.extensionNumber }}</td>
      <td class="px-4 py-3 text-start text-nowrap">{{ props.resultTableData.phoneNumber }}</td>
      <td class="px-4 py-3 text-start text-nowrap">
        {{ props.resultTableData.organizationalPosition }}
      </td>
      <td class="px-4 py-3 text-start text-nowrap">
        {{ props.resultTableData.organizationalUnit }}
      </td>
      <td
        class="px-4 py-3 text-start overflow-hidden text-ellipsis break-words whitespace-normal line-clamp-2"
      >
        {{ props.resultTableData.responsibility }}
      </td>
      <td class="px-4 py-3 text-start text-nowrap">{{ props.resultTableData.description }}</td>
    </tr>
  </tbody>
</template>
