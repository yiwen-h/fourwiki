import requests, re
import webbrowser


def try_me():
    # returns a random four four wiki page
    req = requests.Session()
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnlimit": "444",
        "rnnamespace": "0",
    }
    request = req.get(url=url, params=params)
    data = request.json()
    page_to_open = "https://en.wikipedia.org/?curid="
    random_list = data["query"]["random"]
    status = False

    for i in range(len(random_list)):
        fourmatch = re.fullmatch(
            r"(\b\w[-?']?\w[-?']?\w[?']?\w\b[!?]?\s?)+(\(\w{4}\))?",
            random_list[i]["title"],
        )
        if fourmatch:
            status_text = f"Yayy done! Read four Wiki page: {random_list[i]['title']}"
            link = f'{page_to_open}{random_list[i]["id"]}'
            # webbrowser.open_new_tab(f'{page_to_open}{random_list[i]["id"]}')
            status = True
            break
    if status == False:
        status_text = "Oops, can't find four wiki page! Once more?"
        link = "https://somefourwikipage.herokuapp.com/"
    return link, status_text
