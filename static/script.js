const display = document.querySelector(".display");
const buttons = document.querySelectorAll(".btn");
const themeToggle = document.querySelector(".theme-toggle-switch");
const themeToggleThumb = document.querySelector(".theme-toggle-switch-thumb");

let currentExpression = "";
let currentTheme = 1;

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    const value = button.textContent;

    if (value === "RESET") {
      currentExpression = "";
      display.textContent = "";
    } else if (value === "DEL") {
      currentExpression = currentExpression.slice(0, -1);
      display.textContent = currentExpression;
    } else if (value === "=") {
      try {
        const result = eval(currentExpression);
        display.textContent = result;
        currentExpression = result.toString();
      } catch (error) {
        display.textContent = "Error";
        currentExpression = "";
      }
    } else {
      currentExpression += value;
      display.textContent = currentExpression;
    }
  });
});

themeToggle.addEventListener("click", () => {
  currentTheme = (currentTheme % 3) + 1;
  updateTheme();
});

function updateTheme() {
  document.body.classList.remove("theme-2", "theme-3");

  if (currentTheme === 2) {
    document.body.classList.add("theme-2");
    themeToggleThumb.style.left = "22px";
  } else if (currentTheme === 3) {
    document.body.classList.add("theme-3");
    themeToggleThumb.style.left = "42px";
  } else {
    themeToggleThumb.style.left = "3px";
  }
}