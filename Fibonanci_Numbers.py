def main():
    counter = 0
    a = 1
    b = 1
    while counter <= 100:
        print a, "\n"
        print a+b, "\n"

        b = a + b
        a = a + b
        counter += 1

main()
