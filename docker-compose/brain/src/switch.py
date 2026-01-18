
from dotenv import load_dotenv
import os
import subprocess
import paramiko
# import typer
# app = typer.Typer()

load_dotenv(override=True)
hostname = os.getenv("BRAIN_HOST")
username = os.getenv("BRAIN_USER")
password = os.getenv("BRAIN_PSW")    


import socket
import struct

# def send_magic_packet(mac_address):
#     # Convert MAC address to bytes
#     mac_bytes = bytes.fromhex(mac_address.replace(':', ''))

#     # Create magic packet
#     magic_packet = b'\xff' * 6 + mac_bytes * 16

#     # Send magic packet
#     with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#         s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#         s.sendto(magic_packet, ('<broadcast>', 9))

# def on():
#     send_magic_packet(os.getenv('BRAIN_MAC'))


# @app.command(short_help="Turn brain on")
def on_old():
    try:
        #cmd = ["wakeonlan",
        #  "-i", os.getenv('BRAIN_HOST'), os.getenv('BRAIN_MAC')]
        cmd = ["wakeonlan",  os.getenv('BRAIN_MAC')]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            return {"status": "success",
                    "message": "Command succeeded, brain will wake up"}
        else:
            return {"status": "error",
                    "message": f"Command failed with error: {result.stderr}"}
    except Exception as e:
        return {"status": "error",
                "message": f"An unexpected error occurred: {str(e)}"}

# @app.command(short_help="return brain state")
def state():
    try:
        subprocess.run(["ping", "-c", "1", hostname],
                        capture_output=True, text=True, check=True)
        return {"status": "success", "state": "on", "message": "Brain is ON"}
    except subprocess.CalledProcessError:
        return {"status": "success", "state": "off", "message": "Brain is OFF"}
    except Exception as e:
        return {"status": "error", "state": "off", 
                "message": f"An unexpected error occurred: {str(e)}"}

# @app.command(short_help="Turn brain off")
def off():
    try:

        port = 22

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(hostname, port, username, password)
        stdin, stdout, stderr = ssh.exec_command('/usr/sbin/poweroff')

        output = stdout.read().decode()
        error = stderr.read().decode()

        if error:
            return {"status": "error", 
                    "message": f"Command failed with error: {error}"}
        else:
            return {"status": "success", 
                    "message": f"Command succeeded, brain will sleep, {output}"}

    except Exception as e:
        return {"status": "error", 
                "message": f"An unexpected error occurred: {str(e)}"}
    finally:
        ssh.close()


# if __name__ == "__main__":
    
#     app()

