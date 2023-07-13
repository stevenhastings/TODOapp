import subprocess

def exit_server():
    # Execute the command to stop the Streamlit server
    subprocess.call(["taskkill", "/F", "/IM", "streamlit.exe"])

