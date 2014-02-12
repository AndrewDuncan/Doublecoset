from main_loop import *
from wordmap import *
F1=free_group(4,"x")
F2=free_group(4,"y")

k1=['x3','y3','x1']
k2=['x3','y4','x4','x2']
k3=['x1','X4','Y4','Y4','x1','x2','X3']

words=word_factors(F1,F2,k2)

print(words)

listf=list_factors(F1,F2,[k1,k2,k3])

print("now list ", listf)
