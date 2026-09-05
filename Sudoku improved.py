def daxilet(l,simvol):
    l[uzunluq(l): ]=[simvol]
    return l
def uzunluq(setir):
    say=0
    for i in setir:
        say+=1
    return say
from random import randint
level=int(input("Level (6 or 9): "))
zorluq=int(input('Difficulty (number of empty spaces): '))
reqsay=0
say0 = 0
l=[i for i in range(1,level+1)]
if level==6:
    print("    Sudoku")
else:
    print("        Sudoku")
#Sudokunun özü
while reqsay!=uzunluq(l)**2:
    reqsay = 0
    setirler = dict()
    sutunlar={i:[] for i in range(level)}
    for setir in range(level):
        daxil = []
        nomreler=[]
        for sutun in range(level):
            if uzunluq(l)==6:
                if setir%2==1:
                    if sutun<3:
                        evvelki=setirler[setir-1][ :3]
                    else:
                        evvelki=setirler[setir-1][3: ]
                else:
                    evvelki=[]
            elif level==9:
                evvelki=[]
                evvelki2=[]
                if setir!=0 and setir!=3 and setir!=6:
                    setirbas=0
                    if setir>2 and setir<6:
                        setirbas=3
                    elif setir<9 and setir>5:
                        setirbas=6
                    for set in range(setirbas,setir):
                        if sutun<3:
                            evvelki+=[setirler[set][ :3]]
                        elif sutun<6:
                            evvelki+=[setirler[set][3:6]]
                        else:
                            evvelki+=[setirler[set][6:9]]
                for i2 in evvelki:
                    for j2 in i2:
                        daxilet(evvelki2, j2)
                evvelki=evvelki2
            say0 = 0
            while say0<=level+6:
                a = randint(0, level - 1)
                if a in daxil:
                    continue
                elif (l[a] not in evvelki) and (l[a] not in sutunlar[sutun]):
                    daxilet(daxil, a)
                    daxilet(nomreler,l[a])
                    daxilet(sutunlar[sutun],l[a])
                    break
                else:
                    say0+= 1
        setirler[setir]=nomreler
    for say in range(level):
        reqsay+=uzunluq(setirler[say])
#Sual kimi görünüşü
sualsetir={i: [] for i in range(level)}
sualsetir=setirler
#Cavab
#for setir0 in range(level):
    #print(*setirler[setir0])
yk=level-1
saybos=0
for setir1 in range(level):
    yk-=1
    bosluqlar=[]
    for hard in range(zorluq):
        b = randint(1, level)
        daxilet(bosluqlar,b)
    for xana in range(uzunluq(setirler[setir1])):
        if setirler[setir1][xana] in bosluqlar:
            sualsetir[setir1][xana]=" "
            saybos+=1
bos=level-1
for setir2 in range(level):
    print(f'\033[34m{bos}\033[0m ',*sualsetir[setir2],'',sep="\033[37m|\033[0m")
    bos-=1
if level==9:
    print(f"\033[34m   0 1 2 3 4 5 6 7 8\033[0m")
else:
    print(f"\033[34m   0 1 2 3 4 5\033[0m")
#Həll alqoritmi
while saybos!=0:
    x,y=map(int,input("Enter coordinates: ").split())
    koor=[i for i in range(level-1,-1,-1)]
    y=koor[y]
    texmin=int(input("Number: "))
    cavab=sutunlar[x][y]
    if texmin==cavab:
        saybos-=1
        sualsetir[y][x]=cavab
        print('\033[92mCorrect!\033[0m')
    else:
        print('\033[91mWrong!\033[0m')
        continue
    bos = level-1
    for setir3 in range(level):
        print(f'\033[34m{bos}\033[0m ',*sualsetir[setir3],sep="\033[37m|\033[0m")
        bos-=1
    if level==9:
        print(f"\033[34m   0 1 2 3 4 5 6 7 8\033[0m")
    else:
        print(f"\033[34m   0 1 2 3 4 5\033[0m")
print('\033[93mSolved!\033[0m')
