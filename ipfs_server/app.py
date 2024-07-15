from flask import Flask, request, send_from_directory, abort, render_template_string
import subprocess
import os

app = Flask(__name__)
DOWNLOAD_DIR = './downloads'

# Ensure the download directory exists
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.route('/download', methods=['GET'])
def download():
    cid = request.args.get('cid')
    if not cid:
        return "CID parameter is required", 400

    try:
        # Download the file using ipfs get
        subprocess.run(['ipfs', 'get', cid, '-o', DOWNLOAD_DIR], check=True)
        
        # Determine the path to the downloaded file
        file_path = os.path.join(DOWNLOAD_DIR, cid)
        
        # Check if the file was downloaded
        if not os.path.exists(file_path):
            abort(404, description="File not found")

        # Check the content of the file to determine if it should be rendered as HTML
        if os.path.isfile(file_path) and file_path.endswith('.html'):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return render_template_string(content)
        else:
            # Provide a link to download the file for non-HTML files
            return f"File downloaded successfully. <a href='/downloaded_file?cid={cid}'>Download {cid}</a>"
    except subprocess.CalledProcessError:
        return "Failed to download file from IPFS", 500

@app.route('/downloaded_file', methods=['GET'])
def downloaded_file():
    cid = request.args.get('cid')
    if not cid:
        return "CID parameter is required", 400

    try:
        # Determine the path to the downloaded file
        file_path = os.path.join(DOWNLOAD_DIR, cid)
        
        # Check if the file exists
        if not os.path.exists(file_path):
            abort(404, description="File not found")

        # Send the file to the user
        return send_from_directory(DOWNLOAD_DIR, cid, as_attachment=True)
    except Exception as e:
        print(e)
        abort(500, description="Failed to serve file")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)