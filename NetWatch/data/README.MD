from utils.packet_capture import capture_packets
from models.isolation_forest import detect_anomalies
from visualizations.visualizer import visualize_traffic

# Step 1: Capture network traffic
print("Capturing network traffic...")
df = capture_packets(duration=60)
print("Packet capture complete.")

# Step 2: Detect anomalies
print("Analyzing network traffic...")
df = detect_anomalies(df)
print("Anomaly detection complete.")

# Step 3: Visualize traffic
print("Visualizing results...")
visualize_traffic(df)
print("Visualization complete.")