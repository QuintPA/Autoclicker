# AutoClicker

A Python-based autoclicker for Windows that allows you to:
- Click at rapid speeds (customizable)
- Click at current cursor position or predefined coordinates
- Press multiple keys simultaneously
- Toggle on/off with ESC key
- Easy-to-use menu interface

## Installation

### Prerequisites
- Python 3.6 or higher
- Windows OS

### Setup

1. Clone or download the repository
2. Install required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the autoclicker:

```bash
python autoclicker.py
```

### Menu Options

1. **Start clicking (current position)** - Clicks where your mouse currently is
2. **Start clicking (set coordinates)** - Clicks at specific X, Y coordinates
3. **Start pressing keys** - Presses configured keys rapidly
4. **Stop autoclicker** - Stops the current action
5. **Set click speed** - Change how fast clicks happen (in seconds)
6. **Set keys to press** - Configure which keys to press (e.g., 'a, shift, w')
7. **Set target coordinates** - Set specific coordinates for clicking
8. **Get current mouse position** - Shows your current cursor position
9. **Exit** - Close the program

### Controls

- **ESC Key** - Emergency stop (works globally even if window isn't focused)

## Configuration Tips

### Click Speed
- `0.01` = 10ms between clicks (very fast)
- `0.05` = 50ms between clicks (fast)
- `0.1` = 100ms between clicks (medium)
- Adjust based on your needs

### Keys to Press
Examples:
- Single key: `a`
- Multiple keys: `a, shift, w`
- Special keys: `space`, `shift`, `ctrl`, `alt`, `enter`

### Coordinates
To find your target coordinates:
1. Use menu option 8 to get current mouse position
2. Move mouse to desired location
3. Check the coordinates displayed
4. Enter them in menu option 7

## Examples

### Example 1: Fast clicking at current position
```
1. Choose option 5 and set speed to 0.01
2. Choose option 1
3. Move mouse to target
4. Autoclicker will click rapidly
5. Press ESC to stop
```

### Example 2: Press WASD keys repeatedly (gaming)
```
1. Choose option 6
2. Enter: w, a, s, d
3. Choose option 3
4. Press ESC to stop
```

### Example 3: Click at specific coordinates
```
1. Choose option 8 to find coordinates
2. Choose option 7 to set target
3. Choose option 1 to start
4. Press ESC to stop
```

## Important Notes

⚠️ **WARNING**: Use responsibly! Rapid clicking/key pressing may:
- Damage your mouse/keyboard over time
- Violate terms of service of games/applications
- Cause unintended actions if not carefully configured

## Troubleshooting

**Program won't start:**
- Make sure Python 3.6+ is installed
- Run `pip install -r requirements.txt` again

**ESC key not working:**
- May require admin privileges on some systems
- Try right-clicking and running as administrator

**Clicks too slow/fast:**
- Adjust the click speed in the menu (option 5)

**Permission denied error:**
- Run the script with administrator privileges

## Dependencies

- **pyautogui** - For getting mouse position
- **pynput** - For mouse control and keyboard listening
- **keyboard** - For key press simulation

## License

MIT License - Feel free to use and modify!
