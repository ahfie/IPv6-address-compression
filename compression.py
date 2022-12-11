def convert_ipv6(address):
    # begin insert code
    temp = []
    for i in range(0, len(address),2):
        temp.append(address[i] * 256 + address[i+1])

    candidates = zero_sequences(temp)
    index, length = max(candidates, key=lambda x: x[1])
    str_add = [str(hex(x))[2:] for x in temp]

    del str_add[index: index+length]
    if index+length < len(temp):
        str_add.insert(index, '')
    else:
        str_add.insert(index, ':')
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