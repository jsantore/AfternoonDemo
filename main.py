import requests
import secrets

def get_data(url: str):
    final_data = []
    final_url = f"{url}&api_key={secrets.api_key}&page=8"
    response = requests.get(final_url)
    if response.status_code != 200:
        print(response.text)
        return []
    json_data = response.json()
    page_data = json_data["results"]
    final_data.extend(page_data)
    return final_data


def main():
    url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=id,school.state,school.name"
    all_data = get_data(url)
    for school_data in all_data:
        print(school_data)

if __name__ == '__main__':
    main()