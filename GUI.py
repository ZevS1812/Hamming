from hamming import Hamming
from tkinter import *
import math
from tkinter import filedialog
def run(ukazatel):
    def cod(IshodniyMassiv):
        
        IshodniyMassivBit=[]
        for bait in IshodniyMassiv:
            DvoichniyVidBaita=[]
            while bait>0:
                DvoichniyVidBaita.append(bait%2)
                bait=bait//2
            DvoichniyVidBaita.reverse()
            while len(DvoichniyVidBaita)<8:
                DvoichniyVidBaita.insert(0,0)
            IshodniyMassivBit=IshodniyMassivBit+DvoichniyVidBaita
            
        if ukazatel==1:
            schetchik=math.ceil(len(IshodniyMassivBit)/k)
        else:
            schetchik=len(IshodniyMassivBit)//n
            
        VihodnoyMassivBit=[]
        for i in range(schetchik):
            IshodnoeKodSlovo=IshodniyMassivBit[nk*i:nk*(i+1)]
            if ukazatel==1:
                while len(IshodnoeKodSlovo)!=nk:
                    IshodnoeKodSlovo.append(0)
                VihodKodSlovo=Hamming.encode(IshodnoeKodSlovo)
            else:
                VihodKodSlovo=Hamming.decode(IshodnoeKodSlovo)
            VihodnoyMassivBit=VihodnoyMassivBit+VihodKodSlovo
            
        if ukazatel==1:
            schetchik=math.ceil(len(VihodnoyMassivBit)/8)
        else:
            schetchik=len(VihodnoyMassivBit)//8
            
        VihodnoyMassivBait=[]
        for i in range(schetchik):
            VihodBait=VihodnoyMassivBit[8*i:8*(i+1)]
            if ukazatel==1:
                while len(VihodBait)!=8:
                    VihodBait.append(0)
            DvoichnayStroka=''.join(map(str,VihodBait))
            VihodnoyMassivBait.append(int(DvoichnayStroka,2))
            
        return(VihodnoyMassivBait)

    
    k=int(txt1.get())
    n=k
    r=0
    while n>=2**r:
        n=n+1
        r=r+1
    if ukazatel==1:
        nk=k
        textRezultata='Файл успешно закодирован \n('+str(n)+'; '+str(k)+')-кодом Хэмминга'
    else:
        nk=n
        textRezultata='Файл успешно декодирован \n('+str(n)+'; '+str(k)+')-кодом Хэмминга'
    file=open(txt.get(), "rb")
    newfile=open(txt0.get(),'ab')
    IshodniyMassiv=True
    while IshodniyMassiv:
        IshodniyMassiv=list(file.read(nk))
        VihodnoyMassivBait=cod(IshodniyMassiv)
        newfile.write(bytes(VihodnoyMassivBait))
    file.close()
    newfile.close()
    window2=Toplevel()
    window2.geometry('+650+300')
    lbl = Label(window2, text=textRezultata, font=("Calibry", 10))  
    lbl.grid(column=0, row=0, padx=20, pady=10)
    window2.mainloop()
    
def openf():
    file = filedialog.askopenfilename()
    txt.delete(0,END)
    txt.insert(0, file)
    
window = Tk()
window.title("Hammihg")
window.geometry('400x230+550+250')
frame=Frame()
frame0=Frame()
frame1=Frame()
frame2=Frame()
lbl = Label(frame, text="Укажите путь к обрабатываемому файлу", font=("Calibry", 10))  
lbl.grid(column=0, row=0, sticky=W)
txt = Entry(frame,width=50)  
txt.grid(column=0, row=1)
frame.grid(column=0, row=0, padx=20, pady=10, sticky=S)
btn = Button(window, text="Обзор", command=openf)  
btn.grid(column=1, row=0,pady=8,sticky=S)
lbl0 = Label(frame0, text="Укажите имя результирующего файла", font=("Calibry", 10))  
lbl0.grid(column=0, row=0, sticky=W)
txt0 = Entry(frame0,width=50)  
txt0.grid(column=0, row=1)
frame0.grid(column=0, row=1, padx=20, pady=10, sticky=S)
lbl1 = Label(frame1, text="Укажите параметр k (n;k)-кода Хэмминга", font=("Calibry", 10))  
lbl1.grid(column=0, row=0)
txt1 = Entry(frame1,width=8)  
txt1.grid(column=1, row=0)
frame1.grid(column=0, row=2, sticky=W, padx=20, pady=20)
btn = Button(frame2, text="Закодировать", command=lambda:run(1))  
btn.grid(column=0, row=0,padx=55)
btn = Button(frame2, text="Декодировать", command=lambda:run(0))  
btn.grid(column=1, row=0, padx=55)
frame2.grid(column=0, row=3, columnspan=2)
window.mainloop()
