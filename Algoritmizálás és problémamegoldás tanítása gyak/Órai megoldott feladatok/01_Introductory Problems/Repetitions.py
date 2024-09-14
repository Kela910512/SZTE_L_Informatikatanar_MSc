'''
seq = str(input())
count = 1
currentCount = 1

for i in range(1, len(seq)):
    if seq[i] == seq[i - 1]:
        currentCount += 1
        count = max(count, currentCount)
    else:
        currentCount = 1

print(count)
'''



seq = str(input())
def rep(seq):
    count = 1
    currentCount = 1

    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            currentCount += 1
            count = max(count, currentCount)
        else:
            currentCount = 1

    return count
print(rep(seq))
