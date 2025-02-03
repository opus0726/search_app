import requests

class SearchItems():
    def search(self,keyword,start,site):
        rakuten = Rakuten()
        yahoo = Yahoo()
        genreId = ""
        items = []
        if site == "all":
            items.extend(rakuten.items_search(keyword, genreId, start))
            items.extend(yahoo.items_search(keyword, genreId, start))
        elif site == "rakuten":
            items.extend(rakuten.items_search(keyword, genreId, start))
        elif site == "yahoo":
            items.extend(yahoo.items_search(keyword, genreId, start))

        return items

class Rakuten():
    def __init__(self):
        self.url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601?"
        self.appricationId = "1080638618593042114"
        self.affiliateId = "432a33ac.e1f30558.432a33ad.de61e252"
    
    def items_search(self, keyword, genreId, start):
        items = []
        num = 0
        params = {
            "applicationId": self.appricationId,
            "keyword": keyword,
            "genreId": genreId,
            "format": "json",
            "formatVersion": 1,
            "field" : 1,
            "affiliateId": self.affiliateId,
            "page": start
        }
        res = requests.get(self.url, params=params)
        result = res.json()

        for i in result['Items']:
            images = []
            items.append({
                "name": i['Item']['itemName'],
                "code": "rakuten-"+i['Item']['itemCode'],
                "genre" : i['Item']['genreId'],
                "description": i['Item']['itemCaption'],
                "reviewAverage": i['Item']['reviewAverage'],
                "reviewCount": i['Item']['reviewCount'],
                "url": i['Item']['affiliateUrl'],
                "price": i['Item']['itemPrice']
            })

            for j in i['Item']['mediumImageUrls']:
                images.append(j['imageUrl'])
                
            items[num]['images'] = images
            num += 1

        return items
    
class Yahoo():
    def __init__(self):
        self.url = "https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch"
        self.appricationId = "dj00aiZpPU9hRTdUS0p3TGNDNCZzPWNvbnN1bWVyc2VjcmV0Jng9NTQ-"
        self.affiliateId = "432a33ac.e1f30558.432a33ad.de61e252"
    
    def items_search(self, keyword, genreId, start):
        items = []
        params = {
            "appid": self.appricationId,
            "query": keyword,
            "genre_category_id": genreId,
            "results": 30,
            "start": start
        }
        res = requests.get(self.url, params=params)
        result = res.json()
        for i in result['hits']:
            items.append({
                "name": i['name'],
                "code": "yahoo-"+i['code'],
                "genre" : i['genreCategory']['id'],
                "description": i['description'],
                "reviewAverage": i['review']['rate'],
                "reviewCount": i['review']['count'],
                "url": i['url'],
                "price": i['price'],
                "images": [i['image']['medium']]
            })
        return items
    
class Amazon():
    def __init__(self):
        self.url = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        self.appricationId = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        self.affiliateId = "XXXXXXXX.e1f30558.432a33ad.de61e252"

    def items_search(self, keyword, genreId):
        items = []
        params = {
            "appid": self.appricationId,
            "query": keyword,
            "genre_category_id": genreId,
        }
        res = requests.get(self.url, params=params)
        result = res.json()
        for i in result['hits']:
            items.append({
                "name": i['name'],
                "genre" : i['genreCategory']['id'],
                "description": i['description'],
                "reviewAverage": i['review']['rate'],
                "reviewCount": i['review']['count'],
                "url": i['url'],
                "price": i['price']
            })
        return items
    
