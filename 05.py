import os
from tkinter import *
from tkinter import filedialog as ft
from tkinter import messagebox as tmb

root = Tk()

root.title('zjj editor')

root.resizable(0,0)
root.geometry('800x600')

menu_bar =Menu(root)

content_text = Text(root,wrap='word')
content_text.pack(expand='yes',fill='both')
content_text.tag_config('active_line',background='#f1f1f1')

scroll_bar=Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right',fill='y')

def new_text(event=None):
    root.title("未命名文件")
    global file_name
    file_name = None

def save_as(Event=None):
    t = content_text.get("1.0","end-1c")
    save_location = ft.asksaveasfilename(defaultextension=".txt",filetypes=[("所有文件","*.*"),("文本文件","*.txt")])
    print(save_location)
    file1=open(save_location,"w+")
    file1.write(t)
    global file_name
    file_name = save_location
    print(os.path.basename(save_location))
    root.title('{} --- {}'.format(os.path.basename(save_location),"  || zjj editor"))
    file1.close()

def save(Event=None):
    global file_name
    if not file_name:
        save_as()
    else:
        t = content_text.get("1.0","end-1c")
        file1 = open(file_name,"w+")
        file1.write(t)
    return "break"

def openfile(event=None):
    input_file_name = ft.askopenfilename(defaultextension="*.txt",filetypes=[("所有文件","*.*"),("文本文件","*.txt")])

    if input_file_name:
        global file_name
        file_name = input_file_name
        root.title('{} --- {}'.format(os.path.basename(file_name),"  ||  新记事本"))
        content_text.delete(1.0,END)
        file = open(input_file_name,'r')
        if file != '':
            try:
                txt = file.read()
            except:
                tmb.showwarning("Invalid","Please select a valid file to open")
            content_text.insert(INSERT,txt)
        else:
            pass

def cut():
    content_text.event_generate("<<Cut>>")

def copy():
    content_text.event_generate("<<Copy>>")

def paste():
    content_text.event_generate("<<Paste>>")

def delete():
    content_text.event_generate("<<Delete>>")

def selectAll():
    content_text.event_generate("<<SelectAll>>")

def undo():
    content_text.event_generate("<<Undo>>")

def redo():
    content_text.event_generate("<<Redo>>")

def closefile():
    content_text.event_generate("<<Close>>")

def exit():
    if  tmb.askokcancel("退出？","真的退出？"):
        root.destroy()

def highlight(interval=100):
    content_text.tag_remove("active_live",1.0,"end")
    content_text.tag_add("active_line","insert linestart","insert lineend+lc")
    # content_text.after(interval,toggle_highlight)

def display_about_messagebox(event=None):
    tmb.showinfo(title="关于", message="这是一个简单的记事本，纯做演示讲解用。")


def display_help_messagebox(event=None):
    tmb.showinfo("帮助", "就这东西你还需要帮助。", icon='question')

def display_lience_messagebox(event=None):
    tmb.showinfo(title="许可", message="你想拿它干啥就干啥。")


def display_common_messagebox():
    tmb.showinfo(title='信息', message="不提供信息。")

file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='文件',menu=file_menu)
file_menu.add_command(label='新建',compound='left',accelerator='Ctrl+n',underline=0,command=new_text)
file_menu.add_command(label='打开',compound='left',accelerator='Ctrl+o',underline=0,command=openfile)
file_menu.add_separator()
file_menu.add_command(label='保存',compound='left',accelerator='Ctrl+s',underline=0,command=save)
file_menu.add_command(label='另存为...',compound='left',accelerator='Ctrl+Shift+s',underline=1,command=save_as)
file_menu.add_separator()
file_menu.add_command(label='关闭',compound='left',accelerator='Alt+F4',underline=0,command=closefile)
file_menu.add_command(label='退出',compound='left',command=exit,underline=0)

edit_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='编辑',menu=edit_menu)
edit_menu.add_command(label='返回',accelerator='Ctrl+z',command=undo)
edit_menu.add_command(label='重做',command=redo)
edit_menu.add_separator()
edit_menu.add_command(label='剪切',accelerator='Ctrl+x',command=cut)
edit_menu.add_command(label='复制',accelerator='Ctrl+c',command=copy)
edit_menu.add_command(label='黏贴',accelerator='Ctrl+v',command=paste)
edit_menu.add_command(label='删除',accelerator='del',command=delete)
edit_menu.add_separator()
edit_menu.add_command(label='选定所有',accelerator='Ctrl+a',command=selectAll)
edit_menu.add_command(label='查找',accelerator='Ctrl+f',command=display_common_messagebox)

view_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='视图',menu=view_menu)
view_menu.add_command(label='全屏',accelerator='Ctrl+f11')

about_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='关于',menu=about_menu)
about_menu.add_command(label='关于我',command=display_about_messagebox)

help_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='帮助',menu=help_menu)
help_menu.add_command(label='帮助索引',command=display_help_messagebox)
help_menu.add_command(label='许可',command=display_lience_messagebox)

root.config(menu=menu_bar)
root.mainloop()