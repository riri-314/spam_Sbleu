import random
import requests
import argparse
import threading
import time

parser = argparse.ArgumentParser(description='Spam a Google Form with requests.')
parser.add_argument('n', metavar='N', type=int, help='Number of iterations', default=100)
parser.add_argument('--threads', metavar='T', type=int, help='Number of threads', default=5)
args = parser.parse_args()

url = "https://docs.google.com/forms/d/e/1FAIpQLSeFyryN0f641ieHqtf9Qa5mAS_7xzfyEAZ6Y1UhR8u0T4vTog/formResponse"

posts = ["15n", "quinzaine", "bar", "rachat", "vieux", "sympath", "BAAAR", "Prési", "Clash", "Annim bar", "FLTR", "AGRO", "vieux con", "Je suis puceau", "zigouille", "C au cube", "hackerman", "web", "sympath", "vieux", "sterput"]
sizes = ["S", "M", "L", "XL"]

# Load names from file
with open('first-names.txt', 'r') as file:
    names = [line.strip() for line in file.readlines()]

def fill_form(name, nickname, post, size):
    """Prepares the form data."""
    return {
        "entry.868042368": name,
        "entry.569405921": nickname,
        "entry.146262275": post,
        "entry.874958648": size,
        "entry.874958648_sentinel": " ",
    }

def submit(url, data):
    """Submits the form data."""
    try:
        res = requests.post(url, data=data)
        if res.status_code == 200:
            print(f"Submitted successfully: {data}")
            return True
        else:
            print(f"Failed with status: {res.status_code}")
            return False
    except Exception as e:
        print(f"Error during submission: {e}")
        return False

def spam_form(iterations):
    """Handles the spamming process."""
    for _ in range(iterations):
        name = random.choice(names)
        nickname = random.choice(names)
        post = random.choice(posts)
        size = random.choice(sizes)
        form_data = fill_form(name, nickname, post, size)
        submit(url, form_data)
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
    total_iterations = args.n
    num_threads = args.threads
    start_spam(num_threads, total_iterations)
