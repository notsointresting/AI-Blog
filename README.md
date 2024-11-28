# Instructions for Running the Blog Generator

## Prerequisites
1. Python 3.7 or higher installed on your system
   - Download from: https://www.python.org/downloads/

## Required Libraries
Install the following library using pip:
```
pip install openai
```

## API Key Setup
1. Sign up for an XAI (x.ai) account
2. Get your API key from the XAI dashboard
3. Set up your API key as an environment variable:

   For Windows (in Command Prompt):
   ```
   set XAI_API_KEY=your_api_key_here
   ```

   For Windows (in PowerShell):
   ```
   $env:XAI_API_KEY = "your_api_key_here"
   ```

   For Linux/Mac:
   ```
   export XAI_API_KEY=your_api_key_here
   ```

## Running the Code
1. Save the Python code as `main.py`
2. Open a terminal/command prompt
3. Navigate to the directory containing `main.py`
4. Run the script:
   ```
   python main.py
   ```

## Using the Blog Generator
1. When prompted, enter your desired blog topic
2. Optionally, enter a specific angle or focus for the topic
3. The generated blog post will be displayed in the terminal

## Troubleshooting
1. If you get an API key error:
   - Verify your API key is correctly set as an environment variable
   - Check if your XAI account is active

2. If you get a ModuleNotFoundError:
   - Run `pip install openai` again
   - Make sure you're using the correct Python environment

3. If you get a connection error:
   - Check your internet connection
   - Verify that the XAI API service is available

## Notes
- The generated content uses Grok's humorous style
- Each run will generate a unique blog post
- The quality of output depends on the specificity of your topic and angle

## Support
For API-related issues, refer to:
- XAI API documentation
- OpenAI Python library documentation: https://github.com/openai/openai-python
