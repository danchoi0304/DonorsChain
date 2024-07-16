import shutil 
import os
 
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DonorsChain Tracking</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }

        header {
            text-align: center;
            padding: 20px;
            background-color: #333;
            color: #fff;
        }

        h1 {
            margin: 0;
            font-size: 36px;
        }

        .gallery {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            padding: 20px;
        }

        .gallery img {
            max-width: 100%;
            height: auto;
            margin: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s;
        }
        

        footer {
            text-align: center;
            padding: 10px;
            background-color: #333;
            color: #fff;
        }

        /* Style for links */
        ul {
            list-style-type: none;
            padding: 0;
            text-align: center;
        }

        li {
            margin: 10px 0;
        }

        a {
            text-decoration: none;
            color: #0077b6; /* Link color */
            font-weight: bold;
            font-size: 18px;
            transition: color 0.3s;
        }

        a:hover {
            color: #00557a; /* Link color on hover */
        }

        /* Add margin on left and right for mobile devices */
        @media (max-width: 768px) {
            body {
                margin-left: 10px;
                margin-right: 10px;
            }
        }
        .image-container {
            display: flex;
            justify-content: center;
        }
        .image-container img {
            width: 200px; /* Adjust width as needed */
            height: auto;
    </style>
</head>
<body>
    <header>
        <h1>Bookname</h1>
        <p>Book and Donor Information Provided by DonorsChain</p>
    </header>

    <div class="gallery">
        <img src="https://covers.openlibrary.org/b/isbn/9780385533225-L.jpg">
    </div>

    <!-- Links with styles applied -->
    <ul>
        <li><a href="https://bm.sunykorea.ac.kr/bm/html/sub02/0201.html?mode=V&mng_no=bd9450a4e07706dd8f3bae0aebbb881c">Donor Information</a></li>
    </ul>

    <section style = "text-align:center">
        <h2>About Us</h2>
        <p>Located in Ithaca, NY, our decentralized architecture enables transparent and efficient donations for Tompkins County residents.</p>
    </section>

    <section style = "text-align:center">
        <h2>What we do</h2>
        <ul>
            <li>IPFS (InterPlanetary File System) is a peer-to-peer distributed file system that aims to connect all computing devices with the same system of files.</li>
            <li>Unlike traditional file storage systems, which rely on central servers, IPFS uses a decentralized approach, making it more resilient and efficient.</li>
            <li>Files in IPFS are uniquely identified by a cryptographic hash, ensuring content integrity and versioning.</li>
            <li>With IPFS, one can ensure that files uploaded will not have a single chance of being mutated, since the change will cause the hash (CID) to become different.</li>
            <li>DonorsChain, funded by Ithaca Public Education Initiative, aims to provide cleaner donation with IPFS to Tomkins County Residents.</li>
        </ul>
    </section>

    <footer style = "text-align:center">
        <p>Provided by DonorsChain</p>
        <img src="https://i.ibb.co/sRtVs9N/IPEI-logo-removebg-preview-1.png">
        <p>Funded by IPEI</p>
        <br><br>
        <p style = "text-align:center">Made With </p>
        <div class="image-container">
        <a href="https://ipfs.tech/">
            <img src="https://upload.wikimedia.org/wikipedia/commons/1/18/Ipfs-logo-1024-ice-text.png" alt="Image 1">
        </a>
        </div>
        <div class="image-container">
        <a href="https://cloudflare.com/">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/94/Cloudflare_Logo.png" alt="Image 2">
        </a>
    </div>
    </footer>
</body>
</html>
"""

# Save the HTML content to a file
with open("book_basic.html", "w") as html_file:
    html_file.write(html_content)

# Source path 
# Source path
source = "C:\\Users\\danch\\OneDrive\\바탕 화면\\DonorsChain\\Webpage Generation\\book_basic.html"
  
# Destination path 
destination = "C:\\Users\\danch\\OneDrive\\바탕 화면\\DonorsChain\\Webpage Generation\\outputs\\book_basic.html"

# If the destination file already exists, remove it
if os.path.exists(destination):
    os.remove(destination)

shutil.move(source, destination)