# Visualizing Djikstra's Pathfinding Algorithm in Python

This program visualizes [Djikstra's pathfinding algorithm](https://www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/) to find the shortest path between two nodes in an *undirected* and *unweighted* graph using Pygame. The graph is represented as a grid, where each cell is a node and each node is connected to its neighboring nodes. This project was built along youtube videos visualizing the same algorithm.

## Features

- Real-time visualization of Dijkstra's algorithm 
- Ability to place end point & walls
- Ability to reset the grid and start a new search
- Dynamic window title bar that displays the program status & the length of the shortest path

## Notes 
- `pathfinding.py` is the default program of this project. Visualizes the algorithm and automatically returns the shortest path. 
- `pathfinding_backtracking.py` is the program that purposely slows down the pathfinding and backtracks the path to the source node. This is used for demonstration purposes. 

## Installation

1. Clone this repository: `git clone https://github.com/nxrodata/pathfinding-visualizer.git`
2. Navigate into the project directory: `cd pathfinding-visualizer`
3. Set up a virtual environment:
   - On Windows: `python -m venv venv`
   - On Unix or MacOS: `python3 -m venv venv`
4. Activate the virtual environment:
   - On Windows: `.\venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Run the program: `python main.py`

## Controls

- `Left click` to place the start point, end point, and walls.
- `Right click` to remove points or walls.
- Press `Space` to start the search.
- Press `R` to reset the grid.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)