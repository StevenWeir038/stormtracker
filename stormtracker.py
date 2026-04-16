import cartopy.crs as ccrs  # Provides library to display an unprojected (lat/lon) map in a matplotlib axes
import cartopy.feature as cfeature # Gives access to border features
import matplotlib.pyplot as plt  # the Figure object acts as a container for the display output


'''
Global variables [accessible to whole module each time an instance of plt is called]
'''

# Create a PlateCaree Cartopy projection. Ths is the default projection for displaying lat/long coordinates
proj = ccrs.PlateCarree()


'''
Functions
'''

def displaymap(ax):
    '''
    Render same map boundary, fill and extent values to an instance of plt.axes
    '''

    # Add coastlines and US state boundaries for users spatial context
    ax.add_feature(cfeature.STATES.with_scale('50m'), linewidth=0.5, edgecolor='gray')
    ax.add_feature(cfeature.BORDERS.with_scale('50m'), linewidth=1.0, edgecolor='black')
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=1.0, edgecolor='black')

    # Add a light green land and blue sea colour to map for readability
    ax.add_feature(cfeature.LAND.with_scale('50m'), linewidth=0.5, facecolor='#a5e987', edgecolor='face')
    ax.add_feature(cfeature.OCEAN.with_scale('50m'), linewidth=0.5, facecolor='#74ccf4', edgecolor='face')

    # Set extent to Gulf Coast
    ax.set_extent([-100, -60, 17, 37], proj)  # long min, long max, lat min, lat max boundary coordinate values

    # return instance of map for use in matplotlib axes object
    return ax


def savefig(fig):
    '''
    Save the figure as  stormtrackermap.png with a dpi of 300
    '''
    fig.savefig('stormtrackermap.png', bbox_inches='tight', dpi=300)


'''
Create a Matplotlib figure instance with axes containing PlateCaree default map projection
'''
fig = plt.figure(figsize=(8, 8))  # create a figure of size 8x8 (representing the page size in inches)
ax = plt.axes(projection=proj)  # create an axes object in the figure, use a PlateCarre projection for plotted data
ax = displaymap(ax)
savefig(fig)