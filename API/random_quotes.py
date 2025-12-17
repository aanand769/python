import requests

def fetch_random_quotes():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        quotes = data["data"]
        author = quotes["author"]
        content = quotes["content"]
        return author, content 
    else:
        raise Exception("Failed to get data")
    
def main():
    try:
        author, content = fetch_random_quotes()
        print(f"Author: {author} \nQuotes: {content}")
    except Exception as e:
        print(str(e))
        
     
    
if __name__=='__main__':
    main()