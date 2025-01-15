from ollama import chat
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live
from rich.panel import Panel

def main():
    console = Console()
    text = ""

    def generate_markdown():
        return Panel(Markdown(text))

    stream = chat(
            model='llama3.1',
            messages=[{'role': 'user', 'content': 'What is Python? Use code examples to demonstrate it.'}],
            stream=True,
    )

    with Live(generate_markdown(), console=console, vertical_overflow="visible", refresh_per_second=25) as live:
        for chunk in stream:
            chunk_str = chunk["message"]["content"]
            text += chunk_str
            live.update(generate_markdown())
    

if __name__ == "__main__":
   main()
