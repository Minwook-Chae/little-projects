import random, sys, time


try:
    import bext
except ImportError:
    print("Error trying to import bext module")
    sys.exit()

WIDTH, HEIGHT = bext.size()
WIDTH -= 1
LOGO_COUNT = 1
PAUSE_AMOUNT = 0.2
COLORS = ('red', 'green', 'blue', 'yellow', 'white', 'cyan', 'magenta')
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()
    logos = []
    for i in range(LOGO_COUNT):
        # logos.append({COLOR: random.choice(COLORS),
        #                 X: random.randint(1, WIDTH - 4),
        #                 Y: random.randint(1, HEIGHT - 4),
        #                 DIR: random.choice(DIRECTIONS)})
        logos.append({COLOR: random.choice(COLORS),
                        X: 25,
                        Y: 25,
                        DIR: UP_RIGHT})
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1
    
    corner_bounce_count = 0
    while True:
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print('   ', end='')

            original_direction = logo[DIR]
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                corner_bounce_count += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                corner_bounce_count += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                corner_bounce_count += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                corner_bounce_count += 1
            
            # left edge bounce
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] == DOWN_RIGHT
            
            # right edge bounce
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] == DOWN_LEFT

            # top edge bounce
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] == DOWN_RIGHT
    
            # bottom edge bounce 
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] == UP_RIGHT

            if logo[DIR] != original_direction:
                logo[COLOR] = random.choice(COLORS)

            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

            bext.goto(5, 0)
            print(f"y is {logo[Y]}", end='')
        bext.goto(5, 0)
        bext.fg('white')
        # print(f"{corner_bounce_count} corner bounces", end='')

        for logo in logos:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')
        
        bext.goto(0, 0)

        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)


if __name__ == '__main__':
    try:
        print('hi')
        main()
    except KeyboardInterrupt:
        sys.exit()

