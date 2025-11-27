# 1
# print(["чётное" if x % 2 == 0 else "нечётное" for x in range(1 + int(input()))])

# 2
# print(["FizzBuzz" if x % 5 == 0 else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else x for x in range(101)])

# 3
# some_list = [1, 2, 3, 999, 10, 11]
# print([x if x > 10 else 0 for x in some_list])

# 4
# print({x: "even" if x % 2 == 0 else "odd" for x in range(1, 1 + int(input()))})

# 5
# some_list = ["A", "jsdjd", "12345", "qwer", "sdgftgdfggdkgjdghsdjhgdrhjasgjrghdfjh"]
# print([x if len(x) <= 5 else 5 for x in some_list])
# 6
# some_list = [1, -2, 3, -999, -10, 11, 0]
# print([x if x >= 0 else 0 for x in some_list])

# 7
# some_list = [1, -2, 3, -999, -10, 11, 0]
# print([x**0.5 if x >= 0 else 0 for x in some_list])

# 8
# some_list = [1, -2, 3, -999, -10, 11, 0]
# print([x**2 if x % 2 == 0 else x**3 for x in some_list])

# 9
# some_list = [1, -2, 3, -999, -10, 11, 0, 100, 20, 30, 50]
# print(["High" if x > 50 else "Medium" if x >= 20 else "Low" for x in some_list])