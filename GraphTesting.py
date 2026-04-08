import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import time

def generate_graph(num_nodes, num_edges):
    # Create a connected watts_strogatz graph
    G = nx.connected_watts_strogatz_graph(num_nodes, num_edges, 0.5)
    return G

def calculate_average_shortest_path_length(G):
    # Calculate the average shortest path length of the graph
    if nx.is_connected(G):
        return nx.average_shortest_path_length(G)
    else:
        return float('inf')
    
# Function to calculate the clustering coefficient of a graph
def calculate_clustering_coefficient(G):
    # Calculate the clustering coefficient of the graph
    return nx.average_clustering(G)

def time_function(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Execution time for {func.__name__}: {end_time - start_time:.4f} seconds")
    return result

#G = time_function(generate_graph, 10000, 5)
#average_shortest_path_length = time_function(calculate_average_shortest_path_length, G)
#clustering_coefficient = time_function(calculate_clustering_coefficient, G)
#print(f"Average Shortest Path Length: {average_shortest_path_length}")
#print(f"Clustering Coefficient: {clustering_coefficient}")
# Draw the graph
#plt.figure(figsize=(10, 6))
#plt.title("Watts-Strogatz Graph")
#nx.draw(G, node_size=40, node_color='blue', with_labels=False)
#plt.show()

def analyze_graph_properties():
    node_counts = [10, 100, 1000, 10000]
    avg_shortest_path_lengths = []
    clustering_coefficients = []
    run_times_shortest_path = []
    run_times_clustering = []

    for num_nodes in node_counts:
        # Generate a graph with a fixed average degree of 6
        G = nx.connected_watts_strogatz_graph(num_nodes, 6, 0.5)

        # Time and calculate average shortest path length
        start_time = time.time()
        avg_shortest_path_length = nx.average_shortest_path_length(G) if nx.is_connected(G) else float('inf')
        end_time = time.time()
        run_times_shortest_path.append(end_time - start_time)
        avg_shortest_path_lengths.append(avg_shortest_path_length)

        # Time and calculate clustering coefficient
        start_time = time.time()
        clustering_coefficient = nx.average_clustering(G)
        end_time = time.time()
        run_times_clustering.append(end_time - start_time)
        clustering_coefficients.append(clustering_coefficient)

    # Plot the results
    plt.figure(figsize=(12, 12))

    # Plot average shortest path lengths
    plt.subplot(2, 2, 1)
    plt.plot(node_counts, avg_shortest_path_lengths, marker='o', label='Avg Shortest Path Length')
    plt.xscale('log')
    plt.xlabel('Number of Nodes (log scale)')
    plt.ylabel('Average Shortest Path Length')
    plt.title('Average Shortest Path Length vs Number of Nodes')
    plt.grid(True)
    plt.legend()

    # Plot clustering coefficients
    plt.subplot(2, 2, 2)
    plt.plot(node_counts, clustering_coefficients, marker='o', label='Clustering Coefficient', color='orange')
    plt.xscale('log')
    plt.xlabel('Number of Nodes (log scale)')
    plt.ylabel('Clustering Coefficient')
    plt.title('Clustering Coefficient vs Number of Nodes')
    plt.grid(True)
    plt.legend()

    # Plot run times for shortest path calculation
    plt.subplot(2, 2, 3)
    plt.plot(node_counts, run_times_shortest_path, marker='o', label='Shortest Path Run Time', color='green')
    plt.xscale('log')
    plt.yscale('log')  # Set y-axis to logarithmic scale
    plt.xlabel('Number of Nodes (log scale)')
    plt.ylabel('Run Time (seconds)')
    plt.title('Run Time for Shortest Path Calculation')
    plt.grid(True)
    plt.legend()

    # Plot run times for clustering coefficient calculation
    plt.subplot(2, 2, 4)
    plt.plot(node_counts, run_times_clustering, marker='o', label='Clustering Coefficient Run Time', color='red')
    plt.xscale('log')
    plt.yscale('log')  # Set y-axis to logarithmic scale
    plt.xlabel('Number of Nodes (log scale)')
    plt.ylabel('Run Time (seconds)')
    plt.title('Run Time for Clustering Coefficient Calculation')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

# Call the function to analyze and plot graph properties
#analyze_graph_properties()


# Create a graph
G = nx.Graph()

# Add nodes (connection points)
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Add edges (resistors) with resistance values as attributes
G.add_edge(1, 2, resistance=10)   # Resistor of 10 ohms
G.add_edge(2, 3, resistance=20)   # Resistor of 20 ohms
G.add_edge(3, 4, resistance=30)   # Resistor of 30 ohms
G.add_edge(4, 1, resistance=40)   # Resistor of 40 ohms
G.add_edge(1, 3, resistance=50)   # Resistor of 50 ohms
G.add_edge(2, 5, resistance=15)   # Additional resistor
G.add_edge(5, 6, resistance=25)   # Additional resistor
G.add_edge(6, 3, resistance=35)   # Additional resistor

G.add_edge(5, 7, resistance=10)   # Tree branch
G.add_edge(7, 8, resistance=20)   # Tree branch
G.add_edge(8, 9, resistance=30)   # Tree branch
G.add_edge(9, 10, resistance=40)  # Tree branch

# Extended test case: add more branches and cycles
G.add_edge(4, 6, resistance=45)   # Connect node 4 to 6, new cycle
G.add_edge(2, 8, resistance=22)   # Shortcut from 2 to 8
G.add_edge(7, 10, resistance=18)  # Connect branch end to another node
G.add_edge(1, 9, resistance=55)   # Long connection from 1 to 9
G.add_edge(3, 7, resistance=33)   # Connect cycle between 3 and 7
G.add_edge(6, 10, resistance=27)  # Connect 6 to 10

# Add isolated node for edge case
G.add_node(11)

# Connect node 11 with a subgraph (tree + mesh structure)
# Tree part
G.add_node(12)
G.add_node(13)
G.add_node(14)
G.add_edge(11, 12, resistance=12)
G.add_edge(12, 13, resistance=13)
G.add_edge(13, 14, resistance=14)

# Mesh part
G.add_node(15)
G.add_node(16)
G.add_edge(12, 15, resistance=15)
G.add_edge(13, 15, resistance=16)
G.add_edge(14, 15, resistance=17)
G.add_edge(13, 16, resistance=18)
G.add_edge(14, 16, resistance=19)
G.add_edge(15, 16, resistance=20)

# Connect the subgraph to the main graph
G.add_edge(14, 7, resistance=21)   # Connect tree/mesh to main graph
G.add_edge(16, 10, resistance=22)  # Connect mesh to main graph

G_tree = nx.minimum_spanning_tree(G)  # Create a minimum spanning tree from G

# Function to calculate equivalent resistance between two nodes
def calculate_path_resistance(G, node1, node2):
    try:
        # Use Dijkstra's algorithm to find the shortest path based on resistance
        path = nx.shortest_path(G, source=node1, target=node2, weight='resistance')
        total_resistance = sum(G[u][v]['resistance'] for u, v in zip(path[:-1], path[1:]))
        return total_resistance
    except nx.NetworkXNoPath:
        return float('inf')  # No path between the nodes
    
def calculate_y_parameters(G):
    # Get the list of nodes
    nodes = list(G.nodes)
    n = len(nodes)
    
    # Initialize the admittance matrix
    Y = np.zeros((n, n), dtype=float)
    
    # Build the admittance matrix
    for u, v, data in G.edges(data=True):
        resistance = data['resistance']
        admittance = 1 / resistance  # Convert resistance to admittance
        
        # Get the indices of the nodes
        i = nodes.index(u)
        j = nodes.index(v)
        
        # Update the matrix
        Y[i, i] += admittance  # Self-admittance for node u
        Y[j, j] += admittance  # Self-admittance for node v
        Y[i, j] -= admittance  # Mutual admittance
        Y[j, i] -= admittance  # Mutual admittance (symmetric matrix)
    
    return Y, nodes

def calculate_equivalent_resistance_from_y(G, node1, node2):
    # Calculate the Y-parameters
    Y, nodes = calculate_y_parameters(G)
    
    # Get the indices of the nodes
    i = nodes.index(node1)
    j = nodes.index(node2)
    
    # Calculate the equivalent resistance
    Y_eq = Y[i, i] + Y[j, j] - 2 * Y[i, j]
    if Y_eq == 0:
        return float('inf')  # No connection
    R_eq = 1 / Y_eq
    return R_eq
