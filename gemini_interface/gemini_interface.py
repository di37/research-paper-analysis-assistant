import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

import google.generativeai as genai
from dotenv import load_dotenv

from research_paper_analyst import RESEARCH_PAPER, FOLLOWUP_CONTEXT

_ = load_dotenv()


def initialize_gemini(model_name: str):
    """Initialize the Gemini model with the given model_name."""
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    return genai.GenerativeModel(model_name)


def generate_content(model, pdf_content, prompt):
    response = model.generate_content(
        [{"mime_type": "application/pdf", "data": pdf_content}, prompt],
        stream=True,
    )
    for chunk in response:
        yield chunk


def analyze_pdf_content(model, pdf_content: str):
    """Analyze the given PDF content with the Gemini model."""
    try:
        response = generate_content(model, pdf_content, RESEARCH_PAPER)
        return response
    except Exception as e:
        raise RuntimeError(f"Error analyzing PDF content: {str(e)}")
    # return "".join(full_response)


def process_query_stream(model, pdf_content: str, notes: str, query: str):
    """Process a user query against the analyzed PDF content using the Gemini model."""
    try:
        context = f"{notes}\n\n{FOLLOWUP_CONTEXT}\n\n{query}"
        response = generate_content(model, pdf_content, context)
        return response
    except Exception as e:
        yield f"Error processing query: {str(e)}"
