import cartopy.crs as ccrs  # Provides library to display an unprojected (lat/lon) map in a matplotlib axes
import cartopy.feature as cfeature # Gives access to border/color features
import matplotlib.pyplot as plt  # the Figure object acts as a container for the display output
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER  # to display gridlines
from matplotlib_map_utils.core.north_arrow import north_arrow  # used to draw north arrow
from matplotlib_scalebar.scalebar import ScaleBar  # used to draw scalebar
import matplotlib.ticker as mticker  # use to display gridlines
import pandas as pd
import geopandas as gpd
import numpy as np  # use to display gridlines
from shapely.geometry import LineString  # req for reprojecting geographic geometry values from degrees to metres


'''
GLOBAL VARIABLES [accessible to whole module each time an instance of plt is called]
'''

# data source
datasource = r"C:\Users\weir_\OneDrive\Documents\GitHub\stormtrackerproj\stormtracker\hurdat2Melissa2025.txt"


'''
DATA PROCESSING FUNCTIONS
REWORKED - as creating dataframe is done once, no need to break different stages of build down to separate functions
'''

def createGeodataframe(datasource):
    '''
    # STEP 1
    PURPOSE
    Load data into a table from a delimited text file.
    Create a Pandas DataFrame object to hold tabular data read from a delimited .csv file from the local drive:

    CREDIT
    geeksforgeeks.org at https://www.geeksforgeeks.org/python/creating-a-dataframe-using-csv-files/ for guidance
    creating a dataframe from a csv file.

    INPUT PARAMETERS
    'datasource' setup as a global variable accessible to any function in the module. 'datasource' parameter is a
    'raw string' which is passed into the function. This tells pandas library where to read file.


    EXPECTED OUTPUT
    A new instance of a Pandas dataframe object named 'dataframe' containing data read from .csv file.
    '''
    dataframe = pd.read_csv(datasource)

    '''
    # STEP 2
    PURPOSE
    Convert datetime series in column 1 from 'string' to 'datetime' format.
    Note, this could have been done with ETL software before step 1 though I wanted to demonstrate this can be done 
    programmatically.
    
    CREDIT
    https://stackoverflow.com/questions/32204631/how-to-convert-string-to-datetime-format-in-pandas
    Solution supported by - rad15f | Source - https://stackoverflow.com/a/77848930
    
    INPUT PARAMETERS
    dataframe["DateTime"] series
    
    EXPECTED OUTPUT
    Text value is converted into a datetime value. Whilst displayed as a string, it is stored as a datetime number
    '''
    dataframe["DateTime"] = pd.to_datetime(dataframe["DateTime"], format="mixed", errors="coerce")
    print(f"Data type in Col 1 = {dataframe["DateTime"].dtype}".upper())  # check data format of updated datetime series


    '''
    STEP 3
    PURPOSE
    Display 'dataframe' in terminal to allow manual checking for missing/extraneous data.
    Then iterate through dataframe rows and display datetime, latitude and longitude series values 
    for closer inspection.
    Note, this is a read only operation to support human readability and has no impact on changing dataframe values.
    
    CREDIT
    Solution supported by - Mihai Chelaru | https://stackoverflow.com/a/48951427 and 
    https://stackoverflow.com/questions/23330654/update-a-dataframe-in-pandas-while-iterating-row-by-row
    https://www.datacamp.com/tutorial/pandas-iterate-over-rows
    
    INPUT PARAMETERS
    'dataframe' object
    
    EXPECTED OUTPUT
    Whole 'dataframe' is displayed in terminal using .string() instead of .head() method. 
    Don't want to see ellispes as need to review whole table. 
    Note, as dataset is small dataset it is acceptable to manually iterate using .itertuples() method. 
    On larger tables seek to use a vectorised solution.
    '''
    print("Dataframe Output".upper())
    print(dataframe.to_string())

    print("Alternative View. \n"
          "Check no missing values in lat/long data by displaying on terminal".upper())
    for row in dataframe.itertuples(index=False):  # iterate each row of data
        print(f"DateTime = {row.DateTime}, Latitude = {row.Latitude}, Longitude ={row.Longitude}")  # print tgt series


    '''
    STEP #4
    PURPOSE
    Iterate through 'dataframe' and decimalise 'Latitude' and 'Longitude' series values.
    Decimalised values enable creation of a geometry series in a yet to be created 'geodataframe' object based of the 
    existing dataframe object.  See inline comments for detailed logic.
    
    CREDIT
    freecodecamp.org at https://www.freecodecamp.org/news/python-list-to-string-how-to-convert-lists-in-python
    
    INPUT PARAMETERS
    'local' variables storing 'NESW-' values that are accessed by the inner loop when decimalising string values in 
    dataframe["Latitude"} and dataframe["Longitude"] series.
    
    EXPECTED OUTPUT
    Decimalised values for each row in dataframe["Latitude"} and dataframe["Longitude"] series. 
    Letter on last index of each 'tabular cell' is removed and a minus has been inserted before the first index of 
    Southern and Western hemisphere coordinates.
    Decimalised value replaces the raw value.
    
    Note, degrees run from 180 to 0 to -180 degrees.
    Text string for lats/longs <100 degrees = 5 characters.
    Text string for lats/longs <100 degrees = 6 characters.
    To verify if data is correct there must be at least 5 characters.
    Use a try/else statement within loop to improve error handling in future development.
    
    Note below, a good example of the pros of AI for improving efficiency and readability using list comprehension. 
    Solution not used in project as logic should be human derived for assessment. 
    AI was able to support more concise, pythonic solution shown below.  Ca. 30 lines of code compressed into 2!
    
    dataframe["Latitude"] = dataframe["Latitude"].apply(lambda x: -float(x.strip("W")) if "W" in x else float(x.strip("E")))
    dataframe["Longitude"] = dataframe["Longitude"].apply(lambda x: -float(x.strip("N")) if "N" in x else float(x.strip("S")))
    '''
    for i in dataframe.index:  # loop to iterate through rows in pandas dataframe

        # set local variables INSIDE loop for north, south and minus vals & ref the location of each iterable object
        north = "N"  # north string variable
        south = "S"  # south string variable
        east = "E"  # east string variable
        west = "W"  # west string variable
        minus = "-"  # minus string variable
        raw_lat_val = dataframe.at[i, "Latitude"]  # location of 'Latitude' iterable
        raw_long_val = dataframe.at[i, "Longitude"]  # location of 'Longitude' iterable

        # iterate and update latitude values
        if len(raw_lat_val) >= 5 and raw_lat_val[-1] == north:  # Programmatically check there are at least 5 chars

            interim_lat_val = list(raw_lat_val) # convert 'cell' value to list to manipulate indices within string
            interim_lat_val.pop()  # remove the letter value in 4th index
            dec_lat_val = ",".join(str(x.replace(",", "")) for x in interim_lat_val)  # convert to str using list comp
            dataframe.at[i, "Latitude"] = dec_lat_val.replace(",", "")  # remove "," from string on iterables

        elif len(raw_lat_val) >= 5 and raw_lat_val[-1] == south:  # Programmatically check there are at least 5 chars

            interim_lat_val = list(raw_lat_val) # convert 'cell' value to list to manipulate indices within string
            interim_lat_val.pop()  # remove value in 4th index
            interim_lat_val.insert(0, minus)  # insert minus before 1st index (for S not N values)
            dec_lat_val = ",".join(str(x.replace(",", "")) for x in interim_lat_val)  # convert to str using list comp
            dataframe.at[i, "Latitude"] = dec_lat_val.replace(",", "")  # remove "," from string on iterables

        # iterate and update longitude values
        if len(raw_long_val) >= 5 and raw_long_val[-1] == east:  # Programmatically check there are at least 5 chars

            interim_long_val = list(raw_long_val) # convert 'cell' value to list to manipulate indices within string
            interim_long_val.pop()  # remove the letter value in 4th index
            dec_long_val = ",".join(
                str(x.replace(",", "")) for x in interim_long_val)  # convert to str using list comp
            dataframe.at[i, "longitude"] = dec_long_val.replace(",", "")  # remove "," from string on iterables

        elif len(raw_long_val) >= 5 and raw_long_val[-1] == west:  # Programmatically check there are at least 5 chars

            interim_long_val = list(raw_long_val) # convert 'cell' value to list to manipulate indices within string
            interim_long_val.pop()  # remove value in 4th index (for W not E values)
            interim_long_val.insert(0, minus)  # insert minus before 1st index (for W not E values)
            dec_long_val = ",".join(
                str(x.replace(",", "")) for x in interim_long_val)  # convert to str using list comp
            dataframe.at[i, "longitude"] = dec_long_val.replace(",", "")  # remove "," from string on iterables


    '''
    STEP 5
    PURPOSE
    Create a Geopandas geo-dataframe (gdf) from a Pandas dataframe so points can be displayed on a map
    Geodataframe object contains a geometry column/series derived from dataframe Latitude / Longitude series values. 
    
    CREDIT
    GeoPandas documentation https://geopandas.org/en/stable/gallery/create_geopandas_from_pandas.html
    
    INPUT PARAMETERS
    Pandas 'dataframe' object with decimalised latitude and longitude series values
    
    EXPECTED OUTPUT
    Geopandas 'geodateframe' object with a projected POINT 'geometry' series 
    using dataframe latitude and longitude series values.
    '''
    geodataframe = gpd.GeoDataFrame(
        dataframe,
        geometry=gpd.points_from_xy(dataframe.Longitude, dataframe.Latitude),
        crs="EPSG:4326"
    )  # create a geodataframe with degrees coordinates

    # Use below link to find best fit projection (USA - 84°W to 78°W and GoM OCS) for measuring.
    # https://epsg.org/crs_32167/NAD83-BLM-17N-ftUS.html?sessionkey=kuqo0ksxvxapply
    geodataframe = geodataframe.to_crs(32167)

    # add a length series to geodataframe.
    # geodataframe["Length (km)"] = geodataframe.geometry.length / 1000  # WRONG APPROACH
    print(geodataframe.to_string())  # show geodataframe in terminal
    geodataframe.to_file(
        filename=r"C:\Users\weir_\OneDrive\Documents\GitHub\stormtrackerproj\stormtracker\hurdat2Melissa2025.gdb",
        layer="temptable", driver="OpenFileGDB"
    )  # save geodataframe object to a selected file directory on local disk


    '''
    STEP 6
    PURPOSE
    Convert Point Geometries from GeoPandas geodatabase to Linestring using shapely 

    CREDIT
    Stack Overflow https://stackoverflow.com/questions/66492804/convert-point-geometries-to-linestrings-with-geopandas

    INPUT PARAMETERS
    Using the Geopandas points_from_xy function, create a Linestring from Longitude and Latitude series' from dataframe

    EXPECTED OUTPUT
    A LineString which is actually a list of tuples which can then be passed to displaymap function and plotted to axes.
    
    '''
    # create a linestring object in the geodatabase from a sequence of POINT coordinates
    # CREDIT
    # swatchai https://stackoverflow.com/questions/66492804/convert-point-geometries-to-linestrings-with-geopandas
    # https://gis.stackexchange.com/questions/238533/extracting-points-from-linestring-or-polygon-and-making-dictionary-out-of-them-i
    # https://shapely.readthedocs.io/en/latest/reference/shapely.LineString.html

    # DEBUGGING - length will be calculated in degrees with below code.
    # Need to parse geometry series from geodataframe with transformed projection for calcuations in metres
    points = gpd.points_from_xy(
        geodataframe.Longitude, geodataframe.Latitude)  # create a list of points from the dataframe
    stormtrack = LineString(points)  # create a LineString object named stormtrack from the points

    print(f"Length of 'stormtrack' object= {stormtrack.length}.")  # test to check length before projection transform
    stormtracklist = stormtrack.coords  # converts the coordinate sequence to a list of tuples if using outside Pandas

    # make geodataframe, stormtrack and stormtracklist objects available to other functions
    return geodataframe, stormtrack, stormtracklist


