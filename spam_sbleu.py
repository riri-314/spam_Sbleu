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

real_names = [["Agathe Henry", "Pompelup"],
              ["François Caussin", "Saucisse"],
              ["Xavier Sanchez-Rivas","Uno"],
              ["Lucie Tournay","Kokosnoot"],
              ["Oscar Misson", "Woluwe"],
              ["Charlotte Morelle","Brooklyn99"],
              ["Clarisse Gatot","Otto"],
              ["Antoine Eck","Loci"],
              ["Maxence Dronneau","Nageoire Avant"],
              ["Alexandre Sanchez","Tranquilou Debout"],
              ["Baptiste Leblanc","Supreme Cheese"],
              ["Romain Bongiovanni","Lonely"],
              ["Henri Pihet","Camartichau"],
              ["Alicia De Hert","Germaine"],
              ["Neira Hotilovac","Random"],
              ["Sascha Kurochkin","Viggo"],
              ["Florian Boon Georges","Lemetre"],
              ["Zoé Vanboucq","Céréli-thé"],
              ["Alvaro Farcy","Reinπ"],
              ["Emilie Strimelle","Whisky"],
              ["Isaline De Saffel","Djaccuz" ],
              ["Elsa Biver","Panos"],
              ["Hugo Wouters","2Blues"],
              ["Matteo Deléhouzée","Marylin Manson"],
              ["Louis Van de Laer","Platane"],
              ["Déborah Gemberling","Flash"],
              ["Carole Vinesse","Failaiback"],
              ["Louis Verhelst","Répépète"],
              ["Tatiana Baccus","Bacc14"],
              ["Tess Cluysen","Rouky"],
              ["Audrey Bousquet-Hourat","Tag"],
              ["Joshua Nerenhausen","Rhésus"],
              ["James Ping","Latence"],
              ["Guillaume Garsoux","Perdu"],
              ["Violette Renier","Juke-Box"],
              ["Vadim Auslender","Magicarpe"],
              ["Elise Dejean","Shisha"],
              ["Samantha Revercez","Clover"],
              ["Anna Priem","Fifloflette"],
              ["Henri Pihet","Camartichau"],
              ["Déborah Gemberling","Flash"]
              ]

adjectives = open('french-word-list-adjectives.csv', 'r', encoding='ISO-8859-1')
adjectives = adjectives.readlines()

nouns = open('french-word-list-nouns.csv', 'r', encoding='ISO-8859-1')
nouns = nouns.readlines()

def fill_form(name, nickname, post, size):
    #name = "henri"
    #nickname = "camart"
    #post = "hacker"
    #size = "XL"

    value = {
        #"entry.1138287767": name,
        #"entry.1580613741": "Option 3",
        #"entry.1580613741_sentinel":" ",
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
            adjective_line = random.randint(0, 199)
            noun_line = random.randint(0, 199)
            real_name_int = random.randint(0, 40)

            adj = adjectives[adjective_line].split(';')[1]
            noun = nouns[noun_line].split(';')[1]

            real_name = real_names[real_name_int][0]
            real_surname = real_names[real_name_int][1]
            post = "".join([noun," ", adj])
            print("Prénom: ", real_name)
            print(post)
            
            #post = random.choice(posts)
            size = random.choice(sizes)
            #name = random.choice(lines).strip()
            #nickname = random.choice(lines).strip()
            submit(url, fill_form(real_name, real_surname, post, size)) 