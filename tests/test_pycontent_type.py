import pytest

import pycontent_type
import pycontent_type.query


@pytest.fixture(autouse=True, scope="session")
def logging():
    import logging

    logging.basicConfig(level=logging.DEBUG)


def test_application_content_type():
    assert len(pycontent_type.application) == 1551
    assert isinstance(list(pycontent_type.application)[0], pycontent_type.query.Data)


def test_audio_content_type():
    assert len(pycontent_type.audio) == 158
    assert isinstance(list(pycontent_type.audio)[0], pycontent_type.query.Data)


def test_font_content_type():
    assert len(pycontent_type.font) == 6
    assert isinstance(list(pycontent_type.font)[0], pycontent_type.query.Data)


def test_image_content_type():
    assert len(pycontent_type.image) == 80
    assert isinstance(list(pycontent_type.image)[0], pycontent_type.query.Data)


def test_message_content_type():
    assert len(pycontent_type.message) == 25
    assert isinstance(list(pycontent_type.message)[0], pycontent_type.query.Data)


def test_model_content_type():
    assert len(pycontent_type.model) == 41
    assert isinstance(list(pycontent_type.model)[0], pycontent_type.query.Data)


def test_multipart_content_type():
    assert len(pycontent_type.multipart) == 17
    assert isinstance(list(pycontent_type.multipart)[0], pycontent_type.query.Data)


def test_text_content_type():
    assert len(pycontent_type.text) == 93
    assert isinstance(list(pycontent_type.text)[0], pycontent_type.query.Data)


def test_video_content_type():
    assert len(pycontent_type.video) == 89
    assert isinstance(list(pycontent_type.video)[0], pycontent_type.query.Data)


def test_application_content_type_has_all_attributes():
    application = pycontent_type.application.get(Name="json")
    assert application.Template == "application/json"


def test_get():
    c = pycontent_type.application
    with pytest.raises(TypeError):
        c.get(Name="json", Template="application/json")
    assert c.get(Name="json") == c.get(Template="application/json")
    assert c.get(Name="json") is not None


def test_lookup():
    c = pycontent_type.application
    g = c.get(Name="json")
    assert g == c.get(Template="application/json")
    assert g == c.lookup("json")
    assert g == c.lookup("application/json")
