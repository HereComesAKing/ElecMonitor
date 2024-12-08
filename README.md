# ElecMonitor

A python program to monitor your dorm room's electricity bill and prevent your desktop from suddenly powering down and shutting down.

Support Platform:

- [x] Windows
- [ ] Linux
- [ ] MacOS

Support School:

- XAUAT

## Usage

1. Install Python 3.7 or higher.
2. Clone this repo.
3. Install dependencies by running `pip install -r requirements.txt`.
4. Run `make` to build the executable.
5. Copy the `elecmonitor.exe` to the folder where you want to store the program, etc `C:\Program Files\ElecMonitor`.
6. Edit the config file `config.json` to set your own `openid`, where you can find it in the website of your school `dl.xauat.edu.cn`, one of the arg of the url.
7. Run `elecmonitor.exe` to start the program. You can setup a link to the program at startup (win at `C:\Users\yourname\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`) to make it run automatically when you turn on your computer.