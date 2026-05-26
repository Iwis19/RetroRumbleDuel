# Retro Rumble Duel
Python-based local multiplayer fighting game built with Pygame. Players select a map, choose from four pixel-art fighters, and battle in a retro-style 1v1 duel :)

---

## Repository Note
You may wonder why this is all stuck in one big file and there are no OOP principles or any other classes, thats because my teacher said no to using classes as their final project. ( ˘︹˘ ) will probably refactor this as practice tho

---

## Key Features
1. **Local 2-Player Gameplay**
   - One keyboard, two players
   - Head-to-head retro fighting match
   - Character lock to prevent duplicate picks
2. **Character Selection System**
   - Four playable fighters:
     - Fire Knight
     - Wind Hashashin
     - Water Priestess
     - Metal Bladekeeper
   - Animated character preview during selection
   - Unique hitboxes, damage values, and cooldown timings per character
3. **Map Selection**
   - Five selectable battle maps
   - Animated backgrounds
   - Map-specific ground levels
4. **Combat & UI**
   - Two attack types per character
   - Jumping and directional movement
   - Health bars and cooldown bars
   - Countdown intro and game over screen with auto-close

---

## Tech Stack
- **Python**
- **Pygame**
- **Pixel art sprite sheets and frame-based animations**
- **MP3 sound effects and background music**

---

## Controls
- **Player 1**
  - Move: `A` / `D`
  - Jump: `W`
  - Attack 1: `E`
  - Attack 2: `R`
- **Player 2**
  - Move: `J` / `L`
  - Jump: `I`
  - Attack 1: `O`
  - Attack 2: `P`
- **Menu**
  - Continue from title screen: `Spacebar`
  - Exit game: `Esc`

---

## Project Structure

```text
Retro Rumble Duel.py
backgroundmusic/
character1/
character2/
character3/
character4/
COUNTDOWNBACKGROUND/
font/
MAP1/
MAP2/
MAP3/
MAP4/
MAP5/
MENUBACKGROUND/
```

--- 

## Lessons Learned
- Building a real-time game loop in Pygame
- Managing way too many sprite animations and combat states
- Working with coordinates on a screen to customize hitboxes and mechanics

---

## License
MIT
