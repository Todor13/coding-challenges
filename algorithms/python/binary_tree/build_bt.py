# Tree Node
from algorithms.python.binary_tree.node import Node


def build_tree(arr):
    if not arr:
        return None
    root = Node(arr[0])
    q, n = [(root, 0)], len(arr)
    while q:
        p, i = q.pop(0)
        l_idx = i * 2 + 1
        if l_idx < n and arr[l_idx]:
            left = Node(arr[l_idx])
            p.left = left
            q.append((left, l_idx))
        r_idx = i * 2 + 2
        if r_idx < n and arr[r_idx]:
            right = Node(arr[r_idx])
            p.right = right
            q.append((right, r_idx))

    return root


if __name__ == '__main__':
    root = build_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
