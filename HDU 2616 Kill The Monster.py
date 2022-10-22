def dfs(depth, hp):
    global min_value
    if depth > min_value:
        return
    if hp <= 0:
        if depth < min_value:
            min_value = depth
        return
    for i in range(num):
        if not used[i]:
            used[i] = True
            if hp <= xlist[i]:
                dfs(depth+1, hp-2*damages[i])
            else:
                dfs(depth+1, hp-damages[i])
            used[i] = False
            
count = int(input())
for _ in range(count):
    num, blood = map(int, input().split())
    damages, xlist = [], []
    for _ in range(num):
        damage, x = map(int, input().split())
        damages.append(damage)
        xlist.append(x)
    used = [False for _ in range(num)]
    min_value = float('inf')
    dfs(0, blood)
    if min_value == float('inf'):
        print(-1)
    else:
        print(min_value)