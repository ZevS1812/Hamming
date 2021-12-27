import math,time
from hamming import Hamming
start=time.time()
def cod(f):
    d=[]
    for i in f:
        b=[]
        while i>0:
            n=i%2
            b.append(n)
            i=i//2
        b.reverse()
        while len(b)<8:
            b.insert(0,0)
        d=d+b
    h=[]
    for i in range(math.ceil(len(d)/k)):
        g=d[k*i:k*(i+1)]
        while len(g)!=k:
            g.append(0)
        a=Hamming.encode(g)
        h=h+a
    v=[]
    for i in range(math.ceil(len(h)/8)):
        g=h[8*i:8*(i+1)]
        while len(g)!=8:
            g.append(0)
        m=''.join(map(str,g))
        v.append(int(m,2))      
    return(v)
k=26
n=k
r=0
while n>=2**r:
    n=n+1
    r=r+1
file=open("fff/88.JPG", "rb")
newfile=open('fff/encod.JPG','ab')
f=True
while f:
    f=file.read(k)
    f=list(f)
    v=cod(f)
    vv=bytes(v)
    newfile.write(vv)
file.close()
newfile.close()
print(time.time()-start)
