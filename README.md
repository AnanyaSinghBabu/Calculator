# Futuristic Calculator

This project contains two versions of a full-featured calculator:

1.  A web application built with FastAPI and HTML/CSS/JS.
2.  A desktop GUI application built with Tkinter.

## Features

- Basic operations: addition, subtraction, multiplication, division.
- Advanced functions: square root, exponentiation, percentage, pi constant.
- Memory functions: MC, MR, M+, M-.
- Sign toggle (+/-).
- Clean, modern, and responsive user interface.

## How to Run

### Web Application

1.  **Install dependencies:**

    ```bash
    pip install fastapi uvicorn python-multipart
    ```

2.  **Run the server:**

    From the `calculator` directory, run the following command:

    ```bash
    uvicorn main:app --reload
    ```

3.  **Open in browser:**

    Open your web browser and go to `http://127.0.0.1:8000`.

### Desktop GUI Application

1.  **Run the application:**

    From the `calculator` directory, run the following command:

    ```bash
    python gui.py
    ```

    The calculator window will appear.
