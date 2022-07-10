import io
import sys

_INPUT = """\
6
38 20 17 168 3
1 0 1 3 2
100 10 100 180 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M,X,T,D=map(int,input().split())
  if X>M: print(T-D*(X-M))
  else: print(T)