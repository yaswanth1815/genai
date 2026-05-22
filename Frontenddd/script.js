const newChatButton = document.getElementById("newChatButton");
const recentList = document.getElementById("recentList");
const attachButton = document.getElementById("attachButton");
const fileInput = document.getElementById("fileInput");
const fileChip = document.getElementById("fileChip");
const chatForm = document.getElementById("chatForm");
const questionInput = document.getElementById("questionInput");
const chatWindow = document.getElementById("chatWindow");
const themeToggle = document.getElementById("themeToggle");
const themeIcon = document.getElementById("themeIcon");
const fontSizeSelect = document.getElementById("fontSizeSelect");

let selectedFiles = [];
let chats = [];
let activeChatId = "";

loadTheme();
loadFontSize();
loadChats();
renderRecentChats();
renderActiveChat();

newChatButton.addEventListener("click", createNewChat);
attachButton.addEventListener("click", () => fileInput.click());

themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
  const theme = document.body.classList.contains("dark-mode") ? "dark" : "light";
  localStorage.setItem("theme", theme);
  updateThemeButton(theme);
});

fontSizeSelect.addEventListener("change", () => {
  setFontSize(fontSizeSelect.value);
  localStorage.setItem("fontSize", fontSizeSelect.value);
});

fileInput.addEventListener("change", () => {
  selectedFiles = [...selectedFiles, ...Array.from(fileInput.files)];
  renderFiles();
  fileInput.value = "";
});

chatForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const question = questionInput.value.trim();
  if (!question) return;

  addMessage("user", "You", question, true);
  questionInput.value = "";

  setTimeout(() => {
    addMessage("assistant", "AI", createDemoAnswer(question), true);
  }, 500);
});

function createNewChat() {
  const chat = createChat();
  chats.unshift(chat);
  activeChatId = chat.id;
  selectedFiles = [];
  renderFiles();
  saveChats();
  renderRecentChats();
  renderActiveChat();
  questionInput.focus();
}

function createChat() {
  return {
    id: `chat-${Date.now()}-${Math.random().toString(16).slice(2)}`,
    title: "New chat",
    updatedAt: Date.now(),
    messages: [
      {
        type: "assistant",
        name: "AI",
        text: "Hello! Add your files using the plus button, or ask a general question."
      }
    ]
  };
}

function loadChats() {
  const savedChats = JSON.parse(localStorage.getItem("recentChats") || "[]");
  chats = savedChats.length > 0 ? savedChats : [createChat()];
  activeChatId = localStorage.getItem("activeChatId") || chats[0].id;

  if (!chats.some((chat) => chat.id === activeChatId)) {
    activeChatId = chats[0].id;
  }
}

function saveChats() {
  localStorage.setItem("recentChats", JSON.stringify(chats));
  localStorage.setItem("activeChatId", activeChatId);
}

function getActiveChat() {
  return chats.find((chat) => chat.id === activeChatId) || chats[0];
}

function renderActiveChat() {
  const chat = getActiveChat();
  chatWindow.innerHTML = "";
  chat.messages.forEach((message) => {
    addMessage(message.type, message.name, message.text);
  });
}

function renderRecentChats() {
  recentList.innerHTML = "";

  if (chats.length === 0) {
    recentList.innerHTML = '<div class="empty-recent">No recent chats</div>';
    return;
  }

  chats.forEach((chat) => {
    const item = document.createElement("div");
    item.className = `recent-chat${chat.id === activeChatId ? " active" : ""}`;
    item.innerHTML = `
      <button class="recent-chat-main" type="button">
        <span class="recent-title">${escapeHtml(chat.title)}</span>
        <span class="recent-time">${formatTime(chat.updatedAt)}</span>
      </button>
      <button class="delete-chat-button" type="button" aria-label="Delete chat">x</button>
    `;

    item.querySelector(".recent-chat-main").addEventListener("click", () => {
      activeChatId = chat.id;
      localStorage.setItem("activeChatId", activeChatId);
      renderRecentChats();
      renderActiveChat();
    });

    item.querySelector(".delete-chat-button").addEventListener("click", () => {
      deleteChat(chat.id);
    });

    recentList.appendChild(item);
  });
}

function deleteChat(chatId) {
  chats = chats.filter((chat) => chat.id !== chatId);

  if (chats.length === 0) {
    chats = [createChat()];
  }

  if (activeChatId === chatId) {
    activeChatId = chats[0].id;
  }

  saveChats();
  renderRecentChats();
  renderActiveChat();
}

function renderFiles() {
  if (selectedFiles.length === 0) {
    fileChip.textContent = "No files";
    return;
  }

  const latestFile = selectedFiles[selectedFiles.length - 1];
  const countText = selectedFiles.length === 1 ? "1 file" : `${selectedFiles.length} files`;
  fileChip.textContent = `${countText}: ${latestFile.name}`;
}

function addMessage(type, name, text, shouldSave = false) {
  const message = document.createElement("div");
  message.className = `message ${type}`;

  message.innerHTML = `
    <div class="avatar">${name === "You" ? "U" : "AI"}</div>
    <div class="bubble">${escapeHtml(text)}</div>
  `;

  chatWindow.appendChild(message);
  chatWindow.scrollTop = chatWindow.scrollHeight;

  if (shouldSave) {
    const chat = getActiveChat();
    chat.messages.push({ type, name, text });

    if (chat.title === "New chat" && type === "user") {
      chat.title = text.length > 32 ? `${text.slice(0, 32)}...` : text;
    }

    chat.updatedAt = Date.now();
    saveChats();
    renderRecentChats();
  }
}

function createDemoAnswer(question) {
  if (selectedFiles.length === 0) {
    return `General answer mode: I can reply even without documents. You asked: "${question}". Later, this can connect to your AI model for real answers.`;
  }

  return `Document answer mode: I found ${selectedFiles.length} uploaded file(s). Later, your backend can search Pinecone using your question and show the best answer here.`;
}

function loadTheme() {
  const savedTheme = localStorage.getItem("theme") || "light";
  document.body.classList.toggle("dark-mode", savedTheme === "dark");
  updateThemeButton(savedTheme);
}

function updateThemeButton(theme) {
  const isDark = theme === "dark";
  themeIcon.textContent = isDark ? "Dark" : "Light";
  themeToggle.setAttribute(
    "aria-label",
    isDark ? "Switch to light mode" : "Switch to dark mode"
  );
}

function loadFontSize() {
  const savedSize = localStorage.getItem("fontSize") || "medium";
  fontSizeSelect.value = savedSize;
  setFontSize(savedSize);
}

function setFontSize(size) {
  const sizes = {
    small: "14px",
    medium: "16px",
    large: "18px"
  };

  document.documentElement.style.setProperty(
    "--app-font-size",
    sizes[size] || sizes.medium
  );
}

function formatTime(timestamp) {
  return new Date(timestamp).toLocaleString([], {
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit"
  });
}

function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}