'''
MAP DISPLAY FUNCTIONS
'''

def saveFig(image):
    '''
    PURPOSE
    Save the figure as stormtrackermap.png with a dpi of 300

    INPUT PARAMETERS
    Variable named "image" passed from displaymap() function

    EXPECTED OUTPUTS
    Writes a png file to the local drive for external use
    '''
    fig.savefig('stormtrackermap1.png', bbox_inches='tight', dpi=300)


def displayMap(geodataframe, stormtrack):
    '''
    PURPOSE
    Render a tailored map of the Gulf of Mexico showing path of Storm Melissa (2025)

    INPUT PARAMETERS
    'geodataframe' and 'stormtrack' data created in createGeodataframe(datasource) function where datasource is
    a csv file of observations for Hurricane Melissa (2025)

    EXPECTED OUTPUTS
    A formatted map of GoM with plotted data showing path of Storm Melissa (2025).
    Map is intuitively colored for land and sea with a PlateCaree projection since data is in degrees.
    It also contains gridlines, north arrow, scalebar, legend and a title.

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

    # display track data
    #create a new object to hold passed stormtrack object from geodataframe.
    stormtrack_gdf = gpd.GeoDataFrame(geodataframe,  crs='espg:4326', geometry=stormtrack.geometry)
    ax1 = stormtrack_gdf.plot(style='-o',color="y",ms=4,label="Track",)  # save display parameters to variable
    ax.plot(ax1)  # plot to LineString to axis using preset variables

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
geodataframe = createGeodataframe(datasource)
# create empty instance of storm track list object
stormtracklist = []

def main():
    '''
    Call functions in correct order to read file and display map with plotted geodataframe data.
    '''
    createGeodataframe(datasource)
    displaymap(stormtrack)
    savefig(image)

# run application
main()