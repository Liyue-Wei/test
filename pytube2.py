from pytube import YouTube
from download_path import download

yt = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
print('開始下載：' + yt.title)
pathdir = download()  #下載資料夾
yt.streams.first().download(pathdir)
print('「' + yt.title + '」下載完成！')
