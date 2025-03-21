# 🎯 Precision-Controlled Spotify Web Player Bot (with Real-Time Looping)

**Play. Seek. Loop. Exactly how you want.**

This isn’t your average browser bot. This project allows **dynamic, pixel-perfect control** over Spotify’s web player — letting you **loop any segment** of a song in real time using **live timeline manipulation** and **multithreading**. It's the kind of automation that's usually thought to be "too fiddly" to pull off reliably — and we pulled it off.

---

## 🚀 What Makes It Unique

- 🔁 **Precise audio segment looping** — define any `start` and `end` time, and the bot will keep resetting to that segment in a smooth loop.
- 🧠 **Real-time playback monitoring** — thread-based tracking of Spotify’s playhead ensures accurate trigger points.
- 🖱️ **Offset-based DOM control** — interacts with Spotify’s UI timeline bar using calculated click positions (based on song duration and pixel width).
- 💻 **End-to-end browser automation** — login, search, play, loop... it all happens without lifting a finger after you hit run.

---

## 🛠️ Technologies Used

- Python 3
- Selenium WebDriver
- ChromeDriver (GUI visible for debugging)
- `ActionChains` for precision offset-based UI control
- Multithreading for parallel real-time monitoring

---

## ⚙️ How It Works (Short)

1. Logs into Spotify using credentials you provide in the script.
2. Searches for and starts playing a song (currently searches for "gurbani").
3. Reads the total duration of the song and calculates where to click on the timeline to jump to `start_time`.
4. Starts a real-time thread that monitors current playback time.
5. When playback hits your `end_time`, it jumps back to `start_time`.
6. All visualized through the browser, for better debugging and clarity.

---

## 🧪 How To Run

```bash
pip install selenium
```

Edit your script to add:

```python
EMAIL = "your_spotify_email"
PASSWORD = "your_spotify_password"
starttime = 30       # in seconds
finishtime = 50      # in seconds
```

Then just run the script:
```bash
python your_script.py
```

---

## 🧠 Potential Use Cases

- Mindful meditation or spiritual tracks with repeated segments
- Music production/testing loops
- Audio content review / vocal training
- Just having fun messing with Spotify using actual pixel math and thread timing 😎

---

## ⚠️ Notes

- This is tailored to Spotify’s current web layout — XPaths may need updating if Spotify’s UI changes.
- ChromeDriver version must match your installed Chrome browser.
- This is an educational/personal-use automation project.

---

## ✅ Status

Working as intended. Open to upgrades like:
- Dynamic song selection via CLI or UI
- Visual feedback overlay
- Saving loop segments for reuse

---

Built for people who don’t just play music — they automate it with precision.
