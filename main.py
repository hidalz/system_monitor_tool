import time

import psutil


class NetworkTrafficMonitor:
    def __init__(self):
        self.last_received, self.last_sent, self.last_total = self.generate_bytes()

    def generate_bytes(self):
        net_io = psutil.net_io_counters()

        bytes_received = net_io.bytes_recv
        bytes_sent = net_io.bytes_sent
        bytes_total = bytes_received + bytes_sent

        return bytes_received, bytes_sent, bytes_total

    def log_network_traffic(self):
        # Get the current network usage
        bytes_received, bytes_sent, bytes_total = self.generate_bytes()

        # Calculate the new network usage since the last check in MB
        mb_new_received = (bytes_received - self.last_received) / 1024**2
        mb_new_sent = (bytes_sent - self.last_sent) / 1024**2
        mb_new_total = (bytes_total - self.last_total) / 1024**2

        # Update the last values for the next check
        self.last_received = bytes_received
        self.last_sent = bytes_sent
        self.last_total = bytes_total

        network_usage = (
            f"Network usage: {mb_new_received:.2f} MB received {mb_new_sent:.2f} "
            f"MB sent {mb_new_total:.2f} MB total"
        )
        return network_usage


class ResourceMonitor:
    def generate_progress_bar(self, metric: float, bars: int = 25) -> str:
        total_progress_bar = int((metric / 100) * bars)
        total_percentage_bar = bars - total_progress_bar

        return "█" * total_progress_bar + "-" * total_percentage_bar

    def log_cpu_usage(self) -> str:
        cpu_percent = psutil.cpu_percent()
        cpu_bar = self.generate_progress_bar(cpu_percent)

        return f"CPU Usage: |{cpu_bar}| {cpu_percent:.2f}%"

    def log_mem_usage(self) -> str:
        mem_percent = psutil.virtual_memory().percent
        mem_bar = self.generate_progress_bar(mem_percent)

        return f"RAM Usage: |{mem_bar}| {mem_percent:.2f}%"


class Monitor(ResourceMonitor, NetworkTrafficMonitor):
    """Monitor class wrapper to log CPU, Memory and Network Traffic usage."""

    def __init__(self):
        ResourceMonitor.__init__(self)
        NetworkTrafficMonitor.__init__(self)


if __name__ == "__main__":
    monitor = Monitor()

    while True:
        # Log and display system resource usage
        network_log = monitor.log_network_traffic()
        cpu_log = monitor.log_cpu_usage()
        mem_log = monitor.log_mem_usage()

        print(f"\r {network_log} | {cpu_log} | {mem_log}", end="")
        time.sleep(0.5)
