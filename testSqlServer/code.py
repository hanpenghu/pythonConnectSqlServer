
# -*- coding: UTF-8 -*-
import sys

def str2bin(strText):
    b = bytes((ord(i) for i in strText))
    return b


def getCode(strText, codec):
    b = bytes((ord(i) for i in strText))
    return b.decode(codec)
