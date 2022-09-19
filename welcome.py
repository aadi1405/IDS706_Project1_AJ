import click

@click.command()

@click.option('--name', prompt='Enter your name:',
              help='Enter your name to greet.')
def hello(name):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo(f"Hello {name}!, Welcome to my first Data Engineering project where I explore SQL, Databricks, codespaces and configuring CLI")

if __name__ == '__main__':
   hello()