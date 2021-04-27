## Section 3 - Lane Keeping
  * **Running CV2 Video**
    - Download the record-video.py script from the following website.
      - https://github.com/codingforentrepreneurs/OpenCV-Python-Series/blob/master/src/lessons/record-video.py
      - I recommend placing it in the ~/DeepPiCar/driver/code directory for simplicity’s sake as that is where many of the other Python scripts you will use reside, but you do not need to do so.
      - The easiest way to download the record-video script is to do the following:
        - Move to the correct directory: cd ~/DeepPiCar/driver/code
        - Create/open a new vi file: vi record-video.py
           - You will see an open, empty vi file
        - Copy all the Python script in the above link by highlighting it and using point/click.
        - Move to the open vi file and paste the contents of the script into the vi file with point/click.  Afterwards, the file will look like the below.
        - 
        - Type :wq anywhere on the screen to write (save) the above file and quit (: is a special character that prompts an action command line).
      - Run the script with the following command: “python3 record-video.py”
        - The video will begin recording.  You should see a video screen pop up that shows the recording in real time.
      - Interrupt the Bash prompt by pressing CTRL-C when you are finished.
        - Or, press “q” to stop this program
        - The video will be saved as “video.avi”.  Rename the video as you wish.  Be cautious with running record-video.py because the script will overwrite the video file, destroying the previous video.
  * **Testing DeepPiCar code on your video**
    - Download the code below to your local PC (not the Raspberry Pi), use any Python IDE you are comfortable with:
      - https://github.com/Austin-Willoughby/School_Projects/DeepPiCar_Code.ipynb
      - You can save it as a .py file.
    - Move your video from the Raspberry Pi to your PC, and put the DeepPiCar_Code and the .avi video into the same folder.
    - Open the code and rename the string in the very last line to match the name of your video (e.g. mine is named “Long_Red_Track_1”)
    - Run the code
      - Your video should pop up in two new windows.  One window should show steering angle line overlays (hopefully) following the lane lines.  The other video should show the edges of your color mask
      - If the steering angle lines do not follow the lane lines (e.g. they are spastic and jump all over the screen) then most likely we need to tune your color mask to your particular track
      - Color tuning
        - Adjust the numerical HSV mask values in the arrays in the below code block
        - Note that there are 2 masks used because our red tape contains hues in both the 0-10 range and 170-180 range.  If you are not using red tape (or if your lighting is different) you may only need one mask
        - Use the feed displaying the edges of your color mask to determine how well your color mask is isolating your lane lines.  Mine looks like this:
      - Once you’ve tuned your color mask values and gotten acceptable steering angles you will need to save the changes to DeepPiCar.py on the Raspberry Pi
        - Move to the correct directory (if not already there): cd ~/DeepPiCar/driver/code
        - Type vi hand_coded_lane_follower.py
        - Copy/paste the modified code snippets (i.e. modified mask arrays) into the correct sections of hand_coded_lane_follower.py
        - Type :wq
        - We will run DeepPiCar.py, which uses the hand_coded_lane_follower.py
  

