# Translate PO Files Script

## Overview

This script translates the contents of a PO (Portable Object) file using the Google Translate API. It updates the `msgstr` field of each entry in the PO file with the translated text.

## Prerequisites

- Python 3.x installed on your system
- Required Python libraries installed:
  - translate
  - polib
  - dotenv

## Installation

1. Clone this repository to your local machine:


2. Navigate to the cloned directory:


3. Install the required Python libraries:
    ``` pip install -r requirement.txt ```


4. Set up environment variables:
- Create a `.env` file in the root directory.
- Define the following environment variables in the `.env` file:
  - `TO_TRANSLATE`: The target language code to translate into (e.g., 'fr' for French).
  - `TRANSLATION_FILE`: Path to the PO file to be translated.

## Usage

Run the script using the following command:


The script will translate the contents of the specified PO file into the target language defined in the environment variable `TO_TRANSLATE`.

## Notes

- Make sure to provide the appropriate permissions for accessing the PO file.
- Ensure that the Google Translate API is enabled and the necessary API credentials are set up properly.

