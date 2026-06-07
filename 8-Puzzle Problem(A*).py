from queue import PriorityQueue

goal = (1,2,3,4,5,6,7,8,0)

def h(state):
    return sum(state[i] != goal[i] and state[i] != 0 for i in range(9))

def solve(start):
    pq = PriorityQueue()
    pq.put((h(start), 0, start))
    visited = set()

    while not pq.empty():
        _, cost, state = pq.get()

        if state == goal:
            print("Solved")
            return

        if state in visited:
            continue
        visited.add(state)

        z = state.index(0)
        moves = []
        if z > 2: moves.append(z - 3)
        if z < 6: moves.append(z + 3)
        if z % 3 > 0: moves.append(z - 1)
        if z % 3 < 2: moves.append(z + 1)

        for m in moves:
            s = list(state)
            s[z], s[m] = s[m], s[z]
            s = tuple(s)
            pq.put((cost + 1 + h(s), cost + 1, s))

start = (1,2,3,4,0,6,7,5,8)
solve(start)
