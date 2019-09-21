#encoding：utf-8

from pytesseract import pytesseract
from PIL import Image
import  time
from urllib import request
import json
import pybase64


def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\OCR\Tesseract-OCR\tesseract.exe"
    url="https://sso.toutiao.com/refresh_captcha/"
    headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36",
        "Referer":"https://sso.toutiao.com/"
    }
    while True:
        text1=request.Request(url=url,headers=headers)
        text1 = request.urlopen(text1).read().decode()
        hjson = json.loads(text1)
        print(hjson["captcha"])
        img=pybase64.b64decode(hjson["captcha"])
        file=open("captcha.gif","wb")
        file.write(img)
        file.close()



        image=Image.open('captcha.gif')
        text= pytesseract.image_to_string(image)
        print("-"*30)
        print(text)
        time.sleep(2)



if __name__ == '__main__':
    main()