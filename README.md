# TPPSOMT
_the Team Pursuit Performance and Strategy Optimisation Modelling Tool_  

## Project vision  
In order to better help athletes train, refine daily training methods and strategies, and win cycling competitions, the team collected athletes' data for collation and analysis, providing recommendations.  
The purpose of the project is to present complex data such as athlete body data, race data, bicycle data, etc. in a visual manner, so that users can clearly and concisely understand the data, and provide models to simulate the race.

## Quick Start
- Precondition  
    1. Installed python 3.9.10 or later  
    2. Installed pip 22.2.2 or later  
    3. Installed git  
- Download and Install
    1. `git clone https://github.cs.adelaide.edu.au/a1754209/CYCIN-mel.git`  
    2. `cd CYCIN-mel`  
    3. `python3 -m venv .venv`  
    4. `source .venv/bin/activate`  
    5. `pip3 install -r tppsomt/requirements.txt`  
- Run the project
    1. `cd CYCIN-mel`  
    2. `source .venv/bin/activate`  
    3. `python3 tppsomt/manage.py makemigrations`
    4. `python3 tppsomt/manage.py migrate`
    5. `python3 tppsomt/manage.py runserver 0:8000`  
- Visit the website  
    1. Open your chrome  
    2. Visit the website: http://127.0.0.1:8000  
    3. Bingo, enjoy!  

## Attention
_This is a commercial research project. The purpose of public is to facilitate team communication. Others are not allowed to plagiarize or copy it for commercial use. Note that this project abides by the contract and **the core algorithm is removed**._

---
@ Coded by **CYCIN-Mel**


