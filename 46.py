fr = open('../aaa/data.txt', 'r', encoding='utf-8')
fw = open('../aaa/output.txt', 'w', encoding='utf-8')
data = fr.readlines()
# print(data)
# print(data)
# print(data)

hap = 0
for i in data:
    d = i.rstrip()
    num = float(d)
    hap = hap + num
avg = hap/len(data)

fw.write(f'합계: {hap}\n')
fw.write(f'평균: {avg}')

fr.close()
fw.close()