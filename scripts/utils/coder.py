import zlib
import base64
from urllib import parse


def from_library(val):
    try:
        val_deflated = from_base64(val)
        val_percent = inflate(val_deflated).decode('utf-8')
        return from_percent_encode(val_percent)
    except zlib.error:
        return val


def to_library(val):
    val_percent = to_percent_encode(val)
    val_deflated = deflate(val_percent.encode('utf-8'))
    return to_base64(val_deflated)


def from_shape(val):
    val_decoded = from_base64(val)
    return val_decoded.decode('utf-8')


def to_shape(val):
    val_encoded = val.encode('utf-8')
    return to_base64(val_encoded).decode("utf-8")


def decode_base64_and_inflate(b64string):
    decoded_data = base64.b64decode(b64string)
    return zlib.decompress(decoded_data, -15)


def inflate(string_val):
    return zlib.decompress(string_val, -15)


def deflate(string_val):
    zlib_str = zlib.compress(string_val)
    return zlib_str[2:-4]


def from_base64(b64string):
    return base64.b64decode(b64string)


def to_base64(string_val):
    return base64.b64encode(string_val)


def from_percent_encode(string_val):
    return parse.unquote_plus(string_val)


def to_percent_encode(string_val):
    return parse.quote_plus(string_val)
