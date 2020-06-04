# Author: https://github.com/blackw4tch/
from PIL import Image, ImageFont
from handright import Template, handwrite
import tkinter , os , random
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

root = tkinter.Tk()
root.title("手写转换器v1.0 by 黑色守望")
root.geometry("475x400")
pathshow = tkinter.StringVar()
fontshow = tkinter.StringVar()
path = ""
afont = ""
font_size_show = tkinter.StringVar()
line_spacing_show = tkinter.StringVar()
word_spacing_show = tkinter.StringVar()
line_spacing_sigma_show = tkinter.StringVar()
word_spacing_sigma_show = tkinter.StringVar()
font_size_sigma_show = tkinter.StringVar()
perturb_theta_sigma_show = tkinter.StringVar()
perturb_x_sigma_show = tkinter.StringVar()
perturb_y_sigma_show = tkinter.StringVar()
line_spacing = 125
font_size = 100
word_spacing = 2
line_spacing_sigma = 2  # 行间距随机扰动
word_spacing_sigma = 3  # 字间距随机扰动
font_size_sigma = 4  # 字体大小随机扰动
perturb_theta_sigma = 0.06  # 笔画旋转偏移随机扰动
perturb_x_sigma = 3  # 笔画横向偏移随机扰动
perturb_y_sigma = 3  # 笔画纵向偏移随机扰动
font_size_show.set(font_size)
line_spacing_show.set(line_spacing)
word_spacing_show.set(word_spacing)
line_spacing_sigma_show.set(line_spacing_sigma)
word_spacing_sigma_show.set(word_spacing_sigma)
font_size_sigma_show.set(font_size_sigma)
perturb_theta_sigma_show.set(perturb_theta_sigma)
perturb_x_sigma_show.set(perturb_x_sigma)
perturb_y_sigma_show.set(perturb_y_sigma)
def getpath():
    global path
    path_ = tkinter.filedialog.askopenfilename()
    path = path_.replace("\\", "/")
    pathshow.set(path)
def getfont():
    global afont
    afont = tkinter.filedialog.askopenfilename()
    font = afont.replace("\\", "/")
    fontshow.set(font)
def startswitch():
    global font_size,line_spacing,word_spacing,line_spacing_sigma,font_size_sigma,perturb_y_sigma, perturb_x_sigma_show,perturb_theta_sigma
    template = Template(
        background=Image.new(mode="1", size=(2479, 3508), color=1),
        font_size=font_size,
        line_spacing=line_spacing,  # 行间距
        word_spacing=word_spacing,  # 字间距
        line_spacing_sigma=line_spacing_sigma,  # 行间距随机扰动
        word_spacing_sigma=word_spacing_sigma,  # 字间距随机扰动
        font_size_sigma=font_size_sigma,  # 字体大小随机扰动
        perturb_theta_sigma=perturb_theta_sigma,  # 笔画旋转偏移随机扰动
        perturb_x_sigma=perturb_x_sigma,  # 笔画横向偏移随机扰动
        perturb_y_sigma=perturb_y_sigma,  # 笔画纵向偏移随机扰动
        font=ImageFont.truetype(afont),
    )
    if font_size > line_spacing:
        tkinter.messagebox.showwarning(title = "stupid" , message = "字体大小必须小于行间距，你以为？")
    else:
        with open(path, "r", encoding='UTF-8') as f:
            text = f.read()
            images = handwrite(text, template)
            for i, im in enumerate(images):
                assert isinstance(im, Image.Image)
                isExists = os.path.exists("images")
                if not isExists:
                    os.mkdir("images")
                im.show()
                n = random.random()
                im.save("images/{}.jpg".format(n))
        os.system("start explorer images")


def font_size_add():
    global font_size
    font_size = font_size + 1
    font_size_show.set(font_size)
def line_spacing_add():
    global line_spacing
    line_spacing = line_spacing + 1
    line_spacing_show.set(line_spacing)
def word_spacing_add():
    global word_spacing
    word_spacing = word_spacing + 1
    word_spacing_show.set(word_spacing)
