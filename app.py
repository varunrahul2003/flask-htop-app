from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route( '/htop' )
def htop():
    name = "Varun S"
    username = os.getenv("USER") or os.getenv("USERNAME")   # Get system username
    server_time = datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S IST")

    try:
        top_output = subprocess.check_output( "top -b -n 1", shell=True, text=True)
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    return f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time: {server_time}</h3>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)        

