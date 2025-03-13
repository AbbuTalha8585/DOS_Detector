from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


def detect_anomalies(df):
    df['protocol'] = df['protocol'].fillna(0).astype(int)
    df = df.fillna(0)
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df[['length', 'protocol', 'time']])

    model = IsolationForest(contamination=0.1)
    model.fit(df_scaled)
    df['anomaly'] = model.predict(df_scaled)
    df['anomaly'] = df['anomaly'].map({1: 'Normal', -1: 'Anomaly'})
    return df