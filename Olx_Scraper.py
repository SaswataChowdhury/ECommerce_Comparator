import requests
from bs4 import BeautifulSoup


baseurl = "https://www.olx.in"


def get_product_details(url) :
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    r = requests.get(url, headers = headers)
    sp = BeautifulSoup(r.content, "lxml")
    titles, prices, links, images = [], [], [], []

    page = sp.find_all('li', {'data-aut-id' : "itemBox"})
    for item in page :
        for a in item.find_all('a') :
            links.append(baseurl + a['href'])

    page = sp.find_all('span', {'data-aut-id' : "itemPrice"})
    prices = [price.text.strip().replace(' ', '') for price in page]

    page = sp.find_all('span', {'data-aut-id' : "itemTitle"})
    titles = [t.text for t in page]

    page = sp.find_all('figure', {'data-aut-id' : "itemImage"})

    for item in page :
        img = item.select_one('img')
        images.append(img['src'])

    print(len(titles), len(prices), len(links), len(images))
    return [{"Title" : titles[i],
             "Price" : prices[i], 
             "Link" : links[i],
             "Image Link" : images[i]}
             for i in range(0, min(len(prices), 20))]



def processQuery(query) :
    url = baseurl + "/items/q-"
    s = query.split(' ')
    for word in s :
        url += word + "-"
    #print(url)
    detail = get_product_details(url[: -1])
    
    print(len(detail))
    for pair in detail :
        print("Title : ", pair["Title"])
        print("Price : ", pair["Price"])
        print("Link : ", pair["Link"])
        print("Image Link : ", pair["Image Link"], "\n")

    return detail    


# def main() :
#     query = input('>Search : ')
#     processQuery(query.lower())        


# main()    