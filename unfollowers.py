from instagrapi import Client

# Initialize the client
cl = Client()

# Login to your account
USERNAME = 'your_username'
PASSWORD = 'your_password'
cl.login(USERNAME, PASSWORD)

# Get your user ID
user_id = cl.user_id

# Fetch the list of followers
followers = cl.user_followers(user_id)
follower_usernames = set([user.username for user in followers.values()])

# Fetch the list of users you are following
following = cl.user_following(user_id)
following_usernames = set([user.username for user in following.values()])

# Identify users you follow who don't follow you back
not_following_back = following_usernames - follower_usernames

# Output the results
print("Users who don't follow you back:")
for username in not_following_back:
    print(username)

