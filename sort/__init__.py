import click


def sort(arr):
    temp = []
    for i in range(len(arr)):
        if arr[i] < 6:
            temp.append(arr[i])

    return temp

@click.command()
@click.option("--arr", help="array of integers.", multiple=True, type=int)
def main(arr):
    click.echo(sort(arr))
