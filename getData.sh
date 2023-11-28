#!/bin/bash

curl --request GET 'https://catalog.gamepass.com/sigls/v2?id=fdd9e2a7-0fee-49f6-ad69-4354098401ff&language=en-us&market=CA' > gameIds.json
# ids=$( cat gameIds.json | tr ',' '\n' | tail -n +6 | sed s/{\"id\":\"// | sed s/\"}// | sed s/]// | tr '\n' ',' )
rm gameIdList
rm gameIdList.json
python3 getIdList.py
rm gameIds.json
ids=$( cat gameIdList )
# echo $ids
# echo "https://displaycatalog.mp.microsoft.com/v7.0/products?bigIds=${ids}&market=US&languages=en-us&MS-CV=DGU1mcuYo0WMMp"
curl --request GET "https://displaycatalog.mp.microsoft.com/v7.0/products?bigIds=${ids}&market=US&languages=en-us&MS-CV=DGU1mcuYo0WMMp" > gameInfo
rm gameIdList
python3 cleanGameData.py
rm gameInfo
