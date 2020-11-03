"""Console script for jotter."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for jotter."""
    click.echo("The command line interface for jotter is not implemented, yet.")
    # click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
