document.addEventListener("DOMContentLoaded", () => {
  const tryBtn = document.getElementById("tryBtn");

  tryBtn.addEventListener("click", () => {
    window.open(
      "https://plants-leaf-disease-detection4u.streamlit.app/",
      "_blank"
    );
  });
});
