import json
import heapq

# --- Load Graph ---
with open("ai project\city_graph.json") as f:
    graph_data = json.load(f)

graph = {}
for node in graph_data["nodes"]:
    graph[node] = []
for edge in graph_data["edges"]:
    weight = edge["distance"] + edge["traffic"]  # for now use static traffic
    graph[edge["from"]].append((edge["to"], weight))
    graph[edge["to"]].append((edge["from"], weight))

# --- Dijkstra Algorithm ---
def dijkstra(graph, start, end):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        (dist, node, path) = heapq.heappop(pq)
        if node in visited:
            continue
        path = path + [node]
        visited.add(node)

        if node == end:
            return (dist, path)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (dist + weight, neighbor, path))

    return (float("inf"), [])

# --- Hospital Selection ---
with open("ai project\hospitals.json") as f:
    hospitals = json.load(f)["hospitals"]

def choose_best_hospital(start):
    best_choice = None
    best_score = float("inf")

    for hospital in hospitals:
        if hospital["current_occupancy"] >= hospital["capacity"]:
            continue  # hospital full, skip

        # Estimate waiting time (simple: occupancy % of capacity * 10 min)
        waiting_time = (hospital["current_occupancy"] / hospital["capacity"]) * 10

        # Travel time (using Dijkstra)
        travel_time, path = dijkstra(graph, start, hospital["location"])

        total_time = travel_time + waiting_time

        if total_time < best_score:
            best_score = total_time
            best_choice = {
                "hospital": hospital["name"],
                "location": hospital["location"],
                "travel_time": travel_time,
                "waiting_time": waiting_time,
                "total_time": total_time,
                "path": path
            }

    return best_choice

# Example: Ambulance at "A"
best = choose_best_hospital("A")
print("Best Hospital:", best["hospital"])
print("Location:", best["location"])
print("Travel Time:", best["travel_time"])
print("Waiting Time:", round(best["waiting_time"], 2))
print("Total Estimated Time:", round(best["total_time"], 2))
print("Route:", " → ".join(best["path"]))
