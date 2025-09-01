document.querySelector("#form-login").addEventListener('submit', (event) => {
    event.preventDefault();

    let senha = document.querySelector("#senha-login").value;
    let email = document.querySelector("#email-login").value;

    fetch("/login/entrance", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password: senha, email: email })
    })
        .then(res => res.json())   // ✅ transforma a resposta em JSON
        .then(data => {
            console.log("Resposta do backend:", data); // aqui você verá {"status": "success", "embed_url": "..."}

            if (data.status === "success") {
                // Salva a URL corretamente
                // localStorage.setItem("embed_url", data.embed_url);
                localStorage.setItem("auth_token", data.authentication_token);

                // Redireciona
                window.location.href = '/dashboard';
            } else {
                Swal.fire({
                    icon: "error",
                    title: "Usuário Inválido!",
                    draggable: true
                });
            }
        })
        .catch(error => console.error("Erro na requisição:", error));

});
