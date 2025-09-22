// tailwind.config.js
// Production-ready Tailwind CSS configuration for Vercel deployment
// See https://tailwindcss.com/docs/configuration for more info

module.exports = {
  content: [
    './public/**/*.html', // Scan all HTML files in public for class usage
    './src/js/**/*.js',   // Scan all JS files for class usage
  ],
  theme: {
    extend: {
      colors: {
        primary: '#2563eb',
        secondary: '#10b981',
        accent: '#10b981',
        success: '#059669',
      },
    },
  },
  plugins: [],
};
