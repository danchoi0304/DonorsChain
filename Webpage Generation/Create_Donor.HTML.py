import shutil 
import os
 
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Donor Information</title>
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
        <img src="https://media.licdn.com/dms/image/C5603AQG5b7fPg2IpRQ/profile-displayphoto-shrink_400_400/0/1646884325797?e=1727308800&v=beta&t=ozPj-K9ZSYB6qoOWUioZ35NP-BGRAEdlaD-BwLHvmaI">
        <h1>Sunwoo Kim</h1>
        <p>CEO of Just Q, Inc, Vice President of Korea Social Contribution Association</p>
        <h2>Interests</h2>
        <p>Blockchain and E-commerce</p>
        <h2>About Me</h2>
        <p>I founded a South Korean e-commerce enabler startup JustQ in 2016, with the vision of making online retail accessible to all companies.</p>
        <p>Our company currently enables the global distribution of over 3.5 million products for 400 partner companies across 34 global online marketplaces including Coupang, Lazada and Shopee.</p>
        <p>Donating through DonorsChain has been a significant step in my journey of giving, as the technology behind DonorsChain aligns with my interests.</p>
        <p>I believe that we can all achieve a better world if we help each other, starting with a small benevolence.</p>
        <p>I will continue to help others and contribute to society!</p>
        <p>For more Information, visit <a href="https://www.justq.com/">Just Q website</a></p>
    </div>
</body>
</html>
"""

# Save the HTML content to a file
with open("donor_basic.html", "w") as html_file:
    html_file.write(html_content)