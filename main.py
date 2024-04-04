from translate import Translator
import polib
import os
from dotenv import load_dotenv


load_dotenv()

translator = Translator(to_lang=os.getenv("TO_TRANSLATE"))

pofile = polib.pofile(os.getenv("TRANSLATION_FILE"))

for entry in pofile:
    if not entry.msgstr:
        entry.msgstr = translator.translate(entry.msgid)

pofile.save(os.getenv("TRANSLATION_FILE"))