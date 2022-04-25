import random

def dice_roll(die_number):
    res=0
    for _ in range(die_number):
        res+=random.randint(1, 6)
    return res


def shut_the_box():
    box=[None, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    possibilities= {1: [(1,)], 2: [(2,)], 3: [(1, 2), (3,)], 4: [(1, 3), (4,)], 5: [(1, 4), (2, 3), (5,)],
                    6: [(1, 2, 3), (1, 5), (2, 4), (6,)], 7: [(1, 2, 4), (1, 6), (2, 5), (3, 4), (7,)],
                    8: [(1, 3, 4), (1, 2, 5), (1, 7), (2, 6), (3, 5), (8,)],
                    9: [(1, 2, 6), (1, 3, 5), (2, 3, 4), (1, 8), (2, 7), (3, 6), (4, 5), (9,)],
                    10: [(1, 2, 3, 4), (1, 2, 7), (1, 3, 6), (1, 4, 5), (2, 3, 5), (1, 9), (2, 8), (3, 7), (4, 6)],
                    11: [(1, 2, 3, 5), (1, 2, 8), (1, 3, 7), (1, 4, 6), (2, 3, 6), (2, 4, 5), (2, 9), (3, 8), (4, 7), (5, 6)],
                    12: [(1, 2, 3, 6), (1, 2, 9), (1, 3, 8), (1, 4, 7), (1, 5, 6), (2, 3, 7), (2, 4, 6), (3, 4, 5), (3, 9), (4, 8), (5, 7)]}
    number_of_dice=2
    while box[1:]!=[0]*9:
        number=dice_roll(number_of_dice)
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
        box_nums=random.choice(new_poss) 
        for i in box_nums:
            box[i]=0
        if box[4:]==[0]*6:
            number_of_dice=1
    return True

def probability_of_winning(number_of_games):
    truth=0
    for i in range(number_of_games):
        if shut_the_box()==True:
            truth+=1
    return truth/number_of_games*100

if __name__=='__main__':
    number_of_games=100000
    print(probability_of_winning(number_of_games), '%')
        
