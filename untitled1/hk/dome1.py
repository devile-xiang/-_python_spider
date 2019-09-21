from ctypes import *
msvcrt=cdll.msvcrt
message_string="Hello world!\n"
msvcrt.wprintf("testing:%s",message_string)