document.addEventListener('DOMContentLoaded', function () {
    const hamburgerMenu = document.getElementById('hamburger-menu');
    const headerMenu = document.querySelector('.header-menu');

    hamburgerMenu.addEventListener('click', function () {
        headerMenu.classList.toggle('show');
    });
});

async function enviarFormulario() {
    console.log("Iniciando envio do formulário");

    const formData = new FormData();
    formData.append("nome", document.getElementById("nome").value);
    formData.append("email", document.getElementById("email").value);
    formData.append("telemovel", document.getElementById("telemovel").value);
    formData.append("data", document.getElementById("data").value);
    formData.append("mensagem", document.getElementById("mensagem").value);

    console.log("Dados do formulário:", {
        nome: document.getElementById("nome").value,
        email: document.getElementById("email").value,
        telemovel: document.getElementById("telemovel").value,
        data: document.getElementById("data").value,
        mensagem: document.getElementById("mensagem").value,
    });

    try {
        const response = await fetch("/enviar-email/", {
            method: "POST",
            body: formData,
        });

        console.log("Resposta do servidor:", response);

        if (!response.ok) {
            throw new Error(`Erro HTTP! status: ${response.status}`);
        }

        const result = await response.json();
        console.log("Resultado da API:", result);
        alert(result.message);
    } catch (error) {
        console.error("Erro ao enviar o formulário:", error);
        alert(`Erro ao enviar o formulário: ${error.message}`);
    }
}

