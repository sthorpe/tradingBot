import click

all_colors = (
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "bright_black",
    "bright_red",
    "bright_green",
    "bright_yellow",
    "bright_blue",
    "bright_magenta",
    "bright_cyan",
    "bright_white",
)

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")

def coinbase_console2(count, name):
    """Coinbase console to display data quickly"""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

def coinbase_console1():
    """Coinbase console to display data quickly"""
    for color in all_colors:
        click.echo(click.style(f"I am colored {color}", fg=color))
    for color in all_colors:
        click.echo(click.style(f"I am colored {color} and bold", fg=color, bold=True))
    for color in all_colors:
        click.echo(click.style(f"I am reverse colored {color}", fg=color, reverse=True))

    click.echo(click.style("I am blinking", blink=True))
    click.echo(click.style("I am underlined", underline=True))

def coinbase_console(count, name):
    """Coinbase console to display data quickly"""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    coinbase_console()
