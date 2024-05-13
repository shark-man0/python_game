import random as rm
import tkinter as tk
import sys
import numpy as np

# ウェジットの作成
root = tk.Tk()
root.geometry("500x400") # 横x高さ
root.title("マルバツゲーム")

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turn = 1
x = 50
y = 0

p1n = ""
p2n = ""
name2 = tk.Label(text="プレイヤー２の名前を入力")
r1 = 109+x
r2 = 156+x
r3 = 203+x
g1 = 75+y
g2 = 122+y
g3 = 169+y
memori_point = np.array([[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]])

yline1 = tk.Label(text="|")
yline2 = tk.Label(text="|")
yline3 = tk.Label(text="|")
yline4 = tk.Label(text="|")
yline5 = tk.Label(text="|")
yline6 = tk.Label(text="|")

yline7 = tk.Label(text="|")
yline8 = tk.Label(text="|")
yline9 = tk.Label(text="|")
yline10 = tk.Label(text="|")
yline11 = tk.Label(text="|")
yline12 = tk.Label(text="|")

yline13 = tk.Label(text="|")
yline14 = tk.Label(text="|")
yline15 = tk.Label(text="|")
yline16 = tk.Label(text="|")
yline17 = tk.Label(text="|")
yline18 = tk.Label(text="|")

yline19 = tk.Label(text="|")
yline20 = tk.Label(text="|")
yline21 = tk.Label(text="|")
yline22 = tk.Label(text="|")
yline23 = tk.Label(text="|")
yline24 = tk.Label(text="|")


xline1 = tk.Label(text="------")
xline2 = tk.Label(text="------")
xline3 = tk.Label(text="------")
#xline4 = tk.Label(text="----")

xline5 = tk.Label(text="------")
xline6 = tk.Label(text="------")
xline7 = tk.Label(text="------")
#xline8 = tk.Label(text="----")

xline9 = tk.Label(text="------")
xline10 = tk.Label(text="------")
xline11 = tk.Label(text="------")
#xline12 = tk.Label(text="----")

xline13 = tk.Label(text="------")
xline14 = tk.Label(text="------")
xline15 = tk.Label(text="------")
#xline16 = tk.Label(text="----")

o_1 = "⭕️"
o_2 = "⭕️"
o_3 = "⭕️"
o_4 = "⭕️"
o_5 = "⭕️"
o1 = tk.Label(text=o_1)
o2 = tk.Label(text=o_2)
o3 = tk.Label(text=o_3)
o4 = tk.Label(text=o_4)
o5 = tk.Label(text=o_5)

x_1 = "❌"
x_2 = "❌"
x_3 = "❌"
x_4 = "❌"
x1 = tk.Label(text=x_1)
x2 = tk.Label(text=x_2)
x3 = tk.Label(text=x_3)
x4 = tk.Label(text=x_4)

def stop_pro():
    sys.exit()

def check_turn(plc):
    if plc == 1:
        r = r1
        g = g1
    elif plc == 2:
        r = r2
        g = g1
    elif plc == 3:
        r = r3
        g = g1
    elif plc == 4:
        r = r1
        g = g2
    elif plc == 5:
        r = r2
        g = g2
    elif plc == 6:
        r = r3
        g = g2
    elif plc == 7:
        r = r1
        g = g3
    elif plc == 8:
        r = r2
        g = g3
    elif plc == 9:
        r = r3
        g = g3
    if turn == 1:
        o1.place(x=r, y=g)
    elif turn == 2:
        x1.place(x=r, y=g)
    elif turn == 3:
        o2.place(x=r, y=g)
    elif turn == 4:
        x2.place(x=r, y=g)
    elif turn == 5:
        o3.place(x=r, y=g)
    elif turn == 6:
        x3.place(x=r, y=g)
    elif turn == 7:
        o4.place(x=r, y=g)
    elif turn == 8:
        x4.place(x=r, y=g)
    elif turn == 9:
        o5.place(x=r, y=g)

