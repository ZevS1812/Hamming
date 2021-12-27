class Hamming:
    def __init__(self):
        pass
    def encode(posledovatelnost):
        i=0
        NomerKontrlBity=[]
        while 2**i<=len(posledovatelnost):
            posledovatelnost.insert(2**i-1,0)
            NomerKontrlBity.append(2**i)
            i=i+1
            
        for i in NomerKontrlBity:
            SummaBit=0
            for j in range(i-1,len(posledovatelnost),2*i):
                l=i
                z=0
                while l>0 and j+z<len(posledovatelnost):
                    SummaBit=SummaBit+posledovatelnost[j+z]
                    l=l-1
                    z=z+1
            if SummaBit%2==1:
                posledovatelnost[i-1]=1
        return(posledovatelnost)
    
    def decode(posledovatelnost):
        i=0
        NomerKontrlBity=[]
        while 2**i<=len(posledovatelnost):
            NomerKontrlBity.append(2**i)
            i=i+1
            
        KontrlBity=[]
        for i in NomerKontrlBity:
            KontrlBity.append(posledovatelnost[i-1])
            posledovatelnost[i-1]=0
            
        for i in NomerKontrlBity:
            SummaBit=0
            for j in range(i-1,len(posledovatelnost),2*i):
                l=i
                z=0
                while l>0 and j+z<len(posledovatelnost):
                    SummaBit=SummaBit+posledovatelnost[j+z]
                    l=l-1
                    z=z+1
            if SummaBit%2==1:
                posledovatelnost[i-1]=1
                
        oshibka=0
        for i in range(len(NomerKontrlBity)):
            if KontrlBity[i]!=posledovatelnost[NomerKontrlBity[i]-1]:
                oshibka=oshibka+NomerKontrlBity[i]
                
        if oshibka>0:
            posledovatelnost[oshibka-1]=(posledovatelnost[oshibka-1]+1)%2
            
        for i in NomerKontrlBity[::-1]:
            posledovatelnost.pop(i-1)
        return(posledovatelnost)
