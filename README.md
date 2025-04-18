# TextToTalk: A Text to MP3 Converter Web App

This is a Streamlit-based web application that allows users to input text, summarize it, translate it (optional), and then convert the summarized text to an MP3 audio file. The application uses `transformers` for text summarization, `googletrans` for translation, and `gTTS` (Google Text-to-Speech) for converting text to speech.

## Features

- Input text directly into the web app using a simple text area.
- Optionally summarize the text before converting it to speech, with adjustable summarization strength.
- Optionally translate the summarized text to another language before converting to speech.
- Select the desired language for text-to-speech conversion.
- Convert the input text (summarized and/or translated) to an MP3 audio file.
- Play the generated audio file directly on the web app.
- Download the generated MP3 audio file.
- Download the summarized text as a `.txt` file.
- Copy the summarized text to the clipboard for easy use.



## Requirements

- Python 3.6 or higher
- `transformers`
- `torch`
- `googletrans`
- `gtts`
- `streamlit`

## Installation

1. Clone the repository:
   
   ```sh
   git clone https://github.com/yourusername/TextToTalk.git
   cd TextToTalk

2.  Create a virtual environment:
    
    ```sh
    python -m venv venv source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3.  Install the required packages:
4.  
    ```sh
    pip install -r requirements.txt    



Usage
-----

1.  Run the Streamlit app:
    
    ```sh
    cd scripts streamlit run app.py
    
2.  Open your web browser and go to [http://localhost:8501](http://localhost:8501) to access the app.
    
3.  Input your desired text into the provided text area.
    
4.  Optionally, choose to summarize the text before audio conversion, and adjust the summarization strength using the slider.
    
5.  Optionally, select a language for translation before converting it to speech.
    
6.  Choose the desired language for the audio output (e.g., English, Spanish, French, German).
    
7.  The app will process the input text, generate the summarized/translated text (if applicable), and convert it to speech. An audio player will appear for you to listen to the generated MP3 file.
    
8.  You can also download the generated MP3 file using the download button and save the summarized text as a `.txt` file.
    
9.  Optionally, copy the summarized text to the clipboard for easy use.

    

## File Structure
- **ExtText.py**: Contains the function for extracting text from the uploaded PDF file (now replaced with plain text input).
- **TTS.py**: Contains the function for converting text to speech using gTTS.
- **Summarizer.py**: Contains the function for summarizing the input text using a pre-trained model.
- **Pipeline.py**: Integrates the text summarization, translation, and text-to-speech conversion functions into a single pipeline.
- **app.py**: The main Streamlit app that provides the web interface for the text input, summarization, translation, and MP3 conversion.

    

Contributing
------------

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or create a pull request.

License
-------

This project is licensed under the MIT License. See the LICENSE file for more details.
