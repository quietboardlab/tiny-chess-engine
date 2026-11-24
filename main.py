I=10**9;V=dict(zip('PNBRQK',(100,320,330,500,900,0)));S={'P':"PPPPPPPPUZZ<<ZZUUKFPPFKUPPPddPPPPPdnndPPPZdxxdZPP}}}}}}}PPPPPPPP",'N':"#-2222-#-<PUUP<-2UZ__ZU22P_dd_P22U_dd_U22PZ__ZP2-<PPPP<-#-2222-#",'K':"nxdZZdxnddZPPZddF<<22<<F<22((22<2((((((22((((((2<22((22<<2<FF<2<"};KN=[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)];D8=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
class P:
 def __init__(s):s.b=['.']*64;s.w=1;s.ep=-1
 def fen(s,f):
  q=f.split();s.b=['.']*64;r=7;x=0
  for ch in q[0]:
   if ch=='/':r-=1;x=0
   elif ch.isdigit():x+=int(ch)
   else:s.b[r*8+x]=ch;x+=1
  s.w=q[1]=='w';s.ep=-1
  if q[3]!='-':s.ep=(int(q[3][1])-1)*8+ord(q[3][0])-97
 def atk(s,sq,by):
  b=s.b;x,y=sq&7,sq>>3;pr=y-1 if by else y+1
  if 0<=pr<8 and any(0<=x+d<8 and b[pr*8+x+d]==('P'if by else'p')for d in(-1,1)):return 1
  for dx,dy in KN:
   if 0<=x+dx<8 and 0<=y+dy<8 and b[(y+dy)*8+x+dx]==('N'if by else'n'):return 1
  for dx,dy in D8:
   nx,ny=x+dx,y+dy
   if 0<=nx<8 and 0<=ny<8 and b[ny*8+nx]==('K'if by else'k'):return 1
   while 0<=nx<8 and 0<=ny<8:
    p=b[ny*8+nx]
    if p!='.':
     if p.isupper()==by and(p.upper()in'BQ'and dx and dy or p.upper()in'RQ'and not(dx and dy)):return 1
     break
    nx+=dx;ny+=dy
  return 0
 def gen(s):
  b=s.b;w=s.w;ms=[];A=ms.append
  for sq in range(64):
   p=b[sq]
   if p=='.'or p.isupper()!=w:continue
   u=p.upper();x,y=sq&7,sq>>3
   if u=='P':
    d=1 if w else-1;t=sq+8*d;last=6 if w else 1
    if b[t]=='.':
     A((sq,t,'Q'if y==last else''))
     if y==(1 if w else 6)and b[sq+16*d]=='.':A((sq,sq+16*d,''))
    for dx in(-1,1):
     if 0<=x+dx<8:
      t=sq+8*d+dx
      if t==s.ep or b[t]!='.'and b[t].isupper()!=w and b[t].upper()!='K':A((sq,t,'Q'if y==last else''))
    continue
   ds=KN if u=='N'else D8 if u in'KQ'else D8[:4]if u=='R'else D8[4:]
   for dx,dy in ds:
    nx,ny=x+dx,y+dy
    while 0<=nx<8 and 0<=ny<8:
     t=ny*8+nx;q=b[t]
     if q=='.':A((sq,t,''))
     else:
      if q.isupper()!=w and q.upper()!='K':A((sq,t,''))
      break
     if u in'NK':break
     nx+=dx;ny+=dy
  return ms
 def make(s,m):
  fr,to,pr=m;b=s.b;p=b[fr];u=(b[to],s.ep,-1)
  if p.upper()=='P'and to==s.ep and fr&7!=to&7:u=(b[to],s.ep,to-8 if s.w else to+8);b[u[2]]='.'
  b[to]=(pr if s.w else pr.lower())if pr else p;b[fr]='.';s.ep=fr+(to-fr)//2 if p.upper()=='P'and abs(to-fr)==16 else-1;s.w=not s.w;return u
 def unmake(s,m,u):
  fr,to,pr=m;cap,ep,cs=u;b=s.b;s.w=not s.w;b[fr]=('P'if s.w else'p')if pr else b[to];b[to]=cap
  if cs>=0:b[to]='.';b[cs]='p'if s.w else'P'
  s.ep=ep
 def legal(s):
  out=[]
  for m in s.gen():
   u=s.make(m)
   if not s.atk(s.b.index('K'if not s.w else'k'),s.w):out.append(m)
   s.unmake(m,u)
  return out
def ev(s):
 sc=0
 for sq,p in enumerate(s.b):
  if p!='.':
   u=p.upper();v=V[u]+(ord(S[u][sq if p.isupper()else sq^56])-80 if u in S else 0);sc+=v if p.isupper()else-v
 return sc if s.w else-sc
nd=0
def sr(s,d,a,be):
 global nd;nd+=1
 if nd>15000:return ev(s)
 ms=s.legal();k=s.b.index('K'if s.w else'k')
 if not ms:return-I if s.atk(k,not s.w)else 0
 if d<=0:
  st=ev(s)
  if st>=be:return be
  a=max(a,st)
  if not s.atk(k,not s.w):ms=[m for m in ms if s.b[m[1]]!='.'or m[1]==s.ep or m[2]]
  if not ms:return a
 best=[-I,a][d<=0]
 for m in sorted(ms,key=lambda m:-V.get(s.b[m[1]].upper(),0)):
  u=s.make(m);sc=-sr(s,d-1,-be,-a);s.unmake(m,u);best=max(best,sc);a=max(a,sc)
  if a>=be:break
 return best
def best(s):
 global nd;nd=0;ms=s.legal();rs={}
 for d in 1,2:
  a=-I
  for m in sorted(ms,key=lambda m:-rs.get(m,0)):
   if d>1 and nd>13000:break
   u=s.make(m);v=-sr(s,d,-I,I);s.unmake(m,u)
   if v>a:a=v
   if nd<15000:rs[m]=v
 return max(ms,key=lambda m:rs.get(m,-I))
def um(m):return'%c%d%c%d%s'%(97+(m[0]&7),m[0]//8+1,97+(m[1]&7),m[1]//8+1,m[2].lower())
import json,os,urllib.request as R
U=os.getenv('MAKEFUN_ENV_URL')
def post(p,b):
 q=R.Request(U+p,data=json.dumps(b).encode())
 return json.load(R.urlopen(q))
s=P()
while 1:
 g=post('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  s.fen(g['fen']);m=um(best(s));g=post('/move',{'game':g['game'],'move':m})
