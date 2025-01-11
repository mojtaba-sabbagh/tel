<script>
export default {
  props: {
    label_title: String,
    input_placeholder: {
      type: String,
      default: 'حمیدرضا',
    },
    required: {
      type: Boolean,
      default: false,
    },
    accept_msg: {
      type: String,
      default: '',
    },
    reject_msg: {
      type: String,
      default: '',
    },
    l2r: {
      type: Boolean,
      default: false,
    },
    width_col: {
      type: String,
      default: 'w-1',
    },
    is_number: {
      type: Boolean,
      default: false,
    },
    value: '',
    order: {
      type: Number,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      hasError: false,
      entered: false,
      dataValue: this.value,
    }
  },
  computed: {},
  methods: {
    constraint() {
      this.entered = true
      if (this.required & (this.dataValue == '')) {
        this.hasError = true
      } else {
        this.hasError = false
      }
      if (this.is_number) {
        this.dataValue = this.convert(this.dataValue)
      }
      this.$emit('onChangeValue', this.dataValue)
      this.$emit('onStateChange', this.hasError, this.order)
    },
    onEnterFunc() {
      this.constraint()
      this.$emit('onEnterKey')
    },
    convert(str) {
      let persianNumbers = [/۰/g, /۱/g, /۲/g, /۳/g, /۴/g, /۵/g, /۶/g, /۷/g, /۸/g, /۹/g],
        arabicNumbers = [/٠/g, /١/g, /٢/g, /٣/g, /٤/g, /٥/g, /٦/g, /٧/g, /٨/g, /٩/g]

      if (typeof str === 'string') {
        for (let i = 0; i < 10; i++) {
          str = str.replace(persianNumbers[i], i).replace(arabicNumbers[i], i)
        }
      }
      return str
    },
  },
}
</script>

<template>
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
      class="w-full p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
      v-model="dataValue"
      @blur="constraint"
      @keyup.enter="onEnterFunc"
      :disabled="disabled"
      :required="required"
      v-bind:placeholder="input_placeholder"
    />
  </div>
</template>