def line_spacing_sigma_add():
    global line_spacing_sigma
    line_spacing_sigma = line_spacing_sigma + 1
    line_spacing_sigma_show.set(line_spacing_sigma)
def word_spacing_sigma_add():
    global word_spacing_sigma
    word_spacing_sigma = word_spacing_sigma + 1
    word_spacing_sigma_show.set(word_spacing_sigma)
def font_size_sigma_add():
    global font_size_sigma
    font_size_sigma = font_size_sigma + 1
    font_size_sigma_show.set(font_size_sigma)
def perturb_theta_sigma_add():
    global perturb_theta_sigma
    perturb_theta_sigma = perturb_theta_sigma + 0.01
    perturb_theta_sigma_show.set(perturb_theta_sigma)
def perturb_x_sigma_add():
    global perturb_x_sigma
    perturb_x_sigma = perturb_x_sigma + 1
    perturb_x_sigma_show.set(perturb_x_sigma)
def perturb_y_sigma_add():
    global perturb_y_sigma
    perturb_y_sigma = perturb_y_sigma +1
    perturb_y_sigma_show.set(perturb_y_sigma)
def font_size_sub():
    global font_size
    font_size = font_size - 1
    font_size_show.set(font_size)
def line_spacing_sub():
    global line_spacing
    line_spacing = line_spacing - 1
    line_spacing_show.set(line_spacing)
def word_spacing_sub():
    global word_spacing
    word_spacing = word_spacing - 1
    word_spacing_show.set(word_spacing)
def line_spacing_sigma_sub():
    global line_spacing_sigma
    line_spacing_sigma = line_spacing_sigma - 1
    line_spacing_sigma_show.set(line_spacing_sigma)
def word_spacing_sigma_sub():
    global word_spacing_sigma
    word_spacing_sigma = word_spacing_sigma - 1
    word_spacing_sigma_show.set(word_spacing_sigma)
def font_size_sigma_sub():
    global font_size_sigma
    font_size_sigma = font_size_sigma - 1
    font_size_sigma_show.set(font_size_sigma)
def perturb_theta_sigma_sub():
    global perturb_theta_sigma
    perturb_theta_sigma = perturb_theta_sigma - 0.01
    perturb_theta_sigma_show.set(perturb_theta_sigma)
def perturb_x_sigma_sub():
    global perturb_x_sigma
    perturb_x_sigma = perturb_x_sigma - 1
    perturb_x_sigma_show.set(perturb_x_sigma)
def perturb_y_sigma_sub():
    global perturb_y_sigma
    perturb_y_sigma = perturb_y_sigma - 1
    perturb_y_sigma_show.set(perturb_y_sigma)

tkinter.Label(root, text="have fun!").grid(row=0, column=1)
tkinter.Label(root, text="文本路径").grid(row=1, column=0)
tkinter.Entry(root, textvariable=pathshow, bd=3, width=25).grid(row=1, column=1)
bgetpath = tkinter.Button(root, text="选择文本", command=getpath).grid(row=1, column=3)
tkinter.Label(root, text="字体路径").grid(row=2, column=0)
tkinter.Entry(root, textvariable=fontshow, bd=3, width=25).grid(row=2, column=1)
bgetfont = tkinter.Button(root, text="选择字体", command=getfont).grid(row=2, column=3)
bstartswitch = tkinter.Button(root, text="开始转换", command=startswitch).grid(row=3, column=1)

bfont_size_add = tkinter.Button(root, text="+", command=font_size_add,width=5).grid(row=4, column=4)
tkinter.Label(root , text = "字体大小必须小于行间距")
tkinter.Entry(root, textvariable=font_size_show, bd=3, width=5).grid(row=4, column=2)
tkinter.Label(root,text= "字体大小").grid(row=4,column=0)

bline_spacing_add = tkinter.Button(root, text="+", command=line_spacing_add,width=5).grid(row=5, column=4)
tkinter.Entry(root, textvariable=line_spacing_show, bd=3, width=5).grid(row=5, column=2)
line_spacing = int(line_spacing_show.get())
tkinter.Label(root,text= "行间距").grid(row=5,column=0)

