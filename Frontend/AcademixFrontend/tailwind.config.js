/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ["./src/**/*.{html,ts}", "./node_modules/flowbite/**/*.js"],

  darkMode: "class",
  theme: {
    extend: {
      backgroundColor: {
        dark: "#121212", // Dark mode background color
      },
      textColor: {
        dark: "#ffffff", // Dark mode text color
      },
    },
  },
  plugins: [require("flowbite/plugin")],
};
