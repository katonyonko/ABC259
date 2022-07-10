import io
import sys

_INPUT = """\
6
4
1
7 2
2
2 2
5 1
1
5 1
2
2 1
7 1
1
1
998244353 1000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  N=int(input())
  d=defaultdict(list)
  number=[]
  for _ in range(N):
    m=int(input())
    tmp=[list(map(int,input().split())) for i in range(m)]
    number.append(tmp)
    for i in range(m):
      p,e=tmp[i]
      d[p].append(e)
  ans=0
  for k in d:
    d[k]=sorted(d[k],reverse=True)[:2]
  flg=0
  for i in range(N):
    m=len(number[i])
    flg2=0
    for j in range(m):
      p,e=number[i][j]
      if e==d[p][0] and (len(d[p])==1 or d[p][0]>d[p][1]): flg2=1
    if flg2==0: flg=1
    else: ans+=1
  if flg==1: ans+=1
  print(ans)