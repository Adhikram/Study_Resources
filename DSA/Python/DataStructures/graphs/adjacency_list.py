from collections import defaultdict, deque
from typing import List, Set, Dict, Optional, Any

class Graph:
    """
    A Graph implementation using adjacency list representation.
    Supports both directed and undirected graphs.
    
    Time Complexity:
    - Add Vertex: O(1)
    - Add Edge: O(1)
    - Remove Vertex: O(V + E) where V is vertices and E is edges
    - Remove Edge: O(1)
    - Get Neighbors: O(1)
    - BFS/DFS: O(V + E)
    
    Space Complexity: O(V + E) where V is vertices and E is edges
    """
    
    def __init__(self, directed: bool = False):
        """
        Initialize an empty graph.
        
        Args:
            directed (bool): If True, creates a directed graph. False creates an undirected graph.
        """
        self.graph = defaultdict(set)  # vertex -> set of neighbors
        self.directed = directed
        self.vertices = set()  # set of all vertices
    
    def add_vertex(self, vertex: Any) -> None:
        """Add a vertex to the graph."""
        self.vertices.add(vertex)
        if vertex not in self.graph:
            self.graph[vertex] = set()
    
    def add_edge(self, from_vertex: Any, to_vertex: Any) -> None:
        """
        Add an edge to the graph.
        
        Args:
            from_vertex: Starting vertex of the edge
            to_vertex: Ending vertex of the edge
        """
        # Add vertices if they don't exist
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        
        # Add edge
        self.graph[from_vertex].add(to_vertex)
        if not self.directed:
            self.graph[to_vertex].add(from_vertex)
    
    def remove_vertex(self, vertex: Any) -> None:
        """
        Remove a vertex and all its edges from the graph.
        
        Args:
            vertex: Vertex to remove
        """
        if vertex not in self.vertices:
            return
        
        # Remove all edges pointing to this vertex
        for v in self.vertices:
            self.graph[v].discard(vertex)
        
        # Remove the vertex and its edges
        del self.graph[vertex]
        self.vertices.remove(vertex)
    
    def remove_edge(self, from_vertex: Any, to_vertex: Any) -> None:
        """
        Remove an edge from the graph.
        
        Args:
            from_vertex: Starting vertex of the edge
            to_vertex: Ending vertex of the edge
        """
        if from_vertex in self.graph:
            self.graph[from_vertex].discard(to_vertex)
        if not self.directed and to_vertex in self.graph:
            self.graph[to_vertex].discard(from_vertex)
    
    def get_neighbors(self, vertex: Any) -> Set[Any]:
        """Return the set of neighbors for a given vertex."""
        return self.graph[vertex].copy() if vertex in self.graph else set()
    
    def get_vertices(self) -> Set[Any]:
        """Return the set of all vertices in the graph."""
        return self.vertices.copy()
    
    def get_edges(self) -> List[tuple]:
        """Return a list of all edges in the graph."""
        edges = []
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if self.directed or vertex <= neighbor:
                    edges.append((vertex, neighbor))
        return edges
    
    def bfs(self, start_vertex: Any) -> List[Any]:
        """
        Perform Breadth-First Search starting from start_vertex.
        Returns list of vertices in BFS order.
        """
        if start_vertex not in self.vertices:
            return []
        
        visited = set()
        result = []
        queue = deque([start_vertex])
        visited.add(start_vertex)
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start_vertex: Any) -> List[Any]:
        """
        Perform Depth-First Search starting from start_vertex.
        Returns list of vertices in DFS order.
        """
        if start_vertex not in self.vertices:
            return []
        
        visited = set()
        result = []
        
        def dfs_recursive(vertex: Any):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start_vertex)
        return result
    
    def has_path(self, from_vertex: Any, to_vertex: Any) -> bool:
        """Return True if there is a path from from_vertex to to_vertex."""
        if from_vertex not in self.vertices or to_vertex not in self.vertices:
            return False
        
        visited = set()
        
        def dfs_path(current: Any) -> bool:
            if current == to_vertex:
                return True
            
            visited.add(current)
            for neighbor in self.graph[current]:
                if neighbor not in visited and dfs_path(neighbor):
                    return True
            return False
        
        return dfs_path(from_vertex)
    
    def get_path(self, from_vertex: Any, to_vertex: Any) -> Optional[List[Any]]:
        """
        Find a path from from_vertex to to_vertex.
        Returns the path as a list if found, None otherwise.
        """
        if from_vertex not in self.vertices or to_vertex not in self.vertices:
            return None
        
        visited = set()
        path = []
        
        def dfs_path(current: Any) -> bool:
            visited.add(current)
            path.append(current)
            
            if current == to_vertex:
                return True
            
            for neighbor in self.graph[current]:
                if neighbor not in visited and dfs_path(neighbor):
                    return True
            
            path.pop()
            return False
        
        return path if dfs_path(from_vertex) else None
    
    def is_cyclic(self) -> bool:
        """Return True if the graph contains a cycle."""
        visited = set()
        rec_stack = set()
        
        def has_cycle(vertex: Any) -> bool:
            visited.add(vertex)
            rec_stack.add(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    if has_cycle(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            
            rec_stack.remove(vertex)
            return False
        
        for vertex in self.vertices:
            if vertex not in visited:
                if has_cycle(vertex):
                    return True
        return False
    
    def __len__(self) -> int:
        """Return the number of vertices in the graph."""
        return len(self.vertices)
    
    def __str__(self) -> str:
        """Return a string representation of the graph."""
        return f"Graph(directed={self.directed}, vertices={self.vertices}, edges={self.get_edges()})"

# Example usage
if __name__ == "__main__":
    # Create a new undirected graph
    graph = Graph(directed=False)
    
    # Add edges
    edges = [(1, 2), (1, 3), (2, 3), (3, 4)]
    for from_v, to_v in edges:
        graph.add_edge(from_v, to_v)
    
    print("Graph:", graph)
    print("Vertices:", graph.get_vertices())
    print("Edges:", graph.get_edges())
    
    # BFS and DFS from vertex 1
    print("BFS from 1:", graph.bfs(1))  # Output: [1, 2, 3, 4]
    print("DFS from 1:", graph.dfs(1))  # Output: [1, 2, 3, 4]
    
    # Check paths
    print("Path exists 1->4:", graph.has_path(1, 4))  # Output: True
    print("Path from 1 to 4:", graph.get_path(1, 4))  # Output: [1, 3, 4]
    
    # Check for cycles
    print("Has cycle:", graph.is_cyclic())  # Output: True
    
    # Remove edge and check again
    graph.remove_edge(2, 3)
    print("Has cycle after removing edge:", graph.is_cyclic())  # Output: False
    
    # Create a directed graph
    digraph = Graph(directed=True)
    digraph.add_edge(1, 2)
    digraph.add_edge(2, 3)
    digraph.add_edge(3, 1)  # Creates a cycle
    
    print("\nDirected graph:", digraph)
    print("Has cycle:", digraph.is_cyclic())  # Output: True 