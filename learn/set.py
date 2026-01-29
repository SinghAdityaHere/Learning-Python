# set only stores unique values and no duplicate, ordered  { }

# You are given a list of prog lang
# ["python","java","c++","python","java","c"]
# convert it into a set and print how many unique lang 

progList=["python","java","c++","python","java","c"]
print(type(progList))
print(progList)

progSet=set(progList)
print(type(progSet))
print(progSet)

print("unique langs known: ", len(progSet))
