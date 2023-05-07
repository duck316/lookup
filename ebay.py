import requests
from bs4 import BeautifulSoup

articulos = []
depure_conten = list()
test = list()
show_conten = list()
final_list = list()

def ebayscrao(articulo):
    url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312&_nkw={articulo}n&_sacat=0"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")


    def has_data_search(tag):
        return tag.has_attr("data-viewport")


    results = soup.find_all(has_data_search)

    for items in results:
        try:
            articulos.append({"imagen": items.find("img", loading={"eager"})["src"],
                "titulo": items.find("div", class_="s-item__title").get_text(),
                              "condicion": items.find("div", class_="s-item__subtitle").get_text(),
                              "prices": items.find("span", class_="s-item__price").get_text(),
                              "itlink": items.find("a", class_={"s-item__link"})["href"]
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

    for ebayitem in test:
        if ebayitem not in depure_conten:
            depure_conten.append(ebayitem)


