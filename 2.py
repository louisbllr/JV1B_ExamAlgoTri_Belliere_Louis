tableau = [20,50,51,20,64,14]
save = 0
swap = 0

for i in range (len(tableau)):
    if (tableau[i]>save):
        save=tableau[i]


        
if (save == tableau[4]):
    swap=tableau[4]
    tableau[4]=tableau[5]
    tableau[5]=swap
    


print (save)        
print (tableau)
    