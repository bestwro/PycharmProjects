"""
# 版权声明：本文为CSDN博主「liver100day」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/liver100day/article/details/121258749

# requests是python实现的简单易用的HTTP库，使用起来比urllib简洁很多，
# requests 允许你发送 HTTP/1.1 请求。指定 URL并添加查询url字符串即可开始爬取网页信息
# pip install requests  使用pip安装必备模块 requests
"""

# 1.抓取网页源代码
import requests  # 导入我们需要的requests功能模块

# page = requests.get('https://www.crrcgo.cc/admin/crr_supplier.html?page=1')
# 使用get方式获取该网页的数据。实际上我们获取到的就是浏览器打开百度网址时候首页画面的数据信息
# print(page.text)
# 把我们获取数据的文字（text）内容输出（print）出来

# 2.抓取一个网页源代码中的某标签内容
"""
上面抓取到的代码充满尖括号的一片字符，对我们没作用，这样的充满尖括号的数据就是我们从服务器收到的网页文件，就像Office的doc、pptx文件格式一样，
网页文件一般是html格式。我们的浏览器可以把这些html代码数据展示成我们看到的网页。
我们如果需要这些字符里面提取有价值的数据，就必须先了解标记元素
每个标记的文字内容都是夹在两个尖括号中间的，结尾尖括号用/开头，
尖括号内（img和div）表示标记元素的类型（图片或文字），尖括号内可以有其他的属性（比如src）
"""
from bs4 import BeautifulSoup

# 3.抓取多个网页子标签的内容import
inurl = "https://www.crrcgo.cc/admin/crr_supplier.html?page="
for num in range(1, 6):
    print("---正在抓取第" + str(num) + "页数据---")
    outurl = inurl + str(num)
    req = requests.get(url=outurl)

# req = requests.get(url="https://www.crrcgo.cc/admin/crr_supplier.html?page=1")
    req.encoding = "utf-8"  # import BeautifulSoup
    html = req.text
    soup = BeautifulSoup(req.text, features="html.parser")
# 用html解析器(parser)来分析我们requests得到的html文字内容，soup就是我们解析出来的结果。
    company_items = soup.find_all("div", class_="detail_head")
# find是查找，find_all查找全部。查找标记名是div并且class属性是detail_head的全部元素
# dd = company_item.text.strip()
# strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。在这里就是移除多余的尖括号的html数据
# print(dd)
    for company_item in company_items:
        dd = company_item.text.strip()
        print(dd)
