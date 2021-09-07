import sys
from collections import deque

input = sys.stdin.readline

deq = deque([])

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'push_front':
        deq.appendleft(command[1])
    elif command[0] == 'push_back':
        deq.append(command[1])
    elif command[0] == 'pop_front':
        if not deq:
            print(-1)
        else:
            print(deq.popleft())
    elif command[0] == 'pop_back':
        if not deq:
            print(-1)
        else:
            print(deq.pop())
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        if not deq:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if not deq:
            print(-1)
        else:
            print(deq[0])
    elif command[0] == 'back':
        if not deq:
            print(-1)
        else:
            print(deq[-1])
