import random
import time
import gradio as gr
from dotenv import load_dotenv
from chatbot_engine import chat
import os

from langchain.memory import ChatMessageHistory

## エラーが出たので追加
import matplotlib
matplotlib.use('Agg')

# 履歴をもとに会話をする関数
def respond(message, chat_history):
    history = ChatMessageHistory()
    for [user_message, ai_message] in chat_history:
        history.add_user_message(user_message)
        history.add_ai_message(ai_message)

    bot_message = chat(message, history)
    chat_history.append((message, bot_message))
    return "", chat_history

# ただ会話をするだけの関数
# def respond(message, chat_history):
#     bot_message = chat(message)
#     chat_history.append((message, bot_message))
#     time.sleep(1)
#     return "", chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)


if __name__ == "__main__":
    load_dotenv()

    app_env = os.environ.get("APP_ENV", "production")
    if app_env == "production":
        username = os.environ["GRADIO_USERNAME"]
        password = os.environ["GRADIO_PASSWORD"]
        auth = (username, password)
    else:
        auth = None
    demo.launch(share=True)

