#coding=utf-8
import os, sys, platform

os.system('rm -rf TIME.cpython-311.so')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf TIME.cpython-311.so')
except:
    pass

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('TIME.cpython-311.so'):
        os.system('curl -L https://github.com/XAIVER-XD/KLEIN/blob/main/TIME.cpython-311.so?raw=true -o TIME.cpython-311.so') 
        import TIME
        TIME.random_india()
    else:
        import TIME
        TIME.random_india()