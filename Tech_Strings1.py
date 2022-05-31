def rotationalCipher(input, rotation_factor):
    # Write your code here
    res = ''
    lower = ord('a')
    upper = ord('A')
    for i in input:
        if str.isalnum(i):
            if str.isnumeric(i):
                res = res + str((int(i) + rotation_factor) % 10)
            elif str.isupper(i):
                res = res + chr((ord(i) + rotation_factor - upper) % 26 + upper)
            else:
                res = res + chr((ord(i) + rotation_factor - lower) % 26 + lower)
        else:
            res = res + i

    return "" + res

print(rotationalCipher('Zebra-493?', 3))