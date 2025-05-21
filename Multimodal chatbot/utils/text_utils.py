# from google.generativeai import GenerativeModel

# def generate_text(prompt):
#     model = GenerativeModel('gemini-pro')
#     response = model.generate_content(prompt)
#     return response.text










import google.generativeai as genai
import os

# Set your Gemini API key here
genai.configure(api_key="AIzaSyCq4wzwMRZzi_gOcsA3zWW2IzJexPvcEyU")

model = genai.GenerativeModel("gemini-pro")

def generate_text(prompt):
    response = model.generate_content(prompt)
    return response.text






