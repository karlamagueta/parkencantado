document.addEventListener("DOMContentLoaded", function () {
  const hamburgerMenu = document.getElementById("hamburger-menu");
  const headerMenu = document.querySelector(".header-menu");

  hamburgerMenu.addEventListener("click", function () {
    headerMenu.classList.toggle("show");
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

// Ampliacao de fotos da galeria
// Seleciona os elementos necessários
const fotos = document.querySelectorAll('.foto');
const overlay = document.getElementById('overlay');
const imgAmpliada = document.getElementById('imgAmpliada');
const closeBtn = document.getElementById('close-btn');

// Adiciona eventos de clique às imagens
fotos.forEach(foto => {
    foto.addEventListener('click', () => {
        imgAmpliada.src = foto.src; // Define a imagem ampliada
        overlay.classList.add('active'); // Mostra o overlay
    });
});

// Fecha a imagem ampliada ao clicar no botão ou fora da imagem
closeBtn.addEventListener('click', () => {
    overlay.classList.remove('active'); // Esconde o overlay
});

// Fecha o overlay ao clicar fora da imagem ampliada
overlay.addEventListener('click', () => {
    overlay.classList.remove('active'); // Esconde o overlay
});