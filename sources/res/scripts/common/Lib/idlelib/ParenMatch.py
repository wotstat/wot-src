from idlelib.HyperParser import HyperParser
from idlelib.configHandler import idleConf
_openers = {b')': b'(', b']': b'[', b'}': b'{'}
CHECK_DELAY = 100

class ParenMatch:
    menudefs = [
     (
      b'edit',
      [
       (b'Show surrounding parens', b'<<flash-paren>>')])]
    STYLE = idleConf.GetOption(b'extensions', b'ParenMatch', b'style', default=b'expression')
    FLASH_DELAY = idleConf.GetOption(b'extensions', b'ParenMatch', b'flash-delay', type=b'int', default=500)
    HILITE_CONFIG = idleConf.GetHighlight(idleConf.CurrentTheme(), b'hilite')
    BELL = idleConf.GetOption(b'extensions', b'ParenMatch', b'bell', type=b'bool', default=1)
    RESTORE_VIRTUAL_EVENT_NAME = b'<<parenmatch-check-restore>>'
    RESTORE_SEQUENCES = (b'<KeyPress>', b'<ButtonPress>', b'<Key-Return>', b'<Key-BackSpace>')

    def __init__(self, editwin):
        self.editwin = editwin
        self.text = editwin.text
        editwin.text.bind(self.RESTORE_VIRTUAL_EVENT_NAME, self.restore_event)
        self.counter = 0
        self.is_restore_active = 0
        self.set_style(self.STYLE)
        return

    def activate_restore(self):
        if not self.is_restore_active:
            for seq in self.RESTORE_SEQUENCES:
                self.text.event_add(self.RESTORE_VIRTUAL_EVENT_NAME, seq)

            self.is_restore_active = True
        return

    def deactivate_restore(self):
        if self.is_restore_active:
            for seq in self.RESTORE_SEQUENCES:
                self.text.event_delete(self.RESTORE_VIRTUAL_EVENT_NAME, seq)

            self.is_restore_active = False
        return

    def set_style(self, style):
        self.STYLE = style
        if style == b'default':
            self.create_tag = self.create_tag_default
            self.set_timeout = self.set_timeout_last
        elif style == b'expression':
            self.create_tag = self.create_tag_expression
            self.set_timeout = self.set_timeout_none
        return

    def flash_paren_event(self, event):
        indices = HyperParser(self.editwin, b'insert').get_surrounding_brackets()
        if indices is None:
            self.warn_mismatched()
            return
        else:
            self.activate_restore()
            self.create_tag(indices)
            self.set_timeout_last()
            return

    def paren_closed_event(self, event):
        closer = self.text.get(b'insert-1c')
        if closer not in _openers:
            return
        else:
            hp = HyperParser(self.editwin, b'insert-1c')
            if not hp.is_in_code():
                return
            indices = hp.get_surrounding_brackets(_openers[closer], True)
            if indices is None:
                self.warn_mismatched()
                return
            self.activate_restore()
            self.create_tag(indices)
            self.set_timeout()
            return

    def restore_event(self, event=None):
        self.text.tag_delete(b'paren')
        self.deactivate_restore()
        self.counter += 1
        return

    def handle_restore_timer(self, timer_count):
        if timer_count == self.counter:
            self.restore_event()
        return

    def warn_mismatched(self):
        if self.BELL:
            self.text.bell()
        return

    def create_tag_default(self, indices):
        self.text.tag_add(b'paren', indices[0])
        self.text.tag_config(b'paren', self.HILITE_CONFIG)
        return

    def create_tag_expression(self, indices):
        if self.text.get(indices[1]) in (b')', b']', b'}'):
            rightindex = indices[1] + b'+1c'
        else:
            rightindex = indices[1]
        self.text.tag_add(b'paren', indices[0], rightindex)
        self.text.tag_config(b'paren', self.HILITE_CONFIG)
        return

    def set_timeout_none(self):
        self.counter += 1

        def callme(callme, self=self, c=self.counter, index=self.text.index(b'insert')):
            if index != self.text.index(b'insert'):
                self.handle_restore_timer(c)
            else:
                self.editwin.text_frame.after(CHECK_DELAY, callme, callme)
            return

        self.editwin.text_frame.after(CHECK_DELAY, callme, callme)
        return

    def set_timeout_last(self):
        self.counter += 1
        self.editwin.text_frame.after(self.FLASH_DELAY, (lambda self=self, c=self.counter: self.handle_restore_timer(c)))
        return


if __name__ == b'__main__':
    import unittest
    unittest.main(b'idlelib.idle_test.test_parenmatch', verbosity=2)
