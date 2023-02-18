# Cellular_automaton_generator_flask_application

[Intro]
The code is a Flask web application that generates and displays a cellular automaton animation based on user-defined inputs. The application uses the numpy and matplotlib libraries to generate the animation and Flask to serve the web page. The animation is based on a one-dimensional binary cellular automaton, where each cell is updated according to its neighbors and an update rule specified by the user. The application takes input from the user for the update rule, initial condition, impulse position, and other parameters. The application generates an animation of the cellular automaton and displays it on the web page along with other images.

[General]
- The code imports necessary libraries such as time, random, warnings, os, numpy, matplotlib, flask, and shutil.
- The Flask application is initialized with the name app.
- A path to a folder with GIF images is set.
- The index() function is defined for the main page of the application that displays a GIF image and returns a rendered HTML template.
- The Generator() function is defined that accepts user input for initializing the cellular automata, processes the input, generates the automata, and returns a rendered HTML template that displays an animation of the generated cellular automata.
- The if __name__ == '__main__': block starts the Flask application and runs it on a local server.
- The program is able to generate animations for cellular automata defined by a rule number, size, time steps, initial conditions, and the position of the initial impulse. The generated animations are displayed on a webpage using Flask.

[Process]

The program then processes the contents of the input file, which consists of several lines, each containing a single integer. The program reads each integer, computes its factorial using a recursive function, and then writes the result to an output file named output.txt.

The program uses the built-in open() function to open the input and output files in read and write modes, respectively. It then uses a for loop to iterate over each line in the input file, stripping any leading or trailing whitespace and converting the line to an integer using the int() function.

The program then calls a recursive function named factorial() with the integer as an argument, and stores the result in a variable named result. The factorial() function uses a recursive algorithm to compute the factorial of its input argument, and returns the result to the calling code.

Finally, the program writes the result to the output file using the write() method, converting the result to a string using the str() function and appending a newline character to the end of each line.

Once the loop has processed all lines in the input file, the program closes both files using the close() method, and exits.

[Output]
- In cellular automata, a rule is a set of instructions that determine how the state of a cell in the grid will change based on the state of its neighboring cells. The "rule value" is a number that represents the specific set of instructions for a particular cellular automaton.

- The Initcond phrase, also known as the initial condition phrase, refers to the initial state of the cells in a cellular automaton. This phrase typically defines the starting configuration of the cells, which can be set randomly or according to a specific pattern. The initial condition is used as the starting point for the automaton's evolution, and can have a significant impact on the final outcome of the simulation.

- In cellular automata, the impulse position refers to the specific location or cell in the initial configuration of the automaton where a change or "impulse" is applied. This impulse is typically used to initiate the evolution of the automaton and can take the form of a change in the state of a single cell or a group of cells. The impulse position can also be thought of as the seed for the automaton's evolution. In some cases, the impulse position may be a randomly chosen cell or a user-specified location.

- The color Map (164 colors) in cellular automata refers to the way in which the different states of the cells are represented visually. Typically, each state is assigned a unique color, and the cells are colored according to their current state. The color Map can be chosen based on the specific application or desired visual representation. It can be set to any color Map. The color Map is used to visualize the pattern of states of the cells in the grid over time.

![Example #1](static/images/1.gif)
![Example #1](static/images/2.gif)
![Example #1](static/images/3.gif)


