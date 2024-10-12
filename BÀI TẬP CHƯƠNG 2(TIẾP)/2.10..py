import json

data = '''
{
    "company": {
        "name": "CTCP NTX",
        "address": "256 Trần Hưng Đạo",
        "employees": [
            {"name": "Nguyễn Văn A", "unit": "Sales"},
            {"name": "Lê Thị B", "unit": "HR"},
            {"name": "Trần Văn C", "unit": "BA"},
            {"name": "Đinh Thị D", "unit": "IT"},
            {"name": "Đỗ Văn E", "unit": "HR"},
            {"name": "Phạm Văn H", "unit": "IT"}
        ]
    }
}
'''
data = json.loads(data)
company = data["company"]

unit_stats = {}
for emp in company["employees"]:
    unit_stats[emp["unit"]] = unit_stats.get(emp["unit"], 0) + 1
print(f"Tên công ty: {company['name']}")
print(f"Địa chỉ: {company['address']}")
print(f"Tổng số nhân viên: {len(company['employees'])}")
print("Thống kê nhân viên theo đơn vị:")
for unit, count in unit_stats.items():
    print(f"- {unit}: {count} nhân viên, {count / len(company['employees']) * 100:.2f}%")