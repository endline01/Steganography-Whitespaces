#!/usr/bin/python3
from pwn import *
import binascii
import sys
usage = 'usage: ./whitespaces.py <filename>'
binary = ''


while True:
    try:
        if sys.argv[1] == '-h':
            print(usage);break
        filename = sys.argv[1]
        with open(filename, "rb") as file:
            for _ in range(88):
                data = bytearray(file.readline())
                data = data.replace(b'\x09', b'1')
                data = data.replace(b'\x20', b'0')
                data = data.replace(b'\x0d', b'')
                data = data.replace(b'\x0a', b'')
                data = data.decode("ascii")
                if unbits(data) == b'\x80': 
                    continue
                binary+=data+" "
        break
    except IndexError:
        print(usage)
        break
def b2t(bi):
    ASCII = ''
    for i in bi.split():
        ASCII += chr(int(i,2)) #converting binary data 2 ASCII
    return ASCII
if len(binary) > 1:
    print(f'In binary: {binary}\n')
    print(f'Text data: {b2t(binary)}')