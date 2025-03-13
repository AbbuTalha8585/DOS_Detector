import matplotlib.pyplot as plt

def visualize_traffic(df):
    normal_traffic = df[df['anomaly'] == 'Normal']
    anomalous_traffic = df[df['anomaly'] == 'Anomaly']

    plt.figure(figsize=(10, 6))
    plt.scatter(normal_traffic['time'], normal_traffic['length'], c='green', label='Normal', s=10)
    plt.scatter(anomalous_traffic['time'], anomalous_traffic['length'], c='red', label='Anomaly', s=10)
    plt.title('Network Traffic Analysis')
    plt.xlabel('Time')
    plt.ylabel('Packet Length')
    plt.legend()
    plt.grid()
    plt.show()