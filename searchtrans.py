from tkinter import *
from tkinter import messagebox
import webbrowser
t1='Tip:多个关键词可以用"|"隔开'
root = Tk()
# 设置窗口前段显示
root.wm_attributes('-topmost',1)
#设置居中显示
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
width = 400
height = 260
size = "%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(size)
# 设置窗口标题及大小
root.title('多关键词搜索1.0|QQ403096966')
#设置接受UI界面中Label和它的位置
var = StringVar()
var.set(t1)
url_input=Label(root,textvariable=var,width=21,height=1,font=("微软雅黑",12))
url_input.grid(row=0,column=0,columnspan=3)
# 设置搜索框
t = Entry(root,width=40,font=("微软雅黑",12),text="请在这里输入搜索词...")
t.insert(0, "请在这里输入搜索词...")
#设置entry获得焦点
t.focus_set()
t.grid(row=1,column=0,columnspan=3,padx=10)
#设置右键菜单
def callback1(event=None):
    t.event_generate('<<Cut>>')
def callback2(event=None):
    t.event_generate('<<Copy>>')
def callback3(event=None):
    t.event_generate('<<Paste>>')
#设置退出按钮
def b_quitprog(event=None):
    root.destroy()
def b_clear(event=None):
    var.set(t1)
    t.delete(0,END)
def search(lst,path):
    for i in lst:
        name = path + i  #组合生成下载地址
        wb= webbrowser.get('windows-default') #指定windows默认浏览器
        wb.open(name)
def b_baidu(event=None):
    var.set('正在进行百度搜索...')
    path="https://www.baidu.com/s?wd="
    b_showup(path,event=None)
def b_Bing(event=None):
    var.set('正在进行Bing搜索...')
    path= "https://cn.bing.com/search?q="
    b_showup(path,event=None)
def b_Google(event=None):
    var.set('正在进行Google搜索...')
    path= "https://fsoufsou.com/search?q="
    b_showup(path,event=None)
def search_all():
    b_baidu(),b_Bing(),b_Google()
def b_fanyi(event=None):
    var.set("百度翻译")
    path = "https://fanyi.baidu.com/#zh/en/"
    b_showup(path,event=None)
def b_showup(path,event=None):
    url=str(t.get())
    if url=="":
        messagebox.showinfo("错误提示！","请录入检索词！")
    else:
        try:
            urls=url.split("|")
            search(urls,path)
        except Exception as exc:
            messagebox.showinfo("警告！",f"{exc}输入错误！")
def main():
    #设置按纽
    b_quit = Button(root,text="翻译(F3)",width=10,height=1,font=("微软雅黑",12),command=b_fanyi)
    b_down = Button(root,text='清空(Esc)',width=10,height=1,font=("微软雅黑",12),command=b_clear)
    b_show = Button(root,text='一键搜索',fg="blue",width=10,height=1,font=("微软雅黑",12),command=search_all)
    b_tips = Label(root,text='F1|F2|F3|Esc为快捷键',width=37,height=1,font=("微软雅黑",12))
    #设置按纽布局
    b_quit.grid(row=4,column=0)
    b_show.grid(row=4,column=1)
    b_down.grid(row=4,column=2)
    b_tips.grid(row=6,column=0,columnspan=3)
    #设置按纽
    baidu= Button(root,text="百度(F1)",width=10,height=1,font=("微软雅黑",12),command=b_baidu)
    Bing = Button(root,text="Bing(F2)",width=10,height=1,font=("微软雅黑",12),command=b_Bing)
    Google= Button(root,text="Google(回车)",width=10,height=1,font=("微软雅黑",12),command=b_Google)
    #设置按纽网格布局
    baidu.grid(row=3,column=0)
    Bing.grid(row=3,column=1)
    Google.grid(row=3,column=2)
    def popup(event):
        menu.post(event.x_root, event.y_root)
    #绑定快捷键
    t.bind("<Return>", b_Google)
    t.bind("<Button-3>", popup)
    t.bind_all("<F1>",b_baidu)
    t.bind_all("<F2>",b_Bing)
    b_down.bind_all("<Escape>",b_clear)
    b_quit.bind_all("<F3>",b_fanyi)
    #设置文本框右键菜单
    menu = Menu(root,tearoff=False)#bg="black",
    menu.add_command(label="剪切", command=callback1)
    menu.add_command(label="复制", command=callback2)
    menu.add_command(label="粘贴", command=callback3)
    root.mainloop()
main()
    

