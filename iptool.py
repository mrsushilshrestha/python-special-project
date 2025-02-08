import requests
from opencage.geocoder import OpenCageGeocode

def get_ip_details(ip_address):
    response = requests.get(f"http://ip-api.com/json/{ip_address}")
    data = response.json()

    if data['status'] == 'success':
        details = {
            'IP': data['query'],
            'Country': data['country'],
            'Region': data['regionName'],
            'City': data['city'],
            'Latitude': data['lat'],
            'Longitude': data['lon'],
            'ISP': data['isp'],
            'Organization': data['org'],
            'Area Code': data.get('zip', 'N/A'),
            'Country Code': data['countryCode'],
            'Continent Code': data.get('continent', 'N/A'),
            'ASN': data['as'],
            'Timezone': data['timezone'],
            'Accuracy': data.get('accuracy', 'N/A')
        }

        # Geolocation for the address using Latitude and Longitude
        key = 'API_KEY'
        geocoder = OpenCageGeocode(key)
        results = geocoder.reverse_geocode(data['lat'], data['lon'])
        if results:
            details['Address'] = results[0]['formatted']

        return details
    else:
        return {'error': 'Invalid IP or service unavailable'}

def print_ip_details(ip_address):
    details = get_ip_details(ip_address)
    
    if 'error' in details:
        print(details['error'])
    else:
        print(f"{'-'*30} HOST DETAILS {'-'*30}")
        print(f"Country: {details['Country']}")
        print(f"Country Code: {details['Country Code']}")
        print(f"Area Code: {details['Area Code']}")
        print(f"Organization Name: {details['Organization']}")
        print(f"Country Code3: {details['Country Code']}")
        print(f"Continent Code: {details['Continent Code']}")
        print(f"ASN: {details['ASN']}")
        print(f"Region: {details['Region']}")
        print(f"Latitude: {details['Latitude']}")
        print(f"Longitude: {details['Longitude']}")
        print(f"IP: {details['IP']}")
        print(f"Accuracy: {details['Accuracy']}")
        print(f"Timezone: {details['Timezone']}")
        print(f"Organization: {details['Organization']}")
        print(f"{'-'*30} COUNTRY DETAILS {'-'*30}")
        print(f"Country: {details['Country']}")
        print(f"Country Code: {details['Country Code']}")
        print(f"IP: {details['IP']}")
        print(f"Timezone: {details['Timezone']}")
        print(f"Address: {details['Address']}")

# Example IP to get details for
ip_address = "Target_IP"
print_ip_details(ip_address)
