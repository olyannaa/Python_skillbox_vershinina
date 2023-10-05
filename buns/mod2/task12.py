#task12
number = str(input())
ignor = '-() '
new_number = ""
for i in number:
  if ignor.count(i) == 0:
    new_number+=i
print(new_number)
