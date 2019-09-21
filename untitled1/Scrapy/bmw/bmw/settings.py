# -*- coding: utf-8 -*-

# Scrapy settings for bmw project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bmw'

SPIDER_MODULES = ['bmw.spiders']
NEWSPIDER_MODULE = 'bmw.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bmw (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  'Cache-Control':'max-age=0',
  'Cookie':'__ah_uuid=62852AEE-8A81-41CA-8C8C-E70F8EF3496F; fvlid=1545027806900kNJQInoohA; sessionid=5101EF69-2F7D-4130-A3FD-09C4EF836B34%7C%7C2018-12-17+14%3A23%3A27.488%7C%7Cwww.baidu.com; area=500108; ahpau=1; sessionuid=5101EF69-2F7D-4130-A3FD-09C4EF836B34%7C%7C2018-12-17+14%3A23%3A27.488%7C%7Cwww.baidu.com; FootPrints=28541%7C2018-12-26%2C; live-voteid=pc312188644529295056; mallsfvi=1546581960479CEjlSSdz%7Cev.autohome.com.cn%7C0; historybbsName4=c-3820%7C%E5%89%8D%E9%80%94K50; ahsids=442_3294_4441; sessionip=14.111.63.26; sessionvid=64F9D331-98DF-48BE-8C91-60D8112DFBB4; Hm_lvt_9924a05a5a75caf05dbbfb51af638b07=1546581973,1547002378,1547086985,1547189600; Hm_lpvt_9924a05a5a75caf05dbbfb51af638b07=1547189600; ahpvno=4; index_pic_redpacket=1; isFromBD=; ref=www.baidu.com%7C0%7C0%7C0%7C2019-01-11+15%3A13%3A28.871%7C2018-12-17+14%3A23%3A27.488',


  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bmw.middlewares.BmwSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'bmw.middlewares.BmwDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'bmw.pipelines.BmwPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
