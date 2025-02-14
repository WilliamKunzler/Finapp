requestAnimationFrame(() => {
    if(window.location.pathname == '/settings/') {
        fetch("/settings/loadDetails")
        .then(response => response.json())
        .then(data => {
                let image = document.getElementById('previewImage');
                document.getElementById('first_name').value = data.data[0]['first_name']
                document.getElementById('last_name').value = data.data[0]['last_name']
                document.getElementById('date_birth').value = data.data[0]['date_birth']
                document.getElementById('mobile_number').value = data.data[0]['mobile_number']
                document.getElementById('email').value = data.data[0]['email']
                document.getElementById('senha').value = data.data[0]['senha']
                document.getElementById('confirm_senha').value = data.data[0]['senha']

                data.data[0]['image'] == "" ? image.src = "../static/assets/userDefault.png" : image.src = 'data:image/jpeg;base64,' + data.data[0]['image']
            });
            }
    
})

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
    if (!image) {
        if (document.querySelector('#previewImage').src != '../static/assets/userDefault.png') {
            image = null
        }
    } 

    let formData = new FormData();
    formData.append("first_name", first_name);
    formData.append("last_name", last_name);
    formData.append("email", email);
    formData.append("date_birth", date_birth);
    formData.append("mobile_number", mobile_number);
    formData.append("senha", senha);
    formData.append("image", image); // Adiciona a imagem ao FormData
    


    if (senha != confirm_senha) {
        Swal.fire({
            icon: "error",
            title: "Senhas não coincidem!",
            draggable: true
          });
        return;
    }

    fetch("/settings/update", {
        method: "POST",
        body: formData
    })
    .then(data => {
        if (data.status == 200) {
            Swal.fire({
                icon: "success",
                title: "Success Update!",
                draggable: true
                }).then(() => {
                    location.reload();
              });
            document.querySelector("#btn-edit").style.display = "none"
            document.querySelector("#edit-button").style.display = "block"
            document.querySelectorAll("input").forEach(input => {
                input.style.pointerEvents = "none";
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