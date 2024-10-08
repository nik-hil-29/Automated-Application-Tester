# Automated Application Tester


This project is a tool that uses a multimodal large language model (LLM) to automatically generate detailed test cases for any digital product's features based on screenshots. The goal of this tool is to assist testers by analyzing screenshots of an application's user interface (UI) and generating testing instructions in a structured format.

# Features

Image Upload: A simple web page that allows users to upload multiple screenshots and optionally provide context for the testing.
Multimodal LLM Integration: Utilizes the LLaVA (Large Language and Vision Assistant) model to extract and describe UI elements from the screenshots.
Test Case Output: The tool generates test cases with:
Description: Explanation of what each test case is testing.
Pre-conditions: Conditions that must be met before running the test.
Testing Steps: Step-by-step instructions for performing the test.
Expected Results: The expected outcome if the feature works as intended.

# Project Structure

Frontend: Allows users to upload screenshots and optional text context.
Backend: Processes the images using the LLaVA model to generate descriptions, which are passed  for classification and test case generation.
Multimodal Processing: The LLaVA model processes both image and text inputs to understand the UI elements and generate a human-readable description of what the screenshot contains.
#How It Works

Image Upload: Users upload multiple screenshots (e.g., mobile app UI) and optionally provide some context.
LLaVA Model: The screenshots are processed using the LLaVA model to generate textual descriptions of the UI elements.
LangGraph Agents: The first agent classifies the extracted information, and subsequent agents generate detailed test cases based on pre-defined test templates.
Test Case Generation: The tool outputs detailed testing instructions, including pre-conditions, steps, and expected results.
# Tech Stack

Frontend: HTML, CSS, JavaScript (optional React).
Backend: Python with Flask/FastAPI.
Multimodal Model: HuggingFace LLaVA (liuhaotian/LLaVA-13B-v0).
LangGraph: For handling the logic of multi-agent collaboration.
Setup Instructions

# Clone the repository.
Install the required dependencies:
pip install -r requirements.txt
Run the application:
python app.py
Open the web page at http://localhost:5000, upload your screenshots, and see the generated testing instructions.
# Example Use Case

The tool can be used to generate testing instructions for apps like Red Bus. You can upload screenshots of the following features for testing:

Source, Destination, and Date Selection
Bus Selection
Seat Selection
Pick-up and Drop-off Point Selection
Offers and Discounts
# You can checkout the explanation of the project here : https://www.loom.com/share/45f0873642c34501b7a0892efa90514f?sid=c9293847-799a-43c0-9ffc-18ee5020ca2f
# Screenshots:
<img width="1410" alt="Screenshot 2024-09-08 at 1 24 03 AM" src="https://github.com/user-attachments/assets/f95c25bf-8e49-4d29-9705-593aed5ead22">

<img width="1436" alt="Screenshot 2024-09-08 at 1 25 03 AM" src="https://github.com/user-attachments/assets/c5c895d5-313b-4c91-9be8-c12c901e49e4">

<img width="1399" alt="Screenshot 2024-09-08 at 1 25 12 AM" src="https://github.com/user-attachments/assets/f23fd9f5-eddb-4589-bac0-6b029bb58c63">

<img width="1417" alt="Screenshot 2024-09-08 at 1 25 28 AM" src="https://github.com/user-attachments/assets/d48916b4-12bf-4c1c-a2fb-206903b92a5a">

<img width="1409" alt="Screenshot 2024-09-08 at 1 25 38 AM" src="https://github.com/user-attachments/assets/66a51903-d74a-45fd-8c3a-26f5ad5e9bec">


