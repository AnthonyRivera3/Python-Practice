#sets are created with a name and {}

set1 = {1,2,3,4,5,6}
set2 = {1,2,3,4,5,6,7,8,9,10}

#prints all values from the sets but the duplicates count as one
print(set1|set2)
#prints the same values in both sets
print(set1 & set2)
#prints different values in both sets
print(set1 ^ set2)
#prints values in set1 that arent in set2. The duplicates get subtracted
print(set1 - set2)


#boolean tests
#6 not in would be false 
#6 in would be true


if 3 not in set1: 
    print("3 not in")
else: 
    print(6 in set1)

    #adding to a set and removing

set3 = {1, 2, 3}
print(set3)
set3.add(5)
print(set3)
set3.remove(2)
print(set3)