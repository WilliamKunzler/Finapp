document.querySelector("#edit-button").addEventListener("click", (e) => {
    e.preventDefault()
    document.querySelector("#btn-edit").style.display = "block"
    document.querySelector("#edit-button").style.display = "none"
    document.querySelectorAll("input").forEach(input => {
        input.style.pointerEvents = "all";
        input.style.border = "1px solid var(--text-2)";
    });
})