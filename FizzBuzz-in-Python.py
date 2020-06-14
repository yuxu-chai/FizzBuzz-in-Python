import random
print('OUTPUT for number 1 to 30')
for i in range(1,31):
    if(i % 15==0):
        print (i,"FizzBuzz")
    elif(i % 5==0):
        print (i,"Buzz")
    elif(i % 3==0):
        print (i,"Fizz")
    else:
        print (i)
        
        
        OUTPUT for number 1 to 30
1
2
3 Fizz
4
5 Buzz
6 Fizz
7
8
9 Fizz
10 Buzz
11
12 Fizz
13
14
15 FizzBuzz
16
17
18 Fizz
19
20 Buzz
21 Fizz
22
23
24 Fizz
25 Buzz
26
27 Fizz
28
29
30 FizzBuzz
