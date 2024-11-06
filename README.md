# Video - Automation-

Step-by-Step Guide:

1. Clone the Repository First, clone your repository to your local machine:
git clone https://github.com/shikha-srivastava/Automated_Assessment.git
cd Automated_Assessment
2. Set Up a Virtual Environment It’s best practice to use a virtual environment to manage dependencies:

python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

3. Install Dependencies Use pip to install the required packages from the requirements.txt file:

pip install -r requirements.txt

4. Please Run test by using marker -  pytest -v -s -m "Autoamated_video", marker is defined under pytest.ini file








Automation Assignment: Video Playback and Control Using Selenium
Objective: The goal of this assignment is to evaluate your ability to automate a web-based
video platform using Python and Selenium. You will automate a sequence of steps involving
video selection, playback control, volume adjustment, resolution changes, and logout
functionality. Each step has a point value assigned, and you are required to submit a demo
video of your script in action.
Instructions:
Using Python and Selenium, write a script to automate the following tasks on the provided
web platform:
Platform URL: [FYC Link](https://indeedemo-fyc.watch.indee.tv/)
PIN: WVMVHWBS
1. Sign in to the Platform.
   - Log in using the provided FYC link and PIN.
   - Points: 5
   2. Navigate to the 'Test Automation Project':
   - After logging in, navigate to the "All Titles" screen.
   - Locate and click on the Test automation project.
   - Points: 5
   3. Switch to the 'Details' Tab:
   - When the project opens, the Videos tab will be active by default.
   - Click on the Details tab and wait for 5-10 seconds.
   - Points: 5
   4. Return to the 'Videos' Tab:
   - Switch back to the Videos tab.
   - Points: 5
   5. Play the Video:
   - Locate the video on the page and click play.
   - Allow the video to play for 10 seconds, then pause it.
   - Points: 10

   6. Replay the Video using the 'Continue Watching' button:
   - Use the Continue Watching button to resume playback.
   - Points: 5
   7. Adjust Volume:
   - Set the video volume to 50%.
   - Points: 5
   8. Change Video Resolution:
   - Open the settings menu and change the video resolution to 480p.
   - Then, change the resolution back to 720p.
   - Points: 10
   9. Pause and Exit:
   - Pause the video after adjusting the resolution.
   - Press the Back button at the top of the screen to navigate out of the project. -
   Points: 5
   10. Logout:
   - Locate and click the Logout button to sign out from the platform.
   - Points: 5
   Deliverables:
   1. Automation Script:
   - Your Python Selenium script automating the steps mentioned above.
   - Your code should be clean and well-commented to explain each step.
   2. Demo Video:
   - Record a short demo video showing your script running and performing the required
   tasks.
   - The video should clearly show each of the steps in the automation sequence.
   3. Submission:
   - Submit your Python script (.py file) and the demo video file (.mp4 or similar format).
   - Make sure the video demonstrates the completion of each step.

