import time
from time import localtime, strftime
print(strftime("%a, %d %b %Y %H:%M:%S +0000", localtime()))
print(strftime("%H", localtime())[:1])
print(strftime("%H", localtime())[1:])
strH1 = strftime("%H", localtime())[:1]
strH2 = strftime("%H", localtime())[1:]
strM1 = strftime("%M", localtime())[:1]
strM2 = strftime("%M", localtime())[1:]
if strH1 == "1": print("OK")
