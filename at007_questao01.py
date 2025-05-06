def questao01():
    with open("log.txt") as f:
        linhas = f.readlines()
    print("1) Total de linhas:", len(linhas))

if __name__ == "__main__":
    questao01()
