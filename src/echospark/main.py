from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from echospark.agent import EchoSparkAgent

load_dotenv()
console = Console()


def main():
    console.print(
        Panel.fit(
            "[bold cyan]✦ EchoSpark v0.1.0[/bold cyan]\n"
            "[dim]Autonomous software engineering agent powered by Gemini. Type 'exit' to terminate.[/dim]",
            border_style="cyan",
        )
    )

    agent = EchoSparkAgent()

    while True:
        try:
            user_input = console.input("\n[bold green]Operator > [/bold green]").strip()
            if not user_input:
                continue
            if user_input.lower() in ("exit", "quit", "q"):
                break

            with console.status("[bold cyan]Executing...[/bold cyan]"):
                reply = agent.run(user_input)

            console.print("\n[bold cyan]EchoSpark > [/bold cyan]")
            console.print(Markdown(reply))

        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
