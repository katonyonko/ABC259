import io
import sys

_INPUT = """\
6
7
1 2 1 0 2 1 1
1 2 8
2 3 9
2 4 10
2 5 -3
5 6 8
5 7 3
20
0 2 0 1 2 1 0 0 3 0 1 1 1 1 0 0 3 0 1 2
4 9 583
4 6 -431
5 9 325
17 6 131
17 2 -520
2 16 696
5 7 662
17 15 845
7 8 307
13 7 849
9 19 242
20 6 909
7 11 -775
17 18 557
14 20 95
18 10 646
4 3 -168
1 3 -917
11 12 30
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  d=list(map(int,input().split()))
  G=[dict() for _ in range(N)]
  for _ in range(N-1):
    u,v,w=map(int,input().split())
    u-=1; v-=1
    G[u][v]=w
    G[v][u]=w
  parent=[-1]*N
  st=[0]
  while st:
    x=st.pop()
    for u in G[x]:
      if u!=parent[x]:
        parent[u]=x
        st.append(u)
  dp=[[-1]*2 for _ in range(N)]
  st=[(0,0),(0,1)]
  kouho=[[] for _ in range(N)]
  while st:
    s,dd=st.pop()
    if dd==0:
      kouho[s].sort(key=lambda x: -x[1])
      tmp=sum([kouho[s][i][0] for i in range(len(kouho[s]))])
      dp[s][0]=tmp
      for i in range(min(d[s],len(kouho[s]))):
        if kouho[s][i][1]>0: dp[s][0]+=kouho[s][i][1]
      if d[s]==0: dp[s][1]=-(10**20)
      else:
        dp[s][1]=tmp
        for i in range(min(d[s]-1,len(kouho[s]))):
          if kouho[s][i][1]>0: dp[s][1]+=kouho[s][i][1]
      if parent[s]!=-1:
        kouho[parent[s]].append((dp[s][0],dp[s][1]+G[s][parent[s]]-dp[s][0]))
    else:
      for u in G[s]:
        if u==parent[s]: continue
        st.append((u,0))
        st.append((u,1))
  print(dp[0][0])
