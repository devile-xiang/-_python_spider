#encoding:utf-8


from tkinter import *
import tkinter.messagebox as mebox

def helloworld():
    mebox.showinfo("渣男解释","渣男是一个网络流行词语，是指自私、擅长索取、不负责任，玩弄别人感情的男人。或指用情不专的男人。")


def main():
    root=Tk()

    li=["C","python","php","html","SQL","Java"]
    movie=["CSS","jQuery","Bootstrap"]
    listb=Listbox(root)
    listb2=Listbox(root)
    for item in li:
        listb.insert(0,item)
    w=Button(root,text="渣男",activebackground="#66ff66",command=helloworld)
    for item in movie:
        listb2.insert(0,item)


    w.pack()
    listb.pack()
    listb2.pack()
    root.mainloop()





if __name__ == '__main__':
    main()