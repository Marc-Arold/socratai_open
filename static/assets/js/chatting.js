const msgerForm = get(".msger-inputarea");
const msgerInput = get(".msger-input");
const msgerChat = get(".msger-chat");

const BOT_IMG = "../../assets/images/icons/pro1.png";
const PERSON_IMG = "../../assets/images/icons/profile.png";
const BOT_NAME = "BOT";
const PERSON_NAME = "Kristin Williams";

// var chatMessageUrl = document.body.getAttribute("data-message-url");

// msgerForm.addEventListener("submit", (event) => {
//   event.preventDefault();

//   const msgText = msgerInput.value;
//   if (!msgText) return;

//   appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
//   msgerInput.value = "";

//   // Supprimez botResponse et remplacez par un appel AJAX pour obtenir la réponse du bot
//   getBotResponse(msgText);

//   const nochat = document.querySelector(".no-chat");
//   nochat.classList.add("d-none");
// });

document.addEventListener("DOMContentLoaded", function () {
  var deleteButton = document.querySelector(".del-btn");

  deleteButton.addEventListener("click", function () {
    localStorage.clear(); // Clears all data in local storage
    window.location.reload(); // Reloads the current page
  });
});

function appendMessage(name, img, side, text, isHtml = false) {
  const msgContainer = document.createElement("div");
  msgContainer.classList.add("msg", `msg-${side}`);

  const imgElement = document.createElement("img");
  imgElement.src = img;
  imgElement.alt = name;
  imgElement.classList.add("msg-img");

  const textElement = document.createElement("div");
  textElement.classList.add("msg-text");

  // Insère le contenu en HTML ou en texte brut selon le paramètre isHtml
  if (isHtml) {
    textElement.innerHTML = text; // Utilise innerHTML si le contenu est déjà en HTML
  } else {
    textElement.textContent = text; // Utilise textContent pour du texte brut
  }

  msgContainer.appendChild(imgElement);
  msgContainer.appendChild(textElement);

  document.querySelector(".msger-chat").appendChild(msgContainer);
  document.querySelector(".msger-chat").scrollTop =
    document.querySelector(".msger-chat").scrollHeight;
}

function appendMessage(name, img, side, text) {
  // Solution simple pour les petites applications
  const msgHTML = `
    <div class="msg ${side}-msg">
      <div class="msg-bubble">
            <div class="msg-text">${text}</div>
      </div>
    </div>
  `;

  msgerChat.insertAdjacentHTML("beforeend", msgHTML);
  msgerChat.scrollTop += 500;
  saveMessages();
}

// Fonction pour obtenir la réponse du bot de Django
// function getBotResponse(message) {
//   // Préparez les données à envoyer
//   showTypingIndicator();
//   const data = new FormData();
//   data.append("user_message", message);
//   const csrftoken = getCookie("csrftoken");

//   // Faites une requête POST à Django
//   fetch(chatMessageUrl, {
//     method: "POST",
//     body: JSON.stringify({ user_message: message }),
//     headers: {
//       "Content-Type": "application/json",
//       "X-CSRFToken": csrftoken, // Ajoutez le token CSRF ici
//     },
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       // Utilisez la réponse du bot pour afficher un nouveau message
//       document.getElementById("loadingMessage").remove();
//       appendMessage(BOT_NAME, BOT_IMG, "left", data.response_text);
//     })
//     .catch((error) => {
//       document.getElementById("loadingMessage").remove();
//       appendMessage(
//         BOT_NAME,
//         BOT_IMG,
//         "left",
//         "Il y a eu une erreur, veuillez réessayer"
//       );
//     });
// }

function showTypingIndicator() {
  const loadingHTML = `
    <div class="msg left-msg" id="loadingMessage">
      <div class="msg-bubble">
        <div class="msg-text">
          <span class="dot dot1">.</span><span class="dot dot2">.</span><span class="dot dot3">.</span>
        </div>
      </div>
    </div>
  `;

  msgerChat.insertAdjacentHTML("beforeend", loadingHTML);
  msgerChat.scrollTop += 500;
}

// Fonction utilitaire pour obtenir le cookie CSRF de Django
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Utils
function get(selector, root = document) {
  return root.querySelector(selector);
}

function formatDate(date) {
  const h = "0" + date.getHours();
  const m = "0" + date.getMinutes();

  return `${h.slice(-2)}:${m.slice(-2)}`;
}

function random(min, max) {
  return Math.floor(Math.random() * (max - min) + min);
}

function saveMessages() {
  const messagesHTML = document.querySelector(".msger-chat").innerHTML;
  localStorage.setItem("chatMessages", messagesHTML);
}

function loadMessages() {
  const messages = localStorage.getItem("chatMessages");
  if (messages) {
    document.querySelector(".msger-chat").innerHTML = messages;
  }
}

document.addEventListener("DOMContentLoaded", function () {
  loadMessages(); // Charge les messages sauvegardés dès que le DOM est complètement chargé
});
