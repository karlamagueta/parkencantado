document.addEventListener("DOMContentLoaded", function () {
  const hamburgerMenu = document.getElementById("hamburger-menu");
  const headerMenu = document.querySelector(".header-menu");

  hamburgerMenu.addEventListener("click", function () {
    headerMenu.classList.toggle("show");
  });
});

// whatsapp notificação
const whatsappIcon = document.querySelector('.whatsapp-fixo');

whatsappIcon.addEventListener('click', () => {
  whatsappIcon.classList.add('clicked');
});

//form

async function enviarFormulario(suffix = "") {
  console.log("Iniciando envio do formulário");
  const nome = document.getElementById(`nome${suffix}`).value;
  const email = document.getElementById(`email${suffix}`).value;
  const telemovel = document.getElementById(`telemovel${suffix}`).value;
  const mensagem = document.getElementById(`mensagem${suffix}`).value;

  if (!nome || !email || !telemovel || !mensagem) {
    alert("Todos os campos são obrigatórios!");
    throw new Error("Required fields are missing");
  }

  const formData = new FormData();
  formData.append("nome", nome);
  formData.append("email", email);
  formData.append("telemovel", telemovel);
  formData.append("mensagem", mensagem);

  const data = document.getElementById(`data${suffix}`);
  if (data) {
    formData.append("data", data.value);
  }

  formData.forEach((value, key) => {
    console.log(`${key}: ${value}`);
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

    // clean all inputs on success
    const inputs = document.querySelectorAll(`.emailform${suffix} input, .emailform${suffix} textarea`);
    inputs.forEach(input => {
      input.value = '';
    });

    const sucesso = document.getElementById(`sucesso${suffix}`);
    sucesso.style.display = "inline";
    sucesso.innerText = result.message;

  } catch (error) {
    console.error("Erro ao enviar o formulário:", error);
    alert(`Erro ao enviar o formulário: ${error.message}`);
  }
}

// Fotos

const fotos = document.querySelectorAll(".foto");
const overlay = document.getElementById("overlay");
const imgAmpliada = document.getElementById("imgAmpliada");
const closeBtn = document.getElementById("close-btn");
const prevBtn = document.getElementById("prev-btn");
const nextBtn = document.getElementById("next-btn");

let currentIndex = 0;

// Mapeia as imagens menores para suas respectivas versões maiores
const imagensMaiores = [
  '/static/img/IMG_0885.jpg', // imagem correspondente à espaco_1_small.png
  '/static/img/IMG_0890.jpg', // imagem correspondente à espaco_2_small.png
  '/static/img/IMG_0917.jpg', // imagem correspondente à espaco_3_small.png
  '/static/img/IMG_0987.jpg', // imagem correspondente à espaco_4_small.png
  '/static/img/IMG_0956.jpg', // imagem correspondente à espaco_5_small.png
  '/static/img/IMG_0997.jpg'  // imagem correspondente à espaco_6_small.png
];

function updateImage() {
  imgAmpliada.src = imagensMaiores[currentIndex]; // Atualiza para a imagem maior
}

fotos.forEach((foto, index) => {
  foto.addEventListener("click", () => {
    currentIndex = index;
    updateImage();
    overlay.classList.add("active");
  });
});

prevBtn.addEventListener("click", () => {
  currentIndex--;
  if (currentIndex < 0) {
    currentIndex = fotos.length - 1;
  }
  updateImage();
});

nextBtn.addEventListener("click", () => {
  currentIndex++;
  if (currentIndex >= fotos.length) {
    currentIndex = 0;
  }
  updateImage();
});

closeBtn.addEventListener("click", () => {
  overlay.classList.remove("active");
});

overlay.addEventListener("click", (event) => {
  if (event.target === overlay) {
    overlay.classList.remove("active");
  }
});


// Cards de depoimentos


document.addEventListener("DOMContentLoaded", function () {
  const cardWrapper = document.querySelector('.card--carrossel');
  const cards = document.querySelectorAll('.review-card');
  const prevButton = document.querySelector('.carousel-prev');
  const nextButton = document.querySelector('.carousel-next');
  const cardWidth = cards[0].offsetWidth + 20; // Largura do card + margem
  let currentIndex = 0;
  const visibleCards = 4; // Quantidade de cards visíveis

  // Função para atualizar a posição do carrossel
  function updateCarouselPosition() {
      cardWrapper.style.transform = `translateX(-${currentIndex * cardWidth}px)`;
  }

  // Avançar no carrossel
  nextButton.addEventListener('click', function () {
      currentIndex++;
      if (currentIndex > cards.length - visibleCards) {
          currentIndex = 0; // Volta para o início se ultrapassar
      }
      updateCarouselPosition();
  });

  // Voltar no carrossel
  prevButton.addEventListener('click', function () {
      currentIndex--;
      if (currentIndex < 0) {
          currentIndex = cards.length - visibleCards; // Vai para o final se ultrapassar
      }
      updateCarouselPosition();
  });

  // Modal para "Leia mais"
  const readMoreButtons = document.querySelectorAll('.read-more');
  const modalOverlay = document.getElementById('modal-overlay');
  const modalText = document.getElementById('modal-text');
  const modalReviewer = document.getElementById('modal-reviewer');
  const closeModal = document.getElementById('close-modal');

  readMoreButtons.forEach((button) => {
      button.addEventListener('click', function () {
          const card = this.parentElement;
          const fullText = card.querySelector('.full-text').innerText;
          const reviewerName = card.querySelector('.reviewer-name').innerText;

          modalText.innerText = fullText;
          modalReviewer.innerText = reviewerName;

          modalOverlay.classList.add('active');
      });
  });

  closeModal.addEventListener('click', function () {
      modalOverlay.classList.remove('active');
  });

  modalOverlay.addEventListener('click', function (e) {
      if (e.target === modalOverlay) {
          modalOverlay.classList.remove('active');
      }
  });
});
