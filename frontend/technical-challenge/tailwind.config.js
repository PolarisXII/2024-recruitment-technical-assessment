/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'theme-blue': '#1479f2',
        'theme-purple':'#c1cbf1'
      }
    },
  },
  plugins: [],
}

