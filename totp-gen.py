#!/usr/bin/env python3
import base64
import hmac
import struct
import sys
import time
import getopt
import hashlib
import datetime
import calendar

def getArguments(argv):
    try:
        opts, args = getopt.getopt(argv, "hd:k:a:")
    except getopt.GetoptError:
        print('Unexpected set of arguments. Allowed arguments are:\n'
              '-d digits\n'
              '-k key\n'
              '-h help')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-d"):
            global DIGITS
            DIGITS = arg
        elif opt in ("-k"):
            global KEY
            KEY = arg
        elif opt in ("-h"):
            print('Allowed arguments are:\n'
              '-d digits\n'
              '-k key\n'
              '-h help')
            sys.exit(0)

DIGITS = 0
KEY = ''
ALGO = ''

def int2beint64(i):
    return struct.pack('>Q', int(i))

def dec(h,p):
    digits = str(truncated_value(h))
    code = str(digits)[-int(p):]
    return code.zfill(6)

def truncated_value(h):
    v = h[-1]
    if not isinstance(v, int):
        v = ord(v)  # Python 2.x
    offset = v & 0xF
    (value,) = struct.unpack('>I', h[offset : offset + 4])
    return value & 0x7FFFFFFF

def hotp(key, period=30, digits=6, digest=hashlib.sha1):

    t = int(time.time())
    T = int(t / period)
    T_next = (T*period)+period


    bin_counter = int2beint64(T)
    # In case the string is not a fully filled b64 string, we need
    # to append '=' until it reached a valid length
    last_block_width = len(key) % 8
    if last_block_width != 0:
        key += (8 - last_block_width) * '='
    bin_key = base64.b32decode(key)

    mac = hmac.new(bin_key, bin_counter, digest).digest()
    code = dec(mac, digits)
     # return current code + time valid left in seconds
    return code, int(T_next-t)

if __name__ == '__main__':
    getArguments(sys.argv[1:])
    code,timeleft = hotp(KEY,digits=DIGITS)
    print(f"{code} | time left {timeleft}")