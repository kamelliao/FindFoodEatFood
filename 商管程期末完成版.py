import tkinter as tk
import tkinter.font as tkFont
import pandas as pd
import numpy as np
from PIL import Image
from PIL import ImageTk
import random
import datetime
import webbrowser
import time

list1 = ['地點', []]  #記錄數值list
info = {'region' : [], 'Category' : [], 'Subcategory' : None}  #紀錄數值2
gamelist = []  #點選食物選項的list

class root(tk.Tk):  #基底視窗
    def __init__(self):  #視窗驅動
        tk.Tk.__init__(self)
        self.geometry('500x650')  #視窗大小
        self.title('FindEat 找食瞭瞭')  #視窗名稱
        self._frame = None
        self.switch_frame(FirstPage)

    def switch_frame(self, frame_class):  #一般轉換畫面
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  #破壞原先視畫面替換成新畫面
        self._frame = new_frame
        self._frame.pack()

    def switch_frame2(self, frame_class, var, var2):  #轉換畫面過程與紀錄餐廳地區數值
        global list1
        global info
        list1[0] = var
        info['region'].append(var2)
        
        print(list1)
        print(info)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  #破壞原先視畫面替換成新畫面
        self._frame = new_frame
        self._frame.pack()

    def switch_frame2_5(self, frame_class, var, var2, var3, var4):  #轉換畫面過程與紀錄餐廳地區數值(選擇都可以)
        global list1
        global info
        list1[0] = var4
        info['region'].append(var)
        info['region'].append(var2)
        info['region'].append(var3)
        print(list1)
        print(info)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  #破壞原先視畫面替換成新畫面
        self._frame = new_frame
        self._frame.pack()
    def switch_frame3(self, frame_class, var):  #轉換畫面過程與紀錄食物種類(玩完小遊戲)
        global list1
        global info
        list1[1].append(var)
        info['Subcategory'] = var
        print(list1)
        print(info)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  #破壞原先視畫面替換成新畫面
        self._frame = new_frame
        self._frame.pack()

    def switch_game(self, frame_class, var):  #轉換畫面過程與紀錄心情選項(小遊戲)
        global gamelist
        gamelist.append(var)
        print(gamelist)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  #破壞原先視畫面替換成新畫面
        self._frame = new_frame
        self._frame.pack()

    def switch_game_back(self, frame_class):  #轉換畫面過程與移除心情選項(小遊戲)
        global gamelist
        gamelist.pop()
        print(gamelist)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  #破壞原先視畫面替換成新畫面
        self._frame = new_frame
        self._frame.pack()

    def switch_list1_back(self, frame_class):  #轉換畫面過程與移除地區選項(小遊戲)
        global list1
        info['region'] = []
        list1[1] = []
        print(list1)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  #破壞原先視畫面替換成新畫面
        self._frame = new_frame
        self._frame.pack()

    def switch_infoc_back(self, frame_class):  #轉換畫面過程與重製餐廳種類(餐廳)
        global info
        info['Category'] = []
        print(info)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  #破壞原先視畫面替換成新畫面
        self._frame = new_frame
        self._frame.pack()

    def switch_infop_back(self, frame_class):  #轉換畫面過程與重製地區種類(小遊戲)
        global info
        info['region'] = []
        print(info)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  #破壞原先視畫面替換成新畫面
        self._frame = new_frame
        self._frame.pack()

    def switch_home(self, frame_class):  #home鍵轉換畫面過程
        global gamelist
        global list1
        global info
        list1 = ['地點', []]
        gamelist = []
        info = {
        'region' : [],
        'Category' : [],
        'Subcategory' : None
        }
        print(list1)
        print(gamelist)
        print(info)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  #破壞原先視畫面替換成新畫面
        self._frame = new_frame
        self._frame.pack()

