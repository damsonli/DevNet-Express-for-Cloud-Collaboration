from ciscosparkapi import CiscoSparkAPI

api = CiscoSparkAPI(access_token="Your_Access_Token")

rooms = api.rooms.list()

for room in rooms:
    if room.title == "IT-Pros Learning":
        api.rooms.delete(room.id)
    else:
        print(room.title)
