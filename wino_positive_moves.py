import itertools
permutations=list(itertools.product([0,1,2,3,4,5,6,7,8,9], repeat=3))
for lista in permutations:
    print "Lock Code: " +str(lista) + " -- How many moves: " + str(sum(lista))