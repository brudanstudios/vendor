import os
import sys
import imp
import inspect


class Loader(object):
    def __init__(self, f, filename, description):
        self._f = f
        self._filename = filename
        self._description = description

    def load_module(self, fullname):
        mod = imp.load_module(fullname, self._f, self._filename, self._description)
        return mod


class Finder(object):

    def __init__(self, vendor_dir):
        self._vendor_dir = vendor_dir.rstrip(os.path.sep) + os.path.sep

    def find_module(self, fullname, path=None):

        previous_frame = inspect.currentframe().f_back
        filename, _, _, _, _ = inspect.getframeinfo(previous_frame)

        if not filename.startswith(self._vendor_dir):
            return

        if '{0}_vendor{0}'.format(os.path.sep) in filename[len(self._vendor_dir):]:
            return

        try:
            f, filename, description = imp.find_module(fullname, [self._vendor_dir])
        except ImportError as e:
            pass
        else:
            return Loader(f, filename, description)

    def __eq__(self, other):
        return self._vendor_dir == other._vendor_dir


def register(vendor_dir=None):
    if not vendor_dir:
        vendor_dir = os.path.abspath(os.path.dirname(__file__))

    finder = Finder(vendor_dir)

    if finder not in sys.meta_path:
        sys.meta_path.append(finder)