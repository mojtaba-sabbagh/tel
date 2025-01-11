<script setup>
import { onMounted, ref } from 'vue'

import FilterIcon from './icons/FilterIcon.vue'
import ChevronLeftIcon from './icons/ChevronLeftIcon.vue'
import ChevronDownIcon from './icons/ChevronDownIcon.vue'
import SpinnerIcon from './icons/SpinnerIcon.vue'
import DropDown from './search/DropDown.vue'
import InputText from './search/InputText.vue'
import ResultComponent from '@/components/home/ResultComponent.vue'
import axios from 'axios'

axios.defaults.headers.get['Content-Type'] = 'application/json'

const filterStatus = ref(false)
function toggleFilterStatus() {
  filterStatus.value = !filterStatus.value
}

const serverUrl = import.meta.env.VITE_SERVER_URL
const offset = ref(0)
const pageSize = ref(50)

const mainDep = ref('')
const subDep = ref('')
const subSubDep = ref('')

const mainDepOptions = ref({})
function depList0() {
  axios({
    method: 'get',
    url: serverUrl + '/tel/deps/?level=0',
  })
    .then((response) => {
      mainDepOptions.value = response.data
    })
    .catch((error) => {
      errorMessage.value = error //'خطایی در گرفتن اطلاعات کاربر رخ داد'; //error.data
    })
}
depList0()

const mainSubDepOptions = ref({})
function depList1(sdep) {
  axios({
    method: 'get',
    url: serverUrl + '/tel/deps/?level=1' + '&super-dep=' + sdep,
  })
    .then((response) => {
      mainSubDepOptions.value = response.data
    })
    .catch((error) => {
      errorMessage.value = error //'خطایی در گرفتن اطلاعات کاربر رخ داد'; //error.data
    })
}

const subSubDepOptions = ref(Object)
function depList2(sdep) {
  axios({
    method: 'get',
    url: serverUrl + '/tel/deps/?level=2' + '&super-dep=' + sdep,
  })
    .then((response) => {
      subSubDepOptions.value = response.data
    })
    .catch((error) => {
      errorMessage.value = error //'خطایی در گرفتن اطلاعات کاربر رخ داد'; //error.data
    })
}

function updateDep(newValue) {
  if (newValue && newValue != '0') {
    mainDep.value = newValue
    finalDep.value = newValue
    mainSubDepOptions.value = depList1(finalDep.value)
  } else {
    mainDep.value = ''
    finalDep.value = ''
  }
}

function updateSubDep(newValue) {
  if (newValue && newValue != '0') {
    subDep.value = newValue
    finalDep.value = newValue
    subSubDepOptions.value = depList2(finalDep.value)
  } else {
    subDep.value = ''
    updateDep(mainDep.value)
  }
}

const len = ref(0)
function updateSubSubDep(newValue) {
  if (newValue && newValue != '0') {
    subSubDep.value = newValue
    finalDep.value = newValue
  } else {
    subSubDep.value = ''
    updateSubDep(subDep.value)
  }
}

function updateSearchPost(newValue) {
  if (newValue && newValue != '0') {
    finalPost.value = newValue
  } else {
    finalPost.value = 0
  }
}

const searchPostOptions = ref()
function postList() {
  axios({
    method: 'get',
    url: serverUrl + '/tel/posts/',
  })
    .then((response) => {
      searchPostOptions.value = response.data
    })
    .catch((error) => {
      errorMessage.value = error //'خطایی در گرفتن اطلاعات کاربر رخ داد'; //error.data
    })
}
postList()

const searchStart = ref(false)

const searchBy = ref('sname')
const finalDep = ref('')
const family = ref('')
const finalPost = ref(0)
function submitSearch() {
  let q = ''
  let dep = finalDep.value
  searchStart.value = true
  let url = ''
  offset.value = 0
  if (searchBy.value === 'sname') {
    q = family.value
    url = serverUrl + '/tel/byname/'
  } else if (searchBy.value === 'spost') {
    q = finalPost.value
    url = serverUrl + '/tel/bypost/'
  } else {
    return
  }
  if (q && dep) {
    //url = url + '?q=' + q + '&dep=' + dep;
    url = url + dep + '/' + q + '/'
  } else if (q && !dep) {
    //url = url + '?q=' + q;
    url = url + '0' + '/' + q + '/'
  } else if (!q && dep) {
    //url = url + '?dep=' + dep;
    url = url + dep + '/' + '0' + '/'
  } else {
    url = url + '0/0/'
  }
  //search api call
  getPage(url)
}

const searchResults = ref(null)
const next = ref(null)
const pre = ref(null)
const errorMessage = ref('')
function getPage(url) {
  axios({
    method: 'get',
    url: url,
  })
    .then((response) => {
      searchResults.value = response.data.results
      next.value = response.data.next
      pre.value = response.data.previous
      searchStart.value = false
    })
    .catch((error) => {
      errorMessage.value = error //'خطایی در گرفتن اطلاعات کاربر رخ داد'; //error.data
      searchStart.value = false
    })
}

onMounted(() => {
  submitSearch()
})

function getNext() {
  offset.value = (parseInt(next.value.split('=')[1]) - 1) * pageSize.value
  getPage(next.value)
}

