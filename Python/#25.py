'''The 12th term, F12 (144), is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?'''

# count = 3 because 2 is the 3rd fibo number and we are starting there :)
fib_cache1, fib_cache2, fib, count = 1,1,2,3

while 1:
    if len(str(fib)) == 1000:
        print(count)
        break
    fib = fib_cache1+fib_cache2
    fib_cache1 = fib_cache2
    fib_cache2 = fib
    count += 1



