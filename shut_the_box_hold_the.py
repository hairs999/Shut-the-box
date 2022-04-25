#Preferences larger numbers first, but hold the blank

import shut_the_box as stb

def shut_the_box(hold):
    box=[None, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
    possibilities= {1: [(1,)], 2: [(2,)], 3: [(1, 2), (3,)], 4: [(1, 3), (4,)], 5: [(2, 3), (1, 4), (5,)],
                    6: [(1, 2, 3), (2, 4), (1, 5), (6,)], 7: [(1, 2, 4), (3, 4), (2, 5), (1, 6), (7,)],
                    8: [(1, 3, 4), (1, 2, 5), (3, 5), (2, 6), (1, 7), (8,)],
                    9: [(2, 3, 4), (1, 3, 5), (4, 5), (1, 2, 6), (3, 6), (2, 7), (1, 8), (9,)],
                    10: [(1, 2, 3, 4), (2, 3, 5), (1, 4, 5), (1, 3, 6), (4, 6), (1, 2, 7), (3, 7), (2, 8), (1, 9)],
                    11: [(1, 2, 3, 5), (2, 4, 5), (2, 3, 6), (1, 4, 6), (5, 6), (1, 3, 7), (4, 7), (1, 2, 8), (3, 8), (2, 9)],
                    12: [(3, 4, 5), (1, 2, 3, 6), (2, 4, 6), (1, 5, 6), (2, 3, 7), (1, 4, 7), (5, 7), (1, 3, 8), (4, 8), (1, 2, 9), (3, 9)]}
    number_of_dice=2
    holding=True
    while box[1:]!=[0]*9:
        number=stb.dice_roll(number_of_dice)
        poss=possibilities[number]
        new_poss=[]
        for i in range(len(poss)):
            for j in range(len(poss[i])):
                if box[poss[i][j]]==0:
                    break
                elif j==len(poss[i])-1:
                    new_poss.append(poss[i])
        if len(new_poss)==0:
            return False
        box_nums=()
        if holding: 
            for k in range(len(new_poss)-1, -1, -1):
                for l in range(len(new_poss[k])):
                    if new_poss[k][l]==hold:
                        break
                    elif l==len(new_poss[k])-1:
                        box_nums=new_poss[k]
                if len(box_nums)!=0:
                    break
            if len(box_nums)==0:
                holding=False
                box_nums=new_poss[-1]
        else:
            box_nums=new_poss[-1]
        for i in box_nums:
            box[i]=0
        if box[4:]==[0]*6:
            number_of_dice=1
    return True

def probability_of_winning(number_of_games, game, hold):
    truth=0
    for i in range(number_of_games):
        if game(hold)==True:
            truth+=1
    return truth/number_of_games*100

if __name__=='__main__':
    number_of_games=1000000
    for hold in range(1, 10):
        print(hold, ': ', probability_of_winning(number_of_games, shut_the_box, hold), '%')