class FirstPage(tk.Frame):  #第一個選擇畫面

    def __init__(self, master):  #畫面驅動
        tk.Frame.__init__(self, master)
        self.configure(bg = '#FFEED2')  #畫面背景顏色
        self.creatWidgets()
        self.pack(fill = "both", expand = True)  #把place函數放進畫面

    def creatWidgets(self):      #畫面部件
        f1 = tkFont.Font(size = 35, family = 'jf open 粉圓 1.1')  #各式字體大小、字形
        f2 = tkFont.Font(size = 26, family = 'jf open 粉圓 1.1')
        f3 = tkFont.Font(size = 44, family = 'jf open 粉圓 1.1')

        self.lb1 = tk.Label(self, text = 'FindEat', bg = '#FFEED2', font = f1, fg = '#FFB140')    #開頭標題 FindEat
        self.lb2 = tk.Label(self, text = '找食瞭瞭', bg = '#FFEED2', font = f2, fg = '#FFB140')   #開頭標題 找食瞭瞭
        self.lb3 = tk.Label(self, text = '我想找...', bg = '#FFEED2', font = f3, fg = '#776262')  #開頭標題 我想找...

        image1 = Image.open("./前端圖片/食物.png")  #食物按鈕圖片檔案位置
        image1 = image1.resize((180, 100), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image1)
        self.button1 = tk.Button(self, image= self.image1, relief="flat", bg = '#FFEED2', command = lambda: root.switch_frame(self, Choose_Food))   #食物按鈕外型+跳轉命令
        
        image2 = Image.open("./前端圖片/餐廳.png")  #餐廳按鈕圖片檔案位置
        image2 = image2.resize((180, 95), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image2)
        self.button2 = tk.Button(self, image= self.image2, relief="flat", bg = '#FFEED2', command = lambda: root.switch_frame(self, Choose_Place))  #餐廳按鈕外型+跳轉命令

        self.lb1.place(x = 155, y = 45, anchor = 'nw')       #開頭標題 FindEat   擺放位置
        self.lb2.place(x = 166, y = 105, anchor = 'nw')      #開頭標題 找食瞭瞭  擺放位置
        self.lb3.place(x = 137, y = 285, anchor = 'nw')      #開頭標題 我想找... 擺放位置
        self.button1.place(x = 157, y = 350, anchor = 'nw')  #食物按鈕擺放位置
        self.button2.place(x = 157, y = 440, anchor = 'nw')  #餐廳按鈕擺放位置

        #以下不重要背景圖片
        bg1 = Image.open("./前端圖片/漢堡.png")
        bg1 = bg1.resize((100, 85), Image.ANTIALIAS)
        self.bg1 = ImageTk.PhotoImage(bg1)
        self.bglb1 = tk.Label(self, image= self.bg1, bg = '#FFEED2')
        
        bg2 = Image.open("./前端圖片/壽司.png")
        bg2 = bg2.resize((110, 100), Image.ANTIALIAS)
        self.bg2 = ImageTk.PhotoImage(bg2)
        self.bglb2 = tk.Label(self, image= self.bg2, bg = '#FFEED2')

        bg3 = Image.open("./前端圖片/咖啡杯.png")
        bg3 = bg3.resize((110, 95), Image.ANTIALIAS)
        self.bg3 = ImageTk.PhotoImage(bg3)
        self.bglb3 = tk.Label(self, image= self.bg3, bg = '#FFEED2')

        bg4 = Image.open("./前端圖片/熱狗.png")
        bg4 = bg4.resize((110, 95), Image.ANTIALIAS)
        self.bg4 = ImageTk.PhotoImage(bg4)
        self.bglb4 = tk.Label(self, image= self.bg4, bg = '#FFEED2')

        bg5 = Image.open("./前端圖片/薯條.png")
        bg5 = bg5.resize((110, 95), Image.ANTIALIAS)
        self.bg5 = ImageTk.PhotoImage(bg5)
        self.bglb5 = tk.Label(self, image= self.bg5, bg = '#FFEED2')

        bg6 = Image.open("./前端圖片/杯子蛋糕.png")
        bg6 = bg6.resize((110, 95), Image.ANTIALIAS)
        self.bg6 = ImageTk.PhotoImage(bg6)
        self.bglb6 = tk.Label(self, image= self.bg6, bg = '#FFEED2')

        bg7 = Image.open("./前端圖片/烤肉醬.png")
        bg7 = bg7.resize((110, 95), Image.ANTIALIAS)
        self.bg7 = ImageTk.PhotoImage(bg7)
        self.bglb7 = tk.Label(self, image= self.bg7, bg = '#FFEED2')

        bg8 = Image.open("./前端圖片/梨子.png")
        bg8 = bg8.resize((110, 95), Image.ANTIALIAS)
        self.bg8 = ImageTk.PhotoImage(bg8)
        self.bglb8 = tk.Label(self, image= self.bg8, bg = '#FFEED2')

        bg9 = Image.open("./前端圖片/甜筒.png")
        bg9 = bg9.resize((110, 95), Image.ANTIALIAS)
        self.bg9 = ImageTk.PhotoImage(bg9)
        self.bglb9 = tk.Label(self, image= self.bg9, bg = '#FFEED2')

        bg10 = Image.open("./前端圖片/雞腿.png")
        bg10 = bg10.resize((110, 95), Image.ANTIALIAS)
        self.bg10 = ImageTk.PhotoImage(bg10)
        self.bglb10 = tk.Label(self, image= self.bg10, bg = '#FFEED2')

        bg11 = Image.open("./前端圖片/牛奶.png")
        bg11 = bg11.resize((110, 95), Image.ANTIALIAS)
        self.bg11 = ImageTk.PhotoImage(bg11)
        self.bglb11 = tk.Label(self, image= self.bg11, bg = '#FFEED2')

        bg12 = Image.open("./前端圖片/冰淇淋.png")
        bg12 = bg12.resize((110, 95), Image.ANTIALIAS)
        self.bg12 = ImageTk.PhotoImage(bg12)
        self.bglb12 = tk.Label(self, image= self.bg12, bg = '#FFEED2')

        #背景圖片擺放位置
        self.bglb1.place(x = 17, y = 175, anchor = 'nw')     #漢堡擺放位置
        self.bglb2.place(x = 135, y = 170, anchor = 'nw')    #壽司擺放位置
        self.bglb3.place(x = 258, y = 170, anchor = 'nw')    #咖啡杯擺放位置
        self.bglb4.place(x = 381, y = 170, anchor = 'nw')    #熱狗擺放位置
        self.bglb5.place(x = 12, y = 300, anchor = 'nw')     #薯條擺放位置
        self.bglb6.place(x = 12, y = 430, anchor = 'nw')     #杯子蛋糕擺放位置
        self.bglb7.place(x = 12, y = 550, anchor = 'nw')     #烤肉醬擺放位置
        self.bglb8.place(x = 140, y = 550, anchor = 'nw')    #梨子擺放位置
        self.bglb9.place(x = 265, y = 550, anchor = 'nw')    #甜筒擺放位置
        self.bglb10.place(x = 381, y = 550, anchor = 'nw')   #雞腿擺放位置
        self.bglb11.place(x = 381, y = 430, anchor = 'nw')   #牛奶擺放位置
        self.bglb12.place(x = 381, y = 300, anchor = 'nw')   #冰淇淋擺放位置

