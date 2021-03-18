import sys
import pygame
from ipwebcam import *
import pyvirtualcam
import numpy as np
from pygame_widgets import Slider
from script_utils import clamp

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))

slider = Slider(screen, 50, 50, 300, 20, min=0, max=8, step=1, initial=0)

ipcam = IPWEBCAM('192.168.1.25:8080') #Server adress of the ipwebcam (don't add 'http://' before) => ADRESS:PORT
ipcam.set_resolution("4") #Set the ipwebcam resolution to 640x480

zoom_factor = 0

run = True
with pyvirtualcam.Camera(width=640, height=480, fps=30) as cam:
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            #elif event.type == pygame.KEYDOWN:
        
        zoom_factor = clamp(slider.getValue(), 0, 8) #Clamp the zoom factor [0, 8]
        ipcam.zoom(zoom_factor) #Set the zoom to the zoom factor
        
        img = ipcam.get_pygame_image() #Convert the ipwecam image flux into an pygame image
        img = pygame.transform.scale(img, (640, 480)) #Re-scale the image to be 640x480

        screen.fill((255, 255, 255))

        slider.listen(events)
        slider.draw()
        
        pygame.display.update()
        clock.tick(0)
        
        imgdata = pygame.surfarray.array3d(img) #Convert the pygame image into a numpy array data
        imgdata = np.swapaxes(imgdata,0,1) #Rotate the camera to be in the right position
        
        cam.send(imgdata)
        cam.sleep_until_next_frame()
        cam.sleep_until_next_frame()