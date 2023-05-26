"""
Python library to access all Supported Content-Types/Media-Types
"""

__version__ = "1.1.0"

import os.path
import unicodedata

import pycontent_type.query

try:
    import pkg_resources

    resource_filename = pkg_resources.resource_filename
except ImportError:

    def resource_filename(package_or_requirement, resource_name):
        return os.path.join(os.path.dirname(__file__), resource_name)

else:
    try:
        __version__ = pkg_resources.get_distribution("pycontent_type").version
    except pkg_resources.DistributionNotFound:
        __version__ = "n/a"

DATABASE_DIR = resource_filename("pycontent_type", "data")


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize("NFKD", input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])


class Application(pycontent_type.query.Database):
    """Provide access to application content-types."""

    data_class_name = "application"
    root_key = "application"


class Audio(pycontent_type.query.Database):
    """Provide access to audio content-types."""

    data_class_name = "audio"
    root_key = "audio"


class Font(pycontent_type.query.Database):
    """Provide access to font content-types."""

    data_class_name = "font"
    root_key = "font"


class Image(pycontent_type.query.Database):
    """Provide access to image content-types."""

    data_class_name = "image"
    root_key = "image"


class Message(pycontent_type.query.Database):
    """Provide access to message content-types."""

    data_class_name = "message"
    root_key = "message"


class Model(pycontent_type.query.Database):
    """Provide access to model content-types."""

    data_class_name = "model"
    root_key = "model"


class Multipart(pycontent_type.query.Database):
    """Provide access to multipart content-types."""

    data_class_name = "multipart"
    root_key = "multipart"


class Text(pycontent_type.query.Database):
    """Provide access to text content-types."""

    data_class_name = "text"
    root_key = "text"


class Video(pycontent_type.query.Database):
    """Provide access to video content-types."""

    data_class_name = "video"
    root_key = "video"


application = Application(os.path.join(DATABASE_DIR, "application.json"))
audio = Audio(os.path.join(DATABASE_DIR, "audio.json"))
font = Font(os.path.join(DATABASE_DIR, "font.json"))
image = Image(os.path.join(DATABASE_DIR, "image.json"))
message = Message(os.path.join(DATABASE_DIR, "message.json"))
model = Model(os.path.join(DATABASE_DIR, "model.json"))
multipart = Multipart(os.path.join(DATABASE_DIR, "multipart.json"))
text = Text(os.path.join(DATABASE_DIR, "text.json"))
video = Video(os.path.join(DATABASE_DIR, "video.json"))
