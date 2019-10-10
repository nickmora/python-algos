def fizzBuzz(num):
    i = 1
    sum = 0
    while i<num:
        if(i%3==0 or i%5==0):
            # print("Fizz")
            sum = sum + i
            # print(sum + " added " + i)
        i = i + 1
    print(sum)

fizzBuzz(1000)
