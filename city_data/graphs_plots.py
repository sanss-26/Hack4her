import networkx as nx
import matplotlib.pyplot as plt

gml_file_path = 'booking_ds/social_network.gml'
graph = nx.read_gml(gml_file_path)

plt.figure(figsize=(10, 10))
nx.draw(graph, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=15)
plt.title('Graph from GML')
plt.show()