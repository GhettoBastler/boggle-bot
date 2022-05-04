# boggle-bot

This program finds words in a 4x4 Boggle grid.

![grid](https://user-images.githubusercontent.com/100698182/166723719-b1dc5444-2490-4bfa-84f8-029780d2f541.jpg)
*Grid from [Boggle.fr](https://www.boggle.fr/)*

<img src="https://user-images.githubusercontent.com/100698182/166723061-bbb0ec2c-5699-454f-9ee9-2d02cbcba135.gif" alt="demo" width="500"/>


It performs a breadth-first search, matching letter combinations to a tree structure pregenerated from a list of valid words.
I wrote this program for games in French, but you can generate your own tree using a list of word in any language.
This program is written in Python 3.

## Requirements

Python 3.10+

Also a list of words in the language you want to use (one word per line)

## Usage

The solver needs a JSON file containing a tree of valid words. You need to generate it by passing a list of words to **make_tree.py**:
```./make_tree.py mots.txt > tree.json```

*mots.txt contains a list of French words. Replace it with your own list*

Start the solver by calling **solver.py**, passing the generated JSON file as argument:
```./solver.py tree.json```

Enter the letters in the grid when the program prompts you to (you can type all 16 letters on the same line, line by line, one at a time, whichever you find most practical).

Press Return to search the solutions.

By default the program waits for you to press Return before displaying a new solution. You can pass the **-a** option to go through each pattern automatically. Use **-d SECONDS** to set the delay between each word.

## License

This project is licensed under the terms of the GNU GPLv3 license.
