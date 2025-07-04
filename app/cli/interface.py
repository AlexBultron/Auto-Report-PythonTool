import argparse
from rich.console import Console
from app.data.processor import generate_report

def main():
    parser = argparse.ArgumentParser(description="AutoReport CLI")
    parser.add_argument("--report", help="Generate report", action="store_true")
    args = parser.parse_args()

    console = Console()
    if args.report:
        report = generate_report()
        console.print(f"[bold green]Average Value:[/bold green] {report['average_value']}")
        for row in report["data"]:
            console.print(row)
