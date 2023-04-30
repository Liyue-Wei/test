import openai
import os
import time

time_now = time.time()

openai.api_key = "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"
lang = ['python', 'c', 'c++', 'vb', 'swift', 'java', 'js', 'ruby', 'go', 'cs', 'r', 'powershell', 'lua', 'julia', 'PHP', 'Objective-C', 'vb.net7', 'html', 'coldfusion', 'cython', 'cpython', 'fortran', 'kotlin', 'matlab']

i = len(lang)
print(i)

while(i>0):
    for n in range(0, len(lang)):
        prompt = ("write a code to print hello world uaing " + lang[n])
        completions = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=1280)
        message = completions.choices[0].text
        print(lang[n]+message+'\n')
    i-=1
    print('\n')
    time_now = (time.time()-time_now)
    print("time spend:", time_now)

os.system('pause')