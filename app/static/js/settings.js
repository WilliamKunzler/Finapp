document.querySelector("#edit-button").addEventListener("click", (e) => {
    e.preventDefault()
    document.querySelector("#btn-edit").style.display = "block"
    document.querySelector("#edit-button").style.display = "none"
    document.querySelectorAll("input").forEach(input => {
        input.style.pointerEvents = "all";
        document.querySelector('#field-image').style.pointerEvents = "all";
        input.style.border = "1px solid var(--text-2)";
    });
})

document.querySelector("#form-settings").addEventListener("submit", (e) => {
    e.preventDefault()
    let first_name = document.querySelector("#first_name").value
    let last_name = document.querySelector("#last_name").value
    let email = document.querySelector("#email").value
    let date_birth = document.querySelector("#date_birth").value
    let mobile_number = document.querySelector("#mobile_number").value
    mobile_number == "" ? mobile_number = null : mobile_number
    date_birth == "" ? date_birth = null : date_birth
    let senha = document.querySelector("#senha").value
    let confirm_senha = document.querySelector("#confirm_senha").value
    let image = document.querySelector('#fileInput').files[0]
    console.log(image)
    if (senha != confirm_senha) {
        Swal.fire({
            icon: "error",
            title: "Senhas não coincidem!",
            draggable: true
          });
        return;
    }
    let infoUser = {"first_name": first_name, "last_name": last_name, "email": email, "date_birth": date_birth, "mobile_number": mobile_number, "senha": senha}

    fetch("/settings/update", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(infoUser)
    })
    .then(data => {
        if (data.status == 200) {
            Swal.fire({
                icon: "success",
                title: "Success Update!",
                draggable: true
              });
            document.querySelector("#btn-edit").style.display = "none"
            document.querySelector("#edit-button").style.display = "block"
            document.querySelectorAll("input").forEach(input => {
                input.style.pointerEvents = "all";
                document.querySelector('#field-image').style.pointerEvents = "none";
                input.style.border = "1px solid var(--gray-5)";
            });
        }
        else {
            Swal.fire({
                icon: "error",
                title: "Error!",
                draggable: true
              });
        }

})
    .catch(error => console.error("Erro na requisição:", error));
})

document.querySelector("#field-image").addEventListener('click', () => {
    const fileInput = document.getElementById("fileInput");
    const previewImage = document.getElementById("previewImage");
    fileInput.click();
    fileInput.addEventListener("change", (event) => {
        const file = event.target.files[0]; // Pega o arquivo selecionado
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                previewImage.src = e.target.result; // Define o novo src da imagem
            };
            reader.readAsDataURL(file);
        }
    });
})