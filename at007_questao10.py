import re
from collections import Counter

def questao10():
    ips = Counter()
    with open("log.txt") as f:
        for linha in f:
            if "sshd" in linha:
                match = re.search(r'from ([\d.]+)', linha)
                if match:
                    ips[match.group(1)] += 1
    for ip, count in ips.most_common():
        print(f"{ip} — {count}")

if __name__ == "__main__":
    questao10()
