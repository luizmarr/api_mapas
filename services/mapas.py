from geopy.geocoders import Nominatim

class Mapas:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="myGeocoder")

    def geocode(self, endereco):
        location = self.geolocator.geocode(endereco)
        if location:
            reverse_location = self.geolocator.reverse(
                (location.latitude, location.longitude),
                language="pt"
            )

            pais = reverse_location.raw.get("address", {}).get("country")

            return {
                "endereco": location.address,
                "latitude": location.latitude,
                "longitude": location.longitude,
                "pais": pais,
                "cep": reverse_location.raw.get("address", {}).get("postcode")
            }
        else:
            return None 
        

