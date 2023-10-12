#task8
ignor = '-() '
new_number = ""
for i in str(input()):
  if ignor.count(i) == 0:
    new_number+=i
print(new_number)
