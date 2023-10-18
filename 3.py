import random
trouve = 0
echange = 0


num=int(input("un nombre entre 5 et 10"))

tableau = num * [0]

for i in range (len(tableau)):
    tableau[i]=random.randint(0,num*5)
    trouve = tableau [i]
    tempo = -1
    while (tempo<i-1) :
        tempo += 1
        if ( tableau [tempo] == trouve ) :
            tableau[i]=random.randint(0,num*5)
            trouve = tableau [i]
            tempo = -1
        if (tableau [tempo] > trouve) :
            echange = tableau[tempo]
            tableau [tempo] = tableau [i]
            tableau [i] = echange

print (tableau)            