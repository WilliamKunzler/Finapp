document.querySelector("#form-register").addEventListener('submit', (event) => {
    event.preventDefault();

    let user = document.querySelector("#nome").value;
    let senha = document.querySelector("#senha").value;
    let email = document.querySelector("#email").value;

    fetch("/register/addAccount", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({username:user, password: senha, email: email})
    })
    
    .then(data => {


        if (data.status == 200) {
            Swal.fire({
                title: "Usuário cadastrado!",
                icon: "success",
                draggable: true
            }).then(() => {
                window.location.href = '/login';
            });
        }
        else{
            Swal.fire({
                icon: "error",
                title: "Usuário Inválido!",
                draggable: true
              });
        }

    

})
})