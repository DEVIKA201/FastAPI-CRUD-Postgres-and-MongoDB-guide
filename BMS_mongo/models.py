from enum import Enum

class LanguageEnum(str,Enum):
    ENGLISH = "English"
    HINDI = "Hindi" 
    TAMIL = "Tamil"
    KANNADA = "Kannada"
    TELUGU = "Telugu"
    MALAYALAM = "Malayalam"
    MARATHI = "Marathi"
    SANSKRIT = "Sanskrit"

class FormatEnum(str,Enum):
    _2D = "2D"
    _3D = "3D"
    _4DX = "4DX"
    _4DX_3D = "4DX 3D" 
    IMAX_3D = "IMAX 3D"

class GenreEnums(str,Enum):
    DRAMA = "Drama"
    ACTION = "Action"
    THRILLER = "Thriller"
    COMEDY = "Comedy"
    ADVENTURE = "Adventure"
    ROMANTIC = "Romantic"
    FANTASY = "Fantasy"
    SCIFI = "SciFi"
    FAMILY = "Family"
    SPORTS = "Sports"
    ANIMATION = "Animation"
    DOCUMENTARY = "Documentary"
    MUSICAL = "Musical"