a = ["Satya","Prakash","has","written","this","algorithm"]
sum = 0
for i in range(1,len(a)+1):
  priority = ((len(a)-i+1))/((len(a))*((len(a))+1)/2)
  print(a[i-1], "is",priority)
  sum = sum+priority
print("sum = ", sum)