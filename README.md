# stormtracker

## Setup & Installation
Note that screenshots below are meant as a May 2026 guide and may become outdated over time.
The following instructions will assist in recreating and building on the project.

### Github Repository – Part 1

#### Creating a Github account
If you are new to [Github](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) you'll need to create an account to **fork** the project.

#### Forking the Repository
- [**Fork**](https://github.com/StevenWeir038/stormtracker/tree/main) the stormtracker repository and provide an optimal description.

![Fork Repo1 img](/imgs/setupimgs/forkrepo1.png)

- Name the forked repository ***stormtracker*** and provide an optional description. Select **Copy the main branch only** then **Create Fork**.

![Fork Repo2 img](/imgs/setupimgs/forkrepo2.png)

You now have a copy of the project in your own *origin* repository.  Commits and branching made on your local machine should be made to the origin.  Note, changes here will not affect the forked *upstream* repository.

### Environment Setup – Anaconda
Anaconda Navigator is a free open-source package management system.  It is used by developers to simplify the installation, running and updating of data science software and their dependencies.

It can be installed using this [link](https://www.anaconda.com/docs/getting-started/anaconda/install/overview).

#### About the `environment.yml` file
Before setting up the Integrated Development Environment (IDE) to develop your code, setup a separate environment for your new project in Anaconda.

This prevents potential version conflicts between libraries used on different projects.
A version of the *environment.yml* file is in the forked repository but if you need to create one at a future date do the following.

- Create a new text document locally in the root directory of your project.
- **Open With** a simple text editor such as [**Notepad**](https://apps.microsoft.com/detail/9msmlrh6lzf3?hl=en-GB&gl=GB) or [**Notepad++**](https://notepad-plus-plus.org/downloads/v8.9.1/). 
- **Copy & Paste** the below text and then save as *environment.yml*

```python
name: simplehurricanetracker
channels:
  - conda-forge
  - defaults
dependencies:
  - python>3.9
  - pandas
  - geopandas
  - cartopy
  - folium
```
- **Close** the file.

Select **Anaconda Navigator** from the **Start** menu to open application.

![envsetup 1 img](/imgs/setupimgs/envsetup1.png)

**Select Environments** then **Import From** the `environment.yml` file you just created on the local drive.

![envsetup 2 img](/imgs/setupimgs/envsetup2.png)

Give your new environment a meaningful name (e.g. *simplehurricanetracker*,  I later changed this to *stormtracker*)

Select Python version 3.13.12 as the language from the dropdown menu then **Import**. (note this may take several minutes)

#### Install Anaconda Prompt
As the project developed it became clear that other libraries could be useful/necessary.  These were manually installed in **conda** using the command line interface (CLI) in **Anaconda Prompt** per each developer’s instructions. 

Install **Anaconda Prompt** from **Anaconda Navigator / Home / Install** menu. It can be opened from the Windows Start menu in the same way as Anaconda Navigator.

![envsetup 3 img](/imgs/setupimgs/envsetup3.png)

In the **Start** menu, you should find a prompt with the same name as your environment name (*stormtracker*).

Alternatively you can open the standard **Anaconda Prompt** and activate your new project environment (*stormtracker*) instead of using the default base environment with the following code.

```python
conda activate stormtracker
```

Note the environment change in the command line.

![envsetup 4 img](/imgs/setupimgs/envsetup4.png)

### Github Repository – Part 2

#### Clone Repository
**Clone** the forked repository with the help of this [guide](https://www.w3schools.com/git/git_clone.asp)

Cloning is like downloading your origin version of the project from GitHub to a selected directory in your local machine.

Use **Anaconda Prompt** to select the **correct environment** and **navigate to the directory** where you want to **clone** the origin repository on your local machine using `cd filepath`.
Next type `git clone URL` were *URL* is the weblink to your origin repository and *my folder* is the local drive directory containing your project.

![clone repo 1 img](/imgs/setupimgs/clonerepo1.png)

### Manual Installs
Additional Packages were added including [*matplotlib/](https://matplotlib.org/stable/install/index.html), [*tropycal*](https://anaconda.org/channels/conda-forge/packages/tropycal/overview), [*hurdat2py*](https://pypi.org/project/hurdat2py/0.3.2/ ) and [*geopy*](https://geopy.readthedocs.io/en/stable/#installation).
Note *hurdat2py* and *geopy* were installed using *pip* rather than directly through *conda*.
The above packages mainly handle data retrieval, processing, display. Geopy has s useful library to help us write analytical functions.

![manual installs 1 img](/imgs/setupimgs/manualinstalls1.png)

![manual installs 2 img](/imgs/setupimgs/manualinstalls2.png)

![manual installs 3 img](/imgs/setupimgs/manualinstalls3.png)

![manual installs 4 img](/imgs/setupimgs/manualinstalls4.png)

### IDE - PyCharm
Download the free version of [Pycharm](https://www.jetbrains.com/pycharm/download/?section=windows).
#### Configuring PyCharm to work with the repository and new environment

Open **Pycharm** From the desktop/**Start** menu or directly from **Anaconda Navigator/Home**. Ensure correct environment (*stormtracker*) is selected.
![ide pycharm 1 img](/imgs/setupimgs/idepycharm1.png)

From **Menu** select **File / New Project**.

In the New Project dialog box configure the interpreter.  This enables the IDE to run the correct code for the project when prompted using the conda environment settings.

For **Location**, select the filepath to the cloned repository

Leave **Create Git Repository** blank as you have already forked and cloned the repository in previous steps.

Choose *Conda* for **Select Existing Custom Environment**.

**Path to Conda** is the .bat file location on your local machine where you installed conda.

Set the Environment to stormtracker which you previously set up.

Select **Create**.

![ide pycharm 2 img](/imgs/setupimgs/idepycharm2.png)

Select **Create from Existing Sources** if prompted by a new dialog box.
You should get a similar result as below showing the files in the cloned directory.

![ide pycharm 3 img](/imgs/setupimgs/idepycharm3.png)

#### Configuring PyCharm to run a specific Script
For Pycharm to run the correct script we need to configure the *Run* button. (`Shift + F10`)

Select **Current File / Edit Configurations** to open the **Run/Debug Configurations** dialog.

![ide pycharm 4 img](/imgs/setupimgs/idepycharm4.png)

Add a new Configuration

![ide pycharm 5 img](/imgs/setupimgs/idepycharm5.png)

Set the following parameters:
    - Select **Python**, 
    - change **Name** to *stormtracker* 
    - set **Script** to the location with file name of the scrip to run.
    - Set the **Working directory** to where the script is saved on your local machine
    - Select **OK**.

It should look similar to the below image.

![ide pycharm 6 img](/imgs/setupimgs/idepycharm6.png)

The **Current File** will change the *stormtracker* script when you select Run instead of the default *main*.

![ide pycharm 7 img](/imgs/setupimgs/idepycharm7.png)

Selecting the green '*Play* button or pressing Alt+F10 on the keyboard will run the code from the stormtracker file.

Alternatively, to run the code in the terminal, type `python stormtracker.py`.
Ensure you are working in the correct *conda* environment and local file directory in the terminal.


## Importing Data and ETL
It is necessary to process data before it can be displayed any map.
In this project a csv file was downloaded and processed with FME before being used to create a Pandas Dataframe.
`Latitude` and `Longitude` dataframe series (columns) were then decimalized to enable the creation 
of a geodatabase with a geometry field.

### Step 1 - Download csv file from NOAA and prep using FME
Data was imported in `.csv` format from the HURDAT2 database downloaded from 
['NOAA / AOML](https://www.aoml.noaa.gov/hrd/hurdat/hurdat2.html) to a local drive location.

FME was used to transform raw data prior to use, keeping the 1st 7 columns of data and stripping blank spaces from each.

To understand data format, refer to the following [document](https://www.aoml.noaa.gov/hrd/hurdat/hurdat2-format.pdf).

- **1st** column = date
- **2nd** column = time
- **3rd** column = system category
- **4th** column = Latitude
- **5th** column = Longitude
- **6th** column = Max Sustained Windspeed
- **7th** column = minimum pressure (millibars)

### Step 2 - Open & Read data from downloaded file on local drive
A simple function was used to read a csv data file locally.
The filepath in the form of a raw `r-string` was used to reference the location in memory.
```python
def importdatafromcsv():
'''
Step #2- Open & read data from downloaded file on local drive
'''
raw_data = r"C:\Users\weir_\OneDrive\Documents\GitHub\stormtrackerproj\stormtracker\hurdat2Melissa2025.txt"

return raw_data
```

### Step 3 - Create a DataFrame object from the imported .csv file
Importing the Pandas library enables the creation a Pandas Dataframe object.
Create and assign a dataframe object using the .csv data and display in terminal to review.
```python
import pandas as pd
```

```python
dataframe = pd.read_csv(raw_data)
print(dataframe.to_string())
```


## Testing

### Setup and Configuration

#### Test 1 - Check PyCharm IDE is configured to run *stormtracker* script
**Status** - PASS
![test 1 ide pycharmconfigtest img](/imgs/testimgs/test1_idepycharmconfig.png)

#### Test 2 - Create a simple output map of the Gulf of Mexico
**Status** - PASS
![test 2 map display img](/imgs/testimgs/test2_mapdisplay.png)

#### Test 3 - Add gridlines map of the Gulf of Mexico
**Status** - PARTIAL SUCCESS

Gridlines displaying but labels on top and right of axes still visible despite being set to `False`
after grid params have been set to True.
`xlabels_top` and `ylabels_right` are depreciated and replaced with `top_labels` and `right_labels`.
Same Boolean applied.


```Python
gridparams = {'crs': ccrs.PlateCarree(central_longitude=0),
              'draw_labels':True, 'linewidth':0.5,
              'color':'gray', 'alpha':1, 'linestyle':'--'}
```

``` Python
    gl.xlabels_top = False  # turn off x labels on top of axes
    gl.ylabels_right = False  # turn off y labels on right of axes
```

![test 3 add gridlines with labels img](/imgs/testimgs/test3_addgridlineswithlabels.png)

**Status** - RESOLVED
```Python
    gl.top_labels = False  # turn off x labels on top of axes
    gl.right_labels = False  # turn off y labels on right of axes
```

![test 3 add gridlines with labels resolved img](/imgs/testimgs/test3_addgridlineswithlabelsresolved.png)

<<<<<<< HEAD
#### Test 4 - Test data connection to hurdat2 database
**Status** - PASS

Hurdat2 database has been saved to local drive in case.  If data not found search reverts to online database.
Functionally confirmed as only 2025 storm data retained in local file and "Katrina" storm query is from 2005.

```Python
import hurdat2py

hd2 = hurdat2py.Hurdat2(r"C:\Users\weir_\OneDrive\Documents\GitHub\stormtrackerproj\stormtracker.hurdat2data2025.txt")

# Storm object:
storm = hd2['katrina', 2005]

print(storm.to_dataframe())
```

![test 4 test data connection to hurdat2 database img](/imgs/testimgs/test4_testhurdat2dataconnection.png)
=======
#### Test 4 -  Create a DataFrame object from the imported .csv file
**Status** - RESOLVED

Importing the Pandas library enables the creation a Pandas Dataframe object.
```python
dataframe = pd.read_csv(raw_data)
print(dataframe.to_string())
```

![test 4 create pandas database from csv file](/imgs/testimgs/test4_createpandasdatabase.png)

#### Test 5 -  Convert DateTime series in column 1 from string to datetime format
**Status** - RESOLVED

```python
def datatimeconverter(dataframe):
    '''
    Convert DateTime series in column 1 from string to datetime format to demonstrate programmatic steps.
    '''
    dataframe["DateTime"] = pd.to_datetime(dataframe["DateTime"], format="mixed", errors="coerce")
    print("Step 4 Test - Check if string to datetime conversion in col 1 successful")  # delete after testing
    print(f"Data type in Col 1 = {dataframe["DateTime"].dtype}".upper())  # delete after testing
```

![test 5 string to datetime conversion of a pandas data series](/imgs/testimgs/test5_stringtodatetimeconversioninpandasseries.png)


#### Test 6 -  Print Latitudes/Longitudes to terminal to check no missing values
**Status** - RESOLVED

```python
'''
Iterate through dataframe rows and display latitude and longitude series values.
'''
print("Step 5 Test - Check no missing values in lat/long data by displaying on terminal".upper())
print("OUTPUT SUCCESSFUL")
for row in dataframe.itertuples(index=False):
    print(f"DateTime = {row.DateTime}, Latitude = {row.Latitude}, Longitude ={row.Longitude}")
```
![test 6 Iterate through dataframe rows and display latitude and longitude column values](/imgs/testimgs/test6_iteratedataframetocheckseriesvalues.png)

#### Test 7 -  Parse & Decimalise Latitude/Longitude series values and update dataframe
**Status** - RESOLVED
For N/S/E/W coordinates check:

1. input value is a string
2. display input value to check
3. interim value used in loop is a list
4. display interim value to check
5. output interim value is a string as has last index character removed and minus added before 1st index if `S` or `W`. 
6. display output value
7. display updated value in the series after parsing commas

**North Coordinates**

![test 7a latitude parser north coordinates](/imgs/testimgs/test7a_latitudeparsernorthcoordinates.png)

**South Coordinates**

![test 7b latitude parser south coordinates](/imgs/testimgs/test7b_latitudeparsersouthcoordinates.png)

**East Coordinates**

![test 7clatitude parser east coordinates](/imgs/testimgs/test7c_latitudeparsereastcoordinates.png)

**West Coordinates**

![test 7d latitude parser west coordinates](/imgs/testimgs/test7d_latitudeparserwestcoordinates.png)

#### Test 8 -  Convert Pandas Dataframe to GeoPandas Dataframe by adding a geometry series using decimalised Lats/Longs
**Status** - RESOLVED
```python
geodataframe = gpd.GeoDataFrame(
    dataframe, geometry=gpd.points_from_xy(dataframe.Longitude, dataframe.Latitude), crs="EPSG:4326")
print(geodataframe.to_string())
```
**Before**

![test 8a](/imgs/testimgs/test8a_pandasdataframestructurecomplete.png)

**After**

![test 8b](/imgs/testimgs/test8b_geopandasgeodataframestructurecomplete.png)

#### Test 9 -  Add a customised north arrow
**Status** - RESOLVED
```python
    north_arrow(
        ax,
        location="upper left",
        rotation={"crs": proj, "reference": "center"},
        shadow=False,
        scale=0.4,
        label={"position": "bottom", "text": "N", "fontsize": 10},
    )
```

![test 9](/imgs/testimgs/test9_addnortharrow.png)