#!/usr/bin/env python

import click
from dblib.querydb import querydb
from dblib.querydb import query_year

# build a click group


@click.group()
def cli():
    """A simple CLI to query a SQL database"""


# build a click command
@cli.command()
@click.option(
    "--query",
    default="SELECT * FROM hive_metastore.default.netflix_titles LIMIT 2;",
    help="SQL query to show the entire database from databricks",
)
def cli_query(query):
    """Execute a SQL query to display database"""
    querydb(query)

# building another click command


@cli.command()
@click.option(
    "--movie",
    default="Jaguar",
    help="Query to find the year of the movie ",
)
def cli_query_year(movie):
    """Execute a SQL query to find the year"""
    query_year(movie)


# run the CLI
if __name__ == "__main__":
    cli_query_year()
