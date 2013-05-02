class element(object):
    def __init__(self,word):
       self.word = word
       
    def freely_reduce(self, word):
        i=0
	while i<len(word)-1:
		if (word[i]==word[i].lower() and word[i].upper()==word[i+1]) or (word[i]==word[i].upper() and word[i].lower()==word[i+1]):
			word = word[:i]+word[i+2:]
			if i>0: i-=1
		else:
			i+=1
	return word
    
    def inverse(self,word):
	return ''.join([c.upper() if c==c.lower() else c.lower() for c in word[::-1]])

E = element("WitHhi")
w = "WitHhi"
v = "aAbB"
print(w)
print(E.freely_reduce(w))
print(E.inverse(w))
print(E.word)

print(E.freely_reduce(w))
print(E.inverse(w))
print(E.word)
print("or\n")
E.freely_reduce(w)
