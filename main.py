# Import necessary libraries
import cv2
from cvzone import cornerRect
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller
import keyboard_customization as kc


# Set colors for keys from customization file
key_color=kc.key_color
key_text_color=kc.key_text_color
touched_key_color=kc.touched_key_color
clicked_key_color=kc.clicked_key_color


# Initialize video capture from the default camera
vid = cv2.VideoCapture(0)
vid.set(3, 640)
vid.set(4, 480)


# Define keyboard layout
keyboard_keys = kc.keys


# Initialize key list and clicked text
key_list = []
clicked_text=""


# Initialize keyboard controller and hand detector
# keyboard=Controller()
detector = HandDetector(detectionCon=0.8)


# Define a class for keys
class Key():
    def __init__(self, pos, text, size=[50, 50]):
        self.pos = pos
        self.text = text
        self.size = size


# Function to draw the keyboard on the image
def draw_keyboard(img,key_list):
    overlay = img.copy()  # Create a copy of the image to draw the keyboard on
    for key in key_list:
        x, y = key.pos
        w, h = key.size
        cv2.rectangle(overlay, (x+10, y), (x+w+10, y+h), key_color, cv2.FILLED)
        cv2.putText(overlay, key.text, (x + 15, y + 42),cv2.FONT_HERSHEY_PLAIN, 3, key_text_color, 2)
        cornerRect(overlay,(x+5,y,w+5,h+5),10,2,1, (255,255,255),(0,0,255))

    # Blend the original image with the overlay with a transparency of 80%
    alpha=0.8
    img = cv2.addWeighted(overlay, 0.7, img, 1-alpha, 0)

    return img

# Create keys and add them to the key list
for y in range(len(keyboard_keys)):
        for x, key in enumerate(keyboard_keys[y]):
            key_list.append(Key([(60 * x)+10, (60*y)+50], key))


# Main loop
while True:
    
    # Read frame from the video
    success, img = vid.read()
    
    # Flip the image
    img = cv2.flip(img, 1)
    if not success:
        break

    
    # Detect hands in the image
    img = detector.findHands(img)
    lmlist, bboxInfo = detector.findPosition(img)
    
    # Draw the keyboard on the image
    img=draw_keyboard(img,key_list)
    if lmlist:
        for key in key_list:
            x,y=key.pos
            w,h=key.size
            
            # If the key is touched
            if x<lmlist[8][0]<x+w and y<lmlist[8][1]<y+h:
                
                # Highlight the key
                cv2.rectangle(img, (x+5, y-5), (x+w+15, y+h+5), touched_key_color, cv2.FILLED)
                cv2.putText(img, key.text, (x + 13, y + 42),cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)
                
                # Find the distance between the thumb and the index finger
                dist,_,_=detector.findDistance(8,12,img,draw=False)
                
                # If the distance is less than 25, press the key
                if dist<30:
                    # keyboard.press(key.text)
                    clicked_text+=key.text
                    
                    # Show the pressed key in a different color
                    cv2.rectangle(img, (x+10, y), (x+w+10, y+h), clicked_key_color, cv2.FILLED)
                    cv2.putText(img, key.text, (x + 13, y + 42),cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 255), 2)
                    sleep(0.4)
    
    # Show the clicked text on the image
    cv2.rectangle(img, (50,300), (570,350), (255, 255, 255), cv2.FILLED)
    cv2.putText(img, clicked_text, (58 , 342),cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 2)
    
    # Show the image
    cv2.imshow("Virtual Keyboard", img)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break