import tkinter as tk
import tkinter.font as tkFont
from PIL import Image
from PIL import ImageTk
import random
import datetime

list1 = ['地點', []]
gamelist = []

class root(tk.Tk):  #基底視窗
    def __init__(self):  #視窗驅動
        tk.Tk.__init__(self)
        self.geometry('500x650')  #視窗大小
        self.title('FindEat 找食瞭瞭')  #視窗名稱
        self._frame = None
        self.switch_frame(FirstPage)

    def switch_frame(self, frame_class):  #轉換畫面過程
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  #破壞原先視畫面替換成新畫面
        self._frame = new_frame
        self._frame.pack()

    def switch_frame2(self, frame_class, var):  #home鍵轉換畫面過程
        global list1
        list1[0] = var
        print(list1)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  #破壞原先視畫面替換成新畫面
        self._frame = new_frame
        self._frame.pack()

    def switch_frame3(self, frame_class, var):  #home鍵轉換畫面過程
        global list1
        list1[1].append(var)
        print(list1)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  #破壞原先視畫面替換成新畫面
        self._frame = new_frame
        self._frame.pack()

    def switch_game(self, frame_class, var):  #返回鍵轉換畫面過程
        global gamelist
        gamelist.append(var)
        print(gamelist)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  #破壞原先視畫面替換成新畫面
        self._frame = new_frame
        self._frame.pack()

    def switch_game_back(self, frame_class):  #返回鍵轉換畫面過程
        global gamelist
        gamelist.pop()
        print(gamelist)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  #破壞原先視畫面替換成新畫面
        self._frame = new_frame
        self._frame.pack()

    def switch_list1_back(self, frame_class):  #返回鍵轉換畫面過程
        global list1
        list1[1] = []
        print(list1)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  #破壞原先視畫面替換成新畫面
        self._frame = new_frame
        self._frame.pack()

    def switch_home(self, frame_class):  #home鍵轉換畫面過程
        global gamelist
        global list1
        list1 = ['地點', []]
        gamelist = []
        print(list1)
        print(gamelist)
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

        image1 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\食物.png")  #食物按鈕圖片檔案位置
        image1 = image1.resize((180, 100), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image1)
        self.button1 = tk.Button(self, image= self.image1, relief="flat", bg = '#FFEED2', command = lambda: root.switch_frame(self, Choose_Food))   #食物按鈕外型+跳轉命令
        
        image2 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\餐廳.png")  #餐廳按鈕圖片檔案位置
        image2 = image2.resize((180, 95), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image2)
        self.button2 = tk.Button(self, image= self.image2, relief="flat", bg = '#FFEED2', command = lambda: root.switch_frame(self, Choose_Place))  #餐廳按鈕外型+跳轉命令

        self.lb1.place(x = 155, y = 45, anchor = 'nw')       #開頭標題 FindEat   擺放位置
        self.lb2.place(x = 166, y = 105, anchor = 'nw')      #開頭標題 找食瞭瞭  擺放位置
        self.lb3.place(x = 137, y = 285, anchor = 'nw')      #開頭標題 我想找... 擺放位置
        self.button1.place(x = 157, y = 350, anchor = 'nw')  #食物按鈕擺放位置
        self.button2.place(x = 157, y = 440, anchor = 'nw')  #餐廳按鈕擺放位置

        #以下不重要背景圖片
        bg1 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\漢堡.png")
        bg1 = bg1.resize((100, 85), Image.ANTIALIAS)
        self.bg1 = ImageTk.PhotoImage(bg1)
        self.bglb1 = tk.Label(self, image= self.bg1, bg = '#FFEED2')
        
        bg2 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\壽司.png")
        bg2 = bg2.resize((110, 100), Image.ANTIALIAS)
        self.bg2 = ImageTk.PhotoImage(bg2)
        self.bglb2 = tk.Label(self, image= self.bg2, bg = '#FFEED2')

        bg3 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\咖啡杯.png")
        bg3 = bg3.resize((110, 95), Image.ANTIALIAS)
        self.bg3 = ImageTk.PhotoImage(bg3)
        self.bglb3 = tk.Label(self, image= self.bg3, bg = '#FFEED2')

        bg4 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\熱狗.png")
        bg4 = bg4.resize((110, 95), Image.ANTIALIAS)
        self.bg4 = ImageTk.PhotoImage(bg4)
        self.bglb4 = tk.Label(self, image= self.bg4, bg = '#FFEED2')

        bg5 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\薯條.png")
        bg5 = bg5.resize((110, 95), Image.ANTIALIAS)
        self.bg5 = ImageTk.PhotoImage(bg5)
        self.bglb5 = tk.Label(self, image= self.bg5, bg = '#FFEED2')

        bg6 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\杯子蛋糕.png")
        bg6 = bg6.resize((110, 95), Image.ANTIALIAS)
        self.bg6 = ImageTk.PhotoImage(bg6)
        self.bglb6 = tk.Label(self, image= self.bg6, bg = '#FFEED2')

        bg7 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\烤肉醬.png")
        bg7 = bg7.resize((110, 95), Image.ANTIALIAS)
        self.bg7 = ImageTk.PhotoImage(bg7)
        self.bglb7 = tk.Label(self, image= self.bg7, bg = '#FFEED2')

        bg8 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\梨子.png")
        bg8 = bg8.resize((110, 95), Image.ANTIALIAS)
        self.bg8 = ImageTk.PhotoImage(bg8)
        self.bglb8 = tk.Label(self, image= self.bg8, bg = '#FFEED2')

        bg9 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\甜筒.png")
        bg9 = bg9.resize((110, 95), Image.ANTIALIAS)
        self.bg9 = ImageTk.PhotoImage(bg9)
        self.bglb9 = tk.Label(self, image= self.bg9, bg = '#FFEED2')

        bg10 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\雞腿.png")
        bg10 = bg10.resize((110, 95), Image.ANTIALIAS)
        self.bg10 = ImageTk.PhotoImage(bg10)
        self.bglb10 = tk.Label(self, image= self.bg10, bg = '#FFEED2')

        bg11 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\牛奶.png")
        bg11 = bg11.resize((110, 95), Image.ANTIALIAS)
        self.bg11 = ImageTk.PhotoImage(bg11)
        self.bglb11 = tk.Label(self, image= self.bg11, bg = '#FFEED2')

        bg12 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\冰淇淋.png")
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

        map1 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\地圖.png")  #地圖圖片檔案位置
        map1 = map1.resize((480, 320), Image.ANTIALIAS)
        self.map1 = ImageTk.PhotoImage(map1)
        self.lb3 = tk.Label(self, image= self.map1, relief="flat", bg = '#FFE9C4')

        image1 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\溫州街.png")  #溫州街按鈕圖片檔案位置
        image1 = image1.resize((44, 104), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image1)
        if len(gamelist) == 0:
            self.button1 = tk.Button(self, image= self.image1, relief="flat", bg = '#776262', border = 0, command = lambda: root.switch_frame2(self, Choose_Type, '溫州街'))  #溫州街按鈕外型+跳轉命令
        else:
            self.button1 = tk.Button(self, image= self.image1, relief="flat", bg = '#776262', border = 0, command = lambda: root.switch_frame2(self, Final, '溫州街'))  #溫州街按鈕外型+跳轉命令

        image2 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\公館.png")  #公館按鈕圖片檔案位置
        image2 = image2.resize((87, 36), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image2)
        if len(gamelist) == 0:
            self.button2 = tk.Button(self, image= self.image2, relief="flat", bg = '#776262', border = 0, command = lambda: root.switch_frame2(self, Choose_Type, '公館'))    #公館按鈕外型+跳轉命令
        else:
            self.button2 = tk.Button(self, image= self.image2, relief="flat", bg = '#776262', border = 0, command = lambda: root.switch_frame2(self, Final, '公館'))    #公館按鈕外型+跳轉命令

        image3 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\118巷.png")  #118巷按鈕圖片檔案位置
        image3 = image3.resize((90, 40), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(image3)
        if len(gamelist) == 0:
            self.button3 = tk.Button(self, image= self.image3, relief="flat", bg = '#776262', border = 0, command = lambda: root.switch_frame2(self, Choose_Type, '118巷'))   #118巷按鈕外型+跳轉命令
        else:
            self.button3 = tk.Button(self, image= self.image3, relief="flat", bg = '#776262', border = 0, command = lambda: root.switch_frame2(self, Final, '118巷'))   #118巷按鈕外型+跳轉命令

        image4 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\都可以.png")  #都可以按鈕圖片檔案位置
        image4 = image4.resize((90, 38), Image.ANTIALIAS)
        self.image4 = ImageTk.PhotoImage(image4)
        if len(gamelist) == 0:
            self.button4 = tk.Button(self, image= self.image4, relief="flat", bg = '#776262', border = 0, command = lambda: root.switch_frame2(self, Choose_Type, '都可以'))  #都可以按鈕外型+跳轉命令
        else:
            self.button4 = tk.Button(self, image= self.image4, relief="flat", bg = '#776262', border = 0, command = lambda: root.switch_frame2(self, Final, '都可以'))  #都可以按鈕外型+跳轉命令

        self.lb1.place(x = 0, y = 0, anchor = 'nw', width = 500, height = 60)
        self.lb2.place(x = 77, y = 170, anchor = 'nw')
        self.lb3.place(x = 5, y = 250, anchor = 'nw')
        self.button1.place(x = 100, y = 330, anchor = 'nw')
        self.button2.place(x = 135, y = 520, anchor = 'nw')
        self.button3.place(x = 237, y = 283, anchor = 'nw')
        self.button4.place(x = 285, y = 485, anchor = 'nw')

        #固定區塊home跟返回鍵
        back = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\返回鍵.png")  #返回鍵按鈕圖片檔案位置
        back = back.resize((25, 25), Image.ANTIALIAS)
        self.back = ImageTk.PhotoImage(back)
        if len(gamelist) == 0:
            self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFDEA7', command = lambda: root.switch_frame(self, FirstPage))  #返回鍵按鈕外型+跳轉命令
        else:
            self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFDEA7', command = lambda: root.switch_list1_back(self, game4))  #返回鍵按鈕外型+跳轉命令

        home = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\首頁鍵.png")  #首頁鍵按鈕圖片檔案位置
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

        self.lb1 = tk.Label(self, text = 'FindEat   —   找食瞭瞭', bg = '#FFE9C4', font = f1, fg = '#FFB140')     #開頭標題 FindEat   —   找食瞭瞭

        if (int(now.hour) < 17 or int(now.hour) >= 5) and list1[0] == '118巷':
            image1 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\118-日-食物.png")  #118-日-食物背景圖片檔案位置
        elif (int(now.hour) >= 17 or int(now.hour) < 5) and list1[0] == '118巷':
            image1 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\118-夜-食物.png")  #118-夜-食物背景圖片檔案位置
        elif (int(now.hour) < 17 or int(now.hour) >= 5) and list1[0] == '溫州街':
            image1 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\溫州街-日-食物.png")     #溫州街-日-食物背景圖片檔案位置
        elif (int(now.hour) >= 17 or int(now.hour) < 5) and list1[0] == '溫州街':
            image1 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\溫州街-夜-食物.png")     #溫州街-夜-食物背景圖片檔案位置
        elif (int(now.hour) < 17 or int(now.hour) >= 5) and list1[0] == '都可以':
            image1 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\都可以-日-食物.png")  #都可以-日-食物背景圖片檔案位置
        elif (int(now.hour) >= 17 or int(now.hour) < 5) and list1[0] == '都可以':
            image1 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\都可以-夜-食物.png")  #都可以-夜-食物背景圖片檔案位置
        elif (int(now.hour) < 17 or int(now.hour) >= 5) and list1[0] == '公館':
            image1 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\公館-日-食物.png")    #公館-日-食物背景圖片檔案位置
        elif (int(now.hour) >= 17 or int(now.hour) < 5) and list1[0] == '公館':
            image1 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\公館-夜-食物.png")    #公館-夜-食物背景圖片檔案位置
        image1 = image1.resize((500, 590), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image1)
        self.lb2 = tk.Label(self, image= self.image1, bg = '#FFE9C4')
        
        self.lb1.place(x = 0, y = 0, anchor = 'nw', width = 500, height = 60)
        self.lb2.place(x = 0, y = 55, anchor = 'nw')

        #各類食物按鈕
        image2 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\食物類型_台式小吃.png")  #食物類型_台式小吃按鈕圖片檔案位置
        image2 = image2.resize((160, 58), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image2)
        self.button1 = tk.Button(self, image= self.image2, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button(button1))  #食物類型_台式小吃按鈕外型+跳轉命令

        image3 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\食物類型_日式料理.png")  #食物類型_日式料理按鈕圖片檔案位置
        image3 = image3.resize((160, 58), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(image3)
        self.button2 = tk.Button(self, image= self.image3, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button(button1))  #食物類型_日式料理按鈕外型+跳轉命令

        image4 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\食物類型_美式.png")  #食物類型_美式按鈕圖片檔案位置
        image4 = image4.resize((160, 58), Image.ANTIALIAS)
        self.image4 = ImageTk.PhotoImage(image4)
        self.button3 = tk.Button(self, image= self.image4, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button(button1))  #食物類型_美式按鈕外型+跳轉命令

        image5 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\食物類型_韓式料理.png")  #食物類型_韓式料理按鈕圖片檔案位置
        image5 = image5.resize((160, 58), Image.ANTIALIAS)
        self.image5 = ImageTk.PhotoImage(image5)
        self.button4 = tk.Button(self, image= self.image5, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button(button1))  #食物類型_韓式料理按鈕外型+跳轉命令

        image6 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\食物類型_飲料.png")  #食物類型_飲料按鈕圖片檔案位置
        image6 = image6.resize((160, 58), Image.ANTIALIAS)
        self.image6 = ImageTk.PhotoImage(image6)
        self.button5 = tk.Button(self, image= self.image6, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button(button1))  #食物類型_飲料按鈕外型+跳轉命令

        image7 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\食物類型_東南亞.png")  #食物類型_東南亞按鈕圖片檔案位置
        image7 = image7.resize((160, 58), Image.ANTIALIAS)
        self.image7 = ImageTk.PhotoImage(image7)
        self.button6 = tk.Button(self, image= self.image7, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button(button1))  #食物類型_東南亞按鈕外型+跳轉命令

        image8 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\食物類型_素食.png")  #食物類型_素食按鈕圖片檔案位置
        image8 = image8.resize((160, 58), Image.ANTIALIAS)
        self.image8 = ImageTk.PhotoImage(image8)
        self.button7 = tk.Button(self, image= self.image8, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button(button1))  #食物類型_素食按鈕外型+跳轉命令

        image9 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\食物類型_火鍋.png")  #食物類型_火鍋按鈕圖片檔案位置
        image9 = image9.resize((160, 58), Image.ANTIALIAS)
        self.image9 = ImageTk.PhotoImage(image9)
        self.button8 = tk.Button(self, image= self.image9, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button(button1))  #食物類型_火鍋按鈕外型+跳轉命令

        image10 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\食物類型_隨便.png")  #食物類型_隨便按鈕圖片檔案位置
        image10 = image10.resize((160, 58), Image.ANTIALIAS)
        self.image10 = ImageTk.PhotoImage(image10)
        self.button9 = tk.Button(self, image= self.image10, relief="flat", bg = '#434343', border = 0, command = lambda: self.change_button(button1))  #食物類型_隨便按鈕外型+跳轉命令

        image11 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\食物類型_FIND.png")  #食物類型_FIND按鈕圖片檔案位置
        image11 = image11.resize((160, 58), Image.ANTIALIAS)
        self.image11 = ImageTk.PhotoImage(image11)
        self.button10 = tk.Button(self, image= self.image11, relief="flat", bg = '#434343', border = 0, command = lambda: root.switch_frame(self, Final))  #食物類型_FIND按鈕外型+跳轉命令

        self.button1.place(x = 90, y = 270, anchor = 'nw')
        self.button2.place(x = 260, y = 270, anchor = 'nw')
        self.button3.place(x = 90, y = 340, anchor = 'nw')
        self.button4.place(x = 260, y = 340, anchor = 'nw')
        self.button5.place(x = 90, y = 410, anchor = 'nw')
        self.button6.place(x = 260, y = 410, anchor = 'nw')
        self.button7.place(x = 90, y = 483, anchor = 'nw')
        self.button8.place(x = 260, y = 483, anchor = 'nw')
        self.button9.place(x = 90, y = 555, anchor = 'nw')
        self.button10.place(x = 260, y = 555, anchor = 'nw')


    #固定區塊home跟返回鍵
        back = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\返回鍵.png")  #返回鍵按鈕圖片檔案位置
        back = back.resize((25, 25), Image.ANTIALIAS)
        self.back = ImageTk.PhotoImage(back)
        self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_list1_back(self, Choose_Place))  #返回鍵按鈕外型+跳轉命令

        home = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\首頁鍵.png")  #首頁鍵按鈕圖片檔案位置
        home = home.resize((37, 30), Image.ANTIALIAS)
        self.home = ImageTk.PhotoImage(home)
        self.homebutton = tk.Button(self, image= self.home, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_home(self, FirstPage))  #首頁鍵按鈕外型+跳轉命令

        self.backbutton.place(x = 10, y = 14, anchor = 'nw')
        self.homebutton.place(x = 450, y = 11, anchor = 'nw')

    def change_button(self, var):
        global list1
        a = var
        location = 'C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\' + list1[2] + '_食物類型_隨便_改色' + '.png'

class Choose_Food(tk.Frame):  #選擇食物畫面

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

        image1 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\小遊戲_問號.png")  #小遊戲_問號按鈕圖片檔案位置
        image1 = image1.resize((150, 75), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image1)
        self.button1 = tk.Button(self, image= self.image1, relief="flat", bg = '#FFEED2', border = 0, command = lambda: root.switch_frame(self, game2))  #按鈕外型+跳轉命令

        image2 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\手指.png")  #手指圖片檔案位置
        image2 = image2.resize((64, 45), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image2)
        self.lb3 = tk.Label(self, image= self.image2, bg = '#FFEED2', border = 0)

        image3 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\吐司人1.png")  #吐司人1圖片檔案位置
        image3 = image3.resize((370, 370), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(image3)
        self.lb4 = tk.Label(self, image= self.image3, bg = '#FFEED2', border = 0)
        
        self.lb1.place(x = 0, y = 0, anchor = 'nw', width = 500, height = 60)
        self.lb2.place(x = 70, y = 130, anchor = 'nw')
        self.button1.place(x = 175, y = 200, anchor = 'nw')
        self.lb3.place(x = 105, y = 213, anchor = 'nw')
        self.lb4.place(x = 60, y = 300, anchor = 'nw')

        #固定區塊home跟返回鍵
        back = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\返回鍵.png")  #返回鍵按鈕圖片檔案位置
        back = back.resize((25, 25), Image.ANTIALIAS)
        self.back = ImageTk.PhotoImage(back)
        self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_home(self, FirstPage))  #返回鍵按鈕外型+跳轉命令

        home = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\首頁鍵.png")  #首頁鍵按鈕圖片檔案位置
        home = home.resize((37, 30), Image.ANTIALIAS)
        self.home = ImageTk.PhotoImage(home)
        self.homebutton = tk.Button(self, image= self.home, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_home(self, FirstPage))  #首頁鍵按鈕外型+跳轉命令

        self.backbutton.place(x = 10, y = 14, anchor = 'nw')
        self.homebutton.place(x = 450, y = 11, anchor = 'nw')

class game2(tk.Frame):  #選擇食物畫面

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

        image1 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\開心.png")  #開心按鈕圖片檔案位置
        image1 = image1.resize((150, 75), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image1)
        self.button1 = tk.Button(self, image= self.image1, relief="flat", bg = '#FFEED2', border = 0, command = lambda: root.switch_game(self, game3, '開心'))  #按鈕外型+跳轉命令

        image2 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\難過.png")  #難過按鈕圖片檔案位置
        image2 = image2.resize((150, 75), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image2)
        self.button2 = tk.Button(self, image= self.image2, relief="flat", bg = '#FFEED2', border = 0, command = lambda: root.switch_game(self, game3, '難過'))  #按鈕外型+跳轉命令

        image3 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\生氣.png")  #生氣按鈕圖片檔案位置
        image3 = image3.resize((150, 75), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(image3)
        self.button3 = tk.Button(self, image= self.image3, relief="flat", bg = '#FFEED2', border = 0, command = lambda: root.switch_game(self, game3, '生氣'))  #按鈕外型+跳轉命令

        image4 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\吐司人2.png")  #吐司人2圖片檔案位置
        image4 = image4.resize((370, 370), Image.ANTIALIAS)
        self.image4 = ImageTk.PhotoImage(image4)
        self.lb3 = tk.Label(self, image= self.image4, bg = '#FFEED2', border = 0)

        self.lb1.place(x = 0, y = 0, anchor = 'nw', width = 500, height = 60)
        self.lb2.place(x = 65, y = 130, anchor = 'nw')
        self.lb3.place(x = 65, y = 300, anchor = 'nw')
        self.button1.place(x = 30, y = 200, anchor = 'nw')
        self.button2.place(x = 175, y = 200, anchor = 'nw')
        self.button3.place(x = 320, y = 200, anchor = 'nw')

        #固定區塊home跟返回鍵
        back = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\返回鍵.png")  #返回鍵按鈕圖片檔案位置
        back = back.resize((25, 25), Image.ANTIALIAS)
        self.back = ImageTk.PhotoImage(back)
        self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_frame(self, Choose_Food))  #返回鍵按鈕外型+跳轉命令

        home = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\首頁鍵.png")  #首頁鍵按鈕圖片檔案位置
        home = home.resize((37, 30), Image.ANTIALIAS)
        self.home = ImageTk.PhotoImage(home)
        self.homebutton = tk.Button(self, image= self.home, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_home(self, FirstPage))  #首頁鍵按鈕外型+跳轉命令

        self.backbutton.place(x = 10, y = 14, anchor = 'nw')
        self.homebutton.place(x = 450, y = 11, anchor = 'nw')

class game3(tk.Frame):  #選擇食物畫面

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

        image1 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\內向.png")  #內向按鈕圖片檔案位置
        image1 = image1.resize((150, 75), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image1)
        self.button1 = tk.Button(self, image= self.image1, relief="flat", bg = '#FFEED2', border = 0, command = lambda: root.switch_game(self, game4, '內向'))  #按鈕外型+跳轉命令

        image2 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\外向.png")  #外向按鈕圖片檔案位置
        image2 = image2.resize((150, 75), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image2)
        self.button2 = tk.Button(self, image= self.image2, relief="flat", bg = '#FFEED2', border = 0, command = lambda: root.switch_game(self, game4, '外向'))  #按鈕外型+跳轉命令

        image3 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\吐司人3.png")  #吐司人3圖片檔案位置
        image3 = image3.resize((370, 370), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(image3)
        self.lb3 = tk.Label(self, image= self.image3, bg = '#FFEED2', border = 0)

        self.lb1.place(x = 0, y = 0, anchor = 'nw', width = 500, height = 60)
        self.lb2.place(x = 40, y = 130, anchor = 'nw')
        self.lb3.place(x = 65, y = 300, anchor = 'nw')
        self.button1.place(x = 80, y = 200, anchor = 'nw')
        self.button2.place(x = 255, y = 200, anchor = 'nw')

        #固定區塊home跟返回鍵
        back = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\返回鍵.png")  #返回鍵按鈕圖片檔案位置
        back = back.resize((25, 25), Image.ANTIALIAS)
        self.back = ImageTk.PhotoImage(back)
        self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_game_back(self, game2))  #返回鍵按鈕外型+跳轉命令

        home = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\首頁鍵.png")  #首頁鍵按鈕圖片檔案位置
        home = home.resize((37, 30), Image.ANTIALIAS)
        self.home = ImageTk.PhotoImage(home)
        self.homebutton = tk.Button(self, image= self.home, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_home(self, FirstPage))  #首頁鍵按鈕外型+跳轉命令

        self.backbutton.place(x = 10, y = 14, anchor = 'nw')
        self.homebutton.place(x = 450, y = 11, anchor = 'nw')

class game4(tk.Frame):  #選擇食物畫面

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(bg = '#FFEED2')
        self.creatWidgets()
        self.pack(fill = "both", expand = True)

    def creatWidgets(self):

        f1 = tkFont.Font(size = 18, family = 'jf open 粉圓 1.1')
        f2 = tkFont.Font(size = 32, family = 'jf open 粉圓 1.1')
        f3 = tkFont.Font(size = 16, family = 'jf open 粉圓 1.1')

        self.lb1 = tk.Label(self, text = 'FindEat   —   找食瞭瞭', bg = '#FFE9C4', font = f1, fg = '#FFB140')
        self.lb2 = tk.Label(self, text = "適合你吃的食物是:", bg = '#FFEED2', font = f2, fg = '#554640')

        foodlist = ['義大利麵', '咖哩', '牛排', '粥', '冰品', '飲料', '火鍋', '水餃/鍋貼', '小吃', '炒飯'
                   ,  '日式料理', '韓式料理', '泰式料理', '滷味', '鹹酥雞', '便當', '早午餐', '低GI', '拉麵', '素食', '速食']
        food = str(random.choices(foodlist)[0])
        self.lb3 = tk.Label(self, text = food + '!', bg = '#FFEED2', font = f2, fg = '#554640')

        image1 = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\方框.png")
        image1 = image1.resize((400, 50), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image1)
        self.lb4 = tk.Label(self, image= self.image1, bg = '#FFEED2', border = 0)

        self.button1 = tk.Button(self, text = "找附近的" + food + '餐廳', bg = '#514C44', font = f3, fg = 'white', relief="flat", command = lambda: root.switch_frame3(self, Choose_Place, food))

        self.lb1.place(x = 0, y = 0, anchor = 'nw', width = 500, height = 60)
        self.lb2.place(x = 70, y = 130, anchor = 'nw')

        if len(food) == 1:
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

        if len(food) == 1:
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
        back = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\返回鍵.png")  #返回鍵按鈕圖片檔案位置
        back = back.resize((25, 25), Image.ANTIALIAS)
        self.back = ImageTk.PhotoImage(back)
        self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_game_back(self, game3))  #返回鍵按鈕外型+跳轉命令

        home = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\首頁鍵.png")  #首頁鍵按鈕圖片檔案位置
        home = home.resize((37, 30), Image.ANTIALIAS)
        self.home = ImageTk.PhotoImage(home)
        self.homebutton = tk.Button(self, image= self.home, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_home(self, FirstPage))  #首頁鍵按鈕外型+跳轉命令

        self.backbutton.place(x = 10, y = 14, anchor = 'nw')
        self.homebutton.place(x = 450, y = 11, anchor = 'nw')

