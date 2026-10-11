import heapq

def minimumServers(start, end):
    queue = []

    for i, st in enumerate(start):
        queue.append([st, end[i]])

    queue.sort()

    print(queue)
    servers = []

    heapq.heapify(servers)

    for st, end in queue:

        if servers and servers[0] <= st:
            heapq.heappop(servers)

        heapq.heappush(servers, end)
        
   
    return len(servers)


start = [0, 5, 15]
end   = [10, 20, 30]
print(minimumServers(start, end))

start = [1, 2, 3, 4]
end   = [10, 9, 8, 7]
print(minimumServers(start, end))

start = [15, 0, 5]
end   = [30, 10, 20]
print(minimumServers(start, end))

