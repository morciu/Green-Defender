# Green-Defender

A silly side scrolling 2d arcade shooter created with Pygame.

![VirtualBox_Xubuntu_17_03_2022_09_44_28](https://user-images.githubusercontent.com/67121125/158760959-717081e4-07fd-4288-be63-1a8d4c46238d.png)

## Premise

You are an little green man in a flying saucer in space. Asteroids are coming for you. You must deffend yourself by shooting them up. You are the... **Green Defender**.

![VirtualBox_Xubuntu_17_03_2022_09_46_16](https://user-images.githubusercontent.com/67121125/158761249-0fa6ccaa-08ac-4a98-bd76-d9d785f41c46.png)

## Gameplay
Move up and down and shoot all the asteroids coming for you. You can only shoot 3 laser projectiles at a time. Each stage becomes slightly faster until it becomes unplayable (No way to finish the game).
Try and get a high score.

## Background
I created this game while trying to learng to code during the pandemic. I was reading **Python Crash Course** by Eric Matthes and one of the projects in the book was to make a shooter using Pygame, after coding along to the version in the book I decided to create my own with different features from the original version in the book.

After a few months of struggling and googling trying to figure out how to get certain idea from my head to the python code I finished this game.

## How to run

Install Python

    https://www.python.org/downloads/

Set up a virtual enviroment

    python3 -m venv /path/to/new/virtual/environment

Virtual Enviroment needs to be activated before each use

    Windows -> virtualEnviromentFolder\Scripts\ -> activate
    Linux -> virtualEnviromentFolder/bin/ -> source activate
    
Install dependencies from requirements.txt - Go inside the directory containing requirements.txt and run the following command

    pip install -r requirements.txt

Start game

-inside the game folder run 

```
python3 green_defender.py
```
