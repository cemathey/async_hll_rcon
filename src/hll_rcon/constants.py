from typing import Final

TEMPORARY_BAN: Final = "TEMPORARY"
PERMANENT_BAN: Final = "PERMANENT"
IDLE_KICK: Final = "IDLE"
HOST_CLOSED_CONNECTION_KICK: Final = "HOST"
TEAM_KILLING_KICK: Final = "TEAM KILLING"
ADMIN_KICK: Final = "ADMIN KICK"
ANTI_CHEAT_TIMEOUT_KICK: Final = "ANTI-CHEAT AUTHENTICATION TIMEOUT"
TEMPORARY_BAN_KICK: Final = "TEMPORARY"
PERMANENT_BAN_KICK: Final = "PERMANENT"

ADMIN_CAM_ENTERED = "ENTERED"
ADMIN_CAM_LEFT = "LEFT"

OFFENSIVE_GAME_MODE: Final = "OFFENSIVE"
WARFARE_GAME_MODE: Final = "WARFARE"

TCP_TIMEOUT_READ: Final = 6
TCP_TIMEOUT: Final = 25
CHUNK_SIZE: Final = None

EMPTY_RESPONSE: Final = "EMPTY"
SUCCESS_RESPONSE = "SUCCESS"
FAIL_RESPONSE = "FAIL"
FAIL_MAP_REMOVAL_RESPONSE = "Requested map name was not found"

VALID_ADMIN_ROLES = ("owner", "senior", "junior", "spectator")

HLL_BOOL_ENABLED = "on"
HLL_BOOL_DISABLED = "off"

INVALID_GAME_SERVER_RESPONSE_ERROR_MSG: Final = (
    "Received an invalid response from the game server"
)

PLAYER_ID_64_OR_PLAYER_NAME_REQUIRED_ERROR_MSG: Final = (
    "Must provide at least either a player ID or player name"
)