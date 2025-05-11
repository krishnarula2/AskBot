AskBot is an AI-powered chatbot designed to serve **local businesses** by answering **customer inquiries in real time**, directly through a clean, intuitive web interface. It mimics the responsiveness of platforms like ChatGPT or Drift, allowing business owners to engage with customers even when offline.

Whether it's answering questions about business hours, services offered, or contact info, AskBot provides a highly customizable solution that's **simple to deploy** and **visually polished** — perfect for showcasing on personal portfolios or as a production-ready tool.


##💡 Why AskBot?

Local businesses often lack the time or resources to implement AI solutions. AskBot provides:

- ✅ An always-online assistant
- ✅ Instant answers to FAQs
- ✅ Aesthetic, mobile-first UI inspired by modern chat apps
- ✅ Server-side logic using Django
- ✅ Integration with large language models (LLMs) like Together AI or OpenAI

> 🧠 It’s not just a chatbot — it’s a customer-facing virtual employee.

---

## ✨ Features

- 🔮 **GPT-like experience** with real-time Q&A
- 💬 Styled messages with chat bubbles and animation
- 🟪 Sleek purple-and-white design + responsive layout
- 💻 Built with Django backend & HTML/CSS/JS frontend
- 🔐 Secure `.env` usage to protect your API keys
- 📄 Customizable FAQ database (via Django ORM)

---

## 📦 Tech Stack

| Tech      | Role                          |
|-----------|-------------------------------|
| Django    | Backend framework             |
| JavaScript | Frontend logic + animations  |
| HTML/CSS  | UI layout & styling           |
| Together AI or OpenAI | AI language model |
| SQLite    | Local database                |
| Python-dotenv | Loads secure API keys     |

---

## ⚙️ Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/askbot.git
   cd askbot

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install your dependencies
pip install -r requirements.txt

4. Create your .env file
Add your API key:
TOGETHER_API_KEY=your_key_here

5. Run the development server:
python manage.py runserver

6. Visit the chatbot:
Navigate to http://127.0.0.1:8000/ in your browser.
-------------------------------------------------------------

🧠 AI Behavior
AskBot uses prompt engineering to understand user intent and respond in a friendly, business-appropriate tone. It can:

Handle business-related FAQs

Respond to customer greetings

Escalate issues (e.g., “please contact us at…”)

Simulate fallback replies for unknown questions

You can switch between using mock responses or real LLM replies by modifying views.py.

🔐 Environment Setup
Make sure your .env file is excluded from GitHub:
# .gitignore
.env
__pycache__/
db.sqlite3

💼 Use Cases
Coffee shops, gyms, salons, or dental clinics

Small businesses needing 24/7 FAQ handling

Student portfolios showing full-stack AI integration

Hackathons or rapid MVP builds

🙌 Credits
Together.ai for their accessible free-tier LLMs

OpenAI for foundational API structure

ChatGPT UI inspiration

Designed & built by Krish Narula


