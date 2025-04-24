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

### ✅ Cách 1: Dành cho người dùng Git: Clone project

```bash
git clone https://github.com/baongongo147/chatbotLLM.git
cd chatbot-openrouter
```

### 📁 Cách 2: Dành cho người KHÔNG sử dụng Git

1. Truy cập: https://github.com/baongongo147/chatbotLLM
2. Nhấn **Code → Download ZIP**
3. Giải nén file `.zip`
4. Mở Terminal (CMD hoặc PowerShell), chuyển vào thư mục giải nén:

```bash
cd Downloads/chatbot-openrouter-main
```

## (Tùy chọn) Tạo môi trường ảo
```bash
python -m venv venv
```
### Kích hoạt môi trường ảo
Windows
```bash
venv\Scripts\activate
```
macOS/Linux
```bash
source venv/bin/activate
```

# Cài thư viện
```bash
pip install -r requirements.txt
```

---

## Download file chứa API key và thay thế vào trong code

Link tải file chứa API key: [https://drive.google.com/file/d/1z1w226yf0uWANttXl17FbwwrCVG-wZ3_/view?usp=sharing]
Sau khi tải file về thì copy nội dung dán vào thay thế API key hiện tại trong code
### ⚠️ Lưu ý: Không được public API key lên Internet, nếu API key bị public lên Internet thì sẽ mất hiệu lực
Ngoài ra cũng có thể truy cập [https://openrouter.ai/settings/keys] để tạo API key riêng 

---

## 🚀 Chạy chương trình

```bash
python main.py
```

Ứng dụng sẽ mở ở địa chỉ: [http://localhost:8888](http://localhost:8888)

---

## 📝 Tính năng chính

- 💬 Chatbot AI: Trò chuyện với mô hình GPT-3.5-turbo qua OpenRouter
- 📄 Tóm tắt bài viết: Gửi URL báo/blog để được tóm tắt nội dung
- 🕵️‍♂️ Tìm kiếm sự kiện: Gõ câu hỏi có chứa từ “sự kiện” hoặc “mới nhất”

---

## 🚀 Demo

[https://drive.google.com/file/d/19LYQBKLzs6sFb0ccnI0JPb0OdBgF_-6Z/view?usp=sharing]

---


