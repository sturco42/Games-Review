# Game Reviewz
Game Reviewz is a Content Management Command Line Interface for game data, ratings, and users. It gives the user access to a database of influential video games which includes ratings and reivews. 

## Installation
---
* fork and clone this repository to your local machine
* install pipenv <br>
 ```pipenv install```
* install simple-chalk <br> ```pip install simple_chalk```
* initiate pipenv shell <br> ```pipenv shell```
* navigate to the **lib** directory on your local terminal <br>
 ```cd lib```
* access the Command Line Interface <br> ```python3 cli.py```

## Application Features
---
* Navigation Menu
```
Welcome to 'Game Reviewz'!

Please type in the number corresponding to the choice.
  1. All Games
  2. Search Games
  3. New Releases
  4. Popular Games
  5. Add Rating
  6. Done
```
* Read all games in database
```
...
...
...
  <Game 74. Splinter Cell: Chaos Theory | Publisher: Ubisoft | Year: 2005>
  <Game 75. The Sims 3 | Publisher: Electronic Arts | Year: 2009>
  <Game 76. Donkey Kong | Publisher: Nintendo | Year: 1981>
  <Game 77. Mario Kart 8 Deluxe | Publisher: Nintendo | Year: 2014>
  <Game 78. Dota 2 | Publisher: Valve | Year: 2013>
  <Game 79. Return of the Obra Dinn | Publisher: 3909 LLC. | Year: 2018>
Please enter the game id to see the details: 
```
* Access specific game data by id
```
  Title: Pokemon Yellow
  Publisher: Nintendo
  Year: 1999
  Ave Rating: 10
```
* Search for games by title
```
Please enter the game title: Super Mario World
  Title: Super Mario World
  Publisher: Nintendo
  Year: 2002
  Ave Rating: 3.25
```

* Display new releases
```
  <Game 13. Hades | Publisher: Supergiant Games | Year: 2020>
  <Game 26. Half-Life: Alyx | Publisher: Valve | Year: 2020>
  <Game 38. The Last of Us Part 2 | Publisher: Sony Interactive Entertainment | Year: 2020>
```

* Sort by top rated games
```
  Title: Pokemon Yellow
  Publisher: Nintendo
  Year: 1999
  Ave Rating: 10
      
  Title: Final Fantasy VI
  Publisher: Square
  Year: 1994
  Ave Rating: 8        

  Title: The Legend of Zelda: Breath of the Wild
  Publisher: Nintendo
  Year: 2017
  Ave Rating: 7
        
  Title: The Legend of Zelda: Ocarina of Time 3D
  Publisher: Nintendo
  Year: 2011
  Ave Rating: 7    

  Title: Portal 2
  Publisher: Valve
  Year: 2011
  Ave Rating: 6      

  Title: Super Mario World
  Publisher: Nintendo
  Year: 2002
  Ave Rating: 3.25
```

* Login/Create profile to leave a review
```
  Please login first.
      
  1. Existing User
  2. New User
  2
  Please enter your first name: John
  Please enter your last name: Smith
  Please enter your username: Johnny No3
  <First Name: John | Last Name: Smith | Username: Johnny No3>
  What is the game id: 5
  Please rate from 1-10: 8
```
* Exit CLI

## Contributing
---
Open to pull requests. For major changes, please open an issue first to discuss what you would like to change.  

## Authors and Acknowledgements
---
### Contributors:
* [sturco42](https://github.com/sturco42)
* [RRZhai](https://github.com/RRZhai)
* [Blujay0](https://github.com/Blujay0)  

## License
---
[MIT License](https://choosealicense.com/licenses/mit/)

Copyright (c) [2023]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