class Final(tk.Frame):  #選擇食物畫面

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(bg = '#FFEED2')
        self.creatWidgets()
        self.pack(fill = "both", expand = True)

    def creatWidgets(self):
        f1 = tkFont.Font(size = 18, family = 'jf open 粉圓 1.1')

        self.cv1 = tk.Canvas(self, bg = '#FFEED2', width = 500, height = 600)
        self.cv1.place(x = 0, y = 57)
        scroll_y = tk.Scrollbar(self, orient="vertical", command = self.cv1.yview)
        scroll_y.place(x = 500, y = 55, anchor = 'ne', height = 600)
        self.cv1.create_oval(10, 10, 20, 20, fill="red")
        self.cv1.create_oval(200, 200, 820, 820, fill="blue")
        self.cv1.configure(scrollregion=self.cv1.bbox('all'), yscrollcommand=scroll_y.set)

        self.lb1 = tk.Label(self, text = 'FindEat   —   找食瞭瞭', bg = '#FFE9C4', font = f1, fg = '#FFB140')
        self.lb1.place(x = 0, y = 0, anchor = 'nw', width = 500, height = 60)

        #固定區塊home跟返回鍵
        back = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\返回鍵.png")  #返回鍵按鈕圖片檔案位置
        back = back.resize((25, 25), Image.ANTIALIAS)
        self.back = ImageTk.PhotoImage(back)
        if len(gamelist) != 0:
            self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_frame(self, Choose_Place))  #返回鍵按鈕外型+跳轉命令
        else:
            self.backbutton = tk.Button(self, image= self.back, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_list1_back(self, Choose_Type))  #返回鍵按鈕外型+跳轉命令

        home = Image.open("C:\\Users\\jenny\\Desktop\\商管程式設計\\期末報告\\首頁鍵.png")  #首頁鍵按鈕圖片檔案位置
        home = home.resize((37, 30), Image.ANTIALIAS)
        self.home = ImageTk.PhotoImage(home)
        self.homebutton = tk.Button(self, image= self.home, relief="flat", bg = '#FFE9C4', command = lambda: root.switch_frame2(self, FirstPage))  #首頁鍵按鈕外型+跳轉命令

        self.backbutton.place(x = 10, y = 14, anchor = 'nw')
        self.homebutton.place(x = 450, y = 11, anchor = 'nw')

if __name__ == "__main__":
    app = root()
    app.mainloop()
