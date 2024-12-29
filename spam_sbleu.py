import random
import requests
import argparse
import threading
import time

parser = argparse.ArgumentParser(description='Spam a Google Form with requests.')
parser.add_argument('n', metavar='N', type=int, help='Number of iterations', default=100)
parser.add_argument('--threads', metavar='T', type=int, help='Number of threads', default=5)
args = parser.parse_args()

#url = "https://docs.google.com/forms/d/e/1FAIpQLSeFyryN0f641ieHqtf9Qa5mAS_7xzfyEAZ6Y1UhR8u0T4vTog/formResponse"
url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSeFyryN0f641ieHqtf9Qa5mAS_7xzfyEAZ6Y1UhR8u0T4vTog/formResponse"

posts = ["15n", "quinzaine", "bar", "rachat", "vieux", "sympath", "BAAAR", "Prési", "Clash", "Annim bar", "FLTR", "AGRO", "vieux con", "Je suis puceau", "zigouille", "C au cube", "hackerman", "web", "sympath", "vieux", "sterput", "CI", "Spix", "meme", "cenat", "Cyclofette", "BaR", "BDE"]
sizes = ["XS","S", "M", "L", "XL", "XXL", "3XL"]
pays = ["OUI car je suis cool et détente 😎", "Juste après avoir compléter le form", "Déjà fait 😌 (bv le boss)"]

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
        "entry.45844893": name, #Nom prénom
        "entry.145173097": nicknamePost, #Surnom(adjective+nouns)+Post
        "entry.1387090533": "OUI car je suis cool et détente 😎",
        "entry.720160850": size,
        "entry.1100260589": pay,
        #"entry.1387090533_sentinel": " ",
        #"entry.720160850_sentinel": " ",
        #"entry.1100260589_sentinel": " "
    }

def submit(url, data):
    """Submits the form data."""
    try:
        res = requests.post(url, data=data)
        if res.status_code == 200:
            print(f"Submitted successfully: {data}")
            return True
        else:
            print(f"Failed with status: {res.status_code} and reason: {res.reason}, data: {data}")
            return False
    except Exception as e:
        print(f"Error during submission: {e}")
        return False

def spam_form(iterations):
    """Handles the spamming process."""
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
        submit(url, form_data)
        #print(form_data)
        time.sleep(random.uniform(1, 3))  # Random delay to avoid rate-limiting

def start_spam(threads, iterations):
    """Runs the spamming process with multiple threads."""
    thread_list = []
    per_thread = iterations // threads

    for _ in range(threads):
        thread = threading.Thread(target=spam_form, args=(per_thread,))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    print("Starting the spamming process...")
    #total_iterations = args.n
    #num_threads = args.threads
    #start_spam(num_threads, total_iterations)
    spam_form(args.n)

