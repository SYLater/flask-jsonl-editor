# Flask JSONL Editor

This is a simple Flask web application that allows you to load, view, and save a JSONL (JSON Lines) file. The application provides an API to interact with the JSONL file and a basic HTML interface to view and edit the data.

## Features

- Load a JSONL file and display its contents as a JSON response
- Save changes to the JSONL file
- Disable automatic sorting of JSON keys for better readability

## Prerequisites

- Python 3.x
- Flask
- Flask-CORS

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/SYLater/flask-jsonl-editor.git
   ```

2. Navigate to the project directory:

   ```
   cd flask-jsonl-editor
   ```

3. Install the required dependencies:

   ```
   pip install flask flask-cors
   ```

## Usage

1. Update the `jsonlfile` variable in the `flask-jsonl-editor.py` script to point to the location of your JSONL file.

2. Run the Flask application:

   ```
   python flask-jsonl-editor.py
   ```

3. Open your web browser and navigate to `http://localhost:5000`. You should see the index page.
## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).