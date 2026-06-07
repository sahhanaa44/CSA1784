from itertools import permutations

letters = "SENDMORY"
digits = range(10)

for p in permutations(digits, 8):
    S,E,N,D,M,O,R,Y = p

    if S == 0 or M == 0:
        continue

    send = 1000*S+100*E+10*N+D
    more = 1000*M+100*O+10*R+E
    money = 10000*M+1000*O+100*N+10*E+Y

    if send + more == money:
        print(send, "+", more, "=", money)
        break
