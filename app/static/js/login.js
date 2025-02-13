document.querySelector("#form-login").addEventListener('submit', (event) => {
    event.preventDefault();

    let senha = document.querySelector("#senha-login").value;
    let email = document.querySelector("#email-login").value;

    fetch("/login/entrance", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ password: senha, email: email })
    })
    .then(data => {
        if (data.status == 200) {
            window.location.href = '/';
        }
        else{
            Swal.fire({
                icon: "error",
                title: "Usuário Inválido!",
                draggable: true
              });
        }

})
    .catch(error => console.error("Erro na requisição:", error));
});
