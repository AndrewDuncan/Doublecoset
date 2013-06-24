from alg2a import * #alg2a imports alg1a 

###freely_reduce tests###
#print(element([]).freely_reduce())
#print(element(['a1','A1','A1','A1','a1']).freely_reduce())
#print(element(['a1','b1','c1','d1','D1','C1','B1','A1','D3','D3']).freely_reduce())
#print(element(['z7','D6','b2','A4','A4']).freely_reduce())
#print(element(['','a1','A1','A1','','A1','a1']).freely_reduce()) #(1)
#print(element(['','a1','','A1','A1','','A1','a1']).freely_reduce())#(2)
#print(element(['','a1','','','A1','A1','','A1','a1']).freely_reduce())

#(1) identity elements are treated as being a unique element and must be removed by another function
#(2) identity elements can block other cancellation so early removal is a good idea
#(3) identity elements do cancel each other out (as ''is just '' in any case)

#freely_reduce seems to work

###inverse test###

print(element([]).inverse())
print(element(['a1']).inverse())
print(element(['a1','B2','d7','T19']).inverse())
print(element(['a1','A1','A1','A1','A1']).inverse())

#inverse seems to work

