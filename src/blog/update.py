import shutil
import subprocess

import click


@click.command()
@click.option("--pull/--no-pull", default=True)
def main(pull):
    try:
        if pull:
            subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=True)
        subprocess.run(["uv", "sync"], check=True)
        subprocess.run(["npm", "--prefix=./theme", "install"], check=True)
        shutil.rmtree("public", ignore_errors=True)
    except subprocess.CalledProcessError:
        raise click.Abort()
