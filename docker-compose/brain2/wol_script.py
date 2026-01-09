import socket
import struct

def send_magic_packet(mac_address):
    # Convert MAC address to bytes
    mac_bytes = bytes.fromhex(mac_address.replace(':', ''))

    # Create magic packet
    magic_packet = b'\xff' * 6 + mac_bytes * 16

    # Send magic packet
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(magic_packet, ('<broadcast>', 9))

# Example usage
send_magic_packet('01:02:03:04:05:06')
