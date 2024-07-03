from fastapi import FastAPI
from transformers import AutoTokenizer
import torch
import numpy as np

# モデルの読み込み
model = torch.load('model.pt')
model.eval()

# 使用するモデルを指定して、Tokenizerを読み込む
checkpoint = 'cl-tohoku/bert-base-japanese-whole-word-masking'
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

# エラーメッセージ
error_bad_data = {"message": "クエリが不正です。入力テキストはカンマ区切りで30件まで処理できます。詳しくは入力例をご覧ください。", 
            "example": "http://shiratori.cdl.im.dendai.ac.jp/emotion_analysis?text=おはよう！今日はいい天気だね！,今日は疲れた。帰ろう"}

# 感情ラベル
emotion_names_jp = ['Joy', 'Sadness', 'Anticipation', 'Surprise', 'Anger', 'Fear', 'Disgust', 'Trust']

# アプリ本体
app = FastAPI()

# ソフトマックス関数
def np_softmax(x):
    f_x = np.exp(x) / np.sum(np.exp(x))
    return f_x

# 感情分析
def sentiment_analysis(text: str) -> dict:
    # 入力データ変換 + 推論
    tokens = tokenizer(text, truncation=True, return_tensors="pt")
    tokens.to(model.device)
    preds = model(**tokens)
    prob = np_softmax(preds.logits.cpu().detach().numpy()[0])
    out_dict = {n: str(p) for n, p in zip(emotion_names_jp, prob)}

    return out_dict

@app.get("/")
def result(text: str):
    try:
        text_list = text.split(",")
        return {"responce": [{"text": t, "emotion_score": sentiment_analysis(t)} for t in text_list if len(t) > 0]}
    except Exception:
        return {"responce": {"status": "error", "message": "クエリが不正です。入力例を参照してください。"}}