"""
Main.py
Main entry point.
Usage: "python Main.py"
"""

# Imports
import Bot
import WebScraper
from JsonReader import JsonReader

# Camera info

# Gets us a random image and saves it for our bots
# This is an old method. Used to be used when bot only posted random images
def getRandomImage():

    # While loop, in case a camera is down, get another random camera and retry
    loop = True
    loopCount = 1
    success = False

    while loop:
        print("Loop #" + str(loopCount))

        # Stop attempting after looping 5 times
        if (loopCount > 5):
            print("Tried 5 cameras and they are all down. You know what this means")
            success = False
            return success

        # Get random road
        print("Getting random road...")
        reader = JsonReader("json_file_here")
        randomCamera = reader.getRandomUrl()
        
        roadName = randomCamera["display_name"]
        print("Random road: " + randomCamera["display_name"])


        # Save image of road
        print("Saving image of road...")
        fileName = "highway.png"

        result = WebScraper.save_image(randomCamera["base_url"], fileName)
        imagePath = "images/highway.png"

        if result == "error":
            print("Failed to download image - restarting loop.")
            loopCount += 1
            success = False
        else:
            print("Saved image: " + fileName)
            print("Success - exiting loop.")
            loop = False
            success = ((True, roadName, imagePath))

    return success

# Main
def main():

    """ Highway 153 """

    # Read through the highway json file
    reader153 = JsonReader("urls/hwy153.json")
    urls153 = reader153.getAllUrls()
    saved153Images = []

    # Get all iamges
    count = 1
    for item in urls153:
        url = item["base_url"]
        filename = "downloads/hwy153--" + str(count) + ".png"
        displayName = item["display_name"]
        result = WebScraper.save_image(url, filename)
        if result[0]:
            print("[Main]: Saved image #" + str(count))
            saved153Images.append((displayName, filename))
        else:
            print("[Main]: Error on image #" + str(count))
            saved153Images.append(("displayName", "error"))

        count += 1

    # Post all images in a thread
    bot = Bot()

    tweetId = bot.post_text("Highway 153")
    for item in saved153Images:
        if item[1] == "error":
            tweetId = bot.post_text_as_response(item[0] + " - Camera down", tweetId)
        else:
            tweetId = bot.post_image_as_response(item[0], item[1], tweetId)


    """ Interstate 24 """


    """ Interstate 75 """


    """ US 27 """

    

if __name__ == "__main__":
    main()