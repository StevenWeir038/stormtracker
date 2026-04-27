import cartopy.crs as ccrs  # Provides library to display an unprojected (lat/lon) map in a matplotlib axes
import cartopy.feature as cfeature # Gives access to border/color features
import matplotlib.pyplot as plt  # the Figure object acts as a container for the display output
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER  # to display gridlines
from matplotlib_map_utils.core.north_arrow import north_arrow  # used to draw north arrow
from matplotlib_scalebar.scalebar import ScaleBar  # used to draw scalebar
import matplotlib.ticker as mticker  # use to display gridlines
import pandas as pd
import geopandas as gpd
import numpy as np


'''
GLOBAL VARIABLES [accessible to whole module each time an instance of plt is called]
'''
#data source
raw_data = r"C:\Users\weir_\OneDrive\Documents\GitHub\stormtrackerproj\stormtracker\hurdat2Melissa2025.txt"


'''
DATA PROCESSING FUNCTIONS
'''
def importdatafromcsv():
    '''
    Read data from downloaded file on local drive
    '''
    raw_data = r"C:\Users\weir_\OneDrive\Documents\GitHub\stormtrackerproj\stormtracker\hurdat2Melissa2025.txt"
    return raw_data


def createdataframefromcsv(rawdata):
    '''
    Step #3 - Create a DataFrame object from csv file:
    Credit to geeksforgeeks.org at https://www.geeksforgeeks.org/python/creating-a-dataframe-using-csv-files/
    for guidance creating a dataframe from a csv file.
    '''

    dataframe = pd.read_csv(raw_data)
    return dataframe


def datetimeconverter(dataframe):
    '''
    Convert DateTime series in column 1 from string to datetime format. Note, this could have been done with
    ETL software before step 1 but I wanted to demonstrate this could be done programmatically.
    https://stackoverflow.com/questions/32204631/how-to-convert-string-to-datetime-format-in-pandas
    Solution supported by - rad15f | Source - https://stackoverflow.com/a/77848930
    '''
    dataframe["DateTime"] = pd.to_datetime(dataframe["DateTime"], format="mixed", errors="coerce")


def displaydataframe(dataframe):
    '''
    Iterate through dataframe rows and display latitude and longitude series values on terminal for checking.
    https://stackoverflow.com/questions/23330654/update-a-dataframe-in-pandas-while-iterating-row-by-row
    Solution supported by - Mihai Chelaru | https://stackoverflow.com/a/48951427
    Small dataset that we only want to read and not modify therefore ok to manually iterate
    using .itertuples() method instead of using .at() method or vectorizing.
    Credit also to https://www.datacamp.com/tutorial/pandas-iterate-over-rows
    '''
    print("Check no missing values in lat/long data by displaying on terminal".upper())
    for row in dataframe.itertuples(index=False):
        print(f"DateTime = {row.DateTime}, Latitude = {row.Latitude}, Longitude ={row.Longitude}")


def latitudelongitudeparser(dataframe):
    '''
    Iterate through dataframe and decimalise Latitude series values
    Convert value from string to list to access indexes
    If last index value contains "S" for South, remove letter in last index and add "-" before the 1st index value
    Convert result back to a string and remove commas
    '''
    for i in dataframe.index:  # loop to iterate through rows in pandas dataframe
        # set local variables INSIDE loop for north, south and minus vals & ref the location of each iterable object
        north = "N"
        south = "S"
        minus = "-"
        raw_lat_val = dataframe.at[i, "Latitude"]
        raw_long_val = dataframe.at[i, "Longitude"]

        # iterate and change latitude values
        if len(raw_lat_val) >= 5 and raw_lat_val[-1] == north:  # recheck there are at least 5 chars

            interim_lat_val = list(raw_lat_val)
            interim_lat_val.pop()  # remove the letter value in 4th index
            dec_lat_val = ",".join(str(x.replace(",", "")) for x in interim_lat_val)  # convert using list comprehension
            dataframe.at[i, "Latitude"] = dec_lat_val.replace(",", "")  # remove "," from string

        elif len(raw_lat_val) >= 5 and raw_lat_val[-1] == south:  # recheck there are at least 5 chars
            interim_lat_val = list(raw_lat_val)
            interim_lat_val.pop()  # remove value in 4th index
            interim_lat_val.insert(0, minus)  # insert minus before 1st index
            dec_lat_val = ",".join(str(x.replace(",", "")) for x in interim_lat_val)  # convert using list comprehension
            dataframe.at[i, "Latitude"] = dec_lat_val.replace(",", "")  # remove "," from string

            # iterate and change longitude values
            if len(raw_long_val) >= 5 and raw_long_val[-1] == north:  # recheck there are at least 5 chars
                interim_long_val = list(raw_long_val)
                interim_long_val.pop()  # remove the letter value in 4th index
                dec_long_val = ",".join(
                    str(x.replace(",", "")) for x in interim_long_val)  # convert using list comprehension
                dataframe.at[i, "longitude"] = dec_long_val.replace(",", "")  # remove "," from string

            elif len(raw_long_val) >= 5 and raw_long_val[-1] == south:  # recheck there are at least  5 chars
                interim_long_val = list(raw_long_val)
                interim_long_val.pop()  # remove value in 4th index
                interim_long_val.insert(0, minus)  # insert minus before 1st index
                dec_long_val = ",".join(
                    str(x.replace(",", "")) for x in interim_long_val)  # convert using list comprehension
                dataframe.at[i, "longitude"] = dec_long_val.replace(",", "")   # remove "," from string

    return dataframe


