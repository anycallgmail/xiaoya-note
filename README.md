# Xiaoya Notes - An Open-Source Personal Note-Taking Website Project

## Project Introduction
Xiaoya Notes is a personal note-taking website project based on the Python Flask framework and containerized with Docker. This project draws inspiration from popular note-taking applications currently available, featuring a simple yet elegant interface. It supports functions such as creating, viewing, editing, and deleting notes, enabling users to conveniently record and manage their notes.

## Project Background
In today's era of information explosion, people need an efficient, secure, and aesthetically pleasing note-taking tool to record and organize their knowledge and ideas. Although there are many note-taking software options on the market, many of them suffer from issues such as complex functionality, unattractive interfaces, or require payment. Therefore, we developed Xiaoya Notes to provide users with a simple, easy-to-use, free, and open-source personal note-taking solution.

## Project Structure
- `flask_app.py`: The main code file of the Flask application, which implements the functions of creating, viewing, editing, and deleting notes.
- `Dockerfile`: A file used to build the Docker image, ensuring that the project can be quickly deployed in different environments.
- `templates/`: A directory for storing HTML template files, with a beautiful interface designed using the Bootstrap framework.
  - `index.html`: The home page, displaying a list of all notes.
  - `create.html`: The page for creating new notes.
  - `note.html`: The page for viewing note details.
  - `edit.html`: The page for editing notes.
- `notes/`: A directory for storing notes, where each note is saved as a text file.
- `README.md`: The project documentation, containing information such as project introduction, environment requirements, installation and running steps, usage instructions, contribution guidelines, and license.

## Environment Requirements
- Docker: Used for building and running containers.
- Python 3.9 (only required for local development): Used to run the Flask application.

## Installation and Running
### Local Running
1. Clone the project to your local machine:
```bash
  git clone <Project Repository URL>
  cd <Project Directory>
```
2. Create and activate a virtual environment (optional):
```bash
  python -m venv venv
  source venv/bin/activate  # For Windows users, use `venv\Scripts\activate`
```
3. Install the dependencies:
```bash
  pip install flask
```
4. Run the Flask application:
```bash
  python flask_app.py
```
5. Open your browser and visit `http://localhost:5000`, and you will see the home page of Xiaoya Notes.

### Docker Running
1. Build the Docker image:
```bash
  docker build -t xiaoya-notes .
```
2. Run the Docker container:
```bash
  docker run -p 5000:5000 xiaoya-notes
```
3. Open your browser and visit `http://localhost:5000`, and you will see the home page of Xiaoya Notes.

## Usage Instructions
### Creating a Note
1. Open your browser and visit `http://localhost:5000`.
2. Click the "Create Note" button on the page.
3. Enter the note content in the text box.
4. Click the "Save" button, and the new note will be created and displayed in the note list on the home page.

### Viewing a Note
1. Open your browser and visit `http://localhost:5000`.
2. Click the title of the note you want to view in the note list.
3. The page will redirect to the note details page, displaying the detailed content of the note.

### Editing a Note
1. Open your browser and visit `http://localhost:5000`.
2. Click the title of the note you want to edit in the note list.
3. Click the "Edit" button on the note details page.
4. Modify the note content in the text box.
5. Click the "Save" button, and the modified note will be saved and displayed in the note list on the home page.

### Deleting a Note
1. Open your browser and visit `http://localhost:5000`.
2. Click the title of the note you want to delete in the note list.
3. Click the "Delete" button on the note details page.
4. Confirm the deletion prompt, and the note will be permanently deleted.

## Contribution
If you want to contribute to this project, please follow these steps:
1. Fork this repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Submit a Pull Request.

## License
This project is licensed under the [MIT License](LICENSE).