def uncover_spy(n, trust):
    trustedBy = {}
    maxNumOfRelationships = n - 1

    for relationship in trust:
        if relationship[1] in trustedBy:
            trustedBy[relationship[1]].append(relationship[0])
        else:
            trustedBy[relationship[1]] = [relationship[0]]

    for spy in range(n):
        candidateSpy = spy + 1
        if candidateSpy in trustedBy:
            if len(trustedBy[candidateSpy]) == maxNumOfRelationships:
                candidateTrustsSomeone = False 
                # They're trusted by everyone. Who do they trust?
                for relationship in trust:
                    if relationship[0] == candidateSpy:
                        # Can't be this person. They trust someone.
                        candidateTrustsSomeone = True
                        break 
                # They didn't trust anyone, they're the spy.
                if candidateTrustsSomeone == False:
                    return candidateSpy
        else:
            continue 

    return -1

# 2
print(uncover_spy(2, [[1,2]]))
# -1
print(uncover_spy(4, [[1,2], [3,4]]))
# 3 
print(uncover_spy(3, [[1,3], [2,3]]))
# -1
print(uncover_spy(3, [[1,3], [2,3], [3,1]]))
# -1
print(uncover_spy(3, [[1,2], [2,3]]))
# 3
print(uncover_spy(4, [[1,3], [1,4], [2,3], [2,4], [4,3]]))
