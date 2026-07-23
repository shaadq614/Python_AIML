car = ["Ford", "BMW","Ferrari","BMW"]
print(car)
print(car[1])

print(car[-2])
#Append() : Add the items at the end
car.append("Mercedes")
print(car)
#insert() : Add the item at the specific index
car.insert(1,"Lamborgini")
print(car)
#extend() : Add list to the list
car.extend(["mustang","Range rover"])
print(car)
#remove() : removes value
car.remove("Lamborgini")
print(car)
#pop() : Also removes value but through indexing
car.pop(4)
print(car)
#clear() : Empties the list completely
#car.clear()
#print(car)
#del : 
del car[4]
print(car)
#index() : Tells the index of the value
fry = car.index("BMW")
print(fry)
#count() : Tells the number of occurance
tree = car.count("BMW") 
print(tree)
"""Sorting and reverse"""
#sort() : In ascending order , but for strings it sets them up in alphabetical order
print(car)
free = car.sort()
print(car)
alphy = ["A","z","Z","S","s","y","f","e","D","a"]
print(alphy)
yo = alphy.sort()
print(alphy)
#sort(reverse=True) : Gives the just reverse list of the sorted[sort()] list
print(alphy)
cry = alphy.sort(reverse=True)
print(alphy)
#reverse() : 
print(car)
car.reverse()
print(car)
"""Copy methods"""
#copy(): Just simply copies one list into another
up = car.copy()
print(up)
#list() : Another copy method
down=list(up)
print(down)