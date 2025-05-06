from datetime import datetime

def questao07():
    def get_dt(line):
        try:
            return datetime.strptime(" ".join(line.split()[:3]), "%b %d %H:%M:%S")
        except:
            return datetime.min

    with open("log.txt") as f:
        linhas = f.readlines()
    for linha in sorted(linhas, key=get_dt):
        print(linha.strip())

if __name__ == "__main__":
    questao07()
