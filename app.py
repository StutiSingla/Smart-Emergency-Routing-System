import sys
sys.path.append("D:/python_libs")  # your D: drive packages

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

from hospitals import choose_best_hospital, graph


st.title("🚑 Smart Emergency Routing System")

# Input: Ambulance start location
start_node = st.selectbox("Ambulance Current Location:", list(graph.keys()))

if st.button("Find Best Hospital"):
    result = choose_best_hospital(start_node)

    st.subheader(f"🏥 Best Hospital: {result['hospital']}")
    st.write(f"📍 Location: {result['location']}")
    st.write(f"🕒 Travel Time: {result['travel_time']} min")
    st.write(f"⏳ Waiting Time: {round(result['waiting_time'], 2)} min")
    st.write(f"✅ Total Time: {round(result['total_time'], 2)} min")

    # Draw graph
    G = nx.Graph()
    for node in graph:
        for neighbor, weight in graph[node]:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(6, 6))

    # Draw nodes
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=800)

    # Highlight best path
    path_edges = list(zip(result["path"], result["path"][1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)

    fig = plt.gcf()  # get current figure
    st.pyplot(fig)
    plt.clf()        # clear the figure for next draw
   
"""
to run:
cd "C:\Users\stuti\Desktop\coding\ai project"
python -m streamlit run app.py
"""
