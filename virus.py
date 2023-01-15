import random
import subprocess
import antivirus


def generate_text(length, include_spec_symbols=False):
    text = []
    if include_spec_symbols == False:
        for i in range(length):
            group = random.randint(1, 2)
            if group == 1:
                to_connect = chr(random.randint(65, 90))
            else:
                to_connect = chr(random.randint(97, 122))
            text.append(to_connect)
    else:
        for j in range(length):
            to_connect = chr(random.randint(33, 126))
            text.append(to_connect)
            group = random.randint(1, 75)
            if group == 25:
                text.append("\n")
    res = "".join(text)
    return res


def create_file(dir):
    name_file = generate_text(random.randint(5, 8))
    with open(f"{dir}/{name_file}.log", "w") as file:
        file.write(generate_text(random.randint(4000, 5000), include_spec_symbols=True))  # TODO: increase scope


def create_dir(message, quantity, antivirus_mode=False):
    for el in range(quantity):
        name_dir = generate_text(random.randint(4, 7))  # TODO: increase scope
        subprocess.call(["mkdir", name_dir])

        if antivirus_mode:  # TODO: antivirus
            with open("logs.txt", "a") as file:
                file.write(f"{name_dir}\n")

        n = random.randint(3, 7)  # TODO: increase scope
        for i in range(n):
            create_file(name_dir)
        print(f"{message}")


if __name__ == "__main__":
    delete_dirs = 0  # TODO: change for cleaning
    if delete_dirs == 0:
        create_dir("created", 3, antivirus_mode=True)
    else:
        antivirus.clean_dirs("cleaned")

#{name_dir}