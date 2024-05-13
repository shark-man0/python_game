import random as rm
import time
player1_HP = 0
player1_TP = 0
player1_cost = 0
player1_zo = 0
player2_HP = 0
player2_TP = 0
player2_cost = 0
player2_zo = 0
cpu1_HP = 0
cpu1_TP = 0
cpu1_cost = 0
cpu1_zo = 0
cpu2_HP = 0
cpu2_TP = 0
cpu2_cost = 0
cpu2_zo = 0
cpu3_HP = 0
cpu3_TP = 0
cpu3_cost = 0
cpu3_zo = 0
random_cost = 0
zi_dam1 = 0
zi_heal1 = 0
zi_shield1 = 0
zi_dam2 = 0
zi_heal2 = 0
zi_shield2 = 0
add_dam = 0
action1 = ("通常攻撃　　　　")
action1_cost = 1
action1_getTP = 10
action3 = ("防御　　　　　　")
action3_cost = 0
action3_getTP = 5
count = 0
shield1_num = 0
shield2_num = 0
HP1_num = 0
HP2_num = 0
fire1_num = 0
fire2_num = 0
d_mv1 = 0
d_mv2 = 0
rm_num = 0
atack1_HP = 0
d_ata1 = 0
d_ata2 = 0
print("1. プレイヤー vs プレイヤー")
print("2. プレイヤー vs CPU ")
print("3. ハーフモード")
print()
game_mode = int(input("ゲームモードを選択してください。　"))
if (game_mode != 1) and (game_mode != 2) and (game_mode != 3) :
    print("存在しないゲームモードです。")
