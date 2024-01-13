import requests
import threading


def main():
    url = input("| PYBRUTER | | Enter target url |~>: ")
    wordlist = input("| PYBRUTER | | Wordlist |~>: ")

    try:
        with open(wordlist, "r") as fp:
            for word in fp:
                url = (url + "/" + word)
                try:
                    r = requests.get(url)
                    if r.status_code == 200:
                        print(f"{url} is real")
                    else:
                        continue
                except ConnectionError:
                    continue
    except FileNotFoundError:
        print("No such wordlist!")


if __name__ == "__main__":
    t1 = threading.Thread(target=main)
    t1.start()
