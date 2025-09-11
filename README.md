# Weight Converter

A simple Python program that converts various weight units to kilograms.

## Features

- Converts from multiple weight units to kilograms
- Supports common units: grams, pounds, ounces, stone, metric tons, and more
- Interactive command-line interface
- Error handling for invalid inputs

## Supported Units

- **Grams**: g, gram, grams
- **Kilograms**: kg, kilogram, kilograms
- **Pounds**: lb, lbs, pound, pounds
- **Ounces**: oz, ounce, ounces
- **Stone**: st, stone, stones
- **Metric Tons**: ton, tonne, tons, tonnes, t

## Usage

### Running the Interactive Converter

```bash
python weight_converter.py
```

Then enter weight values in the format: `[weight] [unit]`

Examples:
- `100 g` (100 grams)
- `154 lb` (154 pounds)
- `1 stone` (1 stone)
- `2.5 ton` (2.5 metric tons)

### Running the Test Suite

```bash
python test_converter.py
```

This will run automated tests to verify the conversion accuracy.

## Example Conversions

- 100 grams = 0.1 kg
- 1 pound = 0.453592 kg
- 16 ounces = 0.453592 kg (1 pound)
- 1 stone = 6.35029 kg
- 1 metric ton = 1000 kg

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Download the `weight_converter.py` file
2. Ensure Python is installed on your system
3. Run the program using `python weight_converter.py`

## How to Install Python

If Python is not installed on your system:

### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer and make sure to check "Add Python to PATH"
3. Or install from Microsoft Store: search for "Python" in the Microsoft Store

### macOS
```bash
# Using Homebrew
brew install python3

# Or download from python.org
```

### Linux
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3

# CentOS/RHEL
sudo yum install python3
```

## Program Structure

- `weight_converter.py` - Main interactive converter program
- `test_converter.py` - Automated test suite
- `README.md` - This documentation file
