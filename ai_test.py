import openai
openai.api_key = "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"

model_engine = "text-davinci-002" # 設定模型引擎

while True:
    const = str(input())
    completions = openai.Completion.create(engine=model_engine, prompt=const, max_tokens=1024)
    message = completions.choices[0].text # 獲取模型回應
    print(message)
