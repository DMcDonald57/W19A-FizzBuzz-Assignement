def fizz_buzz(arr):
    for num in arr:
        if (num % 3 == 0 and num % 5 == 0):
            print(num, "FizzBuzz")
        # elif (num % 3 == 0):
        #     print("Fizz")
        #     continue
        # elif (num % 5 == 0):
        #     print("Buzz")

num = [1,30,15,7,55,57,23,9,17,235,1390,44,79,99,348]
print (fizz_buzz(num))