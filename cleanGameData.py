import json

gameInfoF = open('gameInfo')

w = open("gameData.json", "w")

gameInfo = json.load(gameInfoF)
gameInfoF.close()

newData = {}
currObj = {}

for i, val in enumerate(gameInfo['Products']):
    currObj['id'] =                 val['ProductId']
    currObj['price'] =              val['DisplaySkuAvailabilities'][0]['Availabilities'][0]['OrderManagementData']['Price']['ListPrice']
    currObj['category'] =           val['Properties']['Category']
    currObj['categories'] =         val['Properties']['Categories']
    currObj['ratingCount'] =        val['MarketProperties'][0]['UsageData'][2]['RatingCount']
    currObj['rating'] =             val['MarketProperties'][0]['UsageData'][2]['AverageRating']
    currObj['endDate'] =            val['DisplaySkuAvailabilities'][0]['Availabilities'][0]['Conditions']['EndDate']
    currObj['releaseDate'] =        val['MarketProperties'][0]['OriginalReleaseDate']
    currObj['developerName'] =      val['LocalizedProperties'][0]['DeveloperName']
    currObj['publisherName'] =      val['LocalizedProperties'][0]['PublisherName']
    currObj['title'] =              val['LocalizedProperties'][0]['ProductTitle']
    currObj['description'] =        val['LocalizedProperties'][0]['ProductDescription']
    currObj['shortDescription'] =   val['LocalizedProperties'][0]['ShortDescription']
    newData[currObj['id']] = currObj.copy()

w.write(json.dumps(newData, indent=4))

w.close()
