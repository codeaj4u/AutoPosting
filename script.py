

from instagrapi import Client

# Initialize the Instagram client
client = Client()

# Login to Instagram
client.login("r_aj_love_story", "@J@yr@dh@")

# Upload a photo
photo_path = "test.jpg"
caption = "test"
client.photo_upload(photo_path, caption=caption)
