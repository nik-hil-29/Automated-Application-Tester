import os
from groq import Groq
from dotenv import load_dotenv
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from model import process_multiple_images  # Import your backend code

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Initialize client and model
client = Groq()
llava_model = 'llava-v1.5-7b-4096-preview'
app = Flask(__name__)

# Define the directory to store uploaded files temporarily
UPLOAD_FOLDER = 'myracle.io_project'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process-images', methods=['POST'])
def process_images():
    # Get the uploaded files and optional context
    files = request.files.getlist('images')
    optional_context = request.form.get('context')

    # Save and process images one by one
    image_paths = []
    for file in files:
        filename = secure_filename(file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image_path)
        image_paths.append(image_path)

    # Prepare the prompt
    prompt = """
    You are an AI assistant specialized in generating detailed testing instructions for any type of application feature. You will be provided with a screenshot representing a mobile, web, or desktop application, and optionally, some context to guide the process.

Your task is to analyze the screenshot, identify the key feature or functionality being represented, and generate comprehensive test cases that can be used to validate the correct behavior of the feature.

When writing the test cases, follow the structure below for each feature:

Description: A brief summary of what the test case is about and what functionality is being tested.
Pre-conditions: Any setup or requirements that need to be in place before testing.
Testing Steps: Clear, step-by-step instructions on how to perform the test.
Edge Cases: Consider edge cases that could break the functionality.
Expected Result: What should happen if the feature works correctly.
Example 1: E-commerce Product Checkout
Input: A screenshot of the checkout page from an e-commerce website.

Generated Test Case:

Description: Verify that the user can complete a purchase through the checkout page.
Pre-conditions:
The user has added items to their shopping cart.
The user is logged into their account.
Testing Steps:
Navigate to the checkout page.
Verify that the list of items in the cart is correct.
Enter shipping address details.
Select a payment method (e.g., credit card, PayPal).
Review the order summary and apply any discount codes if available.
Click the "Place Order" button.
Edge Cases:
Attempt to proceed without entering the shipping address.
Apply an expired discount code.
Expected Result:
The order confirmation page should be displayed with a summary of the order details.
The order should be processed, and the user should receive a confirmation email.
Example 2: Social Media Post Creation
Input: A screenshot of the post creation screen from a social media platform.

Generated Test Case:

Description: Verify that the user can create and publish a post on the social media platform.
Pre-conditions:
The user is logged into their social media account.
Testing Steps:
Navigate to the post creation screen.
Enter text into the post body field.
Add an image or video to the post if applicable.
Tag other users or add hashtags.
Select the audience for the post (e.g., public, friends).
Click the "Publish" button.
Edge Cases:
Attempt to publish without any content (text or media).
Add invalid hashtags or tags.
Expected Result:
The post should appear on the user’s profile and in the feeds of tagged users or selected audience.
The post should be visible with the correct content and media.
Example 3: Banking Mobile App Funds Transfer
Input: A screenshot of the funds transfer screen from a banking mobile app.

Generated Test Case:

Description: Verify that the user can successfully transfer funds between accounts.
Pre-conditions:
The user is logged into their banking app.
The user has sufficient balance in the source account.
Testing Steps:
Navigate to the funds transfer screen.
Select the source account and destination account.
Enter the amount to transfer.
Provide any required additional information (e.g., transfer notes).
Review the transfer details.
Confirm the transfer by entering any required authentication (e.g., PIN, OTP).
Edge Cases:
Attempt to transfer an amount exceeding the available balance.
Input an invalid account number.
Expected Result:
The transfer should be processed successfully, and the user should see a confirmation message.
The balance of the source and destination accounts should be updated accordingly.
    """

    # Process the images and get the results from the model
    result = process_multiple_images(client, model=llava_model, image_paths=image_paths, prompt=prompt, optional_context=optional_context)

    # Return the result as a response
    return result

if __name__ == '__main__':
    app.run(debug=True)
