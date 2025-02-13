import requests 

def get_data(url):
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"{e} occurred")
        return "error"
    
val = get_data("https://jsonplaceholder.typicode.com/posts")

print(type(val))


    

    
    

