"""
Mental Health Chatbot - Main Application

This application provides an AI-powered chatbot interface for mental health support.
Built with Gradio and Hugging Face's Qwen model for intelligent conversations.

Author: Your Name
Date: 2026-09-18
License: MIT
"""

import gradio as gr
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Hugging Face Inference Client
# Get token from environment variable for security
hf_token = os.getenv("HF_TOKEN")

# Using Qwen 2.5-72B-Instruct model - a powerful, freely accessible model
# You can replace this with any compatible Hugging Face model
client = InferenceClient("Qwen/Qwen2.5-72B-Instruct", token=hf_token)


def respond(
    message,
    history: list[tuple[str, str]],
    system_message,
    max_tokens,
    temperature,
    top_p,
):
    """
    Generate AI response for user message.
    
    Args:
        message (str): User's input message
        history (list): Conversation history as list of (user, assistant) tuples
        system_message (str): System prompt defining bot behavior
        max_tokens (int): Maximum length of response
        temperature (float): Controls randomness (0.1-4.0)
        top_p (float): Controls diversity via nucleus sampling (0.1-1.0)
    
    Yields:
        str: Streaming response from the AI model
    """
    # Build message list with system prompt and conversation history
    messages = [{"role": "system", "content": system_message}]

    # Add conversation history
    for val in history:
        if val[0]:
            messages.append({"role": "user", "content": val[0]})
        if val[1]:
            messages.append({"role": "assistant", "content": val[1]})

    # Add current user message
    messages.append({"role": "user", "content": message})

    response = ""

    # Stream response from the model
    for message in client.chat_completion(
        messages,
        max_tokens=max_tokens,
        stream=True,
        temperature=temperature,
        top_p=top_p,
    ):
        # Check if response contains valid content
        if message.choices and message.choices[0].delta.content:
            token = message.choices[0].delta.content
            response += token
            yield response

"""
Create Gradio ChatInterface with customizable parameters.
For more customization options, see: https://www.gradio.app/docs/chatinterface
"""
demo = gr.ChatInterface(
    respond,
    additional_inputs=[
        gr.Textbox(
            value="You are a friendly and empathetic mental health support chatbot. Provide helpful, supportive, and non-judgmental responses.",
            label="System message",
            placeholder="Define the chatbot's personality and behavior..."
        ),
        gr.Slider(
            minimum=1,
            maximum=2048,
            value=512,
            step=1,
            label="Max new tokens",
            info="Maximum length of the response"
        ),
        gr.Slider(
            minimum=0.1,
            maximum=4.0,
            value=0.7,
            step=0.1,
            label="Temperature",
            info="Controls randomness: lower = more focused, higher = more creative"
        ),
        gr.Slider(
            minimum=0.1,
            maximum=1.0,
            value=0.95,
            step=0.05,
            label="Top-p (nucleus sampling)",
            info="Controls diversity of responses"
        ),
    ],
    title="🧠 Mental Health Support Chatbot",
    description="An AI-powered assistant for mental health support and wellness guidance. Remember: This is not a substitute for professional help.",
    theme="soft",
    examples=[
        ["I'm feeling stressed lately. What are some good coping strategies?"],
        ["How can I improve my sleep quality?"],
        ["Give me tips for building confidence"],
        ["What are some mindfulness exercises I can try?"],
    ],
    cache_examples=False,
)


if __name__ == "__main__":
    # Launch the application
    # Set share=True to create a public link
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False
    )