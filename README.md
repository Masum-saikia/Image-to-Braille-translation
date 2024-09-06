# Image Captioning with Braille Output

This project creates a web application that captures images, generates captions for them using the BLIP (Bootstrapped Language-Image Pretraining) model, and converts those captions into Braille. The application is built using Streamlit for the user interface and Python for processing.

## Project Overview

**Objective:** Develop an accessible tool that allows users to capture images, get descriptive captions, and convert those captions into Braille.

**Technologies Used:**
- **Streamlit:** Framework for building the web app.
- **BLIP (Bootstrapped Language-Image Pretraining):** Model for generating image captions.
- **Python:** Programming language used for the project.

## Features

- Capture images using a built-in camera interface.
- Generate captions for captured images.
- Convert captions into Braille.
- Simple and user-friendly interface.

## Installation

To set up and run this project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/image-captioning-braille.git
cd image-captioning-braille
```
2. Create a Virtual Environment
```bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```
3. Install Dependencies
```bash
Copy code
pip install -r requirements.txt
```
4. Download Pre-trained Model
The BLIP model will be downloaded automatically when you first run the app. Ensure you have internet access for this step.

Usage
To run the Streamlit application, execute the following command:

```bash
Copy code
streamlit run app.py
```
This will start the Streamlit server and open the app in your default web browser. You can then use the camera input to capture images, view the generated captions, and see their Braille representations.

Code Overview
app.py: The main script that runs the Streamlit app, handles image capture, processes images using the BLIP model, and converts captions to Braille.
requirements.txt: Contains a list of Python packages required for the project.
Example
Open the app and capture an image.
The app will display the image and generate a caption.
The caption will be converted into Braille and displayed below the caption.
Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements. Please ensure that your contributions adhere to the project's coding standards.

License
This project is licensed under the MIT License - see the LICENSE file for details.
