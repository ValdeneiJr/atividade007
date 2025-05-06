def questao05():
    with open("log.txt") as f:
        linhas = f.readlines()
    sucesso = sum("Accepted password" in l for l in linhas)
    falha = sum("Failed password" in l for l in linhas)
    print(f"Sucessos: {sucesso}")
    print(f"Falhas: {falha}")

if __name__ == "__main__":
    questao05()
