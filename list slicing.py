#list_name[starting_idx:ending_idx]

a=["name",23,"dhaka","school","boy",306]

print(a[0:3])

#list method

b=[56,78,9]
b.append(67)
print(b)

#sorting

b.sort()
print(b)

#sort in decending order
b.sort(reverse=True)
print(b)


#list.insert(index,element)

c=[12,32,14]
c.insert(0,10)
print(c)

#remove

c.remove(10)
print(c)

c.pop(1)
print(c)