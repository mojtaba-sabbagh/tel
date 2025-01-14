<script>
export default {
  data() {
    return {
      hasError: false,
      entered: false,
      itemSelected: '',
    }
  },
  props: {
    label_title: String,
    options: {},
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
    order: {
      type: Number,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    constraint() {
      this.entered = true
      if (this.required & (this.itemSelected == '')) {
        this.hasError = true
      } else {
        this.hasError = false
      }
      this.$emit('onChangeValue', this.itemSelected)
      this.$emit('onStateChange', this.hasError, this.order)
    },
    onEnterFunc() {
      this.constraint()
      this.$emit('onEnterKey')
    },
  },
}
</script>

<template>
  <div class="flex flex-col items-start">
    <label for="input-success" class="text-sm font-medium text-gray-900 dark:text-white">
      {{ label_title }}
    </label>
    <select
      v-model="itemSelected"
      @blur="constraint"
      :disabled="disabled"
      :required="required"
      @keyup.enter="onEnterFunc"
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    >
      <option v-bind:value="0" selected>همه واحدها</option>
      <option v-for="option in options" v-bind:value="option.ID" v-bind:key="option.ID">
        {{ option.text }}
      </option>
    </select>
  </div>
</template>
