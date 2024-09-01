# MTG Commander Pod Bracketing

This program helps organize and manage pods for a Magic: The Gathering Commander tournament. It allows you to enter player names, determine pod sizes, and create initial pods for the first round.

## Features

- Enter player names interactively.
- Automatically determine pod sizes based on the number of players.
- Shuffle players and create initial pods for the first round.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Spit-ball/MTG-Commander-Pod-Bracketing.git
    cd MTG-Commander-Pod-Bracketing
    ```

2. Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/).

## Usage

1. Run the program:
    ```sh
    python bracketing.py
    ```

2. Follow the prompts to enter player names. Type `complete` when you have finished entering all player names.

3. The program will automatically determine the pod sizes and create initial pods for the first round.

## Example

```sh
$ python bracketing.py
Enter player name (or type 'complete' to finish): Alice
Enter player name (or type 'complete' to finish): Bob
Enter player name (or type 'complete' to finish): Charlie
Enter player name (or type 'complete' to finish): Dave
Enter player name (or type 'complete' to finish): complete

Round 1 Pods:
Pod 1: Alice, Bob, Charlie, Dave
