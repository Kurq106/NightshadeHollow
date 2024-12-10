# NightshadeHollow
Final Milestone for class CSS-225

Code Hosting:
The game code for Nightshade Hollow is hosted on GitHub. Clone the repository to your local machine to access all files.

External Services:
No external tools or online services are required to run this game.
The game is designed to run locally using Python.

Languages & Technologies:
Language: Python 3.8 or later.
Libraries: No additional libraries are required.

System Requirements:
Operating System: Windows, macOS, or Linux.
Python Version: Python 3.8 or higher.
Dependencies: No external dependencies. The game uses standard Python modules.

Coding/Naming Conventions:

File Structure:
globalvars.py: Contains shared variables.

maingame.py: Includes shared functions used across chapters.

chapter1.py, chapter2.py: Contains chapter-specific game logic.

main.py: The entry point for the game.

Naming Patterns:
Variables and functions use snake_case for readability (e.g., print_inventory).
Constants (like inventory or player data) are in lowercase for simplicity.
Each chapter file is named in sequential order (e.g., chapter1.py, chapter2.py) for clarity.

How to Run/Build/Deploy:
Running Locally:
Install Python 3.8 or higher from the official website.
Clone the repository:
git clone https://github.com/kurq106/NightshadeHollow.git
cd NightshadeHollow
Run the game:
python main.py
Running Online:
Host the game on a Python-friendly platform like pythonanywhere.com. Upload all files and set main.py as the executable script.

Architecture Overview:
The game is modular, consisting of multiple files:
globalvars.py: Manages shared variables like playername, inventory, and chapter success states.
maingame.py: Contains utility functions such as printing the inventory.
Chapter Files (chapter1.py, chapter2.py): Handle specific game logic and story elements.
main.py: The main driver that manages the game flow by importing and executing chapter scripts.
Flow:
The player starts in main.py, which sequentially calls chapter1.py and chapter2.py.
Variables and inventory are updated dynamically through globalvars.py and shared between chapters.

How to Start the Game:
Ensure Python 3.8 or later is installed on your system.
Download the project files or clone the repository using the following command:
git clone https://github.com/kurq106/NightshadeHollow.git
Navigate to the project folder:
cd NightshadeHollow
Launch the game:
python main.py
Follow the on-screen instructions to progress through the story.
