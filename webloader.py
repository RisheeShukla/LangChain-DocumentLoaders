from langchain_community.document_loaders  import WebBaseLoader
loader=WebBaseLoader("https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5W4NNB/ref=sr_1_1?crid=2N8F3ULMDVIGI&dib=eyJ2IjoiMSJ9.LZTZP63lERir-20SCySs3uz2jc2FVwu03rqOIlEm7_AwvO-O8BdFAXgQ28KOv86odr4SdMNDDTvLOHbCINiJVY6HVz5oAoqM5sPiGdJWLqYwdIDwFmWr4IEny0t1I4Pzr-yAJbCxJNDF-iq3ld8lppCoQ5z95SwWKUpxV6QN17B1uf-ji7RVixjkqhm3SDIPhoMQg6nZWKeuilJR2MZjLQM_KVzGATjnH0tjsN_ba08.9ahRJDrjomzUYKck-iD6jCf0fGv9kPiPMTdhcUIHBbE&dib_tag=se&keywords=Apple%2Bair&nsdOptOutParam=true&qid=1753883290&sprefix=apple%2Bair%2Caps%2C286&sr=8-1&th=1")
docs=loader.load()
print(len(docs))
print(docs[0].metadata)
