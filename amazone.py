import requests
from bs4 import BeautifulSoup

articulos = []
depure_conten = list()
test = list()
show_conten = list()
final_list = list()

def amascrap(articulo):

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    r = requests.get(
        f"https://www.amazon.com/s?k={articulo}", headers=headers)  # , proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content, "html.parser")

    def has_data_search(tag):
        return tag.has_attr("data-component-type")

    results = soup.find_all(has_data_search)

    for items in results:
        try:
            articulos.append({
                "imagen": items.find("img", {"class": "s-image"})["src"],
                "titulo": items.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"}).get_text(),
                "condicion": items.find("span", {"aria-label": "FREE delivery Fri, May 12 "}).get_text(),
                "prices": items.find("span", {"class": "a-offscreen"}).get_text(),
                "itlink": "https://www.amazon.com/" + items.find("a",
                class_={"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})["href"]
                              })

        except Exception as e:
            # print("Exception: {}".format(e))
            pass

    for i in range(len(articulos)):
        if articulos[i]['titulo'] == "Shop on eBay":
            articulos[i] = ""

        else:
            show_conten.append(articulos[i])
            if len(show_conten) < 10 + 1:
                for show in show_conten:
                    test.append(show)

    for amaitem in test:
        if amaitem not in depure_conten:
            depure_conten.append(amaitem)

