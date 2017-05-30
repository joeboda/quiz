from asciimatics.effects import Sprite, Print
from asciimatics.event import KeyboardEvent, MouseEvent
from asciimatics.exceptions import ResizeScreenError
from asciimatics.renderers import StaticRenderer, SpeechBubble, FigletText
from asciimatics.particles import Explosion, StarFirework, DropScreen, Rain, \
    ShootScreen
from asciimatics.renderers import SpeechBubble, FigletText, Rainbow
from asciimatics.screen import Screen
from asciimatics.paths import DynamicPath
from asciimatics.sprites import Arrow
from asciimatics.scene import Scene
import sys
from time import sleep


def global_shortcuts(event,scenes):
    if isinstance(event, KeyboardEvent):
        c = event.key_code
        # Stop on ctrl+q or ctrl+x
        if c in (98,99):
            scenes.Next()



class KeyboardController():
    def process_event(self, event):
        if isinstance(event, KeyboardEvent):
            key = event.key_code
            if key == Screen.KEY_UP:
                screen.print_at('Hello Sweden!', 0, 0)
                screen.refresh()
            elif key == Screen.KEY_DOWN:
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

	# Pass this to the screen...
	

	key = KeyboardController()
	if isinstance(screen, KeyboardEvent):
		key = event.key_code
		screen.print_at(key, 0, 0)
		screen.refresh()

	
		sleep(10)
	
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

	#screen.play(scenes, stop_on_resize=True)
	screen.play(scenes, unhandled_input=global_shortcuts)



if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(demo)
            sys.exit(0)
        except ResizeScreenError:
            pass
