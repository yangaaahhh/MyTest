# 将ip地址转换成32位二进制数
def ip2bin(ip):
    temp = ip.split('.')
    result = ''
    for i in range(len(temp)):
        temp[i] = str(bin(int(temp[i]))[2:])
        if len(temp[i]) < 8:
            temp[i] = '0' * (8 - len(temp[i])) + temp[i]
        result += temp[i]
    return result


print(ip2bin('127.0.0.1'))