if game_mode == 1 :
    print()
    count_name1 = 0
    while count_name1 == 0 :
        player1_name = input("プレイヤー１の名前を入力してください。(8字以内,半角英数字)　")
        pl1name = len(player1_name)
        if pl1name > 9:
            print("8字以内で名前を決めてください。")
        else :
            break
    pl1_name = map(str,player1_name)
    pl1name_b = list(pl1_name)
    pl1name_num = 8 - pl1name
    for i in range(pl1name_num) :
        pl1name_b.append(" ")
    pl1name_l = "".join(pl1name_b)
    count_name2 = 0
    while count_name2 == 0 :
        player2_name = input("プレイヤー２の名前を入力してください。(8字以内,半角英数字)　")
        pl2name = len(player2_name)
        if pl2name > 9:
            print("8字以内で名前を決めてください。")
        else :
            break
    pl2_name = map(str,player2_name)
    pl2name_b = list(pl2_name)
    pl2name_num = 8 - pl2name
    for i in range(pl2name_num) :
        pl2name_b.append(" ")
    pl2name_l = "".join(pl2name_b)
    print()
    player1_zo = int(rm.choice(range(1,8)))
    if player1_zo == 1 :
        player1_zokusei = ("火　")
        player1_HP = 1000.0
        pl1action2 = ("火炎放射　　　　")
        pl1action2_cost = 5
        pl1action2_getTP = 20
        pl1action4 = ("メラバーン　　　")
        pl1action4_cost = 3
        pl1ac4cost_TP = 100
    elif player1_zo == 2 :
        player1_zokusei = ("水　")
        player1_HP = 700.0
        pl1action2 = ("回復　　　　　　")
        pl1action2_cost = 4
        pl1action2_getTP = 25
        pl1action4 = ("洪水　　　　　　")
        pl1action4_cost = 2
        pl1ac4cost_TP = 100
    elif player1_zo == 3 :
        player1_zokusei = ("草　")
        player1_HP = 1000.0
        pl1action2 = ("持続回復　　　　")
        pl1action2_cost = 3
        pl1action2_getTP = 25
        pl1action4 = ("植物による足止め")
        pl1action4_cost = 3
        pl1ac4cost_TP = 80
    elif player1_zo == 4 :
        player1_zokusei = ("氷　")
        player1_HP = 1000.0
        pl1action2 = ("冷凍保存　　　　")
        pl1action2_cost = 3
        pl1action2_getTP = 15
        pl1action4 = ("氷の結晶　　　　")
        pl1action4_cost = 2
        pl1ac4cost_TP = 90
    elif player1_zo == 5 :
        player1_zokusei = ("物理")
        player1_HP = 950.0
        pl1action2 = ("自己犠牲　　　　")
        pl1action2_cost = 1
        pl1action2_getTP = 20
        pl1action4 = ("微回復　　　　　")
        pl1action4_cost = 5
        pl1ac4cost_TP = 0
    elif player1_zo == 6 :
        player1_zokusei = ("闇　")
        player1_HP = 900.0
        pl1action2 = ("吸収　　　　　　")
        pl1action2_cost = 5
        pl1action2_getTP = 25
        pl1action4 = ("ブラックホール　")
        pl1action4_cost = 7
        pl1ac4cost_TP = 100
    elif player1_zo == 7 :
        player1_zokusei = ("光　")
        player1_HP = 350.0
        pl1action2 = ("ヒーリング　　　")
        pl1action2_cost = 2
        pl1action2_getTP = 10
        pl1action4 = ("ホーリーライト　")
        pl1action4_cost = 3
        pl1ac4cost_TP = 80
    player2_zo = int(rm.choice(range(1,8)))
    if player2_zo == 1 :
        player2_zokusei = ("火　")
        player2_HP = 1000.0
        pl2action2 = ("火炎放射　　　　")
        pl2action2_cost = 5
        pl2action2_getTP = 20
        pl2action4 = ("メラバーン　　　")
        pl2action4_cost = 3
        pl2ac4cost_TP = 100
    elif player2_zo == 2 :
        player2_zokusei = ("水　")
        player2_HP = 700.0
        pl2action2 = ("回復　　　　　　")
        pl2action2_cost = 4
        pl2action2_getTP = 25
        pl2action4 = ("洪水　　　　　　")
        pl2action4_cost = 2
        pl2ac4cost_TP = 100
    elif player2_zo == 3 :
        player2_zokusei = ("草　")
        player2_HP = 1000.0
        pl2action2 = ("持続回復　　　　")
        pl2action2_cost = 3
        pl2action2_getTP = 25
        pl2action4 = ("植物による足止め")
        pl2action4_cost = 3
        pl2ac4cost_TP = 80
    elif player2_zo == 4 :
        player2_zokusei = ("氷　")
        player2_HP = 1000.0
        pl2action2 = ("冷凍保存　　　　")
        pl2action2_cost = 3
        pl2action2_getTP = 15
        pl2action4 = ("氷の結晶　　　　")
        pl2action4_cost = 2
        pl2ac4cost_TP = 90
    elif player2_zo == 5 :
        player2_zokusei = ("物理")
        player2_HP = 950.0
        pl2action2 = ("自己犠牲　　　　")
        pl2action2_cost = 1
        pl2action2_getTP = 20
        pl2action4 = ("微回復　　　　　")
        pl2action4_cost = 5
        pl2ac4cost_TP = 0
    elif player2_zo == 6 :
        player2_zokusei = ("闇　")
        player2_HP = 900.0
        pl2action2 = ("吸収　　　　　　")
        pl2action2_cost = 5
        pl2action2_getTP = 25
        pl2action4 = ("ブラックホール　")
        pl2action4_cost = 7
        pl2ac4cost_TP = 100
    elif player2_zo == 7 :
        player2_zokusei = ("光　")
        player2_HP = 350.0
        pl2action2 = ("ヒーリング　　　")
        pl2action2_cost = 2
        pl2action2_getTP = 10
        pl2action4 = ("ホーリーライト　")
        pl2action4_cost = 3
        pl2ac4cost_TP = 80
    print(pl1name_l,"の属性は",player1_zokusei,"です。 HPは",player1_HP,"です。")
    print(pl2name_l,"の属性は",player2_zokusei,"です。 HPは",player2_HP,"です。")
    print()
    time.sleep(1)
    while (player1_HP > 0) and (player2_HP > 0) :
        if d_mv1 == 0 :
            print(player1_name,"のターンです。")
            time.sleep(1)
            print(pl1name_l," HP:",player1_HP," ,TP:",player1_TP," ,所持コスト:",player1_cost)
            print(pl2name_l," HP:",player2_HP," ,TP:",player2_TP," ,所持コスト:",player2_cost)
            time.sleep(1)
            random_cost = int(rm.choice(range(1,4)))
            player1_cost = player1_cost + random_cost
            print(player1_name,"は",random_cost,"コストを手に入れ、",player1_name,"の所持コストは",player1_cost,"になりました。")
            time.sleep(1)
            random_cost = 0
            print("1.",action1,",消費コスト:",action1_cost,",獲得TP:",action1_getTP)
            print("2.",pl1action2,",消費コスト:",pl1action2_cost,",獲得TP:",pl1action2_getTP)
            print("3.",action3,",消費コスト:",action3_cost,",獲得TP:",action3_getTP)
            print("4.",pl1action4,",消費コスト:",pl1action4_cost,",消費TP:",pl1ac4cost_TP)
            pl1ac_num = 0
            while count == 0:
                time.sleep(1)
                pl1ac_num = int(input("行う行動の番号... "))
                if pl1ac_num == 1 :
                    if player1_cost >= action1_cost :
                        player1_cost = player1_cost - action1_cost
                        count = count + 1
                    else :
                        print("コストが足りません！")
                elif pl1ac_num == 2 :
                    if player1_cost >= pl1action2_cost :
                        player1_cost = player1_cost - pl1action2_cost
                        count = count + 1
                    else :
                        print("コストが足りません！")
                elif pl1ac_num == 3 :
                    count = count + 1
                elif pl1ac_num == 4 :
                    if (player1_cost >= pl1action4_cost) and (player1_TP >= pl1ac4cost_TP) :
                        player1_cost = player1_cost - action1_cost
                        player1_TP = player1_TP - pl1ac4cost_TP
                        count = count + 1
                    else :
                        print("コスト、またはTPが足りません！")
                elif ("" in pl1ac_num) or (" " in pl1ac_num):
                    print("番号を指定してください")
                else:
                    print("その番号に行動はありません！")
            count = 0
            time.sleep(1)
            if pl1ac_num == 1 :
                print()
                print(player1_name,"の通常攻撃！")
                print()
                if d_ata1 > 0:
                    if player1_zo == 4:
                        rm_num = 1
                    else:
                        rm_num = int(rm.choice(range(1,11)))
                else:
                    rm_num = 10
                if (rm_num == 9) or (rm_num == 10):
                    if player1_zo == 5 :
                        pl1action1_dam = int(rm.choice(range(40,51)))
                        if shield2_num >= 1 :
                            pl1action1_dam = int(pl1action1_dam /2)
                        if rm_num > 0 :
                            pl1action1_dam = pl1action1_dam + rm_num
                            rm_num = 0
                        atack_num = int(rm.choice(range(1,11)))
                        if 1 <= atack_num <= 4 :
                            print("会心発生！")
                            print()
                            pl1action1_dam = pl1action1_dam *2
                            print(player2_name,"に",pl1action1_dam,"ダメージ与えた！")
                        else :
                            print(player2_name,"に",pl1action1_dam,"ダメージ与えた！")
                        player2_HP = player2_HP - pl1action1_dam
                        print()
                    elif player1_zo == 7 :
                        pl1action1_dam = int(rm.choice(range(20,31)))
                        if shield2_num >= 1 :
                            pl1action1_dam = int(pl1action1_dam /2)
                        atack_num = int(rm.choice(range(1,101)))
                        if 1 <= atack_num <= 25 :
                            print("会心発生！")
                            print()
                            pl1action1_dam = pl1action1_dam *2
                            print(player2_name,"に",pl1action1_dam,"ダメージ与えた！")
                            atack1_HP = pl1action1_dam/2
                            print(player1_name,"は",atack1_HP,"回復した！")
                            player1_HP += atack1_HP
                        else :
                            print(player2_name,"に",pl1action1_dam,"ダメージ与えた！")
                            atack1_HP = pl1action1_dam/2
                            print(player1_name,"は",atack1_HP,"回復した！")
                            player1_HP += atack1_HP
                        player2_HP = player2_HP - pl1action1_dam
                        atack1_HP = 0
                        print()
                    else :
                        pl1action1_dam = int(rm.choice(range(20,31)))
                        if shield2_num >= 1 :
                            pl1action1_dam = int(pl1action1_dam /2)
                        atack_num = int(rm.choice(range(1,101)))
                        if 1 <= atack_num <= 25 :
                            print("会心発生！")
                            print()
                            pl1action1_dam = pl1action1_dam *2
                            print(player2_name,"に",pl1action1_dam,"ダメージ与えた！")
                        else :
                            print(player2_name,"に",pl1action1_dam,"ダメージ与えた！")
                        player2_HP = player2_HP - pl1action1_dam
                        print()
                    player1_TP = player1_TP + 10
                    atack_num = 0
                    kaisin_1 = 0
                    pl1action_dam = 0
                else:
                    print("しかし植物によって攻撃できなかった！")
                    print()
            elif pl1ac_num == 2 :
                if player1_zo == 1 :
                    if d_ata1 > 0:
                        if player1_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if player2_zo == 3 :
                            print()
                            print(player1_name,"の火炎放射！")
                            print("属性ダメージボーナス付与！")
                            print()
                            pl1action2_dam = 70
                            if shield2_num >= 1 :
                                pl1action2_dam = int(pl1action2_dam /2)
                            atack_num = int(rm.choice(range(1,101)))
                            if 1 <= atack_num <= 25 :
                                print("会心発生！")
                                print()
                                pl1action2_dam = pl1action2_dam *2
                                print(player2_name,"に",pl1action2_dam,"ダメージ与えた！")
                                print()
                            else :
                                print(player2_name,"に",pl1action2_dam,"ダメージ与えた！")
                                print()
                            player2_HP = player2_HP - pl1action2_dam
                        else :
                            print()
                            print(player1_name,"の火炎放射！")
                            print()
                            pl1action2_dam = 60
                            if shield2_num >= 1 :
                                pl1action2_dam = int(pl1action2_dam /2)
                            atack_num = int(rm.choice(range(1,101)))
                            if 1 <= atack_num <= 25 :
                                print("会心発生！")
                                print()
                                pl1action2_dam = pl1action2_dam *2
                                print(player2_name,"に",pl1action2_dam,"ダメージ与えた！")
                                print()
                            else :
                                print(player2_name,"に",pl1action2_dam,"ダメージ与えた！")
                                print()
                            player2_HP = player2_HP - pl1action2_dam
                            player1_TP = player1_TP + 20
                        zi_dam2 = 3
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player1_zo == 2:
                    print()
                    print(player1_name,"の回復！")
                    print()
                    player1_HP = player1_HP + 100
                    print(player1_name,"のHPが 100 回復した！")
                    print()
                    player1_TP = player1_TP + 25
                elif player1_zo == 3:
                    print()
                    print(player1_name,"の持続回復！")
                    print()
                    zi_heal1 = 3
                    player1_TP = player1_TP + 25
                elif player1_zo == 4:
                    print()
                    print(player1_name,"の冷凍保存！")
                    if d_ata1 > 0:
                        if player1_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if player2_zo == 1 :
                            print("属性ダメージボーナス付与！")
                            pl1action2_dam = int(rm.choice(range(30,51)))
                            if shield2_num >= 1 :
                                pl1action2_dam = int(pl1action2_dam /2)
                            atack_num = int(rm.choice(range(1,101)))
                            if 1 <= atack_num <= 25 :
                                print("会心発生！")
                                print()
                                pl1action2_dam = pl1action2_dam *2
                                print(player2_name,"に",pl1action2_dam,"ダメージ与えた！")
                                print()
                            else :
                                print()
                                print(player2_name,"に",pl1action2_dam,"ダメージ与えた！")
                                print()
                            player2_HP = player2_HP - pl1action2_dam
                        else:
                            if player2_zo == 2 :
                                print("属性反応ボーナス付与！")
                                d_mv2 = 2
                            pl1action2_dam = int(rm.choice(range(20,41)))
                            if shield2_num >= 1 :
                                pl1action2_dam = int(pl1action2_dam /2)
                            atack_num = int(rm.choice(range(1,101)))
                            if 1 <= atack_num <= 25 :
                                print("会心発生！")
                                print()
                                pl1action2_dam = pl1action2_dam *2
                                print(player2_name,"に",pl1action2_dam,"ダメージ与えた！")
                                print()
                            else :
                                print()
                                print(player2_name,"に",pl1action2_dam,"ダメージ与えた！")
                                print()
                            player2_HP = player2_HP - pl1action2_dam
                        player1_TP += 15
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player1_zo == 5 :
                    print()
                    print(player1_name,"の自己犠牲！")
                    rm_num = int(rm.choice(range(10,51)))
                    print(player1_name,"は自分の自分のHPを",rm_num,"削った！")
                    print()
                    player1_HP = player1_HP - rm_num
                    player1_TP += 20
                elif player1_zo == 6 :
                    print()
                    print(player1_name,"の吸収！")
                    if d_ata1 > 0:
                        if player1_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if player2_zo == 7:
                            pl1action2_dam = 75
                        else:
                            list_1 = [25 ,50 ,75]
                            pl1action2_dam = rm.choice(list_1)
                        print(player1_name,"は",player2_name,"のHPを",pl1action2_dam,"分吸収した！")
                        print()
                        if player2_cost > 0:
                            chance1_cost = rm.choice(range(1,11))
                            if (chance1_cost == 1) or (chance1_cost == 2):
                                if player2_cost == 1 :
                                    lost2_cost = 1
                                elif player2_cost == 2 :
                                    lost2_cost = 2
                                else :
                                    lost2_cost = 3
                                print(player1_name,"は",player2_name,"から",lost2_cost,"コスト奪った！")
                                print()
                                player2_cost -= lost2_cost
                                player1_cost += lost2_cost
                        player2_HP -= pl1action2_dam
                        player1_HP += pl1action2_dam
                        player1_TP += 25
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player1_zo == 7 :
                    print()
                    print(player1_name,"のヒーリング！")
                    print(player1_name,"は75回復した！")
                    print()
                    player1_HP += 75
                    player1_TP += 10
            elif pl1ac_num == 3 :
                print()
                print(player1_name,"は防御を固めた！")
                print()
                shield1_num = 1
                player1_TP += 5
            elif pl1ac_num == 4 :
                if player1_zo == 1:
                    print()
                    if d_ata1 > 0:
                        if player1_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if zi_dam2 > 0:
                            if player2_zo == 3:
                                pl1action4_dam = 175
                            else:
                                pl1action4_dam = 150
                            zi_dam2 = 0
                        else:
                            if player2_zo == 3:
                                pl1action4_dam = 125
                            else:
                                pl1action4_dam = 100
                        if shield2_num > 0:
                            pl1action4_dam = pl1action4_dam/2
                        print(player1_name,"はメラバーンを唱えた！")
                        print(player1_name,"は",player2_name,"に",pl1action4_dam,"ダメージ与えた！")
                        print()
                        player2_HP -= pl1action4_dam
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player1_zo == 2:
                    print()
                    if d_ata1 > 0:
                        if player1_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        print(player1_name,"の洪水！")
                        if player2_zo == 1:
                            print("属性ダメージボーナス付与！")
                            pl1action4_dam = 150
                            atack_num = int(rm.choice(range(1,101)))
                            if 1<= atack_num <= 25:
                                print("会心発生！")
                                pl1action4_dam = pl1action4_dam*2
                            else:
                                None
                        else:
                            pl1action4_dam = 75
                            atack_num = int(rm.choice(range(1,101)))
                            if 1<= atack_num <= 25:
                                print("会心発生！")
                                pl1action4_dam = pl1action4_dam*2
                            else:
                                None
                        if shield2_num > 0:
                            pl1action4_dam = pl1action4_dam/2
                        print(player1_name,"は",player2_name,"に",pl1action4_dam,"ダメージ与えた！")
                        player2_HP -= pl1action4_dam
                        print()
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player1_zo == 3:
                    print()
                    print(player1_name,"の草による足止め！")
                    print()
                    d_ata2 = 2
                elif player1_zo == 4:
                    print()
                    print(player1_name,"の氷の結晶！")
                    print()
                    if d_ata1 > 0:
                        if player1_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        pl1action4_dam = 200
                        if d_mv2 > 0:
                            pl1action4_dam = pl1action4_dam *2
                        if shield2_num > 0:
                            pl1action4_dam = pl1action4_dam/2
                        print(player1_name,"は",player2_name,"に",pl1action4_dam,"ダメージ与えた！")
                        print()
                        player2_HP -= pl1action4_dam
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player1_zo == 5:
                    print()
                    print(player1_name,"の微回復！")
                    bikaihuku = int(player1_TP/2)
                    x = player1_TP %2
                    player1_TP = 0
                    player1_TP += x
                    print(player1_name,"は",bikaihuku,"回復した！")
                    print()
                    player1_HP += bikaihuku
                elif player1_zo == 6:
                    print()
                    print(player1_name,"のブラックホール！")
                    print()
                    if d_ata1 > 0:
                        if player1_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if (player2_zo == 5) or (player2_zo == 7):
                            pl1action4_dam = 150
                        else:
                            pl1action4_dam = 100
                        print(player1_name,"は",player2_name,"に",pl1action4_dam,"固定ダメージ与えた！")
                        print(player1_name,"は 250 回復した！")
                        print()
                        player1_HP += 250
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player1_zo == 7:
                    print()
                    print(player1_name,"のホーリーライト！")
                    print(player1_name,"は 100 回復した！")
                    player1_HP += 100
                    print()
                    if d_ata1 > 0:
                        if player1_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if player2_zo == 6:
                            pl1action4_dam = 100
                        else:
                            pl1action4_dam = 50
                        print(player1_name,"は",player2_name,"に",pl1action4_dam,"ダメージ与えた！")
                        print()
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
        else:
            print(player1_name,"は行動できなかった！")
            print()
        time.sleep(1)
        if zi_dam1 > 0 :
            print()
            print(player1_name,"は燃焼のためため 10 ダメージ受けた！")
            print()
            player1_HP = player1_HP - 10
            zi_dam1 = zi_dam1 -1
        if zi_heal1 > 0 :
            print()
            print(player1_name,"は持続回復で回復した！")
            print()
            HP1 = int(rm.choice(range(50,101)))
            player1_HP = player1_HP + HP1
            HP1 = 0
            zi_heal1 = zi_heal1 - 1
        if zi_shield1 > 0 :
            zi_shield1 = zi_shield1 - 1
        if d_mv1 > 0 :
            d_mv1 = d_mv1 -1
        if d_ata1 > 0 :
            d_ata1 -= 1
        kaisin_1 = 0
        random_cost = 0
        pl1action2_dam = 0
        pl1action4_dam = 0
        atack_num = 0
        rm_num = 0
        bikaihuku = 0
        x = 0

        if d_mv2 == 0 :
            print(player2_name,"のターンです。")
            time.sleep(1)
            print(pl1name_l," HP:",player1_HP," ,TP:",player1_TP," ,所持コスト:",player1_cost)
            print(pl2name_l," HP:",player2_HP," ,TP:",player2_TP," ,所持コスト:",player2_cost)
            time.sleep(1)
            random_cost = int(rm.choice(range(1,4)))
            player2_cost += random_cost
            print(player2_name,"は",random_cost,"コストを手に入れ、",player2_name,"の所持コストは",player2_cost,"になりました。")
            time.sleep(1)
            random_cost = 0
            print("1.",action1,",消費コスト:",action1_cost,",獲得TP:",action1_getTP)
            print("2.",pl2action2,",消費コスト:",pl2action2_cost,",獲得TP:",pl2action2_getTP)
            print("3.",action3,",消費コスト:",action3_cost,",獲得TP:",action3_getTP)
            print("4.",pl2action4,",消費コスト:",pl2action4_cost,",消費TP:",pl2ac4cost_TP)
            pl2ac_num = 0
            while count == 0:
                time.sleep(1)
                pl2ac_num = int(input("行う行動の番号... "))
                if pl2ac_num == 1 :
                    if player2_cost >= action1_cost :
                        player2_cost = player2_cost - action1_cost
                        count = count + 1
                    else :
                        print("コストが足りません！")
                elif pl2ac_num == 2 :
                    if player2_cost >= pl2action2_cost :
                        player2_cost = player2_cost - pl2action2_cost
                        count = count + 1
                    else :
                        print("コストが足りません！")
                elif pl2ac_num == 3 :
                    count = count + 1
                elif pl2ac_num == 4 :
                    if (player2_cost >= pl2action4_cost) and (player2_TP >= pl2ac4cost_TP) :
                        player2_cost = player2_cost - action1_cost
                        player2_TP -= pl2ac4cost_TP
                        count = count + 1
                    else :
                        print("コスト、またはTPが足りません！")
                elif ("" in pl1ac_num) or (" " in pl1ac_num):
                    print("番号を指定してください")
                else:
                    print("その番号に行動はありません！")
            count = 0
            time.sleep(1)
            if pl2ac_num == 1 :
                print()
                print(player2_name,"の通常攻撃！")
                print()
                if d_ata2 > 0:
                    if player2_zo == 4:
                        rm_num = 1
                    else:
                        rm_num = int(rm.choice(range(1,11)))
                else:
                    rm_num = 10
                if (rm_num == 9) or (rm_num == 10):
                    if player2_zo == 5 :
                        pl2action1_dam = int(rm.choice(range(40,51)))
                        if shield1_num >= 1 :
                            pl2action1_dam = int(pl2action1_dam /2)
                        if rm_num > 0 :
                            pl2action1_dam = pl2action1_dam + rm_num
                            rm_num = 0
                        atack_num = int(rm.choice(range(1,11)))
                        if 1 <= atack_num <= 4 :
                            print("会心発生！")
                            print()
                            pl2action1_dam = pl2action1_dam *2
                            print(player1_name,"に",pl2action1_dam,"ダメージ与えた！")
                        else :
                            print(player1_name,"に",pl2action1_dam,"ダメージ与えた！")
                        player1_HP = player1_HP - pl2action1_dam
                        print()
                    elif player2_zo == 7 :
                        pl2action1_dam = int(rm.choice(range(20,31)))
                        if shield1_num >= 1 :
                            pl2action1_dam = int(pl2action1_dam /2)
                        atack_num = int(rm.choice(range(1,101)))
                        if 1 <= atack_num <= 25 :
                            print("会心発生！")
                            print()
                            pl2action1_dam = pl2action1_dam *2
                            print(player1_name,"に",pl2action1_dam,"ダメージ与えた！")
                            atack2_HP = pl2action1_dam/2
                            print(player2_name,"は",atack2_HP,"回復した！")
                            player2_HP += atack2_HP
                        else :
                            print(player1_name,"に",pl2action1_dam,"ダメージ与えた！")
                            atack2_HP = pl2action1_dam/2
                            print(player2_name,"は",atack2_HP,"回復した！")
                            player2_HP += atack2_HP
                        player1_HP = player1_HP - pl2action1_dam
                        atack2_HP = 0
                        print()
                    else :
                        pl2action1_dam = int(rm.choice(range(20,31)))
                        if shield1_num >= 1 :
                            pl2action1_dam = int(pl2action1_dam /2)
                        atack_num = int(rm.choice(range(1,101)))
                        if 1 <= atack_num <= 25 :
                            print("会心発生！")
                            print()
                            pl2action1_dam = pl2action1_dam *2
                            print(player1_name,"に",pl2action1_dam,"ダメージ与えた！")
                        else :
                            print(player1_name,"に",pl2action1_dam,"ダメージ与えた！")
                        player1_HP = player1_HP - pl2action1_dam
                        print()
                    player2_TP = player2_TP + 10
                    atack_num = 0
                    kaisin_1 = 0
                    pl2action_dam = 0
                else:
                    print("しかし植物によって攻撃できなかった！")
                    print()
            elif pl2ac_num == 2 :
                if player2_zo == 1 :
                    if d_ata2 > 0:
                        if player2_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if player1_zo == 3 :
                            print()
                            print(player2_name,"の火炎放射！")
                            print("属性ダメージボーナス付与！")
                            print()
                            pl2action2_dam = 70
                            if shield1_num >= 1 :
                                pl2action2_dam = int(pl2action2_dam /2)
                            atack_num = int(rm.choice(range(1,101)))
                            if 1 <= atack_num <= 25 :
                                print("会心発生！")
                                print()
                                pl2action2_dam = pl2action2_dam *2
                                print(player1_name,"に",pl2action2_dam,"ダメージ与えた！")
                                print()
                            else :
                                print(player1_name,"に",pl2action2_dam,"ダメージ与えた！")
                                print()
                            player1_HP = player1_HP - pl2action2_dam
                        else :
                            print()
                            print(player2_name,"の火炎放射！")
                            print()
                            pl2action2_dam = 60
                            if shield1_num >= 1 :
                                pl2action2_dam = int(pl2action2_dam /2)
                            atack_num = int(rm.choice(range(1,101)))
                            if 1 <= atack_num <= 25 :
                                print("会心発生！")
                                print()
                                pl2action2_dam = pl2action2_dam *2
                                print(player1_name,"に",pl2action2_dam,"ダメージ与えた！")
                                print()
                            else :
                                print(player1_name,"に",pl2action2_dam,"ダメージ与えた！")
                                print()
                            player1_HP = player1_HP - pl2action2_dam
                            player2_TP = player2_TP + 20
                        zi_dam1 = 3
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player2_zo == 2:
                    print()
                    print(player2_name,"の回復！")
                    print()
                    player2_HP = player2_HP + 100
                    print(player2_name,"のHPが 100 回復した！")
                    print()
                    player2_TP = player2_TP + 25
                elif player2_zo == 3:
                    print()
                    print(player2_name,"の持続回復！")
                    print()
                    zi_heal2 = 3
                    player2_TP = player2_TP + 25
                elif player2_zo == 4:
                    print()
                    print(player2_name,"の冷凍保存！")
                    if d_ata2 > 0:
                        if player2_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if player1_zo == 1 :
                            print("属性ダメージボーナス付与！")
                            pl2action2_dam = int(rm.choice(range(30,51)))
                            if shield1_num >= 1 :
                                pl2action2_dam = int(pl2action2_dam /2)
                            atack_num = int(rm.choice(range(1,101)))
                            if 1 <= atack_num <= 25 :
                                print("会心発生！")
                                print()
                                pl2action2_dam = pl2action2_dam *2
                                print(player1_name,"に",pl2action2_dam,"ダメージ与えた！")
                            else :
                                print()
                                print(player1_name,"に",pl2action2_dam,"ダメージ与えた！")
                            player1_HP = player1_HP - pl2action2_dam
                            print()
                        else:
                            if player1_zo == 2 :
                                print("属性反応ボーナス付与！")
                                d_mv1 = 2
                            pl2action2_dam = int(rm.choice(range(20,41)))
                            if shield1_num >= 1 :
                                pl2action2_dam = int(pl2action2_dam /2)
                            atack_num = int(rm.choice(range(1,101)))
                            if 1 <= atack_num <= 25 :
                                print("会心発生！")
                                print()
                                pl2action2_dam = pl2action2_dam *2
                                print(player1_name,"に",pl2action2_dam,"ダメージ与えた！")
                            else :
                                print()
                                print(player1_name,"に",pl2action2_dam,"ダメージ与えた！")
                            print()
                            player1_HP = player1_HP - pl2action2_dam
                        player2_TP += 15
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player2_zo == 5 :
                    print()
                    print(player2_name,"の自己犠牲！")
                    rm_num = int(rm.choice(range(10,51)))
                    print(player2_name,"は自分の自分のHPを",rm_num,"削った！")
                    print()
                    player2_HP = player2_HP - rm_num
                    player2_TP += 20
                elif player2_zo == 6 :
                    print()
                    print(player2_name,"の吸収！")
                    if d_ata2 > 0:
                        if player2_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if player1_zo == 7:
                            pl2action2_dam = 75
                        else:
                            list_2 = [25 ,50 ,75]
                            pl2action2_dam = rm.choice(list_2)
                        print(player2_name,"は",player1_name,"のHPを",pl2action2_dam,"分吸収した！")
                        print()
                        if player1_cost > 0:
                            chance2_cost = rm.choice(range(1,11))
                            if (chance2_cost == 1) or (chance2_cost == 2):
                                if player1_cost == 1 :
                                    lost1_cost = 1
                                elif player1_cost == 2 :
                                    lost1_cost = 2
                                else :
                                    lost1_cost = 3
                                print(player2_name,"は",player1_name,"から",lost1_cost,"コスト奪った！")
                                print()
                                player1_cost -= lost1_cost
                                player2_cost += lost1_cost
                        player1_HP -= pl2action2_dam
                        player2_HP += pl2action2_dam
                        player2_TP += 25
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player2_zo == 7 :
                    print()
                    print(player2_name,"のヒーリング！")
                    print(player2_name,"は75回復した！")
                    print()
                    player2_HP += 75
                    player2_TP += 10
            elif pl2ac_num == 3 :
                print()
                print(player2_name,"は防御を固めた！")
                print()
                shield2_num = 1
                player2_TP += 5
            elif pl2ac_num == 4 :
                if player2_zo == 1:
                    print()
                    if d_ata2 > 0:
                        if player2_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if zi_dam1 > 0:
                            if player1_zo == 3:
                                pl2action4_dam = 175
                            else:
                                pl2action4_dam = 150
                            zi_dam1 = 0
                        else:
                            if player1_zo == 3:
                                pl2action4_dam = 125
                            else:
                                pl2action4_dam = 100
                        if shield1_num > 0:
                            pl2action4_dam = pl2action4_dam/2
                        print(player2_name,"はメラバーンを唱えた！")
                        print(player2_name,"は",player1_name,"に",pl2action4_dam,"ダメージ与えた！")
                        print()
                        player1_HP -= pl2action4_dam
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player2_zo == 2:
                    print()
                    if d_ata2 > 0:
                        if player2_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        print(player2_name,"の洪水！")
                        if player1_zo == 1:
                            print("属性ダメージボーナス付与！")
                            pl2action4_dam = 150
                            atack_num = int(rm.choice(range(1,101)))
                            if 1<= atack_num <= 25:
                                print("会心発生！")
                                pl2action4_dam = pl2action4_dam*2
                            else:
                                None
                        else:
                            pl2action4_dam = 75
                            atack_num = int(rm.choice(range(1,101)))
                            if 1<= atack_num <= 25:
                                print("会心発生！")
                                pl2action4_dam = pl2action4_dam*2
                            else:
                                None
                        if shield1_num > 0:
                            pl2action4_dam = pl2action4_dam/2
                        print(player2_name,"は",player1_name,"に",pl2action4_dam,"ダメージ与えた！")
                        player1_HP -= pl2action4_dam
                        print()
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player2_zo == 3:
                    print()
                    print(player2_name,"の草による足止め！")
                    print()
                    d_ata1 = 2
                elif player2_zo == 4:
                    print()
                    print(player2_name,"の氷の結晶！")
                    print()
                    if d_ata2 > 0:
                        if player2_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        pl2action4_dam = 200
                        if d_mv1 > 0:
                            pl2action4_dam = pl2action4_dam *2
                        if shield1_num > 0:
                            pl2action4_dam = pl2action4_dam/2
                        print(player2_name,"は",player1_name,"に",pl2action4_dam,"ダメージ与えた！")
                        print()
                        player1_HP -= pl2action4_dam
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player2_zo == 5:
                    print()
                    print(player2_name,"の微回復！")
                    bikaihuku = int(player2_TP/2)
                    x = player2_TP %2
                    player2_TP = 0
                    player2_TP += x
                    print(player2_name,"は",bikaihuku,"回復した！")
                    print()
                    player2_HP += bikaihuku
                elif player2_zo == 6:
                    print()
                    print(player2_name,"のブラックホール！")
                    print()
                    if d_ata2 > 0:
                        if player2_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if (player1_zo == 5) or (player1_zo == 7):
                            pl2action4_dam = 150
                        else:
                            pl2action4_dam = 100
                        print(player2_name,"は",player1_name,"に",pl2action4_dam,"固定ダメージ与えた！")
                        print(player2_name,"は 250 回復した！")
                        print()
                        player2_HP += 250
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player2_zo == 7:
                    print()
                    print(player2_name,"のホーリーライト！")
                    print(player2_name,"は 100 回復した！")
                    player2_HP += 100
                    print()
                    if d_ata2 > 0:
                        if player2_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if player1_zo == 6:
                            pl2action4_dam = 100
                        else:
                            pl2action4_dam = 50
                        print(player2_name,"は",player1_name,"に",pl2action4_dam,"ダメージ与えた！")
                        print()
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
        else:
            print(player2_name,"は行動できなかった！")
            print()
        time.sleep(1)
        if zi_dam2 > 0 :
            print()
            print(player2_name,"は燃焼のためため 10 ダメージ受けた！")
            print()
            player2_HP = player2_HP - 10
            zi_dam2 = zi_dam2 -1
        if zi_heal2 > 0 :
            print()
            print(player2_name,"は持続回復で回復した！")
            HP2 = int(rm.choice(range(50,101)))
            player2_HP = player2_HP + HP2
            HP2 = 0
            zi_heal2 = zi_heal2 - 1
        if zi_shield2 > 0 :
            zi_shield2 = zi_shield2 - 1
        if d_mv2 > 0 :
            d_mv2 = d_mv2 -1
        if d_ata2 > 0 :
            d_ata2 -= 1
        kaisin_2 = 0
        pl2action2_dam = 0
        pl2action4_dam = 0
        atack_num = 0
        rm_num = 0
        bikaihuku = 0
        x = 0

    if player1_HP > 0:
        print("勝者:",player1_name)
    else:
        print("勝者:",player2_name)
