# VirtualWebcam
This python code permit the user to use the IpWebcam app (Android) with the OBS Virtual Camera.

# How to install
You need to have python installed.

1. Download this Github repository.
2. Make sure to install all the following modules (by doing 'pip install module_name') :
    - pygame
    - numpy
    - pygame_widgets
    - pyvirtualcam
    - ipwebcam
3. You also need to have OBS installed (for the virtual camera).
4. Extract the repository (or go in the file if you used 'git' method).

# How to use
1. Install the app IpWebcam (by Pavel Khlebovich) on your Android device.
2. Open the app and click on 'Start the server' (or something like that).
3. You will have an address, copy it somewhere.
4. Open 'main.py' inside the directory of the repository, in line 16, replace the ADDRESS:PORT in brackets by what you saved in step 3 (Don't change anything else!).
5. Open a console in the directory of the repository.
6. Type 'python main.py' and enter !
7. You can now use OBS Virtual Camera.

# Features (Current version : v1.0.0)
- You can use the IpWebcam app as a webcam for your computer
- Panel with currently only a slider that let you zoom in-out

# Planned features
[] A better 

# Resources used
Of course, I didn't figured that code out all by myself, thanks to smarter people on the Internet this project exists :
[PyVirtualCam] (https://stackoverflow.com/questions/63475061/how-to-make-a-virtual-camera-with-python)
[IpWebcamModule Code Example] (https://pypi.org/project/ipwebcam/)