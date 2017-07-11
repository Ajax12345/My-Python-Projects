s = "12345"
converter = {str(i):i for i in range(10)}
print sum(converter[a]*pow(10, i) for i, a in enumerate(s[::-1]))
