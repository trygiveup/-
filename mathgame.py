# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 23:31:16 2021

@author: 國超
"""

import tkinter as tk
import random
import tkinter.messagebox as warn
win=tk.Tk()
win.title('數字遊戲')
win.geometry("600x480+100+100")
win.config(bg="lightskyblue")
var=tk.StringVar()
var3=tk.StringVar()
y=[]
count=8

def play2():
    try:
        play()
    except ValueError:
        warn.showerror(title=('警告'),message=('有非數字的字元'))
def mathgame():
    x=list(range(0,10))
    random.shuffle(x)
    return x[0:4]
a,b,c,d=mathgame()
str(a)
print(a,b,c,d)
def play():
    global count
    z=var.get()
    var.set('')
    A,B=0,0
    aa=int(z[0:1])
    bb=int(z[1:2])
    cc=int(z[2:3])
    dd=int(z[3:4])
    if aa==bb or aa==cc or aa==dd or bb==cc or bb==dd or cc==dd:
        warn.showwarning('警告','數字不能重複')
        #var3.set('數字不能重複')
    elif len(z)!=4 or len(z)<4:
        warn.showwarning('警告','數字長度超過限制')
        #var3.set('數字不能重複')
    else:
        count-=1
        if count<0:
            var3.set('GAME OVER')
        else:
            if a==aa:
                A+=1
            if a==bb or a==cc or a==dd:
                B+=1
            if b==bb:
                A+=1
            if b==aa or b==cc or b==dd:
                B+=1
            if c==cc:
                A+=1
            if c==bb or c==aa or c==dd:
                B+=1
            if d==dd:
                A+=1
            if d==bb or d==cc or d==aa:
                B+=1
            var3.set('剩餘{}次機會'.format(count))
            var2="{}\t{}A{}B".format(z,A,B)
        if A==4:
            if count>6:
                var3.set('你根本就是偷看答案嘛')
            elif count>4:
                var3.set('你真神')
            elif count>2:
                var3.set('你贏了,你真厲害')
            else:
                var3.set('YOU WIN')
            
        answer['state']=tk.NORMAL
        answer.insert(tk.INSERT,var2)
        answer['state']=tk.DISABLED
def restart():
    global a,b,c,d,count
    answer['state']=tk.NORMAL
    answer.delete('1.0','end')
    answer['state']=tk.DISABLED
    var3.set('重新開始')
    count=8
    a,b,c,d=mathgame()
rule_label=tk.Label(win,height=5,font=('Arial',16),bg='#00ff7f',
                    text='請輸入4個0~9不同的數字,\nA代表數字相同位置相同,B代表數字相同位置不同,\n4個數字位置皆正確既獲得勝利').pack(fill=tk.BOTH)
limit_label=tk.Label(win,height=1,fg='red',font=('Arial',20),bg='lightskyblue',
                    textvariable=var3).place(x=145,y=150)
guess_label=tk.Label(win,font=('Arial',16),bg='lightskyblue',text='請輸入4個數字').place(x=0,y=200)
guess_entry=tk.Entry(win,width=10,font=('Arial',16),textvariable=var).place(x=180,y=200)
guess_button=tk.Button(win,font=('Arial',12),state=tk.NORMAL,text='輸入',command=play2).place(x=220,y=230)
answer=tk.Text(win,width=13,height=8,bg='#6495ed',font=('Arial',16))
answer.place(x=435,y=130)
guess_button=tk.Button(win,font=('Arial',12),state=tk.NORMAL,text='重新開始',command=restart).place(x=0,y=450)

win.mainloop()

