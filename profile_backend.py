import pandas as pd
import ssl
import random

ssl._create_default_https_context = ssl._create_unverified_context
sheet_id = '1h9qfd0N7EDcdhWPAAyv-ySKUEj86ye0_j0rjuHyG17k'

df = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')
element = df.values[[-1],[0,3]]
name = df.values[[-1],[1]]
ls_name = df.values[[-1],[6]]
full_name = name+' '+ls_name
email = df.values[[-1],[2]]
street_address = df.values[[-1],[5]]

randomLowerLetter1 = chr(random.randint(ord('a'), ord('z')))
randomLowerLetter2= chr(random.randint(ord('a'), ord('z')))
randomUpperLetter1 = chr(random.randint(ord('A'), ord('Z')))
randomUpperLetter2 = chr(random.randint(ord('A'), ord('Z')))
username = randomLowerLetter1 + randomUpperLetter1 + randomLowerLetter2 +randomUpperLetter2 + str((random.randint(1,9)))

with open('profile.html','w') as f:
        f.write("<html><head><title>Data Display</title><style>h1{color:black;position:relative;left:38rem;font-size:2rem;}p{padding:1rem;width:15rem;background-color:#009DD1;color:#ffffff;;border-radius:1rem;margin-left:5rem;margin-top:3rem}body{background-color:#BBE2EC;overflow-x:hidden}div{padding:2rem;border-radius:1rem;height:40rem;width:30rem;background:url(https://images.squarespace-cdn.com/content/v1/5908027c20099e374ad3d70e/1498497433363-9FIJ7FA1O2O1OMU760YE/symbol-of-caduceus.jpg);background-size:cover;object-fit:cover;opacity:75%;display:flex;width:60%;margin-bottom:3rem;align-items:center;flex-direction:column;position:absolute;left:15%;top:10rem;position:absolute}img{position:absolute;height:6rem;width:6rem;background-color:transparent;border-radius:50%;}</style></head><body>")
        f.write("<a href=./index.html class=margin-left:5rem style=text-decoration:none;color:white;background-color:black;border-radius:0.5rem;padding:0.7rem;left:1rem;top:1rem;position:absolute>Home</a>")
        f.write("<h1>Profile</h1>")
        f.write("<div><img src=https://media.istockphoto.com/id/1337144146/vector/default-avatar-profile-icon-vector.jpg?s=612x612&w=0&k=20&c=BIbFwuv7FxTWvh5S3vB6bkT0Qv8Vn8N5Ffseq84ClGI= style=left:14rem;top:3.5rem;z-index:99></img><p>Name: {}</p> <p>Your Email: {}</p> <p>Username: {}</p><p>Street Address: {}</p></div>".format(full_name,email,username,street_address))
        f.write("</body></html>")

