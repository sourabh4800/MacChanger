import subprocess
import re

def get_current_mac(interface):
    result = subprocess.run(['ifconfig', interface], capture_output=True, text=True)
    mac_address = re.search(r'(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)', result.stdout)
    if mac_address:
        return mac_address.group(0)
    else:
        print(f"Could not read MAC address for {interface}")
        return None

def change_mac(interface, new_mac):
    print(f"Changing MAC address for {interface} to {new_mac}")
    
    subprocess.run(['sudo', 'ifconfig', interface, 'down'])
    subprocess.run(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.run(['sudo', 'ifconfig', interface, 'up'])

def main():
    interface = input("Enter the interface (e.g., eth0, wlan0): ")
    new_mac = input("Enter the new MAC address (e.g., 00:11:22:33:44:55): ")

    current_mac = get_current_mac(interface)
    if current_mac:
        print(f"Current MAC address: {current_mac}")
        change_mac(interface, new_mac)
        
        updated_mac = get_current_mac(interface)
        if updated_mac == new_mac:
            print(f"MAC address was successfully changed to {updated_mac}")
        else:
            print("Failed to change the MAC address")

if __name__ == "__main__":
    main()
