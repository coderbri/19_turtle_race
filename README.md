# 19 Turtle Race

This project is part of the **Day 19 Challenge** of the **100 Days of Code: Python Pro Bootcamp** by Dr. Angela Yu. It uses Python's Turtle graphics library to create a colorful turtle race. The project demonstrates key programming concepts, including higher-order functions, event listeners, state, and the creation and use of instances.

## Project Overview

The Turtle Race app allows users to bet on which turtle will win the race. Multiple turtles are displayed on the screen, each moving forward a random distance in each iteration. The race continues until one turtle crosses the finish line.

Users interact with the app by entering their bet through a popup text input and can observe the race as it progresses.

![Turtle Race Demo](#)

## Features

### 1. Setting Up the Turtles
- **Screen Setup**: The race screen is set up with custom dimensions to accommodate the race.
- **User Interaction**: A popup window collects the user's bet.
- **Turtle Initialization**: Turtles are created with unique colors, positioned at starting coordinates, and prepared for the race.

### 2. Making the Turtles Race
- **Randomized Movement**: Each turtle's progress is randomized to simulate unpredictability.
- **Winner Detection**: The app determines the winning turtle based on its position and announces the result, comparing it to the user's bet.

## Methods Used

### Screen Setup
- `screen.setup(width, height)`: Sets the screen dimensions. In this project, the width is set to 550px and the height to 400px using keyword parameters for clarity.
- `screen.textinput(title, prompt)`: Displays a popup window to capture user input. The title is displayed as the window title, and the prompt describes the required input.

### Turtle Initialization
- `turtle_obj.goto(x, y)`: Moves a turtle instance to specified coordinates without drawing.
- `Turtle(shape="turtle")`: Creates a new turtle instance with the turtle shape.
- `turtle_obj.color(outline, fill)`: Sets the turtle’s outline and fill colors.
- `turtle_obj.penup()`: Lifts the pen to prevent drawing when moving to the start position.

### Race Logic
- **Randomized Movement**:
  ```python
  random_distance = random.randint(0, 10)
  turtle.forward(random_distance)
  ```
  Each turtle moves forward by a random number of pixels (between 0 and 10) per iteration.

- **Winner Detection**:
  ```python
  if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor()
      ```
  The race ends when a turtle's x-coordinate exceeds 230, and the color of the winning turtle is retrieved.

### Event Handling
- **User Bet**: The user's input is checked to ensure the race starts only when a valid bet is placed.
- **Exit on Click**: The app remains open until the user clicks on the screen, handled by `screen.exitonclick()`.

## How Concepts Were Achieved

### Higher-Order Functions
The `random.randint()` function is used to determine each turtle's movement in every iteration, demonstrating the use of a higher-order function.

### Event Listeners
`screen.listen()` sets the screen to listen for user input events, and `screen.textinput()` captures the user’s bet as an interactive event.

### State
The `is_race_on` boolean variable maintains the state of the race and determines when the loop controlling the race should terminate.

### Instances
Each turtle is an instance of the `Turtle` class, created dynamically within a loop. These instances are stored in a list and manipulated individually during the race.

## Running the Project
1. Clone the repository.
2. Run the Python script `turtle_race.py` in your IDE or terminal.
3. Enter your bet through the popup window.
4. Watch the race and see if your chosen turtle wins!

## Example Output
```
You've won! The red turtle is the winner!
```
Or:
```
You've lost... The green turtle is the winner!
```

---
<section align="center">
  <code>coderBri © 2024</code>
</section>