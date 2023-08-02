# JARVIS - Your Personal AI Assistant

JARVIS is a Python-based AI assistant that can perform various tasks and provide you with information using speech recognition and synthesis. It can search Wikipedia, send emails, take screenshots, play songs, provide system information, tell jokes, and much more!

## Getting Started

To use JARVIS, you need to have Python installed on your system along with some additional libraries. You can install the required libraries using the following command:

```bash
pip install pyttsx3 sounddevice numpy wavio speechrecognition wikipedia psutil pyjokes
```

You will also need to install `tkinter` to use the `MouseInfo` module for taking screenshots. Use the following command for Debian-based distributions:

```bash
sudo apt-get install python3-tk
```

For Red Hat-based distributions, you can use:

```bash
sudo dnf install python3-tkinter
```

## Features

- Greet you and tell the current time.
- Perform online speech recognition to understand your commands.
- Search Wikipedia and provide summarized results.
- Send emails through your Gmail account.
- Open Firefox and search the web based on your command.
- Perform system actions like logout, shutdown, and restart.
- Play songs from your local Music directory.
- Take screenshots and save them as "screenshot.png".
- Get CPU usage and battery status.
- Tell you jokes for some fun!

## How to Use

1. Clone or download this repository to your local machine.
2. Make sure you have installed all the required libraries and `tkinter` (if needed).
3. Run the JARVIS.py file using Python.

```bash
python JARVIS.py
```

4. JARVIS will greet you and listen for your commands.
5. You can interact with JARVIS using voice commands or text inputs.
6. Enjoy using JARVIS to perform various tasks!

## Supported Commands

- "Time" - To get the current time.
- "Offline" - To exit and turn off JARVIS.
- "Wikipedia" - To search Wikipedia. JARVIS will read a summarized result for you.
- "Send Email" - To send an email through your Gmail account.
- "Search in Chrome" - To search the web using Firefox (you can change the browser path if needed).
- "Logout" - To logout of the system.
- "Shutdown" - To shut down the system.
- "Restart" - To restart the system.
- "Play Songs" - To play songs from your local Music directory.
- "Remember That" - To make JARVIS remember something you say.
- "Do You Remember Anything" - To check if JARVIS remembers something.
- "Screenshot" - To take a screenshot and save it as "screenshot.png".
- "CPU" - To get the current CPU usage and battery status.
- "Joke" - To hear a random joke and have some fun!

## Disclaimer

This project is intended for educational purposes only. The usage of some features like email sending might require additional setup and authorization. Use at your own risk.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/TheRealSaitama/JARVIS/main/LICENSE) file for details.

---

Happy coding with JARVIS!
