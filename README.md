explain — AI-powered terminal error explainer

explain is a small command-line tool that runs a shell command, captures its output (stdout + stderr), and asks an AI model to explain what went wrong in simple terms.


Project Structure:

    ai_explain/
    ├── explain.py          # Main script
    ├── requirements.txt    # Python dependencies
    ├── README.md           # This file

Setting up:

1.Clone the respository

2.Install dependencies:

pip install -r requirements.txt

3.Set  API_KEY as your openai api key in the explain.py file

4.Make it a global command:

chmod +x explain.py

sudo cp explain.py /usr/local/bin/explain


After that to run on examples:

explain ls /nonexistent
explain python faulty_script.py
