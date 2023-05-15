import random

i_table = [['CSK', 0, 0, 0, 0], ['DC', 0, 0, 0, 0], ['GT', 0, 0, 0, 0], ['KKR', 0, 0, 0, 0], ['LSG', 0, 0, 0, 0],
           ['MI', 0, 0, 0, 0], ['PBKS', 0, 0, 0, 0], ['RCB', 0, 0, 0, 0], ['RR', 0, 0, 0, 0], ['SRH', 0, 0, 0, 0]]
i = 1
fixtures = [[1, 'CSK', 'GT'], [2, 'PBKS', 'KKR'], [3, 'LSG', 'DC'], [4, 'SRH', 'RR'], [5, 'RCB', 'MI'],
            [6, 'CSK', 'LSG'], [7, 'DC', 'GT'], [8, 'RR', 'PBKS'], [9, 'KKR', 'RCB'], [10, 'LSG', 'SRH'],
            [11, 'RR', 'DC'], [12, 'MI', 'CSK'], [13, 'GT', 'KKR'], [14, 'SRH', 'PBKS'], [15, 'RCB', 'LSG'],
            [16, 'DC', 'MI'], [17, 'CSK', 'RR'], [18, 'PBKS', 'GT'], [19, 'KKR', 'SRH'], [20, 'RCB', 'DC'],
            [21, 'LSG', 'PBKS'], [22, 'MI', 'KKR'], [23, 'GT', 'RR'], [24, 'RCB', 'CSK'], [25, 'SRH', 'MI'],
            [26, 'RR', 'LSG'], [27, 'PBKS', 'RCB'], [28, 'DC', 'KKR'], [29, 'CSK', 'SRH'], [30, 'LSG', 'GT'],
            [31, 'MI', 'PBKS'], [32, 'RCB', 'RR'], [33, 'KKR', 'CSK'], [34, 'SRH', 'DC'], [35, 'GT', 'MI'],
            [36, 'RCB', 'KKR'], [37, 'RR', 'CSK'], [38, 'PBKS', 'LSG'], [39, 'KKR', 'GT'], [40, 'DC', 'SRH'],
            [41, 'CSK', 'PBKS'], [42, 'MI', 'RR'], [43, 'LSG', 'RCB'], [44, 'GT', 'DC'], [45, 'PBKS', 'MI'],
            [46, 'LSG', 'CSK'], [47, 'SRH', 'KKR'], [48, 'RR', 'GT'], [49, 'CSK', 'MI'], [50, 'DC', 'RCB'],
            [51, 'GT', 'LSG'], [52, 'RR', 'SRH'], [53, 'KKR', 'PBKS'], [54, 'MI', 'RCB'], [55, 'CSK', 'DC'],
            [56, 'KKR', 'RR'], [57, 'MI', 'GT'], [58, 'SRH', 'LSG'], [59, 'DC', 'PBKS'], [60, 'RR', 'RCB'],
            [61, 'CSK', 'KKR'], [62, 'GT', 'SRH'], [63, 'LSG', 'MI'], [64, 'PBKS', 'DC'], [65, 'SRH', 'RCB'],
            [66, 'PBKS', 'RR'], [67, 'DC', 'CSK'], [68, 'KKR', 'LSG'], [69, 'MI', 'SRH'], [70, 'RCB', 'GT']]
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
        table[0][2] = 7.5
        table[0][3] = 5.5
        table[0][4] = 0.381
        # dc
        table[1][1] = 12
        table[1][2] = 4
        table[1][3] = 8
        table[1][4] = -0.686
        # gt
        table[2][1] = 13
        table[2][2] = 8
        table[2][3] = 5
        table[2][4] = 0.761
        # kkr
        table[3][1] = 13
        table[3][2] = 6
        table[3][3] = 7
        table[3][4] = -0.256
        # lsg
        table[4][1] = 12
        table[4][2] = 6.5
        table[4][3] = 5.5
        table[4][4] = 0.309
        # mi
        table[5][1] = 12
        table[5][2] = 7
        table[5][3] = 5
        table[5][4] = -0.117
        # pbks
        table[6][1] = 12
        table[6][2] = 6
        table[6][3] = 6
        table[6][4] = -0.268
        # rcb
        table[7][1] = 12
        table[7][2] = 6
        table[7][3] = 6
        table[7][4] = 0.166
        # rr
        table[8][1] = 13
        table[8][2] = 6
        table[8][3] = 7
        table[8][4] = 0.140
        # srh
        table[9][1] = 12
        table[9][2] = 5
        table[9][3] = 7
        table[9][4] = -0.471
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
    sum+=final_result[te][1]
print(sum)
sumz=0
sum-=400
for te in range(len(final_result)):
    print(str(final_result[te][0])+ "--->" +str(round(final_result[te][1]*(1-sum/400),2)) + "----" + str(final_result[te][2]))
    sumz+=final_result[te][1]*(1-sum/400)
print(sumz)
# for x in range(len(result)):
#     if(result[x]<=result[-1]+(result[-1]*0.005)) and (result[x]>=result[-1]-(result[-1]*0.005)) :
#         print(x)
