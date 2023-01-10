def convert_ipv6(address):
    temp = []
    for i in range(0, len(address),2):
        temp.append(address[i] * 256 + address[i+1])
    str_add = [str(hex(x))[2:] for x in temp]
    
    candidates = zero_sequences(temp)
    if len(candidates) > 0:
        index, length = max(candidates, key=lambda x: x[1])
        del str_add[index: index+length]
        if len(str_add) == 0:
            return "::"
        elif len(str_add) == 1:
            str_add.insert(0, ':')
            return ':'.join(str_add)
            
        if index+length > len(temp):
            str_add.append(':')
        else:
            str_add.insert(index, '')
        
    return ':'.join(str_add)

def zero_sequences(address):
    N = len(address)
    result = []
    index = -1
    length = 0
    i = 0
    j = 0
    while (i < N):
        if j == N:
            return result
        if address[i] == 0:
            index = i
            length += 1
            j = i + 1
            while (j < N):
                if address[j] == 0:
                    length += 1
                    j += 1
                else:
                    i = j
                    j = len(address) + 1
            result.append((index, length))
            length = 0
        i += 1
    return result

if __name__ == "__main__":

    ipv6 = bytearray(b'\xff\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff\xd7\x6d\xa0')
    # should convert to ff02::1:ffd7:6da0
    print(convert_ipv6(ipv6))

    ipv6 = bytearray(b'\xff\xff\x00\x00\xff\xff\x00\x00\xff\xff\x00\x00\xff\xff\x00\x00')
    print(convert_ipv6(ipv6))

    ipv6 = bytearray(b'\xff\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff\xd7\x6d\xa0')
    print(convert_ipv6(ipv6))
    ipv6 = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    print(convert_ipv6(ipv6))
    ipv6 = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01')
    print(convert_ipv6(ipv6))
    ipv6 = bytearray(b'\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01')
    print(convert_ipv6(ipv6))
    ipv6 = bytearray(b'\xfe\x80\x00\x00\x00\x00\x00\x00\x4f\x21\x13\xff\xfe\xa1\xde\xe2')
    print(convert_ipv6(ipv6))
    ipv6 = bytearray(b'\xfe\x80\x00\x00\x00\x00\x00\x00\x1f\x00\x00\x00\x00\x01\xed\xe6')
    print(convert_ipv6(ipv6))
    ipv6 = bytearray(b'\x20\x01\x4c\xa0\x20\x01\x3a\x40\xe1\x14\x90\xfe\x38\x62\x44\x4f')
    print(convert_ipv6(ipv6))
