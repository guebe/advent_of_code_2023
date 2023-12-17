import numpy as np
import heapq as hq

a = np.array([list(line.strip()) for line in open("input").readlines()])
END = (len(a)-1, len(a[0])-1)
N, E, S, W = range(4)

# return next node after going at direction
def goto(node, direction):
    offset = [(-1,0), (0,1), (1,0), (0,-1)][direction]
    return (node[0]+offset[0], node[1]+offset[1])

# returns True if node is inside array, False otherwise
def in_board(node):
    return True if (0 <= node[0] <= END[0]) and (0 <= node[1] <= END[1]) else False

# returns True if we go back where we came from, False otherwise
def backwards(direction1, direction2):
    return ((direction1 + 2) % 4) == direction2

# This implements a modified dijkstra where we just insert all nodes we are
# allowed to visit into the priority queue. We do not care for higher cost
# nodes being also inserted there, because they will only be taken into account
# (heapq being a priority sorted queue) if we have to backtrack (if we are not
# allowed to follow the shortest path because of path-constraints)
# Returns the shortest path costs to END
def dijkstra():
    heap = [(0, (0,0), S, 0), (0, (0,0), E, 0)]
    visited = set()
    while heap:
        cost, node, direction, count = hq.heappop(heap)
        # dont visit a node from same direction and count twice, because it
        # must be the same path
        if (node, direction, count) not in visited:
            visited.add((node, direction, count))
            if node == END and count >= 3:
                return cost
            for direction_ in (range(4)):
                node_ = goto(node, direction_)
                if (in_board(node_)):
                    cost_ = cost + int(a[node_[0]][node_[1]])
                    count_ = count + 1 if direction_ == direction else 0
                    if ((node_, direction_, count_) not in visited and
                        count_ <= 9 and
                        not backwards(direction, direction_) and
                        ((direction_ == direction) or (count >= 3))):
                        hq.heappush(heap, (cost_, node_, direction_, count_))
print(dijkstra())
