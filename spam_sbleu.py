import random
import requests
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('n', metavar='N', type=int, help='an integer for the number of iterations', default=100)

args = parser.parse_args()

#url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdwcwvrOeBG200L0tCSUHc1MLebycACWIi3qw0UBK31GE26Yg/formResponse"
#url = "https://docs.google.com/forms/d/e/1FAIpQLSc9o79d3nQIkFj0n3cE22ocRgKdMNdczHOaHsE9g50bzXMjJA/formResponse" 

url = "https://docs.google.com/forms/d/e/1FAIpQLSfWm5CkbKknD93xJ230mViaBBXkDLYfEX8tfRxBwLx-WiAiyA/formResponse"

posts = ["15n", "quinzaine", "bar", "rachat", "vieux", "sympath", "BAAAR", "Prési", "Clash", "Annim bar", "FLTR", "AGRO", "vieux con", "Je suis puceau", "zigouille", "C au cube", "hackerman", "web", "sympath", "vieux", "sterput"]
sizes = ["S", "M", "L", "XL"]

def fill_form(name, nickname, post, size):
    #name = "henri"
    #nickname = "camart"
    #post = "hacker"
    #size = "XL"

    value = {
        "entry.868042368": name,
        "entry.569405921": nickname,
        "entry.146262275": post ,
        "entry.874958648": size,
        "entry.874958648_sentinel":" ",
    }
    print(value, flush = True)
    return value

def submit(url, data):
    try:
        res = requests.post(url, data = data)
        if res.status_code != 200:
            # TODO: show error message
            raise Exception("Error! Can't submit form", res.status_code)
        return True
    except Exception as e:
        print("Error!", e)
        return False


    
if __name__ == "__main__":
    print("Running script...", flush = True)
    with open('first-names.txt', 'r') as file:
        lines = file.readlines()
        for _ in range(args.n):
            post = random.choice(posts)
            size = random.choice(sizes)
            name = random.choice(lines).strip()
            nickname = random.choice(lines).strip()
            #print(random.choice(lines).strip(), random.choice(lines).strip(), post, size)
            submit(url, fill_form(name, nickname, post, size)) 