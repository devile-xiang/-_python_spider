#encoding:utf-8

import json
import csv

#将python对象转换成json字符串
#
# persons=[
#     {
#         "username":"张珊",
#         "age":"18",
#         "conutry":"china"
#     },
# {
#         "username":"hello",
#         "age":"20",
#         "conutry":"china"
#     }
#
#
#
# ]
# #使用json库的dumps转换成json
# # json_str=json.dumps(persons)
# # print(type(json_str))
# # print(json_str)
#
# #写入json到本地
#
# with open('person.json','w',encoding='utf-8') as fp:
#     #ensure_ascii=False,关闭这个并设置utf-8编码格式，不然会自动转回为啊斯克码
#     json.dump(persons,fp,ensure_ascii=False)

#
# with open('person.json','r',encoding='utf-8') as fp:
#     pesons=json.load(fp)
#     for peson in pesons:
#         print(peson)


def write_csv_dome1():
    headers = ['username', 'age', 'height']

    values = [
        ('张三', 18, 201),
        ('李四', 85, 185),
        ('丽萨', 23, 158),
        ('胖杰克', 14, 81),
    ]
    # newline='',默认写一行就加个换行
    with open('classromm.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(values)
def write_csv_dome2():
    headers = ['username', 'age', 'height']

    values =[
        {'username': '张三', 'age': '18', 'height': '158'},
        {'username': '王五', 'age': '28', 'height': '138'},
        {'username': '橘猫', 'age': '78', 'height': '120'},
        {'username': '奥巴马', 'age': '12', 'height': '89'},

    ]
    with open('classroom1.csv','w',encoding='utf-8',newline='')as fp:
        writer=csv.DictWriter(fp,headers)
        #写入表头
        writer.writeheader()
        writer.writerows(values)


if __name__ == '__main__':
    write_csv_dome2()
