# doubanFlask
 python爬虫 豆瓣电影Top250数据分析与可视化（应用Flask框架、Echarts、WordCloud等技术）

+ 学习的课程（B站）：[https://www.bilibili.com/video/BV12E411A7ZQ](https://www.bilibili.com/video/BV12E411A7ZQ)
 
+ 视频演示地址（B站）：[https://www.bilibili.com/video/BV1rU4y1P7bg](https://www.bilibili.com/video/BV1rU4y1P7bg)

+ 将此项目部署在服务器上的教程：[https://www.cnblogs.com/xinyangblog/p/16326433.html](https://www.cnblogs.com/xinyangblog/p/16326433.html)

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

