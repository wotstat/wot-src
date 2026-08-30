import sys, unittest, Tkinter as tkinter, ttk
from test.test_support import requires, run_unittest, swap_attr
from test_ttk.support import AbstractTkTest, destroy_default_root
requires(b'gui')

class LabeledScaleTest(AbstractTkTest, unittest.TestCase):

    def tearDown(self):
        self.root.update_idletasks()
        super(LabeledScaleTest, self).tearDown()
        return

    def test_widget_destroy(self):
        x = ttk.LabeledScale(self.root)
        var = x._variable._name
        x.destroy()
        self.assertRaises(tkinter.TclError, x.tk.globalgetvar, var)
        myvar = tkinter.DoubleVar(self.root)
        name = myvar._name
        x = ttk.LabeledScale(self.root, variable=myvar)
        x.destroy()
        if self.wantobjects:
            self.assertEqual(x.tk.globalgetvar(name), myvar.get())
        else:
            self.assertEqual(float(x.tk.globalgetvar(name)), myvar.get())
        del myvar
        self.assertRaises(tkinter.TclError, x.tk.globalgetvar, name)
        myvar = tkinter.IntVar(self.root)
        x = ttk.LabeledScale(self.root, variable=myvar)
        x.destroy()
        ttk.LabeledScale(self.root, variable=myvar)
        if hasattr(sys, b'last_type'):
            self.assertNotEqual(sys.last_type, tkinter.TclError)
        return

    def test_initialization_no_master(self):
        with swap_attr(tkinter, b'_default_root', None):
            with swap_attr(tkinter, b'_support_default_root', True):
                try:
                    x = ttk.LabeledScale()
                    self.assertIsNotNone(tkinter._default_root)
                    self.assertEqual(x.master, tkinter._default_root)
                    self.assertEqual(x.tk, tkinter._default_root.tk)
                    x.destroy()
                finally:
                    destroy_default_root()

        return

    def test_initialization(self):
        master = tkinter.Frame(self.root)
        x = ttk.LabeledScale(master)
        self.assertEqual(x.master, master)
        x.destroy()
        passed_expected = (
         (b'0', 0), (0, 0), (10, 10),
         (-1, -1), (sys.maxint + 1, sys.maxint + 1))
        if self.wantobjects:
            passed_expected += ((2.5, 2),)
        for pair in passed_expected:
            x = ttk.LabeledScale(self.root, from_=pair[0])
            self.assertEqual(x.value, pair[1])
            x.destroy()

        x = ttk.LabeledScale(self.root, from_=b'2.5')
        self.assertRaises(ValueError, x._variable.get)
        x.destroy()
        x = ttk.LabeledScale(self.root, from_=None)
        self.assertRaises(ValueError, x._variable.get)
        x.destroy()
        myvar = tkinter.DoubleVar(self.root, value=20)
        x = ttk.LabeledScale(self.root, variable=myvar)
        self.assertEqual(x.value, 0)
        x.destroy()
        x = ttk.LabeledScale(self.root, variable=myvar, from_=0.5)
        self.assertEqual(x.value, 0.5)
        self.assertEqual(x._variable._name, myvar._name)
        x.destroy()

        def check_positions(scale, scale_pos, label, label_pos):
            self.assertEqual(scale.pack_info()[b'side'], scale_pos)
            self.assertEqual(label.place_info()[b'anchor'], label_pos)
            return

        x = ttk.LabeledScale(self.root, compound=b'top')
        check_positions(x.scale, b'bottom', x.label, b'n')
        x.destroy()
        x = ttk.LabeledScale(self.root, compound=b'bottom')
        check_positions(x.scale, b'top', x.label, b's')
        x.destroy()
        x = ttk.LabeledScale(self.root, compound=b'unknown')
        check_positions(x.scale, b'top', x.label, b's')
        x.destroy()
        x = ttk.LabeledScale(self.root)
        check_positions(x.scale, b'bottom', x.label, b'n')
        x.destroy()
        self.assertRaises(tkinter.TclError, ttk.LabeledScale, master, a=b'b')
        return

    def test_horizontal_range(self):
        lscale = ttk.LabeledScale(self.root, from_=0, to=10)
        lscale.pack()
        lscale.wait_visibility()
        lscale.update()
        linfo_1 = lscale.label.place_info()
        prev_xcoord = lscale.scale.coords()[0]
        self.assertEqual(prev_xcoord, int(linfo_1[b'x']))
        lscale.scale.configure(from_=-5, to=5)
        lscale.update()
        curr_xcoord = lscale.scale.coords()[0]
        self.assertNotEqual(prev_xcoord, curr_xcoord)
        linfo_2 = lscale.label.place_info()
        self.assertEqual(lscale.label[b'text'], 0 if self.wantobjects else b'0')
        self.assertEqual(curr_xcoord, int(linfo_2[b'x']))
        lscale.scale.configure(from_=0, to=10)
        self.assertNotEqual(prev_xcoord, curr_xcoord)
        self.assertEqual(prev_xcoord, int(linfo_1[b'x']))
        lscale.destroy()
        return

    def test_variable_change(self):
        x = ttk.LabeledScale(self.root)
        x.pack()
        x.wait_visibility()
        x.update()
        curr_xcoord = x.scale.coords()[0]
        newval = x.value + 1
        x.value = newval
        x.update()
        self.assertEqual(x.label[b'text'], newval if self.wantobjects else str(newval))
        self.assertGreater(x.scale.coords()[0], curr_xcoord)
        self.assertEqual(x.scale.coords()[0], int(x.label.place_info()[b'x']))
        if self.wantobjects:
            conv = lambda x: x
        else:
            conv = int
        x.value = conv(x.scale[b'to']) + 1
        x.update()
        self.assertEqual(conv(x.label[b'text']), newval)
        self.assertEqual(x.scale.coords()[0], int(x.label.place_info()[b'x']))
        x.destroy()
        return

    def test_resize(self):
        x = ttk.LabeledScale(self.root)
        x.pack(expand=True, fill=b'both')
        x.wait_visibility()
        x.update()
        width, height = x.master.winfo_width(), x.master.winfo_height()
        width_new, height_new = width * 2, height * 2
        x.value = 3
        x.update()
        x.master.wm_geometry(b'%dx%d' % (width_new, height_new))
        self.assertEqual(int(x.label.place_info()[b'x']), x.scale.coords()[0])
        x.master.wm_geometry(b'%dx%d' % (width, height))
        x.destroy()
        return


