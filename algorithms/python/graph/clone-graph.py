# https://leetcode.com/problems/clone-graph

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node

        if len(node.neighbors) == 0:
            return Node(node.val)

        nodes = {}
        queue = [node]
        visited = {node.val}

        while queue:
            curr = queue.pop(0)

            if curr.val not in nodes:
                nodes[curr.val] = Node(curr.val)

            for n in curr.neighbors:
                if n.val not in visited:
                    queue.append(n)
                    visited.add(n.val)

                if n.val not in nodes:
                    nodes[n.val] = Node(n.val)

                nodes[curr.val].neighbors.append(nodes[n.val])

        return nodes[node.val]
