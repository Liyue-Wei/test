import openai
import os

openai.api_key = "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"
lang = ['python', 'c', 'c++', 'vb', 'swift', 'java', 'js', 'ruby', 'go', 'cs', 'r', 'powershell', 'lua', 'julia']

for i in range(0, len(lang)):
    prompt = ("write a code to print hello world uaing " + lang[i])
    completions = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=256)
    message = completions.choices[0].text
    print(lang[i]+message+'\n')

os.system('pause')