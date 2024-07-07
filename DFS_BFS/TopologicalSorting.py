from collections import deque


def topological_sort(graph):
    in_degree = [0] * len(graph)
    queue = deque()

    # Step 2: Calculate in-degrees
    for vertex in graph:
        for neighbor in graph[vertex]:
            in_degree[neighbor] += 1

    # Step 3: Enqueue vertices with in-degree zero
    for i in range(len(graph)):
        if in_degree[i] == 0:
            queue.append(i)

    # Step 4
    while queue:
        v = queue.popleft()
        print(v)  # Output vertex

        # Step 4c: Reduce in-degree of adjacent vertices
        for neighbor in graph[v]:
            in_degree[neighbor] -= 1

            # Step 4d: Enqueue vertices with in-degree zero
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 5: Check for cycles
    if any(in_degree): print("Graph contains a cycle.")