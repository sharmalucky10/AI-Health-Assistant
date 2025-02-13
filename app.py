import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load the text generation model
chatbot = pipeline("text-generation", model="distilgpt2")

def Healthcare_chatbot(user_input):
    # Check for specific healthcare-related queries
    if "symptom" in user_input:
        return "Please consult a doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like to schedule a doctor's appointment?"
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly. If you have concerns, consult your doctor."
    else:
        # Generate chatbot response if no healthcare-specific keywords found
        response = chatbot(user_input, max_length=500, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Health Care Assistant")
    
    # Get user input
    user_input = st.text_input("How can I help you today?")
    
    if st.button("Submit"):
        if user_input:
            # Display user input
            st.write("User:", user_input)
            
            with st.spinner("Processing your query, please wait..."):
                # Get healthcare response if applicable
                healthcare_response = Healthcare_chatbot(user_input)
                
                # Display the healthcare assistant's response
                st.write("Healthcare Assistant:", healthcare_response)
        else:
            st.write("Please enter a message to get a response.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
