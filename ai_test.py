import openai
openai.api_key = "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"

model_engine = "text-davinci-003" # 設定模型引擎

while True:
    const = str(input())
    completions = openai.Completion.create(engine=model_engine, prompt=const, max_tokens=1024)
    message = completions.choices[0].text # 獲取模型回應
    print(message)
