def de_identify(a):
    a = a[:6] + "*" * 7
    return a
    
print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))