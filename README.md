# Real-time Horse Detection and Tracking with YOLOv8 and Streamlit

Welcome to my project, which was completed and done for the ministry of sport at horse jumping detection! In this fascinating project, i explore the worlds of artificial intelligence and computer vision to create a system that can automatically detect and evaluate horses and riders during jumping competitions in the British Sport organisation. In addition to being an entertaining equestrian sport, horse jumping is a discipline that calls for accuracy, technique, and safety.
I have used the cutting-edge YOLO (You Only Look Once) algorithm in this project because of its accuracy and speed in real-time object recognition. I can detect several objects using the YOLO method in a single run through the neural network, which makes it perfect for applications that need real-time monitoring and immediate response, like horse jumping competitions and also streamlit for visualization.


## Requirements
Python 3.6+
Streamlit
YOLOv8

## Installation Steps

You are advised to create a python environment for this project to avoid problems with conflicting versions of dependencies. You may use 'venv' or 'conda'. See example below:

- Clone the repository: git clone https://github.com/Odigie43/horse-jumping-detection.git
- Change to the repository directory: `cd horse-jumping-detection`
- To make it easy for you to test out this project, we have included the `weights`, `videos`, and `images` foldrs in this repository. These folders contains the custom trained Yolov8 model as well as the orginal yolov8 model. There are sample videos and images in the respective folders.
- The Original pre-trained YOLOv8 weights was downloaded from (<https://githubo.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt>) and saved in the `weights` directory. 

## PIP ENV HANDLING

Python -m venv <virtual-environment-name>
Python -m venv venv

## ACTIVATION
unix: source env/bin/activate
win:  venv/Scripts/activate.bat //In CMD
      venv/Scripts/Activate.ps1 //In Powershe

## DEACTIVATION
deactivate

## INSTALL REQUIREMENTS
```bash
pip install ultralytics streamlit youtube-dl pafy
```
Or use

```bash
 pip install -r requirements.txt
 ```

# Models Used
All our models are stored in the `weights` folder.
- yolov8n-seg.pt was used for segmentation
- yolov8n.pt was used for detection.
- Our custom trained model is named best.pt
- The custom dataset used for training is in the `train` folder

## How to run the Project

- Open the project folder in your terminal of choice, we used windows Terminal
- Run the app with the following command: `streamlit run app.py`
- If the above command fails, try the following command: `python -m streamlit run app.py`
- The app should open in a new browser window.

### ML Model Config

- Select task (Detection, Segmentation)
- Select model confidence
- Use the slider to adjust the confidence threshold (25-100) for the model.

One the model config is done, select a source.

### Detection on images

- The default image with its objects-detected image is displayed on the main page.
- Select a source. (radio button selection `Image`).
- Upload an image by clicking on the "Browse files" button.
- Click the "Detect Objects" button to run the object detection algorithm on the uploaded image with the selected confidence threshold.
- The resulting image with objects detected will be displayed on the page. Click the "Download Image" button to download the image.("If save image to download" is selected)

## Detection in Videos

- Create a folder with name `videos` in the same directory
- Dump your videos in this folder
- In `settings.py` edit the following lines.

```python
# video
VIDEO_DIR = ROOT / 'videos' # After creating the videos folder

# Suppose you have four videos inside videos folder
# Edit the name of video_1, 2, 3, 4 (with the names of your video files) 
VIDEO_1_PATH = VIDEO_DIR / 'video_1.mp4' 
VIDEO_2_PATH = VIDEO_DIR / 'video_2.mp4'
VIDEO_3_PATH = VIDEO_DIR / 'video_3.mp4'
VIDEO_4_PATH = VIDEO_DIR / 'video_4.mp4'

# Edit the same names here also.
VIDEOS_DICT = {
    'video_1': VIDEO_1_PATH,
    'video_2': VIDEO_2_PATH,
    'video_3': VIDEO_3_PATH,
    'video_4': VIDEO_4_PATH,
}

# Your videos will start appearing inside streamlit webapp 'Choose a video'.
```

- Click on `Detect Video Objects` button and the selected task (detection/segmentation) will start on the selected video.

## Acknowledgements

This app is based on the YOLOv8(<https://github.com/ultralytics/ultralytics>) object detection algorithm. The app uses the Streamlit(<https://github.com/streamlit/streamlit>) library for the user interface. https://github.com/CodingMantras/yolov8-streamlit-detection-tracking.git was a great inspiration for the streamlit interface.

### Disclaimer Notice

Please note that this project is intended for educational purposes only and must never be used in a production environments.

