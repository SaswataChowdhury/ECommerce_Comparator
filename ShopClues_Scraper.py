import requests
from bs4 import BeautifulSoup


baseurl = "https://bazaar.shopclues.com/"


def get_product_details(url) :
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    r = requests.get(url, headers = headers)
    sp = BeautifulSoup(r.content, "lxml")
    titles, prices, links, images = [], [], [], []

    page = sp.find_all('div', {'class' : 'column col3 search_blocks'})
    for item in page :
        for a in item.find_all('a') :
            links.append("https:" + a['href'])
            for h in a.find_all('h2') :
                titles.append(h.text)

    page = sp.find_all('span', {'class' : 'p_price'})
    prices = [price.text.strip().replace(' ', '') for price in page]

    page = sp.find_all('div', {'class' : 'img_section'})
    for item in page :
        for img in item.find_all('img') :
            images.append(img['data-img'])


    print(len(titles), len(prices), len(links), len(images))
    return [{"Title" : titles[i],
             "Price" : prices[i], 
             "Link" : links[i],
             "Image Link" : images[i]}
             for i in range(0, min(20, len(links)))]
       

def processQuery(query) :
    url = baseurl + "search?q="
    s = query.split(' ')
    for word in s :
        url += word + "+"

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