import click

@click.command()
@click.option("--arr", help="array of integers.")
def sort(arr):
    temp = []
    for i in range(len(arr)):
        if arr[i] < 6:
            temp += arr[i]

    return temp

@click.command()
def main():
    arr = list(map(int, input().split()))

    click.echo(sort(arr))