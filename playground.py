
def check(number):
    r_number = ''
    ROMANS = (('M',  1000),
            ('CM', 900),
            ('D',  500),
            ('CD', 400),
            ('C',  100),
            ('XC', 90),
            ('L',  50),
            ('XL', 40),
            ('X',  10),
            ('IX', 9),
            ('V',  5),
            ('IV', 4),
            ('I',  1))

    for roman, value in ROMANS:
        while number >= value:
            number -= value
            print(number)
            r_number += roman
    
    return r_number

print(check(7))