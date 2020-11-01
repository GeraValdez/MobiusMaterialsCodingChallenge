import requests

BASE = "http://127.0.0.1:5000/"

response_get = requests.get(BASE + "bom/1001")
print(response_get.json())

response_put = requests.put(BASE + "bom/1001", {"model":"core.bomitem", "pk":10005, 
               "uuid":"f0as8c69-1b3c-7943-89fc-e10vb863x8z7",
               "created_at":"2020-10-31T00:17:23.815Z",
               "updated_at":"2020-10-31T00:17:23.815Z",
               "is_active":"true",
               "bom":1003,
               "quantity":4,
               "specific_part":10005,
               "item_unit_cost":"1.2000"})

print(response_put.text)
