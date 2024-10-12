import requests
respone = requests.get("https://jsonplaceholder.typicode.com/comments?postId=1")
json_data = respone.json()
count=0
for post in json_data:
    id = post["id"]
    if id ==1:
        print("name: ",post["name"])
        print("email: ",post["email"])
        if count <3:
            print("body: ",post["body"])
            count+=1
        else:
            break
        
    