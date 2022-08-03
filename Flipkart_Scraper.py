import requests
from bs4 import BeautifulSoup


baseurl = "https://www.flipkart.com/search?q="


def get_product_details(url):
    r = requests.get(url)
    sp = BeautifulSoup(r.content, "lxml")
    links, prices, titles, images, aux = [], [], [], [], []
    i, j = 0, 0

    page = sp.select("div._30jeq3")
    prices = [price.text.strip().replace(' ', '') for price in page]
    prices = prices[0 : - 5]

    for a in sp.find_all('a', {'rel': True}):
        aux.append(baseurl[0 : 24] + a['href'])
    
    for img in sp.find_all('img', {'alt' : True, 'src' : True}):
            images.append(img['src'])
    images = images[len(images) - 5 - len(prices) : len(images) - 5]
        
    print(len(prices), len(aux), len(images))
    if len(aux)  - 6 == len(prices) :
        page = sp.select("div._4rR01T")
        titles = [t.text.strip() for t in page]
       
        #print(len(titles))
        while i < len(aux) - 6:
            links.append(aux[i])
            i += 1

    else :
        for a in sp.find_all('a', {'rel': True, 'title' : True}):
            titles.append(a['title'])

        #print(len(titles))
        while j < len(prices) and i < len(aux) - 6:
            links.append(aux[i])
            i += 3     
            j += 1
    #print("\n")
    
    return [{"Title" : titles[i], 
            "Price" : prices[i], 
            "Link" : links[i],
            "Image Link" : images[i]} 
            for i in range(0, min(20, len(links)))]    


def processQuery(query) :
    url = baseurl
    s = query.split(' ')
    for word in s :
        url += word + "+"

    detail = get_product_details(url[: - 1])

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