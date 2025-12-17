import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    data = response.json()
   
    if data["success"] and "data" in data:
        user_data = data["data"]["data"][1  ]
        '''username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        gender = user_data["gender"]
        return username, country, gender'''
        return user_data
    else:
        raise Exception("Failed to fetch data")
        

def main():
    try:
        userdata = fetch_random_user()
        print(userdata)
        # username, country, gender= fetch_random_user()
        # print(f"Username: {username} \nCountry: {country} \nGender: {gender}")
    except Exception as e:
        print(str(e))

    
if __name__=="__main__":
    main()
 