def creategeodataframe(dataframe):
    '''
    Create a geo-dataframe (gdf) from dataframe so points can be displayed on a map
    Create geometry column in gdf object from Lat/Long dataframe columns
    Credit to GeoPandas documentation at https://geopandas.org/en/stable/gallery/create_geopandas_from_pandas.html
    for guidance creating a GeoPandas geo-dataframe from a Pandas dataframe.
    '''
    geodataframe = gpd.GeoDataFrame(
        dataframe,
        geometry=gpd.points_from_xy(dataframe.Longitude, dataframe.Latitude),
        crs="EPSG:4326")
    print(geodataframe.to_string())  # delete after testing

    return geodataframe


'''
MAP DISPLAY FUNCTIONS
'''
def savefig(image):
    '''
    Save the figure as stormtrackermap.png with a dpi of 300
    '''
    fig.savefig('stormtrackermap1.png', bbox_inches='tight', dpi=300)


def displaymap():
    '''
    Render a map of the Gulf of Mexico
    '''
    proj= ccrs.PlateCarree()
    # create a figure of size 8x11 (representing the page size in inches)
    # Create a blank plt figure instance with axes containing PlateCaree default map projection

    fig, ax = plt.subplots(1,1, figsize=(8, 11), subplot_kw=dict(projection=proj))
    # Add coastlines and US state boundaries for users spatial context
    ax.add_feature(cfeature.STATES.with_scale('50m'), linewidth=0.5, edgecolor='gray')
    ax.add_feature(cfeature.BORDERS.with_scale('50m'), linewidth=1.0, edgecolor='black')
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=1.0, edgecolor='black')

    # Add a light green land and blue sea colour to map for readability
    ax.add_feature(cfeature.LAND.with_scale('50m'), linewidth=0.5, facecolor='#a5e987', edgecolor='face')
    ax.add_feature(cfeature.OCEAN.with_scale('50m'), linewidth=0.5, facecolor='#74ccf4', edgecolor='face')

    # Add bespoke gridlines to map
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,)
    gl.top_labels = False  # turn off x labels on top of axes
    gl.right_labels = False  # turn off y labels on right of axes
    gl.xlocator = mticker.FixedLocator(np.arange(-180, 180 + 40, 10))
    gl.ylocator = mticker.FixedLocator(np.arange(-90, 90 + 10, 10))
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER


    # Set extent to Gulf Coast
    ax.set_extent([-100, -60, 17, 37], crs=proj)  # long min, long max, lat min, lat max boundary coordinate values

    # Add title to map
    ax.title.set_text('Storm Track Map \n Gulf of Mexico')

    # add and customise north arrow
    # Credit moss_xyz - https://stackoverflow.com/a/79346562
    north_arrow(
        ax,
        location="upper left",
        rotation={"crs": proj, "reference": "center"},
        shadow=False,
        scale=0.4,
        label={"position": "bottom", "text": "N", "fontsize": 10},
    )

    # add a simple scalebar
    # For PlateCarree (degrees), dx is usually the size of 1 meter in degrees.
    # Approximately 111km per degree at equator, changes with latitude.
    # Using a local conversion factor is safer.
    scale_bar = ScaleBar(
        111e3,  # e3 to display as km
        "m",
        location="lower left",
        label="Approx\n Scale",
        label_loc="left",
        scale_loc="bottom",
        color="black",
        font_properties={"family": "sans-serif", "size": 10}
    )
    ax.add_artist(scale_bar)


    # save the figure to a .png image
    image = fig.savefig('stormtrackermap.png', bbox_inches='tight', dpi=300)


    # Show plot in Pycharm without figure disappearing off-screen
    # Source - https://stackoverflow.com/a/46225722, Posted by tairen
    plt.show(block=True)
    plt.interactive(False)

    # return image of map to pass to savefig function
    return image


'''
CALL FUNCTIONS
'''
displaymap()
savefig(image)
