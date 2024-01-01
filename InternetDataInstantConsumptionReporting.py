import psutil
import time

def print_network_usage():
    # Get network io statistics
    net_io_before = psutil.net_io_counters()

    # Sleep and get network io statistics again
    time.sleep(1)
    net_io_after = psutil.net_io_counters()

    # Calculate network usage (received + sent)
    received_bytes = net_io_after.bytes_recv - net_io_before.bytes_recv
    sent_bytes = net_io_after.bytes_sent - net_io_before.bytes_sent

    print(f"Received: {received_bytes / 1024:.2f} KB")
    print(f"Sent: {sent_bytes / 1024:.2f} KB")

# Continuously print network usage
while True:
    print_network_usage()
