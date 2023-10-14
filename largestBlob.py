"""
Finding largest contiguous region of same color (or integer value) in grid.
bfs is run to find all connected cells for each region,
each cell is linked into a double linked list builtin to grid and counted(visited) flag

taken from: https://teklern.blogspot.com/2019/05/simplified-algorithm-to-find-largest.html
"""

class Node:
    def __init__(self, x, y, color, prev, next):
        self.x = x
        self.y = y
        self.color = color
        self.prev = prev  # double linked list of unvisited cells
        self.next = next  # so we can choose next cell from this list
        self.counted = False  # keeps track of visited cells


class LargestColorBlob:

    def __init__(self, grid):
        self.n = len(grid)
        self.m = len(grid[0])
        self.head = None
        self.tail = None
        self.grid = []

        prev = None
        for x in range(self.n):  # build grid and double linked list
            self.grid.append(list())
            for y in range(self.m):
                self.grid[-1].append(Node(x, y, grid[x][y], prev, None))
                n = self.grid[x][y]
                if prev:
                    prev.next = n
                prev = n

        self.head = self.grid[0][0]
        self.tail = self.grid[-1][-1]

    def delete_linked(self, n):  # delete node in double linked list
        before = n.prev
        after = n.next
        if before:
            before.next = after
        else:
            self.head = after
        if after:
            after.prev = before
        else:
            self.tail = before

    # note that if you are solving such large grids that the stack would overflow, then you can change
    # to a non-recursive dfs using a list to hold the adjacent cells to be explored from.
    # in fact you could unlink the cell from the big double linked list and string them together to form the list

    def dfs(self, n, c):  # dfs to find all connected colors and count them
        if n.color != c or n.counted:
            return 0
        count = 1
        self.delete_linked(n)
        n.counted = True

        # explore adjacent cells, not edge conditions are checked before
        if n.x > 0:        count += self.dfs(self.grid[n.x-1][n.y], c)
        if n.x < self.n-1: count += self.dfs(self.grid[n.x+1][n.y], c)
        if n.y > 0:        count += self.dfs(self.grid[n.x][n.y-1], c)
        if n.y < self.m-1: count += self.dfs(self.grid[n.x][n.y+1], c)
        return count

    def biggest_blob(self, col):
        max_blob = 0  # 1 for starting cell
        while self.head:  # each time though loop will collect a color blob count
            m = self.dfs(self.head, col)  # do next item in not counted list
            max_blob = max(m, max_blob)  # only need to keep track of max count
        return max_blob
