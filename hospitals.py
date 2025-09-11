import json

# Load hospital data
with open("C:/Users/stuti/Desktop/coding/ai project/hospitals_data.json") as f:
    hospitals = json.load(f)["hospitals"]


# Dummy graph for example (replace with your actual city graph)
graph = {
    "A": [("B", 5), ("C", 10)],
    "B": [("A", 5), ("C", 3)],
    "C": [("A", 10), ("B", 3)],
    "D": [("B", 2)],
    "E": [("C", 4)],
    "F": [("C", 6)]
}

def choose_best_hospital(start_node):
    # Dummy logic: choose hospital with lowest total time (travel + occupancy)
    best = None
    best_time = float("inf")
    path = [start_node]

    for h in hospitals:
        travel_time = 5  # dummy, replace with real path calculation
        waiting_time = (h["current_occupancy"] / h["capacity"]) * 10  # example waiting time
        total_time = travel_time + waiting_time
        if total_time < best_time:
            best_time = total_time
            best = h
            path = [start_node, h["location"]]

    return {
        "hospital": best["name"],
        "location": best["location"],
        "travel_time": travel_time,
        "waiting_time": waiting_time,
        "total_time": total_time,
        "path": path
    }
