import requests


def get_data(url: str):
    final_data = []
    response = requests.get(url)

    if response.status_code != 200:
        print(response.text)
        return []
    return final_data


def main():
    url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=id,school.state,school.name"
    all_data = get_data(url)
    print(all_data)

if __name__ == '__main__':
    main()