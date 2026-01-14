TODO App
A lightweight, professional TODO application for Windows with dark/light themes and smooth animations.
Quick Start

Install Python 3.8+ from https://python.org (check "Add Python to PATH")
Build: Double-click build.bat
Run: dist\TODO-App.exe

Features

✅ Add tasks with title, description, priority, and due date
✅ Sort by Priority, Due Date, or Name
✅ Dark/Light mode toggle
✅ Complete tasks (double-click) or delete (right-click)
✅ Auto-save to local JSON file
✅ Professional dark red theme (#8B1538)
✅ Responsive design that scales with window

Usage
Add Task: Enter title → (optional) description → select priority → set due date → click "Add Task" or press Enter
Manage Tasks:

Complete: Double-click task
Delete: Right-click → Delete Task
Sort: Use dropdown (Priority/Due Date/Name)

Toggle Theme: Click 🌙 or ☀️ button
Technical Details

Size: ~50-60 MB executable
Memory: 80-150 MB at runtime
Startup: <1 second
Storage: C:\Users\[YourName]\.todoapp\tasks.json
Built with: Python 3.10+, PyQt6 6.6.1

Building
First time:
bashpip install -r requirements.txt
python -m PyInstaller --onefile --windowed --name "TODO-App" src\main.py
Quick rebuild:
bashbuild_quick.bat
Sharing
The .exe is completely standalone - no Python needed to run it. Just copy dist\TODO-App.exe and share!
Note: Windows SmartScreen may warn on first run (unsigned app). Click "More info" → "Run anyway"
Troubleshooting
Python not found: Install from python.org with "Add to PATH" checked
App won't start: Install Visual C++ Redistributable
Build fails:
bashpip install --upgrade pyinstaller PyQt6
Customization
Edit src\main.py to change colors, fonts, or features. Then run build_quick.bat to rebuild.

Version 1.0 | Free for personal use | Built with Python & PyQt6