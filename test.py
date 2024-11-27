import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature

# add north sea bounds
north_sea_bounds = {
    'min_lon': 2.5,
    'max_lon': 6.5,
    'min_lat': 51.0,
    'max_lat': 53.5
}

stations = [
    {'name': 'Station 2', 'lat': 52.0, 'lon': 4.0, 'temperature': 9.8, 'salinity': 35.2},
    {'name': 'Station 3', 'lat': 52.5, 'lon': 5.0, 'temperature': 11.5, 'salinity': 35.7},
    {'name': 'Station 4', 'lat': 53.0, 'lon': 6.0, 'temperature': 10.0, 'salinity': 35.0},
    {'name': 'Station 5', 'lat': 51.5, 'lon': 3.0, 'temperature': 10.2, 'salinity': 35.5},
    {'name': 'Station 6', 'lat': 52.0, 'lon': 4.0, 'temperature': 9.8, 'salinity': 35.2},
    {'name': 'Station 7', 'lat': 52.5, 'lon': 5.0, 'temperature': 11.5, 'salinity': 35.7},
    {'name': 'Station 8', 'lat': 53.0, 'lon': 6.0, 'temperature': 10.0, 'salinity': 35.0},
    {'name': 'Station 9', 'lat': 51.5, 'lon': 3.0, 'temperature': 10.2, 'salinity': 35.5},
    {'name': 'Station 10', 'lat': 52.0, 'lon': 4.0, 'temperature': 9.8, 'salinity': 35.2}
]

# create a DataFrame with the stations
df = pd.DataFrame(stations)

# add jitter to the coordinates
jitter_strength = 0.5
df['lat'] += np.random.uniform(-jitter_strength, jitter_strength, size=len(df))
df['lon'] += np.random.uniform(-jitter_strength, jitter_strength, size=len(df))

# create a scatter plot with the stations using cartopy
plt.figure(figsize=(10, 8))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([north_sea_bounds['min_lon'], north_sea_bounds['max_lon'], north_sea_bounds['min_lat'], north_sea_bounds['max_lat']], crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.COASTLINE)
ax.add_feature(cartopy.feature.BORDERS, linestyle=':')
ax.add_feature(cartopy.feature.LAND, edgecolor='black')
ax.add_feature(cartopy.feature.OCEAN)
ax.scatter(df['lon'], df['lat'], transform=ccrs.PlateCarree(), color='red', s=100)

# add some gridlines for lat/lon
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_right = False


plt.title('Stations in the North Sea')


# save the figure in 600 dpi
plt.savefig('/home/fricour/dataViz/coherens_workshop/stations_in_north_sea.png', dpi=600)

# plot figure
plt.show()