# Import packages
from groq import Groq
import base64
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Initialize client and model
client = Groq()
llava_model = 'llava-v1.5-7b-4096-preview'

# Define image encoding function
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Define image to text function for a single image
def image_to_text(client, model, base64_image, prompt, optional_context=None):
    if optional_context:
        prompt = f"{prompt}\n\nContext: {optional_context}"
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        model=model
    )

    return chat_completion.choices[0].message.content

# Define function to process multiple images
def process_multiple_images(client, model, image_paths, prompt, optional_context=None):
    all_results = []
    
    # Process each image
    for i, image_path in enumerate(image_paths):
        base64_image = encode_image(image_path)
        result = image_to_text(client, model, base64_image, prompt, optional_context)
        all_results.append(result)
    
    # Combine all results with formatting
    combined_result = "\n\n"  # Start with a newline for separation
    for i, result in enumerate(all_results):
        combined_result += f"--- Image {i+1} Result ---\n"
        combined_result += f"{result}\n"
        combined_result += "\n"  # Add extra space between results
    
    return combined_result


# # Example usage
# image_paths = [
#     '/Users/nikhilkushwaha/Desktop/testing_redbus/1.png', 
#     '/Users/nikhilkushwaha/Desktop/testing_redbus/2.png', 
#     '/Users/nikhilkushwaha/Desktop/testing_redbus/3.png',
#     '/Users/nikhilkushwaha/Desktop/testing_redbus/4.png', 
#     '/Users/nikhilkushwaha/Desktop/testing_redbus/5.png', 
#     '/Users/nikhilkushwaha/Desktop/testing_redbus/6.png', 
#     '/Users/nikhilkushwaha/Desktop/testing_redbus/7.png'
# ]  # List of image paths

# prompt = """You are an AI assistant specialized in generating detailed testing instructions for any type of application feature.
#     You will be provided with a screenshot that may represent a mobile, web, or desktop application, and optionally, some context to guide the process.
#     Your task is to analyze the screenshot and generate detailed test cases for the feature you identify along with capturing all the neccasary Details.
    
#     For each feature, provide the following:
#     1. **Description**: A brief summary of what the test case is about and what functionality is being tested.
#     2. **Pre-conditions**: Any setup or requirements that need to be in place before testing.
#     3. **Testing Steps**: Clear, step-by-step instructions on how to perform the test.
#     4. **Expected Result**: What should happen if the feature works correctly.

#     Analyze the provided screenshot and describe the feature or functionality it represents. Then, generate the detailed test case using the format above."""

# optional_context = "This application is for booking bus tickets, and the screenshots show different steps in the ticket booking process."

# # Process all images and generate final combined result
# final_result = process_multiple_images(client, llava_model, image_paths, prompt, optional_context)
# print(final_result)
