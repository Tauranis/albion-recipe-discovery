import click
from recipe_discovery.discovery import ProfitDiscover
from recipe_discovery.config import QUALITY_DICT


@click.command()
@click.option("--quality", default="Normal", type=click.Choice(list(QUALITY_DICT.keys())), help="Quality of the products")
@click.option(
    "--city",
    default="Bridgewatch,Fort%20Sterling,Lymhurst,Martlock,Thetford",
    help="Which city to run analysis",
)
@click.option("--output_path", default="./report.csv", help="Output path")
def app(city, quality, output_path):
    """Run profit scanner"""
    profitDiscover = ProfitDiscover()
    stats = profitDiscover.scan(city, quality)
    stats.to_csv(output_path, index=False)


if __name__ == "__main__":
    app()
