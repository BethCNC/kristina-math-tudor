/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/**/*.{ts,tsx,js,jsx}", "./components/**/*.{ts,tsx,js,jsx}", "./pages/**/*.{ts,tsx,js,jsx}"],
  theme: {
    extend: {
      colors: {
        black: "#080808",
        white: "#fafafa",
        neutral: {
          50:"#e5e6e6",100:"#d4d5d6",200:"#bec0c1",300:"#a9acac",400:"#939798",
          500:"#7e8283",600:"#696c6d",700:"#545757",800:"#3f4142",900:"#2a2b2c",950:"#191a1a"
        },
        coral: {
          50:"#fbe4dd",100:"#f8d2c6",200:"#f5bba9",300:"#f2a48d",400:"#ee8e71",
          500:"#eb7754",600:"#c46346",700:"#9d4f38",800:"#763c2a",900:"#4e281c",950:"#2f1811"
        },
        pink: {
          50:"#faf5f6",100:"#f6eeef",200:"#f2e5e7",300:"#eedde0",400:"#e9d4d8",
          500:"#e5ccd0",600:"#bfaaad",700:"#99888b",800:"#736668",900:"#4c4445",950:"#2e292a"
        },
        yellow: {
          50:"#fafae5",100:"#f6f7d3",200:"#f1f2bd",300:"#edeea7",400:"#e8ea91",
          500:"#e4e67b",600:"#bec067",700:"#989952",800:"#72733e",900:"#4c4d29",950:"#2e2e19"
        },
        blue: {
          50:"#f3f8fb",100:"#ebf4f8",200:"#e1eef4",300:"#d7e8f0",400:"#cde3ed",
          500:"#c3dde9",600:"#a2b8c2",700:"#82939b",800:"#626f75",900:"#414a4e",950:"#272c2f"
        }
      },
      fontFamily: {
        sans: ["Vend Sans","ui-sans-serif","system-ui","-apple-system","Segoe UI","Roboto","Arial","Noto Sans","sans-serif"]
      },
      borderRadius: {xl:"0.875rem", "2xl":"1rem"},
      boxShadow: {
        card:"0 1px 2px rgba(0,0,0,0.06), 0 6px 20px rgba(0,0,0,0.06)"
      }
    }
  },
  plugins: []
}
