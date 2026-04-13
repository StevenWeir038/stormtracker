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