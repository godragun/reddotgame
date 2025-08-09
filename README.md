# Touch the Dots Game

A simple hand-tracking game using OpenCV and MediaPipe. The objective is to "touch" as many red dots as possible with your hand within 30 seconds using your webcam. Each time you touch a dot, your score increases and a new dot appears.

## Features

- Real-time hand tracking using MediaPipe.
- Play using your webcam, no mouse or keyboard required.
- Visual feedback: score and timer displayed on the screen.
- Fun and interactive way to practice computer vision and Python skills.

## How to Play

1. **Run the Script**  
   Make sure you have all requirements installed (see below), then run the script:
   ```bash
   python touch_the_dots.py
   ```

2. **Allow Webcam Access**  
   The game will use your default webcam.

3. **Touch the Dots**  
   Move your hand in front of the camera and try to touch the red dots on the screen. Each touch increases your score and spawns a new dot.

4. **Game Duration**  
   The game lasts 30 seconds. Your final score will be shown in the terminal after the game ends.

5. **Quit Early**  
   Press the `q` key to exit the game at any time.

## Requirements

- Python 3.7+
- OpenCV (`opencv-python`)
- MediaPipe
- NumPy

Install the dependencies with pip:
```bash
pip install opencv-python mediapipe numpy
```

## File Structure

- `touch_the_dots.py` — Main game script.
- `README.md` — This file.

## Notes

- For best results, play in a well-lit environment.
- The game uses both hands if visible, so you can play with one or two hands.
- Dot collision is based on the closeness of any hand landmark to a dot.

## Troubleshooting

- **Webcam not detected:**  
  Make sure your webcam is connected and not being used by another application.
- **Slow performance:**  
  Lower resolutions or better hardware will improve performance.
- **Hand not detected:**  
  Try improving lighting or moving your hand closer to the camera.

---

Enjoy playing and practicing your hand-eye coordination with computer vision!
