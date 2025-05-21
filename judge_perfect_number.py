#judge the perfect number
def judge_perfect_number(n):
    for i in range(1,1000):
        sum = 0
        for j in range(1,i):
            if n%j == 0:
                sum += j
        if sum == i:
            print(f"{i} is a perfect number")
judge_perfect_number(100)