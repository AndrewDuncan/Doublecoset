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

E = element("WitHhi")
print(E.word)
print(E.inverse())
w = "WitHhi"
v = "aAbB"
print(w)
print(E.freely_reduce())
print(E.inverse())
print(E.word)

print("or\n")
E.freely_reduce()
