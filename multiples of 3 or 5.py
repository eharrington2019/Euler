def get_multiples():
    final_num = int(input("What is the hightest number you would like to get to? "))
    start_value = int(input("What number owuld you like to start with? "))
    while True:
        vals = []
        if 3 * start_value < final_num:
            vals.append(start_value)
        else:
            print "All done."

get_multiples()
