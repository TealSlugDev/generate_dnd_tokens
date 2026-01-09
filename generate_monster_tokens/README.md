# D&D Monster Token Generator

A Python utility to generate **numbered circular monster tokens** for tabletop RPGs. 
I made this one long ago for a quick generation as needed for my tokens, which is basically poker chips.

The script takes a monster image and a border image, then automatically creates multiple numbered tokens.

---

## Features

- Circular token generation for DMs
- Custom border overlay
- Generate any number of tokens via CLI argument
- VTT-friendly PNG output (Foundry, Roll20, Owlbear Rodeo)

---

## Requirements

- Python **3.9+**
- Pillow (Python Imaging Library fork)

Install dependencies:

```
pip install pillow
```

## Usage

1. Place your monster artwork and border image in the project root:
   - `monster_img.png`
   - `border.png`

2. Run the script and pass the number of tokens to generate:

```
python main.py <number_of_tokens>
```

The generated tokens will be saved in the output/ directory:
output/ 
```
.
├── token_1.png
├── token_2.png
├── token_3.png
└── ...
```
