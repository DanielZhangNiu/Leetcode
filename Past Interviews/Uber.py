# test cases:
#input = [(1,3,0.7),(2,3,0.4),(3,3,0.9)]
#input = [(1.5,1.5,1.3),(4,4,0.7)]
input = [(0.5,0.5,0.5),(1.5,1.5,1.1),(0.7,0.7,0.4),(4,4,0.7)]
#input = [(0.5,0.5,0.5),(1.5,1.5,1.1),(0.7,0.7,0.4),(3,3,0.5),(4,4,0.7)]

# Helper function determinate whether two circle are overlapped
def checkOverlap(circle1, circle2):
    dist = ((circle1[0] - circle2[0]) ** 2) + ((circle1[1] - circle2[1]) ** 2)
    radius = ((circle1[2] + circle2[2]) ** 2)
    return True if dist <= radius else False

# Helper function apply dfs to find one cluster from the overlapping pairs list
def bfs(head, ad_list,input_list):
    cluster = []
    list = [head]
    while len(list) > 0:
        circle1 = list.pop(0)
        if cluster.count(circle1) >= input_list.count(circle1):
            continue
        # traverse the overlapped circle list, find next circle that overlapping with the current one
        circle2 = [second for first, second in ad_list if first == circle1]
        pointer = pointer + circle2 #update pointer to the next circle
        cluster.append(circle1) # add circle to cluster
    #print(cluster)
    return cluster

# Main function which maintain the length of input circles, parse input list and overlapped list into clustering
# Delete circle which already appears in any one cluster, return when there is no circle left in list.
def circle_cluster(input_list, overlapped):
    res = []
    while len(input_list) > 0:
        clusters = bfs(input_list[0], overlapped, input_list)
        # append the "biggest" circle of every cluster into result
        res.append(max(clusters,key = lambda x:x[2]))
        # remove all traversed circles from the return cluster
        for i in clusters:
            input_list.remove(i)
    return res   #output

# initialize and create the overlapped circle pairs list from input
overlapped = []
for i in range (len(input)):
    for j in range(i+1, len(input)):
        if checkOverlap(input[i],input[j]):
            overlapped.append([input[i],input[j]])


# Entrance:
rts = circle_cluster(input,overlapped)

print(rts)





#Non maximal Suppression




# Ransac

