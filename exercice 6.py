from re import T


def moy_som(x,y,z,t):
    som=x+y+z+t
    moy =som/4 
    return moy,som

x=int (input ("entrez le 1er nombre "))
y=int (input ("entrez le 2eme nombre "))
z=int (input ("entrez le 3 eme nombre "))
t=int (input ("entrez le 4 eme nombre "))
print ("la moyenne et la somme : ",moy_som(x,y,z,t) )