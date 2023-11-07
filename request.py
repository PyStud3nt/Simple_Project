import requests

urlinput = input("Give me a url to check it for you : ")

with open("file.txt", "r") as wd:
    red = wd.readlines()
    for url in red:
        url = urlinput.format(url.strip())
        req = requests.get(url , timeout = 5)
        stat = req.status_code
        if stat == 200:
            message = "open"
            print(f"{stat} {url}: {message}")
        else:
            message = "close" 
            print(f"{stat} {url}: {message}")

    




# req = requests.get(url)
# req2 = requests.head(url)
# def code():
#     if req.status_code == 200:
#         print("\b" + "  success ! ")
#     elif req.status_code != 200:
#         print("\n" , "not found")

# code()
# print(req2.text)

