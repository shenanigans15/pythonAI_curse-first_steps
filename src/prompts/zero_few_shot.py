from rich.console import Console
from rich.table import Table
from rich.rule import Rule

from src.helpers.ai_client import call_ai

console = Console()

def run_zero_few_shot():
    console.print(Rule("[bold yellow]Técnica: Zero-Shot"))
    zero_shot = call_ai([
        {
            "role": "user",
            "content": "Clasifica este email como URGENTE O NORMAL: "
            "'El servidor de producción está caído, los clientes no pueden acceder'"
        }
    ])

    table = Table(title="Comparación")
    table.add_column("Técnica", style="cyan")
    table.add_column("Resultado", style="magenta")

    table.add_row("Zero-shot", zero_shot)

    console.print(table)