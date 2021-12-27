from hamming import Hamming
import time
start=time.time()
def decod(f):
    d=[]
    for i in f:
        b=[]
        while i>0:
            u=i%2
            b.append(u)
            i=i//2
        b.reverse()
        while len(b)<8:
            b.insert(0,0)
        d=d+b
    h=[]
    for i in range(len(d)//n):
        g=d[n*i:n*(i+1)]
        a=Hamming.decode(g)
        h=h+a
    v=[]
    for i in range(len(h)//8):
        g=h[8*i:8*(i+1)]
        m=''.join(map(str,g))
        v.append(int(m,2))
    return(v)
k=26
n=k
r=0
while n>=2**r:
    n=n+1
    r=r+1
file=open("fff/encod.JPG", "rb")
newfile=open('fff/decode.JPG','ab')
f=True
while f:
    f=file.read(n)
    f=list(f)
    v=decod(f)
    vv=bytes(v)
    newfile.write(vv)
file.close()
newfile.close()
print(time.time()-start)
