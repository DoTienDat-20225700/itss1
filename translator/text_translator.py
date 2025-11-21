from deep_translator import GoogleTranslator

class TextTranslator:
    def __init__(self, source='auto', target='vi'):
        self.source = source
        self.target = target
        self.translator = GoogleTranslator(source=self.source, target=self.target)

    def translate(self, text):
        if not text or not text.strip():
            return ""
        try:
            return self.translator.translate(text)
        except Exception as e:
            # return message so UI can show error
            return f"Translate error: {e}"
