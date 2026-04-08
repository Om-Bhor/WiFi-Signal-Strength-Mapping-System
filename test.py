from wifi_scanner_mac import scan_wifi

data = scan_wifi()

for net in data:
    print(net)