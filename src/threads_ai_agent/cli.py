import click
import logging
from pathlib import Path
from datetime import datetime

from threads_ai_agent.agent import create_agent

OUTPUTS_DIR = Path("outputs")


@click.command()
@click.argument("user")
def main(user):
    """Create a Thread post mimicking the style of USER."""
    OUTPUTS_DIR.mkdir(exist_ok=True)
    
    agent = create_agent()
    result = agent(f"Create a Thread for user: '{user}'")
    
    output_file = OUTPUTS_DIR / f"{user}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    output_file.write_text(str(result))
    click.echo(f"Output saved to: {output_file}")


if __name__ == "__main__":
    main()
