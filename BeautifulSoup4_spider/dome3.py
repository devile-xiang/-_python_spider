
from bs4 import BeautifulSoup

html="""
<tbody><tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43326&amp;keywords=python&amp;tid=0&amp;lid=0">21882-医学NLP研究员</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2018-08-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43305&amp;keywords=python&amp;tid=0&amp;lid=0">22989-腾讯云运营系统开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-14</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43253&amp;keywords=python&amp;tid=0&amp;lid=0">MIG03-资深运营开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43238&amp;keywords=python&amp;tid=0&amp;lid=0">18302-动作类手游资深TA（深圳）</a><span class="hot">&nbsp;</span></td>
					<td>设计类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2018-08-14</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43224&amp;keywords=python&amp;tid=0&amp;lid=0">WXG02-134 微信运营优化分析工程师（广州）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>广州</td>
					<td>2018-08-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43181&amp;keywords=python&amp;tid=0&amp;lid=0">SNG17-支付后台开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>5</td>
					<td>深圳</td>
					<td>2018-08-14</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43173&amp;keywords=python&amp;tid=0&amp;lid=0">25927-高级测试开发工程师（深圳）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43158&amp;keywords=python&amp;tid=0&amp;lid=0">25923-海外游戏技术运营工程师（深圳）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-14</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43150&amp;keywords=python&amp;tid=0&amp;lid=0">22025-沙盒游戏资深TA技术美术（深圳）</a></td>
					<td>设计类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43140&amp;keywords=python&amp;tid=0&amp;lid=0">23673-高级全栈工程师（偏向后端）（北京）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2018-08-14</td>
		    	</tr>
		    			    	<tr class="f">
		    		<td colspan="5">
		    			<div class="left">共<span class="lightblue total">508</span>个职位</div>
		    			<div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=10#a">2</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=20#a">3</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=30#a">4</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=40#a">5</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=50#a">6</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=60#a">7</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=70#a">...</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=500#a">51</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
		    			<div class="clr"></div>
		    		</td>
		    	</tr>
		    </tbody> 
		       <p><!--  我是注释字符串--></p>
		       
		       """

soup=BeautifulSoup(html,'lxml')
#获取所有tr标签
# trs=soup.select("tr")
# for i in  trs:
#     print(i)
#     print("="*30)
#获取第二个tr标签
# trs=soup.select('tr')[1]
# print(trs)
#获取所有classd等于even的标签

# evens=soup.select(".even")
# evens=soup.select("tr[class='even']")
# for i in evens:
#     print(i)

#获取所有的a标签的href属性
# aList=soup.select('a')
# for i in aList:
#     # print(i)
#     herf=i['href']
#     print(herf)

# 获取所有的职位信息纯文本
# trs=soup.select('tr')
# for tr in trs:
#     insos=list(tr.stripped_strings)
#     print(insos)

# div=soup.find('div')
p=soup.find('tr')
for i in p:
    print(i)