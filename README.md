# Hand and Face Mesh Tracking Application 👋🤳

This project utilizes OpenCV and MediaPipe to track and display hand and face landmarks in real-time from a webcam feed. The application processes each video frame to detect and draw landmarks for both the hands and face, providing a detailed visualization of these features. The project allows users to interact with the system through hand gestures and view face mesh data. ✋👤

## Features ✨
- **Hand Tracking** 🖐: Detects and visualizes hand landmarks (including fingertips) in real-time.
- **Face Mesh Tracking** 😄: Detects and visualizes facial landmarks with an offset for better viewing.
- **Customizable Configuration** ⚙️: Various parameters like video source, confidence thresholds, and tracking settings can be configured via a YAML configuration file.

## Technologies Used 🛠
- **Python** 🐍: The primary language for the application.
- **OpenCV** 🖥: Used for video capture and image processing.
- **MediaPipe** 🔮: Used for hand and face mesh landmark detection.
- **YAML** 📄: Used to load the configuration settings.

## Installation 🚀
1. Clone this repository:
   ```bash
   git clone https://github.com/Syam-1133/Face-Mesh-Tracking-Application
   cd hand-face-mesh-app
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should include:
   ```text
   opencv-python
   mediapipe
   pyyaml
   ```

3. Ensure you have a webcam connected to your system. 📸

## Configuration ⚙️
The application reads a configuration file (`config.yaml`) for customizable settings. Example configuration:

```yaml
video_source: 0  
min_detection_confidence: 0.5
min_tracking_confidence: 0.5
face_min_detection_confidence: 0.5
face_min_tracking_confidence: 0.5
```

- `video_source`: Index of the video source (usually 0 for the default webcam).
- `min_detection_confidence`: Minimum confidence for detection (range: 0 to 1).
- `min_tracking_confidence`: Minimum confidence for tracking (range: 0 to 1).
- `face_min_detection_confidence`: Minimum confidence for face detection.
- `face_min_tracking_confidence`: Minimum confidence for face tracking.

## Usage 🎮
1. Ensure your webcam is properly set up.
2. Edit the `config.yaml` file to set your desired configuration.
3. Run the application:
   ```bash
   python app.py
   ```

   The video feed will appear with the hand and face landmarks drawn. Press 'q' to exit the application. 🚪

## Code Explanation 📚

### Class: `HandFaceMeshApp` 🖥
The main class that handles the video processing, hand and face mesh detection, and visualization.

#### `__init__(self, config_path)`
- Loads the configuration settings from the provided YAML file.
- Initializes the webcam capture and MediaPipe solutions for hand and face mesh detection.
- Sets up drawing specifications for hand and face landmarks.

#### `process_frame(self, image)`
- Processes each frame from the video feed.
- Converts the frame to RGB (required by MediaPipe).
- Detects and processes hand and face landmarks.
- Calls the respective drawing functions for hands and faces.

#### `draw_hand_landmarks(self, image, hand_results)`
- Draws hand landmarks on the image.
- Highlights fingertips with white circles.
- Uses MediaPipe’s drawing utilities to render the hand connections.

#### `draw_face_landmarks(self, image, face_results)`
- Draws face landmarks with an offset to move the landmarks further right.
- Adds thicker lines for the connections between face landmarks for better visualization.

#### `run(self)`
- Main loop for processing video frames.
- Continuously captures frames from the webcam, processes them, and displays the results.
- Waits for the user to press 'q' to exit.

## Contributing 🤝
Feel free to fork this repository and submit pull requests for improvements or additional features.

#