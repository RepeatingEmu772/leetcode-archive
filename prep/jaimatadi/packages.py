def minimumShipments(packages, maxPackages, maxWeight):
    numPackages = 0
    
    p = 0
    while p < len(packages):
        curr_weight = 0
        curr_numPackages = 0

        numPackages += 1

        if packages[p] > maxWeight:
            return -1 

        while p < len(packages) and (curr_weight + packages[p]) <= maxWeight and curr_numPackages < maxPackages:

            # print("adding package: ", packages[p], "to", numPackages)
            curr_weight += packages[p]
            curr_numPackages += 1
            p += 1

    return numPackages

packages = [2, 3, 4, 1, 2]
maxPackages = 2
maxWeight = 6
print(minimumShipments(packages, maxPackages, maxWeight))


packages = [3, 8, 2]
maxPackages = 3
maxWeight = 7
print(minimumShipments(packages, maxPackages, maxWeight))

packages = [4, 2, 2, 3]
maxPackages = 3
maxWeight = 6
print(minimumShipments(packages, maxPackages, maxWeight))

