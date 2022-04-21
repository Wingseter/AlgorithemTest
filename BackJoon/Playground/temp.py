def get_size(num):
    size = 0
    while num > 0:
        num = int(num/10)
        size += 1
    
    return size


def get_num_at(num, index):
    if index == 0:
        return num % 10
    size = get_size(num)

    res = num / pow(10.0, size - index)
    return res % 10


n = 0
sum = 0
i = 0
n = int(input())
while sum < n:
    i += 1
    sum += get_size(i)

if sum != n:
    sum -= get_size(i)

print(get_num_at(i, (n - sum)))