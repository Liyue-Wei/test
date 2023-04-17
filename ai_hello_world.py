import openai
import os

openai.api_key = "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"
lang = ['python', 'c', 'c++', 'vb', 'swift', 'java', 'js', 'ruby', 'go', 'cs', 'r', 'powershell', 'lua', 'julia', 'PHP', 'Objective-C', 'vb.net7']

for i in range(0, len(lang)):
    prompt = ("write a code to print hello world uaing " + lang[i])
    completions = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=1280)
    message = completions.choices[0].text
    print(lang[i]+message+'\n')

os.system('pause')