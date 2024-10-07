import json
data = {
        "name": "Nguyễn Văn A",
        "age": 19,
        "city": "Thái Bình"
    }  
json_string = json.dumps(data, ensure_ascii=False)
print("Chuỗi JSON:")
print(json_string)
print(type(json_string)) 
print("\nCác giá trị:")
for value in data.values():
        print(value)
