import typer
from typer import Typer, Argument, Option, colors, secho
from .utils import getPytorchWheelLinks, rmTrailingHash, EPlatformPytorch


def findUrls(package: str, version: str=Option('2.2.0', '--version', '-v'), device='cpu'):
    secho('Votre URL wheel est parmi les suivants:', fg=colors.CYAN)

    liensTorch: list[str] = getPytorchWheelLinks(package, device, version)
    if len(liensTorch):
        for l in liensTorch:
            secho(f'{rmTrailingHash(l)}', fg=colors.GREEN)
            pass


if __name__ == '__main__':
    typer.run(findUrls)