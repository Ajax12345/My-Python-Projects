def main():
  my_string = input("Enter your word/s: ")
  piglatin(my_string)


def piglatin(first_word):
  
  
    print ' '.join(i+"ay" if i.lower() == "i" else i[1:]+i[0]+"ay" for i in first_word.split())

main()
