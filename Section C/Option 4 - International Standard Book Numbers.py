def isbn13(isbn):
    if len(isbn) == 10:
        sum = 0
        
        for i in range(len(isbn) - 1):
            if isbn[i] == 'X':
                sum += 10 * (10 - i)
            else:
                sum += int(isbn[i]) * (10 - i)
            
        if sum % 11 == 0:
            return '978' + isbn[0:9] + '0'
        else:
            return 'Invalid'        
        
    elif len(isbn) == 13:
        sum = 0
        for i in range(len(isbn)):
            sum += int(isbn[i]) * (1 if i % 2 == 0 else 3)
        if sum % 10 == 0:
            return 'Valid'
        else:
            return 'Invalid'
    else:
        return 'Invalid'

#Test Cases        
assert isbn13("9780316066525") == 'Valid'
assert isbn13("0330301824") == 'Invalid'
assert isbn13("0316066544") == '9780316066540'


