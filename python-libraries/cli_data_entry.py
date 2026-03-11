from rich.console import Console
from rich.table import Table
import csv
import os

console = Console()

#title
console.print("Welcome to the Music Data Entry App!", style="bold cyan")

#example table
table = Table(title="Example Albums")

table.add_column("Artist", style="magenta")
table.add_column("Album", style="green")
table.add_column("Year", style="yellow")

table.add_row("The Weeknd", "After Hours", "2020")
table.add_row("Taylor Swift", "1989", "2014")
table.add_row("SZA", "SOS", "2022")

console.print(table)
console.print("\nNow you can enter your own music data!", style="bold blue")

entries = []

while True:

    artist = input("Artist name: ")
    album = input("Album title: ")
    year = input("Release year: ")

    console.print("\nYou entered:", style="bold yellow")
    console.print("Artist: " + artist)
    console.print("Album: " + album)
    console.print("Year: " + year)

    confirm = input("Is this correct? (yes/no): ")

    if confirm.lower() == "yes" or confirm.lower() == "y":
        entries.append([artist, album, year])
        console.print("Entry saved!", style="green")

    else:
        console.print("Okay, please re-enter the data.", style="red")
        continue

    again = input("Do you want to add another album? (yes/no): ")

    if again.lower() == "no" or again.lower() == "n":
        break


#save to csv
filename = "music_data.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Artist", "Album", "Year"])

    for entry in entries:
        writer.writerow(entry)


#print path
path = os.path.abspath(filename)
console.print("\nYour data has been saved!", style="bold green")
console.print("File location:", style="bold cyan")
console.print(path)