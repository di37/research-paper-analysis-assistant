# Research Paper Analysis Assistant

This application uses the Gemini model to provide in-depth analysis of research papers (in PDF format). By leveraging Gemini’s extended context window—capable of handling up to 2 million tokens—this tool can retain and reference large sections of a research paper at once, enabling a more comprehensive understanding and more accurate responses to user queries.

## Features

- **PDF Upload & Analysis:** Upload a PDF research paper and initiate automatic analysis.
- **Real-Time Streaming Responses:** View analysis results and Q&A responses as they are generated.
- **Follow-Up Queries:** After analysis, ask questions about the paper's content.
- **Model Selection:** Choose from a list of available Gemini models for processing.
- **API Key Configuration:** Provide your Gemini API key to authenticate and use the chosen model.

## Requirements

- Python 3.8 or higher
- [Streamlit](https://streamlit.io/) for the web interface
- Gemini-related Python packages (as defined in `requirements.txt` or the project’s `utilities` module)
- A Gemini API Key

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <REPO_URL>
   cd <REPO_DIRECTORY>
   ```

2. **Install Dependencies:**
   If there is a `requirements.txt` file provided:

   ```bash
   pip install -r requirements.txt
   ```

   Make sure all required packages such as `streamlit` and Gemini utilities are installed. If not, install them individually:

   ```bash
   pip install streamlit
   # ... any other required packages
   ```

3. **Set Up Your Gemini API Key:**
   Obtain an API key from Gemini. You will be prompted to enter it in the application’s sidebar once you run the app.

## Usage

1. **Run the Application:**

   ```bash
   streamlit run main.py
   ```

   This will start the Streamlit app on a local server. The terminal output will display a local URL (e.g., `http://localhost:8501`).

2. **Open in Browser:**
   Open the displayed URL in your web browser. You’ll see the app’s interface.

3. **Configure the Application:**

   - In the sidebar, select a Gemini model from the dropdown.
   - Enter your Gemini API key.
   - Upload a PDF file that you want to analyze.

4. **Analyze the Paper:**
   Click the **"Analyze Paper"** button after uploading your PDF. The app will:

   - Initialize the selected Gemini model.
   - Process your PDF and display analysis results in real-time.

5. **Ask Questions:**
   After analysis, a chat interface is available at the bottom of the main page. Type a question related to the analyzed paper and press **Enter**. The app will provide a streamed response.

6. **Clear Chat (Optional):**
   To clear all previous messages and start fresh, click the **"Clear Chat"** button in the sidebar.

## Development Notes

- The main user interface logic resides in `main.py`.
- Gemini-specific logic is encapsulated in a separate module (e.g., `gemini_interface.py`).
- Utilities such as model initialization, PDF encoding, and constant definitions (like `GEMINI_MODELS`) are found in the `utilities` module.
- For local development, ensure that paths and imports are configured correctly.

## Contributing

If you would like to contribute:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Open a Pull Request with a detailed description of your changes.

## License

This project is provided under the terms specified by the repository owner (add your license details here, e.g., MIT, Apache 2.0, GPL-3.0, etc.). If no license is specified, the default is "All Rights Reserved."

---

**Disclaimer:** This application relies on the Gemini model and its associated API. Ensure you have the necessary permissions and adhere to the API provider’s usage and billing policies.
