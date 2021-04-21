import click
from recipe_discovery.discovery import ProfitDiscover


@click.command()
@click.option("--quality", default=1, help="Quality of the products")
@click.option(
    "--city",
    default="Bridgewatch,Fort%20Sterling,Lymhurst,Martlock,Thetford",
    help="Which city to run analysis",
)
@click.option("--output_path", default="./report.csv", help="Output path")
def app(city, quality, output_path):
    """Run profit discovery"""
    profitDiscover = ProfitDiscover(city, quality)
    stats = profitDiscover.scan()
    stats.to_csv(output_path, index=False)


if __name__ == "__main__":
    app()
