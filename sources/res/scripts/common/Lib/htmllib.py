from warnings import warnpy3k
warnpy3k(b'the htmllib module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
import sgmllib
from formatter import AS_IS
__all__ = [
 b'HTMLParser', b'HTMLParseError']

class HTMLParseError(sgmllib.SGMLParseError):
    pass


class HTMLParser(sgmllib.SGMLParser):
    from htmlentitydefs import entitydefs

    def __init__(self, formatter, verbose=0):
        sgmllib.SGMLParser.__init__(self, verbose)
        self.formatter = formatter
        return

    def error(self, message):
        raise HTMLParseError(message)
        return

    def reset(self):
        sgmllib.SGMLParser.reset(self)
        self.savedata = None
        self.isindex = 0
        self.title = None
        self.base = None
        self.anchor = None
        self.anchorlist = []
        self.nofill = 0
        self.list_stack = []
        return

    def handle_data(self, data):
        if self.savedata is not None:
            self.savedata = self.savedata + data
        elif self.nofill:
            self.formatter.add_literal_data(data)
        else:
            self.formatter.add_flowing_data(data)
        return

    def save_bgn(self):
        self.savedata = b''
        return

    def save_end(self):
        data = self.savedata
        self.savedata = None
        if not self.nofill:
            data = (b' ').join(data.split())
        return data

    def anchor_bgn(self, href, name, type):
        self.anchor = href
        if self.anchor:
            self.anchorlist.append(href)
        return

    def anchor_end(self):
        if self.anchor:
            self.handle_data(b'[%d]' % len(self.anchorlist))
            self.anchor = None
        return

    def handle_image(self, src, alt, *args):
        self.handle_data(alt)
        return

    def start_html(self, attrs):
        return

    def end_html(self):
        return

    def start_head(self, attrs):
        return

    def end_head(self):
        return

    def start_body(self, attrs):
        return

    def end_body(self):
        return

    def start_title(self, attrs):
        self.save_bgn()
        return

    def end_title(self):
        self.title = self.save_end()
        return

    def do_base(self, attrs):
        for a, v in attrs:
            if a == b'href':
                self.base = v

        return

    def do_isindex(self, attrs):
        self.isindex = 1
        return

    def do_link(self, attrs):
        return

    def do_meta(self, attrs):
        return

    def do_nextid(self, attrs):
        return

    def start_h1(self, attrs):
        self.formatter.end_paragraph(1)
        self.formatter.push_font((b'h1', 0, 1, 0))
        return

    def end_h1(self):
        self.formatter.end_paragraph(1)
        self.formatter.pop_font()
        return

    def start_h2(self, attrs):
        self.formatter.end_paragraph(1)
        self.formatter.push_font((b'h2', 0, 1, 0))
        return

    def end_h2(self):
        self.formatter.end_paragraph(1)
        self.formatter.pop_font()
        return

    def start_h3(self, attrs):
        self.formatter.end_paragraph(1)
        self.formatter.push_font((b'h3', 0, 1, 0))
        return

    def end_h3(self):
        self.formatter.end_paragraph(1)
        self.formatter.pop_font()
        return

    def start_h4(self, attrs):
        self.formatter.end_paragraph(1)
        self.formatter.push_font((b'h4', 0, 1, 0))
        return

    def end_h4(self):
        self.formatter.end_paragraph(1)
        self.formatter.pop_font()
        return

    def start_h5(self, attrs):
        self.formatter.end_paragraph(1)
        self.formatter.push_font((b'h5', 0, 1, 0))
        return

    def end_h5(self):
        self.formatter.end_paragraph(1)
        self.formatter.pop_font()
        return

    def start_h6(self, attrs):
        self.formatter.end_paragraph(1)
        self.formatter.push_font((b'h6', 0, 1, 0))
        return

    def end_h6(self):
        self.formatter.end_paragraph(1)
        self.formatter.pop_font()
        return

    def do_p(self, attrs):
        self.formatter.end_paragraph(1)
        return

    def start_pre(self, attrs):
        self.formatter.end_paragraph(1)
        self.formatter.push_font((AS_IS, AS_IS, AS_IS, 1))
        self.nofill = self.nofill + 1
        return

    def end_pre(self):
        self.formatter.end_paragraph(1)
        self.formatter.pop_font()
        self.nofill = max(0, self.nofill - 1)
        return

    def start_xmp(self, attrs):
        self.start_pre(attrs)
        self.setliteral(b'xmp')
        return

    def end_xmp(self):
        self.end_pre()
        return

    def start_listing(self, attrs):
        self.start_pre(attrs)
        self.setliteral(b'listing')
        return

    def end_listing(self):
        self.end_pre()
        return

    def start_address(self, attrs):
        self.formatter.end_paragraph(0)
        self.formatter.push_font((AS_IS, 1, AS_IS, AS_IS))
        return

    def end_address(self):
        self.formatter.end_paragraph(0)
        self.formatter.pop_font()
        return

    def start_blockquote(self, attrs):
        self.formatter.end_paragraph(1)
        self.formatter.push_margin(b'blockquote')
        return

    def end_blockquote(self):
        self.formatter.end_paragraph(1)
        self.formatter.pop_margin()
        return

    def start_ul(self, attrs):
        self.formatter.end_paragraph(not self.list_stack)
        self.formatter.push_margin(b'ul')
        self.list_stack.append([b'ul', b'*', 0])
        return

    def end_ul(self):
        if self.list_stack:
            del self.list_stack[-1]
        self.formatter.end_paragraph(not self.list_stack)
        self.formatter.pop_margin()
        return

    def do_li(self, attrs):
        self.formatter.end_paragraph(0)
        if self.list_stack:
            dummy, label, counter = top = self.list_stack[-1]
            top[2] = counter = counter + 1
        else:
            label, counter = (b'*', 0)
        self.formatter.add_label_data(label, counter)
        return

    def start_ol(self, attrs):
        self.formatter.end_paragraph(not self.list_stack)
        self.formatter.push_margin(b'ol')
        label = b'1.'
        for a, v in attrs:
            if a == b'type':
                if len(v) == 1:
                    v = v + b'.'
                label = v

        self.list_stack.append([b'ol', label, 0])
        return

    def end_ol(self):
        if self.list_stack:
            del self.list_stack[-1]
        self.formatter.end_paragraph(not self.list_stack)
        self.formatter.pop_margin()
        return

    def start_menu(self, attrs):
        self.start_ul(attrs)
        return

    def end_menu(self):
        self.end_ul()
        return

    def start_dir(self, attrs):
        self.start_ul(attrs)
        return

    def end_dir(self):
        self.end_ul()
        return

    def start_dl(self, attrs):
        self.formatter.end_paragraph(1)
        self.list_stack.append([b'dl', b'', 0])
        return

    def end_dl(self):
        self.ddpop(1)
        if self.list_stack:
            del self.list_stack[-1]
        return

    def do_dt(self, attrs):
        self.ddpop()
        return

    def do_dd(self, attrs):
        self.ddpop()
        self.formatter.push_margin(b'dd')
        self.list_stack.append([b'dd', b'', 0])
        return

    def ddpop(self, bl=0):
        self.formatter.end_paragraph(bl)
        if self.list_stack:
            if self.list_stack[-1][0] == b'dd':
                del self.list_stack[-1]
                self.formatter.pop_margin()
        return

    def start_cite(self, attrs):
        self.start_i(attrs)
        return

    def end_cite(self):
        self.end_i()
        return

    def start_code(self, attrs):
        self.start_tt(attrs)
        return

    def end_code(self):
        self.end_tt()
        return

    def start_em(self, attrs):
        self.start_i(attrs)
        return

    def end_em(self):
        self.end_i()
        return

    def start_kbd(self, attrs):
        self.start_tt(attrs)
        return

    def end_kbd(self):
        self.end_tt()
        return

    def start_samp(self, attrs):
        self.start_tt(attrs)
        return

    def end_samp(self):
        self.end_tt()
        return

    def start_strong(self, attrs):
        self.start_b(attrs)
        return

    def end_strong(self):
        self.end_b()
        return

    def start_var(self, attrs):
        self.start_i(attrs)
        return

    def end_var(self):
        self.end_i()
        return

    def start_i(self, attrs):
        self.formatter.push_font((AS_IS, 1, AS_IS, AS_IS))
        return

    def end_i(self):
        self.formatter.pop_font()
        return

    def start_b(self, attrs):
        self.formatter.push_font((AS_IS, AS_IS, 1, AS_IS))
        return

    def end_b(self):
        self.formatter.pop_font()
        return

    def start_tt(self, attrs):
        self.formatter.push_font((AS_IS, AS_IS, AS_IS, 1))
        return

    def end_tt(self):
        self.formatter.pop_font()
        return

    def start_a(self, attrs):
        href = b''
        name = b''
        type = b''
        for attrname, value in attrs:
            value = value.strip()
            if attrname == b'href':
                href = value
            if attrname == b'name':
                name = value
            if attrname == b'type':
                type = value.lower()

        self.anchor_bgn(href, name, type)
        return

    def end_a(self):
        self.anchor_end()
        return

    def do_br(self, attrs):
        self.formatter.add_line_break()
        return

    def do_hr(self, attrs):
        self.formatter.add_hor_rule()
        return

    def do_img(self, attrs):
        align = b''
        alt = b'(image)'
        ismap = b''
        src = b''
        width = 0
        height = 0
        for attrname, value in attrs:
            if attrname == b'align':
                align = value
            if attrname == b'alt':
                alt = value
            if attrname == b'ismap':
                ismap = value
            if attrname == b'src':
                src = value
            if attrname == b'width':
                try:
                    width = int(value)
                except ValueError:
                    pass

            if attrname == b'height':
                try:
                    height = int(value)
                except ValueError:
                    pass

        self.handle_image(src, alt, ismap, align, width, height)
        return

    def do_plaintext(self, attrs):
        self.start_pre(attrs)
        self.setnomoretags()
        return

    def unknown_starttag(self, tag, attrs):
        return

    def unknown_endtag(self, tag):
        return


def test(args=None):
    import sys, formatter
    if not args:
        args = sys.argv[1:]
    silent = args and args[0] == b'-s'
    if silent:
        del args[0]
    if args:
        file = args[0]
    else:
        file = b'test.html'
    if file == b'-':
        f = sys.stdin
    else:
        try:
            f = open(file, b'r')
        except IOError as msg:
            print file, b':', msg
            sys.exit(1)

    data = f.read()
    if f is not sys.stdin:
        f.close()
    if silent:
        f = formatter.NullFormatter()
    else:
        f = formatter.AbstractFormatter(formatter.DumbWriter())
    p = HTMLParser(f)
    p.feed(data)
    p.close()
    return


if __name__ == b'__main__':
    test()
