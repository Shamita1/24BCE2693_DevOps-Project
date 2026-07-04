document.addEventListener("DOMContentLoaded", () => {
  const el = document.getElementById("build-info");
  if (el) {
    el.textContent = "Version 1.0 | Served from Docker + Kubernetes | Deployed " + new Date().toLocaleDateString();
  }
});