class Choose_Place(tk.Frame):  #選擇餐廳後畫面

    def __init__(self, parent):  #畫面驅動
        tk.Frame.__init__(self, parent)
        self.configure(bg = '#FFE9C4')  #畫面背景顏色
        self.creatWidgets()
        self.pack(fill = "both", expand = True)  #把place函數放進畫面

    def creatWidgets(self):      #畫面部件
        f1 = tkFont.Font(size = 18, family = 'jf open 粉圓 1.1')  #各式字體大小、字形
        f2 = tkFont.Font(size = 30, family = 'jf open 粉圓 1.1')

        self.lb1 = tk.Label(self, text = 'FindEat   —   找食瞭瞭', bg = '#FFDEA7', font = f1, fg = '#FFB140')     #開頭標題 FindEat   —   找食瞭瞭
        self.lb2 = tk.Label(self, text = '現在想去哪吃飯呢?', bg = '#FFE9C4', font = f2, fg = '#6E6E6E')          #開頭標題 現在想去哪吃飯呢?

        map1 = Image.open("./前端圖片/地圖.png")      #地圖圖片檔案位置
        map1 = map1.resize((480, 320), Image.ANTIALIAS)
        self.map1 = ImageTk.PhotoImage(map1)
        self.lb3 = tk.Label(self, image= self.map1, relief="flat", bg = '#FFE9C4')

        image1 = Image.open("./前端圖片/溫州街.png")  #溫州街按鈕圖片檔案位置
        image1 = image1.resize((44, 104), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image1)
        if len(gamelist) == 0:
            self.button1 = tk.Button(self, image= self.image1, relief="flat", bg = '#776262', border = 0, command = lambda: root.switch_frame2(self, Choose_Type, '溫州街', 'wenzhou'))  #溫州街按鈕外型+跳轉命令
        else:
            self.button1 = tk.Button(self, image= self.image1, relief="flat", bg = '#776262', border = 0, command = lambda: root.switch_frame2(self, Final, '溫州街', 'wenzhou'))        #溫州街按鈕外型+跳轉命令

        image2 = Image.open("./前端圖片/公館.png")    #公館按鈕圖片檔案位置
        image2 = image2.resize((87, 36), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image2)
        if len(gamelist) == 0:
            self.button2 = tk.Button(self, image= self.image2, relief="flat", bg = '#776262', border = 0, command = lambda: root.switch_frame2(self, Choose_Type, '公館', 'gongguan'))   #公館按鈕外型+跳轉命令
        else:
            self.button2 = tk.Button(self, image= self.image2, relief="flat", bg = '#776262', border = 0, command = lambda: root.switch_frame2(self, Final, '公館', 'gongguan'))         #公館按鈕外型+跳轉命令

        image3 = Image.open("./前端圖片/118巷.png")   #118巷按鈕圖片檔案位置
        image3 = image3.resize((90, 40), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(image3)
        if len(gamelist) == 0:
            self.button3 = tk.Button(self, image= self.image3, relief="flat", bg = '#776262', border = 0, command = lambda: root.switch_frame2(self, Choose_Type, '118巷', '118'))       #118巷按鈕外型+跳轉命令
        else:
            self.button3 = tk.Button(self, image= self.image3, relief="flat", bg = '#776262', border = 0, command = lambda: root.switch_frame2(self, Final, '118巷', '118'))             #118巷按鈕外型+跳轉命令

        image4 = Image.open("./前端圖片/都可以.png")  #都可以按鈕圖片檔案位置
        image4 = image4.resize((90, 38), Image.ANTIALIAS)
        self.image4 = ImageTk.PhotoImage(image4)
        if len(gamelist) == 0:
            self.button4 = tk.Button(self, image= self.image4, relief="flat", bg = '#776262', border = 0, command = lambda: root.switch_frame2_5(self, Choose_Type, 'gongguan', '118', 'wenzhou', '都可以'))  #都可以按鈕外型+跳轉命令
        else:
            self.button4 = tk.Button(self, image= self.image4, relief="flat", bg = '#776262', border = 0, command = lambda: root.switch_frame2_5(self, Final, 'gongguan', '118', 'wenzhou', '都可以'))        #都可以按鈕外型+跳轉命令

        self.lb1.place(x = 0, y = 0, anchor = 'nw', width = 500, height = 60)  #標題擺放位置
        self.lb2.place(x = 77, y = 170, anchor = 'nw')
        self.lb3.place(x = 5, y = 250, anchor = 'nw')        #地圖擺放位置
        self.button1.place(x = 100, y = 330, anchor = 'nw')  #溫州街按鈕擺放位置
        self.button2.place(x = 135, y = 520, anchor = 'nw')  #公館按鈕擺放位置
        self.button3.place(x = 237, y = 283, anchor = 'nw')  #118巷按鈕擺放位置
        self.button4.place(x = 285, y = 485, anchor = 'nw')  #都可以按鈕擺放位置

        #固定區塊home跟返回鍵
        back = Image.open("./前端圖片/返回鍵.png")  #返回鍵按鈕圖片檔案位置
        back = back.resize((25, 25), Image.ANTIALIAS)
        self.back = ImageTk.PhotoImage(back)
        if len(gamelist) == 0:
            self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFDEA7', command = lambda: root.switch_infop_back(self, FirstPage))  #返回鍵按鈕外型+跳轉命令
        else:
            self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFDEA7', command = lambda: root.switch_list1_back(self, game4))  #返回鍵按鈕外型+跳轉命令

        home = Image.open("./前端圖片/首頁鍵.png")  #首頁鍵按鈕圖片檔案位置
        home = home.resize((37, 30), Image.ANTIALIAS)
        self.home = ImageTk.PhotoImage(home)
        self.homebutton = tk.Button(self, image= self.home, relief="flat", bg = '#FFDEA7', command = lambda: root.switch_home(self, FirstPage))  #首頁鍵按鈕外型+跳轉命令

        self.backbutton.place(x = 10, y = 14, anchor = 'nw')
        self.homebutton.place(x = 450, y = 11, anchor = 'nw')

class Choose_Type(tk.Frame):  #選擇食物種類畫面

    def __init__(self, parent):  #畫面驅動
        tk.Frame.__init__(self, parent)  
        self.creatWidgets()
        self.pack(fill = "both", expand = True)  #把place函數放進畫面  

    def creatWidgets(self):      #畫面部件
        now = datetime.datetime.now()
        f1 = tkFont.Font(size = 18, family = 'jf open 粉圓 1.1')  #各式字體大小、字形

        if (int(now.hour) < 17 and int(now.hour) >= 5) and list1[0] == '118巷':
            image_location = random.choices(["./前端圖片/118_day_1.png", "./前端圖片/118_day_2.png"])
            image1 = Image.open(image_location[0])  #118-日-食物背景圖片檔案位置
        elif (int(now.hour) >= 17 or int(now.hour) < 5) and list1[0] == '118巷':
            image_location = random.choices(["./前端圖片/118_night_1.png", "./前端圖片/118_night_2.png"])
            image1 = Image.open(image_location[0])  #118-夜-食物背景圖片檔案位置
        elif (int(now.hour) < 17 and int(now.hour) >= 5) and list1[0] == '溫州街':
            image_location = random.choices(["./前端圖片/溫州街_day_1.png", "./前端圖片/溫州街_day_2.png"])
            image1 = Image.open(image_location[0])  #溫州街-日-食物背景圖片檔案位置
        elif (int(now.hour) >= 17 or int(now.hour) < 5) and list1[0] == '溫州街':
            image_location = random.choices(["./前端圖片/溫州街_night_1.png", "./前端圖片/溫州街_night_2.png"])
            image1 = Image.open(image_location[0])  #溫州街-夜-食物背景圖片檔案位置
        elif (int(now.hour) < 17 and int(now.hour) >= 5) and list1[0] == '都可以':
            image_location = random.choices(["./前端圖片/都可以_day_1.png", "./前端圖片/都可以_day_2.png"])
            image1 = Image.open(image_location[0])  #都可以-日-食物背景圖片檔案位置
        elif (int(now.hour) >= 17 or int(now.hour) < 5) and list1[0] == '都可以':
            image_location = random.choices(["./前端圖片/都可以_night_1.png", "./前端圖片/都可以_night_2.png"])
            image1 = Image.open(image_location[0])  #都可以-夜-食物背景圖片檔案位置
        elif (int(now.hour) < 17 and int(now.hour) >= 5) and list1[0] == '公館':
            image_location = random.choices(["./前端圖片/公館_day_1.png", "./前端圖片/公館_day_2.png"])
            image1 = Image.open(image_location[0])  #公館-日-食物背景圖片檔案位置
        elif (int(now.hour) >= 17 or int(now.hour) < 5) and list1[0] == '公館':
            image_location = random.choices(["./前端圖片/公館_night_1.png", "./前端圖片/公館_night_2.png"])
            image1 = Image.open(image_location[0])  #公館-夜-食物背景圖片檔案位置
        image1 = image1.resize((500, 650), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image1)
        self.lb2 = tk.Label(self, image= self.image1, bg = '#FFE9C4')
        
        self.lb2.place(x = 0, y = 0, anchor = 'nw')

        #各類食物按鈕
        image2 = Image.open("./前端圖片/食物類型_台式小吃.png")  #食物類型_台式小吃按鈕圖片檔案位置
        image2 = image2.resize((160, 58), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image2)
        self.button1 = tk.Button(self, image= self.image2, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button('台式小吃', 1, 85, 275, '台式/小吃'))  #食物類型_台式小吃按鈕外型+反白命令

        image3 = Image.open("./前端圖片/食物類型_日式料理.png")  #食物類型_日式料理按鈕圖片檔案位置
        image3 = image3.resize((160, 58), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(image3)
        self.button2 = tk.Button(self, image= self.image3, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button('日式料理', 2, 255, 275, '日式料理'))  #食物類型_日式料理按鈕外型+反白命令

        image4 = Image.open("./前端圖片/食物類型_美式.png")      #食物類型_美式按鈕圖片檔案位置
        image4 = image4.resize((160, 58), Image.ANTIALIAS)
        self.image4 = ImageTk.PhotoImage(image4)
        self.button3 = tk.Button(self, image= self.image4, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button('美式', 3, 85, 345, '西式/美式'))  #食物類型_美式按鈕外型+反白命令

        image5 = Image.open("./前端圖片/食物類型_韓式料理.png")  #食物類型_韓式料理按鈕圖片檔案位置
        image5 = image5.resize((160, 58), Image.ANTIALIAS)
        self.image5 = ImageTk.PhotoImage(image5)
        self.button4 = tk.Button(self, image= self.image5, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button('韓式料理', 4, 255, 345, '韓式料理'))  #食物類型_韓式料理按鈕外型+反白命令

        image6 = Image.open("./前端圖片/食物類型_飲料.png")      #食物類型_飲料按鈕圖片檔案位置
        image6 = image6.resize((160, 58), Image.ANTIALIAS)
        self.image6 = ImageTk.PhotoImage(image6)
        self.button5 = tk.Button(self, image= self.image6, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button('飲料', 5, 85, 415, '飲料/甜點'))  #食物類型_飲料按鈕外型+反白命令

        image7 = Image.open("./前端圖片/食物類型_東南亞.png")    #食物類型_東南亞按鈕圖片檔案位置
        image7 = image7.resize((160, 58), Image.ANTIALIAS)
        self.image7 = ImageTk.PhotoImage(image7)
        self.button6 = tk.Button(self, image= self.image7, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button('東南亞', 6, 255, 415, '東南亞'))  #食物類型_東南亞按鈕外型+反白命令

        image8 = Image.open("./前端圖片/食物類型_素食.png")      #食物類型_素食按鈕圖片檔案位置
        image8 = image8.resize((160, 58), Image.ANTIALIAS)
        self.image8 = ImageTk.PhotoImage(image8)
        self.button7 = tk.Button(self, image= self.image8, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button('素食', 7, 85, 488, '素食/健康'))  #食物類型_素食按鈕外型+反白命令

        image9 = Image.open("./前端圖片/食物類型_火鍋.png")      #食物類型_火鍋按鈕圖片檔案位置
        image9 = image9.resize((160, 58), Image.ANTIALIAS)
        self.image9 = ImageTk.PhotoImage(image9)
        self.button8 = tk.Button(self, image= self.image9, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button('火鍋', 8, 255, 488, '火鍋'))  #食物類型_火鍋按鈕外型+反白命令

        image10 = Image.open("./前端圖片/食物類型_隨便.png")     #食物類型_隨便按鈕圖片檔案位置
        image10 = image10.resize((160, 58), Image.ANTIALIAS)
        self.image10 = ImageTk.PhotoImage(image10)
        foodlist = ['台式/小吃', '日式料理', '西式/美式', '韓式料理', '飲料/甜點', '東南亞', '素食/健康', '火鍋']
        food = str(random.choices(foodlist)[0])
        self.button9 = tk.Button(self, image= self.image10, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button('隨便', 9, 85, 560, food))  #食物類型_隨便按鈕外型+反白命令

        image11 = Image.open("./前端圖片/食物類型_FIND.png")     #食物類型_FIND按鈕圖片檔案位置
        image11 = image11.resize((160, 58), Image.ANTIALIAS)
        self.image11 = ImageTk.PhotoImage(image11)
        self.button10 = tk.Button(self, image= self.image11, relief="flat", bg = '#434343', border = 0, command = lambda: root.switch_frame(self, Final))  #食物類型_FIND按鈕外型+跳轉命令

        self.lb1 = tk.Label(self, text = 'FindEat   —   找食瞭瞭', bg = '#FFE9C4', font = f1, fg = '#FFB140')     #開頭標題 FindEat   —   找食瞭瞭
        self.lb1.place(x = 0, y = 0, anchor = 'nw', width = 500, height = 60)

        self.button1.place(x = 85, y = 275, anchor = 'nw')    #台式小吃按鈕擺放位置
        self.button2.place(x = 255, y = 275, anchor = 'nw')   #日式料理按鈕擺放位置
        self.button3.place(x = 85, y = 345, anchor = 'nw')    #美式按鈕擺放位置
        self.button4.place(x = 255, y = 345, anchor = 'nw')   #韓式料理按鈕擺放位置
        self.button5.place(x = 85, y = 415, anchor = 'nw')    #飲料按鈕擺放位置
        self.button6.place(x = 255, y = 415, anchor = 'nw')   #東南亞按鈕擺放位置
        self.button7.place(x = 85, y = 488, anchor = 'nw')    #素食按鈕擺放位置
        self.button8.place(x = 255, y = 488, anchor = 'nw')   #火鍋按鈕擺放位置
        self.button9.place(x = 85, y = 560, anchor = 'nw')    #隨便按鈕擺放位置
        self.button10.place(x = 255, y = 560, anchor = 'nw')  #_FIND按鈕擺放位置


        #固定區塊home跟返回鍵
        back = Image.open("./前端圖片/返回鍵.png")  #返回鍵按鈕圖片檔案位置
        back = back.resize((25, 25), Image.ANTIALIAS)
        self.back = ImageTk.PhotoImage(back)
        self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_list1_back(self, Choose_Place))  #返回鍵按鈕外型+跳轉命令

        home = Image.open("./前端圖片/首頁鍵.png")  #首頁鍵按鈕圖片檔案位置
        home = home.resize((37, 30), Image.ANTIALIAS)
        self.home = ImageTk.PhotoImage(home)
        self.homebutton = tk.Button(self, image= self.home, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_home(self, FirstPage))  #首頁鍵按鈕外型+跳轉命令

        self.backbutton.place(x = 10, y = 14, anchor = 'nw')
        self.homebutton.place(x = 450, y = 11, anchor = 'nw')

    def change_button(self, var, var2,  xplace, yplace, var3):  #反白命令
        global list1
        global info
        list1[1].append(var3)  #將按鈕選項增進list中
        info['Category'].append(var3)
        print(list1)
        print(info)
        if list1[0] == '118巷':  #根據選擇不同的地點顯示不同色調
            bt_image_location = './前端圖片/食物類型_'+ var + '_改色.png'
        elif list1[0] == '公館':
            bt_image_location = './前端圖片/食物類型_'+ var + '_改色2.png'
        elif list1[0] == '溫州街':
            bt_image_location = './前端圖片/食物類型_'+ var + '_改色3.png'
        elif list1[0] == '都可以':
            bt_image_location = './前端圖片/食物類型_'+ var + '_改色4.png'
        if var2 == 1:    
            image12 = Image.open(bt_image_location)
            image12 = image12.resize((160, 58), Image.ANTIALIAS)
            self.image12 = ImageTk.PhotoImage(image12)
            self.button11 = tk.Button(self, image= self.image12, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button2(var3, self.button11))  #台式小吃反白按鈕外型+命令
            self.button11.place(x = xplace, y = yplace, anchor = 'nw')
        elif var2 == 2:    
            image13 = Image.open(bt_image_location)
            image13 = image13.resize((160, 58), Image.ANTIALIAS)
            self.image13 = ImageTk.PhotoImage(image13)
            self.button12 = tk.Button(self, image= self.image13, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button2(var3, self.button12))  #日式料理反白按鈕外型+命令
            self.button12.place(x = xplace, y = yplace, anchor = 'nw')
        elif var2 == 3:    
            image14 = Image.open(bt_image_location)
            image14 = image14.resize((160, 58), Image.ANTIALIAS)
            self.image14 = ImageTk.PhotoImage(image14)
            self.button13 = tk.Button(self, image= self.image14, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button2(var3, self.button13))  #美式反白按鈕外型+命令
            self.button13.place(x = xplace, y = yplace, anchor = 'nw')
        elif var2 == 4:    
            image15 = Image.open(bt_image_location)
            image15 = image15.resize((160, 58), Image.ANTIALIAS)
            self.image15 = ImageTk.PhotoImage(image15)
            self.button14 = tk.Button(self, image= self.image15, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button2(var3, self.button14))  #韓式料理反白按鈕外型+命令
            self.button14.place(x = xplace, y = yplace, anchor = 'nw')
        elif var2 == 5:    
            image16 = Image.open(bt_image_location)
            image16 = image16.resize((160, 58), Image.ANTIALIAS)
            self.image16 = ImageTk.PhotoImage(image16)
            self.button15 = tk.Button(self, image= self.image16, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button2(var3, self.button15))  #飲料反白按鈕外型+命令
            self.button15.place(x = xplace, y = yplace, anchor = 'nw')
        elif var2 == 6:    
            image17 = Image.open(bt_image_location)
            image17 = image17.resize((160, 58), Image.ANTIALIAS)
            self.image17 = ImageTk.PhotoImage(image17)
            self.button16 = tk.Button(self, image= self.image17, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button2(var3, self.button16))  #東南亞反白按鈕外型+命令
            self.button16.place(x = xplace, y = yplace, anchor = 'nw')
        elif var2 == 7:    
            image18 = Image.open(bt_image_location)
            image18 = image18.resize((160, 58), Image.ANTIALIAS)
            self.image18 = ImageTk.PhotoImage(image18)
            self.button17 = tk.Button(self, image= self.image18, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button2(var3, self.button17))  #素食反白按鈕外型+命令
            self.button17.place(x = xplace, y = yplace, anchor = 'nw')
        elif var2 == 8:    
            image19 = Image.open(bt_image_location)
            image19 = image19.resize((160, 58), Image.ANTIALIAS)
            self.image19 = ImageTk.PhotoImage(image19)
            self.button18 = tk.Button(self, image= self.image19, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button2(var3, self.button18))  #火鍋反白按鈕外型+命令
            self.button18.place(x = xplace, y = yplace, anchor = 'nw')
        elif var2 == 9:    
            image20 = Image.open(bt_image_location)
            image20 = image20.resize((160, 58), Image.ANTIALIAS)
            self.image20 = ImageTk.PhotoImage(image20)
            self.button19 = tk.Button(self, image= self.image20, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button2(var3, self.button19))  #隨便反白按鈕外型+命令
            self.button19.place(x = xplace, y = yplace, anchor = 'nw')

    def change_button2(self, var1, bt):  #取消反白命令
        global list1
        global info
        info['Category'].remove(var1)  #移除已選擇的食物種類
        list1[1].remove(var1)
        
        bt.destroy()
        print(list1)
        print(info)

class Choose_Food(tk.Frame):  #選擇食物畫面(小遊戲)

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(bg = '#FFEED2')
        self.creatWidgets()
        self.pack(fill = "both", expand = True)

    def creatWidgets(self):
        f1 = tkFont.Font(size = 18, family = 'jf open 粉圓 1.1')
        f2 = tkFont.Font(size = 32, family = 'jf open 粉圓 1.1')

        self.lb1 = tk.Label(self, text = 'FindEat   —   找食瞭瞭', bg = '#FFE9C4', font = f1, fg = '#FFB140')
        self.lb2 = tk.Label(self, text = "Let's play a game.", bg = '#FFEED2', font = f2, fg = '#554640')

        image1 = Image.open("./前端圖片/小遊戲_問號.png")  #小遊戲_問號按鈕圖片檔案位置
        image1 = image1.resize((150, 75), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image1)
        self.button1 = tk.Button(self, image= self.image1, relief="flat", bg = '#FFEED2', border = 0, command = lambda: root.switch_frame(self, game2))  #按鈕外型+跳轉命令

        image2 = Image.open("./前端圖片/手指.png")         #手指圖片檔案位置
        image2 = image2.resize((64, 45), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image2)
        self.lb3 = tk.Label(self, image= self.image2, bg = '#FFEED2', border = 0)

        image3 = Image.open("./前端圖片/吐司人1.png")      #吐司人1圖片檔案位置
        image3 = image3.resize((370, 370), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(image3)
        self.lb4 = tk.Label(self, image= self.image3, bg = '#FFEED2', border = 0)
        
        self.lb1.place(x = 0, y = 0, anchor = 'nw', width = 500, height = 60)
        self.lb2.place(x = 70, y = 130, anchor = 'nw')
        self.button1.place(x = 175, y = 200, anchor = 'nw')
        self.lb3.place(x = 105, y = 213, anchor = 'nw')
        self.lb4.place(x = 60, y = 300, anchor = 'nw')

        #固定區塊home跟返回鍵
        back = Image.open("./前端圖片/返回鍵.png")  #返回鍵按鈕圖片檔案位置
        back = back.resize((25, 25), Image.ANTIALIAS)
        self.back = ImageTk.PhotoImage(back)
        self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_home(self, FirstPage))  #返回鍵按鈕外型+跳轉命令

        home = Image.open("./前端圖片/首頁鍵.png")  #首頁鍵按鈕圖片檔案位置
        home = home.resize((37, 30), Image.ANTIALIAS)
        self.home = ImageTk.PhotoImage(home)
        self.homebutton = tk.Button(self, image= self.home, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_home(self, FirstPage))  #首頁鍵按鈕外型+跳轉命令

        self.backbutton.place(x = 10, y = 14, anchor = 'nw')
        self.homebutton.place(x = 450, y = 11, anchor = 'nw')

class game2(tk.Frame):  #小遊戲畫面2

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(bg = '#FFEED2')
        self.creatWidgets()
        self.pack(fill = "both", expand = True)

    def creatWidgets(self):

        f1 = tkFont.Font(size = 18, family = 'jf open 粉圓 1.1')
        f2 = tkFont.Font(size = 32, family = 'jf open 粉圓 1.1')

        self.lb1 = tk.Label(self, text = 'FindEat   —   找食瞭瞭', bg = '#FFE9C4', font = f1, fg = '#FFB140')
        self.lb2 = tk.Label(self, text = "你現在的心情如何?", bg = '#FFEED2', font = f2, fg = '#554640')

        image1 = Image.open("./前端圖片/空虛寂寞.png")  #空虛寂寞按鈕圖片檔案位置
        image1 = image1.resize((135, 50), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image1)
        self.button1 = tk.Button(self, image= self.image1, relief="flat", bg = '#FFEED2', border = 0, command = lambda: root.switch_game(self, game3, '空虛寂寞'))  #按鈕外型+跳轉命令

        image2 = Image.open("./前端圖片/憤怒焦慮.png")  #憤怒焦慮按鈕圖片檔案位置
        image2 = image2.resize((135, 50), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image2)
        self.button2 = tk.Button(self, image= self.image2, relief="flat", bg = '#FFEED2', border = 0, command = lambda: root.switch_game(self, game3, '憤怒焦慮'))  #按鈕外型+跳轉命令

        image3 = Image.open("./前端圖片/平靜輕鬆.png")  #平靜輕鬆按鈕圖片檔案位置
        image3 = image3.resize((135, 50), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(image3)
        self.button3 = tk.Button(self, image= self.image3, relief="flat", bg = '#FFEED2', border = 0, command = lambda: root.switch_game(self, game3, '平靜輕鬆'))  #按鈕外型+跳轉命令

        image4 = Image.open("./前端圖片/吐司人2.png")   #吐司人2圖片檔案位置
        image4 = image4.resize((370, 370), Image.ANTIALIAS)
        self.image4 = ImageTk.PhotoImage(image4)
        self.lb3 = tk.Label(self, image= self.image4, bg = '#FFEED2', border = 0)

        self.lb1.place(x = 0, y = 0, anchor = 'nw', width = 500, height = 60)  #標題擺放位置
        self.lb2.place(x = 65, y = 130, anchor = 'nw')
        self.lb3.place(x = 65, y = 300, anchor = 'nw')       #吐司人2擺放位置
        self.button1.place(x = 30, y = 200, anchor = 'nw')   #空虛寂寞按鈕擺放位置
        self.button2.place(x = 175, y = 200, anchor = 'nw')  #憤怒焦慮按鈕擺放位置
        self.button3.place(x = 320, y = 200, anchor = 'nw')  #平靜輕鬆按鈕擺放位置

        #固定區塊home跟返回鍵
        back = Image.open("./前端圖片/返回鍵.png")  #返回鍵按鈕圖片檔案位置
        back = back.resize((25, 25), Image.ANTIALIAS)
        self.back = ImageTk.PhotoImage(back)
        self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_frame(self, Choose_Food))  #返回鍵按鈕外型+跳轉命令

        home = Image.open("./前端圖片/首頁鍵.png")  #首頁鍵按鈕圖片檔案位置
        home = home.resize((37, 30), Image.ANTIALIAS)
        self.home = ImageTk.PhotoImage(home)
        self.homebutton = tk.Button(self, image= self.home, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_home(self, FirstPage))  #首頁鍵按鈕外型+跳轉命令

        self.backbutton.place(x = 10, y = 14, anchor = 'nw')
        self.homebutton.place(x = 450, y = 11, anchor = 'nw')

class game3(tk.Frame):  #小遊戲畫面3

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(bg = '#FFEED2')
        self.creatWidgets()
        self.pack(fill = "both", expand = True)

    def creatWidgets(self):

        f1 = tkFont.Font(size = 18, family = 'jf open 粉圓 1.1')
        f2 = tkFont.Font(size = 32, family = 'jf open 粉圓 1.1')

        self.lb1 = tk.Label(self, text = 'FindEat   —   找食瞭瞭', bg = '#FFE9C4', font = f1, fg = '#FFB140')
        self.lb2 = tk.Label(self, text = "你是一個怎麼樣的人?", bg = '#FFEED2', font = f2, fg = '#554640')

        image1 = Image.open("./前端圖片/溫和穩重.png")  #溫和穩重按鈕圖片檔案位置
        image1 = image1.resize((135, 50), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image1)
        self.button1 = tk.Button(self, image= self.image1, relief="flat", bg = '#FFEED2', border = 0, command = lambda: root.switch_game(self, game4, '溫和穩重'))  #按鈕外型+跳轉命令

        image2 = Image.open("./前端圖片/熱情急躁.png")  #熱情急躁按鈕圖片檔案位置
        image2 = image2.resize((135, 50), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image2)
        self.button2 = tk.Button(self, image= self.image2, relief="flat", bg = '#FFEED2', border = 0, command = lambda: root.switch_game(self, game4, '熱情急躁'))  #按鈕外型+跳轉命令

        image3 = Image.open("./前端圖片/吐司人3.png")   #吐司人3圖片檔案位置
        image3 = image3.resize((370, 370), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(image3)
        self.lb3 = tk.Label(self, image= self.image3, bg = '#FFEED2', border = 0)

        self.lb1.place(x = 0, y = 0, anchor = 'nw', width = 500, height = 60)  #標題擺放位置
        self.lb2.place(x = 40, y = 130, anchor = 'nw')
        self.lb3.place(x = 65, y = 300, anchor = 'nw')       #吐司人3擺放位置
        self.button1.place(x = 100, y = 200, anchor = 'nw')  #溫和穩重按鈕擺放位置
        self.button2.place(x = 255, y = 200, anchor = 'nw')  #熱情急躁按鈕擺放位置

        #固定區塊home跟返回鍵
        back = Image.open("./前端圖片/返回鍵.png")  #返回鍵按鈕圖片檔案位置
        back = back.resize((25, 25), Image.ANTIALIAS)
        self.back = ImageTk.PhotoImage(back)
        self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_game_back(self, game2))  #返回鍵按鈕外型+跳轉命令

        home = Image.open("./前端圖片/首頁鍵.png")  #首頁鍵按鈕圖片檔案位置
        home = home.resize((37, 30), Image.ANTIALIAS)
        self.home = ImageTk.PhotoImage(home)
        self.homebutton = tk.Button(self, image= self.home, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_home(self, FirstPage))  #首頁鍵按鈕外型+跳轉命令

        self.backbutton.place(x = 10, y = 14, anchor = 'nw')
        self.homebutton.place(x = 450, y = 11, anchor = 'nw')

class game4(tk.Frame):  #小遊戲畫面4

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(bg = '#FFEED2')
        self.creatWidgets()
        self.pack(fill = "both", expand = True)

    def creatWidgets(self):
        now = datetime.datetime.now()

        f1 = tkFont.Font(size = 18, family = 'jf open 粉圓 1.1')
        f2 = tkFont.Font(size = 32, family = 'jf open 粉圓 1.1')
        f3 = tkFont.Font(size = 16, family = 'jf open 粉圓 1.1')

        self.lb1 = tk.Label(self, text = 'FindEat   —   找食瞭瞭', bg = '#FFE9C4', font = f1, fg = '#FFB140')
        self.lb2 = tk.Label(self, text = "適合你吃的食物是:", bg = '#FFEED2', font = f2, fg = '#554640')

        if gamelist[0] == '空虛寂寞' and gamelist[1] == '溫和穩重':  #依據心情選擇的不同推薦隨機不同的食物種類
            foodlist = ['牛排', '火鍋', '冰品']
        elif gamelist[0] == '空虛寂寞' and gamelist[1] == '熱情急躁':
            foodlist = ['炒飯', '滷味', '速食', '飲料']
        elif gamelist[0] == '憤怒焦慮':
            foodlist = ['義大利麵', '拉麵', '咖哩', '鹹酥雞', '韓式料理', '泰式料理']
        elif gamelist[0] == '平靜輕鬆':
            if int(now.hour) <= 13 and int(now.hour) >= 5:
                foodlist = ['早午餐', '日式料理', '水餃/鍋貼', '便當', '粥', '低GI', '素食']
            else:
                foodlist = ['日式料理', '水餃/鍋貼', '便當', '粥', '低GI', '素食']
        food = str(random.choices(foodlist)[0])
        self.lb3 = tk.Label(self, text = food + '!', bg = '#FFEED2', font = f2, fg = '#554640')

        image1 = Image.open("./前端圖片/方框.png")  #跳轉按鈕的外圍方框
        image1 = image1.resize((400, 50), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image1)
        self.lb4 = tk.Label(self, image= self.image1, bg = '#FFEED2', border = 0)

        if food == '水餃/鍋貼':  #修改字樣方便對資料
            food = '水餃鍋貼'
        image_location = "./前端圖片/" + food + ".png"
        image2 = Image.open(image_location)
        image2 = image2.resize((250, 200), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image2)
        self.lb5 = tk.Label(self, image= self.image2, bg = '#FFEED2', border = 0)
        self.lb5.place(x = 130, y = 200, anchor = 'nw')

        self.button1 = tk.Button(self, text = "找附近的" + food + '餐廳', bg = '#514C44', font = f3, fg = 'white', relief="flat", command = lambda: root.switch_frame3(self, Choose_Place, food))  #跳轉按鈕擺放位置

        self.lb1.place(x = 0, y = 0, anchor = 'nw', width = 500, height = 60)
        self.lb2.place(x = 70, y = 130, anchor = 'nw')

        if len(food) == 1:  #根據字串的長度修改擺放的位置
            self.lb3.place(x = 220, y = 450, anchor = 'nw')
        elif len(food) == 2:
            self.lb3.place(x = 200, y = 450, anchor = 'nw')
        elif len(food) == 3:
            self.lb3.place(x = 180, y = 450, anchor = 'nw')
        elif len(food) == 4:
            self.lb3.place(x = 160, y = 450, anchor = 'nw')
        elif len(food) == 5:
            self.lb3.place(x = 140, y = 450, anchor = 'nw')

        self.lb4.place(x = 50, y = 530, anchor = 'nw')

        if len(food) == 1:  #根據字串的長度修改擺放的位置
            self.button1.place(x = 160, y = 531, anchor = 'nw')
        elif len(food) == 2:
            self.button1.place(x = 155, y = 531, anchor = 'nw')
        elif len(food) == 3:
            self.button1.place(x = 150, y = 531, anchor = 'nw')
        elif len(food) == 4:
            self.button1.place(x = 140, y = 531, anchor = 'nw')
        else:
            self.button1.place(x = 125, y = 531, anchor = 'nw')

        #固定區塊home跟返回鍵
        back = Image.open("./前端圖片/返回鍵.png")  #返回鍵按鈕圖片檔案位置
        back = back.resize((25, 25), Image.ANTIALIAS)
        self.back = ImageTk.PhotoImage(back)
        self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_game_back(self, game3))  #返回鍵按鈕外型+跳轉命令

        home = Image.open("./前端圖片/首頁鍵.png")  #首頁鍵按鈕圖片檔案位置
        home = home.resize((37, 30), Image.ANTIALIAS)
        self.home = ImageTk.PhotoImage(home)
        self.homebutton = tk.Button(self, image= self.home, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_home(self, FirstPage))  #首頁鍵按鈕外型+跳轉命令

        self.backbutton.place(x = 10, y = 14, anchor = 'nw')
        self.homebutton.place(x = 450, y = 11, anchor = 'nw')

