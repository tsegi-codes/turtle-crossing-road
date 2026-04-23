# 🐢 Turtle Crossing Capstone Project

A Python recreation of the classic Frogger arcade game, built using Object-Oriented Programming (OOP) and the Python Turtle graphics library.

## 🎮 How to play
* **Objective:** Guide the turtle safely across a busy highway to the top of the screen.
* **Controls:** Press the **Up Arrow** key to move forward.
* **Rules:** * If you touch a car, the game is over.
  * Every time you successfully cross the finish line, you level up.
  * With each new level, the traffic speed increases!

## Features & Architecture
* **Multi-File Architecture:** The game logic is cleanly separated into modular classes (`player.py`, `car_manager.py`, `scoreboard.py`, and a main `main.py` referee).
* **Random Car Generation** using Python's random module, Cars are generated dynamically using random probability logic (`random.randrange`) to prevent infinite traffic jams and ensure spaced-out horizontal movement.
* **Collision Detection** using Turtle's built-in distance method to Utilize precise coordinate math to detect distance-based collisions between the player object and a constantly updating list of autonomous car objects.
* **Dynamic Difficulty:** Level-up system that scales the `car_speed` variable iteratively.

## 🧠 What I Learned Building This
This was a major milestone project that solidified my understanding of:
* **Object-Oriented Programming:** Managing state and behavior across multiple independent classes.
* **Version Control:**Initializing a local repository and pushing to GitHub using Git terminal. 
* **Game Loops:** Using `while` loops combined with `time.sleep()` to manage frame updates and control the flow of time.

## How to run the project
1. Install Python
2. Clone the repository
3. Run:
   ```bash
   python main.py
   ```
## Screenshot
<img width="400" alt="turtle" src="https://github.com/user-attachments/assets/5d7e532b-afc4-4948-be2f-8a4c1858f885" />
