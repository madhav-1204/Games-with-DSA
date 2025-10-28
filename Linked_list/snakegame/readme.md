# 🐍 Linked List Snake Game

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6+-blue?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green?logo=pygame&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

*A classic Snake game implemented with Linked List data structure visualization*

[🎮 Play Now](#-quick-start) | [📖 How to Play](#-how-to-play) | [🏗️ Architecture](#️-architecture)

</div>

## 📋 Table of Contents

- [🌟 Overview](#-overview)
- [🚀 Quick Start](#-quick-start)
- [🎮 How to Play](#-how-to-play)
- [🔧 Installation](#-installation)
- [💻 Usage](#-usage)
- [📊 Features](#-features)
- [🔬 Technical Details](#-technical-details)
- [🎨 Customization](#-customization)

## 🌟 Overview

<div align="center">

![Gameplay Demo](https://via.placeholder.com/600x400/000000/FFFFFF?text=Snake+Game+Demo)

</div>

This **Linked List Snake Game** is not just a fun classic game, but also an **educational tool** that demonstrates real-time data structure operations. Each segment of the snake's body is represented as a node in a linked list, providing visual insight into how this fundamental data structure works.

### 🎯 Key Highlights

- 🐍 **Linked List Visualization** - Watch data structures in action
- 🎓 **Educational Value** - Learn while playing
- ⚡ **Real-time Operations** - See linked list manipulations live
- 🎨 **Smooth Gameplay** - Classic snake mechanics with modern implementation

## 🚀 Quick Start

### 📥 Prerequisites

- 🐍 **Python 3.6+** [Download here](https://www.python.org/downloads/)
- 🎮 **Pygame Library**

### ⚡ One-Command Installation

```bash
# Clone and run (if you have the code)
pip install pygame && python snake_game.py
```

### 🔧 Manual Setup

```bash
# 1. Create project directory
mkdir snake-game && cd snake-game

# 2. Install required package
pip install pygame

# 3. Download the game file (save as snake_game.py)

# 4. Run the game
python snake_game.py
```

### ✅ Verification

```bash
python --version
# Python 3.8.0 or higher

pip show pygame
# Version 2.0.0 or higher
```

## 🎮 How to Play

### 🎯 Objective
- 🍎 Eat red food pellets to grow longer
- ⚡ Avoid colliding with your own body
- 🏆 Achieve the highest score possible

### ⌨️ Controls

| Key | Action | Icon |
|-----|--------|------|
| **↑** | Move Up | 🔼 |
| **↓** | Move Down | 🔽 |
| **←** | Move Left | ◀️ |
| **→** | Move Right | ▶️ |
| **R** | Restart Game | 🔄 |
| **ESC** | Quit Game | ❌ |

### 📊 Scoring System

| Action | Points | Effect |
|--------|--------|--------|
| 🍎 Eat Food | +10 points | Snake grows longer |
| 🎯 Every 50 points | +0 points | Game speed increases |
| 💀 Self-Collision | Game Over | Restart required |



### 🔗 Linked List Implementation

```python
# 🏷️ Node Class - Represents each snake segment
class Node:
    def __init__(self, x, y):
        self.x = x          # 🗺️ Grid X position
        self.y = y          # 🗺️ Grid Y position  
        self.next = None    # ➡️ Pointer to next node

# 🔗 Linked List Class - Manages snake body
class LinkedList:
    def __init__(self):
        self.head = None    # 🐍 First node (snake head)
        self.tail = None    # 🐍 Last node (snake tail)
        self.length = 0     # 📏 Number of segments
```

### ⚡ Key Operations

| Operation | Method | ⏱️ Complexity | 🎯 Usage |
|-----------|---------|----------------|----------|
| **Add Head** | `append_left()` | O(1) | 🐍 Snake movement |
| **Remove Tail** | `pop_right()` | O(n) | 📏 Length management |
| **Collision Check** | `contains()` | O(n) | 💥 Self-collision detection |
| **Get Positions** | `get_positions()` | O(n) | 🎨 Rendering |

## 🔧 Installation

### 📋 Step-by-Step Guide

1. **🐍 Install Python**
   ```bash
   # Verify installation
   python --version
   # Should show Python 3.6 or higher
   ```

2. **🎮 Install Pygame**
   ```bash
   pip install pygame
   ```

3. **📥 Get the Game Code**
   ```bash
   # Option 1: Download snake_game.py manually
   # Option 2: Clone from repository (if available)
   git clone <repository-url>
   cd linked-list-snake-game
   ```

4. **🚀 Run the Game**
   ```bash
   python snake_game.py
   ```

### 🔍 Verification Commands

```bash
# Check Python version
python --version

# Check Pygame installation
python -c "import pygame; print(f'Pygame {pygame.version.ver} installed successfully')"

# Run the game
python snake_game.py
```

## 💻 Usage

### 🎯 Basic Gameplay

1. **🎮 Start the Game**
   ```bash
   python snake_game.py
   ```

2. **🐍 Control the Snake**
   - Use arrow keys to change direction
   - Guide the snake to eat red food pellets
   - Avoid running into yourself

3. **📈 Watch Your Growth**
   - Each food pellet makes the snake longer
   - Score increases with each food eaten
   - Game speeds up as you progress

### 🎮 Game States

| State | Display | Actions Available |
|-------|---------|-------------------|
| **🏃 Playing** | Green snake, moving | All direction keys |
| **💀 Game Over** | Red message, static | Restart (R) or Quit |
| **🔄 Restart** | Reset snake | Continue playing |

## 📊 Features

### 🎯 Core Features

| Feature | Status | Description |
|---------|--------|-------------|
| 🐍 Linked List Visualization | ✅ Implemented | Real-time data structure display |
| 🎮 Classic Gameplay | ✅ Implemented | Traditional snake mechanics |
| 📈 Progressive Difficulty | ✅ Implemented | Speed increases with score |
| 🏆 Score Tracking | ✅ Implemented | Real-time score display |
| 🔄 Wrap-around Borders | ✅ Implemented | Infinite playing field |
| 💥 Collision Detection | ✅ Implemented | Self-collision prevention |
| 🔧 Easy Restart | ✅ Implemented | Quick game reset |

### 🚀 Advanced Features

- **⚡ Real-time Updates**: Linked list operations visible during gameplay
- **🎨 Visual Feedback**: Different colors for head and body segments
- **📊 Performance Metrics**: Segment count and score display
- **🔧 Configurable Settings**: Easy-to-modify game parameters

## 🔬 Technical Details

### 🎮 Game Loop Architecture

```python
def run(self):
    """🔄 Main game loop"""
    running = True
    while running:
        # 🎯 Handle user input
        running = self.handle_input()
        
        # ⚡ Update game state
        self.update()
        
        # 🎨 Render graphics
        self.draw()
        
        # ⏱️ Maintain frame rate
        self.clock.tick(self.speed)
```

### 🗺️ Grid System Specifications

| Parameter | Value | Description |
|-----------|-------|-------------|
| **Grid Size** | 20×20 pixels | Size of each cell |
| **Play Area** | 30×30 cells | 600×600 pixel game window |
| **Coordinates** | Grid-based | Integer positions |
| **Wrap-around** | Enabled | Infinite playing field |

### ⚡ Performance Characteristics

| Aspect | Specification | Impact |
|--------|---------------|--------|
| **Base FPS** | 10 frames/sec | Smooth gameplay |
| **Speed Scaling** | Increases with score | Progressive challenge |
| **Memory Usage** | O(n) for snake length | Efficient scaling |
| **Rendering** | Optimized surface updates | Smooth graphics |

## 🎨 Customization

### 🎯 Easy Modifications

#### 🚀 Change Game Speed
```python
# In SnakeGame.__init__()
self.speed = 15  # 🎯 Increase for faster gameplay
```

#### 🗺️ Modify Grid Size
```python
GRID_SIZE = 25    # 🎯 Larger cells for different visual style
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
```

#### 🎨 Change Color Scheme
```python
# 🎨 Modify color constants
GREEN = (0, 255, 100)      # 🟢 Brighter green for head
RED = (255, 100, 100)      # 🔴 Softer red for food
DARK_GREEN = (0, 150, 50)  # 🟢 Darker green for body
BLUE = (100, 100, 255)     # 🔵 Alternative color scheme
```

#### 📊 Adjust Scoring
```python
# In SnakeGame.update()
self.score += 5    # 🎯 Less points per food (easier)
# or
self.score += 20   # 🎯 More points per food (harder)
```

### 🔧 Advanced Customizations

#### Add Power-ups
```python
# Example: Golden food worth more points
GOLD_FOOD = (255, 215, 0)  # 🟡 Gold color
```

#### Implement Levels
```python
# Example: Level-based speed increases
self.level = self.score // 100 + 1
self.speed = FPS + self.level * 2
```
