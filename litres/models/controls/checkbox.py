from selene.support.shared import browser
from selene import command


def select_checkbox(id_element):
    return browser.element(id_element).click().perform(command.js.scroll_into_view)
