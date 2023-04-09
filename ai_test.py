'''
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
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
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
'''

import openai
openai.api_key = "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"

model_engine = "text-davinci-002" # 設定模型引擎
prompt = "Hello, how are you?" # 輸入提示信息

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=60
)

message = completions.choices[0].text # 獲取模型回應
print(message)


'''
import openai
import os

# 設定 API Key
openai.api_key = os.environ['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']

# 輸入您要對話的文字
prompt = "Hello, I'm ChatGPT. What can I help you with today?"

# 設定模型和引擎
model_engine = "text-davinci-002"

# 設定輸出的字元數量
max_tokens = 50

# 設定重要度
importance = 1.0

# 設定回覆的溫度
temperature = 0.7

# 執行模型並取得回覆
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=max_tokens,
    n=1,
    stop=None,
    temperature=temperature,
    frequency_penalty=0,
    presence_penalty=importance
)

# 輸出回覆
print(response.choices[0].text)
'''