# 知的処理及び演習_感情分析API

[WRIMEデータセット](https://github.com/ids-cv/wrime)を学習した、正解率70%くらいのBERTモデルをAPIから利用できます。  
感情ラベルは以下の通りで、総和が1に正規化された感情値を返します。
|Joy|Sadness|Anticipation|Surprise|Anger|Fear|Disgust|Trust|
|----|----|----|----|----|----|----|----|
|喜び|悲しみ|期待|驚き|怒り|恐れ|嫌悪|信頼|

## 使い方
**必ず学内LAN or VPNから利用してください。**  
text属性に、分析したいテキストをカンマ区切りで入力します。  
2,000文字くらいが限界なので適当に調節してください。  

#### エンドポイント
```
http://shiratori.cdl.im.dendai.ac.jp:50000/
```
  
#### リクエスト例
```
http://shiratori.cdl.im.dendai.ac.jp:50000/?text=曲は素晴らしい、何回も...,Androidにくらべると画面は大きくなりましたが、文字は...
```


#### レスポンス例
```
{
    "responce": [
        {
            "text": "曲は素晴らしい、何回も聴いてるストーリーはまあベタな感じだけど嫌いじゃない",
            "emotion_score": {
                "Joy": "0.8092415",
                "Sadness": "0.014647802",
                "Anticipation": "0.0253136",
                "Surprise": "0.030134391",
                "Anger": "0.00824347",
                "Fear": "0.013505802",
                "Disgust": "0.03657079",
                "Trust": "0.06234263"
            }
        },
        {
            "text": "Androidにくらべると画面は大きくなりましたが、文字は変更してもアプリやサイトにより小さいままの所が多いので　慣れるまでの辛抱です。 早くカメラを屋外で撮影したいです。望遠が素晴らしいです。",
            "emotion_score": {
                "Joy": "0.14712891",
                "Sadness": "0.005931779",
                "Anticipation": "0.81967485",
                "Surprise": "0.0070435335",
                "Anger": "0.0011118796",
                "Fear": "0.0045338823",
                "Disgust": "0.002430033",
                "Trust": "0.012145223"
            }
        }
    ]
}
```

## 注意事項
授業内でのみ利用するようお願いします。

## 参考文献
[Hugging Face + WRIMEデータセットで、8クラスの感情分類](https://qiita.com/izaki_shin/items/2b4573ee7fbea5ec8ed6)
