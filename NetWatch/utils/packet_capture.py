from scapy.all import sniff
import pandas as pd

def capture_packets(duration=60):
    packets_data = []

    def packet_callback(packet):
        try:
            packet_data = {
                "time": packet.time,
                "src_ip": packet[1].src if packet.haslayer(1) else None,
                "dst_ip": packet[1].dst if packet.haslayer(1) else None,
                "protocol": packet[1].proto if packet.haslayer(1) else None,
                "length": len(packet)
            }
            packets_data.append(packet_data)
        except Exception:
            pass

    sniff(prn=packet_callback, store=0, timeout=duration)
    return pd.DataFrame(packets_data)