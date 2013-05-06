from graph import *
import string

class generators(object):
    def __init__(self,rank,alpha):
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

        return(i)
    
class test(object):
    def __init__(self, parm): 
        self.parm = parm

    def red(self, word):
        out = word - self.parm
        return(out)

class test1(object):
    def __init__(self, parm, word): 
        self.parm = parm
        self.word = word
        
    def red(self):
        out = self.word - self.parm
        return(out) 

#I=test(5)
#J=I.red(6)
#print("J",J)
#K=test(11)
#L=K.red(5113)
#print("L",L)
#print("J",J)
A=test1(3,7)
B=test1(11,11111)
print("A",A.red())
print("B",B.red())
