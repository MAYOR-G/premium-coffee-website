/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'brand-black': '#0a0a0a',
        'brand-charcoal': '#1a1a1a',
        'brand-cream': '#f4f1eb',
        'brand-accent': '#e63946',
        'brand-beige': '#d5c7b3',
      },
      fontFamily: {
        heading: ['Oswald', 'sans-serif'],
        body: ['Inter', 'sans-serif'],
        accent: ['Playfair Display', 'serif'],
      }
    },
  },
  plugins: [],
}
