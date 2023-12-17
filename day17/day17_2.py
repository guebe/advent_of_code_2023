import numpy as np
import heapq as hq

a = np.array([list(line.strip()) for line in open("input").readlines()])

end = (len(a)-1, len(a[0])-1)
N, E, S, W = range(4)
to_direction = ['N','E','S','W']

def goto(node, direction):
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    d = dirs[direction]
    return (node[0]+d[0], node[1]+d[1])

def in_board(node):
    return True if (0 <= node[0] <= end[0]) and (0 <= node[1] <= end[1]) else False

# just insert all nodes in the priority queue
# and dont care for higher cost nodes
# they will not be taken out there anyways

# dijkstra
# node: direction of travel  N O S W
# and a counter for same directions
# three same -> turn
# previous list to backtrack
def dijkstra():

    PR = [(-1,-1)]
    heap = [(0, (0,0), S, 0, PR),(0, (0,0), E, 0, PR)] # 0 is the distance, S is the start vertice (x,y) coordintates, direction and count
    visited = set()
    # idea is that we have a sorted heap queue
    # we add every traversed node unconditionally to the hq
    # this means we have duplicates with shorter paths
    # but because of the sorting we always find the best path
    # and duplicates are detected and thrown away later on
    # in other words we spare the step to modify the temporary node list
    # instead we add new elements - this must be checked later on by
    # comparing if we already found a shorter distance
    while heap:
        #print(heap)
        dist, node, direction, count, prev = hq.heappop(heap)
        if (node, direction, count) not in visited: # forward only, dont step back
            print(f"visiting {node}")
            if node == end and count > 2:
                print(dist)
                print(prev)
                return dist
            if in_board(node) and (count <= 10): # nodes not in board are consumed # FIXME double conditions both
                visited.add((node, direction, count))
                for direction_next in (range(4)):
                    node_next = goto(node, direction_next)
                    if (in_board(node_next)):
                        # update distance of this node
                        dist_next = dist + int(a[node_next[0]][node_next[1]])
                        count_next = count + 1 if direction_next == direction else 0
                        if (node_next, direction_next, count_next) not in visited and count_next <= 9 and ((direction + 2) % 4) != direction_next and ((direction_next == direction) or (count > 2)):
                            print(f"goto {node_next}")
                            x = prev.copy()
                            x.append(node)
                            hq.heappush(heap, (dist_next, node_next, direction_next, count_next, x)) # FIXME only add if not visited

print(dijkstra())
