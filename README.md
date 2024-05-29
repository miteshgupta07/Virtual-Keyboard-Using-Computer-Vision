# Virtual Keyboard using Computer Vision

This project implements a virtual keyboard using computer vision techniques to detect hand gestures and simulate key presses. The application uses OpenCV for video capture and hand detection, and it allows for customization of the keyboard appearance and behavior through a separate configuration file.

## Features
- Hand detection and tracking using the `cvzone` library
- Customizable keyboard layout and colors
- Visual feedback for key touches and presses
- Real-time display of typed text
  
![Screenshot (194)](https://github.com/miteshgupta07/Virtual-Keyboard-Using-Computer-Vision/assets/111682782/c81905d7-c955-464f-9d8c-32a1830b06cd)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/miteshgupta07/Virtual-Keyboard-Using-Computer-Vision.git
    cd virtual-keyboard
    ```

2. Install the required libraries:
    ```sh
    pip install requirements.txt
    ```

## Usage
1. Run the `virtual_keyboard.py` script:
    ```sh
    python virtual_keyboard.py
    ```

2. The application will open a window displaying the video feed from your webcam with the virtual keyboard overlayed.

3. Use your index finger to point at the keys and touch them. When the middle and index finger come close together, the key will be registered as pressed.

4. Press the 'q' key on your physical keyboard to exit the application.