class Final(tk.Frame):  #最終呈現畫面

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(bg = '#FFEED2')
        self.creatWidgets()
        self.pack(fill = "both", expand = True)

    def creatWidgets(self):
        global list1
        #開始連接前後端資料
        # back to end
        # 讀取總資料集
        all_info = pd.read_csv('all_info.csv', encoding='utf-8', converters={'periods': eval})
        today=int(time.strftime("%w"))
        # 篩選資料並輸出前端要求的list
        def filter_restaurants(all_info, info, date: int) -> list:
            list_result = []
            print('mazafaka')
            print(info)
            # 篩選食物與地區
            print((all_info['region'].isin(info['region'])))
            if info['Category']:
                # 當模式為「選餐廳」
                idx = np.where((all_info['region'].isin(info['region'])) & (all_info['Category'].isin(info['Category'])))
            else:
                # 當模式為「選食物」
                idx = np.where((all_info['region'].isin(info['region'])) & (all_info['Subcategory'] == info['Subcategory']))
            selected_restaurant = all_info.loc[idx]
            print(idx)

            # 將篩選結果轉換成前端的輸出格式
            for _, row in selected_restaurant.iterrows():
                # 處理營業時間
                # 並不是每家店都0~6天都有
                time_week = row['periods']
                time_week_tbl = dict()
                if time_week is not None:
                    for i, data_day in enumerate(time_week):
                        time_week_tbl[data_day['close']['day']] = '{opent}-{closet}'.format(opent=data_day['open']['time'], closet=data_day['close']['time'])
                    # 再判斷是否有該天的資料
                    if date in time_week_tbl:
                        time_day = time_week_tbl[date]
                    else:
                        time_day = 'None'
                else:
                    time_day = 'None'

                # 將結果加入list
                region_in_chinese = {'118': '118', 'gongguan': '公館', 'wenzhou': '溫州街'}
                date_map = {0: 'Sun', 1: 'Mon', 2: 'Tues', 3: 'Wed', 4: 'Thur', 5: 'Fri', 6: 'Sat'}  # 將輸入的日期轉為字串格式
                food_path = './food/{Id}.png'.format(Id=row['Id'])
                word_cloud_path = './wordcloud/{Id}.png'.format(Id=row['Id'])  # 文字雲檔案路徑
                busyness_path = './busyness/{Id}_{Date}.png'.format(Id=row['Id'], Date=date_map[date])  # 繁忙時間柱狀圖檔案路徑
                row_data = [row['Name'], region_in_chinese[row['region']], row['pinyin'], row['Score'], row['Subcategory'], time_day, row['Google_link'], food_path, word_cloud_path, busyness_path]
                list_result.append(row_data)
             
            print(list_result)
            # 輸出結果
            return list_result
        final_list = filter_restaurants(all_info=all_info, info=info, date=today)
        #後端資料連接完成

        f1 = tkFont.Font(size = 18, family = 'jf open 粉圓 1.1')
        f2 = tkFont.Font(size = 32, family = 'jf open 粉圓 1.1')
        f3 = tkFont.Font(size = 18, family = 'jf open 粉圓 1.1')
        f4 = tkFont.Font(size = 24, family = 'jf open 粉圓 1.1')
        f5 = tkFont.Font(size = 12, family = 'jf open 粉圓 1.1')

        self.cv1 = tk.Canvas(self, bg = '#FFF9EE', width = 500, height = 600)       #創建畫布以便資料呈現
        self.cv1.place(x = 0, y = 57)
        scroll_y = tk.Scrollbar(self, orient="vertical", command = self.cv1.yview)  #滾輪滑動
        scroll_y.place(x = 500, y = 55, anchor = 'ne', height = 600)

        self.lb3 = tk.Label(self.cv1, text = 'FindEat   —   找食瞭瞭', bg = '#FFF9EE', font = f1, fg = '#FFF9EE')  #最上方標題
        self.lb3.pack()
        self.cv1.create_window(0, 0, window = self.lb3, anchor = 'nw')

        #以迴圈創造相應變數
        for i in final_list:  #餐廳名稱
            locals()['self.lb_firm_' + str(final_list.index(i))] = tk.Label(self.cv1, text = i[0], bg = '#FFF9EE', font = f2, fg = '#FAAF4E')
            locals()['self.lb_firm_' + str(final_list.index(i))].pack()
            self.cv1.create_window(17, 30 + 550 * final_list.index(i), window = locals()['self.lb_firm_' + str(final_list.index(i))], anchor = 'nw')

        for i in final_list:  #餐廳地點大分類
            locals()['self.lb_Rome_' + str(final_list.index(i))] = tk.Label(self.cv1, text = i[2], bg = '#FFF9EE', font = f3, fg = '#D6A985')
            locals()['self.lb_Rome_' + str(final_list.index(i))].pack()
            self.cv1.create_window(19, 85 + 550 * final_list.index(i), window = locals()['self.lb_Rome_' + str(final_list.index(i))], anchor = 'nw')

        for i in final_list:  #餐廳評分
            i[3] = round(i[3], 2)
            locals()['self.lb_score_' + str(final_list.index(i))] = tk.Label(self.cv1, text = '綜合評分 ' + str(i[3]) + '/10', bg = '#FFF9EE', font = f4, fg = '#FF595E')
            locals()['self.lb_score_' + str(final_list.index(i))].pack()
            if len(str(i[3])) == 1:
                self.cv1.create_window(230, 122 + 550 * final_list.index(i), window = locals()['self.lb_score_' + str(final_list.index(i))], anchor = 'nw')
            else:
                self.cv1.create_window(220, 122 + 550 * final_list.index(i), window = locals()['self.lb_score_' + str(final_list.index(i))], anchor = 'nw')

        for i in final_list:  #餐廳食物類行
            locals()['self.lb_type_' + str(final_list.index(i))] = tk.Label(self.cv1, text = i[4] + '類,' + i[1], bg = '#FFF9EE', font = f5, fg = '#D6A985')
            locals()['self.lb_type_' + str(final_list.index(i))].pack()
            self.cv1.create_window(19, 120 + 550 * final_list.index(i), window = locals()['self.lb_type_' + str(final_list.index(i))], anchor = 'nw')

        for i in final_list:  #餐廳營業時間
            locals()['self.lb_open_' + str(final_list.index(i))] = tk.Label(self.cv1, text = '營業時間:' + i[5], bg = '#FFF9EE', font = f5, fg = '#D6A985')
            locals()['self.lb_open_' + str(final_list.index(i))].pack()
            self.cv1.create_window(19, 140 + 550 * final_list.index(i), window = locals()['self.lb_open_' + str(final_list.index(i))], anchor = 'nw')

        for i in final_list:  #餐廳google_map_連結
            globals()['self.lb_place_' + str(final_list.index(i))] = tk.Label(self.cv1, text = '詳細資訊', bg = '#FFF9EE', font = f3, fg = '#71A9D9', cursor="hand2")
            globals()['self.lb_place_' + str(final_list.index(i))].pack()
            globals()['self.lb_place_' + str(final_list.index(i))].bind("<Button-1>", lambda e, url=i[6]: webbrowser.open_new(url))
            self.cv1.create_window(370, 85 + 550 * final_list.index(i), window = globals()['self.lb_place_' + str(final_list.index(i))], anchor = 'nw')

        for i in final_list:  #餐廳範例圖片
            image_location =  i[7]
            try:
                globals()['image1_' + str(final_list.index(i))] = Image.open(image_location)
            except:
                globals()['image1_' + str(final_list.index(i))] = Image.open('./找不到照片.png')
            globals()['image1_' + str(final_list.index(i))] = globals()['image1_' + str(final_list.index(i))].resize((200, 210), Image.ANTIALIAS)
            globals()['self.image1_' + str(final_list.index(i))] = ImageTk.PhotoImage(globals()['image1_' + str(final_list.index(i))])
            globals()['self.lb_image1_' + str(final_list.index(i))] = tk.Label(self.cv1, image= globals()['self.image1_' + str(final_list.index(i))])
            globals()['self.lb_image1_' + str(final_list.index(i))].pack()
            self.cv1.create_window(19, 180 + 550 * final_list.index(i), window = globals()['self.lb_image1_' + str(final_list.index(i))], anchor = 'nw')

        for i in final_list:  #餐廳文字雲圖片
            image_location = i[8]
            globals()['image2_' + str(final_list.index(i))] = Image.open(image_location)
            globals()['image2_' + str(final_list.index(i))] = globals()['image2_' + str(final_list.index(i))].resize((200, 210), Image.ANTIALIAS)
            globals()['self.image2_' + str(final_list.index(i))] = ImageTk.PhotoImage(globals()['image2_' + str(final_list.index(i))])
            globals()['self.lb_image2_' + str(final_list.index(i))] = tk.Label(self.cv1, image= globals()['self.image2_' + str(final_list.index(i))])
            globals()['self.lb_image2_' + str(final_list.index(i))].pack()
            self.cv1.create_window(270, 180 + 550 * final_list.index(i), window = globals()['self.lb_image2_' + str(final_list.index(i))], anchor = 'nw')

        for i in final_list:  #餐廳尖峰時段圖片
            image_location = i[9]
            try:
                globals()['time_image_' + str(final_list.index(i))] = Image.open(image_location)
            except:
                globals()['time_image_' + str(final_list.index(i))] = Image.open('./找不到忙碌狀況.png')
            globals()['time_image_' + str(final_list.index(i))] = globals()['time_image_' + str(final_list.index(i))].resize((450, 90), Image.ANTIALIAS)
            globals()['self.time_image_' + str(final_list.index(i))] = ImageTk.PhotoImage(globals()['time_image_' + str(final_list.index(i))])
            globals()['self.lb_time_image_' + str(final_list.index(i))] = tk.Label(self.cv1, image= globals()['self.time_image_' + str(final_list.index(i))])
            globals()['self.lb_time_image_' + str(final_list.index(i))].pack()
            self.cv1.create_window(19, 430 + 550 * final_list.index(i), window = globals()['self.lb_time_image_' + str(final_list.index(i))], anchor = 'nw')

        for i in final_list:  #不同餐廳間的分隔線段
            image_location = './呈現頁面圖片/分隔線段.png'
            globals()['divide_' + str(final_list.index(i))] = Image.open(image_location)
            globals()['divide_' + str(final_list.index(i))] = globals()['divide_' + str(final_list.index(i))].resize((450, 1), Image.ANTIALIAS)
            globals()['self.divide_' + str(final_list.index(i))] = ImageTk.PhotoImage(globals()['divide_' + str(final_list.index(i))])
            globals()['self.lb_divide_' + str(final_list.index(i))] = tk.Label(self.cv1, image= globals()['self.divide_' + str(final_list.index(i))])
            globals()['self.lb_divide_' + str(final_list.index(i))].pack()
            self.cv1.create_window(19, 540 + 550 * final_list.index(i), window = globals()['self.lb_divide_' + str(final_list.index(i))], anchor = 'nw')

        self.cv1.configure(scrollregion=self.cv1.bbox('all'), yscrollcommand=scroll_y.set)

        self.lb1 = tk.Label(self, text = 'FindEat   —   找食瞭瞭', bg = '#FFE9C4', font = f1, fg = '#FFB140')
        self.lb1.place(x = 0, y = 0, anchor = 'nw', width = 500, height = 60)
        print(final_list)

        #固定區塊home跟返回鍵
        back = Image.open("./前端圖片/返回鍵.png")  #返回鍵按鈕圖片檔案位置
        back = back.resize((25, 25), Image.ANTIALIAS)
        self.back = ImageTk.PhotoImage(back)
        if len(gamelist) != 0:
            self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_infop_back(self, Choose_Place))  #返回鍵按鈕外型+跳轉命令
        else:
            self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_infoc_back(self, Choose_Type))  #返回鍵按鈕外型+跳轉命令

        home = Image.open("./前端圖片/首頁鍵.png")  #首頁鍵按鈕圖片檔案位置
        home = home.resize((37, 30), Image.ANTIALIAS)
        self.home = ImageTk.PhotoImage(home)
        self.homebutton = tk.Button(self, image= self.home, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_home(self, FirstPage))  #首頁鍵按鈕外型+跳轉命令

        self.backbutton.place(x = 10, y = 14, anchor = 'nw')
        self.homebutton.place(x = 450, y = 11, anchor = 'nw')


if __name__ == "__main__":
    app = root()
    app.mainloop()
