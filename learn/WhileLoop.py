# # 1-10 while loop
i=1
while i<=10:
  print(i)
  i+=1


# # 10-1 while loop
i=10
while i>=1:
  print(i)
  i-=1


# print even num between 1-50
i=2
while i<=50:
  print(i)
  i+=2


# another one
i=1
while i<=50:
  if(i%2==0):
    print(i)
  i+=1


# Write a program that prints the sum of first n natural numbers
n= int(input("Enter a number:"))
sum=0
while n>=1:
  sum+=n
  n-=1

print(f'Sum is: {sum}')
