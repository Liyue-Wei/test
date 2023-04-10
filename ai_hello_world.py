import openai

openai.api_key = "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"
lang = ['python', 'c', 'c++', 'vb', 'swift', 'java', 'js', 'ruby', 'go', 'cs', 'r', 'powershell', 'lua', 'julia']

for i in range(0, len(lang)):
    prompt = ("write a code to print hello world uaing " + lang[i])
    completions = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=256)
    message = completions.choices[0].text
    print(lang[i]+message+'\n')

'''
import openai
openai.api_key = "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"

model_engine = "text-davinci-002" # 設定模型引擎
prompt = "write a code to print hello world uaing basic" # 輸入提示信息

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=256
)

message = completions.choices[0].text # 獲取模型回應
print(message)
'''