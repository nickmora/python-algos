def fibb(num):
    i = 1
    # a = 0
    # b = 
    previous_val = 0
    current_val = 1
    output = 0

    while current_val < num:
        if(current_val%2==0):
            output = output + current_val
        temp = current_val
        current_val = current_val + previous_val
        previous_val = temp
        # print(current_val)
        i = i + 1
    print(output)

fibb(4000000)

