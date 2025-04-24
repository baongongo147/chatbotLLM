import openai
import gradio as gr
from newspaper import Article
from duckduckgo_search import DDGS 

# Khai báo API key OpenRouter
openai.api_key = "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"  # Thay API key
openai.api_base = "https://openrouter.ai/api/v1"

# hàm sử dụng để tóm tắt bài viết từ link
def summarize_article_from_url(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text[:3000]  # Giới hạn độ dài để tránh lỗi quá token

        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Bạn là trợ lý AI có thể tóm tắt bài viết."},
                {"role": "user", "content": f"Tóm tắt nội dung sau:\n{text}"}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Lỗi khi xử lý link: {str(e)}"

# hàm sử dụng để tìm kiếm sự kiện mới nhất
def search_latest_event(query):
    try:
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=3):
                results.append(f"- [{r['title']}]({r['href']})")
        return "\n".join(results) if results else "Không tìm thấy kết quả."
    except Exception as e:
        return f"Lỗi tìm kiếm: {str(e)}"

# Hàm xử lý tin nhắn từ người dùng và trả lời từ bot
def chat_with_bot(message, history):
    history = history or []
    messages = [{"role": "system", "content": "Bạn là một trợ lý AI thân thiện và hiểu biết."}]
    for user_msg, bot_reply in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": bot_reply})

    # Nếu người dùng gửi link
    if message.startswith("http://") or message.startswith("https://"):
        reply = summarize_article_from_url(message)
        yield reply
        return

    # Nếu nhập từ khóa là "tìm kiếm" hoặc "sự kiện" thì sẽ tìm kiếm sự kiện mới nhất
    if "sự kiện" in message.lower() or "mới nhất" in message.lower():
        reply = search_latest_event(message)
        yield reply
        return

    # tạo message cho bot
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="openai/gpt-3.5-turbo",
        messages=messages,
        stream=True
    )

    full_reply = ""
    for chunk in response:
        if "choices" in chunk and "delta" in chunk["choices"][0]:
            delta = chunk["choices"][0]["delta"]
            if "content" in delta:
                full_reply += delta["content"]
                yield full_reply

# Giao diện Gradio
gr.ChatInterface(fn=chat_with_bot).launch(server_port=8888)
