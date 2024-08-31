# MAC Address Changer

This script allows you to change the MAC address of a network interface on a Linux machine.

## Prerequisites

- Python 3.x
- `ifconfig` command (usually available in the `net-tools` package)
- Root privileges to change the MAC address

## Usage

1. Clone the repository or download the `macchanger.py` script.
2. Open a terminal and navigate to the directory containing `macchanger.py`.
3. Run the script with Python:

    ```sh
    sudo python3 macchanger.py
    ```

4. Follow the prompts to enter the network interface and the new MAC address.

## Example

```sh
$ sudo python3 macchanger.py
Enter the interface (e.g., eth0, wlan0): eth0
Enter the new MAC address (e.g., 00:11:22:33:44:55): 00:11:22:33:44:55
Current MAC address: 08:00:27:4c:22:6a
Changing MAC address for eth0 to 00:11:22:33:44:55
MAC address was successfully changed to 00:11:22:33:44:55
