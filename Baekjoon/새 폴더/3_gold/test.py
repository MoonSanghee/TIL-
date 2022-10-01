import heapq
n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))
li.sort()
rooms = [li[0][1]]
for i in range(1, n):
    if rooms[0] > li[i][0]:
        heapq.heappush(rooms, li[i][1])
    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms, li[i][1])
print(len(rooms))