def mem_mark(plc):
    if turn%2 == 1:
        if plc == 1:
            memori_point[0, 0] = 1
        elif plc == 2:
            memori_point[1, 0] = 1
        elif plc == 3:
            memori_point[2, 0] = 1
        elif plc == 4:
            memori_point[0, 1] = 1
        elif plc == 5:
            memori_point[1, 1] = 1
        elif plc == 6:
            memori_point[2, 1] = 1
        elif plc == 7:
            memori_point[0, 2] = 1
        elif plc == 8:
            memori_point[1, 2] = 1
        elif plc == 9:
            memori_point[2, 2] = 1
    elif turn%2 == 0:
        if plc == 1:
            memori_point[0, 0] = 2
        elif plc == 2:
            memori_point[1, 0] = 2
        elif plc == 3:
            memori_point[2, 0] = 2
        elif plc == 4:
            memori_point[0, 1] = 2
        elif plc == 5:
            memori_point[1, 1] = 2
        elif plc == 6:
            memori_point[2, 1] = 2
        elif plc == 7:
            memori_point[0, 2] = 2
        elif plc == 8:
            memori_point[1, 2] = 2
        elif plc == 9:
            memori_point[2, 2] = 2

def check_win():
        # 丸チェック
    if (np.all(memori_point[0:3, 0] == np.array([1, 1, 1])) or
        np.all(memori_point[0:3, 1] == np.array([1, 1, 1])) or
        np.all(memori_point[0:3, 2] == np.array([1, 1, 1])) or
        np.all(memori_point[0, 0:3] == np.array([1, 1, 1])) or
        np.all(memori_point[1, 0:3] == np.array([1, 1, 1])) or
        np.all(memori_point[2, 0:3] == np.array([1, 1, 1])) or
        np.all(np.array([memori_point[0, 0], memori_point[1, 1], memori_point[2, 2]]) == np.array([1, 1, 1])) or
        np.all(np.array([memori_point[2, 0], memori_point[1, 1], memori_point[0, 2]]) == np.array([1, 1, 1]))):
        result = "先行の勝利"
        result_text = tk.Label(text=result)
        result_text.place(x=200, y=300)

    # バツチェック
    if (np.all(memori_point[0:3, 0] == np.array([2, 2, 2])) or
        np.all(memori_point[0:3, 1] == np.array([2, 2, 2])) or
        np.all(memori_point[0:3, 2] == np.array([2, 2, 2])) or
        np.all(memori_point[0, 0:3] == np.array([2, 2, 2])) or
        np.all(memori_point[1, 0:3] == np.array([2, 2, 2])) or
        np.all(memori_point[2, 0:3] == np.array([2, 2, 2])) or
        np.all(np.array([memori_point[0, 0], memori_point[1, 1], memori_point[2, 2]]) == np.array([2, 2, 2])) or
        np.all(np.array([memori_point[2, 0], memori_point[1, 1], memori_point[0, 2]]) == np.array([2, 2, 2]))):
        result = "後攻の勝利"
        result_text = tk.Label(text=result)
        result_text.place(x=200, y=300)

def disable():
    p1_button.configure(state="disable")
    p2_button.configure(state="disable")
    p3_button.configure(state="disable")
    p4_button.configure(state="disable")
    p5_button.configure(state="disable")
    p6_button.configure(state="disable")
    p7_button.configure(state="disable")
    p8_button.configure(state="disable")
    p9_button.configure(state="disable")

