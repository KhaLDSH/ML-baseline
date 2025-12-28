import json
import time
import typer
from pathlib import Path

from ml_baseline.sample_data import make_sample_feature_table


app = typer.Typer(help="A CLI tool to generate Data ,apply training and testing.")

@app.command()
def help():
    print("help")

@app.command()
def hello():
    print("hello")


@app.command()
def make_sample_data(
    output_dir: Path = typer.Option(
        None, "--output-dir", "-o", help="Output directory"
    ),
    n_users: int = typer.Option(
        50, "--n-users", help="Number of users"
    ),
    seed: int = typer.Option(
        0, "--seed", help="Random seed"
    ),
):
    """
    Generate sample feature data.
    """
    path = make_sample_feature_table(
        root=output_dir,
        n_users=n_users,
        seed=seed,
    )
    typer.echo(f"Sample data written to: {path}")


if __name__ == "__main__":
    app()