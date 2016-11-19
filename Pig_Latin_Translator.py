def main():
  my_string = input("Enter your word/s: ")
  piglatin(my_string)


def piglatin(first_word):
  vowels = ["a", "e", "i", "o", "u"]

  word = first_word.split(" ")
  for i in word:
    if i[:1] not in vowels:
      new_word = i[1:]+i[:1]+"ay"
      print(new_word)
    else:
      new_word = i[1:]+"hay"
      print(new_word)

main()
