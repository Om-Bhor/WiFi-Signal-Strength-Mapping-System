import subprocess
import re

def scan_wifi():
    command = ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-s"]
    
    result = subprocess.run(command, capture_output=True, text=True)
    output = result.stdout

    lines = output.split("\n")[1:]
    networks = []

    for line in lines:
        if line.strip() == "":
            continue

        try:
            # Extract RSSI
            signal_match = re.search(r'-(\d+)', line)
            if not signal_match:
                continue

            signal = int(signal_match.group())

            # Extract SSID
            signal_index = line.find(str(signal))
            ssid = line[:signal_index].strip()

            networks.append({
                "SSID": ssid,
                "Signal": signal
            })

        except:
            continue

    return networks


# Test
if __name__ == "__main__":
    data = scan_wifi()
    for net in data:
        print(net)