def replace():
    xline1.place(x=100+x, y=50+y)
    xline2.place(x=147+x, y=50+y)
    xline3.place(x=194+x, y=50+y)
    #xline4.place(x=250, y=50)

    xline5.place(x=100+x, y=97+y)
    xline6.place(x=147+x, y=97+y)
    xline7.place(x=194+x, y=97+y)
    #xline8.place(x=250, y=100)

    xline9.place(x=100+x, y=144+y)
    xline10.place(x=147+x, y=144+y)
    xline11.place(x=194+x, y=144+y)
    #xline12.place(x=250, y=150)

    xline13.place(x=100+x, y=191+y)
    xline14.place(x=147+x, y=191+y)
    xline15.place(x=194+x, y=191+y)
    #xline16.place(x=250, y=200)


    yline1.place(x=93+x, y=62+y)
    yline2.place(x=93+x, y=84+y)
    yline3.place(x=93+x, y=110+y)
    yline4.place(x=93+x, y=132+y)
    yline5.place(x=93+x, y=158+y)
    yline6.place(x=93+x, y=180+y)

    yline7.place(x=140+x, y=62+y)
    yline8.place(x=140+x, y=84+y)
    yline9.place(x=140+x, y=110+y)
    yline10.place(x=140+x, y=132+y)
    yline11.place(x=140+x, y=158+y)
    yline12.place(x=140+x, y=180+y)

    yline13.place(x=187+x, y=62+y)
    yline14.place(x=187+x, y=84+y)
    yline15.place(x=187+x, y=110+y)
    yline16.place(x=187+x, y=132+y)
    yline17.place(x=187+x, y=158+y)
    yline18.place(x=187+x, y=180+y)

    yline19.place(x=234+x, y=62+y)
    yline20.place(x=234+x, y=84+y)
    yline21.place(x=234+x, y=110+y)
    yline22.place(x=234+x, y=132+y)
    yline23.place(x=234+x, y=158+y)
    yline24.place(x=234+x, y=180+y)


    p1_button.place(x=99+x, y=65+y)
    p2_button.place(x=146+x, y=65+y)
    p3_button.place(x=193+x, y=65+y)
    p4_button.place(x=99+x, y=112+y)
    p5_button.place(x=146+x, y=112+y)
    p6_button.place(x=193+x, y=112+y)
    p7_button.place(x=99+x, y=159+y)
    p8_button.place(x=146+x, y=159+y)
    p9_button.place(x=193+x, y=159+y)

def plant1():
    global turn
    p1_button.place_forget()
    check_turn(1)
    mem_mark(1)
    check_win()
    turn += 1
def plant2():
    global turn
    p2_button.place_forget()
    check_turn(2)
    mem_mark(2)
    check_win()
    turn += 1
def plant3():
    global turn
    p3_button.place_forget()
    check_turn(3)
    mem_mark(3)
    check_win()
    turn += 1
def plant4():
    global turn
    p4_button.place_forget()
    check_turn(4)
    mem_mark(4)
    check_win()
    turn += 1
def plant5():
    global turn
    p5_button.place_forget()
    check_turn(5)
    mem_mark(5)
    check_win()
    turn += 1
def plant6():
    global turn
    p6_button.place_forget()
    check_turn(6)
    mem_mark(6)
    check_win()
    turn += 1
def plant7():
    global turn
    p7_button.place_forget()
    check_turn(7)
    mem_mark(7)
    check_win()
    turn += 1
def plant8():
    global turn
    p8_button.place_forget()
    check_turn(8)
    mem_mark(8)
    check_win()
    turn += 1
def plant9():
    global turn
    p9_button.place_forget()
    check_turn(9)
    mem_mark(9)
    check_win()
    turn += 1

exit_button = tk.Button(text="exit", command=stop_pro)
p1_button = tk.Button(text="1", width=1, height=2, command=plant1)
p2_button = tk.Button(text="2", width=1, height=2, command=plant2)
p3_button = tk.Button(text="3", width=1, height=2, command=plant3)
p4_button = tk.Button(text="4", width=1, height=2, command=plant4)
p5_button = tk.Button(text="5", width=1, height=2, command=plant5)
p6_button = tk.Button(text="6", width=1, height=2, command=plant6)
p7_button = tk.Button(text="7", width=1, height=2, command=plant7)
p8_button = tk.Button(text="8", width=1, height=2, command=plant8)
p9_button = tk.Button(text="9", width=1, height=2, command=plant9)

replace()

exit_button.place(x=400, y=350)

if turn == 10:
    result = "引き分け"
    result_text = tk.Label(text=result)
    result_text.place(x=200, y=300)

root.mainloop() # 表示

    # entry の作成
    # get で取得
    # enable関数とdisable関数の作成(buttonを表示したり非表示にしたり)
    # replace関数の作成(罫線の再設置) -> 名前の取得、使用目的
    # まっさらな状態で名前を入力、その後罫線を配置。全て関数で処理
    # while文を消して、定義、関数、処理の順に並び替える(整頓する)
