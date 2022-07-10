import io
import sys

_INPUT = """\
6
4
0 -2 3 3
0 0 2
2 0 2
2 3 1
-3 3 3
3
0 1 0 3
0 0 1
0 0 2
0 0 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  def bfs(G,s):
    inf=10**10
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    return D
  N=int(input())
  sx,sy,tx,ty=map(int,input().split())
  c=[list(map(int,input().split())) for _ in range(N)]
  G=[[] for _ in range(N)]
  for i in range(N):
    x,y,r=c[i]
    if (sx-x)**2+(sy-y)**2==r**2: s=i
    if (tx-x)**2+(ty-y)**2==r**2: t=i
    for j in range(i+1,N):
      xd,yd,rd=c[j]
      if (x-xd)**2+(y-yd)**2<=(r+rd)**2 and (x-xd)**2+(y-yd)**2>=(r-rd)**2:
        G[i].append(j)
        G[j].append(i)
  if bfs(G,s)[t]==10**10: print('No')
  else: print('Yes')