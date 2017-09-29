from ciscosparkapi import CiscoSparkAPI

api = CiscoSparkAPI(access_token="Your_Access_Token")

#print(api.people.me())

message1 = "**I am an IT-Professional, and I have completed this challenge!!!**"

room = api.rooms.create("IT-Pros Learning")
print(room.id)

api.messages.create(roomId=room.id, text=message1)

all_messages = api.messages.list(room.id)
for msg in all_messages:
    api.messages.delete(msg.id)

api.rooms.delete(room.id)