from collections import Counter

def questao08():
    users = []
    with open("log.txt") as f:
        for linha in f:
            if "Failed password" in linha:
                user = linha.split("Failed password for ")[1].split()[0]
                users.append(user)
    for u, count in Counter(users).items():
        if count > 1:
            print(f"{u} ({count})")

if __name__ == "__main__":
    questao08()
