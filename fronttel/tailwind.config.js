/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      // Some useful comment
      fontFamily: {
        'farsi': ['Yekan'],
      },
    },
  },
  plugins: [
    require('tailwindcss-rtl'),
  ],
}
