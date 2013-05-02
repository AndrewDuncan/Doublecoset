import string

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
        self.Alph =  string.ascii_lowercase
        
    def make_gens(self):
        for x in range(0, self.rank):
             if self.alpha == "alpha":
                self.gens.append(str(self.Alph[x]))
                self.GENS.append(self.Alph[x].upper())
             else:
                self.gens.append(self.alpha.lower()+str(x+1))
                self.GENS.append(self.alpha.upper()+str(x+1))
             print(x)
            
    def is_element(self,word): 
        for c in word:
            print(c)
            if c in self.gens:
              print("matched")
            else:  
              print("missed")
              
F=free_group(2,"b")
G=free_group(2,"alpha")
w="ababa"
F.make_gens()
x=F.gens
print(x)
X=F.GENS
print(X)
F.is_element(w)
print("now G\n")
v=["b1","b1","b1","B1","b1","B2"]
F.is_element(v)

print(G.make_gens())
print(G.gens)
print(G.GENS)
G.is_element(v)
G.is_element(w)
