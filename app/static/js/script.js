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

// Carrossel Espaço

let currentIndex = 0;
let autoSlideInterval;

// Função para exibir o slide
function showSlide(index) {
  const carrossel = document.querySelector('.carrossel');
  const totalSlides = document.querySelectorAll('.carrossel-item').length;

  if (index >= totalSlides) {
    currentIndex = 0;
  } else if (index < 0) {
    currentIndex = totalSlides - 1;
  } else {
    currentIndex = index;
  }

  carrossel.style.transform = `translateX(-${currentIndex * 100}%)`;
}

// Função para iniciar o auto-slide
function startAutoSlide() {
  autoSlideInterval = setInterval(() => {
    showSlide(currentIndex + 1);
  }, 2500); // 15 segundos para trocar a imagem
}

// Função para parar o auto-slide
function stopAutoSlide() {
  clearInterval(autoSlideInterval);
}

// Próximo slide
document.querySelector('.next').addEventListener('click', function () {
  stopAutoSlide(); // Para o auto-slide quando o usuário clica
  showSlide(currentIndex + 1);
  startAutoSlide(); // Reinicia o auto-slide após a interação
});

// Slide anterior
document.querySelector('.prev').addEventListener('click', function () {
  stopAutoSlide();
  showSlide(currentIndex - 1);
  startAutoSlide();
});

// Inicia o auto-slide ao carregar a página
window.addEventListener('load', function () {
  startAutoSlide();
});