from rich.console import Console
from rich.table import Table


def show_report(result):
    console = Console()

    table = Table(title="AI CODE ENGINE REPORT", style="cyan")

    table.add_column("Metric", style="bold")
    table.add_column("Value", style="white")

    static = result.get("static", {})
    ai = result.get("ai", {})

    # Risk
    table.add_row("Risk Score", str(static.get("risk", 0)))

    # Complexity
    table.add_row("Complexity", str(static.get("complexity", 0)))

    # Issues
    issues = static.get("issues", [])
    table.add_row("Issues", "\n".join(issues) if issues else "None")

    # AI Severity
    table.add_row("AI Severity", ai.get("severity", "N/A"))

    # Suggestions
    suggestions = ai.get("suggestions", [])
    table.add_row(
        "Suggestions",
        "\n".join(suggestions) if suggestions else "None"
    )

    # Optimized code preview
    optimized = result.get("optimized", "")
    table.add_row("Optimized Code", optimized[:200] + "...")

    console.print(table)