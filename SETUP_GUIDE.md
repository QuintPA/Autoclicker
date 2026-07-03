# Step-by-Step Setup Guide

This guide will walk you through setting up and running the autoclicker on Windows, even if you're completely new to Python!

## Step 1: Install Python (If you don't have it)

1. Go to https://www.python.org/downloads/
2. Click the big yellow button that says "Download Python 3.x.x"
3. **IMPORTANT:** When the installer opens, check the box that says **"Add Python to PATH"** ✓
4. Click "Install Now"
5. Wait for it to finish, then click "Close"

### Verify Python is installed:
1. Press `Win + R` on your keyboard
2. Type: `cmd` and press Enter
3. Type: `python --version` and press Enter
4. You should see something like: `Python 3.11.0`

If you see an error, restart your computer and try again.

---

## Step 2: Download Your Autoclicker Project

### Option A: Using Git (Recommended if you have it)
1. Press `Win + R`
2. Type: `cmd` and press Enter
3. Type: `git clone https://github.com/QuintPA/Autoclicker.git`
4. Press Enter
5. Type: `cd Autoclicker`

### Option B: Using GitHub Website
1. Go to https://github.com/QuintPA/Autoclicker
2. Click the green "Code" button
3. Click "Download ZIP"
4. Extract the ZIP file to a folder (like `C:\Users\YourName\Desktop\Autoclicker`)
5. Open that folder

---

## Step 3: Open PyCharm

1. Open PyCharm
2. Click "File" → "Open"
3. Select the `Autoclicker` folder you downloaded
4. Click "Open"
5. If it asks about trusting the project, click "Trust Project"

---

## Step 4: Configure Python in PyCharm

PyCharm needs to know which Python version to use.

1. Click "File" → "Settings" (or "Preferences" on Mac)
2. Go to "Project: Autoclicker" → "Python Interpreter"
3. Click the gear icon ⚙️ → "Add..."
4. Click "Add Local Interpreter"
5. Make sure "Existing environment" is selected
6. Click the "..." button to browse
7. Find your Python installation:
   - Usually at: `C:\Users\YourName\AppData\Local\Programs\Python\Python311` (or similar version)
   - Look for `python.exe`
8. Select it and click "OK"
9. Click "OK" again

---

## Step 5: Install Required Packages

These are the extra tools your autoclicker needs to work.

1. In PyCharm, click "Terminal" at the bottom (or View → Tool Windows → Terminal)
2. Copy and paste this command:
   ```
   pip install -r requirements.txt
   ```
3. Press Enter
4. Wait for it to finish (you'll see messages about installing packages)

You should see something like:
```
Successfully installed pyautogui-0.9.53 pynput-1.7.6 keyboard-0.13.5
```

---

## Step 6: Run the Autoclicker

### Method 1: Using PyCharm (Easiest)
1. In PyCharm, find and click on `autoclicker.py` in the left sidebar
2. Right-click it
3. Click "Run 'autoclicker'"
4. A terminal window will open with the menu!

### Method 2: Using Command Prompt
1. Press `Win + R`
2. Type: `cmd` and press Enter
3. Type: `cd C:\path\to\Autoclicker` (replace with your folder path)
4. Type: `python autoclicker.py`
5. Press Enter

---

## Step 7: Using the Autoclicker

Once it's running, you'll see a menu like this:

```
==================================================
AUTOCLICKER MENU
==================================================
1. Start clicking (current position)
2. Start clicking (set coordinates)
3. Start pressing keys
4. Stop autoclicker
5. Set click speed
6. Set keys to press
7. Set target coordinates
8. Get current mouse position
9. Exit
==================================================
```

### Simple Example: Click Really Fast

1. Type `5` and press Enter
2. Type `0.01` and press Enter (this is 10 milliseconds between clicks)
3. Type `1` and press Enter
4. Move your mouse to where you want to click
5. The autoclicker will start clicking rapidly
6. **Press ESC on your keyboard to stop it**

### Example: Press Multiple Keys (for gaming)

1. Type `6` and press Enter
2. Type `w, a, s, d` and press Enter (these are the WASD keys)
3. Type `3` and press Enter
4. The autoclicker will press W, A, S, D rapidly
5. **Press ESC to stop**

---

## Common Issues & Solutions

### Issue: "ModuleNotFoundError: No module named 'pynput'"
**Solution:** You forgot to install packages!
1. Open PyCharm Terminal
2. Run: `pip install -r requirements.txt`
3. Run the autoclicker again

### Issue: "Python not found" when using Command Prompt
**Solution:** Python wasn't added to PATH. Reinstall Python and make sure to check "Add Python to PATH"

### Issue: Permission denied or "Access Denied"
**Solution:** Run PyCharm as Administrator
1. Right-click PyCharm shortcut
2. Click "Run as Administrator"
3. Try running the script again

### Issue: ESC key doesn't work
**Solution:** This sometimes happens. Try:
1. Run PyCharm as Administrator
2. Close the terminal/program using Ctrl+C in the PyCharm terminal

### Issue: Clicks too slow
**Solution:** Reduce the click speed
1. While running, press Ctrl+C to stop
2. Type `5` and choose a smaller number like `0.001` or `0.005`

---

## Tips for Success

✅ **Do this:**
- Save your project regularly (Ctrl+S)
- Test on a safe application first (Notepad, empty document)
- Start with slower speeds and increase gradually
- Always keep ESC key handy to stop

❌ **Don't do this:**
- Run it on important documents without testing first
- Use extremely fast speeds (below 0.001) at first
- Don't close the terminal window while it's running

---

## Getting Help

If something doesn't work:

1. **Read the error message** - It usually tells you what's wrong
2. **Check you followed all steps** - Go back and verify each step
3. **Try restarting PyCharm** - Close and open it again
4. **Run as Administrator** - Right-click PyCharm → Run as Administrator
5. **Reinstall packages** - Type `pip install --upgrade -r requirements.txt` in terminal

---

## Next Steps

Once it's working:
- Experiment with different click speeds
- Try clicking at different locations
- Test different key combinations
- Read the README.md for more advanced features

Happy clicking! 🎯
