# On an typical application, this would instead be a database, in fact
# given more time, this could be a simple SQLite3 database even
class Database:
    def __init__(self):
        self.fields = ["id", "name", "desc", "url", "category"]
        print("Database connection established.")

    # Select the distinct features of a given field in the db
    def select_distinct(self, field):
        key = field
        output = []
        for item in self.storage:
            if item[key] not in output:
                output.append(item[key])
        return output

    #return all records
    def select_all(self):
        return self.storage

    # using a whitelist is a good way to avoid SQL injection, and several other attacks
    # I understand we don't have any risk here, but if it was an actual db...
    def select_where(self, key, value):
        output = []
        #checking 'whitelist'
        if key in self.fields:
            if value in self.select_distinct(key):
                for item in self.storage:
                    if item[key] == value:
                        output.append(item)
        return output

######################
# START OF DATABASE
######################
    storage = [
        {
            "id": 0,
            "name": "Building Windows",
            "desc": "Awesome reflecction for the windows of a building.",
            "url": "winows_building.jpg",
            "category": "building"
        },{
            "id": 1,
            "name": "Restaurant Window",
            "desc": "A man sitting in a local restaurant.",
            "url": "through_window.jpg",
            "category": "people"
        },{
            "id": 2,
            "name": "Snow Building",
            "desc": "A building through the snow",
            "url": "snow_building.jpg",
            "category": "building"
        },{
            "id": 3,
            "name": "A Cold Night",
            "desc": "People walking downtown on a cold winter night",
            "url": "night_outdoor.jpg",
            "category": "people"
        },{
            "id": 4,
            "name": "Misty City",
            "desc": "Almost from another world.",
            "url": "mist.jpg",
            "category": "building"
        },{
            "id": 5,
            "name": "Building of Glass",
            "desc": "Amazing patterns on the side of a Toronto building.",
            "url": "glass_building.jpg",
            "category": "building"
        },{
            "id": 6,
            "name": "CN Tower Reflection",
            "desc": "The CN Tower visible in the reflection of a glass building.",
            "url": "cntower_building.jpg",
            "category": "building"
        }
    ]
