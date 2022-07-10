import io
from re import I
import sys

_INPUT = """\
6
abbaac
abbbbaaac
xyzz
xyyzz
bbaaaa
aa
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  T=input()
  ans='Yes'
  nows=0
  nowt=0
  ls=[]
  lt=[]
  while nows<len(S):
    s=S[nows]
    cs=0
    while nows<len(S) and S[nows]==s:
      cs+=1
      nows+=1
    ls.append((s,cs))
  while nowt<len(T):
    t=T[nowt]
    ct=0
    while nowt<len(T) and T[nowt]==t:
      ct+=1
      nowt+=1
    lt.append((t,ct))
  if len(ls)!=len(lt):
    ans='No'
  else:
    for i in range(len(ls)):
      if ls[i][0]!=lt[i][0]: ans='No'
      if ls[i][1]==1 and lt[i][1]>1: ans='No'
      if ls[i][1]>lt[i][1]: ans='No'
  print(ans)