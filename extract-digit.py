

def extract_last_digit(num):
    while num>0:
        l_d=num%10
        num=num//10
    return l_d
print(extract_last_digit(12345))