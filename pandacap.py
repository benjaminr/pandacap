import sys
import pandas as pd
from scapy.all import rdpcap


def pcap_to_df(pcap_location: str) -> pd.DataFrame:
    """
    :pcap_location param: File path to pcap
    """
    pkts = rdpcap(pcap_location)
    return pd.DataFrame([[bytes(pkt)[i] 
                         for i in range(0, len(pkt), 2)] 
                         for pkt in pkts
                        ])


if __name__ == "__main__":
    p = pkts_to_df(sys.argv[1])
