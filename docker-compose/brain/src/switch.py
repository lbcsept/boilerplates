
from dotenv import load_dotenv
import os
import subprocess
import json
import paramiko
# import typer
# app = typer.Typer()

load_dotenv(override=True)
    
# @app.command(short_help="Turn brain on")
def on():
    try:
        cmd = ["wakeonlan", "-i", os.getenv('BRAIN_HOST'), os.getenv('BRAIN_MAC')]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            return json.dumps({"status": "success",
                               "message": "Command succeeded, brain will wake up"})
        else:
            return json.dumps({"status": "error",
                               "message": f"Command failed with error: {result.stderr}"})
    except Exception as e:
        return json.dumps({"status": "error",
                           "message": f"An unexpected error occurred: {str(e)}"})



# @app.command(short_help="Turn brain off")
def off():
    try:
        hostname = os.getenv("BRAIN_HOST")
        username = os.getenv("BRAIN_USER")
        password = os.getenv("BRAIN_PSW")
        port = 22

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(hostname, port, username, password)
        stdin, stdout, stderr = ssh.exec_command('/usr/sbin/poweroff')

        output = stdout.read().decode()
        error = stderr.read().decode()

        if error:
            return json.dumps({"status": "error", 
                               "message": f"Command failed with error: {error}"})
        else:
            return json.dumps({"status": "success", 
                               "message": f"Command succeeded: {output}"})

    except Exception as e:
        return json.dumps({"status": "error", 
                           "message": f"An unexpected error occurred: {str(e)}"})
    finally:
        ssh.close()


# if __name__ == "__main__":
    
#     app()

