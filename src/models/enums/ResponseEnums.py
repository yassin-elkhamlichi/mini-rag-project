from enum import Enum

class ResponseMessage(Enum):
    UNSUPPORTED_MEDIA_TYPE =  "media type not supported"
    REQUEST_ENTITY_TOO_LARGE = "size expected"