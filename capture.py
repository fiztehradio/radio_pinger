from gopro.gopro import GoPro

camera = GoPro.GoPro()

print("Status")
print(camera.status)

# camera.poweron()

camera.photo()
camera.capture()

# camera.sleep()

from pymongo import MongoClient

client = MongoClient()

for item in client.gopro.photos.find({},{'_id':0}):
    print("item", item)
    query = {'dt':
        {'$gt': item['dt']}
    }
    print("query", query)
    search = client.gopro.gpx.find_one(query, {'_id':0})
    print("search", search)
    print("update", item.update(search))
    print("client", client.gopro.process.save(item))
