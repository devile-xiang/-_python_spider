#encoding:utf-8

from urllib import request


import pytesseract as pya
import time

try:
    from PIL import Image
except ImportError:
    import Image

def main():
    try:
        from PIL import Image
    except ImportError:
        import Image
    url="http://web.1xinxi.cn/CheckCode.aspx"

    for i in range(50):
        time.sleep(1)
        #下载图片
        request.urlretrieve(url,'tu%d.jpg'%i)
        image=Image.open("tu%d.jpg"%i)
        # image.show()
        text = pya.image_to_string(image,lang='chi_sim')
        print(text)
        with open("output.txt",'a',encoding="utf-8") as f:
            # print(text)

            f.write(str(i)+"---"+text+"\n")







if __name__ == '__main__':
    main()