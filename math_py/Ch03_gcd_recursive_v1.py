# greatest common divider

def gcd_recursive(a, b):
    i = 0
    print(a, b)
    i += 1
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

gcd_recursive(300, 1050)
