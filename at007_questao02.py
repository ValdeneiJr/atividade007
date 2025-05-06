def questao02():
    with open("log.txt") as f:
        for linha in f:
            if "Accepted password" in linha:
                print(linha.strip())

if __name__ == "__main__":
    questao02()
