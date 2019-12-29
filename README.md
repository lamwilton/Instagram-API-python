# Banned Hashtag checker (main.py)
Using this IG API by LevPasha, reads all posts of a user after inputing username  
Checks and outputs if banned hashtags is found.  
Also outputs the top 10 frequent hashtags of the user.  

main.py is the Python script for the above  
dict.txt contains the list of banned hashtags

Limitations:  
The program can only read hashtags from captions of the post but not comments

Sample output for account tombrady:
```
Enter Instagram username: tombrady
===========Post code: BSO0O6QhD6v=============
{'humpday'}
Found banned hashtags:
{'humpday'}
========All posts successfully checked========
========Top 10 Hashtags=========
LFG 20
1 4
GameReady 4
LifeReady 4
ROS 4
tbtimes 4
LETSGO 3
TB1K 3
patsnation 2
MetGala 2
```

## Instagram-API-python by LevPasha
<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=7BMM6JGE73322&lc=US&item_name=GitHub%20donation&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHosted" title="Support project"><img src="https://img.shields.io/badge/Support%20project-paypal-brightgreen.svg"></a>
<a href="https://github.com/LevPasha/Instagram-bot-cs" title="Instagram C# bot"><img src="https://img.shields.io/badge/C%23%20InstaBot-v1.0-blue.svg"></a>
<a href="https://github.com/LevPasha/instabot.py" title="python InstaBot"><img src="https://img.shields.io/badge/python%20InstaBot-v1.0.1-blue.svg"></a>
<a href="http://isdb.pw" title="Instagram stories data base"><img src="https://img.shields.io/badge/ISDB.pw-free-purple.svg"></a>

Unofficial Instagram API to give you access to ALL Instagram features (like, follow, upload photo and video, etc)! Written in Python.

This is the Python port of https://github.com/mgp25/Instagram-API which is written in PHP.
It is still a work in progress to copy all of its API endpoints.

NOTE: To successfully parse for a long time you should verify your phone number in your Instagram account. 
The new fake Instagram account with an unverified phone number after ~ 1-24 hours could not do any requests. All requests will be redirected to the page https://instagram.com/challenge

### Installation Instructions

1. Fork/Clone/Download this repo

    `git clone https://github.com/lamwilton/Instagram-API-python.git`


2. Navigate to the directory

    `cd Instagram-API-python`


3. Install the dependencies

    `pip install -r requirements.txt`


4. Modify examples\test.py with your own username and password


5. Run the test.py script (**use text editor to edit the script and type in valid Instagram username/password**)

