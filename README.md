# Aircraft War 
> Team members: Zach (Zhe) Chen, Junhao Liang

This file is used to generate the game Aircraft War game with python. Air Wargaming are classic and popular in game market since 1920s. From the ealiest card games to modern PC and mobile games, air wargames have developed different genres with multiple methods to bring players with numerous pleasures. This file brings a new small aircraft wargame through python.

**Package Install**

In order to run the game, python 3.0+ is required. In addition, [pygame](https://www.pygame.org/wiki/GettingStarted) should be installed.
```
pip install pygame
```
**Game Instruction**
![Image text](https://github.com/Zacooky/AircraftWar-Project/blob/master/images/Instruction_image.png)
1. In the game interface, the current score is shown in the upper left corner, the pause/resume button is shown at the upper right corner, the number of bombs available is shown in the lower left corner, and the number of life remaining is shown in the lower right corner.
2. In the beginning of the game, our plane will be created in the middle bottom of the screen. Players can control the plane with up, down, left, and right keys on the keyboard.
3. Our plane will shoot bullets automatically at constant speed. Players can move the plane to attack enemy planes with buttles. Destroying a small, mid, big enemy will require 1, 8, and 20 shots, and will reward 1000, 6000, 10000 points, respectively.

![Image text](https://github.com/Zacooky/AircraftWar-Project/blob/master/images/enemy1.png)
Small Enemy
![Image text](https://github.com/Zacooky/AircraftWar-Project/blob/master/images/enemy2.png)
Mid Enermy
![Image text](https://github.com/Zacooky/AircraftWar-Project/blob/master/images/enemy3_n1.png)
Big Enemy

4. Supplies will drop every 5 seconds (for better effects in instruction) at a speed of 6. There will be two kinds of supplies, super bullet and bombs. Our plane can obtain the supply by touching them. With super bullet, our plane can shoot two bullets at the same time with faster speed, the super bullet time will last 20 seconds. In terms of bombs, player can release the bomb actively by pressing the space button on keyboard. The bomb will destroy all the enemy planes in the screen regardless of the types, and the scores will be added to current score. The plane will start with 3 bomb in the beginning of the game, and the maximum number of bombs storing is 3.

![Image text](https://github.com/Zacooky/AircraftWar-Project/blob/master/images/ufo1.png)
Super Bullet
![Image text](https://github.com/Zacooky/AircraftWar-Project/blob/master/images/ufo2.png)
Bomb

5. As the game continues, the hardness of the game will increase. There are total of 5 levels of hardness, and the players can updrade the hardness through achieve certain scores(5000, 50000, 500000, 1000000). As the level of hardness upgraded, the number of enemy planes and their speeds will increase.
6. Our plane will be given three lives in the beginning of each game. The lives will be affected by the time our plane colliding with enemy planes. Once there is a collision between our plane and enemy planes, both planes will be destroyed. If our plane has life remaining, it will resurrect at the bottom middle of the screen with three seconds of safe time.
7. The game will record the histrical highest score. After game is over, players can choose to restart or end the game.
