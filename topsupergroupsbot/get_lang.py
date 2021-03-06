# TopSupergroupsBot - A telegram bot for telegram public groups leaderboards
# Copyright (C) 2017-2018  Dario <dariomsn@hotmail.it> (github.com/91DarioDev)
#
# TopSupergroupsBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TopSupergroupsBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with TopSupergroupsBot.  If not, see <http://www.gnu.org/licenses/>.

from topsupergroupsbot.langs import en, it, pt_br

lang_obj = {
    "en": en,
    "it": it,
    "pt": pt_br
}


def get_string(lang, variable):
    """
    returns the right string. example of usage:
    print(get_string("en", "test"))
    'en' is the language of the user returned from the db
    '"test"' is the name of the variable in the relative file lang
    """

    try:
        string = getattr(lang_obj[lang], variable)
    except AttributeError:
        string = getattr(en, variable)
    except KeyError:
        string = getattr(en, variable)
    return string


def get_string_buttons(lang, variable):
    try:
        dct = getattr(lang_obj[lang], 'buttons_strings')
    except AttributeError:
        dct = getattr(en, 'buttons_strings')
    except KeyError:
        dct = getattr(en, 'buttons_strings')
    return dct[variable]

