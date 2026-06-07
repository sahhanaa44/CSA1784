from collections import deque

start = (3,3,1)
goal = (0,0,0)

moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

q = deque([(start, [])])
visited = set()

while q:
    state, path = q.popleft()

    if state == goal:
        print(path + [state])
        break

    if state in visited:
        continue
    visited.add(state)

    m,c,b = state

    for dm,dc in moves:
        if b:
            nm,nc,nb = m-dm,c-dc,0
        else:
            nm,nc,nb = m+dm,c+dc,1

        if 0<=nm<=3 and 0<=nc<=3:
            if (nm==0 or nm>=nc) and (3-nm==0 or 3-nm>=3-nc):
                q.append(((nm,nc,nb), path+[state]))
