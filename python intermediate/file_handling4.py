

def file_handle_showcase(path: str) -> None:
    """
    this function opens a file and 
    prints the data and adds data
    input -> path
    return -> None
    """
    with open (path, "r+") as doc:
        data = doc.read()
        print(data)

        doc.write("matan")
    

def config(path: str) -> None:
    """
    this function opens file and saves Data to file in uppercase
    input: path
    returns: none
    """
    with open(path, "r+") as conf:
        info = conf.readlines()
        data = info[0][5:-1:].upper()
        silent = info[1][7::]
        conf.write(f"\n {data}")
        
        if silent == "True":
            print(data)

def main():
    # file_handle_showcase("test")
    # config("conf")


if __name__ == "__main__":
    main()