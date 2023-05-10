import requests
from bs4 import BeautifulSoup

articulos = []
depure_conten = list()
test = list()
show_conten = list()
final_list = list()

# Funcion para hacer el Scrapping
def ebayscrao(articulo):

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw={articulo}&_sacat=0&_ipg=120"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all(class_="s-item__wrapper clearfix")

    # Lee linea por linea el codigo HTML para hacer la busqueda de objetos deseados
    for items in results:
        try:
            articulos.append({
                "imagen": items.find("img")["src"],
                "titulo": items.find("div", class_="s-item__title").get_text(),
                "condicion": items.find("div", class_="s-item__subtitle").get_text(),
                "prices": items.find("span", class_="s-item__price").get_text(),
                "itlink": items.find("a", class_="s-item__link")["href"]
                              })

        except Exception as e:
            # print("Exception: {}".format(e))
            pass

    # Elimina un elemento especifico agregado por la pagina scrapeada y depura los elementos duplicados
    for i in range(len(articulos)):
        if articulos[i]["titulo"] == "Shop on eBay":
            articulos[i] = ""
        else:
            show_conten.append(articulos[i])
            for ebayitem in show_conten:
                if ebayitem not in depure_conten:
                    depure_conten.append(ebayitem)




