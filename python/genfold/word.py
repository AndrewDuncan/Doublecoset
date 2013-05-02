def freelyReduce(word):
	i=0
	while i<len(word)-1:
		if (word[i]==word[i].lower() and word[i].upper()==word[i+1]) or (word[i]==word[i].upper() and word[i].lower()==word[i+1]):
			word = word[:i]+word[i+2:]
			if i>0: i-=1
		else:
			i+=1
	return word

def inverse(word):
	return ''.join([c.upper() if c==c.lower() else c.lower() for c in word[::-1]])
