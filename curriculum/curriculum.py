import csv
from sys import argv

if len(argv) < 2:
    MAX = None
else:
    MAX = int(argv[1])


def read_csv():
    with open("curriculum.csv", "r") as f:
        reader = csv.DictReader(f)
        if MAX:
            time = [
                int(l['Minutes']) for i, l in enumerate(reader) if i <= MAX + 1
            ]
        else:
            time = [int(l['Minutes']) for l in reader]
        minutes = sum(time)
        total = 4 * 2 * 3
        print("Total hours: {} ({} minutes) Out of: {}".
              format(minutes / 60, minutes, total))


if __name__ == "__main__":
    read_csv()