bword_spacing_add = tkinter.Button(root, text="+", command=word_spacing_add,width=5).grid(row=6, column=4)
tkinter.Entry(root, textvariable=word_spacing_show, bd=3, width=5).grid(row=6, column=2)
word_spacing = int(word_spacing_show.get())
tkinter.Label(root,text= "字间距").grid(row=6,column=0)

bline_spacing_sigma_add = tkinter.Button(root,text="+", command=line_spacing_sigma_add,width=5).grid(row=7,column=4)
tkinter.Entry(root, textvariable=line_spacing_sigma_show, bd=3, width=5).grid(row=6, column=2)
line_spacing_sigma = int(line_spacing_sigma_show.get())
tkinter.Label(root,text= "行间距随机扰动").grid(row=6,column=0)

bword_spacing_sigma_add = tkinter.Button(root,text="+",command=word_spacing_sigma_add,width=5).grid(row=7,column=4)
tkinter.Entry(root, textvariable=word_spacing_sigma_show, bd=3, width=5).grid(row=7, column=2)
word_spacing_sigma = int(word_spacing_sigma_show.get())
tkinter.Label(root,text= "字间距随机扰动").grid(row=7,column=0)

bfont_size_sigma_add = tkinter.Button(root,text="+",command=font_size_sigma_add,width=5).grid(row=8,column=4)
tkinter.Entry(root, textvariable=font_size_sigma_show, bd=3, width=5).grid(row=8, column=2)
font_size_sigma = int(font_size_sigma_show.get())
tkinter.Label(root,text= "字体大小随机扰动").grid(row=8,column=0)

bperturb_theta_sigma_add = tkinter.Button(root,text="+",command=perturb_theta_sigma_add,width=5).grid(row=9,column=4)
tkinter.Entry(root, textvariable=perturb_theta_sigma_show, bd=3, width=5).grid(row=9, column=2)
perturb_theta_sigma = float(perturb_theta_sigma_show.get())
tkinter.Label(root,text= "笔画旋转偏移随机扰动").grid(row=9,column=0)

bperturb_x_sigma_add = tkinter.Button(root,text="+",command=perturb_x_sigma_add,width=5).grid(row=10,column=4)
tkinter.Entry(root, textvariable=perturb_x_sigma_show, bd=3, width=5).grid(row=10, column=2)
perturb_x_sigma = int(perturb_x_sigma_show.get())
tkinter.Label(root,text= "笔画横向偏移随机扰动").grid(row=10,column=0)

bperturb_y_sigma_add = tkinter.Button(root,text="+",command=perturb_y_sigma_add,width=5).grid(row=11,column=4)
tkinter.Entry(root, textvariable=perturb_y_sigma_show, bd=3, width=5).grid(row=11, column=2)
perturb_y_sigma = int(perturb_y_sigma_show.get())
tkinter.Label(root,text= "笔画纵向偏移随机扰动").grid(row=11,column=0)

bfont_size_sub = tkinter.Button(root, text="-", command=font_size_sub,width=5).grid(row=4, column=1)
bline_spacing_sub = tkinter.Button(root, text="-", command=line_spacing_sub,width=5).grid(row=5, column=1)
bword_spacing_sub = tkinter.Button(root, text="-", command=word_spacing_sub,width=5).grid(row=5, column=1)
bline_spacing_sigma_sub = tkinter.Button(root,text="-",command=line_spacing_sigma_sub,width=5).grid(row=6,column=1)
bword_spacing_sigma_sub = tkinter.Button(root,text="-",command=word_spacing_sigma_sub,width=5).grid(row=7,column=1)
bfont_size_sigma_sub = tkinter.Button(root,text="-",command=font_size_sigma_sub,width=5).grid(row=8,column=1)
bperturb_theta_sigma_sub = tkinter.Button(root,text="-",command=perturb_theta_sigma_sub,width=5).grid(row=9,column=1)
bperturb_x_sigma_sub = tkinter.Button(root,text="-",command=perturb_x_sigma_sub,width=5).grid(row=10,column=1)
bperturb_y_sigma_sub = tkinter.Button(root,text="-",command=perturb_y_sigma_sub,width=5).grid(row=11,column=1)






root.mainloop()
