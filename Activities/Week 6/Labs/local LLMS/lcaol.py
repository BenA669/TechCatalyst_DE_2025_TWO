
from ollama import chat

model = 'mollm2:135m'

# Function to generate an email
def generate_email(subject, recipient_name, additional_info):
    # Step 1: Create the prompt to guide the AI in generating the email
    prompt = f"Write a professional email to {recipient_name} with the subject '{subject}'. Include the following information: {additional_info}"
    
    # Step 2: Call the OpenAI API to generate the email
    # Hint: Use the 'chat' endpoint to create a completion based on the prompt
    response = chat(
        model= model, 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    
    # Step 3: Extract and return the generated email content from the API response
    return #YOURCODE # <-- Complete this line to get the email content

# Function to start the email writing assistant
def email_writing_assistant():
    print("Welcome to the Email Writing Assistant!\n")
    
    # Step 4: Gather user input for the email subject, recipient name, and additional information
    subject = input("Input subject") 
    recipient_name = input("Input Recipient ")
    additional_info = input("Input additional info")
    
    # Step 5: Call the 'generate_email' function and display the generated email
    email = generate_email(subject, recipient_name, additional_info)
    print(f"Email:\n{email}")

# Start the email writing assistant
email_writing_assistant()