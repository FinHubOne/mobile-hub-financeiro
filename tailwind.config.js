/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  safelist: [
    'bg-yellow-500',
    'shadow-yellow-500/30',
    'border-yellow-600',
    'bg-purple-500',
    'shadow-purple-500/30',
    'border-purple-600',
    'bg-blue-500',
    'shadow-blue-500/30',
    'border-blue-600',
    'bg-green-500',
    'shadow-green-500/30',
    'border-green-600',
    'bg-red-500',
    'shadow-red-500/30',
    'border-red-600',
    'bg-teal-500',
    'shadow-teal-500/30',
    'border-teal-600',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
