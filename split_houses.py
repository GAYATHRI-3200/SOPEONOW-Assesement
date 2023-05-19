#2
n = int(input())
village = input().strip()

flag = False
village_list = list(village)

for i in range(len(village_list)-1):
    if village_list[i] == 'H' and village_list[i+1] == 'H':
        flag = True
    elif village_list[i] == '.':
        village_list[i] = 'B'

if flag:
    print('NO')
else:
    print('YES')
    print(''.join(village_list))


