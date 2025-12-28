import json
import time
import typer
from pathlib import Path



app = typer.Typer(help="A CLI tool to generate Data ,apply training and testing.")

@app.command(help="Generate random data into a CSV file.")
def profile(
    input_path: Path = typer.Argument(..., help="Input CSV file"),
    out_dir: Path = typer.Option(Path("outputs"), "--out-dir", help="Output folder"),
    report_name: str = typer.Option("report", "--report-name", help="Base name for outputs"),
    preview: bool = typer.Option(False, "--preview", help="Print a short summary"),
):

        # rows = read_csv_rows(input_path)  # Reads the data
        
        # 2. Profiling
        # report = profile_rows(rows)       # Performs the data analysis
        
        out_dir.mkdir(parents=True, exist_ok=True)
        typer.secho(f"Output directory confirmed: {out_dir}", fg=typer.colors.BLUE)
        
        md_path = out_dir / f"{report_name}.md"
        # md_path.write_text(render_markdown(report), encoding="utf-8")
        typer.secho(f"Wrote Markdown report to: {md_path}", fg=typer.colors.GREEN)
        
        # if preview:
        #     typer.echo("-" * 30)
        #     typer.echo(f"Summary:")
        #     typer.echo(f"  Rows: {report['n_rows']}")
        #     typer.echo(f"  Cols: {report['n_cols']}")
        #     typer.echo("-" * 30)


if __name__ == "__main__":
    app()