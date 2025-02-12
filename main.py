import requests

websites_list = [
    {
        "url": "https://wwebdesign.co.uk",
        "string_to_match": "W Web Design"
    }, {
        "url": "https://google.com/nothere",
        "string_to_match": "Google"
    },{
        "url": "https://facebook.com",
        "string_to_match": "Facebook"
    }
]

for website in websites_list:
    print()
    print(f"Checking website: {website['url']}")
    response = requests.get(website['url'])

    if response.status_code != 200:
        print(f"Error on site! Status code received: {response.status_code}")
    else:
        print(f"Status code is OK! Status code received: {response.status_code}")
        if website['string_to_match'] not in response.text:
            print(f"{website['string_to_match']} not found!")
        else:
            print(f"{website['string_to_match']} found")

# This is my edited code
# This is code on my new branch
