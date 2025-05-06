import re

def questao03():
    with open("log.txt") as f:
        ips = set()
        for linha in f:
            if "sshd" in linha:
                match = re.search(r'from ([\d.]+)', linha)
                if match:
                    ips.add(match.group(1))
    for ip in sorted(ips):
        print(ip)

if __name__ == "__main__":
    questao03()
