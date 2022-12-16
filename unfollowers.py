'''SETUP

pip3 install instaloader

set username and password variables to such

IF you have 2fa enabled, then do:
instaloader --login=username
'''

import instaloader

# Loading instaloader object
L = instaloader.Instaloader()
 
username = "username"
password = "passwd"

try:
	# Loading session stored in the system
	L.load_session_from_file(username)
except:
	# Login with username and password
	L.login(username, password)

profile = instaloader.Profile.from_username(L.context, username)
followers = [i.username for i in profile.get_followers()]
followees = [i.username for i in profile.get_followees()]

unfollowers = set(followees)-set(followers)

print(unfollowers)

print("Amount: ", len(unfollowers))
