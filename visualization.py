###eviromment: evrm_4
import networkx as nx
import pickle
import matplotlib.pyplot as plt
from temp_color import get_gradient_color,get_source_color
from guas_plot import add_guass
noise_ratio=0.0
max_cascade_rank=20
f=open('v_data/christianity_graph_adj','rb')
data=pickle.load(f)
f=open(f'v_data/christianity_max{max_cascade_rank}_cascade','rb')
max_cascade=pickle.load(f)

G = nx.from_scipy_sparse_array(data)
print("1:")

plt.figure(figsize=(5, 5), dpi=60)

pos=nx.spring_layout(G,k=0.1, seed=10396953)
#pos=nx.shell_layout(G)
#pos = nx.spiral_layout(G)
#pos=nx.random_layout(G)

node_number=G.number_of_nodes()
color_map = ["white"]*node_number
color_gradient=100
cl=len(max_cascade)
cascade_color_map=get_gradient_color((200, 50, 0),(50, 200, 0),color_gradient,noise_ratio)
cascade_color_map=get_source_color((200, 50, 0),(50, 200, 0),color_gradient,noise_ratio)

color_step=cl/color_gradient
color_idx=0
cascade_color=[]
print("len(cascade_color_map)",len(cascade_color_map))
print("color_gradient",color_gradient)
print("cl",cl)
print("color_step",color_step)

for cascade_idx in  range(cl):
    print("int(cascade_idx/color_step-1)", int(cascade_idx / color_step ))
    cascade_color.append(cascade_color_map[int(cascade_idx/color_step)])

#cascade_color.append(cascade_color)

count=0

for cascade_idx in  max_cascade:
    color_map[cascade_idx]=cascade_color[count]
    count=count+1
    print("count",count)

print("cascade_color[-1]",cascade_color[-1])
print("cascade_color_map[-1]",cascade_color_map[-1])
cascade_edges=[]
for node in max_cascade:
    cascade_edges.extend(list(G.edges(node)))
    print(G.edges(node))
print(cascade_edges)

subgraph = G.subgraph(max_cascade)
subpos=nx.spring_layout(subgraph,k=0.3, seed=1)
#subpos=nx.shell_layout(subgraph)
#####################draw graph#################
#nx.draw_networkx_edges(G, pos,alpha=0.3,width=0.1,edge_color="#666666")
nx.draw_networkx_edges(subgraph,subpos,alpha=0.1,width=2,edge_color="#666666",edgelist=subgraph.edges)
#nx.draw_networkx_nodes(G, pos,node_size=1,node_color=color_map)
#nx.draw(G,pos,node_size=2,node_color=color_map,width=0.1,with_labels=False,font_size=0.01)

nx.draw_networkx_nodes(subgraph,subpos, nodelist=max_cascade, node_size=15, node_color=cascade_color)
print("2:")

plt.savefig(f'v_data/G_christianity_{max_cascade_rank}graph_{noise_ratio}.pdf',bbox_inches='tight',pad_inches=0)
plt.show()
print("3:")


