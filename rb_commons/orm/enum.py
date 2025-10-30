from enum import Enum

class OriginType(str, Enum):
    MANUAL = "MANUAL"
    ETL = "ETL"
    API = "API"
    DEFAULT = "DEFAULT"
    BILLZ = "BILLZ"
    BITO = "BITO"
    SMARTUP = "SMARTUP"
    DIZGO = "DIZGO"
    ERA = "ERA"
    YESPOS = "YESPOS"
    STORFOX = "STORFOX"

class MediaSource(str, Enum):
    ROBO = "ROBO"
    BILLZ = "BILLZ"
    BITO = "BITO"
    EUROPHARM = "EUROPHARM"
    DIZGO = "DIZGO"
    YESPOS = "YESPOS"
    STORFOX = "STORFOX"