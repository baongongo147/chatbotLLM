# chatbotLLM
# 🤖 Chatbot AI với OpenRouter, Gradio, Newspaper3k và DuckDuckGo

Một chatbot thông minh sử dụng GPT-3.5-Turbo qua OpenRouter, có khả năng:
- 💬 Trả lời hội thoại tự nhiên
- 📰 Tóm tắt bài viết từ URL
- 🔍 Tìm kiếm sự kiện mới nhất bằng DuckDuckGo
- 🌐 Giao diện người dùng đơn giản qua Gradio

---

## 📦 Yêu cầu

- Python 3.11
- Các thư viện: `openai`, `gradio`, `newspaper3k`, `duckduckgo-search`

---

## 🔧 Cài đặt

### ✅ Cách 1: Dành cho người dùng Git

```bash
# 1. Clone project
git clone https://github.com/your-username/chatbot-openrouter.git
cd chatbot-openrouter
```

### 📁 Cách 2: Dành cho người KHÔNG sử dụng Git

1. Truy cập: [https://github.com/your-username/chatbot-openrouter](https://github.com/baongongo147/chatbotLLM)
2. Nhấn **Code → Download ZIP**
3. Giải nén file `.zip`
4. Mở Terminal (CMD hoặc PowerShell), chuyển vào thư mục giải nén:

```bash
cd Downloads/chatbot-openrouter-main
```

# 2. (Tùy chọn) Tạo môi trường ảo
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. Cài thư viện
pip install -r requirements.txt
