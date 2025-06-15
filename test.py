

def sol(n,m):
    sum = 0
    for i in range(n,m+1,):
        sum += i
    return sum 


if __name__ == "__main__":
    t = int(input())
    ans = []
    while t > 0:
        n,m = map(int, input().split())
        t -= 1
        print(sol(n,m))
    
