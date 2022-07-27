ElectionsScraper - scrapes data from public server volby.cz and saves them into newly made CSV file 

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)



## General Information
- This is my final project of Python academy on https://engeto.cz/ platform.
- My code scrapes selected regional data of 2017 Czech legislative elections, see this link: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ
- More specifically, it scrapes these data for every municipality in selected district: code of the municipality, name of the municipality, number of voters, number of issued ballots, number of legal votes and list of candidate parties.
- Finally, all scraped data are written into and saved as csv file.



## Technologies Used
- PyCharm
- Python - version 3.10
- for modules, see requirement.txt file


## Screenshots
![Example screenshot](https://github.com/PetaGb/ElectionsScraper/blob/main/volby_2017.odg)



## Setup
- In PyCharm, virtual enviroment is installed automatically, so are some of the modules from requirements file like pip. You only need to install bs4 and requests modules. You can use terminal via running  "pip install 'name_module'" command. Alternatively, you can add this module via IDE.
- If you use different programming enviroment and it supports using terminal directly from it, I recommend to install requirements this way since everything will be saved in right directory in order to avoid problems with running program.
- If you use programming enviroment which doesn´t support direct use of terminal, you will have to install requirements (and run the script) using terminal from your OS. This requires a little more familiarity with command line.


## Usage
- After saving script as some_file.py, opening it, saving required modules, you can run script by opening terminal and setting command like this: PS- C:\Users\peter\PycharmProjects\Election_scraper> python main.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6206' "Vyškov.csv"
- Python is the program executing script, main.py is name of the script
- First argument is url address of scraped district. You can access it by opening the link mentioned above: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ and clicking on any X symbol in column named  "Výběr obce". Please, see the picture from the screenshot section.
- Second argument is name of future CSV file to be made. I recommend to name it after okres(district) name. 
- You can see an example file named "Vyškov" made by the command from above uploaded to this repository.

## Room for Improvement
- Creating analogous script using Pandas module

## Acknowledgements
- Automate the Boring Stuff book helped me with this project
- Many thanks to https://github.com/ritaly for providing cheatsheet helping me with this very first readme