function getPre() {
  let page = pre.value.split('=')[1]
  if (page) {
    offset.value = (parseInt(page) - 1) * this.pageSize
  } else {
    offset.value = 0
  }
  this.getPage(pre.value)
}

function updatefamily(newValue) {
  family.value = newValue
}
</script>

<template>
  <main>
    <section>
      <div
        class="flex justify-between items-center bg-white dark:bg-gray-800 text-lg font-medium dark:border dark:border-gray-700 rounded-t-lg py-2 px-4 shadow-sm"
        v-on:click="toggleFilterStatus"
      >
        <div class="flex flex-row justify-center items-center gap-1 text-gray-900 dark:text-white">
          <FilterIcon></FilterIcon>
          <span>فیلتر</span>
        </div>
        <ChevronDownIcon v-if="filterStatus"></ChevronDownIcon>
        <ChevronLeftIcon v-else></ChevronLeftIcon>
      </div>

      <transition name="slide-fade">
        <div
          class="bg-slate-50 dark:bg-gray-800 mx-0.5 mt-0.25 dark:border dark:border-gray-700 rounded-t-none rounded-lg p-8 shadow-md"
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
                    v-model="searchBy"
                    id="by-name"
                    type="radio"
                    value="sname"
                    class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-600"
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
                    id="by-department-position"
                    type="radio"
                    v-model="searchBy"
                    value="spost"
                    class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-600"
                  />
                  <label
                    for="by-department-position"
                    class="text-gray-900 dark:text-gray-300 text-sm font-medium ms-1.5"
                  >
                    براساس پست سازمانی
                  </label>
                </div>
              </div>

              <div class="w-full md:w-1/2 2xl:w-2/5">
                <InputText
                  v-if="sname"
                  input_placeholder=""
                  @onChangeValue="updatefamily"
                  :order="1"
                  @onEnterKey="submitSearch"
                />
                <DropDown
                  v-if="spost"
                  :options="searchPostOptions"
                  @onChangeValue="updateSearchPost"
                  :order="5"
                  @onEnterKey="submitSearch"
                />
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
                  <DropDown
                    label_title="واحد اصلی"
                    :options="mainDepOptions"
                    @onChangeValue="updateDep"
                    :order="1"
                  />
                </div>

                <div class="flex flex-col gap-2 w-full md:w-1/3">
                  <DropDown
                    label_title="زیر واحد اصلی"
                    :options="mainSubDepOptions"
                    @onChangeValue="updateSubDep"
                    :order="2"
                  />
                </div>

                <div class="flex flex-col gap-2 w-full md:w-1/3">
                  <DropDown
                    label_title="زیر واحد فرعی"
                    :options="subSubDepOptions"
                    @onChangeValue="updateSubSubDep"
                    :order="3"
                  />
                </div>
              </div>
            </div>

            <div class="flex flex-col md:block">
              <button
                type="submit"
                @click="submitSearch"
                class="bg-blue-600 dark:bg-blue-600 hover:bg-blue-700 dark:hover:bg-blue-700 focus:ring-4 focus:ring-blue-300 dark:focus:ring-blue-800 text-white text-sm font-medium focus:outline-none rounded-lg py-2.5 px-5 text-center"
              >
                <span v-if="searchStart">
                  <SpinnerIcon></SpinnerIcon>
                </span>
                <span>{{ searchStart ? 'در حال جستجو...' : 'جستجو' }}</span>
              </button>
            </div>
          </form>
        </div>
      </transition>
    </section>

    <section>
      <div class="mt-4 shadow-lg">
        <div class="bg-white dark:bg-gray-800 relative shadow-md sm:rounded-lg overflow-hidden">
          <ResultComponent :items-row="searchResults"></ResultComponent>

          <nav
            class="flex flex-col sm:flex-row justify-between items-center p-4"
            aria-label="Table navigation"
          >
            <span class="text-sm font-normal text-gray-500 dark:text-gray-400">
              نمایش
              <span class="font-semibold text-gray-900 dark:text-white">
                {{ `${offset + 1}-${offset + pageSize + 1}` }}
              </span>
            </span>
            <ul class="inline-flex items-stretch -space-x-px">
              <li>
                <button
                  type="button"
                  @click.prevent="getNext"
                  class="flex items-center justify-center h-full py-1.5 px-3 ml-0 text-gray-500 bg-white rounded-s-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white disabled:bg-slate-100"
                  :disabled="!next"
                >
                  <span class="sr-only">قبل</span>
                  <svg
                    class="w-5 h-5"
                    aria-hidden="true"
                    fill="currentColor"
                    viewbox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                      clip-rule="evenodd"
                    />
                  </svg>
                </button>
              </li>
              <li>
                <button
                  :disabled="!pre"
                  type="button"
                  @click="getPre"
                  class="flex items-center justify-center h-full py-1.5 px-3 leading-tight text-gray-500 bg-white rounded-e-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white disabled:bg-slate-100"
                >
                  <span class="sr-only">بعد</span>
                  <svg
                    class="w-5 h-5"
                    aria-hidden="true"
                    fill="currentColor"
                    viewbox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
                      clip-rule="evenodd"
                    />
                  </svg>
                </button>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </section>
  </main>
</template>

<style scoped>
/*
  Enter and leave animations can use different
  durations and timing functions.
*/
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateY(-20px);
  opacity: 0;
}
</style>
