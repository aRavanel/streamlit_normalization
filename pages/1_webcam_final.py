import streamlit as st
import cv2 as cv2
from PIL import Image
from datetime import date
from datetime import datetime
import numpy as np
import random
from PIL import Image

import src.video_utils_2 as video_utils_2
from src.video_utils_2 import *

import streamlit as st
#CameraThread is a sub-class of threading.Thread

# ===============================================
# params
# ===============================================
st.set_page_config(layout="wide")

# ===============================================
# Globals
# ===============================================
global camera

# ===============================================
# Private functions
# ===============================================
@st.cache(allow_output_mutation=True)
def get_or_create_camera_thread():
    '''
    Restart the thread CameraThread
    '''
    for th in threading.enumerate(): # Returns a list of all thread objects that are currently active.
        if th.name == 'CameraThread':
            th.stop()
            th.join() # The join() waits for threads to terminate.
    cw = video_utils_2.CameraThread(name='CameraThread')
    cw.start() # The start() method starts a thread by calling the run method.
    return cw

@st.cache()
def stop_camera_thread():
    '''
    Stop the thread named CameraThread
    '''
    for th in threading.enumerate(): # Returns a list of all thread objects that are currently active.
        if th.name == 'CameraThread':
            th.stop()
            th.join() # The join() waits for threads to terminate.


# def callback_checkbox_run_webcam():
#     '''
#     checkbox to activate for running webcam
#     '''
#     global camera
#     previousRun = bool(run) # value of run before changing
#     newRun = not previousRun
    
#     # checkbox run OFF -> ON
#     if newRun: 
#         st.session_state['state_cam'] = 'state_cam_ON'
#         camera = get_or_create_camera_thread()

#     # checkbox run ON -> OFF    
#     else:
#         st.session_state['state_cam'] = 'state_cam_OFF'
#         #stop_camera_thread() # shut down every camera thread
#         camera = None
    

 # Button take picture 
def button_takepicture_action():
    '''
    Action of the button taking pictures
    '''
    st.session_state['timestamp']  = str(datetime.now())
    st.session_state['screenshot'] = True
    
    # rotate an image and save it under another name
    # try:
    #     im_pil = Image.open('./resources/images/placeholder.png')
    #     im_pil = im_pil.rotate(random.randint(1,45))
    #     im_pil.save('./resources/images/placeholder2.png')

    # except:
    #     im_pil = Image.open('./resources/images/placeholder.png')
    #     im_pil = im_pil.rotate(random.randint(1,45))
    #     im_pil.save('./resources/images/placeholder2.png')
    # st.session_state['picture'] = Image.open('./resources/images/placeholder2.png')
    # st.session_state['picture_cam']= Image.open('./resources/images/placeholder2.png')
        
def button_normalize_action():
    '''
    Action of the button to normalize
    '''
    a=1
            
 

# Button take picture 
def button_restart_action():
    '''
    Restart function in case of bug
    '''
    global camera
    st.session_state['picture_screenshot'] = st.session_state['picture_placeholder'] # will reinit the screenshot image automatically
    img_placeholder_2.image(st.session_state['picture_screenshot'], caption='screenshot')
    img_placeholder_3.image(st.session_state['picture_screenshot'], caption='screenshot')
    camera = get_or_create_camera_thread()
    

# =============================================
#               Initialize 
# =============================================

camera = get_or_create_camera_thread()

# initialize state
if 'timestamp' not in st.session_state:
    st.session_state['timestamp'] = 'None'
    
if 'state_cam' not in st.session_state:
    st.session_state['state_cam'] = 'None'
        
if 'restart' not in st.session_state:
    st.session_state['restart'] = False

if 'picture_placeholder' not in st.session_state:
    st.session_state['picture_placeholder'] = Image.open('./resources/images/placeholder.png')
    
if 'picture_camfeed' not in st.session_state:
    st.session_state['picture_camfeed'] = st.session_state['picture_placeholder']
    
if 'picture_screenshot' not in st.session_state:
    st.session_state['picture_screenshot'] = st.session_state['picture_placeholder']
    st.session_state['message_screenshot'] = 'please take a picture'
    
if 'screenshot' not in st.session_state:
    st.session_state['screenshot'] = False

# =====================================
# UI 
# =====================================
st.title("Image normalization using GANS")


col_1, col_2, col_3, col_4, col_5 = st.columns((2,1,2,1,2))

with col_1:
    
    st.markdown("**Webcam Live Feed**")
    
    # frame for image
    img_placeholder = st.empty()
    img_placeholder_2 = st.empty()
    
 
with col_2:
    
    st.markdown("")
    st.markdown("")
    st.markdown("")
    
    # checkbox indicating running
    st.button('RESTART', on_click=button_restart_action)

    # button to take picture
    st.button('take picture', on_click=button_takepicture_action)
    
    # some text (currenlty counter running)
    txt_placeholder = st.empty()
    
    
    # some info
    # st.write(st.session_state['state_cam'])
    # st.write(st.session_state['explain_button'])
    
    
with col_3:
    st.markdown("**Face detection**")
    
    # information on picture
    txt_placeholder_screenshot = st.empty() 
    
    # screenshot image
    img_placeholder_3 = st.empty()
   
    #img_placeholder_2.image(st.session_state['picture_screenshot'], caption=st.session_state['explain_image'])

with col_4:
    st.markdown("")
    st.markdown("")
    st.markdown("")
    
    # checkbox indicating running
    st.button('NORMALIZE WITH AI', on_click=button_normalize_action)
    
with col_5:
    
    st.markdown("**Face Normalized**")
    
    st.write('here will go normalized picture')
    
    
# ======================================================================    
# Updating loop to have constant webcam feed refresh
# - python stuck in the loop (but not st elements : theyll keep updating) if not in separate thread
# -> thats why i put it at the end

counter = 0
from src.utils_cv import detect_face

while True:
    counter += 1
    if counter >= 301:
        counter = 0
    
    # update webcam feed
    frame = camera.read()  # update camera
    frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_placeholder.image(frame_RGB)
    
    # update counter to check its alive
    spinner = (counter//20)*'.'
    txt_placeholder.write(spinner) 
    txt_placeholder_screenshot.write(st.session_state['message_screenshot']) 
    
    # when take picture pressed, register image and display it on image
    if st.session_state['screenshot'] == True:
        
        #check if face can be detected
        st.session_state['picture_screenshot'] = frame_RGB # maybe not needed
        img_placeholder_2.image(st.session_state['picture_screenshot'], caption='screenshot')
        bool_detect, cropped = detect_face(st.session_state['picture_screenshot'])
        if bool_detect:
            st.session_state['message_screenshot'] = ' ' # good picture
            img_placeholder_3.image(cropped,  caption='lets use frame : ' + st.session_state['timestamp'] )
            st.session_state['screenshot'] = False
        else:
            st.session_state['message_screenshot'] = 'get closer please'
            
        
        
    # break in case of button restart
    if st.session_state['restart']:
        st.session_state['restart'] = False
        break
    