if game_mode == 2:
    print("coming soon...")
if game_mode == 3:
    print()
    count_name1 = 0
    while count_name1 == 0 :
        player1_name = input("プレイヤー１の名前を入力してください。(8字以内,半角英数字)　")
        pl1name = len(player1_name)
        if pl1name > 9:
            print("8字以内で名前を決めてください。")
        else :
            break
    pl1_name = map(str,player1_name)
    pl1name_b = list(pl1_name)
    pl1name_num = 8 - pl1name
    for i in range(pl1name_num) :
        pl1name_b.append(" ")
    pl1name_l = "".join(pl1name_b)
    count_name2 = 0
    while count_name2 == 0 :
        player2_name = input("プレイヤー２の名前を入力してください。(8字以内,半角英数字)　")
        pl2name = len(player2_name)
        if pl2name > 9:
            print("8字以内で名前を決めてください。")
        else :
            break
    pl2_name = map(str,player2_name)
    pl2name_b = list(pl2_name)
    pl2name_num = 8 - pl2name
    for i in range(pl2name_num) :
        pl2name_b.append(" ")
    pl2name_l = "".join(pl2name_b)
    print()
    player1_zo = int(rm.choice(range(1,8)))
    if player1_zo == 1 :
        player1_zokusei = ("火　")
        player1_HP = 500.0
        pl1action2 = ("火炎放射　　　　")
        pl1action2_cost = 5
        pl1action2_getTP = 20
        pl1action4 = ("メラバーン　　　")
        pl1action4_cost = 3
        pl1ac4cost_TP = 100
    elif player1_zo == 2 :
        player1_zokusei = ("水　")
        player1_HP = 350.0
        pl1action2 = ("回復　　　　　　")
        pl1action2_cost = 4
        pl1action2_getTP = 25
        pl1action4 = ("洪水　　　　　　")
        pl1action4_cost = 2
        pl1ac4cost_TP = 100
    elif player1_zo == 3 :
        player1_zokusei = ("草　")
        player1_HP = 500.0
        pl1action2 = ("持続回復　　　　")
        pl1action2_cost = 3
        pl1action2_getTP = 25
        pl1action4 = ("植物による足止め")
        pl1action4_cost = 3
        pl1ac4cost_TP = 80
    elif player1_zo == 4 :
        player1_zokusei = ("氷　")
        player1_HP = 500.0
        pl1action2 = ("冷凍保存　　　　")
        pl1action2_cost = 3
        pl1action2_getTP = 15
        pl1action4 = ("氷の結晶　　　　")
        pl1action4_cost = 2
        pl1ac4cost_TP = 90
    elif player1_zo == 5 :
        player1_zokusei = ("物理")
        player1_HP = 475.0
        pl1action2 = ("自己犠牲　　　　")
        pl1action2_cost = 1
        pl1action2_getTP = 20
        pl1action4 = ("微回復　　　　　")
        pl1action4_cost = 5
        pl1ac4cost_TP = 0
    elif player1_zo == 6 :
        player1_zokusei = ("闇　")
        player1_HP = 450.0
        pl1action2 = ("吸収　　　　　　")
        pl1action2_cost = 5
        pl1action2_getTP = 25
        pl1action4 = ("ブラックホール　")
        pl1action4_cost = 7
        pl1ac4cost_TP = 100
    elif player1_zo == 7 :
        player1_zokusei = ("光　")
        player1_HP = 175.0
        pl1action2 = ("ヒーリング　　　")
        pl1action2_cost = 2
        pl1action2_getTP = 10
        pl1action4 = ("ホーリーライト　")
        pl1action4_cost = 3
        pl1ac4cost_TP = 80
    player2_zo = int(rm.choice(range(1,8)))
    if player2_zo == 1 :
        player2_zokusei = ("火　")
        player2_HP = 500.0
        pl2action2 = ("火炎放射　　　　")
        pl2action2_cost = 5
        pl2action2_getTP = 20
        pl2action4 = ("メラバーン　　　")
        pl2action4_cost = 3
        pl2ac4cost_TP = 100
    elif player2_zo == 2 :
        player2_zokusei = ("水　")
        player2_HP = 350.0
        pl2action2 = ("回復　　　　　　")
        pl2action2_cost = 4
        pl2action2_getTP = 25
        pl2action4 = ("洪水　　　　　　")
        pl2action4_cost = 2
        pl2ac4cost_TP = 100
    elif player2_zo == 3 :
        player2_zokusei = ("草　")
        player2_HP = 500.0
        pl2action2 = ("持続回復　　　　")
        pl2action2_cost = 3
        pl2action2_getTP = 25
        pl2action4 = ("植物による足止め")
        pl2action4_cost = 3
        pl2ac4cost_TP = 80
    elif player2_zo == 4 :
        player2_zokusei = ("氷　")
        player2_HP = 500.0
        pl2action2 = ("冷凍保存　　　　")
        pl2action2_cost = 3
        pl2action2_getTP = 15
        pl2action4 = ("氷の結晶　　　　")
        pl2action4_cost = 2
        pl2ac4cost_TP = 90
    elif player2_zo == 5 :
        player2_zokusei = ("物理")
        player2_HP = 475.0
        pl2action2 = ("自己犠牲　　　　")
        pl2action2_cost = 1
        pl2action2_getTP = 20
        pl2action4 = ("微回復　　　　　")
        pl2action4_cost = 5
        pl2ac4cost_TP = 0
    elif player2_zo == 6 :
        player2_zokusei = ("闇　")
        player2_HP = 450.0
        pl2action2 = ("吸収　　　　　　")
        pl2action2_cost = 5
        pl2action2_getTP = 25
        pl2action4 = ("ブラックホール　")
        pl2action4_cost = 7
        pl2ac4cost_TP = 100
    elif player2_zo == 7 :
        player2_zokusei = ("光　")
        player2_HP = 175.0
        pl2action2 = ("ヒーリング　　　")
        pl2action2_cost = 2
        pl2action2_getTP = 10
        pl2action4 = ("ホーリーライト　")
        pl2action4_cost = 3
        pl2ac4cost_TP = 80
    print(pl1name_l,"の属性は",player1_zokusei,"です。 HPは",player1_HP,"です。")
    print(pl2name_l,"の属性は",player2_zokusei,"です。 HPは",player2_HP,"です。")
    print()
    time.sleep(1)
    while (player1_HP > 0) and (player2_HP > 0) :
        if d_mv1 == 0 :
            print(player1_name,"のターンです。")
            time.sleep(1)
            print(pl1name_l," HP:",player1_HP," ,TP:",player1_TP," ,所持コスト:",player1_cost)
            print(pl2name_l," HP:",player2_HP," ,TP:",player2_TP," ,所持コスト:",player2_cost)
            time.sleep(1)
            random_cost = int(rm.choice(range(1,4)))
            player1_cost = player1_cost + random_cost
            print(player1_name,"は",random_cost,"コストを手に入れ、",player1_name,"の所持コストは",player1_cost,"になりました。")
            time.sleep(1)
            random_cost = 0
            print("1.",action1,",消費コスト:",action1_cost,",獲得TP:",action1_getTP)
            print("2.",pl1action2,",消費コスト:",pl1action2_cost,",獲得TP:",pl1action2_getTP)
            print("3.",action3,",消費コスト:",action3_cost,",獲得TP:",action3_getTP)
            print("4.",pl1action4,",消費コスト:",pl1action4_cost,",消費TP:",pl1ac4cost_TP)
            pl1ac_num = 0
            while count == 0:
                time.sleep(1)
                pl1ac_num = int(input("行う行動の番号... "))
                if pl1ac_num == 1 :
                    if player1_cost >= action1_cost :
                        player1_cost = player1_cost - action1_cost
                        count = count + 1
                    else :
                        print("コストが足りません！")
                elif pl1ac_num == 2 :
                    if player1_cost >= pl1action2_cost :
                        player1_cost = player1_cost - pl1action2_cost
                        count = count + 1
                    else :
                        print("コストが足りません！")
                elif pl1ac_num == 3 :
                    count = count + 1
                elif pl1ac_num == 4 :
                    if (player1_cost >= pl1action4_cost) and (player1_TP >= pl1ac4cost_TP) :
                        player1_cost = player1_cost - action1_cost
                        player1_TP = player1_TP - pl1ac4cost_TP
                        count = count + 1
                    else :
                        print("コスト、またはTPが足りません！")
                elif ("" in pl1ac_num) or (" " in pl1ac_num):
                    print("番号を指定してください")
                else:
                    print("その番号に行動はありません！")
            count = 0
            time.sleep(1)
            if pl1ac_num == 1 :
                print()
                print(player1_name,"の通常攻撃！")
                print()
                if d_ata1 > 0:
                    if player1_zo == 4:
                        rm_num = 1
                    else:
                        rm_num = int(rm.choice(range(1,11)))
                else:
                    rm_num = 10
                if (rm_num == 9) or (rm_num == 10):
                    if player1_zo == 5 :
                        pl1action1_dam = int(rm.choice(range(40,51)))
                        if shield2_num >= 1 :
                            pl1action1_dam = int(pl1action1_dam /2)
                        if rm_num > 0 :
                            pl1action1_dam = pl1action1_dam + rm_num
                            rm_num = 0
                        atack_num = int(rm.choice(range(1,11)))
                        if 1 <= atack_num <= 4 :
                            print("会心発生！")
                            print()
                            pl1action1_dam = pl1action1_dam *2
                            print(player2_name,"に",pl1action1_dam,"ダメージ与えた！")
                        else :
                            print(player2_name,"に",pl1action1_dam,"ダメージ与えた！")
                        player2_HP = player2_HP - pl1action1_dam
                        print()
                    elif player1_zo == 7 :
                        pl1action1_dam = int(rm.choice(range(20,31)))
                        if shield2_num >= 1 :
                            pl1action1_dam = int(pl1action1_dam /2)
                        atack_num = int(rm.choice(range(1,101)))
                        if 1 <= atack_num <= 25 :
                            print("会心発生！")
                            print()
                            pl1action1_dam = pl1action1_dam *2
                            print(player2_name,"に",pl1action1_dam,"ダメージ与えた！")
                            atack1_HP = pl1action1_dam/2
                            print(player1_name,"は",atack1_HP,"回復した！")
                            player1_HP += atack1_HP
                        else :
                            print(player2_name,"に",pl1action1_dam,"ダメージ与えた！")
                            atack1_HP = pl1action1_dam/2
                            print(player1_name,"は",atack1_HP,"回復した！")
                            player1_HP += atack1_HP
                        player2_HP = player2_HP - pl1action1_dam
                        atack1_HP = 0
                        print()
                    else :
                        pl1action1_dam = int(rm.choice(range(20,31)))
                        if shield2_num >= 1 :
                            pl1action1_dam = int(pl1action1_dam /2)
                        atack_num = int(rm.choice(range(1,101)))
                        if 1 <= atack_num <= 25 :
                            print("会心発生！")
                            print()
                            pl1action1_dam = pl1action1_dam *2
                            print(player2_name,"に",pl1action1_dam,"ダメージ与えた！")
                        else :
                            print(player2_name,"に",pl1action1_dam,"ダメージ与えた！")
                        player2_HP = player2_HP - pl1action1_dam
                        print()
                    player1_TP = player1_TP + 10
                    atack_num = 0
                    kaisin_1 = 0
                    pl1action_dam = 0
                else:
                    print("しかし植物によって攻撃できなかった！")
                    print()
            elif pl1ac_num == 2 :
                if player1_zo == 1 :
                    if d_ata1 > 0:
                        if player1_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if player2_zo == 3 :
                            print()
                            print(player1_name,"の火炎放射！")
                            print("属性ダメージボーナス付与！")
                            print()
                            pl1action2_dam = 70
                            if shield2_num >= 1 :
                                pl1action2_dam = int(pl1action2_dam /2)
                            atack_num = int(rm.choice(range(1,101)))
                            if 1 <= atack_num <= 25 :
                                print("会心発生！")
                                print()
                                pl1action2_dam = pl1action2_dam *2
                                print(player2_name,"に",pl1action2_dam,"ダメージ与えた！")
                                print()
                            else :
                                print(player2_name,"に",pl1action2_dam,"ダメージ与えた！")
                                print()
                            player2_HP = player2_HP - pl1action2_dam
                        else :
                            print()
                            print(player1_name,"の火炎放射！")
                            print()
                            pl1action2_dam = 60
                            if shield2_num >= 1 :
                                pl1action2_dam = int(pl1action2_dam /2)
                            atack_num = int(rm.choice(range(1,101)))
                            if 1 <= atack_num <= 25 :
                                print("会心発生！")
                                print()
                                pl1action2_dam = pl1action2_dam *2
                                print(player2_name,"に",pl1action2_dam,"ダメージ与えた！")
                                print()
                            else :
                                print(player2_name,"に",pl1action2_dam,"ダメージ与えた！")
                                print()
                            player2_HP = player2_HP - pl1action2_dam
                            player1_TP = player1_TP + 20
                        zi_dam2 = 3
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player1_zo == 2:
                    print()
                    print(player1_name,"の回復！")
                    print()
                    player1_HP = player1_HP + 100
                    print(player1_name,"のHPが 100 回復した！")
                    print()
                    player1_TP = player1_TP + 25
                elif player1_zo == 3:
                    print()
                    print(player1_name,"の持続回復！")
                    print()
                    zi_heal1 = 3
                    player1_TP = player1_TP + 25
                elif player1_zo == 4:
                    print()
                    print(player1_name,"の冷凍保存！")
                    if d_ata1 > 0:
                        if player1_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if player2_zo == 1 :
                            print("属性ダメージボーナス付与！")
                            pl1action2_dam = int(rm.choice(range(30,51)))
                            if shield2_num >= 1 :
                                pl1action2_dam = int(pl1action2_dam /2)
                            atack_num = int(rm.choice(range(1,101)))
                            if 1 <= atack_num <= 25 :
                                print("会心発生！")
                                print()
                                pl1action2_dam = pl1action2_dam *2
                                print(player2_name,"に",pl1action2_dam,"ダメージ与えた！")
                                print()
                            else :
                                print()
                                print(player2_name,"に",pl1action2_dam,"ダメージ与えた！")
                                print()
                            player2_HP = player2_HP - pl1action2_dam
                        else:
                            if player2_zo == 2 :
                                print("属性反応ボーナス付与！")
                                d_mv2 = 2
                            pl1action2_dam = int(rm.choice(range(20,41)))
                            if shield2_num >= 1 :
                                pl1action2_dam = int(pl1action2_dam /2)
                            atack_num = int(rm.choice(range(1,101)))
                            if 1 <= atack_num <= 25 :
                                print("会心発生！")
                                print()
                                pl1action2_dam = pl1action2_dam *2
                                print(player2_name,"に",pl1action2_dam,"ダメージ与えた！")
                                print()
                            else :
                                print()
                                print(player2_name,"に",pl1action2_dam,"ダメージ与えた！")
                                print()
                            player2_HP = player2_HP - pl1action2_dam
                        player1_TP += 15
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player1_zo == 5 :
                    print()
                    print(player1_name,"の自己犠牲！")
                    rm_num = int(rm.choice(range(10,51)))
                    print(player1_name,"は自分の自分のHPを",rm_num,"削った！")
                    print()
                    player1_HP = player1_HP - rm_num
                    player1_TP += 20
                elif player1_zo == 6 :
                    print()
                    print(player1_name,"の吸収！")
                    if d_ata1 > 0:
                        if player1_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if player2_zo == 7:
                            pl1action2_dam = 75
                        else:
                            list_1 = [25 ,50 ,75]
                            pl1action2_dam = rm.choice(list_1)
                        print(player1_name,"は",player2_name,"のHPを",pl1action2_dam,"分吸収した！")
                        print()
                        if player2_cost > 0:
                            chance1_cost = rm.choice(range(1,11))
                            if (chance1_cost == 1) or (chance1_cost == 2):
                                if player2_cost == 1 :
                                    lost2_cost = 1
                                elif player2_cost == 2 :
                                    lost2_cost = 2
                                else :
                                    lost2_cost = 3
                                print(player1_name,"は",player2_name,"から",lost2_cost,"コスト奪った！")
                                print()
                                player2_cost -= lost2_cost
                                player1_cost += lost2_cost
                        player2_HP -= pl1action2_dam
                        player1_HP += pl1action2_dam
                        player1_TP += 25
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player1_zo == 7 :
                    print()
                    print(player1_name,"のヒーリング！")
                    print(player1_name,"は75回復した！")
                    print()
                    player1_HP += 75
                    player1_TP += 10
            elif pl1ac_num == 3 :
                print()
                print(player1_name,"は防御を固めた！")
                print()
                shield1_num = 1
                player1_TP += 5
            elif pl1ac_num == 4 :
                if player1_zo == 1:
                    print()
                    if d_ata1 > 0:
                        if player1_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if zi_dam2 > 0:
                            if player2_zo == 3:
                                pl1action4_dam = 175
                            else:
                                pl1action4_dam = 150
                            zi_dam2 = 0
                        else:
                            if player2_zo == 3:
                                pl1action4_dam = 125
                            else:
                                pl1action4_dam = 100
                        if shield2_num > 0:
                            pl1action4_dam = pl1action4_dam/2
                        print(player1_name,"はメラバーンを唱えた！")
                        print(player1_name,"は",player2_name,"に",pl1action4_dam,"ダメージ与えた！")
                        print()
                        player2_HP -= pl1action4_dam
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player1_zo == 2:
                    print()
                    if d_ata1 > 0:
                        if player1_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        print(player1_name,"の洪水！")
                        if player2_zo == 1:
                            print("属性ダメージボーナス付与！")
                            pl1action4_dam = 150
                            atack_num = int(rm.choice(range(1,101)))
                            if 1<= atack_num <= 25:
                                print("会心発生！")
                                pl1action4_dam = pl1action4_dam*2
                            else:
                                None
                        else:
                            pl1action4_dam = 75
                            atack_num = int(rm.choice(range(1,101)))
                            if 1<= atack_num <= 25:
                                print("会心発生！")
                                pl1action4_dam = pl1action4_dam*2
                            else:
                                None
                        if shield2_num > 0:
                            pl1action4_dam = pl1action4_dam/2
                        print(player1_name,"は",player2_name,"に",pl1action4_dam,"ダメージ与えた！")
                        player2_HP -= pl1action4_dam
                        print()
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player1_zo == 3:
                    print()
                    print(player1_name,"の草による足止め！")
                    print()
                    d_ata2 = 2
                elif player1_zo == 4:
                    print()
                    print(player1_name,"の氷の結晶！")
                    print()
                    if d_ata1 > 0:
                        if player1_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        pl1action4_dam = 200
                        if d_mv2 > 0:
                            pl1action4_dam = pl1action4_dam *2
                        if shield2_num > 0:
                            pl1action4_dam = pl1action4_dam/2
                        print(player1_name,"は",player2_name,"に",pl1action4_dam,"ダメージ与えた！")
                        print()
                        player2_HP -= pl1action4_dam
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player1_zo == 5:
                    print()
                    print(player1_name,"の微回復！")
                    bikaihuku = int(player1_TP/2)
                    x = player1_TP %2
                    player1_TP = 0
                    player1_TP += x
                    print(player1_name,"は",bikaihuku,"回復した！")
                    print()
                    player1_HP += bikaihuku
                elif player1_zo == 6:
                    print()
                    print(player1_name,"のブラックホール！")
                    print()
                    if d_ata1 > 0:
                        if player1_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if (player2_zo == 5) or (player2_zo == 7):
                            pl1action4_dam = 150
                        else:
                            pl1action4_dam = 100
                        print(player1_name,"は",player2_name,"に",pl1action4_dam,"固定ダメージ与えた！")
                        print(player1_name,"は 250 回復した！")
                        print()
                        player1_HP += 250
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player1_zo == 7:
                    print()
                    print(player1_name,"のホーリーライト！")
                    print(player1_name,"は 100 回復した！")
                    player1_HP += 100
                    print()
                    if d_ata1 > 0:
                        if player1_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if player2_zo == 6:
                            pl1action4_dam = 100
                        else:
                            pl1action4_dam = 50
                        print(player1_name,"は",player2_name,"に",pl1action4_dam,"ダメージ与えた！")
                        print()
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
        else:
            print(player1_name,"は行動できなかった！")
            print()
        time.sleep(1)
        if zi_dam1 > 0 :
            print()
            print(player1_name,"は燃焼のためため 10 ダメージ受けた！")
            print()
            player1_HP = player1_HP - 10
            zi_dam1 = zi_dam1 -1
        if zi_heal1 > 0 :
            print()
            print(player1_name,"は持続回復で回復した！")
            print()
            HP1 = int(rm.choice(range(50,101)))
            player1_HP = player1_HP + HP1
            HP1 = 0
            zi_heal1 = zi_heal1 - 1
        if zi_shield1 > 0 :
            zi_shield1 = zi_shield1 - 1
        if d_mv1 > 0 :
            d_mv1 = d_mv1 -1
        if d_ata1 > 0 :
            d_ata1 -= 1
        kaisin_1 = 0
        random_cost = 0
        pl1action2_dam = 0
        pl1action4_dam = 0
        atack_num = 0
        rm_num = 0
        bikaihuku = 0
        x = 0

        if d_mv2 == 0 :
            print(player2_name,"のターンです。")
            time.sleep(1)
            print(pl1name_l," HP:",player1_HP," ,TP:",player1_TP," ,所持コスト:",player1_cost)
            print(pl2name_l," HP:",player2_HP," ,TP:",player2_TP," ,所持コスト:",player2_cost)
            time.sleep(1)
            random_cost = int(rm.choice(range(1,4)))
            player2_cost += random_cost
            print(player2_name,"は",random_cost,"コストを手に入れ、",player2_name,"の所持コストは",player2_cost,"になりました。")
            time.sleep(1)
            random_cost = 0
            print("1.",action1,",消費コスト:",action1_cost,",獲得TP:",action1_getTP)
            print("2.",pl2action2,",消費コスト:",pl2action2_cost,",獲得TP:",pl2action2_getTP)
            print("3.",action3,",消費コスト:",action3_cost,",獲得TP:",action3_getTP)
            print("4.",pl2action4,",消費コスト:",pl2action4_cost,",消費TP:",pl2ac4cost_TP)
            pl2ac_num = 0
            while count == 0:
                time.sleep(1)
                pl2ac_num = int(input("行う行動の番号... "))
                if pl2ac_num == 1 :
                    if player2_cost >= action1_cost :
                        player2_cost = player2_cost - action1_cost
                        count = count + 1
                    else :
                        print("コストが足りません！")
                elif pl2ac_num == 2 :
                    if player2_cost >= pl2action2_cost :
                        player2_cost = player2_cost - pl2action2_cost
                        count = count + 1
                    else :
                        print("コストが足りません！")
                elif pl2ac_num == 3 :
                    count = count + 1
                elif pl2ac_num == 4 :
                    if (player2_cost >= pl2action4_cost) and (player2_TP >= pl2ac4cost_TP) :
                        player2_cost = player2_cost - action1_cost
                        player2_TP -= pl2ac4cost_TP
                        count = count + 1
                    else :
                        print("コスト、またはTPが足りません！")
                elif ("" in pl1ac_num) or (" " in pl1ac_num):
                    print("番号を指定してください")
                else:
                    print("その番号に行動はありません！")
            count = 0
            time.sleep(1)
            if pl2ac_num == 1 :
                print()
                print(player2_name,"の通常攻撃！")
                print()
                if d_ata2 > 0:
                    if player2_zo == 4:
                        rm_num = 1
                    else:
                        rm_num = int(rm.choice(range(1,11)))
                else:
                    rm_num = 10
                if (rm_num == 9) or (rm_num == 10):
                    if player2_zo == 5 :
                        pl2action1_dam = int(rm.choice(range(40,51)))
                        if shield1_num >= 1 :
                            pl2action1_dam = int(pl2action1_dam /2)
                        if rm_num > 0 :
                            pl2action1_dam = pl2action1_dam + rm_num
                            rm_num = 0
                        atack_num = int(rm.choice(range(1,11)))
                        if 1 <= atack_num <= 4 :
                            print("会心発生！")
                            print()
                            pl2action1_dam = pl2action1_dam *2
                            print(player1_name,"に",pl2action1_dam,"ダメージ与えた！")
                        else :
                            print(player1_name,"に",pl2action1_dam,"ダメージ与えた！")
                        player1_HP = player1_HP - pl2action1_dam
                        print()
                    elif player2_zo == 7 :
                        pl2action1_dam = int(rm.choice(range(20,31)))
                        if shield1_num >= 1 :
                            pl2action1_dam = int(pl2action1_dam /2)
                        atack_num = int(rm.choice(range(1,101)))
                        if 1 <= atack_num <= 25 :
                            print("会心発生！")
                            print()
                            pl2action1_dam = pl2action1_dam *2
                            print(player1_name,"に",pl2action1_dam,"ダメージ与えた！")
                            atack2_HP = pl2action1_dam/2
                            print(player2_name,"は",atack2_HP,"回復した！")
                            player2_HP += atack2_HP
                        else :
                            print(player1_name,"に",pl2action1_dam,"ダメージ与えた！")
                            atack2_HP = pl2action1_dam/2
                            print(player2_name,"は",atack2_HP,"回復した！")
                            player2_HP += atack2_HP
                        player1_HP = player1_HP - pl2action1_dam
                        atack2_HP = 0
                        print()
                    else :
                        pl2action1_dam = int(rm.choice(range(20,31)))
                        if shield1_num >= 1 :
                            pl2action1_dam = int(pl2action1_dam /2)
                        atack_num = int(rm.choice(range(1,101)))
                        if 1 <= atack_num <= 25 :
                            print("会心発生！")
                            print()
                            pl2action1_dam = pl2action1_dam *2
                            print(player1_name,"に",pl2action1_dam,"ダメージ与えた！")
                        else :
                            print(player1_name,"に",pl2action1_dam,"ダメージ与えた！")
                        player1_HP = player1_HP - pl2action1_dam
                        print()
                    player2_TP = player2_TP + 10
                    atack_num = 0
                    kaisin_1 = 0
                    pl2action_dam = 0
                else:
                    print("しかし植物によって攻撃できなかった！")
                    print()
            elif pl2ac_num == 2 :
                if player2_zo == 1 :
                    if d_ata2 > 0:
                        if player2_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if player1_zo == 3 :
                            print()
                            print(player2_name,"の火炎放射！")
                            print("属性ダメージボーナス付与！")
                            print()
                            pl2action2_dam = 70
                            if shield1_num >= 1 :
                                pl2action2_dam = int(pl2action2_dam /2)
                            atack_num = int(rm.choice(range(1,101)))
                            if 1 <= atack_num <= 25 :
                                print("会心発生！")
                                print()
                                pl2action2_dam = pl2action2_dam *2
                                print(player1_name,"に",pl2action2_dam,"ダメージ与えた！")
                                print()
                            else :
                                print(player1_name,"に",pl2action2_dam,"ダメージ与えた！")
                                print()
                            player1_HP = player1_HP - pl2action2_dam
                        else :
                            print()
                            print(player2_name,"の火炎放射！")
                            print()
                            pl2action2_dam = 60
                            if shield1_num >= 1 :
                                pl2action2_dam = int(pl2action2_dam /2)
                            atack_num = int(rm.choice(range(1,101)))
                            if 1 <= atack_num <= 25 :
                                print("会心発生！")
                                print()
                                pl2action2_dam = pl2action2_dam *2
                                print(player1_name,"に",pl2action2_dam,"ダメージ与えた！")
                                print()
                            else :
                                print(player1_name,"に",pl2action2_dam,"ダメージ与えた！")
                                print()
                            player1_HP = player1_HP - pl2action2_dam
                            player2_TP = player2_TP + 20
                        zi_dam1 = 3
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player2_zo == 2:
                    print()
                    print(player2_name,"の回復！")
                    print()
                    player2_HP = player2_HP + 100
                    print(player2_name,"のHPが 100 回復した！")
                    print()
                    player2_TP = player2_TP + 25
                elif player2_zo == 3:
                    print()
                    print(player2_name,"の持続回復！")
                    print()
                    zi_heal2 = 3
                    player2_TP = player2_TP + 25
                elif player2_zo == 4:
                    print()
                    print(player2_name,"の冷凍保存！")
                    if d_ata2 > 0:
                        if player2_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if player1_zo == 1 :
                            print("属性ダメージボーナス付与！")
                            pl2action2_dam = int(rm.choice(range(30,51)))
                            if shield1_num >= 1 :
                                pl2action2_dam = int(pl2action2_dam /2)
                            atack_num = int(rm.choice(range(1,101)))
                            if 1 <= atack_num <= 25 :
                                print("会心発生！")
                                print()
                                pl2action2_dam = pl2action2_dam *2
                                print(player1_name,"に",pl2action2_dam,"ダメージ与えた！")
                            else :
                                print()
                                print(player1_name,"に",pl2action2_dam,"ダメージ与えた！")
                            player1_HP = player1_HP - pl2action2_dam
                            print()
                        else:
                            if player1_zo == 2 :
                                print("属性反応ボーナス付与！")
                                d_mv1 = 2
                            pl2action2_dam = int(rm.choice(range(20,41)))
                            if shield1_num >= 1 :
                                pl2action2_dam = int(pl2action2_dam /2)
                            atack_num = int(rm.choice(range(1,101)))
                            if 1 <= atack_num <= 25 :
                                print("会心発生！")
                                print()
                                pl2action2_dam = pl2action2_dam *2
                                print(player1_name,"に",pl2action2_dam,"ダメージ与えた！")
                            else :
                                print()
                                print(player1_name,"に",pl2action2_dam,"ダメージ与えた！")
                            print()
                            player1_HP = player1_HP - pl2action2_dam
                        player2_TP += 15
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player2_zo == 5 :
                    print()
                    print(player2_name,"の自己犠牲！")
                    rm_num = int(rm.choice(range(10,51)))
                    print(player2_name,"は自分の自分のHPを",rm_num,"削った！")
                    print()
                    player2_HP = player2_HP - rm_num
                    player2_TP += 20
                elif player2_zo == 6 :
                    print()
                    print(player2_name,"の吸収！")
                    if d_ata2 > 0:
                        if player2_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if player1_zo == 7:
                            pl2action2_dam = 75
                        else:
                            list_2 = [25 ,50 ,75]
                            pl2action2_dam = rm.choice(list_2)
                        print(player2_name,"は",player1_name,"のHPを",pl2action2_dam,"分吸収した！")
                        print()
                        if player1_cost > 0:
                            chance2_cost = rm.choice(range(1,11))
                            if (chance2_cost == 1) or (chance2_cost == 2):
                                if player1_cost == 1 :
                                    lost1_cost = 1
                                elif player1_cost == 2 :
                                    lost1_cost = 2
                                else :
                                    lost1_cost = 3
                                print(player2_name,"は",player1_name,"から",lost1_cost,"コスト奪った！")
                                print()
                                player1_cost -= lost1_cost
                                player2_cost += lost1_cost
                        player1_HP -= pl2action2_dam
                        player2_HP += pl2action2_dam
                        player2_TP += 25
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player2_zo == 7 :
                    print()
                    print(player2_name,"のヒーリング！")
                    print(player2_name,"は75回復した！")
                    print()
                    player2_HP += 75
                    player2_TP += 10
            elif pl2ac_num == 3 :
                print()
                print(player2_name,"は防御を固めた！")
                print()
                shield2_num = 1
                player2_TP += 5
            elif pl2ac_num == 4 :
                if player2_zo == 1:
                    print()
                    if d_ata2 > 0:
                        if player2_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if zi_dam1 > 0:
                            if player1_zo == 3:
                                pl2action4_dam = 175
                            else:
                                pl2action4_dam = 150
                            zi_dam1 = 0
                        else:
                            if player1_zo == 3:
                                pl2action4_dam = 125
                            else:
                                pl2action4_dam = 100
                        if shield1_num > 0:
                            pl2action4_dam = pl2action4_dam/2
                        print(player2_name,"はメラバーンを唱えた！")
                        print(player2_name,"は",player1_name,"に",pl2action4_dam,"ダメージ与えた！")
                        print()
                        player1_HP -= pl2action4_dam
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player2_zo == 2:
                    print()
                    if d_ata2 > 0:
                        if player2_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        print(player2_name,"の洪水！")
                        if player1_zo == 1:
                            print("属性ダメージボーナス付与！")
                            pl2action4_dam = 150
                            atack_num = int(rm.choice(range(1,101)))
                            if 1<= atack_num <= 25:
                                print("会心発生！")
                                pl2action4_dam = pl2action4_dam*2
                            else:
                                None
                        else:
                            pl2action4_dam = 75
                            atack_num = int(rm.choice(range(1,101)))
                            if 1<= atack_num <= 25:
                                print("会心発生！")
                                pl2action4_dam = pl2action4_dam*2
                            else:
                                None
                        if shield1_num > 0:
                            pl2action4_dam = pl2action4_dam/2
                        print(player2_name,"は",player1_name,"に",pl2action4_dam,"ダメージ与えた！")
                        player1_HP -= pl2action4_dam
                        print()
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player2_zo == 3:
                    print()
                    print(player2_name,"の草による足止め！")
                    print()
                    d_ata1 = 2
                elif player2_zo == 4:
                    print()
                    print(player2_name,"の氷の結晶！")
                    print()
                    if d_ata2 > 0:
                        if player2_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        pl2action4_dam = 200
                        if d_mv1 > 0:
                            pl2action4_dam = pl2action4_dam *2
                        if shield1_num > 0:
                            pl2action4_dam = pl2action4_dam/2
                        print(player2_name,"は",player1_name,"に",pl2action4_dam,"ダメージ与えた！")
                        print()
                        player1_HP -= pl2action4_dam
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player2_zo == 5:
                    print()
                    print(player2_name,"の微回復！")
                    bikaihuku = int(player2_TP/2)
                    x = player2_TP %2
                    player2_TP = 0
                    player2_TP += x
                    print(player2_name,"は",bikaihuku,"回復した！")
                    print()
                    player2_HP += bikaihuku
                elif player2_zo == 6:
                    print()
                    print(player2_name,"のブラックホール！")
                    print()
                    if d_ata2 > 0:
                        if player2_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if (player1_zo == 5) or (player1_zo == 7):
                            pl2action4_dam = 150
                        else:
                            pl2action4_dam = 100
                        print(player2_name,"は",player1_name,"に",pl2action4_dam,"固定ダメージ与えた！")
                        print(player2_name,"は 250 回復した！")
                        print()
                        player2_HP += 250
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
                elif player2_zo == 7:
                    print()
                    print(player2_name,"のホーリーライト！")
                    print(player2_name,"は 100 回復した！")
                    player2_HP += 100
                    print()
                    if d_ata2 > 0:
                        if player2_zo == 4:
                            rm_num = 1
                        else:
                            rm_num = int(rm.choice(range(1,11)))
                    else:
                        rm_num = 10
                    if 9<= rm_num <= 10:
                        if player1_zo == 6:
                            pl2action4_dam = 100
                        else:
                            pl2action4_dam = 50
                        print(player2_name,"は",player1_name,"に",pl2action4_dam,"ダメージ与えた！")
                        print()
                    else:
                        print("しかし植物によって攻撃できなかった！")
                        print()
        else:
            print(player2_name,"は行動できなかった！")
            print()
        time.sleep(1)
        if zi_dam2 > 0 :
            print()
            print(player2_name,"は燃焼のためため 10 ダメージ受けた！")
            print()
            player2_HP = player2_HP - 10
            zi_dam2 = zi_dam2 -1
        if zi_heal2 > 0 :
            print()
            print(player2_name,"は持続回復で回復した！")
            HP2 = int(rm.choice(range(50,101)))
            player2_HP = player2_HP + HP2
            HP2 = 0
            zi_heal2 = zi_heal2 - 1
        if zi_shield2 > 0 :
            zi_shield2 = zi_shield2 - 1
        if d_mv2 > 0 :
            d_mv2 = d_mv2 -1
        if d_ata2 > 0 :
            d_ata2 -= 1
        kaisin_2 = 0
        pl2action2_dam = 0
        pl2action4_dam = 0
        atack_num = 0
        rm_num = 0
        bikaihuku = 0
        x = 0

    if player1_HP > 0:
        print("勝者:",player1_name)
    else:
        print("勝者:",player2_name)
