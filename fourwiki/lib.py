import requests, re
import webbrowser



def try_me():
    # returns a random four four wiki page
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnlimit": "444",
        "rnnamespace": "0",
    }
    request = S.get(url=URL, params=PARAMS)
    data = request.json()
    page_to_open = 'https://en.wikipedia.org/?curid='
    random_list = data["query"]["random"]

    for i in range(len(random_list)):
        fourmatch = re.fullmatch(r"(\b\w[-?']?\w[-?']?\w[?']?\w\b[!?]?\s?)+(\(\w{4}\))?", random_list[i]['title'])
        if fourmatch:
            print(f"Read four Wiki page: {random_list[i]['title']}")
            webbrowser.open(f'{page_to_open}{random_list[i]["id"]}')
            break
        return random_list[i]['title']
