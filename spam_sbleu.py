import random
import requests
import argparse
import threading
import time

parser = argparse.ArgumentParser(
    description='Spam a Google Form with requests.')
parser.add_argument('n', metavar='N', type=int,
                    help='Number of iterations', default=100)
args = parser.parse_args()

url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSeFyryN0f641ieHqtf9Qa5mAS_7xzfyEAZ6Y1UhR8u0T4vTog/formResponse"
#url = "https://docs.google.com/forms/d/e/1FAIpQLSdV9Ez-bog289UVeebvDElEXfa6VfGsXlITgYEWSLgSuTK-Ig/formResponse" # Test form

posts = ["15n", "quinzaine", "bar", "rachat", "vieux", "sympath", "BAAAR", "Prési", "Clash", "Annim bar", "FLTR", "AGRO", "vieux con", "Je suis puceau",
         "zigouille", "C au cube", "hackerman", "web", "sympath", "vieux", "sterput", "CI", "Spix", "meme", "cenat", "Cyclofette", "BaR", "BDE"]
sizes = ["XS", "S", "M", "L", "XL", "XXL", "3XL"]
pays = ["AVANT le 20/01/2025",
        "Juste après avoir compléter le form", "Déjà fait 😌 (bv le boss)"]


# Load names from file
with open('first-names.txt', 'r') as file:
    names = [line.strip() for line in file.readlines()]

with open('adjectives.txt', 'r') as file:
    adjectives = [line.strip() for line in file.readlines()]

with open('nouns.txt', 'r') as file:
    nouns = [line.strip() for line in file.readlines()]


def fill_form(name, nicknamePost, size, pay):
    """Prepares the form data."""
    return {
        "entry.45844893": name,  # Nom prénom
        "entry.145173097": nicknamePost,  # Surnom(adjective+nouns)+Post
        "entry.1387090533": "OUI car je suis cool et détente 😎",
        "entry.720160850": size,
        "entry.1100260589": pay,
    }


def submit(url, data):
    """Submits the form data."""
    try:
        res = requests.post(url, data=data)
        if res.status_code == 200:
            print(f"\033[92mSubmitted successfully\033[0m: {data}")
            return True
        else:
            print(f"\033[91mFailed with status\033[0m: {res.status_code} and reason: {res.reason}, data: {data}")
            return False
    except Exception as e:
        print(f"Error during submission: {e}")
        return False


def spam_form(iterations):
    """Handles the spamming process."""
    succes = 0
    fail = 0
    i = 1
    for _ in range(iterations):
        name1 = random.choice(names)
        name2 = random.choice(names)
        name = name1 + " " + name2
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        nickname = adjective + " " + noun
        post = random.choice(posts)
        nicknamePost = nickname + ", " + post
        size = random.choice(sizes)
        pay = random.choice(pays)
        form_data = fill_form(name, nicknamePost, size, pay)
        print(" ")
        print(f"Submitting form {i}/{iterations}... ")
        ret = submit(url, form_data)
        if ret:
            succes += 1
        else:
            fail += 1
        print(f"Succes: {succes/(fail+succes)*100:.2f}%")
        # print(form_data)
        i += 1
        # Random delay to avoid rate-limiting
        time.sleep(random.uniform(0.2, 0.5))
    print(f"Successfully submitted: {succes}")
    print(f"Failed to submit: {fail}")

if __name__ == "__main__":
    print("Starting the spamming process...Yahouuuu Hack the world")
    spam_form(args.n)
