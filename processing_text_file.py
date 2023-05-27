def store(extracted):
    """This function stores extracted data to .txt file"""
    with open("files/data.txt", "a") as file:
        file.write(extracted + "\n")


def read():
    """reading text file"""
    with open("files/data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    pass