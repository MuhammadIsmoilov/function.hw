m = int(input())
t = int(input())
def division():
    if m % t == 0 or t % m == 0:
        print('YES')
    else:
        print('NO') 
division(m,t)           