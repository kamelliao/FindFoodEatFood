import tkinter as tk
import tkinter.font as tkFont
from PIL import Image
from PIL import ImageTk

class root(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x650')
        self.title('FindEat 找食瞭瞭')
        self._frame = None
        self.switch_frame(FindEat1)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class FindEat1(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg = 'white')
        self.creatWidgets()
        self.pack(fill = "both", expand = True)

    def creatWidgets(self):
        f1 = tkFont.Font(size = 31, family = 'jf open 粉圓 1.1')
        f2 = tkFont.Font(size = 22, family = 'jf open 粉圓 1.1')
        f3 = tkFont.Font(size = 40, family = 'jf open 粉圓 1.1')

        self.lb1 = tk.Label(self, text = 'FindEat', bg = 'white', font = f1, fg = 'orange')
        self.lb2 = tk.Label(self, text = '找食瞭瞭', bg = 'white', font = f2, fg = 'orange')
        self.lb3 = tk.Label(self, text = '我想找...', bg = 'white', font = f3, fg = 'saddlebrown')

        image1 = Image.open("C:\\Users\\jenny\\Desktop\\1.png")
        image1 = image1.resize((140, 55), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image1)
        self.button1 = tk.Button(self, image= self.image1, relief="flat", bg = 'white', command = lambda: root.switch_frame(self, FindEat2))
        
        image2 = Image.open("C:\\Users\\jenny\\Desktop\\2.png")
        image2 = image2.resize((140, 55), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image2)
        self.button2 = tk.Button(self, image= self.image2, relief="flat", bg = 'white', command = lambda: root.switch_frame(self, FindEat2))

        self.lb1.place(x = 165, y = 50, anchor = 'nw')
        self.lb2.place(x = 186, y = 102, anchor = 'nw')
        self.lb3.place(x = 147, y = 256, anchor = 'nw')
        self.button1.place(x = 173, y = 332, anchor = 'nw')
        self.button2.place(x = 173, y = 412, anchor = 'nw')

class FindEat2(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(bg = 'blanchedalmond')
        self.creatWidgets()
        self.pack(fill = "both", expand = True)

    def creatWidgets(self):
        f1 = tkFont.Font(size = 14, family = 'jf open 粉圓 1.1')
        f2 = tkFont.Font(size = 23, family = 'jf open 粉圓 1.1')
        f3 = tkFont.Font(size = 40, family = 'jf open 粉圓 1.1')

        self.lb1 = tk.Label(self, text = 'FindEat   —   找食瞭瞭', bg = '#FFDEAD', font = f1, fg = 'orange')
        self.lb2 = tk.Label(self, text = '現在想去哪吃飯呢?', bg = 'blanchedalmond', font = f2, fg = 'gray')
        self.lb3 = tk.Button(self, text = '返回!', relief="flat", bg = 'blanchedalmond', font = f3, fg = 'saddlebrown', command = lambda: root.switch_frame(self, FindEat1))
        
        self.lb1.place(x = 0, y = 0, anchor = 'nw', width = 500, height = 50)
        self.lb2.place(x = 120, y = 130, anchor = 'nw')
        self.lb3.place(x = 147, y = 256, anchor = 'nw')
        

if __name__ == "__main__":
    app = root()
    app.mainloop()