#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/7 20:16
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : 20240419 26 rich 01.py
# @Desc     : 

from rich.console import Console
from rich.table import Table


def main() -> None:
    """ Main Function """
    console = Console()

    console.print("Hello, [bold green]World[/bold green]!", style="bold red")

    table = Table(title="Table Title", show_header=True, header_style="bold magenta")
    table.add_column("Name", style="dim", width=12)
    table.add_column("Age", style="dim", width=12)
    table.add_column("Gender", style="dim", width=12)

    table.add_row("Tom", "25", "Female")
    table.add_row("Jerry", "24", "Male")



if __name__ == "__main__":
    main()
