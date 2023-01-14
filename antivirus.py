import subprocess


def clean_dirs(message):
    to_delete = []
    with open("logs.txt") as file:
        for i in file:
            to_delete.append(i.strip("\n"))
    for i in to_delete:
        subprocess.call(["rm", "-rf", i])
        print(i, message)


if __name__ == "__main__":
    clean_dirs("cleaned")
