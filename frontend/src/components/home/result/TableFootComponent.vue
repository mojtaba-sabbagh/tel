<template>
  <nav
    class="flex flex-col sm:flex-row justify-between items-center space-y-3 sm:space-y-0 p-4"
    aria-label="Table navigation"
  >
    <span class="text-sm font-normal text-gray-500 dark:text-gray-400">
      نمایش
      <span class="font-semibold text-gray-900 dark:text-white">1-10</span>
      از
      <span class="font-semibold text-gray-900 dark:text-white">1000</span>
    </span>
    <ul class="inline-flex items-stretch -space-x-px">
      <li>
        <a
          href="#"
          class="flex items-center justify-center h-full py-1.5 px-3 ml-0 text-gray-500 bg-white rounded-s-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
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
        </a>
      </li>
      <li>
        <a
          href="#"
          class="flex items-center justify-center h-full py-1.5 px-3 leading-tight text-gray-500 bg-white rounded-e-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
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
        </a>
      </li>
    </ul>
  </nav>
</template>
