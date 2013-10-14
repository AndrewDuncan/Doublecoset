dict={'jack': [['x1','x2'],[]], 'sape': [4139], 'spoeg':['aa','bb']}
print(dict)
print(dict['jack'][0])
print(dict['jack'][1])
L=dict['jack']
print(L)
L.append(['y1'])
dict['jack']=L
L.sort()
print(dict['jack'])
key='jak'
if key in dict:
    print(dict[key])
else: 
    print(key, " not a key")
