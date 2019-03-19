def main(n):
    return(nth_prime_number(n))


def nth_prime_number(n):
    if n==1:
        return 2
    count = 1
    num = 3
    while(count <= n):
        if is_prime(num):
            count +=1
            if count == n:
                return num
        num +=2 #optimization
        
def is_prime(num):
    factor = 2
    while (factor < num):
        if num%factor == 0:
            return False
        factor +=1
    return True 