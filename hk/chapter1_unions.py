from ctypes import * #引入ctypes所有模块
class barley_amount(Union):#构建一个union，三个变量分享相同内存
    _fields_ =[
    ("barley_long",c_long),
    ("barley_int",c_int),
    ("barley_char",c_char * 8)]
value = input("Enter the amount of barley to put into the beer vat:")
my_barley = barley_amount(int(value))
print ("Barley amount as a long: %ld" % my_barley.barley_long)
print ("Barley amount as an int: %d" % my_barley.barley_int)
print ("Barley amount as a char:%s" % my_barley.barley_char)
