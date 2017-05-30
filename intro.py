from random import randint
from asciimatics.effects import Print
from asciimatics.particles import Explosion, StarFirework, DropScreen, Rain, \
    ShootScreen
from asciimatics.renderers import SpeechBubble, FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from asciimatics.event import KeyboardEvent
from asciimatics.sprites import Arrow
import sys

class KeyboardController():
    def process_event(self, event):
        if isinstance(event, KeyboardEvent):
            key = event.key_code
            if key == Screen.KEY_UP:
                self._y -= 1
                self._y = max(self._y, 2)
            elif key == Screen.KEY_DOWN:
                screen.print_at('Hello world!', 0, 0)
                screen.refresh()
                sleep(10)
                self._y += 1
                self._y = min(self._y, self._screen.height-2)
            elif key == Screen.KEY_LEFT:
                self._x -= 1
                self._x = max(self._x, 3)
            elif key == Screen.KEY_RIGHT:
                self._x += 1
                self._x = min(self._x, self._screen.width-3)
            else:
                return event
        else:
            return event

def demo(screen):
    screen.set_title("Campusfest")

    scenes = []

    # First scene: title page
    effects = [
        Print(screen,
              Rainbow(screen, FigletText("v0id", font="big")),
              y=screen.height // 4 - 5),
        Print(screen,
              FigletText("Campusfest"),
              screen.height // 2 - 3),
        Print(screen,
              FigletText("Beer "),
              screen.height * 3 // 4 - 3),
        Print(screen,
              SpeechBubble("Press SPACE to continue..."),
              screen.height - 3,
              transparent=False,
              start_frame=70)
    ]
    scenes.append(Scene(effects, -1))

    # Next scene: just dissolve the title.
    effects = [
        ShootScreen(screen, screen.width // 2, screen.height // 2, 100),
    ]
    scenes.append(Scene(effects, 40, clear=False))

    screen.play(scenes, stop_on_resize=True)


    

while True:
    try:
        Screen.wrapper(demo)
        sys.exit(0)
    except ResizeScreenError:
        pass