class OptionMenuTest(AbstractTkTest, unittest.TestCase):

    def setUp(self):
        super(OptionMenuTest, self).setUp()
        self.textvar = tkinter.StringVar(self.root)
        return

    def tearDown(self):
        del self.textvar
        super(OptionMenuTest, self).tearDown()
        return

    def test_widget_destroy(self):
        var = tkinter.StringVar(self.root)
        optmenu = ttk.OptionMenu(self.root, var)
        name = var._name
        optmenu.update_idletasks()
        optmenu.destroy()
        self.assertEqual(optmenu.tk.globalgetvar(name), var.get())
        del var
        self.assertRaises(tkinter.TclError, optmenu.tk.globalgetvar, name)
        return

    def test_initialization(self):
        self.assertRaises(tkinter.TclError, ttk.OptionMenu, self.root, self.textvar, invalid=b'thing')
        optmenu = ttk.OptionMenu(self.root, self.textvar, b'b', b'a', b'b')
        self.assertEqual(optmenu._variable.get(), b'b')
        self.assertTrue(optmenu[b'menu'])
        self.assertTrue(optmenu[b'textvariable'])
        optmenu.destroy()
        return

    def test_menu(self):
        items = (b'a', b'b', b'c')
        default = b'a'
        optmenu = ttk.OptionMenu(self.root, self.textvar, default, *items)
        found_default = False
        for i in range(len(items)):
            value = optmenu[b'menu'].entrycget(i, b'value')
            self.assertEqual(value, items[i])
            if value == default:
                found_default = True

        self.assertTrue(found_default)
        optmenu.destroy()
        default = b'd'
        optmenu = ttk.OptionMenu(self.root, self.textvar, default, *items)
        curr = None
        i = 0
        while True:
            last, curr = curr, optmenu[b'menu'].entryconfigure(i, b'value')
            if last == curr:
                break
            self.assertNotEqual(curr, default)
            i += 1

        self.assertEqual(i, len(items))
        optmenu.pack()
        optmenu.wait_visibility()
        optmenu[b'menu'].invoke(0)
        self.assertEqual(optmenu._variable.get(), items[0])
        self.assertRaises(tkinter.TclError, optmenu[b'menu'].invoke, -1)
        self.assertEqual(optmenu._variable.get(), items[0])
        optmenu.destroy()
        success = []

        def cb_test(item):
            self.assertEqual(item, items[1])
            success.append(True)
            return

        optmenu = ttk.OptionMenu(self.root, self.textvar, b'a', command=cb_test, *items)
        optmenu[b'menu'].invoke(1)
        if not success:
            self.fail(b'Menu callback not invoked')
        optmenu.destroy()
        return

    def test_unique_radiobuttons(self):
        items = (b'a', b'b', b'c')
        default = b'a'
        optmenu = ttk.OptionMenu(self.root, self.textvar, default, *items)
        textvar2 = tkinter.StringVar(self.root)
        optmenu2 = ttk.OptionMenu(self.root, textvar2, default, *items)
        optmenu.pack()
        optmenu.wait_visibility()
        optmenu2.pack()
        optmenu2.wait_visibility()
        optmenu[b'menu'].invoke(1)
        optmenu2[b'menu'].invoke(2)
        optmenu_stringvar_name = optmenu[b'menu'].entrycget(0, b'variable')
        optmenu2_stringvar_name = optmenu2[b'menu'].entrycget(0, b'variable')
        self.assertNotEqual(optmenu_stringvar_name, optmenu2_stringvar_name)
        self.assertEqual(self.root.tk.globalgetvar(optmenu_stringvar_name), items[1])
        self.assertEqual(self.root.tk.globalgetvar(optmenu2_stringvar_name), items[2])
        optmenu.destroy()
        optmenu2.destroy()
        return


tests_gui = (
 LabeledScaleTest, OptionMenuTest)
if __name__ == b'__main__':
    run_unittest(*tests_gui)
