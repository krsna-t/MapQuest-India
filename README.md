#MapQuest: India
MapQuest: India is an interactive Python-based game that tests your knowledge of India's states and union territories. Using the turtle graphics module, the game displays a map of India and challenges players to guess the names of states and UTs. Correct guesses are marked on the map at their corresponding coordinates. The goal is to identify all 37 states and union territories.

Features
Interactive Map: Visual interface using the turtle graphics module.
Geography Quiz: Guess the names of Indian states and UTs.
Real-time Feedback: Correct guesses are marked on the map.
Progress Tracking: Tracks your correct guesses and shows missed states/UTs if you choose to exit.
How to Play
Run the Python script MapQuest_India.py.
A map of India will be displayed.
You will be prompted to guess the names of Indian states and union territories.
If your guess is correct, it will be marked on the map at its location.
The game ends when you guess all 37 states and UTs or type "Exit" to stop. If you exit, the game will display any remaining states/UTs you missed.
Requirements
Python 3.x

The turtle module (comes pre-installed with Python)

The pandas module (install using pip)

Copy code
pip install pandas
Files
MapQuest_India.py: The main game script.
state.csv: CSV file containing state/UT names and their coordinates.
map_resized.gif: The map of India used in the game.
Installation
Clone this repository:
bash
Copy code
git clone https://github.com/yourusername/mapquest-india.git
Navigate to the project directory:
bash
Copy code
cd mapquest-india
Install required dependencies:
Copy code
pip install pandas
Run the game:
Copy code
python MapQuest_India.py
