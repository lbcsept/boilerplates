
from dotenv import load_dotenv
import os
# import typer
# app = typer.Typer()

load_dotenv(override=True)
# import logging
# logging.basicConfig(level=logging.INFO)

# @app.command(short_help="Turn brain on")
# def on_old():
#     import wakeonlan as wol

#     brain_mac = os.getenv('BRAIN_MAC')
#     brain_host = os.getenv('BRAIN_HOST')
#     print("Waking up brain at ", brain_mac, " on host ", brain_host)
#     wol.send_magic_packet(brain_mac, ip_address=brain_host, interface="eth0")
#     # wol.send_magic_packet(brain_mac)

# @app.command(short_help="Turn brain on")
def on():
    import subprocess
    cmd = ["wakeonlan", "-i", os.getenv('BRAIN_HOST'), os.getenv('BRAIN_MAC')]
    # logging("Running command: ", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True)
    if result.returncode == 0:
        return "Command succeeded, brain will wake up"


# @app.command(short_help="Turn brain off")
def off():
    import paramiko

    # SSH connection details
    hostname = os.getenv("BRAIN_HOST")
    username = os.getenv("BRAIN_USER")
    password = os.getenv("BRAIN_PSW") # Use key-based authentication if possible
    port = 22  # Default SSH port

    # Create an SSH client
    ssh = paramiko.SSHClient()

    # Automatically add the server's host key (this is insecure; use with caution)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the server
        ssh.connect(hostname, port, username, password)

        # Execute a command
        stdin, stdout, stderr = ssh.exec_command('/usr/sbin/poweroff')

        # Print the output
        output = stdout.read().decode()
        print(output)
        return output
    except Exception as e:
        raise Exception(e)

    finally:
        # Close the connection
        ssh.close()
        #subprocess.run(["ssh", "-t", env.str("BRAIN_IP"), "/usr/sbin/poweroff"])


# if __name__ == "__main__":
    
#     app()

