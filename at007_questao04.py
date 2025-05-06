def questao04():
    with open("log.txt") as f:
        for linha in f:
            if "Failed password" in linha:
                print(linha.strip())

if __name__ == "__main__":
    questao04()
