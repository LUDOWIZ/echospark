import json
import os
from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from echospark.tools import AVAILABLE_TOOLS, TOOL_SCHEMAS

console = Console()

SYSTEM_PROMPT = """
Du är EchoSpark – en skarp, lösningsorienterad AI-utvecklarkollega med glimten i ögat.
Använd dina verktyg stegvis för att inspektera miljön och skapa filer vid behov. Håll svaren koncisa och handlingskraftiga.
"""


class EchoSparkAgent:
    def __init__(self, max_steps: int = 6):
        self.client = OpenAI(
            api_key=os.getenv("GEMINI_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        )
        self.model = os.getenv("MODEL_NAME", "gemini-2.5-flash")
        self.max_steps = max_steps
        self.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    def run(self, user_input: str) -> str:
        self.messages.append({"role": "user", "content": user_input})

        for step in range(1, self.max_steps + 1):
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                tools=TOOL_SCHEMAS,
                tool_choice="auto",
            )

            message = response.choices[0].message
            self.messages.append(message)

            if not message.tool_calls:
                return message.content or "Klart!"

            for tool_call in message.tool_calls:
                func_name = tool_call.function.name
                func_args = json.loads(tool_call.function.arguments or "{}")

                console.print(
                    Panel(
                        f"[bold cyan]Steg {step}[/bold cyan] → [bold yellow]{func_name}[/bold yellow]({func_args})",
                        border_style="dim",
                        expand=False,
                    )
                )

                tool_fn = AVAILABLE_TOOLS.get(func_name)
                result = tool_fn(**func_args) if tool_fn else f"Okänt verktyg: {func_name}"

                self.messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(result),
                    }
                )

        return "Max antal steg uppnått."