#task9
def count_vowels_and_consonants(string):
  vowels = 'аеёиоуыэюя'
  consonants = 'бвгджзйклмнпрстфхцчшщ'
  vowels_count = 0
  consonants_count = 0

  for char in string:
    if char in vowels:
      vowels_count += 1
    elif char in consonants:
      consonants_count += 1

  return vowels_count, consonants_count

string = str(input())
vowels, consonants = count_vowels_and_consonants(string)
print(vowels, consonants)