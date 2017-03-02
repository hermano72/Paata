x = int(input("Type a number: "))
line = "\nThe number " + str(x) + " is"

b = True
arr = []

d = 2
while d <= x//2 :
  if x % d == 0:
    b = False
    arr.append(d)
  d+=1

if b:
  print(line + " prime")
else:
  print(line + " not prime. All dividers:")
print(', '. join(str(i) for i in arr))
