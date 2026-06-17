# 🚀 AI Prompt Library

AI Prompt Library is a lightweight, modern **Full-Stack** web application designed to store, organize, and track usage statistics of your effective prompts used with AI models (such as ChatGPT, Claude, Midjourney, etc.).

The project is built using **Flask (Python)** on the backend, and **HTML5, JavaScript (Fetch API)** along with the latest **Tailwind CSS v4** on the frontend.

---

## ✨ Features

* **Add Prompts:** Easily expand your library by entering a title, category, description, and the prompt text.
* **Dynamic Listing:** View all your saved prompts instantly without refreshing the page.
* **Usage Tracking:** Track how many times you have used a specific prompt with the `⚡ Use and Increase Counter` button.
* **Auto-Copy to Clipboard:** Clicking the button automatically copies the prompt text to your clipboard, allowing you to instantly paste it into your AI model.
* **Modern Dark Theme:** A sleek, eye-friendly, and fully responsive (mobile-friendly) interface.

---

## 🛠️ Technologies Used

* **Backend:** Python 3.x, Flask
* **Frontend:** HTML5, Modern JavaScript (ES6+ Async/Await)
* **Styling:** Tailwind CSS v4 (via CDN)

---

## 📁 Project Structure

```text
ai-prompt-library/
│
├── main.py              # Flask Backend (API Endpoints & Server)
├── templates/
│   └── index.html       # Single Page Application Interface & JS Scripts
└── README.md            # Project Documentation
```

---

## ⚙️ Installation & Local Setup

Follow these steps to run the Digital Wallet platform locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/onurcanbircan/ai-prompt-library.git](https://github.com/onurcanbircan/ai-prompt-library.git)
   cd flask-digital-wallet
   ```

---

2. **Create and activate a virtual environment:**
```bash
python -m venv venv
```
- ###  On Windows:
```bash
venv\Scripts\activate
```
- ### On macOS/Linux:
```bash
source venv/bin/activate
```

---

3. **Install dependencies:**
```bash
pip install Flask Flask-SQLAlchemy
```
4. **Run the application:**
```bash
python main.py
```
---
Open http://127.0.0.1:5000 in your browser to access the dashboard.
