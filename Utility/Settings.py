from Utility.Point import Point

PLAYER_CONTROL = False
# Wybor pomiedzy sterowaniem przez gracza a sterowaniem przez czarna skrzynke

TIME_LIMIT = 200
# Ile klatek ma trwac jedna generacja Springerow.
# Po tym czasie powinno dochodzic do rekombinacji genomu i utworzenia nowych Springerow

START_HEAD_COORDS, START_FOOT_COORDS = (100, 100), (50, 200)
# Poczatkowa pozycja springera zaraz po utworzeniu

HEADLESS_MODE = False
# Tryb bez okna graficznego

FRAME_TIME = 1/70
RES_X = 800
RES_Y = 600
GRAVITY_ACCELERATION = 0.1
COLLISION_EPSILON = 3
FLOOR_HEIGHT = 100
BOUNCE_COEFFICIENT = 0.08
