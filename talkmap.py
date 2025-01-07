import glob
import getorg
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

def get_location(geocoder, location, max_retries=3):
    for i in range(max_retries):
        try:
            return geocoder.geocode(location)
        except GeocoderTimedOut:
            if i == max_retries - 1:
                print(f"Failed to geocode {location} after {max_retries} attempts")
                return None
            time.sleep(1)

def create_talkmap():
    files = glob.glob("*.md")
    geocoder = Nominatim(user_agent="academic-website")
    location_dict = {}

    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.read()
            if 'location: "' in lines:
                loc_start = lines.find('location: "') + 11
                lines_trim = lines[loc_start:]
                loc_end = lines_trim.find('"')
                location = lines_trim[:loc_end]
                
                if location and location not in location_dict:
                    geo_location = get_location(geocoder, location)
                    if geo_location:
                        location_dict[location] = geo_location
                        print(f"Located: {location} -> {geo_location}")
                    time.sleep(1)  # Be nice to the geocoding service

    if location_dict:
        m = getorg.orgmap.create_map_obj()
        getorg.orgmap.output_html_cluster_map(location_dict, 
                                            folder_name="../talkmap",
                                            hashed_usernames=False)
        print("Talkmap created successfully!")
    else:
        print("No locations found to map")

if __name__ == "__main__":
    create_talkmap()




