import json
data = {
        "name": "Nguyễn Văn A",
        "age": 19,
        "city": "Thái Bình"
    }
json_string = json.dumps(data, ensure_ascii=False,indent=4)
print("Chuỗi JSON:")
print(json_string)
