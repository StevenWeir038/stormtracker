import cartopy.crs as ccrs  # Provides library to display an unprojected (lat/lon) map in a matplotlib axes
import cartopy.feature as cfeature # Gives access to border features
import matplotlib.pyplot as plt  # the Figure object acts as a container for the display output

'''
Hurricanes occur in the Gulf of Mexico, make a function to display a map of the area
to reduce repeat of code
'''

# Create a PlateCaree Cartopy projection. Ths is the default projection for displaying lat/long coordinates
proj = ccrs.PlateCarree()

# Create a Matplotlib figure instance with axes containing PlateCaree default map projection
fig = plt.figure(figsize=(8, 8))  # create a figure of size 10x10 (representing the page size in inches)
ax = plt.axes(projection=proj)  # create an axes object in the figure, using a PlateCarre projection for plotted data

# Add coastlines and US state boundaries for users spatial context
ax.add_feature(cfeature.STATES.with_scale('50m'), linewidth=0.5, edgecolor='k')
ax.add_feature(cfeature.BORDERS.with_scale('50m'), linewidth=1.0, edgecolor='k')
ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=1.0, edgecolor='k')

# Set extent to Gulf Coast
ax.set_extent([-100, -70, 18, 37], proj)  # long min, long max, lat min, lat max boundary coordinate values

#save the figure as a map.png with a dpi of 200
fig.savefig('stormtrackermap.png', bbox_inches='tight', dpi=300)