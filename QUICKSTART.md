# TODO App - Quick Start Guide

## Installation & Setup

### Option 1: Build from Source (Recommended for First Time)

1. **Download and Install Python** (if not already installed)
   - Visit: https://www.python.org/downloads/
   - Download Python 3.10 or later
   - **IMPORTANT**: During installation, check "Add Python to PATH"

2. **Extract the TODO App folder** to a location on your computer

3. **Double-click `setup_and_build.bat`**
   - This will automatically install dependencies and build the executable
   - Wait for completion (this takes 1-2 minutes on first run)
   - You'll see "SUCCESS" when complete

4. **Find your executable**
   - Location: `dist\TODO-App.exe`
   - You can create a shortcut to this file on your desktop

### Option 2: Run from Source (Development)

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the app:
   ```
   python src/main_advanced.py
   ```

---

## Usage Guide

### Adding Tasks

1. **Enter task title** in the "Task to Add" field
2. **Add description** (optional) for more details
3. **Select priority**: Low, Medium, or High
4. **Set due date** using the date picker
5. **Click "Add Task"** or press Enter

**Keyboard Shortcut**: Press `Enter` while in the title field to quickly add a task

### Managing Tasks

- **Complete a task**: Double-click the task to mark it as done (will show strikethrough)
- **Delete a task**: Right-click on a task and select "Delete Task"
- **Sort tasks**: Use the "Sort by" dropdown to organize by:
  - Priority (High → Medium → Low)
  - Due Date (earliest first)
  - Name (alphabetical)

### Theme Options

- **Toggle Dark/Light Mode**: Click the 🌙 or ☀️ button in the top-right corner
- **Dark Mode** (default): Dark red theme with light accents, easy on the eyes
- **Light Mode**: Bright theme with the same professional color scheme

---

## Features Overview

✅ **Task Management**
- Create, edit, complete, and delete tasks
- Add descriptions for detailed task info
- Set priority levels and due dates
- Multiple sorting options

✅ **Themes & Appearance**
- Dark and Light modes
- Professional dark red color scheme (#8B1538)
- Smooth animations for task interactions
- Hover effects on tasks
- Responsive design - scales with window

✅ **Performance**
- Lightweight executable (~50-60 MB)
- Low RAM usage (80-150 MB typical)
- Fast startup time
- Automatic task saving

✅ **Data**
- Tasks automatically saved locally
- Data persists between sessions
- Stored in: `C:\Users\YourName\.todoapp\tasks.json`

---

## Troubleshooting

### "Python is not installed" error

**Solution**: Install Python from https://www.python.org/
- Make sure to check "Add Python to PATH" during installation
- Restart your computer after installation

### Executable won't start

**Solution**: Install Visual C++ Redistributable
- Download from: https://support.microsoft.com/en-us/help/2977003/
- Run the installer and follow the prompts
- Try running the TODO App again

### Tasks not saving

**Solution**: Check folder permissions
- Make sure your user has write permissions to `C:\Users\YourName`
- Try running the app as Administrator (right-click → Run as administrator)

### Build failed

**Solution**: Try the quick rebuild
1. Open Command Prompt in the TODO-App folder
2. Run: `build_quick.bat`
3. If still failing, try:
   ```
   pip install --upgrade pyinstaller
   ```

---

## File Structure

```
TODO-App/
├── src/
│   ├── main_advanced.py       (Main application - RECOMMENDED)
│   └── main.py                (Basic version)
├── dist/
│   └── TODO-App.exe           (Built executable)
├── requirements.txt           (Python dependencies)
├── setup_and_build.bat        (First-time setup & build)
├── build_quick.bat            (Quick rebuild)
├── README.md                  (Full documentation)
└── QUICKSTART.md              (This file)
```

---

## Tips & Tricks

💡 **Pro Tips**:
- Double-click a task to mark it complete
- Right-click for quick delete option
- Use Priority sorting for urgent tasks
- Use Due Date sorting to meet deadlines
- Switch themes based on lighting conditions

⚡ **Performance Tips**:
- Keep descriptions concise
- Archive old completed tasks occasionally
- The app uses minimal resources - safe to leave open all day

---

## Version Info

- **Version**: 1.0
- **Built with**: Python 3.10+, PyQt6
- **OS**: Windows 7 and later
- **File Size**: ~50-60 MB
- **Memory**: ~80-150 MB at runtime

---

## Support

For issues or questions:
1. Check the README.md file for detailed documentation
2. Ensure Python is properly installed and in PATH
3. Try rebuilding the executable with `setup_and_build.bat`

Enjoy your TODO App! 🎉
