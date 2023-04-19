import openai
import os

openai.api_key = "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"
lang = ['python', 'c', 'c++', 'vb', 'swift', 'java', 'js', 'ruby', 'go', 'cs', 'r', 'powershell', 'lua', 'julia', 'PHP', 'Objective-C', 'vb.net7', 'html']

for i in range(0, len(lang)):
    prompt = ("write a code to print a heart with * uaing " + lang[i])
    completions = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=1280)
    message = completions.choices[0].text
    print(lang[i]+message+'\n')

os.system('pause')