def decimal_to_binary(num):
    if num == 0:
        return '0'
    binary = ''
    while num > 0:
        binary = str(num & 1) + binary
        #adds towards
        num >>= 1
    return binary

print(decimal_to_binary(9))