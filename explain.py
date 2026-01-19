#!/usr/bin/env python3
import openai
import sys
from rich import print
import subprocess


API_KEY = ""
MODEL = "gpt-4o-mini"
VERBOSE = False 

openai.api_key = API_KEY


def print_error(text):
    print(f"[red]{text}[/red]")


def print_info(text):
    print(f"[green]{text}[/green]")


def main():

    # 1.Read input from sys.stdin
    if len(sys.argv) < 2:
        print_error("How to use: explain <command> [args...]")
        sys.exit(1)

    command = sys.argv[1:]

    try:
        result = subprocess.run(command, capture_output=True,text=True)
        input_text = result.stdout + result.stderr
    except Exception as e:
        print_error(f"Failed to run command{e}")
        sys.exit(1)
    if not input_text.strip():
        print_error(f"No output")
        sys.exit(1)

    # 2.Prompt model
    prompt = f"Explain in simple terms the following terminal output:\n{input_text}\n"
    if VERBOSE:
        prompt += "Provide a detailed explanation and suggest possible fixes if applicable."

    # 3.Call API
    try:
        response = openai.chat.completions.create(
            model=MODEL,
            messages=[{"role":"user","content":prompt}],
            temperature=0.2
        )
        explanation = response.choices[0].message.content.strip()

    # 4. Print AI explanation
        print_info(explanation)
    except Exception as e:
        print_error(f"Error calling openai api: {e}")


if __name__ == "__main__":
    main()

