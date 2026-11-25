import requests

URL = "https://geocoding-api.open-meteo.com/v1/search"


def fetch_data(name):
    try:
        response = requests.get(
            URL,
            params={
                "name": name,
                "count": 10,
                "language": "en",
                "format": "json"
            },
            timeout=10
        )

        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                print("Invalid response from API.")
                return None

        elif response.status_code == 404:
            print("Resource not found.")

        elif response.status_code == 429:
            print("Too many requests. Try again later.")

        elif response.status_code >= 500:
            print("Server error.")

        else:
            print(f"Error: {response.status_code}")

        return None

    except requests.exceptions.Timeout:
        print("Request timed out.")
        return None

    except requests.exceptions.ConnectionError:
        print("Connection error.")
        return None

    except requests.exceptions.RequestException:
        print("Request failed.")
        return None


def display_results(results):
    if not results:
        print("\nNo results found.")
        return

    print()

    for i, place in enumerate(results, start=1):
        print(f"{i}. {place.get('name', 'N/A')}")
        print(f"   Country: {place.get('country', 'N/A')}")
        print(f"   Latitude: {place.get('latitude', 'N/A')}")
        print(f"   Longitude: {place.get('longitude', 'N/A')}")
        print()


def filter_by_country(results, country):
    # Ignore uppercase/lowercase differences
    return [
        place for place in results
        if place.get("country", "").lower() == country.lower()
    ]


def main():
    last_results = []

    while True:
        print("\n1. Search")
        print("2. Filter last results by country")
        print("3. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Enter location: ").strip()

            if not name:
                print("Please enter a location.")
                continue

            data = fetch_data(name)

            if data:
                last_results = data.get("results", [])
                display_results(last_results)
            else:
                print("Search failed.")

        elif choice == "2":
            if not last_results:
                print("No previous results.")
                continue

            country = input("Enter country: ").strip()

            filtered = filter_by_country(last_results, country)
            display_results(filtered)

        elif choice == "3":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()