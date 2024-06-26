# System Resource Monitor

A Python application to monitor and log system resources including CPU usage, RAM usage, and network traffic. This tool provides real-time insights into your system's performance, leveraging the `psutil` library for gathering system metrics.

## Features

- **CPU Usage Monitoring**: Displays the CPU usage percentage along with a visual progress bar.
- **RAM Usage Monitoring**: Shows the RAM usage percentage with a corresponding progress bar.
- **Network Traffic Monitoring**: Logs the amount of data received and sent over the network in megabytes.

## Requirements

- Python 3.x
- `psutil` library

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the `psutil` library using pip:

```bash
pip install psutil
```

## Usage

To start monitoring your system's resources, run the script from the command line:

```bash
python main.py
```

The script will continuously display the CPU usage, RAM usage, and network traffic in the terminal. Press `Ctrl+C` to stop the monitoring process.

## Code Snippet

Here's a brief look at the core functionality:

```python
import logging
import time
import psutil

class NetworkTrafficMonitor:
    # Initialization and network traffic monitoring methods

class ResourceMonitor:
    # Methods to generate progress bars and log CPU/RAM usage

class Monitor(ResourceMonitor, NetworkTrafficMonitor):
    # Wrapper class to log CPU, Memory, and Network Traffic usage

if __name__ == "__main__":
    monitor = Monitor()
    while True:
        # Log and display system resource usage
        network_log = monitor.log_network_traffic()
        cpu_log = monitor.log_cpu_usage()
        mem_log = monitor.log_mem_usage()

        print(f"\r {network_log} | {cpu_log} | {mem_log}", end="")
        time.sleep(0.5)
```

## Acknowledgments

Inspired by a tutorial on system monitoring with Python: YouTube Video.

## License

This project is open-source and available under the MIT License.
