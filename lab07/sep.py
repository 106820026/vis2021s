total = []
f = open('text.txt')
for line in f.readlines():
    data = []
    for i in line.split(","):
        data.append(float(i))
    total.append(data)
f.close
print(total)
print(len(total))