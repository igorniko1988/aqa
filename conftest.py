import json

import allure
from allure import attachment_type
import pytest


@pytest.fixture(autouse=True)
def attachments():
    yield
    allure.attach("test_content", name='Text', attachment_type=attachment_type.TEXT)
    allure.attach("html", name='Html', attachment_type=attachment_type.HTML)
    allure.attach("test_content", name='Text', attachment_type=attachment_type.TEXT)
    allure.attach(json.dumps({"first": 1, "second": 2}), name='Json', attachment_type=attachment_type.JSON)
