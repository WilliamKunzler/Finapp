document.querySelector(".userAdd").addEventListener('click', (event) => {
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

        console.log(data)
        if (data.status == 200) {
            Swal.fire({
                title: "Drag me!",
                icon: "success",
                draggable: true
        });
}})            
})