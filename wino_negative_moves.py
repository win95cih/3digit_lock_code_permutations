import itertools
permutations=list(itertools.product([0,1,2,3,4,5,6,7,8,9], repeat=3))
for lista in permutations:
    move_list=0
    combination=""
    for i in range(len(lista)):
        if lista[i] > 5:
            ile_ruchow=10-lista[i]
            move_list+=ile_ruchow
            combination+=str(ile_ruchow) + " down | "
        elif lista[i] < 5:
            ile_ruchow=0+lista[i]
            move_list+=ile_ruchow
            combination+=str(ile_ruchow) + " up | "
        elif lista[i] == 5:
            ile_ruchow=0+lista[i]
            move_list+=ile_ruchow
            combination+=str(ile_ruchow) + " up/down | "
    print "Lock Code: " +str(lista) +" -- Move list: "+ combination + " -- How many moves: " + str(move_list)