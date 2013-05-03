import string
from graph import *


class element(object):
    def __init__(self,word):
       self.word = word
       
    def freely_reduce(self):
        i=0
	while i<len(self.word)-1:
		if (self.word[i]==self.word[i].lower() and self.word[i].upper()==self.word[i+1]) or (self.word[i]==self.word[i].upper() and self.word[i].lower()==self.word[i+1]):
			self.word = self.word[:i]+self.word[i+2:]
			if i>0: i-=1
		else:
			i+=1
	return self.word
    
    def inverse(self):
	return ''.join([c.upper() if c==c.lower() else c.lower() for c in self.word[::-1]])


class free_group(object):
    def __init__(self, rank, alpha): # alpha = "alpha", or a single alpanumeric letter 
        self.rank = rank
        self.alpha = alpha
        self.gens =[]
        self.GENS =[]
        self.mongens =[]
        self.Alph =  string.ascii_lowercase
                
    def make_gens(self):
        for x in range(0, self.rank):
             if self.alpha == "alpha":
                self.gens.append(self.Alph[x])
                self.GENS.append(self.Alph[x].upper())
             else:
                self.gens.append(self.alpha.lower()+str(x+1))
                self.GENS.append(self.alpha.upper()+str(x+1))
             
             self.mongens = self.gens + self.GENS
             
    def is_element(self,word):
        i = 1
        for c in word:
            if not (c in self.mongens):
              i = 0
            
        if i == 0:
            print("Warning word", word, "is not in the free group")

class subgroup(object):
   def __init__(self, name, subgp_gens):
       self.name = name
       self.subgp_gens = subgp_gens
       self.flower = Graph(rooted=True,label= self.name)

   def make_flower(self):
       for w in self.subgp_gens:
           self.flower.addLoop(self.flower.root,w)


      #return(K)
              
F=free_group(2,"b")
G=free_group(2,"alpha")
w="abBbA"
y="abbBA"
v=["b1","B1","b1","B2"]
F.make_gens()
X=F.mongens
print(X)
F.is_element(v)
F.is_element(w)
print("now G\n")
G.make_gens()
Y=G.mongens
print(Y)
G.is_element(v)
G.is_element(w)
R=subgroup("H1",[w,v,y])
R.make_flower()
print "digraph R.flower {"
print (str(R.flower))
print "}"
R.flower.fold()
print "folded digraph R.flower {"
print (str(R.flower))
print "}"
