# Deepfake Detector - Django Project

## Overview:
This is a **Deepfake Detector** built with **Python Django**. It allows users to upload media (images or videos), which is then analyzed using a **dummy AI model** to detect whether it’s a deepfake or not. The system also shows a heatmap visualizing the manipulated areas.

## Features:
- **User Upload**: Users can upload images or videos for analysis.
- **Deepfake Detection**: The system predicts whether the uploaded media is **real** or **fake** with a confidence score.
- **Heatmap**: A heatmap is generated to visualize the manipulated areas of the media.
- **Spinning Loader**: A professional **spinner** appears while the media is being analyzed.
- **Django Backend**: The backend is built using **Django** with all required functionality for upload, processing, and displaying results.
- **Interactive GUI**: The system provides an interactive and user-friendly interface.

## Project Structure:
- **Frontend**: HTML, CSS (with spinner animation for professional loading experience)
- **Backend**: Python Django (views, model, settings, and routing)
- **AI Model**: Dummy model to simulate prediction of media (for the purpose of this project)
- **Heatmap**: Generated using **Matplotlib** to visualize manipulation regions.

## Setup Instructions:
1. **Clone or download** the project.
2. **Install dependencies**:
   ```bash
   pip install django matplotlib numpy
   ```
3. **Run the server**:
   ```bash
   python manage.py runserver
   ```
4. **Access the application** in a browser:
   - Open `http://127.0.0.1:8000/` to use the upload and detection interface.

## How to Use:
- Go to the upload page, select a media file (image/video).
- Click **Upload and Analyze**.
- Wait for the system to analyze the media and display the result (prediction and heatmap).

## Conclusion:
This project demonstrates the potential of AI and Django for building a **Deepfake Detector** system with an interactive web interface. The **spinner** enhances the user experience, making it feel smooth and professional during analysis.

## Author:
Your Name / Student Project
