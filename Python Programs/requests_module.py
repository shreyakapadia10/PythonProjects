import requests

web = requests.get('https://financialmodelingprep.com/api/v3/quote/AAPL?apikey=demo')

print(web.text)
print("Status code:", web.status_code)

# url = "https://financialmodelingprep.com/api/v3/key-executives/AAPL?apikey=demo"
# API_KEY = "demo"
#
# data = {
#     "api_dev_key": API_KEY,
#     "p1": 4,
#     "p2": 5
# }
#
# post_req = requests.post(url=url, data=data)
# print(post_req.status_code)
# print(post_req.text)

payload = {'user_name': 'admin', 'password': 'password'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)