from flask import Flask, request, render_template_string
import socket

app = Flask(__name__)

# Get local IP address
local_ip = socket.gethostbyname(socket.gethostname())

@app.route('/view_file', methods=['GET'])
def view_file():
    cid = request.args.get('cid')
    if not cid:
        return "CID parameter is required", 400

    # Generate the URL for the local IPFS gateway
    ipfs_url = f"http://{local_ip}:8080/ipfs/{cid}"
    
    # Render a simple template to display the link
    return render_template_string('''
        <!doctype html>
        <title>View IPFS File</title>
        <h1>View IPFS File</h1>
        <p>Click the link below to view the file:</p>
        <a href="{{ ipfs_url }}" target="_blank">{{ ipfs_url }}</a>
    ''', ipfs_url=ipfs_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)