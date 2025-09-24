from random import randint
from time import sleep

def buiti(l):
    s=''
    for i in l:
        s+=str(i) + ' '
    return s

def hod(p,out):
    if out==True:
        return p
    p+=koloda[randint(0,len(koloda)-1)]
    return p
    
def zhp():
    print('\n'*50)
    print(pname1, ' '*5, pname2+'\n',
          'очки:{:d}'.format(p1),' '*5,
          'очки:{:d}'.format(p2),sep='')
pwin1=[]
pwin2=[]
print('\n'*50)
net=['n','net','no',"не","нет","нэт","н","но"]
k=str(input('Поиграем в очко?\n'))
if k in net:
    quit()
koloda = [5,6,7,8,9,10,11,12,13]
print('\n'*50)
pname1=str(input('Введите имя, Игрок 1\n'))
sleep(0.5)
print('\n'*50)
pname2=str(input('Введите имя, Игрок 2\n'))
sleep(0.5)
print('\n'*50)
while True:
    
    p1=0
    p2=0
    p1+=koloda[randint(0,len(koloda)-1)]
    p2+=koloda[randint(0,len(koloda)-1)]
    pout1=False
    pout2=False

    while True:
        if pout1==True and pout2==True:
            if p1>p2:
                win=1
            elif p2>p1:
                win=2
            else:
                win=3
            break
        
        p1
        zhp()
        sleep(1)
        print('Будете брать карты,',pname1)
        k=str(input())

        if k in net:
            pout1==True
        else:
            p1=hod(p1,pout1)
        if p1>21:
            win=2
            break
        if pout1==True and pout2==True:
            if p1>p2:
                win=1
            elif p2>p1:
                win=2
            else:
                win=3
            break
        if p1==21:
            win=1
            break
        zhp()
        sleep(1)
        print('Будете брать карты,',pname2)
        k=str(input())

        if k in net:
            pout2==True
        else:
            p2=hod(p2,pout2)
        if p2>21:
            win=1
            break
        if p2==21:
            win=2
            break

    zhp()
    if win==1:
        print(pname1, 'won!')
        pwin1.append(1)

    elif win==2:
        print( pname2,'won!')
        pwin2.append(1)
    else:
        print("Выиграл Эль Бебра")

    print("Ещё сыграем в очко?")
    k=str(input())
    if k in net:
        break
    else:
        pass

print(pname1,'-----',buiti(pwin1),'-----',sum(pwin1))
print(pname2,'-----',buiti(pwin2),'-----',sum(pwin2))

print('До новых встреч!')