import shutil 
import os
 
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Introduction to Alex Johnson</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .profile-pic {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            margin-bottom: 20px;
        }
        h1 {
            color: #333;
        }
        .social-links a {
            margin: 0 10px;
            text-decoration: none;
            color: #1a0dab;
        }
    </style>
</head>
<body>
    <div class="container" style = "text-align:center">
        <img src="https://fina.hkust.edu.hk/sites/finance/files/styles/sbm_ppl_details_p/public/2022-06/_files_seth_480x480_3c85ffffff1.png">
        <h1>Seth Hwang</h1>
        <p>Adjunct Associate Professor at HKUST</p>
        <h2>Interests</h2>
        <p>Artificial Intelligence and Machine Learning Applications in Finance, Portfolio Management with Financial Technology, Cryptocurrency Market</p>
        <h2>About Me</h2>
        <p>Seth Hwang: Brief information of Hwo I am and Why I want to donate to the younger generation</p>
        <p>For more Informations, visit <a href="https://fina.hkust.edu.hk/faculty/directory/sethhuang">HKUST website</a></p>
    </div>
</body>
</html>
"""

# Save the HTML content to a file
with open("donor_basic.html", "w") as html_file:
    html_file.write(html_content)