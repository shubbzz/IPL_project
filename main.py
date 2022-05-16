import random

i_table = [['CSK', 0, 0, 0, 0], ['DC', 0, 0, 0, 0], ['GT', 0, 0, 0, 0], ['KKR', 0, 0, 0, 0], ['LSG', 0, 0, 0, 0],
           ['MI', 0, 0, 0, 0], ['PBKS', 0, 0, 0, 0], ['RCB', 0, 0, 0, 0], ['RR', 0, 0, 0, 0], ['SRH', 0, 0, 0, 0]]
i = 1
fixtures = [[1, 'CSK', 'KKR'], [2, 'DC', 'MI'], [3, 'PBKS', 'RCB'], [4, 'GT', 'LSG'], [5, 'SRH', 'RR'],
            [6, 'RCB', 'KKR'], [7, 'CSK', 'LSG'], [8, 'KKR', 'PBKS'], [9, 'MI', 'RR'], [10, 'GT', 'DC'],
            [11, 'CSK', 'PBKS'], [12, 'SRH', 'LSG'], [13, 'RCB', 'RR'], [14, 'KKR', 'MI'], [15, 'DC', 'LSG'],
            [16, 'PBKS', 'GT'], [17, 'CSK', 'SRH'], [18, 'RCB', 'MI'], [19, 'DC', 'KKR'], [20, 'RR', 'LSG'],
            [21, 'GT', 'SRH'], [22, 'CSK', 'RCB'], [23, 'PBKS', 'MI'], [24, 'RR', 'GT'], [25, 'KKR', 'SRH'],
            [26, 'MI', 'LSG'], [27, 'RCB', 'DC'], [28, 'PBKS', 'SRH'], [29, 'CSK', 'GT'], [30, 'RR', 'KKR'],
            [31, 'RCB', 'LSG'], [32, 'DC', 'PBKS'], [33, 'CSK', 'MI'], [34, 'DC', 'RR'], [35, 'GT', 'KKR'],
            [36, 'RCB', 'SRH'], [37, 'MI', 'LSG'], [38, 'PBKS', 'CSK'], [39, 'RR', 'RCB'], [40, 'GT', 'SRH'],
            [41, 'KKR', 'DC'], [42, 'PBKS', 'LSG'], [43, 'RCB', 'GT'], [44, 'RR', 'MI'], [45, 'LSG', 'DC'],
            [46, 'SRH', 'CSK'], [47, 'RR', 'KKR'], [48, 'GT', 'PBKS'], [49, 'CSK', 'RCB'], [50, 'DC', 'SRH'],
            [51, 'MI', 'GT'], [52, 'PBKS', 'RR'], [53, 'KKR', 'LSG'], [54, 'SRH', 'RCB'], [55, 'DC', 'CSK'],
            [56, 'MI', 'KKR'], [57, 'GT', 'LSG'], [58, 'RR', 'DC'], [59, 'MI', 'CSK'], [60, 'RCB', 'PBKS'],
            [61, 'SRH', 'KKR'], [62, 'CSK', 'GT'], [63, 'RR', 'LSG'], [64, 'PBKS', 'DC'], [65, 'SRH', 'MI'],
            [66, 'KKR', 'LSG'], [67, 'GT', 'RCB'], [68, 'RR', 'CSK'], [69, 'DC', 'MI'], [70, 'SRH', 'PBKS']]
final_result = [['CSK', 0], ['DC', 0], ['GT', 0], ['KKR', 0], ['LSG', 0],
           ['MI', 0], ['PBKS', 0], ['RCB', 0], ['RR', 0], ['SRH', 0]]
for te in range(len(final_result)):
    team=final_result[te][0]
    pos = list()
    pos_adv = list()
    present = 2
    count = 0
    result = list()
    iterr = 200000
    for x in range(0, iterr):
        table = list(i_table)
        # csk
        table[0][1] = 13
        table[0][2] = 4
        table[0][3] = 9
        table[0][4] = -0.206
        # dc
        table[1][1] = 12
        table[1][2] = 6
        table[1][3] = 6
        table[1][4] = 0.210
        # gt
        table[2][1] = 13
        table[2][2] = 10
        table[2][3] = 3
        table[2][4] = 0.391
        # kkr
        table[3][1] = 13
        table[3][2] = 6
        table[3][3] = 7
        table[3][4] = 0.160
        # lsg
        table[4][1] = 13
        table[4][2] = 8
        table[4][3] = 5
        table[4][4] = 0.262
        # mi
        table[5][1] = 12
        table[5][2] = 3
        table[5][3] = 9
        table[5][4] = -0.613
        # pbks
        table[6][1] = 12
        table[6][2] = 6
        table[6][3] = 6
        table[6][4] = 0.023
        # rcb
        table[7][1] = 13
        table[7][2] = 7
        table[7][3] = 6
        table[7][4] = -0.323
        # rr
        table[8][1] = 13
        table[8][2] = 8
        table[8][3] = 5
        table[8][4] = 0.304
        # srh
        table[9][1] = 12
        table[9][2] = 5
        table[9][3] = 7
        table[9][4] = -0.270
        cm = 0
        for inn in range(len(table)):
            cm += int(table[inn][1])
        cm = cm // 2
        cm -= 1
        i = cm
        while i < 69:
            i += 1
            win = random.randint(1, 2)
            winner = fixtures[i][win]
            if win == 2:
                looser = fixtures[i][1]
            else:
                looser = fixtures[i][2]
            for y in range(len(table)):
                nrr = round(random.uniform(0, 1), 2)
                if table[y][0] == winner:
                    table[y][1] += 1
                    table[y][2] += 1
                    table[y][4] += nrr
                    table[y][4] = round(table[y][4], 2)
                if table[y][0] == looser:
                    table[y][1] += 1
                    table[y][3] += 1
                    table[y][4] -= nrr
                    table[y][4] = round(table[y][4], 2)
        table.clear()
        new_table = i_table
        i_table.sort(reverse=True, key=lambda vv: (vv[2], vv[4]))
        for kk in range(len(i_table)):
            if i_table[kk][0] == team:
                if kk < 4:
                    pos.append(int(1))
                    if(kk<2):pos_adv.append(float(0.375))
                    else:pos_adv.append(float(0.25))
                else:
                    pos.append(int(0))
                    pos_adv.append(float(0))
        i_table.sort(key=lambda vv: vv[0])
        curr = sum(pos) / len(pos)
        curr_adv = sum(pos_adv)/len(pos_adv)
        # print(round(curr, 3))
        if present + (present * 0.01) >= round(curr, 3) >= present - (present * 0.01):
            count += 1
        else:
            count = 1
            present = curr
        if count == 10000:
            print("--------------------------------------->", count)
            print(x)
            final_result[te][1]=round(curr*100,1)
            final_result[te].append(round(curr_adv * 100, 1))
            break
final_result.sort(reverse=True,key=lambda vv: vv[1])
sum=0
for te in range(len(final_result)):
    print(str(final_result[te][0])+ "--->" +str(final_result[te][1]) + "----" + str(final_result[te][2]))
    sum+=final_result[te][1]
print(sum)
# for x in range(len(result)):
#     if(result[x]<=result[-1]+(result[-1]*0.005)) and (result[x]>=result[-1]-(result[-1]*0.005)) :
#         print(x)
