def get_multiples():
    final_num = int(input("What is the hightest number you would like to get to? "))
    total = 0
    for i in range(final_num):
        if i % 3 == 0 or i % 5 == 0:
            total = total + i
        else:
            continue
    print (total)
get_multiples()
