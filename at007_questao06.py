import re

def questao06():
    with open("log.txt") as f:
        users = set()
        for linha in f:
            if "sudo" in linha:
                match = re.search(r'sudo\[\d+\]: (\w+)', linha)
                if match:
                    users.add(match.group(1))
    for u in sorted(users):
        print(u)

if __name__ == "__main__":
    questao06()
