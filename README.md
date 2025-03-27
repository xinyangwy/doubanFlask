# doubanFlask
 python爬虫 豆瓣电影Top250数据分析与可视化（应用Flask框架、Echarts、WordCloud等技术）

+ 学习的课程（B站）：[https://www.bilibili.com/video/BV12E411A7ZQ](https://www.bilibili.com/video/BV12E411A7ZQ)
 
+ 视频演示地址（B站）：[https://www.bilibili.com/video/BV1rU4y1P7bg](https://www.bilibili.com/video/BV1rU4y1P7bg)

+ 将此项目部署在服务器上的教程：[https://www.cnblogs.com/xinyangblog/p/16326433.html](https://www.cnblogs.com/xinyangblog/p/16326433.html)
  
+ CSDN对应文章：[https://blog.csdn.net/weixin_45912291/category_11346699.html](https://blog.csdn.net/weixin_45912291/category_11346699.html)

+ 百度网盘链接: https://pan.baidu.com/s/1bee-4OBE7CEyweN_vJs4DA?pwd=m9zx 提取码: m9zx 复制这段内容后打开百度网盘手机App，操作更方便哦
+ 【注：此文件中含有python虚拟环境venv文件夹，版本python3.8，记得修改venv目录中的pyvenv.cfg文件中的home路径，修改到自己电脑中的python的对应的位置】


> 记得修改 doubanFlask/venv/pyvenv.cfg 文件中的相关路径

---

# 注：一些大致的说明
+ 对应的html文本位置标注：
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/6a92675c8b917930252f0daba94cbbc6.png)
# 一、爬取“豆瓣电影 Top 250”相关信息：
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/409013183c364e74148e6cf72003e3c6.png)
## 1、准备工作
![image](https://github.com/user-attachments/assets/ebe26ecf-ef03-4f7c-9326-7d038d2a43d0)

## 2、获取数据
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/a25567299fc43e70c783b374d2769922.png)
### 补充：urllib
urllib的详解使用 - 简书：[https://www.jianshu.com/p/63dad93d7000](https://www.jianshu.com/p/63dad93d7000)
## 3、标签解析
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/d615234b4ab20614283ada344e0a4d15.png)
### 补充：BeautifulSoup4和re
BeautifulSoup4相关介绍 - web教程网：[http://www.jsphp.net/python/show-24-214-1.html](http://www.jsphp.net/python/show-24-214-1.html)
Python 正则表达式 | 菜鸟教程：[https://www.runoob.com/python/python-reg-expressions.html](https://www.runoob.com/python/python-reg-expressions.html)
## 4、保存数据
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/a59488905c37bd1c4b832a98e0b2d0f8.png)
### 补充：xlwt
python模块之xlwt模块:[https://blog.csdn.net/qq_31851107/article/details/103691790](https://blog.csdn.net/qq_31851107/article/details/103691790)

爬取成功后生成的Excel表格：
（注：生成的xls文件路径：`savepath = "豆瓣电影top250.xls"  # 默认与此.py文件在同一个目录下`）
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/3ec79e2dac1a095203992ed021c8521b.png)
# 二、爬取/下载top250电影对应的封面
对“爬取“豆瓣电影 Top 250”相关信息”的代码适当修改，正则表达式提取部分只保留`findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)`部分，
找到所有图片的链接之后，保存图片的关键函数如下（含有对图片的命名）：
```python
def DownloadImg(datalist):
    x = 1
    for imgurl in datalist:
        urllib.request.urlretrieve(imgurl, 'D:\IDMdownload\Image\%s.jpg' % x)
        x += 1
        print("已经爬取", x, "张图片")
```
## 效果展示
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/77ea32b62fe302a0874204f82825a5dc.gif)

# 爬取豆瓣top250信息并存入数据库中 | sqlite3:
![e6c176ab021cc3da19ff6e8c0475dd90](https://github.com/user-attachments/assets/490adc1a-d38d-492e-9f33-e41b2d6978c1)


## 遇到的问题：

### 1.关于数据库表格中出现：NBSP

![image-20210904163239086](https://i-blog.csdnimg.cn/blog_migrate/29cc814b911256c9cdf11c0c97f1a705.png)

原本的代码：

```python
html = response.read().decode("utf-8")
```

修改之后：

```python
html = response.read().decode("utf-8").replace('&nbsp;','')
```

参考：python爬虫 爬取内容的时候&nbsp 空格内容变成问号‘？’ - 可乐爆炸的回答 - 知乎 https://www.zhihu.com/question/35945782/answer/382589149

![image-20210904172027665](https://i-blog.csdnimg.cn/blog_migrate/e694c68714d354714b31d4a47d9f9e43.png)

### 2. 为什么HTML字段中会出现&NBSP？

+ 在html代码中每输入一个转义字符&nbsp就表示一个空格，输入十个&nbsp，页面中就显示10个空格位置。
+ 而在html代码中输入空格，不管输入多少个空格，最终在页面中显示的空格位置只有一个。

举例：hmtl代码中，在两个字之间输入十个空格与输入十个转义字符&nbsp的效果对比。

![img](https://i-blog.csdnimg.cn/blog_migrate/11f934a73a9624bbc3b353340282ebe0.png)

![img](https://i-blog.csdnimg.cn/blog_migrate/e9b38fd4ebaeeb82cd53b693bf8430bb.png)

### 3.java.io.IOException: 不能删除数据库文件

![image-20210904172503424](https://i-blog.csdnimg.cn/blog_migrate/15721e7b84f4ccacda1af8aa48ceed6a.png)

+ 方法一：首先在右侧的数据库中将其“remove”，然后再在文件目录中将其删除；
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/6f3b9515ae533ccb4634ac7cddb1ba7e.png)


+ 方法二：
启动任务管理器，结束pycharm进程下的插件（结束任务）
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/c37253d086c6ce5b456e1f4a31e0627d.png)

参考：[java.io.IOException: 不能删除数据库文件](https://blog.csdn.net/gets_s/article/details/112177029)

### 4.  关于decode和encode的区别

+ 首先要搞清楚，字符串在Python内部的表示是unicode编码，因此，在做编码转换时，通常需要以unicode作为中间编码；
+ （即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。）
+ decode的作用：将其他编码的字符串转换成unicode编码；
  + 如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
+ encode的作用：将unicode编码转换成其他编码的字符串；
  + 如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。

总结：想要将其他的编码转换成utf-8必须先将其解码成unicode然后重新编码成utf-8,它是以unicode为转换媒介的

参考：[decode和encode的区别](https://segmentfault.com/a/1190000015788943)

## 豆瓣电影数据可视化（Flask框架）部署在服务器上
### 1. 在宝塔面板下载“python项目管理器”
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/14e671c7ab0414d5a1f52d23b960f972.png)
### 2. 上传文件至服务器
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/4d1e372c6c45d02370d39ad993c23ba3.png)

### 3. 生成requirements.txt文件
进入你的项目根目录，使用命令把项目依赖包导出到项目根目录。

```python
pip freeze >requirements.txt
```
![0cfa7dfc1702bc1a8e98124e0f9b708f](https://github.com/user-attachments/assets/688792e6-5387-4cf2-9b0b-a89f3a4f6ed8)

### 4.在python项目管理器添加python项目
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/bd46cffd72a6f141ff8db3b172a253b6.png)
注：如果python 项目管理器的项目状态一直显示：“已暂停”，可以尝试重新安装python 项目管理器。
+ 相关：
	+ [部署 Flask 应用时，为什么会需要 gunicorn 或 uWSGI？](https://www.zhihu.com/question/37148421?sort=created)
	+ [深入理解uwsgi和gunicorn网络模型](https://www.jianshu.com/p/2b184c5eb90d)
### 5. 演示
+ 在线演示地址：[链接](http://101.32.183.14:5000/index)
+ 本地编译演示：[https://www.bilibili.com/video/bv1rU4y1P7bg](https://www.bilibili.com/video/bv1rU4y1P7bg)
+ 源代码下载地址（蓝奏云）：[https://wws.lanzoui.com/i5Sg4ttokwj](https://wws.lanzoui.com/i5Sg4ttokwj)


