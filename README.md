# Mp3 to Wav Converter

A Tkinter-based GUI application that uses Pydub to convert one or more MP3 files to WAV format.

## Table of Contents

1.  [Description](#description)
2.  [Requirements](#requirements)
3.  [Installation](#installation)
    *   [Python](#python)
    *   [FFmpeg](#ffmpeg)
        *   [Windows (Chocolatey)](#windows-chocolatey)
        *   [macOS (Homebrew)](#macos-homebrew)
        *   [Linux (Package Managers)](#linux-package-managers)
    *   [Python Packages](#python-packages)
        *   [Using pip](#using-pip)
        *   [Using pyenv](#using-pyenv)
        *   [Using uv (Fast Alternative)](#using-uv-fast-alternative)
4.  [Usage](#usage)
5.  [Contributing](#contributing)
6.  [License](#license)

## Description

This Python script provides a simple graphical user interface (GUI) built with Tkinter to convert MP3 audio files to WAV format.  It leverages the Pydub library for the audio processing, making the conversion process straightforward.  You can select single or multiple MP3 files for conversion.

## Requirements

*   **Python 3.7 or higher:**  This script is designed to run on modern Python versions.  While it *might* work on older 3.x versions, it's not guaranteed.
*   **FFmpeg:**  This is a powerful multimedia framework that Pydub relies on for encoding and decoding audio.  It *must* be installed and available in your system's PATH.
*   **Python Packages:**
    *   `pydub`
    *   `simpleaudio`
    *   `tk` (Usually included with Python installations, but good to be explicit)

## Installation

### Python

If you don't have Python installed, download the latest version from the official Python website ([https://www.python.org/downloads/](https://www.python.org/downloads/)) and follow the installation instructions.  Make sure to check the box that adds Python to your PATH during installation (especially on Windows).

### FFmpeg

FFmpeg is essential for this script to function.  Install it using one of the following methods depending on your operating system:

#### Windows (Chocolatey)

1.  **Install Chocolatey:** If you don't have Chocolatey (a package manager for Windows), open PowerShell as an **Administrator** and run the following command:

    ```powershell
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    ```
    Follow any on-screen prompts.  You might need to close and reopen PowerShell.

2.  **Install FFmpeg:**  In PowerShell (as a regular user or Administrator), run:

    ```powershell
    choco install ffmpeg
    ```

#### macOS (Homebrew)

1.  **Install Homebrew:** If you don't have Homebrew (a package manager for macOS), open Terminal and run:

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
    Follow any on-screen instructions.

2.  **Install FFmpeg:** In Terminal, run:

    ```bash
    brew install ffmpeg
    ```

#### Linux (Package Managers)

Use your distribution's package manager to install FFmpeg.  Here are some common examples:

*   **Debian/Ubuntu:**

    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```

*   **Fedora/CentOS/RHEL:**

    ```bash
    sudo dnf install ffmpeg  # Or 'yum' on older versions
    ```

*   **Arch Linux:**

    ```bash
    sudo pacman -S ffmpeg
    ```

**Verify FFmpeg Installation:** After installing FFmpeg, open a new terminal (or command prompt) window and type `ffmpeg -version`.  If FFmpeg is installed correctly, you should see version information. **If you get a "command not found" or similar error, FFmpeg is *not* in your system's PATH. You *must* add the directory containing the `ffmpeg` executable to your PATH environment variable for Pydub to work. Refer to your operating system's documentation for instructions on how to modify the PATH.**

### Python Packages

You can install the required Python packages using `pip`, `pyenv`, or `uv`. `pyenv` is recommended for managing multiple Python versions and project-specific environments. `uv` is a fast alternative to pip.

#### Using pip

Open a terminal or command prompt and run:

```bash
pip install pydub simpleaudio
```

#### Using pyenv  

pyenv allows you to easily switch between different Python versions and manage virtual environments.

1. **Install pyenv: Follow the installation instructions for your operating system on the pyenv GitHub repository: https://github.com/pyenv/pyenv#installation**

* Important: Make sure to follow the instructions to configure your shell (e.g., adding lines to your .bashrc, .zshrc, or similar). You'll likely need to restart your terminal after this.

2. **Install a Python Version:**

```bash
pyenv install 3.10 
```

3. **Create a Virtual Environment: (This isolates your project's dependencies)**

```bash
pyenv virtualenv 3.10 mp3-to-wav-converter
```
4. **Activate the Environment:**

```bash
pyenv activate mp3-to-wav-converter
```
5. **Install Packages: Now, within the activated environment, use pip:**

```bash
pip install pydub simpleaudio
```
#### Using uv (Fast Alternative)

`uv` is a fast Python package installer and resolver.  It's designed to be used within a virtual environment, and it provides its own command for creating them.

1.  **Install uv:**

    ```bash
    pip install uv
    ```

2.  **Clone the Repository (or Download the Script):**

    ```bash
    git clone https://github.com/Ktiseos-Nyx/Mp3_To_Wav.git
    cd Mp3_To_Wav
    ```
    Alternatively, you can download the `converter.py` file directly and place it in a new directory (e.g., `Mp3_To_Wav`).  Make sure you `cd` into that directory.  The important point is that the `uv venv` command (in the next step) should be run *inside* the project directory.

3.  **Create a Virtual Environment using `uv venv`:**  Run this command *inside* the `Mp3_To_Wav` directory:

    ```bash
    uv venv
    ```
    This creates a virtual environment in a directory named `.venv` *within* your project directory (`Mp3_To_Wav`).

4.  **Activate the Virtual Environment (Optional, but good for clarity):** Although `uv run` will automatically use the `.venv` if it exists, it's still good practice to know how to activate it manually.

    *   **Linux/macOS:**
        ```bash
        source .venv/bin/activate
        ```
    *   **Windows (PowerShell):**
        ```powershell
        .venv\Scripts\Activate.ps1
        ```
    *   **Windows (Command Prompt):**
        ```
        .venv\Scripts\activate.bat
        ```

5.  **Install Packages using `uv pip install`:**

    ```bash
    uv pip install pydub simpleaudio
    ```

## Usage

1.  **Clone the Repository (or Download the Script):**

    ```bash
    git clone https://github.com/Ktiseos-Nyx/Mp3_To_Wav.git
    cd Mp3_To_Wav
    ```
    Alternatively, you can download the `converter.py` file directly.

2.  **Run the Script (Two Options):**

    You have two main options for running the script, especially if you've used `uv` to manage your environment:

    *   **Option 1: Activate the environment and run:**  This is the traditional approach.

        ```bash
        source .venv/bin/activate  # Or the appropriate activation command for your OS
        python converter.py
        ```

    *   **Option 2: Use `uv run`:** This is more convenient, as it avoids the explicit activation step.  `uv run` automatically executes the command *within* the virtual environment (as long as a `.venv` directory exists in the current working directory or a parent directory).

        ```bash
        uv run python converter.py
        ```

        This command does the following:
        1.  It finds the `.venv` environment (created by `uv venv`).
        2.  It *temporarily* activates that environment.
        3.  It executes `python converter.py` within that activated environment.
        4.  It deactivates the environment when the command finishes.

3.  **GUI Instructions:**

    *   Click the "Browse" button to select one or more MP3 files.  You can use Ctrl+Click (or Cmd+Click on macOS) to select multiple files.
    *   The selected files will be listed in the GUI.
    *   Click the "Convert" button to start the conversion process.
    *   The converted WAV files will be saved in the same directory as the original MP3 files, with the same filenames (but with a `.wav` extension).  A message box will appear when the conversion is complete.

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details. 


