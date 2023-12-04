# Rocket Scorer

This is a Python application that calculates the score of a rocket for competition

## Prerequisites

- Python 3.12 or higher
- PyInstaller

## Installation

1. Clone the repository (requires Git):
```bash
git clone https://github.com/PouplarWesel/RocketScorer.git
```

2. Navigate to the project directory:

```bash
cd rocketscorer
```
3. Install the required Python packages:
```bash
pip install -r requirements.txt
```
## Running the Application

You can run the application with the following command:
```bash
pyinstaller --onefile --noconsole rocket_app.py
```
## Building the Executable

You can build an executable version of the application with PyInstaller:


This will create a single executable file in the `dist` directory. You can run this executable to start the application without needing to have Python installed.


Wondering why Window Defender is flagging the executable as a virus? See [this stack overflow conversation](https://stackoverflow.com/questions/43777106/program-made-with-pyinstaller-now-seen-as-a-trojan-horse-by-avg) for more information.