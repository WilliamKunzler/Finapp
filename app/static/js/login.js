document.querySelector("#form-login").addEventListener('submit', (event) => {
    event.preventDefault();

    let senha = document.querySelector("#senha-login").value;
    let email = document.querySelector("#email-login").value;

    console.log(senha, email)

    // fetch("/login/entrance", {
    //     method: "POST",
    //     headers: {
    //         "Content-Type": "application/json"
    //     },
    //     body: JSON.stringify({ password: senha, email: email})
    // })
    // }).then(data => {
    //     if (data.status == 200) {
    //             window.location.href = '/login';
        })


