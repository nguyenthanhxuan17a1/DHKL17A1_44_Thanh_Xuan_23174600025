import json
json_string = '{"name": "Nguyễn Văn  A", "age": 19, "city": "Thái Bình"}'
json_object = json.loads(json_string)
print("Dữ liệu dưới dạng đối tượng Python:")
print(json_object)
