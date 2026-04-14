# stormtracker

### Setup & Installation
Note that screenshots below are meant as a May 2026 guide and may become outdated over time.
The following insructions will assist in recreating and building on the project.

### Github Repository – Part 1

#### Creating a Github account
If you are new to [Github](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) you'll need to create an account to **fork** the project.

#### Forking the Repository
- [**Fork**](https://github.com/StevenWeir038/stormtracker/tree/main) the stormtracker repository and provide an optimal description.

![Fork Repo1 img](/setupimgs/forkrepo1.png)

- Name the forked repository ***stormtracker*** and provide an optional description. Select **Copy the main branch only** then **Create Fork**.

![Fork Repo2 img](/setupimgs/forkrepo2.png)

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
  - python>3.9<3.13
  - pandas
  - geopandas
  - cartopy
  - folium
```
- **Close** the file.

Select **Anaconda Navigator** from the **Start** menu to open application.

![envsetup 1 img](/setupimgs/envsetup1.png)

**Select Environments** then **Import From** the `environment.yml` file you just created on the local drive.

![envsetup 2 img](/setupimgs/envsetup2.png)

Give your new environment a meaningful name (e.g. *simplehurricanetracker*,  I later changed this to *stormtracker*)

Select Python version 3.13.12 as the language from the dropdown menu then **Import**. (note this may take several minutes)

#### Install Anaconda Prompt
As the project developed it became clear that other libraries could be useful/necessary.  These were manually installed in **conda** using the command line interface (CLI) in **Anaconda Prompt** per each developer’s instructions. 

Install **Anaconda Prompt** from **Anaconda Navigator / Home / Install** menu. It can be opened from the Windows Start menu in the same way as Anaconda Navigator.

![envsetup 3 img](/setupimgs/envsetup3.png)

In the **Start** menu, you should find a prompt with the same name as your environment name (*stormtracker*).

Alternatively you can open the standard **Anaconda Prompt** and activate your new project environment (*stormtracker*) instead of using the default base environment with the following code.

```python
conda activate stormtracker
```

Note the environment change in the command line.

![envsetup 4 img](/setupimgs/envsetup4.png)

### Github Repository – Part 2

#### Clone Repository
**Clone** the forked repository with the help of this [guide](https://www.w3schools.com/git/git_clone.asp)

Cloning is like downloading your origin version of the project from GitHub to a selected directory in your local machine.

Use **Anaconda Prompt** to select the **correct environment** and **navigate to the directory** where you want to **clone** the origin repository on your local machine using `cd filepath`.
Next type `git clone URL` were *URL* is the weblink to your origin repository and *my folder* is the local drive directory containing your project.

![clone repo 1 img](/setupimgs/clonerepo1.png)

### Manual Installs
Additional Packages were added including [matplotlib](https://matplotlib.org/stable/install/index.html), [tropycal](https://anaconda.org/channels/conda-forge/packages/tropycal/overview) and [hurdat2py](https://pypi.org/project/hurdat2py/0.3.2/ ).
Note hurdat2py was installed using *pip* rather than directly through *conda*.
The above packages handle data retrieval, processing and display, thus allowing us to focus on writing analytical functions.

![manual installs 1 img](/setupimgs/manualinstalls1.png)

![manual installs 2 img](/setupimgs/manualinstalls2.png)

![manual installs 2 img](/setupimgs/manualinstalls3.png)

### IDE - PyCharm
Download the free version of [Pycharm](https://www.jetbrains.com/pycharm/download/?section=windows).
#### Configuring PyCharm to work with the repository and new environment

Open **Pycharm** From the desktop/**Start** menu or directly from **Anaconda Navigator/Home**. Ensure correct environment (*stormtracker*) is selected.
![ide pycharm 1 img](/setupimgs/idepycharm1.png)

From **Menu** select **File / New Project**.

In the New Project dialog box configure the interpreter.  This enables the IDE to run the correct code for the project when prompted using the conda environment settings.

For **Location**, select the filepath to the cloned repository

Leave **Create Git Repository** blank as you have already forked and cloned the repository in previous steps.

Choose *Conda* for **Select Existing Custom Environment**.

**Path to Conda** is the .bat file location on your local machine where you installed conda.

Set the Environment to stormtracker which you previously set up.

Select **Create**.

![ide pycharm 2 img](/setupimgs/idepycharm2.png)

Select **Create from Existing Sources** if prompted by a new dialog box.
You should get a similar result as below showing the files in the cloned directory.

![ide pycharm 3 img](/setupimgs/idepycharm3.png)

#### Configuring PyCharm to run a specific Script
For Pycharm to run the correct script we need to configure the *Run* button. (`Shift + F10`)

Select **Current File / Edit Configurations** to open the **Run/Debug Configurations** dialog.

![ide pycharm 4 img](/setupimgs/idepycharm4.png)

Add a new Configuration

![ide pycharm 5 img](/setupimgs/idepycharm5.png)

Set the following parameters:
    - Select **Python**, 
    - change **Name** to *stormtracker* 
    - set **Script** to the location with file name of the scrip to run.
    - Set the **Working directory** to where the script is saved on your local machine
    - Select **OK**.

It should look similar to the below image.

![ide pycharm 6 img](/setupimgs/idepycharm6.png)

The **Current File** will change the *stormtracker* script when you select Run instead of the default *main*.

![ide pycharm 7 img](/setupimgs/idepycharm7.png)

Ensure you are working in the correct *conda* environment and local file directory in the terminal.

Selecting the green '*Play* button or pressing Alt+F10 on the keyboard will run the code from the stormtracker file.

Alternatively, to run the code in the terminal, type `python stormtracker.py`.