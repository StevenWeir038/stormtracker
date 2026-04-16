import cartopy.crs as ccrs  # Provides library to display an unprojected (lat/lon) map in a matplotlib axes
import cartopy.feature as cfeature # Gives access to border/colour features
import matplotlib.pyplot as plt  # the Figure object acts as a container for the display output
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER  # to display gridlines
import matplotlib.ticker as mticker  # use to display gridlines
import numpy as np



'''
Global variables [accessible to whole module each time an instance of plt is called]
'''

# Create a PlateCaree Cartopy projection. Ths is the default projection for displaying lat/long coordinates
proj = ccrs.PlateCarree()

# Define dictionary to set grid parameters for display on stormtracker map.
# CREDIT to https://python.nicolasbarrier.fr/maps/carto.html

#give gridlines same projection.  Set grid style parameters
gridparams = {'crs': ccrs.PlateCarree(central_longitude=0),
              'draw_labels':True, 'linewidth':0.25,
              'color':'gray', 'alpha':1, 'linestyle':'-'}

'''
Functions
'''

def displaymap(ax):
    '''
    Render same map boundary, fill and extent values and gridlines to an instance of plt.axes
    '''

    # Add coastlines and US state boundaries for users spatial context
    ax.add_feature(cfeature.STATES.with_scale('50m'), linewidth=0.5, edgecolor='gray')
    ax.add_feature(cfeature.BORDERS.with_scale('50m'), linewidth=1.0, edgecolor='black')
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=1.0, edgecolor='black')

    # Add a light green land and blue sea colour to map for readability
    ax.add_feature(cfeature.LAND.with_scale('50m'), linewidth=0.5, facecolor='#a5e987', edgecolor='face')
    ax.add_feature(cfeature.OCEAN.with_scale('50m'), linewidth=0.5, facecolor='#74ccf4', edgecolor='face')

    # Add bespoke gridlines to map
    gl = ax.gridlines(**gridparams)
    gl.top_labels = False  # turn off x labels on top of axes
    gl.right_labels = False  # turn off y labels on right of axes
    gl.xlocator = mticker.FixedLocator(np.arange(-180, 180 + 40, 10))
    gl.ylocator = mticker.FixedLocator(np.arange(-90, 90 + 10, 10))
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER

    #Add title to map
    ax.title.set_text('Hurricane Track Map | Gulf of Mexico')

    # Set extent to Gulf Coast
    ax.set_extent([-100, -60, 17, 37], proj)  # long min, long max, lat min, lat max boundary coordinate values

    # return instance of map for use in matplotlib axes object
    return ax


def savefig(fig):
    '''
    Save the figure as stormtrackermap.png with a dpi of 300
    '''
    fig.savefig('stormtrackermap.png', bbox_inches='tight', dpi=300)


'''
Create a blank plt figure instance with axes containing PlateCaree default map projection
'''
fig = plt.figure(figsize=(8, 8))  # create a figure of size 8x8 (representing the page size in inches)
ax = plt.axes(projection=proj)  # use a PlateCarre projection in the axes object
ax = displaymap(ax) # create an axes object in the figure
savefig(fig)  # save an output file to view


