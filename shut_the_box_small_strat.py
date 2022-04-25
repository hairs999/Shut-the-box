#Preferences smaller numbers first

import shut_the_box as stb

def shut_the_box():
    box=[None, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
    possibilities= {1: [(1,)], 2: [(2,)], 3: [(1, 2), (3,)], 4: [(1, 3), (4,)], 5: [(2, 3), (1, 4), (5,)],
                    6: [(1, 2, 3), (2, 4), (1, 5), (6,)], 7: [(1, 2, 4), (3, 4), (2, 5), (1, 6), (7,)],
                    8: [(1, 3, 4), (1, 2, 5), (3, 5), (2, 6), (1, 7), (8,)],
                    9: [(2, 3, 4), (1, 3, 5), (4, 5), (1, 2, 6), (3, 6), (2, 7), (1, 8), (9,)],
                    10: [(1, 2, 3, 4), (2, 3, 5), (1, 4, 5), (1, 3, 6), (4, 6), (1, 2, 7), (3, 7), (2, 8), (1, 9)],
                    11: [(1, 2, 3, 5), (2, 4, 5), (2, 3, 6), (1, 4, 6), (5, 6), (1, 3, 7), (4, 7), (1, 2, 8), (3, 8), (2, 9)],
                    12: [(3, 4, 5), (1, 2, 3, 6), (2, 4, 6), (1, 5, 6), (2, 3, 7), (1, 4, 7), (5, 7), (1, 3, 8), (4, 8), (1, 2, 9), (3, 9)]}
    number_of_dice=2
    while box[1:]!=[0]*9:
        number=stb.dice_roll(number_of_dice)
        poss=possibilities[number]
        box_nums=()
        for i in range(len(poss)):
            if len(box_nums)>0:
                break
            for j in range(len(poss[i])):
                if box[poss[i][j]]==0:
                    break
                elif j==len(poss[i])-1:
                    box_nums=poss[i]
        if len(box_nums)==0:
            return False
        for i in box_nums:
            box[i]=0
        if box[4:]==[0]*6:
            number_of_dice=1
    return True

if __name__=='__main__':
    number_of_games=1000000
    print(stb.probability_of_winning(number_of_games, shut_the_box), '%')