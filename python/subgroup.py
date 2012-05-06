from graph import Graph
from word import *

#a folded subgroup graph
#subgroup is implicitly a subgroup of the free group generated by the letters of the alphabet
class subgroupGraph(Graph):
	#create a graph from a list of generators
	@classmethod
	def fromGenerators(self,words):
		g=subgroupGraph(rooted=True)
		for word in words:
			g.addLoop(g.root,word)
		while g.fold():
			pass
		return g

	#does word belong to this subgroup?
	#read the word along the graph, and if you end up back at the root vertex, then the word is in the subgroup
	def __contains__(self,word):
		word = freelyReduce(word)	#make sure word is freely reduced, just to save time
		v=self.root					#start at the root vertex
		for c in word:				#for each letter in the word
			v = v.neighbour(c)		#travel along edge labelled by current letter
			if not v:
				return False		#if there's no such edge, and hence no graph vertex to travel to, word is not in the subgroup

		return v==self.root			#if we finish at the root vertex after reading the whole word, then the word is in the subgroup
	
	#find h and s such that word = sh
	#if w = sh, then W = HS, so can find a right coset representative for the inverse of the word, then find the inverse of that
	def leftCosetRepresentative(self,word):
		h,s = self.rightCosetRepresentative(inverse(word))
		return inverse(h),inverse(s)

	#find h and s such that word = hs by reading word round the graph
	def rightCosetRepresentative(self,word):
		word = freelyReduce(word)
		v = self.root				#start at the graph's root vertex
		h = ''						#this will be the subgroup element part
		acc = ''					#this will store the subword read since last at the root vertex

		for c in word:				#for each letter in the word
			if v==self.root:		#if we are at the root vertex, 
				h+=acc				#the accumulated subword is an element of the subgroup
				acc=''

			acc += c				#add the letter to the accumulator
			v = v.neighbour(c)		#try to move along the edge labelled by the current letter
			if not v:				#if no such edge exists, the accumulator contains the coset representative and we are done
				break

		if v==self.root:		#if we are at the root vertex, 
			h+=acc				#the accumulated subword is an element of the subgroup
			acc=''

		s = word[len(h):]		#the coset representative is the remainder of the word after the subgroup element has been read off
	
		return h,s

	def doubleCosetRepresentative(self,word):
		h1,sr = self.rightCosetRepresentative(word)	#read loops round the left as much as possible
		h2, s = self.leftCosetRepresentative(sr)	#read loops off the right of the remainder as much as possible
		return h1,s,h2

#a simple test
def _test_():
	gens = ['abAB','abC','adbC']
	print('H = < %s >' % ', '.join(gens))
	g = subgroupGraph.fromGenerators(gens)

	#try a few words to see if they're in the subgroup
	for word in ['abAB','a','cBA','abCababaadbC']:
		print(word)
		if word in g:
			print(' in H')
		else:
			print(' not in H')
			print(' %s . %s . %s' % g.doubleCosetRepresentative(word))


if __name__=='__main__':
	_test_()
