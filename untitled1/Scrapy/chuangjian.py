#
#创建一个scrapy 爬虫现做的
#
#scrapy startproject 你的项目名
#
#然后在 cd 到你创建的文件名 cd firsitname
#
#然后现在开始创建第一个项目
#
#
# scrapy genspider -t crawl 你的爬虫文件名 爬取的页面域名
#
#
#运行爬虫的代码
#
#
#在项目文件目录，创建一个py文件，在里面输入一下内容

#导入运行scrapy的库
#from scrapy import cmdline
#
#运行文件的代码，weisuen 是你的爬虫，名字
# cmdline.execute("scrapy crawl weisuen".split())
#
#
#
#下面是scrapy对rules的理解：
#https://blog.csdn.net/wqh_jingsong/article/details/56865433
#
#
#我们需要设置setting.py
#我们先设置ROBOTSTXT_OBEY 为 False
#
#
#
#我们还要设置DEFAULT_REQUEST_HEADERS
#
#为了避免网站检测到我们是爬虫
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
