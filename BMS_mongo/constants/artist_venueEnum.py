from enum import Enum

class OccupationEnum(str, Enum):
    ACTOR = "Actor"
    MUSICIAN = "Musician"
    SINGER = "Singer"
    PRODUCER = "Producer"
    DIRECTOR = "Director"
    CAMERAMAN = "Cameraman"
    MUSIC_DIRECTOR = "Music Director"
    COMPOSER = "Composer"
    BACKGROUND_SCORE = "Background Score"
    SPECIAL_APPEARANCES = "Special Appearances"
    LYRICIST = "Lyricist"
    WRITER = "Writer"
    SCREENPLAY = "Screenplay"
    DIALOGUE_WRITER = "Dialogue Writer"
    VOICE_CAST = "Voice Cast"
    
class FacilitiesEnum(str, Enum):
    PARKING_FACILITY = "Parking Facility"
    TICKET_CANCELLATION = "Ticket Cancellation"
    F_B = "F&B"
    M_TICKET = "M Ticket"
    FOOD_COURT = "Food Court"
