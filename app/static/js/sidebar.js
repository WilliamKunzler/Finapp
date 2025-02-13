document.querySelectorAll('.item-sidebar').forEach(elemento => {
    elemento.addEventListener('click', function() {
        window.location.href = `/${elemento.id}`
    });
});