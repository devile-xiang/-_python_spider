#endoing:utf-8

import requests
from lxml import etree
import time

def request_list_page():
    url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    headers={
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36',
        'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'Origin':'https://www.lagou.com',
        'Cookie':'JSESSIONID=ABAAABAABEEAAJA7187BCA6BAFAEF64E80D4E7269B24F08; _ga=GA1.2.218594.1540350246; _gid=GA1.2.2108958500.1540350246; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1540350246; user_trace_token=20181024110410-7a5b78e2-d739-11e8-80d2-5254005c3644; LGUID=20181024110410-7a5b7d10-d739-11e8-80d2-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; _gat=1; LGSID=20181024141309-e15a4e27-d753-11e8-9cd0-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20181024141317-e603bf54-d753-11e8-9cd0-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1540361595; SEARCH_ID=50389030f9eb474a857a314415cabb22',

        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token':'None',
        'X-Requested-With':'XMLHttpRequest'

    }
    data={
        'first':'false',
        'pn':2,
        'kd':'python'
    }
    for x in range(1,14):
        data['pn'] = x
        response = requests.post(url=url, headers=headers, data=data)
        #
        # print(response.json())
        result=response.json()
        print(result['content']['hrInfoMap'])

        time.sleep(5)

def main():
    request_list_page()
if __name__ == '__main__':
    main()