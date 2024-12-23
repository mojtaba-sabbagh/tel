<script setup>
import { ref } from 'vue'

import FilterIcon from './icons/FilterIcon.vue'
import ChevronLeftIcon from './icons/ChevronLeftIcon.vue'
import ChevronDownIcon from './icons/ChevronDownIcon.vue'

const filterStatus = ref(false)
function toggleFilterStatus() {
  filterStatus.value = !filterStatus.value
}

const searchFormData = ref({
  advanced: {
    radioBox: '',
    search: '',
  },

  limited: {
    mianUnit: '',
    mainSubnit: '',
    subunit: '',
  },
})

function search() {}
</script>

<template>
  <section>
    <div
      class="flex justify-between items-center bg-white dark:bg-gray-800 text-lg font-medium dark:border dark:border-gray-700 rounded-t-lg py-2 px-4 shadow"
      v-on:click="toggleFilterStatus"
    >
      <div class="flex flex-row justify-center items-center gap-1 text-gray-900 dark:text-white">
        <FilterIcon></FilterIcon>
        <span>فیلتر</span>
      </div>
      <ChevronDownIcon v-if="filterStatus"></ChevronDownIcon>
      <ChevronLeftIcon v-else></ChevronLeftIcon>
    </div>

    <div
      class="bg-slate-50 dark:bg-gray-800 mx-0.5 mt-0.25 dark:border dark:border-gray-700 rounded-t-none rounded-lg p-8 shadow"
      v-if="filterStatus"
    >
      <form class="flex flex-col gap-10">
        <div class="flex flex-col gap-4">
          <div>
            <span
              class="bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-300 text-xs font-medium rounded-full px-4 py-1"
            >
              جستجو پیشرفته
            </span>
          </div>

          <div class="flex justify-start items-center gap-5">
            <div class="flex items-center">
              <input
                id="by-name"
                type="radio"
                value="byName"
                class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-600"
                v-model="searchFormData.advanced.radioBox"
              />
              <label
                for="by-name"
                class="text-gray-900 dark:text-gray-300 text-sm font-medium ms-1.5"
              >
                براساس نام
              </label>
            </div>

            <div class="flex items-center">
              <input
                checked
                id="by-department-position"
                type="radio"
                value="byDepartmentPosition"
                class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-600"
                v-model="searchFormData.advanced.radioBox"
              />
              <label
                for="by-department-position"
                class="text-gray-900 dark:text-gray-300 text-sm font-medium ms-1.5"
              >
                براساس پست سازمانی
              </label>
            </div>
          </div>

          <div>
            <div class="relative">
              <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                <svg
                  class="w-4 h-4 text-gray-500 dark:text-gray-400"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 20 20"
                >
                  <path
                    stroke="currentColor"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
                  />
                </svg>
              </div>
              <input
                type="search"
                id="search"
                class="w-full 2xl:w-2/5 md:w-1/2 p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                v-model.lazy.trim="searchFormData.advanced.search"
              />
            </div>
          </div>
        </div>

        <div class="flex flex-col gap-4">
          <div>
            <span
              class="bg-blue-100 text-blue-800 text-xs font-medium px-4 py-0.5 rounded-full dark:bg-blue-900 dark:text-blue-300"
            >
              جستجو محدود شده
            </span>
          </div>

          <div class="flex flex-col md:flex-row gap-6">
            <div class="flex flex-col gap-2 w-full md:w-1/3">
              <label for="main-unit" class="text-sm font-medium text-gray-900 dark:text-white">
                واحد اصلی
              </label>
              <select
                id="main-unit"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                v-model="searchFormData.limited.mianUnit"
              >
                <option value="default" selected>انتخاب کنید...</option>
                <option>United States</option>
                <option>Canada</option>
                <option>France</option>
                <option>Germany</option>
              </select>
            </div>

            <div class="flex flex-col gap-2 w-full md:w-1/3">
              <label for="main-subunit" class="text-sm font-medium text-gray-900 dark:text-white">
                زیر واحد اصلی
              </label>
              <select
                id="main-subunit"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                v-model="searchFormData.limited.mainSubnit"
              >
                <option value="default" selected>انتخاب کنید...</option>
                <option>United States</option>
                <option>Canada</option>
                <option>France</option>
                <option>Germany</option>
              </select>
            </div>

            <div class="flex flex-col gap-2 w-full md:w-1/3">
              <label for="sub-unit" class="text-sm font-medium text-gray-900 dark:text-white">
                زیر واحد فرعی
              </label>
              <select
                id="sub-unit"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                v-model="searchFormData.limited.subunit"
              >
                <option value="default" selected>انتخاب کنید...</option>
                <option>United States</option>
                <option>Canada</option>
                <option>France</option>
                <option>Germany</option>
              </select>
            </div>
          </div>
        </div>

        <div class="flex flex-col md:block">
          <button
            type="submit"
            class="bg-blue-600 dark:bg-blue-600 hover:bg-blue-700 dark:hover:bg-blue-700 focus:ring-4 focus:ring-blue-300 dark:focus:ring-blue-800 text-white text-sm font-medium focus:outline-none rounded-lg py-2.5 px-5 text-center"
          >
            جستجو
          </button>
        </div>
      </form>
    </div>
  </section>
</template>
