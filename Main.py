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

# Gets us an image and saves it for our bots
def getImage():

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
        reader = JsonReader("base_urls.json")
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
    
    # Get image
    result = getImage()
    if result[0]:
        print("Success")

        
    else:
        print("Failure")

    

    # Post image with bot
    Bot.init()
    print(result[1] + ", " + result[2])
    Bot.sendTweet(result[1], result[2])

if __name__ == "__main__":
    main()