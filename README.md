# Preprocessor CLI

A terminal-based Machine Learning preprocessing tool built using Python, Rich and Click.

This project helps perform common preprocessing tasks directly from the terminal using an interactive CLI interface.

---

# Features

* Dataset Loading
* Data Description
* NULL Value Handling
* Feature Scaling
* Dataset Preview
* Dataset Download
* Interactive CLI UI using Rich

---

# Project Structure

```text
preprocessor-cli/
│
├── main.py
├── data_input.py
├── data_description.py
├── null_handler.py
├── categorical.py
├── feature_scaling.py
├── download.py
├── sample_dataset.csv
├── requirements.txt
├── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/adminsanjay/ml_prepCLI
cd ml_prepCLI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Requirements

```text
pandas
scikit-learn
rich
click
```

---

# Run the Project

```bash
python3 main.py sample_dataset.csv
```

---

# Available Operations

## Data Description

* Describe specific columns
* View dataset statistics
* Preview dataset rows

---

## NULL Value Handling

* Show NULL counts
* Remove columns
* Fill NULL values using:

  * Mean
  * Median
  * Mode

---

## Encoding

| Color |
| ----- |
| Red   |
| Blue  |

↓

| Color_Red | Color_Blue |
| --------- | ---------- |
| 1         | 0          |
| 0         | 1          |

---

## Feature Scaling

* Standard Scaling
* Min-Max Scaling

---

# Example Workflow

```text
1. Load Dataset
2. Handle NULL Values
3. Encode Categorical Columns
4. Scale Features
5. Download Processed Dataset
```

---

# Technologies Used

* Python
* Pandas
* Scikit-learn
* Rich
* Click

---

# Future Improvements

* Support Excel files
* Add data visualization
* Add outlier detection
* Add feature selection
* Add automated preprocessing pipeline
* Add model training support

---

# Author

SANJAY R
