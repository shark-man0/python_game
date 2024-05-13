#! /usr/bin/env python3
import tkinter as tk
import sys
import random as rm

while True:

    # カードボックス
    kh_list = ['hA', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'hJ', 'hQ', 'hK']
    kd_list = ['dA', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'dJ', 'dQ', 'dK']
    ks_list = ['sA', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 'sJ', 'sQ', 'sK']
    kc_list = ['cA', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'cJ', 'cQ', 'cK']
    kard_list = kh_list + kd_list + ks_list + kc_list
    cp_list = kard_list
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dec_info = {**dict(zip(kh_list, numbers)), **dict(zip(kd_list, numbers)), **dict(zip(ks_list, numbers)), **dict(zip(kc_list, numbers))}

    def stopex():
        sys.exit()

    def firstDraw():
        startbutton.place_forget()
        draw_button.place(x=225, y=325)
        stand_button.place(x=150, y=325)
        text1.place(x=200, y=250)
        text2.place(x=200, y=275)
        text3.place(x=200, y=175)
        text4.place(x=100, y=25)
        text5.place(x=200, y=50)
        text6.place(x=200, y=75)
        text9.place(x=100, y=50)
        text10.place(x=100, y=75)
        text11.place(x=100, y=225)
        text12.place(x=100, y=250)
        text13.place(x=100, y=275)
        for inten in range(2):
            nameplate_deal.append(cp_list.pop(rm.choice(range(len(cp_list)))))
            nameplate_ndeal = int(dec_info[nameplate_deal[-1]])
            ent2.insert(tk.END,nameplate_ndeal)
            n_deal.append(int(ent2.get()))
            ent2.delete(0, tk.END)
        ent3.insert(tk.END,nameplate_deal[-1])
        nameplate_deal.pop(-1)
        nameplate_deal.append("？")
        number = "？"
        text5.configure(text=nameplate_deal)
        text6.configure(text=number)

        for inten in range(2):
            nameplate_pl1.append(cp_list.pop(rm.choice(range(len(cp_list)))))
            nameplate_n = dec_info[nameplate_pl1[-1]]
            ent.insert(tk.END,nameplate_n)
            n.append(int(ent.get()))
            amo = n.count(1)
            if sum(n) >= 21:
                amo = 0
            if amo > 0:
                n11.clear()
                n11.extend(n)
                for i in range(amo):
                    n11.remove(1)
                    n11.append(11)
                    if sum(n11) == 21:
                        n.clear()
                        n.extend(n11)
                        break
                    elif sum(n11) >= 21:
                        break
            ent.delete(0, tk.END)
            numb = sum(n)
            if numb == 21:
                text1.configure(text=nameplate_pl1)
                text2.configure(text=numb)
                text8.place(x=200, y=150)
                if n_deal != 21:
                    text8.configure(text="Black Jack!")
                    draw_button.configure(state="disable")
                    stand_button.configure(state="disable")
                else:
                    draw_button.configure(state="disable")
            else:
                text2.configure(text=numb)
                text1.configure(text=nameplate_pl1)

    def hit_kard():
        nameplate_pl1.append(cp_list.pop(rm.choice(range(len(cp_list)))))
        nameplate_n = dec_info[nameplate_pl1[-1]]
        ent.insert(tk.END,nameplate_n)
        n.append(int(ent.get()))
        amo = n.count(1)
        if sum(n) >= 21:
            amo = 0
        if amo > 0:
            n11.clear()
            n11.extend(n)
            for i in range(amo):
                n11.remove(1)
                n11.append(11)
                if sum(n11) == 21:
                    n.clear()
                    n.extend(n11)
                    break
                elif sum(n11) >= 21:
                    break
        ent.delete(0, tk.END)
        numb = sum(n)
        if numb > 21:
            text1.configure(text=nameplate_pl1)
            text2.configure(text="burst!")
            draw_button.configure(state="disable")
            stand_button.configure(state="disable")
            text3.configure(text="you lose!")
        elif numb == 21:
            text1.configure(text=nameplate_pl1)
            text2.configure(text=numb)
            draw_button.configure(state="disable")
        else:
            text2.configure(text=numb)
            text1.configure(text=nameplate_pl1)

    def stand():
        text7.place(x=200, y=200)
        stand_button.configure(state="disable")
        draw_button.configure(state="disable")
        reg = str(ent3.get())
        nameplate_deal.pop(-1)
        nameplate_deal.append(reg)
        ent3.delete(0,tk.END)
        amo_deal = n_deal.count(1)
        if sum(n_deal) >= 21:
            amo_deal = 0
        if amo_deal > 0:
            n11_deal.clear()
            n11_deal.extend(n_deal)
            for i in range(amo_deal):
                n11_deal.remove(1)
                n11_deal.append(11)
                if sum(n11_deal) == 21:
                    n_deal.clear()
                    n_deal.extend(n11_deal)
                    break
                elif sum(n11_deal) >= 21:
                    break
        number = sum(n_deal)
        if number == 21:
            text5.configure(text=nameplate_deal)
            text6.configure(text=number)
            if sum(n) != 21:
                text3.configure(text="you lose!")
            else:
                text3.configure(text="push!")
        else:
            text6.configure(text=number)
            text5.configure(text=nameplate_deal)
        while sum(n_deal) <= 17:
            nameplate_deal.append(cp_list.pop(rm.choice(range(len(cp_list)))))
            nameplate_ndeal = dec_info[nameplate_deal[-1]]
            ent2.insert(tk.END,nameplate_ndeal)
            n_deal.append(int(ent2.get()))
            amo_deal = n_deal.count(1)
            if sum(n_deal) >= 21:
                amo_deal = 0
            if amo_deal > 0:
                n11_deal.clear()
                n11_deal.extend(n_deal)
                for i in range(amo_deal):
                    n11_deal.remove(1)
                    n11_deal.append(11)
                    if sum(n11_deal) == 21:
                        n_deal.clear()
                        n_deal.extend(n11_deal)
                        break
                    elif sum(n11_deal) >= 21:
                        break
            ent2.delete(0, tk.END)
            number = sum(n_deal)
            if number > 21:
                text5.configure(text=nameplate_deal)
                text6.configure(text="burst!")
                text3.configure(text="you win!")
            elif number == 21:
                text5.configure(text=nameplate_deal)
                text6.configure(text=number)
                if sum(n) != 21:
                    text3.configure(text="you lose!")
                else:
                    text3.configure(text="push!")
            else:
                text6.configure(text=number)
                text5.configure(text=nameplate_deal)
        if sum(n_deal) <= 21:
            if (sum(n_deal) <= sum(n)) == True:
                text3.configure(text="you win!")
            else:
                text3.configure(text="you lose!")

    def reset():
        root.destroy()

    root = tk.Tk()
    # root.geometry("500x400") # 横x高さ
    root.attributes('-fullscreen', True)
    root.title("Black Jack")

    nameplate_pl1 = []
    n = []
    n11 = []
    nameplate_deal = []
    n_deal = []
    n11_deal = []

    # labelの定義
    label = tk.Label(text="The Black Jack")
    text1 = tk.Label(text="")
    text2 = tk.Label(text="")
    text3 = tk.Label(text="")
    text4 = tk.Label(text="dealer")
    text5 = tk.Label(text="")
    text6 = tk.Label(text="")
    text7 = tk.Label(text="stand")
    text8 = tk.Label(text="")
    text9 = tk.Label(text="dealer's cards")
    text10 = tk.Label(text="sum number")
    text11 = tk.Label(text="you")
    text12 = tk.Label(text="your cards")
    text13 = tk.Label(text="sum number")

    # buttonの定義
    fin = tk.Button(text="finish", command=stopex)
    startbutton = tk.Button(text="start", command=firstDraw)
    draw_button = tk.Button(text="hit", command=hit_kard)
    stand_button = tk.Button(text="stand", command=stand)
    reset_button = tk.Button(text="reset", command=reset)

    # entryの定義
    ent = tk.Entry()
    ent2 = tk.Entry()
    ent3 = tk.Entry()
    ent4 = tk.Entry()
    ent5 = tk.Entry()

    # labelの位置決定
    label.place(x=25, y= 0)
    text1.place(x=200, y=250)
    text1.place_forget()
    text2.place(x=200, y=275)
    text2.place_forget()
    text3.place(x=200, y=175)
    text3.place_forget()
    text4.place(x=100, y=25)
    text4.place_forget()
    text5.place(x=200, y=50)
    text5.place_forget()
    text6.place(x=200, y=75)
    text6.place_forget()
    text7.place(x=200, y=200)
    text7.place_forget()
    text8.place(x=200, y=150)
    text8.place_forget()
    text9.place(x=100, y=50)
    text9.place_forget()
    text10.place(x=100, y=75)
    text10.place_forget()
    text11.place(x=100, y=225)
    text11.place_forget()
    text12.place(x=100, y=250)
    text12.place_forget()
    text13.place(x=100, y=275)
    text13.place_forget()

    # buttonの位置決定
    startbutton.place(x=200, y=200)
    draw_button.place(x=225, y=325)
    draw_button.place_forget()
    stand_button.place(x=150, y=325)
    stand_button.place_forget()
    fin.place(x=400, y=360)
    reset_button.place(x=50, y=360)

    # entryの位置決定
    ent.place(x=10000, y=10000)
    ent2.place(x=10000, y=10000)
    ent3.place(x=10000, y=10000)
    ent4.place(x=10000, y=10000)
    ent5.place(x=10000, y=10000)

    root.mainloop() # 表示
