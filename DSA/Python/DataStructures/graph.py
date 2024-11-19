def main():
    # Initialize the graph as a dictionary
    graph = {}

    # Add Vertex
    graph[1] = []

    # Add Edge
    graph[1].append(2)

    # Remove Vertex
    graph.pop(1, None)

    # Add Vertex again for removing edge demonstration
    graph[1] = [2, 3]

    # Remove Edge
    graph[1].remove(2)

    print("Graph:", graph)

if __name__ == "__main__":
    main()