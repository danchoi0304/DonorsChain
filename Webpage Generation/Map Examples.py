import folium
from folium.plugins import AntPath
from DC_Functions.Folder_Move import *


# This example shows that the donated item went from Sciencenter to Warren Wood Apartments.

# Latitude and longitude coordinates of the points
start_coords = (37.3861, 126.6389)
end_coords = (42.449879, -76.504051)

# Create a map centered around the starting coordinates
m = folium.Map(location=start_coords, zoom_start=5)

Donor = "Joung Hwa Choi"
Receiver = "Sciencenter"

# Add markers for the starting and ending points
folium.Marker(location=start_coords, popup = Donor).add_to(m)
folium.Marker(location=end_coords, popup = Receiver).add_to(m)

# latitude longitude coordinates of the lines
cords = [(37.3861, 126.6389), (42.449879, -76.504051)]


# create antpaths and add to map
ant_path = AntPath(locations = cords, color ='blue', delay = 1000)

ant_path.add_to(m)

# Save the map to an HTML file
m.save('proto_map.html')
move_to_outputs("proto_map.html")


a = folium.Map(location=[37.3861, 126.6389],
                    zoom_start=5)

# latitude longitude coordinates of the lines
cords = [(37.3861, 126.6389), (42.449879, -76.504051)]


# create antpaths and add to map
ant_path = AntPath(locations = cords, color ='blue', delay = 1000)

ant_path.add_to(a)

# save the map object as a html
a.save('antmap.html')

a
move_to_outputs("antmap.html")
