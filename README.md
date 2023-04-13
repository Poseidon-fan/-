# 爬取酷狗音乐

## 程序介绍

本代码基于Python语言及selenium、requests、BeautifulSoup等第三方库编写。其中.py文件是源文件，运行的话需要下载Python环境与上述第三方库、.exe文件是用pyinstaller打包后形成的可执行文件，可以直接在电脑上运行。

## 使用方法

运行文件后，按照提示输入要下载的音乐名：

![](https://github.com/Poseidon-fan/-/blob/main/img/p1.png?raw=true)

回车后，会返回酷狗音乐上搜索结果的列表，按照提示选择对应的序号输入即可：
![](C:\Users\86186\Desktop\33215ce93108806f8655d5728c2bc29.png)

最后会提示下载成功，其.mp3文件会下载到该文件同级目录下：

![](C:\Users\86186\Desktop\002afa18c66b4d13d9a372532e58d97.png)

## 说明

由于法律约束加上作者初学爬虫水平有限，对于平台中的VIP歌曲，本程序所下载的并不是完整的歌曲文件，而是其前60s的音频文件，并没有实现绕过VIP爬取。代码也仅供学习参考使用。
