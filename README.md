# data-entry-application

## Introduction
This project is a Dash web application that allows users to enter details about themselves and view the previous entries in a table format. The application uses Dash, a Python framework for building web applications, and Dash Bootstrap Components to style the application components.

## Features
1. **Data Entry Form**: A form to input personal details like Name, Age, Title, and Hometown.
2. **Confirmation Section**: Shows a confirmation of the entered data upon submitting the form.
3. **Previous Entries Table**: Displays a table of all previous entries submitted through the data entry form.

## Setup and Installation
1. Ensure you have Python installed.
2. Install the necessary libraries:
   
   ```bash
   pip install dash dash-bootstrap-components
   
## Clone this repository or copy the code into your local machine.

### Run the application:
1. Clone this repository or copy the code into your local machine.
2. Run the application:

```bash
   python -u form.py
```
3. Open a web browser and navigate to http://127.0.0.1:8050/ to access the application.

# How to Use

In the "Data Entry Form" section:
1. Fill in the details:
    - **Name** (Required)
    - **Age**
    - **Title** (Required)
    - **Hometown**
2. Click the "Submit" button.
3. Upon successful submission, the "Confirmation" section will display the entered details.
4. All submissions will be added to the "Previous Entries" table at the bottom of the application.

# Code Structure

- **Layout**: The app's layout consists of a container with three main rows:
    1. Data Entry Form
    2. Confirmation Section
    3. Previous Entries Table

- **Callbacks**: The app utilizes a single callback activated by the "Submit" button:
    - When the "Submit" button is clicked, the callback function verifies the input's validity.
    - If the data is valid, the details are added to the "Previous Entries" table, and a confirmation message appears. Otherwise, an alert is shown.

# Known Limitations

- The data isn't persistent. Restarting the server or reloading the app will wipe out all previous entries.
- No validations exist for the Age or Hometown fields.

# Future Improvements

- Implement data persistence to retain previous entries even after restarting the app.
- Introduce additional validations for the input fields.
- Add features to modify or remove previous entries.

# Conclusion

This application demonstrates the basic use of Dash and Dash Bootstrap Components to create a straightforward web application. It can be further enhanced with more features and functionalities as needed.
