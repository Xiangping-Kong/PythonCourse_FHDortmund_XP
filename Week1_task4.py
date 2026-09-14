if __name__ == '__main__':
    # 计算阶乘，n! = 1*2*3...*n
    n = int(input("Please input a number to calculate factorial: "))
    result = 1
    for i in range(1, n + 1):
        result = result * i
    print("The factorial of " + str(n) + " is: " + str(result))
