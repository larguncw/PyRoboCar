
## Section 3 - Lane Keeping
  * **Running CV2 Video**
    - To record a video on your raspberry pi, navigate to ~/PyRoboCar/driver/code/RaspberryPi
      - Run the script with the following command: “python3 record-video.py”
      - ![](images/sec3image2.PNG)
        - The video will begin recording.  You should see a video screen pop up that shows the recording in real time.
      - Interrupt the Bash prompt by pressing CTRL-C when you are finished.
        - Or, press “q” to stop this program
        - The video will be saved as “video.avi”.  Rename the video as you wish.  Be cautious with running record_video.py because the script will overwrite the video file, destroying the previous video.
  * **Testing PyRoboCar code on your video**
    - You can complete the next steps on either your PC or the Raspberry Pi itself. We would recommend using your PC for the increased processing power. 
    
	    - Move your video and the hand_coded_lane_follower.py file from the Raspberry Pi to your PC. Make sure your video file and .py file are in the same folder. The hand_coded_lane_follower.py file can be found in ~/PyRoboCar/driver/code/PC
	    - Open the code and rename the string in the very last line to match the name 		of your video (e.g. mine is named “angle_3”)
    - ![](images/sec3image3.PNG)
	    - Run the code
      - Your video should pop up in two new windows.  One window should show steering angle line overlays (hopefully) following the lane lines.  The other video should show the edges of your color mask
      - If the steering angle lines do not follow the lane lines (e.g. they jump all over the screen) then most likely we need to tune your color mask to your particular track
- **Color tuning**
	- Adjust the numerical HSV mask values in the arrays in the below code block
        
  ![](images/sec3image4.PNG)
        
	- Note that there are 2 masks used because our yellow tape contains hues in two different ranges.  If you are not using yellow tape (or if your lighting is different) you may only need one mask
        
  ![](images/sec3image5.PNG)
        
	- Use the feed displaying the edges of your color mask to determine how well your color mask is isolating your lane lines.  Mine looks like this:
        
  ![](images/sec3image6.PNG)
      
- This is an iterative process. Keep repeating and adjusting your color mask until you are happy with the results. 
  * **Fixing a PyRoboCar Bug**
    - If you are using Raspberry Pi 4, your hardware is not recognized/supported by SunFounder’s code, so follow there instruction here and add your Raspberry Pi version to the SunFounder’s code in PCA9685.py:
      -  This file could be in different places, please do a search:
         - find home/pi/* -name ‘PCA9685.py’
       - Add this line of to the supported Raspberry Pi versions in all the PCA9685.py:
         - RPI_REVISION_4_MODULE_B = ["c03111",”c03112”]
    - There is one bug that set the move direction to backward, to fix it:
      - The problem with the picar moving backwards when the py_robo_car.py initiates was solved
        - The line ‘self.back_wheels.forward()’ was added at line 100 in the drive() function
        - The py_robo_car.py was apparently defaulting to moving backwards in the absence of code dictating its direction.
        - Looking at the test() function in the back_wheels.py script, the picar’s wheels were directed to move forward before the wheels were given a speed
  
  <style type="text/css">
#submit {
 background-color: #008080;
 padding: .5em;
 -moz-border-radius: 5px;
 -webkit-border-radius: 5px;
 border-radius: 6px;
 color: #fff;
 align: center;
 font-size: 20px;
 text-decoration: none;
 border: none;
}
#submit:hover {
 border: none;
 background: orange;
 box-shadow: 0px 0px 1px #777;
}
</style>

<form>
<input id='submit' type="BUTTON" value="Section 2" onclick="window.location.href='https://larguncw.github.io/PyRoboCar/pages/section_2'">
</form>

<form>
<input id='submit' style="position: relative; left: 368px; bottom: 45px;" type="BUTTON" value="Homepage" onclick="window.location.href='https://larguncw.github.io/PyRoboCar/'">
</form>

<form>
<input id='submit' style="position: relative; left: 750px; bottom: 93px;" type="BUTTON" value="Section 4" onclick="window.location.href='https://larguncw.github.io/PyRoboCar/pages/section_4'">
</form>
