import cartopy.crs as ccrs  # Provides library to display an unprojected (lat/lon) map in a matplotlib axes
import cartopy.feature as cfeature # Gives access to border/colour features
import matplotlib.pyplot as plt  # the Figure object acts as a container for the display output
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER  # to display gridlines
import matplotlib.ticker as mticker  # use to display gridlines
import numpy as np
import pandas as pd


'''
RAW DATA SOURCE
'''
raw_data = r"C:\Users\weir_\OneDrive\Documents\GitHub\stormtrackerproj\stormtracker\hurdat2Melissa2025.txt"  # file loc


'''
GLOBAL VARIABLES [accessible to whole module each time an instance of plt is called]
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
FUNCTIONS
'''

'''
MAP DISPLAY FUNCTIONS
'''
# Create a blank plt figure instance with axes containing PlateCaree default map projection
fig = plt.figure(figsize=(8, 11))  # create a figure of size 8x11 (representing the page size in inches)
ax = plt.axes(projection=proj)  # use a PlateCarre projection in the axes object
ax = displaymap(ax) # create an axes object in the figure
savefig(fig)  # save an output file to view

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
DATA PROCESSING FUNCTIONS
'''
def importdatafromcsv():
    '''
    Step #2- Open & read data from downloaded file on local drive
    '''
    raw_data = r"C:\Users\weir_\OneDrive\Documents\GitHub\stormtrackerproj\stormtracker\hurdat2Melissa2025.txt"
    return raw_data


def createdataframefromcsv():
    '''
    Step #3 - Create a DataFrame object from csv file:
    Credit to geeksforgeeks.org at https://www.geeksforgeeks.org/python/creating-a-dataframe-using-csv-files/
    for guidance creating a dataframe from a csv file.
    '''

    dataframe = pd.read_csv(raw_data)  # import pandas at top of module
    print("Step 3 Test - Create Dataframe from raw data file".upper())
    print("OUTPUT SUCCESSFUL")
    print(dataframe.to_string())  # test #3 - view sample of dataframe obj in terminal based on csv file on local drive
    return dataframe  # make dataframe available to other functions


def datetimeconverter(dataframe):
    '''
    Convert DateTime series in column 1 from string to datetime format. Note, this could have been done with
    ETL software before step 1 but I wanted to demonstrate this could be done programmatically.
    https://stackoverflow.com/questions/32204631/how-to-convert-string-to-datetime-format-in-pandas
    Solution supported by - rad15f | Source - https://stackoverflow.com/a/77848930
    '''
    dataframe["DateTime"] = pd.to_datetime(dataframe["DateTime"], format="mixed", errors="coerce")
    print("Step 4 Test - Check if string to datetime conversion in col 1 successful")  # delete after testing
    print(f"Data type in Col 1 = {dataframe["DateTime"].dtype}".upper())  # delete after testing


def displaydataframe(dataframe):
    '''
    Step #5 Iterate through dataframe rows and display latitude and longitude series values on terminal for checking.
    https://stackoverflow.com/questions/23330654/update-a-dataframe-in-pandas-while-iterating-row-by-row
    Solution supported by - Mihai Chelaru | https://stackoverflow.com/a/48951427
    Small dataset that we only want to read and not modify therefore ok to manually iterate
    using .itertuples() method instead of using .at() method or vectorizing.
    Credit also to https://www.datacamp.com/tutorial/pandas-iterate-over-rows
    '''
    print("Step 5 Test - Check no missing values in lat/long data by displaying on terminal".upper())
    print("OUTPUT SUCCESSFUL")
    for row in dataframe.itertuples(index=False):
        print(f"DateTime = {row.DateTime}, Latitude = {row.Latitude}, Longitude ={row.Longitude}")