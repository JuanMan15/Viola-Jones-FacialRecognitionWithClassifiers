# Viola-Jones Facial Recognition Project

## Overview

This project implements a real-time facial feature detection system using the **Viola-Jones algorithm** and **Haar Cascade classifiers**. It is capable of detecting faces, eyes, noses, and mouths in a live video stream from a webcam.

The system is built using Python and OpenCV, and it includes a stabilization mechanism to reduce flickering in detections across frames.

## Features

-   **Real-time Detection:** Processes video frames from the webcam in real-time.
-   **Multi-Feature Detection:**
    -   **Face:** Detects the frontal face.
    -   **Eyes:** Detects eyes within the face region.
    -   **Nose:** Detects the nose within the central face region.
    -   **Mouth:** Detects the mouth within the lower face region.
-   **Stabilization:** Uses a detection history (`ultima_deteccion`) to maintain bounding boxes even if they are missed in a few frames, providing a smoother visual experience.

## Project Structure

```
.
├── classifiers/          # Custom Haar Cascade XML files (nose, mouth)
├── utils/
│   └── detector.py       # Detection logic (detectar_partes_faciales function)
├── main.py               # Main entry point to run the application
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Prerequisites

-   Python 3.x
-   Webcam

## Installation

1.  **Clone the repository** (if applicable) or download the source code.

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the facial recognition system, run the `main.py` script:

```bash
python main.py
```

-   The application will open a window showing the webcam feed.
-   Detected features will be highlighted with colored shapes:
    -   **Face:** Blue Rectangle
    -   **Eyes:** Green Circles
    -   **Nose:** Yellow Circles
    -   **Mouth:** Magenta Rectangle
-   Press **ESC** to exit the application.

## How it Works

### The Viola-Jones Algorithm

The Viola-Jones object detection framework is the first object detection framework to provide competitive object detection rates in real-time, proposed in 2001 by Paul Viola and Michael Jones.

It uses:
1.  **Haar-like Features:** Simple rectangular features that capture the difference in intensity between adjacent rectangular regions.
2.  **Integral Image:** A data structure that allows for the rapid computation of these features.
3.  **AdaBoost:** A machine learning algorithm that selects a small number of critical features from a large set and combines them into a strong classifier.
4.  **Cascade of Classifiers:** A method to quickly discard background regions of the image, spending more computation on promising face-like regions.

### Implementation Details

-   **`utils/detector.py`:** Contains the core logic.
    -   Loads classifiers at the start of the script.
    -   The `detectar_partes_faciales(frame)` function processes each image.
    -   **Region of Interest (ROI):** To improve performance and accuracy, eyes, nose, and mouth are searched for only within specific regions of the detected face (e.g., eyes in the upper half, mouth in the lower half).
    -   **Stabilization:** A global dictionary `ultima_deteccion` is used to store the coordinates of the last detected features. If a feature is not detected in the current frame, the previous coordinates are used (or not drawn if the face is lost), reducing flickering.

## Troubleshooting

-   **Camera not opening:** Ensure your webcam is connected and not being used by another application.
-   **Classifiers not found:** Ensure the `classifiers/` directory contains `haarcascade_mcs_nose.xml` and `haarcascade_mcs_mouth.xml`. The face and eye classifiers are loaded directly from OpenCV's built-in data.

## License

This project is open-source and available for educational purposes.
