a=[10,20,30,40,50,50,60]
a.append(60)
print(a)
a.insert(1,15)
print(a)
print(15 in a)
print(a.count(50))
a.remove(20)
print(a)
a.pop(3)
print(a)
del a[1]
max(a),min(a),sum(a)
max(a)
print(max(a))
min(a)
print(min(a))
sum(a)
print(sum(a))
a.reverse()
print(a)
print(a.sort()) #no return
a.sort()
print(a)
print(sorted(a))
c=55.5
d=12
f=c//d
print(f)
print(5+4-2)
print(2**2**-1)
print(5%2)

a=20
b=30
c=50
print(a<b and b<c)
print(a<b or b<c)
print(not a<b)

#tuple
t=(20,20,30)
print(t[0])
#t[1]=30
#print(t)


#dietionary
alpha={"a":1,"b":2,"c":3}
#print(alpha[a])
#print(["b"]=5)
alpha["a"]=5
print(alpha)

#set
s=set((10,20,30,30,40,40))
print(s)