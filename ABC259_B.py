import io
import sys

_INPUT = """\
6
2 2 180
5 0 120
0 0 11
15 5 360
-505 191 278
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import math
  a,b,d=map(int,input().split())
  x=(math.degrees(math.atan2(b, a))+d)*math.pi/180
  r=(a**2+b**2)**.5
  print(math.cos(x)*r,math.sin(x)*r)