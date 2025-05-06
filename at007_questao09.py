def questao09():
    with open("log.txt") as f:
        for linha in f:
            if "sudo" in linha and "COMMAND=" in linha:
                print(linha.split("COMMAND=")[1].strip())

if __name__ == "__main__":
    questao09()
