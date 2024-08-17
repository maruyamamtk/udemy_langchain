import langchain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ChatMessageHistory
from langchain.schema import HumanMessage

langchain.verbose = True

def chat(message: str, history: ChatMessageHistory) -> str:
    # モデルの用意
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    # 過去の会話の履歴を取得
    messages = history.messages
    # 新しいユーザーのメッセージを履歴に追加
    messages.append(HumanMessage(content=message))

    # 履歴も加味してユーザーの質問に回答
    return llm(messages).content

# テスト用
# def chat(message: str) -> str:
#     return f"hello! you said: {message}"