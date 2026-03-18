r"""Wrapper for hal_base.h

Generated with:
/home/user/iec61850_open_gateway/.venv/bin/ctypesgen -l libiec60870.so -I ../lib60870/lib60870-C/src/hal/inc ../lib60870/lib60870-C/src/hal/inc/hal_base.h ../lib60870/lib60870-C/src/hal/inc/hal_serial.h ../lib60870/lib60870-C/src/hal/inc/hal_socket.h ../lib60870/lib60870-C/src/hal/inc/hal_thread.h ../lib60870/lib60870-C/src/hal/inc/hal_time.h ../lib60870/lib60870-C/src/hal/inc/lib_memory.h ../lib60870/lib60870-C/src/hal/inc/platform_endian.h ../lib60870/lib60870-C/src/hal/inc/tls_ciphers.h ../lib60870/lib60870-C/src/hal/inc/tls_config.h ../lib60870/lib60870-C/src/hal/inc/tls_socket.h -I ../lib60870/lib60870-C/src/inc/api ../lib60870/lib60870-C/src/inc/api/cs101_information_objects.h ../lib60870/lib60870-C/src/inc/api/cs101_master.h ../lib60870/lib60870-C/src/inc/api/cs101_slave.h ../lib60870/lib60870-C/src/inc/api/cs104_connection.h ../lib60870/lib60870-C/src/inc/api/cs104_slave.h ../lib60870/lib60870-C/src/inc/api/iec60870_common.h ../lib60870/lib60870-C/src/inc/api/iec60870_master.h ../lib60870/lib60870-C/src/inc/api/iec60870_slave.h ../lib60870/lib60870-C/src/inc/api/link_layer_parameters.h -o lib60870.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["libiec60870.so"] = load_library("libiec60870.so")

# 1 libraries
# End libraries

# No modules

__uint8_t = c_ubyte# /usr/include/x86_64-linux-gnu/bits/types.h: 38

__uint16_t = c_ushort# /usr/include/x86_64-linux-gnu/bits/types.h: 40

__uint32_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 42

__uint64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 45

uint8_t = __uint8_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 24

uint16_t = __uint16_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 25

uint32_t = __uint32_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 26

uint64_t = __uint64_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 27

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 39
class struct_sSerialPort(Structure):
    pass

SerialPort = POINTER(struct_sSerialPort)# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 39

enum_anon_18 = c_int# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_NONE = 0# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_INVALID_ARGUMENT = 1# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_INVALID_BAUDRATE = 2# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_OPEN_FAILED = 3# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_UNKNOWN = 99# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SerialPortError = enum_anon_18# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 61
if _libs["libiec60870.so"].has("SerialPort_create", "cdecl"):
    SerialPort_create = _libs["libiec60870.so"].get("SerialPort_create", "cdecl")
    SerialPort_create.argtypes = [String, c_int, uint8_t, c_char, uint8_t]
    SerialPort_create.restype = SerialPort

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 67
if _libs["libiec60870.so"].has("SerialPort_destroy", "cdecl"):
    SerialPort_destroy = _libs["libiec60870.so"].get("SerialPort_destroy", "cdecl")
    SerialPort_destroy.argtypes = [SerialPort]
    SerialPort_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 75
if _libs["libiec60870.so"].has("SerialPort_open", "cdecl"):
    SerialPort_open = _libs["libiec60870.so"].get("SerialPort_open", "cdecl")
    SerialPort_open.argtypes = [SerialPort]
    SerialPort_open.restype = c_bool

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 81
if _libs["libiec60870.so"].has("SerialPort_close", "cdecl"):
    SerialPort_close = _libs["libiec60870.so"].get("SerialPort_close", "cdecl")
    SerialPort_close.argtypes = [SerialPort]
    SerialPort_close.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 89
if _libs["libiec60870.so"].has("SerialPort_getBaudRate", "cdecl"):
    SerialPort_getBaudRate = _libs["libiec60870.so"].get("SerialPort_getBaudRate", "cdecl")
    SerialPort_getBaudRate.argtypes = [SerialPort]
    SerialPort_getBaudRate.restype = c_int

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 97
if _libs["libiec60870.so"].has("SerialPort_setTimeout", "cdecl"):
    SerialPort_setTimeout = _libs["libiec60870.so"].get("SerialPort_setTimeout", "cdecl")
    SerialPort_setTimeout.argtypes = [SerialPort, c_int]
    SerialPort_setTimeout.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 103
if _libs["libiec60870.so"].has("SerialPort_discardInBuffer", "cdecl"):
    SerialPort_discardInBuffer = _libs["libiec60870.so"].get("SerialPort_discardInBuffer", "cdecl")
    SerialPort_discardInBuffer.argtypes = [SerialPort]
    SerialPort_discardInBuffer.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 111
if _libs["libiec60870.so"].has("SerialPort_readByte", "cdecl"):
    SerialPort_readByte = _libs["libiec60870.so"].get("SerialPort_readByte", "cdecl")
    SerialPort_readByte.argtypes = [SerialPort]
    SerialPort_readByte.restype = c_int

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 123
if _libs["libiec60870.so"].has("SerialPort_write", "cdecl"):
    SerialPort_write = _libs["libiec60870.so"].get("SerialPort_write", "cdecl")
    SerialPort_write.argtypes = [SerialPort, POINTER(uint8_t), c_int, c_int]
    SerialPort_write.restype = c_int

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 129
if _libs["libiec60870.so"].has("SerialPort_getLastError", "cdecl"):
    SerialPort_getLastError = _libs["libiec60870.so"].get("SerialPort_getLastError", "cdecl")
    SerialPort_getLastError.argtypes = [SerialPort]
    SerialPort_getLastError.restype = SerialPortError

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 44
class struct_sServerSocket(Structure):
    pass

ServerSocket = POINTER(struct_sServerSocket)# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 44

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 46
class struct_sUdpSocket(Structure):
    pass

UdpSocket = POINTER(struct_sUdpSocket)# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 46

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 49
class struct_sSocket(Structure):
    pass

Socket = POINTER(struct_sSocket)# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 49

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 52
class struct_sHandleSet(Structure):
    pass

HandleSet = POINTER(struct_sHandleSet)# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 52

enum_anon_19 = c_int# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 60

SOCKET_STATE_CONNECTING = 0# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 60

SOCKET_STATE_FAILED = 1# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 60

SOCKET_STATE_CONNECTED = 2# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 60

SocketState = enum_anon_19# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 60

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 69
if _libs["libiec60870.so"].has("Handleset_new", "cdecl"):
    Handleset_new = _libs["libiec60870.so"].get("Handleset_new", "cdecl")
    Handleset_new.argtypes = []
    Handleset_new.restype = HandleSet

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 75
if _libs["libiec60870.so"].has("Handleset_reset", "cdecl"):
    Handleset_reset = _libs["libiec60870.so"].get("Handleset_reset", "cdecl")
    Handleset_reset.argtypes = [HandleSet]
    Handleset_reset.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 84
if _libs["libiec60870.so"].has("Handleset_addSocket", "cdecl"):
    Handleset_addSocket = _libs["libiec60870.so"].get("Handleset_addSocket", "cdecl")
    Handleset_addSocket.argtypes = [HandleSet, Socket]
    Handleset_addSocket.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 90
if _libs["libiec60870.so"].has("Handleset_removeSocket", "cdecl"):
    Handleset_removeSocket = _libs["libiec60870.so"].get("Handleset_removeSocket", "cdecl")
    Handleset_removeSocket.argtypes = [HandleSet, Socket]
    Handleset_removeSocket.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 108
if _libs["libiec60870.so"].has("Handleset_waitReady", "cdecl"):
    Handleset_waitReady = _libs["libiec60870.so"].get("Handleset_waitReady", "cdecl")
    Handleset_waitReady.argtypes = [HandleSet, c_uint]
    Handleset_waitReady.restype = c_int

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 116
if _libs["libiec60870.so"].has("Handleset_destroy", "cdecl"):
    Handleset_destroy = _libs["libiec60870.so"].get("Handleset_destroy", "cdecl")
    Handleset_destroy.argtypes = [HandleSet]
    Handleset_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 129
if _libs["libiec60870.so"].has("TcpServerSocket_create", "cdecl"):
    TcpServerSocket_create = _libs["libiec60870.so"].get("TcpServerSocket_create", "cdecl")
    TcpServerSocket_create.argtypes = [String, c_int]
    TcpServerSocket_create.restype = ServerSocket

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 137
if _libs["libiec60870.so"].has("UdpSocket_create", "cdecl"):
    UdpSocket_create = _libs["libiec60870.so"].get("UdpSocket_create", "cdecl")
    UdpSocket_create.argtypes = []
    UdpSocket_create.restype = UdpSocket

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 145
if _libs["libiec60870.so"].has("UdpSocket_createIpV6", "cdecl"):
    UdpSocket_createIpV6 = _libs["libiec60870.so"].get("UdpSocket_createIpV6", "cdecl")
    UdpSocket_createIpV6.argtypes = []
    UdpSocket_createIpV6.restype = UdpSocket

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 156
if _libs["libiec60870.so"].has("UdpSocket_addGroupMembership", "cdecl"):
    UdpSocket_addGroupMembership = _libs["libiec60870.so"].get("UdpSocket_addGroupMembership", "cdecl")
    UdpSocket_addGroupMembership.argtypes = [UdpSocket, String]
    UdpSocket_addGroupMembership.restype = c_bool

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 167
if _libs["libiec60870.so"].has("UdpSocket_setMulticastTtl", "cdecl"):
    UdpSocket_setMulticastTtl = _libs["libiec60870.so"].get("UdpSocket_setMulticastTtl", "cdecl")
    UdpSocket_setMulticastTtl.argtypes = [UdpSocket, c_int]
    UdpSocket_setMulticastTtl.restype = c_bool

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 170
if _libs["libiec60870.so"].has("UdpSocket_bind", "cdecl"):
    UdpSocket_bind = _libs["libiec60870.so"].get("UdpSocket_bind", "cdecl")
    UdpSocket_bind.argtypes = [UdpSocket, String, c_int]
    UdpSocket_bind.restype = c_bool

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 173
if _libs["libiec60870.so"].has("UdpSocket_sendTo", "cdecl"):
    UdpSocket_sendTo = _libs["libiec60870.so"].get("UdpSocket_sendTo", "cdecl")
    UdpSocket_sendTo.argtypes = [UdpSocket, String, c_int, POINTER(uint8_t), c_int]
    UdpSocket_sendTo.restype = c_bool

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 187
if _libs["libiec60870.so"].has("UdpSocket_receiveFrom", "cdecl"):
    UdpSocket_receiveFrom = _libs["libiec60870.so"].get("UdpSocket_receiveFrom", "cdecl")
    UdpSocket_receiveFrom.argtypes = [UdpSocket, String, c_int, POINTER(uint8_t), c_int]
    UdpSocket_receiveFrom.restype = c_int

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 191
if _libs["libiec60870.so"].has("ServerSocket_listen", "cdecl"):
    ServerSocket_listen = _libs["libiec60870.so"].get("ServerSocket_listen", "cdecl")
    ServerSocket_listen.argtypes = [ServerSocket]
    ServerSocket_listen.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 208
if _libs["libiec60870.so"].has("ServerSocket_accept", "cdecl"):
    ServerSocket_accept = _libs["libiec60870.so"].get("ServerSocket_accept", "cdecl")
    ServerSocket_accept.argtypes = [ServerSocket]
    ServerSocket_accept.restype = Socket

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 221
if _libs["libiec60870.so"].has("Socket_activateTcpKeepAlive", "cdecl"):
    Socket_activateTcpKeepAlive = _libs["libiec60870.so"].get("Socket_activateTcpKeepAlive", "cdecl")
    Socket_activateTcpKeepAlive.argtypes = [Socket, c_int, c_int, c_int]
    Socket_activateTcpKeepAlive.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 233
if _libs["libiec60870.so"].has("ServerSocket_setBacklog", "cdecl"):
    ServerSocket_setBacklog = _libs["libiec60870.so"].get("ServerSocket_setBacklog", "cdecl")
    ServerSocket_setBacklog.argtypes = [ServerSocket, c_int]
    ServerSocket_setBacklog.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 245
if _libs["libiec60870.so"].has("ServerSocket_destroy", "cdecl"):
    ServerSocket_destroy = _libs["libiec60870.so"].get("ServerSocket_destroy", "cdecl")
    ServerSocket_destroy.argtypes = [ServerSocket]
    ServerSocket_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 255
if _libs["libiec60870.so"].has("TcpSocket_create", "cdecl"):
    TcpSocket_create = _libs["libiec60870.so"].get("TcpSocket_create", "cdecl")
    TcpSocket_create.argtypes = []
    TcpSocket_create.restype = Socket

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 264
if _libs["libiec60870.so"].has("Socket_setConnectTimeout", "cdecl"):
    Socket_setConnectTimeout = _libs["libiec60870.so"].get("Socket_setConnectTimeout", "cdecl")
    Socket_setConnectTimeout.argtypes = [Socket, uint32_t]
    Socket_setConnectTimeout.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 278
if _libs["libiec60870.so"].has("Socket_bind", "cdecl"):
    Socket_bind = _libs["libiec60870.so"].get("Socket_bind", "cdecl")
    Socket_bind.argtypes = [Socket, String, c_int]
    Socket_bind.restype = c_bool

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 299
if _libs["libiec60870.so"].has("Socket_connect", "cdecl"):
    Socket_connect = _libs["libiec60870.so"].get("Socket_connect", "cdecl")
    Socket_connect.argtypes = [Socket, String, c_int]
    Socket_connect.restype = c_bool

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 302
if _libs["libiec60870.so"].has("Socket_connectAsync", "cdecl"):
    Socket_connectAsync = _libs["libiec60870.so"].get("Socket_connectAsync", "cdecl")
    Socket_connectAsync.argtypes = [Socket, String, c_int]
    Socket_connectAsync.restype = c_bool

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 305
if _libs["libiec60870.so"].has("Socket_checkAsyncConnectState", "cdecl"):
    Socket_checkAsyncConnectState = _libs["libiec60870.so"].get("Socket_checkAsyncConnectState", "cdecl")
    Socket_checkAsyncConnectState.argtypes = [Socket]
    Socket_checkAsyncConnectState.restype = SocketState

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 324
if _libs["libiec60870.so"].has("Socket_read", "cdecl"):
    Socket_read = _libs["libiec60870.so"].get("Socket_read", "cdecl")
    Socket_read.argtypes = [Socket, POINTER(uint8_t), c_int]
    Socket_read.restype = c_int

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 336
if _libs["libiec60870.so"].has("Socket_write", "cdecl"):
    Socket_write = _libs["libiec60870.so"].get("Socket_write", "cdecl")
    Socket_write.argtypes = [Socket, POINTER(uint8_t), c_int]
    Socket_write.restype = c_int

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 338
if _libs["libiec60870.so"].has("Socket_getLocalAddress", "cdecl"):
    Socket_getLocalAddress = _libs["libiec60870.so"].get("Socket_getLocalAddress", "cdecl")
    Socket_getLocalAddress.argtypes = [Socket]
    if sizeof(c_int) == sizeof(c_void_p):
        Socket_getLocalAddress.restype = ReturnString
    else:
        Socket_getLocalAddress.restype = String
        Socket_getLocalAddress.errcheck = ReturnString

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 352
if _libs["libiec60870.so"].has("Socket_getPeerAddress", "cdecl"):
    Socket_getPeerAddress = _libs["libiec60870.so"].get("Socket_getPeerAddress", "cdecl")
    Socket_getPeerAddress.argtypes = [Socket]
    if sizeof(c_int) == sizeof(c_void_p):
        Socket_getPeerAddress.restype = ReturnString
    else:
        Socket_getPeerAddress.restype = String
        Socket_getPeerAddress.errcheck = ReturnString

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 369
if _libs["libiec60870.so"].has("Socket_getPeerAddressStatic", "cdecl"):
    Socket_getPeerAddressStatic = _libs["libiec60870.so"].get("Socket_getPeerAddressStatic", "cdecl")
    Socket_getPeerAddressStatic.argtypes = [Socket, String]
    if sizeof(c_int) == sizeof(c_void_p):
        Socket_getPeerAddressStatic.restype = ReturnString
    else:
        Socket_getPeerAddressStatic.restype = String
        Socket_getPeerAddressStatic.errcheck = ReturnString

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 383
if _libs["libiec60870.so"].has("Socket_destroy", "cdecl"):
    Socket_destroy = _libs["libiec60870.so"].get("Socket_destroy", "cdecl")
    Socket_destroy.argtypes = [Socket]
    Socket_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 38
class struct_sThread(Structure):
    pass

Thread = POINTER(struct_sThread)# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 38

Semaphore = POINTER(None)# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 41

ThreadExecutionFunction = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(None))# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 44

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 56
if _libs["libiec60870.so"].has("Thread_create", "cdecl"):
    Thread_create = _libs["libiec60870.so"].get("Thread_create", "cdecl")
    Thread_create.argtypes = [ThreadExecutionFunction, POINTER(None), c_bool]
    Thread_create.restype = Thread

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 67
if _libs["libiec60870.so"].has("Thread_start", "cdecl"):
    Thread_start = _libs["libiec60870.so"].get("Thread_start", "cdecl")
    Thread_start.argtypes = [Thread]
    Thread_start.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 75
if _libs["libiec60870.so"].has("Thread_destroy", "cdecl"):
    Thread_destroy = _libs["libiec60870.so"].get("Thread_destroy", "cdecl")
    Thread_destroy.argtypes = [Thread]
    Thread_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 81
if _libs["libiec60870.so"].has("Thread_sleep", "cdecl"):
    Thread_sleep = _libs["libiec60870.so"].get("Thread_sleep", "cdecl")
    Thread_sleep.argtypes = [c_int]
    Thread_sleep.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 84
if _libs["libiec60870.so"].has("Semaphore_create", "cdecl"):
    Semaphore_create = _libs["libiec60870.so"].get("Semaphore_create", "cdecl")
    Semaphore_create.argtypes = [c_int]
    Semaphore_create.restype = Semaphore

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 88
if _libs["libiec60870.so"].has("Semaphore_wait", "cdecl"):
    Semaphore_wait = _libs["libiec60870.so"].get("Semaphore_wait", "cdecl")
    Semaphore_wait.argtypes = [Semaphore]
    Semaphore_wait.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 91
if _libs["libiec60870.so"].has("Semaphore_post", "cdecl"):
    Semaphore_post = _libs["libiec60870.so"].get("Semaphore_post", "cdecl")
    Semaphore_post.argtypes = [Semaphore]
    Semaphore_post.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 94
if _libs["libiec60870.so"].has("Semaphore_destroy", "cdecl"):
    Semaphore_destroy = _libs["libiec60870.so"].get("Semaphore_destroy", "cdecl")
    Semaphore_destroy.argtypes = [Semaphore]
    Semaphore_destroy.restype = None

nsSinceEpoch = uint64_t# /home/user/lib60870/lib60870-C/src/hal/inc/hal_time.h: 35

msSinceEpoch = uint64_t# /home/user/lib60870/lib60870-C/src/hal/inc/hal_time.h: 36

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_time.h: 47
if _libs["libiec60870.so"].has("Hal_getTimeInMs", "cdecl"):
    Hal_getTimeInMs = _libs["libiec60870.so"].get("Hal_getTimeInMs", "cdecl")
    Hal_getTimeInMs.argtypes = []
    Hal_getTimeInMs.restype = msSinceEpoch

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_time.h: 58
if _libs["libiec60870.so"].has("Hal_getTimeInNs", "cdecl"):
    Hal_getTimeInNs = _libs["libiec60870.so"].get("Hal_getTimeInNs", "cdecl")
    Hal_getTimeInNs.argtypes = []
    Hal_getTimeInNs.restype = nsSinceEpoch

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_time.h: 69
if _libs["libiec60870.so"].has("Hal_setTimeInNs", "cdecl"):
    Hal_setTimeInNs = _libs["libiec60870.so"].get("Hal_setTimeInNs", "cdecl")
    Hal_setTimeInNs.argtypes = [nsSinceEpoch]
    Hal_setTimeInNs.restype = c_bool

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_time.h: 77
if _libs["libiec60870.so"].has("Hal_getMonotonicTimeInMs", "cdecl"):
    Hal_getMonotonicTimeInMs = _libs["libiec60870.so"].get("Hal_getMonotonicTimeInMs", "cdecl")
    Hal_getMonotonicTimeInMs.argtypes = []
    Hal_getMonotonicTimeInMs.restype = msSinceEpoch

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_time.h: 85
if _libs["libiec60870.so"].has("Hal_getMonotonicTimeInNs", "cdecl"):
    Hal_getMonotonicTimeInNs = _libs["libiec60870.so"].get("Hal_getMonotonicTimeInNs", "cdecl")
    Hal_getMonotonicTimeInNs.argtypes = []
    Hal_getMonotonicTimeInNs.restype = nsSinceEpoch

MemoryExceptionHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None))# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 32

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 35
if _libs["libiec60870.so"].has("Memory_installExceptionHandler", "cdecl"):
    Memory_installExceptionHandler = _libs["libiec60870.so"].get("Memory_installExceptionHandler", "cdecl")
    Memory_installExceptionHandler.argtypes = [MemoryExceptionHandler, POINTER(None)]
    Memory_installExceptionHandler.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 37
if _libs["libiec60870.so"].has("Memory_malloc", "cdecl"):
    Memory_malloc = _libs["libiec60870.so"].get("Memory_malloc", "cdecl")
    Memory_malloc.argtypes = [c_size_t]
    Memory_malloc.restype = POINTER(c_ubyte)
    Memory_malloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 40
if _libs["libiec60870.so"].has("Memory_calloc", "cdecl"):
    Memory_calloc = _libs["libiec60870.so"].get("Memory_calloc", "cdecl")
    Memory_calloc.argtypes = [c_size_t, c_size_t]
    Memory_calloc.restype = POINTER(c_ubyte)
    Memory_calloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 43
if _libs["libiec60870.so"].has("Memory_realloc", "cdecl"):
    Memory_realloc = _libs["libiec60870.so"].get("Memory_realloc", "cdecl")
    Memory_realloc.argtypes = [POINTER(None), c_size_t]
    Memory_realloc.restype = POINTER(c_ubyte)
    Memory_realloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 47
if _libs["libiec60870.so"].has("Memory_free", "cdecl"):
    Memory_free = _libs["libiec60870.so"].get("Memory_free", "cdecl")
    Memory_free.argtypes = [POINTER(None)]
    Memory_free.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 38
class struct_sTLSConfiguration(Structure):
    pass

TLSConfiguration = POINTER(struct_sTLSConfiguration)# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 38

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 48
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_create", "cdecl"):
        continue
    TLSConfiguration_create = _lib.get("TLSConfiguration_create", "cdecl")
    TLSConfiguration_create.argtypes = []
    TLSConfiguration_create.restype = TLSConfiguration
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 52
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setClientMode", "cdecl"):
        continue
    TLSConfiguration_setClientMode = _lib.get("TLSConfiguration_setClientMode", "cdecl")
    TLSConfiguration_setClientMode.argtypes = [TLSConfiguration]
    TLSConfiguration_setClientMode.restype = None
    break

enum_anon_20 = c_int# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 61

TLS_VERSION_NOT_SELECTED = 0# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 61

TLS_VERSION_SSL_3_0 = 3# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 61

TLS_VERSION_TLS_1_0 = 4# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 61

TLS_VERSION_TLS_1_1 = 5# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 61

TLS_VERSION_TLS_1_2 = 6# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 61

TLS_VERSION_TLS_1_3 = 7# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 61

TLSConfigVersion = enum_anon_20# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 61

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 70
for _lib in _libs.values():
    if not _lib.has("TLSConfigVersion_toString", "cdecl"):
        continue
    TLSConfigVersion_toString = _lib.get("TLSConfigVersion_toString", "cdecl")
    TLSConfigVersion_toString.argtypes = [TLSConfigVersion]
    TLSConfigVersion_toString.restype = c_char_p
    break

enum_anon_21 = c_int# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 77

TLS_SEC_EVT_INFO = 0# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 77

TLS_SEC_EVT_WARNING = 1# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 77

TLS_SEC_EVT_INCIDENT = 2# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 77

TLSEventLevel = enum_anon_21# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 77

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 108
class struct_sTLSConnection(Structure):
    pass

TLSConnection = POINTER(struct_sTLSConnection)# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 108

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 118
for _lib in _libs.values():
    if not _lib.has("TLSConnection_getPeerAddress", "cdecl"):
        continue
    TLSConnection_getPeerAddress = _lib.get("TLSConnection_getPeerAddress", "cdecl")
    TLSConnection_getPeerAddress.argtypes = [TLSConnection, String]
    if sizeof(c_int) == sizeof(c_void_p):
        TLSConnection_getPeerAddress.restype = ReturnString
    else:
        TLSConnection_getPeerAddress.restype = String
        TLSConnection_getPeerAddress.errcheck = ReturnString
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 129
for _lib in _libs.values():
    if not _lib.has("TLSConnection_getPeerCertificate", "cdecl"):
        continue
    TLSConnection_getPeerCertificate = _lib.get("TLSConnection_getPeerCertificate", "cdecl")
    TLSConnection_getPeerCertificate.argtypes = [TLSConnection, POINTER(c_int)]
    TLSConnection_getPeerCertificate.restype = POINTER(uint8_t)
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 140
for _lib in _libs.values():
    if not _lib.has("TLSConnection_getTLSVersion", "cdecl"):
        continue
    TLSConnection_getTLSVersion = _lib.get("TLSConnection_getTLSVersion", "cdecl")
    TLSConnection_getTLSVersion.argtypes = [TLSConnection]
    TLSConnection_getTLSVersion.restype = TLSConfigVersion
    break

TLSConfiguration_EventHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), TLSEventLevel, c_int, String, TLSConnection)# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 142

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 151
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setEventHandler", "cdecl"):
        continue
    TLSConfiguration_setEventHandler = _lib.get("TLSConfiguration_setEventHandler", "cdecl")
    TLSConfiguration_setEventHandler.argtypes = [TLSConfiguration, TLSConfiguration_EventHandler, POINTER(None)]
    TLSConfiguration_setEventHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 162
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_enableSessionResumption", "cdecl"):
        continue
    TLSConfiguration_enableSessionResumption = _lib.get("TLSConfiguration_enableSessionResumption", "cdecl")
    TLSConfiguration_enableSessionResumption.argtypes = [TLSConfiguration, c_bool]
    TLSConfiguration_enableSessionResumption.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 170
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setSessionResumptionInterval", "cdecl"):
        continue
    TLSConfiguration_setSessionResumptionInterval = _lib.get("TLSConfiguration_setSessionResumptionInterval", "cdecl")
    TLSConfiguration_setSessionResumptionInterval.argtypes = [TLSConfiguration, c_int]
    TLSConfiguration_setSessionResumptionInterval.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 178
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setChainValidation", "cdecl"):
        continue
    TLSConfiguration_setChainValidation = _lib.get("TLSConfiguration_setChainValidation", "cdecl")
    TLSConfiguration_setChainValidation.argtypes = [TLSConfiguration, c_bool]
    TLSConfiguration_setChainValidation.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 186
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setTimeValidation", "cdecl"):
        continue
    TLSConfiguration_setTimeValidation = _lib.get("TLSConfiguration_setTimeValidation", "cdecl")
    TLSConfiguration_setTimeValidation.argtypes = [TLSConfiguration, c_bool]
    TLSConfiguration_setTimeValidation.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 197
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setAllowOnlyKnownCertificates", "cdecl"):
        continue
    TLSConfiguration_setAllowOnlyKnownCertificates = _lib.get("TLSConfiguration_setAllowOnlyKnownCertificates", "cdecl")
    TLSConfiguration_setAllowOnlyKnownCertificates.argtypes = [TLSConfiguration, c_bool]
    TLSConfiguration_setAllowOnlyKnownCertificates.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 208
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setOwnCertificate", "cdecl"):
        continue
    TLSConfiguration_setOwnCertificate = _lib.get("TLSConfiguration_setOwnCertificate", "cdecl")
    TLSConfiguration_setOwnCertificate.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int]
    TLSConfiguration_setOwnCertificate.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 218
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setOwnCertificateFromFile", "cdecl"):
        continue
    TLSConfiguration_setOwnCertificateFromFile = _lib.get("TLSConfiguration_setOwnCertificateFromFile", "cdecl")
    TLSConfiguration_setOwnCertificateFromFile.argtypes = [TLSConfiguration, String]
    TLSConfiguration_setOwnCertificateFromFile.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 230
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setOwnKey", "cdecl"):
        continue
    TLSConfiguration_setOwnKey = _lib.get("TLSConfiguration_setOwnKey", "cdecl")
    TLSConfiguration_setOwnKey.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int, String]
    TLSConfiguration_setOwnKey.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 241
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setOwnKeyFromFile", "cdecl"):
        continue
    TLSConfiguration_setOwnKeyFromFile = _lib.get("TLSConfiguration_setOwnKeyFromFile", "cdecl")
    TLSConfiguration_setOwnKeyFromFile.argtypes = [TLSConfiguration, String, String]
    TLSConfiguration_setOwnKeyFromFile.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 251
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addAllowedCertificate", "cdecl"):
        continue
    TLSConfiguration_addAllowedCertificate = _lib.get("TLSConfiguration_addAllowedCertificate", "cdecl")
    TLSConfiguration_addAllowedCertificate.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int]
    TLSConfiguration_addAllowedCertificate.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 260
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addAllowedCertificateFromFile", "cdecl"):
        continue
    TLSConfiguration_addAllowedCertificateFromFile = _lib.get("TLSConfiguration_addAllowedCertificateFromFile", "cdecl")
    TLSConfiguration_addAllowedCertificateFromFile.argtypes = [TLSConfiguration, String]
    TLSConfiguration_addAllowedCertificateFromFile.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 270
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCACertificate", "cdecl"):
        continue
    TLSConfiguration_addCACertificate = _lib.get("TLSConfiguration_addCACertificate", "cdecl")
    TLSConfiguration_addCACertificate.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int]
    TLSConfiguration_addCACertificate.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 279
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCACertificateFromFile", "cdecl"):
        continue
    TLSConfiguration_addCACertificateFromFile = _lib.get("TLSConfiguration_addCACertificateFromFile", "cdecl")
    TLSConfiguration_addCACertificateFromFile.argtypes = [TLSConfiguration, String]
    TLSConfiguration_addCACertificateFromFile.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 289
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setRenegotiationTime", "cdecl"):
        continue
    TLSConfiguration_setRenegotiationTime = _lib.get("TLSConfiguration_setRenegotiationTime", "cdecl")
    TLSConfiguration_setRenegotiationTime.argtypes = [TLSConfiguration, c_int]
    TLSConfiguration_setRenegotiationTime.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 302
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setRenegotiationTimeout", "cdecl"):
        continue
    TLSConfiguration_setRenegotiationTimeout = _lib.get("TLSConfiguration_setRenegotiationTimeout", "cdecl")
    TLSConfiguration_setRenegotiationTimeout.argtypes = [TLSConfiguration, c_int]
    TLSConfiguration_setRenegotiationTimeout.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 308
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setMinTlsVersion", "cdecl"):
        continue
    TLSConfiguration_setMinTlsVersion = _lib.get("TLSConfiguration_setMinTlsVersion", "cdecl")
    TLSConfiguration_setMinTlsVersion.argtypes = [TLSConfiguration, TLSConfigVersion]
    TLSConfiguration_setMinTlsVersion.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 314
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setMaxTlsVersion", "cdecl"):
        continue
    TLSConfiguration_setMaxTlsVersion = _lib.get("TLSConfiguration_setMaxTlsVersion", "cdecl")
    TLSConfiguration_setMaxTlsVersion.argtypes = [TLSConfiguration, TLSConfigVersion]
    TLSConfiguration_setMaxTlsVersion.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 322
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setMinimumKeyLength", "cdecl"):
        continue
    TLSConfiguration_setMinimumKeyLength = _lib.get("TLSConfiguration_setMinimumKeyLength", "cdecl")
    TLSConfiguration_setMinimumKeyLength.argtypes = [TLSConfiguration, c_int]
    TLSConfiguration_setMinimumKeyLength.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 332
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCRL", "cdecl"):
        continue
    TLSConfiguration_addCRL = _lib.get("TLSConfiguration_addCRL", "cdecl")
    TLSConfiguration_addCRL.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int]
    TLSConfiguration_addCRL.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 341
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCRLFromFile", "cdecl"):
        continue
    TLSConfiguration_addCRLFromFile = _lib.get("TLSConfiguration_addCRLFromFile", "cdecl")
    TLSConfiguration_addCRLFromFile.argtypes = [TLSConfiguration, String]
    TLSConfiguration_addCRLFromFile.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 347
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_resetCRL", "cdecl"):
        continue
    TLSConfiguration_resetCRL = _lib.get("TLSConfiguration_resetCRL", "cdecl")
    TLSConfiguration_resetCRL.argtypes = [TLSConfiguration]
    TLSConfiguration_resetCRL.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 356
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCipherSuite", "cdecl"):
        continue
    TLSConfiguration_addCipherSuite = _lib.get("TLSConfiguration_addCipherSuite", "cdecl")
    TLSConfiguration_addCipherSuite.argtypes = [TLSConfiguration, c_int]
    TLSConfiguration_addCipherSuite.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 364
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_clearCipherSuiteList", "cdecl"):
        continue
    TLSConfiguration_clearCipherSuiteList = _lib.get("TLSConfiguration_clearCipherSuiteList", "cdecl")
    TLSConfiguration_clearCipherSuiteList.argtypes = [TLSConfiguration]
    TLSConfiguration_clearCipherSuiteList.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 372
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_destroy", "cdecl"):
        continue
    TLSConfiguration_destroy = _lib.get("TLSConfiguration_destroy", "cdecl")
    TLSConfiguration_destroy.argtypes = [TLSConfiguration]
    TLSConfiguration_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 48
class struct_sTLSSocket(Structure):
    pass

TLSSocket = POINTER(struct_sTLSSocket)# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 48

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 63
for _lib in _libs.values():
    if not _lib.has("TLSSocket_create", "cdecl"):
        continue
    TLSSocket_create = _lib.get("TLSSocket_create", "cdecl")
    TLSSocket_create.argtypes = [Socket, TLSConfiguration, c_bool]
    TLSSocket_create.restype = TLSSocket
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 69
for _lib in _libs.values():
    if not _lib.has("TLSSocket_performHandshake", "cdecl"):
        continue
    TLSSocket_performHandshake = _lib.get("TLSSocket_performHandshake", "cdecl")
    TLSSocket_performHandshake.argtypes = [TLSSocket]
    TLSSocket_performHandshake.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 78
for _lib in _libs.values():
    if not _lib.has("TLSSocket_getPeerCertificate", "cdecl"):
        continue
    TLSSocket_getPeerCertificate = _lib.get("TLSSocket_getPeerCertificate", "cdecl")
    TLSSocket_getPeerCertificate.argtypes = [TLSSocket, POINTER(c_int)]
    TLSSocket_getPeerCertificate.restype = POINTER(uint8_t)
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 94
for _lib in _libs.values():
    if not _lib.has("TLSSocket_read", "cdecl"):
        continue
    TLSSocket_read = _lib.get("TLSSocket_read", "cdecl")
    TLSSocket_read.argtypes = [TLSSocket, POINTER(uint8_t), c_int]
    TLSSocket_read.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 106
for _lib in _libs.values():
    if not _lib.has("TLSSocket_write", "cdecl"):
        continue
    TLSSocket_write = _lib.get("TLSSocket_write", "cdecl")
    TLSSocket_write.argtypes = [TLSSocket, POINTER(uint8_t), c_int]
    TLSSocket_write.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 112
for _lib in _libs.values():
    if not _lib.has("TLSSocket_close", "cdecl"):
        continue
    TLSSocket_close = _lib.get("TLSSocket_close", "cdecl")
    TLSSocket_close.argtypes = [TLSSocket]
    TLSSocket_close.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 59
class struct_anon_22(Structure):
    pass

struct_anon_22.__slots__ = [
    'major',
    'minor',
    'patch',
]
struct_anon_22._fields_ = [
    ('major', c_int),
    ('minor', c_int),
    ('patch', c_int),
]

Lib60870VersionInfo = struct_anon_22# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 59

enum_anon_23 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 67

IEC60870_LINK_LAYER_BALANCED = 0# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 67

IEC60870_LINK_LAYER_UNBALANCED = 1# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 67

IEC60870_LinkLayerMode = enum_anon_23# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 67

enum_anon_24 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

LL_STATE_IDLE = 0# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

LL_STATE_ERROR = (LL_STATE_IDLE + 1)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

LL_STATE_BUSY = (LL_STATE_ERROR + 1)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

LL_STATE_AVAILABLE = (LL_STATE_BUSY + 1)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

LinkLayerState = enum_anon_24# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

IEC60870_LinkLayerStateChangedHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, LinkLayerState)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 91

IEC60870_RawMessageHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(uint8_t), c_int, c_bool)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 105

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 112
class struct_sCS101_AppLayerParameters(Structure):
    pass

CS101_AppLayerParameters = POINTER(struct_sCS101_AppLayerParameters)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 110

struct_sCS101_AppLayerParameters.__slots__ = [
    'sizeOfTypeId',
    'sizeOfVSQ',
    'sizeOfCOT',
    'originatorAddress',
    'sizeOfCA',
    'sizeOfIOA',
    'maxSizeOfASDU',
]
struct_sCS101_AppLayerParameters._fields_ = [
    ('sizeOfTypeId', c_int),
    ('sizeOfVSQ', c_int),
    ('sizeOfCOT', c_int),
    ('originatorAddress', c_int),
    ('sizeOfCA', c_int),
    ('sizeOfIOA', c_int),
    ('maxSizeOfASDU', c_int),
]

enum_anon_25 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_SP_NA_1 = 1# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_SP_TA_1 = 2# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_DP_NA_1 = 3# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_DP_TA_1 = 4# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ST_NA_1 = 5# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ST_TA_1 = 6# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_BO_NA_1 = 7# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_BO_TA_1 = 8# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_NA_1 = 9# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_TA_1 = 10# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_NB_1 = 11# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_TB_1 = 12# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_NC_1 = 13# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_TC_1 = 14# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_IT_NA_1 = 15# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_IT_TA_1 = 16# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_EP_TA_1 = 17# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_EP_TB_1 = 18# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_EP_TC_1 = 19# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_PS_NA_1 = 20# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_ND_1 = 21# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_SP_TB_1 = 30# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_DP_TB_1 = 31# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ST_TB_1 = 32# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_BO_TB_1 = 33# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_TD_1 = 34# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_TE_1 = 35# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_TF_1 = 36# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_IT_TB_1 = 37# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_EP_TD_1 = 38# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_EP_TE_1 = 39# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_EP_TF_1 = 40# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_IT_TC_1 = 41# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_SC_NA_1 = 45# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_DC_NA_1 = 46# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_RC_NA_1 = 47# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_SE_NA_1 = 48# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_SE_NB_1 = 49# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_SE_NC_1 = 50# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_BO_NA_1 = 51# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_SC_TA_1 = 58# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_DC_TA_1 = 59# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_RC_TA_1 = 60# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_SE_TA_1 = 61# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_SE_TB_1 = 62# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_SE_TC_1 = 63# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_BO_TA_1 = 64# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_EI_NA_1 = 70# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_CH_NA_1 = 81# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_RP_NA_1 = 82# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_AR_NA_1 = 83# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_KR_NA_1 = 84# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_KS_NA_1 = 85# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_KC_NA_1 = 86# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_ER_NA_1 = 87# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_US_NA_1 = 90# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_UQ_NA_1 = 91# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_UR_NA_1 = 92# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_UK_NA_1 = 93# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_UA_NA_1 = 94# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_UC_NA_1 = 95# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_IC_NA_1 = 100# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_CI_NA_1 = 101# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_RD_NA_1 = 102# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_CS_NA_1 = 103# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_TS_NA_1 = 104# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_RP_NA_1 = 105# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_CD_NA_1 = 106# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_TS_TA_1 = 107# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

P_ME_NA_1 = 110# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

P_ME_NB_1 = 111# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

P_ME_NC_1 = 112# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

P_AC_NA_1 = 113# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

F_FR_NA_1 = 120# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

F_SR_NA_1 = 121# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

F_SC_NA_1 = 122# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

F_LS_NA_1 = 123# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

F_AF_NA_1 = 124# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

F_SG_NA_1 = 125# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

F_DR_TA_1 = 126# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

F_SC_NB_1 = 127# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

IEC60870_5_TypeID = enum_anon_25# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

TypeID = IEC60870_5_TypeID# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 209

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 211
class struct_sInformationObject(Structure):
    pass

InformationObject = POINTER(struct_sInformationObject)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 211

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 216
class struct_sCS101_ASDU(Structure):
    pass

CS101_ASDU = POINTER(struct_sCS101_ASDU)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 216

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 225
class struct_anon_26(Structure):
    pass

struct_anon_26.__slots__ = [
    'parameters',
    'asdu',
    'asduHeaderLength',
    'payload',
    'payloadSize',
    'encodedData',
]
struct_anon_26._fields_ = [
    ('parameters', CS101_AppLayerParameters),
    ('asdu', POINTER(uint8_t)),
    ('asduHeaderLength', c_int),
    ('payload', POINTER(uint8_t)),
    ('payloadSize', c_int),
    ('encodedData', uint8_t * int(256)),
]

sCS101_StaticASDU = struct_anon_26# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 225

CS101_StaticASDU = POINTER(sCS101_StaticASDU)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 227

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 231
class struct_sCP16Time2a(Structure):
    pass

CP16Time2a = POINTER(struct_sCP16Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 229

struct_sCP16Time2a.__slots__ = [
    'encodedValue',
]
struct_sCP16Time2a._fields_ = [
    ('encodedValue', uint8_t * int(2)),
]

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 237
class struct_sCP24Time2a(Structure):
    pass

CP24Time2a = POINTER(struct_sCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 235

struct_sCP24Time2a.__slots__ = [
    'encodedValue',
]
struct_sCP24Time2a._fields_ = [
    ('encodedValue', uint8_t * int(3)),
]

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 246
class struct_sCP32Time2a(Structure):
    pass

CP32Time2a = POINTER(struct_sCP32Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 241

struct_sCP32Time2a.__slots__ = [
    'encodedValue',
]
struct_sCP32Time2a._fields_ = [
    ('encodedValue', uint8_t * int(4)),
]

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 255
class struct_sCP56Time2a(Structure):
    pass

CP56Time2a = POINTER(struct_sCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 253

struct_sCP56Time2a.__slots__ = [
    'encodedValue',
]
struct_sCP56Time2a._fields_ = [
    ('encodedValue', uint8_t * int(7)),
]

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 264
class struct_sBinaryCounterReading(Structure):
    pass

BinaryCounterReading = POINTER(struct_sBinaryCounterReading)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 262

struct_sBinaryCounterReading.__slots__ = [
    'encodedValue',
]
struct_sBinaryCounterReading._fields_ = [
    ('encodedValue', uint8_t * int(5)),
]

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 273
class struct_sCS104_APCIParameters(Structure):
    pass

CS104_APCIParameters = POINTER(struct_sCS104_APCIParameters)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 271

struct_sCS104_APCIParameters.__slots__ = [
    'k',
    'w',
    't0',
    't1',
    't2',
    't3',
]
struct_sCS104_APCIParameters._fields_ = [
    ('k', c_int),
    ('w', c_int),
    ('t0', c_int),
    ('t1', c_int),
    ('t2', c_int),
    ('t3', c_int),
]

enum_anon_27 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_PERIODIC = 1# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_BACKGROUND_SCAN = 2# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_SPONTANEOUS = 3# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INITIALIZED = 4# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_REQUEST = 5# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_ACTIVATION = 6# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_ACTIVATION_CON = 7# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_DEACTIVATION = 8# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_DEACTIVATION_CON = 9# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_ACTIVATION_TERMINATION = 10# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_RETURN_INFO_REMOTE = 11# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_RETURN_INFO_LOCAL = 12# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_FILE_TRANSFER = 13# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_AUTHENTICATION = 14# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_MAINTENANCE_OF_AUTH_SESSION_KEY = 15# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_MAINTENANCE_OF_USER_ROLE_AND_UPDATE_KEY = 16# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_STATION = 20# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_1 = 21# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_2 = 22# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_3 = 23# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_4 = 24# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_5 = 25# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_6 = 26# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_7 = 27# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_8 = 28# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_9 = 29# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_10 = 30# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_11 = 31# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_12 = 32# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_13 = 33# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_14 = 34# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_15 = 35# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_16 = 36# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_REQUESTED_BY_GENERAL_COUNTER = 37# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_REQUESTED_BY_GROUP_1_COUNTER = 38# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_REQUESTED_BY_GROUP_2_COUNTER = 39# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_REQUESTED_BY_GROUP_3_COUNTER = 40# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_REQUESTED_BY_GROUP_4_COUNTER = 41# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_UNKNOWN_TYPE_ID = 44# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_UNKNOWN_COT = 45# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_UNKNOWN_CA = 46# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_UNKNOWN_IOA = 47# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_CauseOfTransmission = enum_anon_27# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 329
if _libs["libiec60870.so"].has("CS101_CauseOfTransmission_toString", "cdecl"):
    CS101_CauseOfTransmission_toString = _libs["libiec60870.so"].get("CS101_CauseOfTransmission_toString", "cdecl")
    CS101_CauseOfTransmission_toString.argtypes = [CS101_CauseOfTransmission]
    CS101_CauseOfTransmission_toString.restype = c_char_p

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 333
if _libs["libiec60870.so"].has("Lib60870_enableDebugOutput", "cdecl"):
    Lib60870_enableDebugOutput = _libs["libiec60870.so"].get("Lib60870_enableDebugOutput", "cdecl")
    Lib60870_enableDebugOutput.argtypes = [c_bool]
    Lib60870_enableDebugOutput.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 336
if _libs["libiec60870.so"].has("Lib60870_getLibraryVersionInfo", "cdecl"):
    Lib60870_getLibraryVersionInfo = _libs["libiec60870.so"].get("Lib60870_getLibraryVersionInfo", "cdecl")
    Lib60870_getLibraryVersionInfo.argtypes = []
    Lib60870_getLibraryVersionInfo.restype = Lib60870VersionInfo

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 342
if _libs["libiec60870.so"].has("CS101_ASDU_isTest", "cdecl"):
    CS101_ASDU_isTest = _libs["libiec60870.so"].get("CS101_ASDU_isTest", "cdecl")
    CS101_ASDU_isTest.argtypes = [CS101_ASDU]
    CS101_ASDU_isTest.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 348
if _libs["libiec60870.so"].has("CS101_ASDU_setTest", "cdecl"):
    CS101_ASDU_setTest = _libs["libiec60870.so"].get("CS101_ASDU_setTest", "cdecl")
    CS101_ASDU_setTest.argtypes = [CS101_ASDU, c_bool]
    CS101_ASDU_setTest.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 354
if _libs["libiec60870.so"].has("CS101_ASDU_isNegative", "cdecl"):
    CS101_ASDU_isNegative = _libs["libiec60870.so"].get("CS101_ASDU_isNegative", "cdecl")
    CS101_ASDU_isNegative.argtypes = [CS101_ASDU]
    CS101_ASDU_isNegative.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 360
if _libs["libiec60870.so"].has("CS101_ASDU_setNegative", "cdecl"):
    CS101_ASDU_setNegative = _libs["libiec60870.so"].get("CS101_ASDU_setNegative", "cdecl")
    CS101_ASDU_setNegative.argtypes = [CS101_ASDU, c_bool]
    CS101_ASDU_setNegative.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 366
if _libs["libiec60870.so"].has("CS101_ASDU_getOA", "cdecl"):
    CS101_ASDU_getOA = _libs["libiec60870.so"].get("CS101_ASDU_getOA", "cdecl")
    CS101_ASDU_getOA.argtypes = [CS101_ASDU]
    CS101_ASDU_getOA.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 372
if _libs["libiec60870.so"].has("CS101_ASDU_getCOT", "cdecl"):
    CS101_ASDU_getCOT = _libs["libiec60870.so"].get("CS101_ASDU_getCOT", "cdecl")
    CS101_ASDU_getCOT.argtypes = [CS101_ASDU]
    CS101_ASDU_getCOT.restype = CS101_CauseOfTransmission

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 378
if _libs["libiec60870.so"].has("CS101_ASDU_setCOT", "cdecl"):
    CS101_ASDU_setCOT = _libs["libiec60870.so"].get("CS101_ASDU_setCOT", "cdecl")
    CS101_ASDU_setCOT.argtypes = [CS101_ASDU, CS101_CauseOfTransmission]
    CS101_ASDU_setCOT.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 384
if _libs["libiec60870.so"].has("CS101_ASDU_getCA", "cdecl"):
    CS101_ASDU_getCA = _libs["libiec60870.so"].get("CS101_ASDU_getCA", "cdecl")
    CS101_ASDU_getCA.argtypes = [CS101_ASDU]
    CS101_ASDU_getCA.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 392
if _libs["libiec60870.so"].has("CS101_ASDU_setCA", "cdecl"):
    CS101_ASDU_setCA = _libs["libiec60870.so"].get("CS101_ASDU_setCA", "cdecl")
    CS101_ASDU_setCA.argtypes = [CS101_ASDU, c_int]
    CS101_ASDU_setCA.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 401
if _libs["libiec60870.so"].has("CS101_ASDU_getTypeID", "cdecl"):
    CS101_ASDU_getTypeID = _libs["libiec60870.so"].get("CS101_ASDU_getTypeID", "cdecl")
    CS101_ASDU_getTypeID.argtypes = [CS101_ASDU]
    CS101_ASDU_getTypeID.restype = IEC60870_5_TypeID

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 413
if _libs["libiec60870.so"].has("CS101_ASDU_setTypeID", "cdecl"):
    CS101_ASDU_setTypeID = _libs["libiec60870.so"].get("CS101_ASDU_setTypeID", "cdecl")
    CS101_ASDU_setTypeID.argtypes = [CS101_ASDU, IEC60870_5_TypeID]
    CS101_ASDU_setTypeID.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 424
if _libs["libiec60870.so"].has("CS101_ASDU_isSequence", "cdecl"):
    CS101_ASDU_isSequence = _libs["libiec60870.so"].get("CS101_ASDU_isSequence", "cdecl")
    CS101_ASDU_isSequence.argtypes = [CS101_ASDU]
    CS101_ASDU_isSequence.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 435
if _libs["libiec60870.so"].has("CS101_ASDU_setSequence", "cdecl"):
    CS101_ASDU_setSequence = _libs["libiec60870.so"].get("CS101_ASDU_setSequence", "cdecl")
    CS101_ASDU_setSequence.argtypes = [CS101_ASDU, c_bool]
    CS101_ASDU_setSequence.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 443
if _libs["libiec60870.so"].has("CS101_ASDU_getNumberOfElements", "cdecl"):
    CS101_ASDU_getNumberOfElements = _libs["libiec60870.so"].get("CS101_ASDU_getNumberOfElements", "cdecl")
    CS101_ASDU_getNumberOfElements.argtypes = [CS101_ASDU]
    CS101_ASDU_getNumberOfElements.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 455
if _libs["libiec60870.so"].has("CS101_ASDU_setNumberOfElements", "cdecl"):
    CS101_ASDU_setNumberOfElements = _libs["libiec60870.so"].get("CS101_ASDU_setNumberOfElements", "cdecl")
    CS101_ASDU_setNumberOfElements.argtypes = [CS101_ASDU, c_int]
    CS101_ASDU_setNumberOfElements.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 465
if _libs["libiec60870.so"].has("CS101_ASDU_getVSQ", "cdecl"):
    CS101_ASDU_getVSQ = _libs["libiec60870.so"].get("CS101_ASDU_getVSQ", "cdecl")
    CS101_ASDU_getVSQ.argtypes = [CS101_ASDU]
    CS101_ASDU_getVSQ.restype = uint8_t

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 475
if _libs["libiec60870.so"].has("CS101_ASDU_getElement", "cdecl"):
    CS101_ASDU_getElement = _libs["libiec60870.so"].get("CS101_ASDU_getElement", "cdecl")
    CS101_ASDU_getElement.argtypes = [CS101_ASDU, c_int]
    CS101_ASDU_getElement.restype = InformationObject

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 486
if _libs["libiec60870.so"].has("CS101_ASDU_getElementEx", "cdecl"):
    CS101_ASDU_getElementEx = _libs["libiec60870.so"].get("CS101_ASDU_getElementEx", "cdecl")
    CS101_ASDU_getElementEx.argtypes = [CS101_ASDU, InformationObject, c_int]
    CS101_ASDU_getElementEx.restype = InformationObject

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 502
if _libs["libiec60870.so"].has("CS101_ASDU_create", "cdecl"):
    CS101_ASDU_create = _libs["libiec60870.so"].get("CS101_ASDU_create", "cdecl")
    CS101_ASDU_create.argtypes = [CS101_AppLayerParameters, c_bool, CS101_CauseOfTransmission, c_int, c_int, c_bool, c_bool]
    CS101_ASDU_create.restype = CS101_ASDU

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 517
if _libs["libiec60870.so"].has("CS101_ASDU_createFromBuffer", "cdecl"):
    CS101_ASDU_createFromBuffer = _libs["libiec60870.so"].get("CS101_ASDU_createFromBuffer", "cdecl")
    CS101_ASDU_createFromBuffer.argtypes = [CS101_AppLayerParameters, POINTER(uint8_t), c_int]
    CS101_ASDU_createFromBuffer.restype = CS101_ASDU

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 536
if _libs["libiec60870.so"].has("CS101_ASDU_initializeStatic", "cdecl"):
    CS101_ASDU_initializeStatic = _libs["libiec60870.so"].get("CS101_ASDU_initializeStatic", "cdecl")
    CS101_ASDU_initializeStatic.argtypes = [CS101_StaticASDU, CS101_AppLayerParameters, c_bool, CS101_CauseOfTransmission, c_int, c_int, c_bool, c_bool]
    CS101_ASDU_initializeStatic.restype = CS101_ASDU

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 548
if _libs["libiec60870.so"].has("CS101_ASDU_clone", "cdecl"):
    CS101_ASDU_clone = _libs["libiec60870.so"].get("CS101_ASDU_clone", "cdecl")
    CS101_ASDU_clone.argtypes = [CS101_ASDU, CS101_StaticASDU]
    CS101_ASDU_clone.restype = CS101_ASDU

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 557
if _libs["libiec60870.so"].has("CS101_ASDU_getPayload", "cdecl"):
    CS101_ASDU_getPayload = _libs["libiec60870.so"].get("CS101_ASDU_getPayload", "cdecl")
    CS101_ASDU_getPayload.argtypes = [CS101_ASDU]
    CS101_ASDU_getPayload.restype = POINTER(uint8_t)

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 573
if _libs["libiec60870.so"].has("CS101_ASDU_addPayload", "cdecl"):
    CS101_ASDU_addPayload = _libs["libiec60870.so"].get("CS101_ASDU_addPayload", "cdecl")
    CS101_ASDU_addPayload.argtypes = [CS101_ASDU, POINTER(uint8_t), c_int]
    CS101_ASDU_addPayload.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 583
if _libs["libiec60870.so"].has("CS101_ASDU_getPayloadSize", "cdecl"):
    CS101_ASDU_getPayloadSize = _libs["libiec60870.so"].get("CS101_ASDU_getPayloadSize", "cdecl")
    CS101_ASDU_getPayloadSize.argtypes = [CS101_ASDU]
    CS101_ASDU_getPayloadSize.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 589
if _libs["libiec60870.so"].has("CS101_ASDU_destroy", "cdecl"):
    CS101_ASDU_destroy = _libs["libiec60870.so"].get("CS101_ASDU_destroy", "cdecl")
    CS101_ASDU_destroy.argtypes = [CS101_ASDU]
    CS101_ASDU_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 602
if _libs["libiec60870.so"].has("CS101_ASDU_addInformationObject", "cdecl"):
    CS101_ASDU_addInformationObject = _libs["libiec60870.so"].get("CS101_ASDU_addInformationObject", "cdecl")
    CS101_ASDU_addInformationObject.argtypes = [CS101_ASDU, InformationObject]
    CS101_ASDU_addInformationObject.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 610
if _libs["libiec60870.so"].has("CS101_ASDU_removeAllElements", "cdecl"):
    CS101_ASDU_removeAllElements = _libs["libiec60870.so"].get("CS101_ASDU_removeAllElements", "cdecl")
    CS101_ASDU_removeAllElements.argtypes = [CS101_ASDU]
    CS101_ASDU_removeAllElements.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 616
if _libs["libiec60870.so"].has("CP16Time2a_getEplapsedTimeInMs", "cdecl"):
    CP16Time2a_getEplapsedTimeInMs = _libs["libiec60870.so"].get("CP16Time2a_getEplapsedTimeInMs", "cdecl")
    CP16Time2a_getEplapsedTimeInMs.argtypes = [CP16Time2a]
    CP16Time2a_getEplapsedTimeInMs.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 622
if _libs["libiec60870.so"].has("CP16Time2a_setEplapsedTimeInMs", "cdecl"):
    CP16Time2a_setEplapsedTimeInMs = _libs["libiec60870.so"].get("CP16Time2a_setEplapsedTimeInMs", "cdecl")
    CP16Time2a_setEplapsedTimeInMs.argtypes = [CP16Time2a, c_int]
    CP16Time2a_setEplapsedTimeInMs.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 628
if _libs["libiec60870.so"].has("CP24Time2a_getMillisecond", "cdecl"):
    CP24Time2a_getMillisecond = _libs["libiec60870.so"].get("CP24Time2a_getMillisecond", "cdecl")
    CP24Time2a_getMillisecond.argtypes = [CP24Time2a]
    CP24Time2a_getMillisecond.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 634
if _libs["libiec60870.so"].has("CP24Time2a_setMillisecond", "cdecl"):
    CP24Time2a_setMillisecond = _libs["libiec60870.so"].get("CP24Time2a_setMillisecond", "cdecl")
    CP24Time2a_setMillisecond.argtypes = [CP24Time2a, c_int]
    CP24Time2a_setMillisecond.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 640
if _libs["libiec60870.so"].has("CP24Time2a_getSecond", "cdecl"):
    CP24Time2a_getSecond = _libs["libiec60870.so"].get("CP24Time2a_getSecond", "cdecl")
    CP24Time2a_getSecond.argtypes = [CP24Time2a]
    CP24Time2a_getSecond.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 646
if _libs["libiec60870.so"].has("CP24Time2a_setSecond", "cdecl"):
    CP24Time2a_setSecond = _libs["libiec60870.so"].get("CP24Time2a_setSecond", "cdecl")
    CP24Time2a_setSecond.argtypes = [CP24Time2a, c_int]
    CP24Time2a_setSecond.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 652
if _libs["libiec60870.so"].has("CP24Time2a_getMinute", "cdecl"):
    CP24Time2a_getMinute = _libs["libiec60870.so"].get("CP24Time2a_getMinute", "cdecl")
    CP24Time2a_getMinute.argtypes = [CP24Time2a]
    CP24Time2a_getMinute.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 658
if _libs["libiec60870.so"].has("CP24Time2a_setMinute", "cdecl"):
    CP24Time2a_setMinute = _libs["libiec60870.so"].get("CP24Time2a_setMinute", "cdecl")
    CP24Time2a_setMinute.argtypes = [CP24Time2a, c_int]
    CP24Time2a_setMinute.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 664
if _libs["libiec60870.so"].has("CP24Time2a_isInvalid", "cdecl"):
    CP24Time2a_isInvalid = _libs["libiec60870.so"].get("CP24Time2a_isInvalid", "cdecl")
    CP24Time2a_isInvalid.argtypes = [CP24Time2a]
    CP24Time2a_isInvalid.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 670
if _libs["libiec60870.so"].has("CP24Time2a_setInvalid", "cdecl"):
    CP24Time2a_setInvalid = _libs["libiec60870.so"].get("CP24Time2a_setInvalid", "cdecl")
    CP24Time2a_setInvalid.argtypes = [CP24Time2a, c_bool]
    CP24Time2a_setInvalid.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 676
if _libs["libiec60870.so"].has("CP24Time2a_isSubstituted", "cdecl"):
    CP24Time2a_isSubstituted = _libs["libiec60870.so"].get("CP24Time2a_isSubstituted", "cdecl")
    CP24Time2a_isSubstituted.argtypes = [CP24Time2a]
    CP24Time2a_isSubstituted.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 682
if _libs["libiec60870.so"].has("CP24Time2a_setSubstituted", "cdecl"):
    CP24Time2a_setSubstituted = _libs["libiec60870.so"].get("CP24Time2a_setSubstituted", "cdecl")
    CP24Time2a_setSubstituted.argtypes = [CP24Time2a, c_bool]
    CP24Time2a_setSubstituted.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 688
if _libs["libiec60870.so"].has("CP56Time2a_createFromMsTimestamp", "cdecl"):
    CP56Time2a_createFromMsTimestamp = _libs["libiec60870.so"].get("CP56Time2a_createFromMsTimestamp", "cdecl")
    CP56Time2a_createFromMsTimestamp.argtypes = [CP56Time2a, uint64_t]
    CP56Time2a_createFromMsTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 692
if _libs["libiec60870.so"].has("CP32Time2a_create", "cdecl"):
    CP32Time2a_create = _libs["libiec60870.so"].get("CP32Time2a_create", "cdecl")
    CP32Time2a_create.argtypes = [CP32Time2a]
    CP32Time2a_create.restype = CP32Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 695
if _libs["libiec60870.so"].has("CP32Time2a_setFromMsTimestamp", "cdecl"):
    CP32Time2a_setFromMsTimestamp = _libs["libiec60870.so"].get("CP32Time2a_setFromMsTimestamp", "cdecl")
    CP32Time2a_setFromMsTimestamp.argtypes = [CP32Time2a, uint64_t]
    CP32Time2a_setFromMsTimestamp.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 698
if _libs["libiec60870.so"].has("CP32Time2a_getMillisecond", "cdecl"):
    CP32Time2a_getMillisecond = _libs["libiec60870.so"].get("CP32Time2a_getMillisecond", "cdecl")
    CP32Time2a_getMillisecond.argtypes = [CP32Time2a]
    CP32Time2a_getMillisecond.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 701
if _libs["libiec60870.so"].has("CP32Time2a_setMillisecond", "cdecl"):
    CP32Time2a_setMillisecond = _libs["libiec60870.so"].get("CP32Time2a_setMillisecond", "cdecl")
    CP32Time2a_setMillisecond.argtypes = [CP32Time2a, c_int]
    CP32Time2a_setMillisecond.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 704
if _libs["libiec60870.so"].has("CP32Time2a_getSecond", "cdecl"):
    CP32Time2a_getSecond = _libs["libiec60870.so"].get("CP32Time2a_getSecond", "cdecl")
    CP32Time2a_getSecond.argtypes = [CP32Time2a]
    CP32Time2a_getSecond.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 707
if _libs["libiec60870.so"].has("CP32Time2a_setSecond", "cdecl"):
    CP32Time2a_setSecond = _libs["libiec60870.so"].get("CP32Time2a_setSecond", "cdecl")
    CP32Time2a_setSecond.argtypes = [CP32Time2a, c_int]
    CP32Time2a_setSecond.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 710
if _libs["libiec60870.so"].has("CP32Time2a_getMinute", "cdecl"):
    CP32Time2a_getMinute = _libs["libiec60870.so"].get("CP32Time2a_getMinute", "cdecl")
    CP32Time2a_getMinute.argtypes = [CP32Time2a]
    CP32Time2a_getMinute.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 714
if _libs["libiec60870.so"].has("CP32Time2a_setMinute", "cdecl"):
    CP32Time2a_setMinute = _libs["libiec60870.so"].get("CP32Time2a_setMinute", "cdecl")
    CP32Time2a_setMinute.argtypes = [CP32Time2a, c_int]
    CP32Time2a_setMinute.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 717
if _libs["libiec60870.so"].has("CP32Time2a_isInvalid", "cdecl"):
    CP32Time2a_isInvalid = _libs["libiec60870.so"].get("CP32Time2a_isInvalid", "cdecl")
    CP32Time2a_isInvalid.argtypes = [CP32Time2a]
    CP32Time2a_isInvalid.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 720
if _libs["libiec60870.so"].has("CP32Time2a_setInvalid", "cdecl"):
    CP32Time2a_setInvalid = _libs["libiec60870.so"].get("CP32Time2a_setInvalid", "cdecl")
    CP32Time2a_setInvalid.argtypes = [CP32Time2a, c_bool]
    CP32Time2a_setInvalid.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 723
if _libs["libiec60870.so"].has("CP32Time2a_isSubstituted", "cdecl"):
    CP32Time2a_isSubstituted = _libs["libiec60870.so"].get("CP32Time2a_isSubstituted", "cdecl")
    CP32Time2a_isSubstituted.argtypes = [CP32Time2a]
    CP32Time2a_isSubstituted.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 726
if _libs["libiec60870.so"].has("CP32Time2a_setSubstituted", "cdecl"):
    CP32Time2a_setSubstituted = _libs["libiec60870.so"].get("CP32Time2a_setSubstituted", "cdecl")
    CP32Time2a_setSubstituted.argtypes = [CP32Time2a, c_bool]
    CP32Time2a_setSubstituted.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 729
if _libs["libiec60870.so"].has("CP32Time2a_getHour", "cdecl"):
    CP32Time2a_getHour = _libs["libiec60870.so"].get("CP32Time2a_getHour", "cdecl")
    CP32Time2a_getHour.argtypes = [CP32Time2a]
    CP32Time2a_getHour.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 732
if _libs["libiec60870.so"].has("CP32Time2a_setHour", "cdecl"):
    CP32Time2a_setHour = _libs["libiec60870.so"].get("CP32Time2a_setHour", "cdecl")
    CP32Time2a_setHour.argtypes = [CP32Time2a, c_int]
    CP32Time2a_setHour.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 735
if _libs["libiec60870.so"].has("CP32Time2a_isSummerTime", "cdecl"):
    CP32Time2a_isSummerTime = _libs["libiec60870.so"].get("CP32Time2a_isSummerTime", "cdecl")
    CP32Time2a_isSummerTime.argtypes = [CP32Time2a]
    CP32Time2a_isSummerTime.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 738
if _libs["libiec60870.so"].has("CP32Time2a_setSummerTime", "cdecl"):
    CP32Time2a_setSummerTime = _libs["libiec60870.so"].get("CP32Time2a_setSummerTime", "cdecl")
    CP32Time2a_setSummerTime.argtypes = [CP32Time2a, c_bool]
    CP32Time2a_setSummerTime.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 744
if _libs["libiec60870.so"].has("CP56Time2a_setFromMsTimestamp", "cdecl"):
    CP56Time2a_setFromMsTimestamp = _libs["libiec60870.so"].get("CP56Time2a_setFromMsTimestamp", "cdecl")
    CP56Time2a_setFromMsTimestamp.argtypes = [CP56Time2a, uint64_t]
    CP56Time2a_setFromMsTimestamp.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 750
if _libs["libiec60870.so"].has("CP56Time2a_toMsTimestamp", "cdecl"):
    CP56Time2a_toMsTimestamp = _libs["libiec60870.so"].get("CP56Time2a_toMsTimestamp", "cdecl")
    CP56Time2a_toMsTimestamp.argtypes = [CP56Time2a]
    CP56Time2a_toMsTimestamp.restype = uint64_t

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 756
if _libs["libiec60870.so"].has("CP56Time2a_getMillisecond", "cdecl"):
    CP56Time2a_getMillisecond = _libs["libiec60870.so"].get("CP56Time2a_getMillisecond", "cdecl")
    CP56Time2a_getMillisecond.argtypes = [CP56Time2a]
    CP56Time2a_getMillisecond.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 762
if _libs["libiec60870.so"].has("CP56Time2a_setMillisecond", "cdecl"):
    CP56Time2a_setMillisecond = _libs["libiec60870.so"].get("CP56Time2a_setMillisecond", "cdecl")
    CP56Time2a_setMillisecond.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setMillisecond.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 765
if _libs["libiec60870.so"].has("CP56Time2a_getSecond", "cdecl"):
    CP56Time2a_getSecond = _libs["libiec60870.so"].get("CP56Time2a_getSecond", "cdecl")
    CP56Time2a_getSecond.argtypes = [CP56Time2a]
    CP56Time2a_getSecond.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 768
if _libs["libiec60870.so"].has("CP56Time2a_setSecond", "cdecl"):
    CP56Time2a_setSecond = _libs["libiec60870.so"].get("CP56Time2a_setSecond", "cdecl")
    CP56Time2a_setSecond.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setSecond.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 771
if _libs["libiec60870.so"].has("CP56Time2a_getMinute", "cdecl"):
    CP56Time2a_getMinute = _libs["libiec60870.so"].get("CP56Time2a_getMinute", "cdecl")
    CP56Time2a_getMinute.argtypes = [CP56Time2a]
    CP56Time2a_getMinute.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 774
if _libs["libiec60870.so"].has("CP56Time2a_setMinute", "cdecl"):
    CP56Time2a_setMinute = _libs["libiec60870.so"].get("CP56Time2a_setMinute", "cdecl")
    CP56Time2a_setMinute.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setMinute.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 777
if _libs["libiec60870.so"].has("CP56Time2a_getHour", "cdecl"):
    CP56Time2a_getHour = _libs["libiec60870.so"].get("CP56Time2a_getHour", "cdecl")
    CP56Time2a_getHour.argtypes = [CP56Time2a]
    CP56Time2a_getHour.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 780
if _libs["libiec60870.so"].has("CP56Time2a_setHour", "cdecl"):
    CP56Time2a_setHour = _libs["libiec60870.so"].get("CP56Time2a_setHour", "cdecl")
    CP56Time2a_setHour.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setHour.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 783
if _libs["libiec60870.so"].has("CP56Time2a_getDayOfWeek", "cdecl"):
    CP56Time2a_getDayOfWeek = _libs["libiec60870.so"].get("CP56Time2a_getDayOfWeek", "cdecl")
    CP56Time2a_getDayOfWeek.argtypes = [CP56Time2a]
    CP56Time2a_getDayOfWeek.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 786
if _libs["libiec60870.so"].has("CP56Time2a_setDayOfWeek", "cdecl"):
    CP56Time2a_setDayOfWeek = _libs["libiec60870.so"].get("CP56Time2a_setDayOfWeek", "cdecl")
    CP56Time2a_setDayOfWeek.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setDayOfWeek.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 789
if _libs["libiec60870.so"].has("CP56Time2a_getDayOfMonth", "cdecl"):
    CP56Time2a_getDayOfMonth = _libs["libiec60870.so"].get("CP56Time2a_getDayOfMonth", "cdecl")
    CP56Time2a_getDayOfMonth.argtypes = [CP56Time2a]
    CP56Time2a_getDayOfMonth.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 792
if _libs["libiec60870.so"].has("CP56Time2a_setDayOfMonth", "cdecl"):
    CP56Time2a_setDayOfMonth = _libs["libiec60870.so"].get("CP56Time2a_setDayOfMonth", "cdecl")
    CP56Time2a_setDayOfMonth.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setDayOfMonth.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 800
if _libs["libiec60870.so"].has("CP56Time2a_getMonth", "cdecl"):
    CP56Time2a_getMonth = _libs["libiec60870.so"].get("CP56Time2a_getMonth", "cdecl")
    CP56Time2a_getMonth.argtypes = [CP56Time2a]
    CP56Time2a_getMonth.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 808
if _libs["libiec60870.so"].has("CP56Time2a_setMonth", "cdecl"):
    CP56Time2a_setMonth = _libs["libiec60870.so"].get("CP56Time2a_setMonth", "cdecl")
    CP56Time2a_setMonth.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setMonth.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 816
if _libs["libiec60870.so"].has("CP56Time2a_getYear", "cdecl"):
    CP56Time2a_getYear = _libs["libiec60870.so"].get("CP56Time2a_getYear", "cdecl")
    CP56Time2a_getYear.argtypes = [CP56Time2a]
    CP56Time2a_getYear.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 824
if _libs["libiec60870.so"].has("CP56Time2a_setYear", "cdecl"):
    CP56Time2a_setYear = _libs["libiec60870.so"].get("CP56Time2a_setYear", "cdecl")
    CP56Time2a_setYear.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setYear.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 827
if _libs["libiec60870.so"].has("CP56Time2a_isSummerTime", "cdecl"):
    CP56Time2a_isSummerTime = _libs["libiec60870.so"].get("CP56Time2a_isSummerTime", "cdecl")
    CP56Time2a_isSummerTime.argtypes = [CP56Time2a]
    CP56Time2a_isSummerTime.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 830
if _libs["libiec60870.so"].has("CP56Time2a_setSummerTime", "cdecl"):
    CP56Time2a_setSummerTime = _libs["libiec60870.so"].get("CP56Time2a_setSummerTime", "cdecl")
    CP56Time2a_setSummerTime.argtypes = [CP56Time2a, c_bool]
    CP56Time2a_setSummerTime.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 833
if _libs["libiec60870.so"].has("CP56Time2a_isInvalid", "cdecl"):
    CP56Time2a_isInvalid = _libs["libiec60870.so"].get("CP56Time2a_isInvalid", "cdecl")
    CP56Time2a_isInvalid.argtypes = [CP56Time2a]
    CP56Time2a_isInvalid.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 836
if _libs["libiec60870.so"].has("CP56Time2a_setInvalid", "cdecl"):
    CP56Time2a_setInvalid = _libs["libiec60870.so"].get("CP56Time2a_setInvalid", "cdecl")
    CP56Time2a_setInvalid.argtypes = [CP56Time2a, c_bool]
    CP56Time2a_setInvalid.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 839
if _libs["libiec60870.so"].has("CP56Time2a_isSubstituted", "cdecl"):
    CP56Time2a_isSubstituted = _libs["libiec60870.so"].get("CP56Time2a_isSubstituted", "cdecl")
    CP56Time2a_isSubstituted.argtypes = [CP56Time2a]
    CP56Time2a_isSubstituted.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 842
if _libs["libiec60870.so"].has("CP56Time2a_setSubstituted", "cdecl"):
    CP56Time2a_setSubstituted = _libs["libiec60870.so"].get("CP56Time2a_setSubstituted", "cdecl")
    CP56Time2a_setSubstituted.argtypes = [CP56Time2a, c_bool]
    CP56Time2a_setSubstituted.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 845
if _libs["libiec60870.so"].has("BinaryCounterReading_create", "cdecl"):
    BinaryCounterReading_create = _libs["libiec60870.so"].get("BinaryCounterReading_create", "cdecl")
    BinaryCounterReading_create.argtypes = [BinaryCounterReading, c_int32, c_int, c_bool, c_bool, c_bool]
    BinaryCounterReading_create.restype = BinaryCounterReading

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 849
if _libs["libiec60870.so"].has("BinaryCounterReading_destroy", "cdecl"):
    BinaryCounterReading_destroy = _libs["libiec60870.so"].get("BinaryCounterReading_destroy", "cdecl")
    BinaryCounterReading_destroy.argtypes = [BinaryCounterReading]
    BinaryCounterReading_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 852
if _libs["libiec60870.so"].has("BinaryCounterReading_getValue", "cdecl"):
    BinaryCounterReading_getValue = _libs["libiec60870.so"].get("BinaryCounterReading_getValue", "cdecl")
    BinaryCounterReading_getValue.argtypes = [BinaryCounterReading]
    BinaryCounterReading_getValue.restype = c_int32

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 855
if _libs["libiec60870.so"].has("BinaryCounterReading_setValue", "cdecl"):
    BinaryCounterReading_setValue = _libs["libiec60870.so"].get("BinaryCounterReading_setValue", "cdecl")
    BinaryCounterReading_setValue.argtypes = [BinaryCounterReading, c_int32]
    BinaryCounterReading_setValue.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 858
if _libs["libiec60870.so"].has("BinaryCounterReading_getSequenceNumber", "cdecl"):
    BinaryCounterReading_getSequenceNumber = _libs["libiec60870.so"].get("BinaryCounterReading_getSequenceNumber", "cdecl")
    BinaryCounterReading_getSequenceNumber.argtypes = [BinaryCounterReading]
    BinaryCounterReading_getSequenceNumber.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 861
if _libs["libiec60870.so"].has("BinaryCounterReading_hasCarry", "cdecl"):
    BinaryCounterReading_hasCarry = _libs["libiec60870.so"].get("BinaryCounterReading_hasCarry", "cdecl")
    BinaryCounterReading_hasCarry.argtypes = [BinaryCounterReading]
    BinaryCounterReading_hasCarry.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 864
if _libs["libiec60870.so"].has("BinaryCounterReading_isAdjusted", "cdecl"):
    BinaryCounterReading_isAdjusted = _libs["libiec60870.so"].get("BinaryCounterReading_isAdjusted", "cdecl")
    BinaryCounterReading_isAdjusted.argtypes = [BinaryCounterReading]
    BinaryCounterReading_isAdjusted.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 867
if _libs["libiec60870.so"].has("BinaryCounterReading_isInvalid", "cdecl"):
    BinaryCounterReading_isInvalid = _libs["libiec60870.so"].get("BinaryCounterReading_isInvalid", "cdecl")
    BinaryCounterReading_isInvalid.argtypes = [BinaryCounterReading]
    BinaryCounterReading_isInvalid.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 870
if _libs["libiec60870.so"].has("BinaryCounterReading_setSequenceNumber", "cdecl"):
    BinaryCounterReading_setSequenceNumber = _libs["libiec60870.so"].get("BinaryCounterReading_setSequenceNumber", "cdecl")
    BinaryCounterReading_setSequenceNumber.argtypes = [BinaryCounterReading, c_int]
    BinaryCounterReading_setSequenceNumber.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 873
if _libs["libiec60870.so"].has("BinaryCounterReading_setCarry", "cdecl"):
    BinaryCounterReading_setCarry = _libs["libiec60870.so"].get("BinaryCounterReading_setCarry", "cdecl")
    BinaryCounterReading_setCarry.argtypes = [BinaryCounterReading, c_bool]
    BinaryCounterReading_setCarry.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 876
if _libs["libiec60870.so"].has("BinaryCounterReading_setAdjusted", "cdecl"):
    BinaryCounterReading_setAdjusted = _libs["libiec60870.so"].get("BinaryCounterReading_setAdjusted", "cdecl")
    BinaryCounterReading_setAdjusted.argtypes = [BinaryCounterReading, c_bool]
    BinaryCounterReading_setAdjusted.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 879
if _libs["libiec60870.so"].has("BinaryCounterReading_setInvalid", "cdecl"):
    BinaryCounterReading_setInvalid = _libs["libiec60870.so"].get("BinaryCounterReading_setInvalid", "cdecl")
    BinaryCounterReading_setInvalid.argtypes = [BinaryCounterReading, c_bool]
    BinaryCounterReading_setInvalid.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 883
class struct_sIPeerConnection(Structure):
    pass

IPeerConnection = POINTER(struct_sIPeerConnection)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 881

struct_sIPeerConnection.__slots__ = [
    'isReady',
    'sendASDU',
    'sendASDUEx',
    'sendACT_CON',
    'sendACT_TERM',
    'close',
    'getPeerAddress',
    'getApplicationLayerParameters',
    'object',
]
struct_sIPeerConnection._fields_ = [
    ('isReady', CFUNCTYPE(UNCHECKED(c_bool), IPeerConnection)),
    ('sendASDU', CFUNCTYPE(UNCHECKED(c_bool), IPeerConnection, CS101_ASDU)),
    ('sendASDUEx', CFUNCTYPE(UNCHECKED(c_bool), IPeerConnection, CS101_ASDU, c_bool)),
    ('sendACT_CON', CFUNCTYPE(UNCHECKED(c_bool), IPeerConnection, CS101_ASDU, c_bool)),
    ('sendACT_TERM', CFUNCTYPE(UNCHECKED(c_bool), IPeerConnection, CS101_ASDU)),
    ('close', CFUNCTYPE(UNCHECKED(None), IPeerConnection)),
    ('getPeerAddress', CFUNCTYPE(UNCHECKED(c_int), IPeerConnection, String, c_int)),
    ('getApplicationLayerParameters', CFUNCTYPE(UNCHECKED(CS101_AppLayerParameters), IPeerConnection)),
    ('object', POINTER(None)),
]

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 896
if _libs["libiec60870.so"].has("IPeerConnection_isReady", "cdecl"):
    IPeerConnection_isReady = _libs["libiec60870.so"].get("IPeerConnection_isReady", "cdecl")
    IPeerConnection_isReady.argtypes = [IPeerConnection]
    IPeerConnection_isReady.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 907
if _libs["libiec60870.so"].has("IPeerConnection_sendASDU", "cdecl"):
    IPeerConnection_sendASDU = _libs["libiec60870.so"].get("IPeerConnection_sendASDU", "cdecl")
    IPeerConnection_sendASDU.argtypes = [IPeerConnection, CS101_ASDU]
    IPeerConnection_sendASDU.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 919
for _lib in _libs.values():
    if not _lib.has("IPeerConnection_sendASDUEx", "cdecl"):
        continue
    IPeerConnection_sendASDUEx = _lib.get("IPeerConnection_sendASDUEx", "cdecl")
    IPeerConnection_sendASDUEx.argtypes = [IPeerConnection, CS101_ASDU, c_bool]
    IPeerConnection_sendASDUEx.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 922
if _libs["libiec60870.so"].has("IPeerConnection_sendACT_CON", "cdecl"):
    IPeerConnection_sendACT_CON = _libs["libiec60870.so"].get("IPeerConnection_sendACT_CON", "cdecl")
    IPeerConnection_sendACT_CON.argtypes = [IPeerConnection, CS101_ASDU, c_bool]
    IPeerConnection_sendACT_CON.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 925
if _libs["libiec60870.so"].has("IPeerConnection_sendACT_TERM", "cdecl"):
    IPeerConnection_sendACT_TERM = _libs["libiec60870.so"].get("IPeerConnection_sendACT_TERM", "cdecl")
    IPeerConnection_sendACT_TERM.argtypes = [IPeerConnection, CS101_ASDU]
    IPeerConnection_sendACT_TERM.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 928
if _libs["libiec60870.so"].has("IPeerConnection_getApplicationLayerParameters", "cdecl"):
    IPeerConnection_getApplicationLayerParameters = _libs["libiec60870.so"].get("IPeerConnection_getApplicationLayerParameters", "cdecl")
    IPeerConnection_getApplicationLayerParameters.argtypes = [IPeerConnection]
    IPeerConnection_getApplicationLayerParameters.restype = CS101_AppLayerParameters

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 931
if _libs["libiec60870.so"].has("IPeerConnection_close", "cdecl"):
    IPeerConnection_close = _libs["libiec60870.so"].get("IPeerConnection_close", "cdecl")
    IPeerConnection_close.argtypes = [IPeerConnection]
    IPeerConnection_close.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 934
if _libs["libiec60870.so"].has("IPeerConnection_getPeerAddress", "cdecl"):
    IPeerConnection_getPeerAddress = _libs["libiec60870.so"].get("IPeerConnection_getPeerAddress", "cdecl")
    IPeerConnection_getPeerAddress.argtypes = [IPeerConnection, String, c_int]
    IPeerConnection_getPeerAddress.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 940
class struct_sFrame(Structure):
    pass

Frame = POINTER(struct_sFrame)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 940

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 943
if _libs["libiec60870.so"].has("Frame_destroy", "cdecl"):
    Frame_destroy = _libs["libiec60870.so"].get("Frame_destroy", "cdecl")
    Frame_destroy.argtypes = [Frame]
    Frame_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 946
if _libs["libiec60870.so"].has("Frame_resetFrame", "cdecl"):
    Frame_resetFrame = _libs["libiec60870.so"].get("Frame_resetFrame", "cdecl")
    Frame_resetFrame.argtypes = [Frame]
    Frame_resetFrame.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 949
if _libs["libiec60870.so"].has("Frame_setNextByte", "cdecl"):
    Frame_setNextByte = _libs["libiec60870.so"].get("Frame_setNextByte", "cdecl")
    Frame_setNextByte.argtypes = [Frame, uint8_t]
    Frame_setNextByte.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 952
if _libs["libiec60870.so"].has("Frame_appendBytes", "cdecl"):
    Frame_appendBytes = _libs["libiec60870.so"].get("Frame_appendBytes", "cdecl")
    Frame_appendBytes.argtypes = [Frame, POINTER(uint8_t), c_int]
    Frame_appendBytes.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 955
if _libs["libiec60870.so"].has("Frame_getMsgSize", "cdecl"):
    Frame_getMsgSize = _libs["libiec60870.so"].get("Frame_getMsgSize", "cdecl")
    Frame_getMsgSize.argtypes = [Frame]
    Frame_getMsgSize.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 957
if _libs["libiec60870.so"].has("Frame_getBuffer", "cdecl"):
    Frame_getBuffer = _libs["libiec60870.so"].get("Frame_getBuffer", "cdecl")
    Frame_getBuffer.argtypes = [Frame]
    Frame_getBuffer.restype = POINTER(uint8_t)

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 961
if _libs["libiec60870.so"].has("Frame_getSpaceLeft", "cdecl"):
    Frame_getSpaceLeft = _libs["libiec60870.so"].get("Frame_getSpaceLeft", "cdecl")
    Frame_getSpaceLeft.argtypes = [Frame]
    Frame_getSpaceLeft.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 43
if _libs["libiec60870.so"].has("TypeID_toString", "cdecl"):
    TypeID_toString = _libs["libiec60870.so"].get("TypeID_toString", "cdecl")
    TypeID_toString.argtypes = [TypeID]
    TypeID_toString.restype = c_char_p

QualityDescriptor = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 46

QualityDescriptorP = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 51

StartEvent = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 65

OutputCircuitInfo = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 80

QualifierOfParameterMV = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 99

CauseOfInitialization = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 111

QualifierOfCommand = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 120

SelectAndCallQualifier = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 131

QualifierOfInterrogation = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 146

QualifierOfCIC = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 185

QualifierOfRPC = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 201

QualifierOfParameterActivation = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 211

SetpointCommandQualifier = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 219

enum_anon_28 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 226

IEC60870_DOUBLE_POINT_INTERMEDIATE = 0# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 226

IEC60870_DOUBLE_POINT_OFF = 1# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 226

IEC60870_DOUBLE_POINT_ON = 2# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 226

IEC60870_DOUBLE_POINT_INDETERMINATE = 3# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 226

DoublePointValue = enum_anon_28# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 226

enum_anon_29 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 233

IEC60870_EVENTSTATE_INDETERMINATE_0 = 0# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 233

IEC60870_EVENTSTATE_OFF = 1# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 233

IEC60870_EVENTSTATE_ON = 2# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 233

IEC60870_EVENTSTATE_INDETERMINATE_3 = 3# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 233

EventState = enum_anon_29# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 233

enum_anon_30 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 243

IEC60870_STEP_INVALID_0 = 0# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 243

IEC60870_STEP_LOWER = 1# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 243

IEC60870_STEP_HIGHER = 2# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 243

IEC60870_STEP_INVALID_3 = 3# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 243

StepCommandValue = enum_anon_30# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 243

tSingleEvent = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 245

SingleEvent = POINTER(tSingleEvent)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 247

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 250
if _libs["libiec60870.so"].has("SingleEvent_setEventState", "cdecl"):
    SingleEvent_setEventState = _libs["libiec60870.so"].get("SingleEvent_setEventState", "cdecl")
    SingleEvent_setEventState.argtypes = [SingleEvent, EventState]
    SingleEvent_setEventState.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 253
if _libs["libiec60870.so"].has("SingleEvent_getEventState", "cdecl"):
    SingleEvent_getEventState = _libs["libiec60870.so"].get("SingleEvent_getEventState", "cdecl")
    SingleEvent_getEventState.argtypes = [SingleEvent]
    SingleEvent_getEventState.restype = EventState

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 256
if _libs["libiec60870.so"].has("SingleEvent_setQDP", "cdecl"):
    SingleEvent_setQDP = _libs["libiec60870.so"].get("SingleEvent_setQDP", "cdecl")
    SingleEvent_setQDP.argtypes = [SingleEvent, QualityDescriptorP]
    SingleEvent_setQDP.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 259
if _libs["libiec60870.so"].has("SingleEvent_getQDP", "cdecl"):
    SingleEvent_getQDP = _libs["libiec60870.so"].get("SingleEvent_getQDP", "cdecl")
    SingleEvent_getQDP.argtypes = [SingleEvent]
    SingleEvent_getQDP.restype = QualityDescriptorP

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 266
class struct_sStatusAndStatusChangeDetection(Structure):
    pass

tStatusAndStatusChangeDetection = struct_sStatusAndStatusChangeDetection# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 262

StatusAndStatusChangeDetection = POINTER(tStatusAndStatusChangeDetection)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 264

struct_sStatusAndStatusChangeDetection.__slots__ = [
    'encodedValue',
]
struct_sStatusAndStatusChangeDetection._fields_ = [
    ('encodedValue', uint8_t * int(4)),
]

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 271
if _libs["libiec60870.so"].has("StatusAndStatusChangeDetection_getSTn", "cdecl"):
    StatusAndStatusChangeDetection_getSTn = _libs["libiec60870.so"].get("StatusAndStatusChangeDetection_getSTn", "cdecl")
    StatusAndStatusChangeDetection_getSTn.argtypes = [StatusAndStatusChangeDetection]
    StatusAndStatusChangeDetection_getSTn.restype = uint16_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 274
if _libs["libiec60870.so"].has("StatusAndStatusChangeDetection_getCDn", "cdecl"):
    StatusAndStatusChangeDetection_getCDn = _libs["libiec60870.so"].get("StatusAndStatusChangeDetection_getCDn", "cdecl")
    StatusAndStatusChangeDetection_getCDn.argtypes = [StatusAndStatusChangeDetection]
    StatusAndStatusChangeDetection_getCDn.restype = uint16_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 277
if _libs["libiec60870.so"].has("StatusAndStatusChangeDetection_setSTn", "cdecl"):
    StatusAndStatusChangeDetection_setSTn = _libs["libiec60870.so"].get("StatusAndStatusChangeDetection_setSTn", "cdecl")
    StatusAndStatusChangeDetection_setSTn.argtypes = [StatusAndStatusChangeDetection, uint16_t]
    StatusAndStatusChangeDetection_setSTn.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 280
if _libs["libiec60870.so"].has("StatusAndStatusChangeDetection_getST", "cdecl"):
    StatusAndStatusChangeDetection_getST = _libs["libiec60870.so"].get("StatusAndStatusChangeDetection_getST", "cdecl")
    StatusAndStatusChangeDetection_getST.argtypes = [StatusAndStatusChangeDetection, c_int]
    StatusAndStatusChangeDetection_getST.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 283
if _libs["libiec60870.so"].has("StatusAndStatusChangeDetection_getCD", "cdecl"):
    StatusAndStatusChangeDetection_getCD = _libs["libiec60870.so"].get("StatusAndStatusChangeDetection_getCD", "cdecl")
    StatusAndStatusChangeDetection_getCD.argtypes = [StatusAndStatusChangeDetection, c_int]
    StatusAndStatusChangeDetection_getCD.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 286
if _libs["libiec60870.so"].has("NormalizedValue_fromScaled", "cdecl"):
    NormalizedValue_fromScaled = _libs["libiec60870.so"].get("NormalizedValue_fromScaled", "cdecl")
    NormalizedValue_fromScaled.argtypes = [c_int]
    NormalizedValue_fromScaled.restype = c_float

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 289
if _libs["libiec60870.so"].has("NormalizedValue_toScaled", "cdecl"):
    NormalizedValue_toScaled = _libs["libiec60870.so"].get("NormalizedValue_toScaled", "cdecl")
    NormalizedValue_toScaled.argtypes = [c_float]
    NormalizedValue_toScaled.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 301
if _libs["libiec60870.so"].has("InformationObject_getMaxSizeInMemory", "cdecl"):
    InformationObject_getMaxSizeInMemory = _libs["libiec60870.so"].get("InformationObject_getMaxSizeInMemory", "cdecl")
    InformationObject_getMaxSizeInMemory.argtypes = []
    InformationObject_getMaxSizeInMemory.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 304
if _libs["libiec60870.so"].has("InformationObject_getObjectAddress", "cdecl"):
    InformationObject_getObjectAddress = _libs["libiec60870.so"].get("InformationObject_getObjectAddress", "cdecl")
    InformationObject_getObjectAddress.argtypes = [InformationObject]
    InformationObject_getObjectAddress.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 307
if _libs["libiec60870.so"].has("InformationObject_getType", "cdecl"):
    InformationObject_getType = _libs["libiec60870.so"].get("InformationObject_getType", "cdecl")
    InformationObject_getType.argtypes = [InformationObject]
    InformationObject_getType.restype = TypeID

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 317
if _libs["libiec60870.so"].has("InformationObject_destroy", "cdecl"):
    InformationObject_destroy = _libs["libiec60870.so"].get("InformationObject_destroy", "cdecl")
    InformationObject_destroy.argtypes = [InformationObject]
    InformationObject_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 323
class struct_sSinglePointInformation(Structure):
    pass

SinglePointInformation = POINTER(struct_sSinglePointInformation)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 323

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 326
if _libs["libiec60870.so"].has("SinglePointInformation_create", "cdecl"):
    SinglePointInformation_create = _libs["libiec60870.so"].get("SinglePointInformation_create", "cdecl")
    SinglePointInformation_create.argtypes = [SinglePointInformation, c_int, c_bool, QualityDescriptor]
    SinglePointInformation_create.restype = SinglePointInformation

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 330
if _libs["libiec60870.so"].has("SinglePointInformation_getValue", "cdecl"):
    SinglePointInformation_getValue = _libs["libiec60870.so"].get("SinglePointInformation_getValue", "cdecl")
    SinglePointInformation_getValue.argtypes = [SinglePointInformation]
    SinglePointInformation_getValue.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 333
if _libs["libiec60870.so"].has("SinglePointInformation_getQuality", "cdecl"):
    SinglePointInformation_getQuality = _libs["libiec60870.so"].get("SinglePointInformation_getQuality", "cdecl")
    SinglePointInformation_getQuality.argtypes = [SinglePointInformation]
    SinglePointInformation_getQuality.restype = QualityDescriptor

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 336
if _libs["libiec60870.so"].has("SinglePointInformation_destroy", "cdecl"):
    SinglePointInformation_destroy = _libs["libiec60870.so"].get("SinglePointInformation_destroy", "cdecl")
    SinglePointInformation_destroy.argtypes = [SinglePointInformation]
    SinglePointInformation_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 342
class struct_sSinglePointWithCP24Time2a(Structure):
    pass

SinglePointWithCP24Time2a = POINTER(struct_sSinglePointWithCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 342

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 345
if _libs["libiec60870.so"].has("SinglePointWithCP24Time2a_create", "cdecl"):
    SinglePointWithCP24Time2a_create = _libs["libiec60870.so"].get("SinglePointWithCP24Time2a_create", "cdecl")
    SinglePointWithCP24Time2a_create.argtypes = [SinglePointWithCP24Time2a, c_int, c_bool, QualityDescriptor, CP24Time2a]
    SinglePointWithCP24Time2a_create.restype = SinglePointWithCP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 349
if _libs["libiec60870.so"].has("SinglePointWithCP24Time2a_destroy", "cdecl"):
    SinglePointWithCP24Time2a_destroy = _libs["libiec60870.so"].get("SinglePointWithCP24Time2a_destroy", "cdecl")
    SinglePointWithCP24Time2a_destroy.argtypes = [SinglePointWithCP24Time2a]
    SinglePointWithCP24Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 352
if _libs["libiec60870.so"].has("SinglePointWithCP24Time2a_getTimestamp", "cdecl"):
    SinglePointWithCP24Time2a_getTimestamp = _libs["libiec60870.so"].get("SinglePointWithCP24Time2a_getTimestamp", "cdecl")
    SinglePointWithCP24Time2a_getTimestamp.argtypes = [SinglePointWithCP24Time2a]
    SinglePointWithCP24Time2a_getTimestamp.restype = CP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 358
class struct_sSinglePointWithCP56Time2a(Structure):
    pass

SinglePointWithCP56Time2a = POINTER(struct_sSinglePointWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 358

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 361
if _libs["libiec60870.so"].has("SinglePointWithCP56Time2a_create", "cdecl"):
    SinglePointWithCP56Time2a_create = _libs["libiec60870.so"].get("SinglePointWithCP56Time2a_create", "cdecl")
    SinglePointWithCP56Time2a_create.argtypes = [SinglePointWithCP56Time2a, c_int, c_bool, QualityDescriptor, CP56Time2a]
    SinglePointWithCP56Time2a_create.restype = SinglePointWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 365
if _libs["libiec60870.so"].has("SinglePointWithCP56Time2a_destroy", "cdecl"):
    SinglePointWithCP56Time2a_destroy = _libs["libiec60870.so"].get("SinglePointWithCP56Time2a_destroy", "cdecl")
    SinglePointWithCP56Time2a_destroy.argtypes = [SinglePointWithCP56Time2a]
    SinglePointWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 368
if _libs["libiec60870.so"].has("SinglePointWithCP56Time2a_getTimestamp", "cdecl"):
    SinglePointWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("SinglePointWithCP56Time2a_getTimestamp", "cdecl")
    SinglePointWithCP56Time2a_getTimestamp.argtypes = [SinglePointWithCP56Time2a]
    SinglePointWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 375
class struct_sDoublePointInformation(Structure):
    pass

DoublePointInformation = POINTER(struct_sDoublePointInformation)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 375

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 378
if _libs["libiec60870.so"].has("DoublePointInformation_destroy", "cdecl"):
    DoublePointInformation_destroy = _libs["libiec60870.so"].get("DoublePointInformation_destroy", "cdecl")
    DoublePointInformation_destroy.argtypes = [DoublePointInformation]
    DoublePointInformation_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 381
if _libs["libiec60870.so"].has("DoublePointInformation_create", "cdecl"):
    DoublePointInformation_create = _libs["libiec60870.so"].get("DoublePointInformation_create", "cdecl")
    DoublePointInformation_create.argtypes = [DoublePointInformation, c_int, DoublePointValue, QualityDescriptor]
    DoublePointInformation_create.restype = DoublePointInformation

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 385
if _libs["libiec60870.so"].has("DoublePointInformation_getValue", "cdecl"):
    DoublePointInformation_getValue = _libs["libiec60870.so"].get("DoublePointInformation_getValue", "cdecl")
    DoublePointInformation_getValue.argtypes = [DoublePointInformation]
    DoublePointInformation_getValue.restype = DoublePointValue

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 388
if _libs["libiec60870.so"].has("DoublePointInformation_getQuality", "cdecl"):
    DoublePointInformation_getQuality = _libs["libiec60870.so"].get("DoublePointInformation_getQuality", "cdecl")
    DoublePointInformation_getQuality.argtypes = [DoublePointInformation]
    DoublePointInformation_getQuality.restype = QualityDescriptor

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 394
class struct_sDoublePointWithCP24Time2a(Structure):
    pass

DoublePointWithCP24Time2a = POINTER(struct_sDoublePointWithCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 394

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 397
if _libs["libiec60870.so"].has("DoublePointWithCP24Time2a_destroy", "cdecl"):
    DoublePointWithCP24Time2a_destroy = _libs["libiec60870.so"].get("DoublePointWithCP24Time2a_destroy", "cdecl")
    DoublePointWithCP24Time2a_destroy.argtypes = [DoublePointWithCP24Time2a]
    DoublePointWithCP24Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 400
if _libs["libiec60870.so"].has("DoublePointWithCP24Time2a_create", "cdecl"):
    DoublePointWithCP24Time2a_create = _libs["libiec60870.so"].get("DoublePointWithCP24Time2a_create", "cdecl")
    DoublePointWithCP24Time2a_create.argtypes = [DoublePointWithCP24Time2a, c_int, DoublePointValue, QualityDescriptor, CP24Time2a]
    DoublePointWithCP24Time2a_create.restype = DoublePointWithCP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 404
if _libs["libiec60870.so"].has("DoublePointWithCP24Time2a_getTimestamp", "cdecl"):
    DoublePointWithCP24Time2a_getTimestamp = _libs["libiec60870.so"].get("DoublePointWithCP24Time2a_getTimestamp", "cdecl")
    DoublePointWithCP24Time2a_getTimestamp.argtypes = [DoublePointWithCP24Time2a]
    DoublePointWithCP24Time2a_getTimestamp.restype = CP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 410
class struct_sDoublePointWithCP56Time2a(Structure):
    pass

DoublePointWithCP56Time2a = POINTER(struct_sDoublePointWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 410

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 413
if _libs["libiec60870.so"].has("DoublePointWithCP56Time2a_create", "cdecl"):
    DoublePointWithCP56Time2a_create = _libs["libiec60870.so"].get("DoublePointWithCP56Time2a_create", "cdecl")
    DoublePointWithCP56Time2a_create.argtypes = [DoublePointWithCP56Time2a, c_int, DoublePointValue, QualityDescriptor, CP56Time2a]
    DoublePointWithCP56Time2a_create.restype = DoublePointWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 417
if _libs["libiec60870.so"].has("DoublePointWithCP56Time2a_destroy", "cdecl"):
    DoublePointWithCP56Time2a_destroy = _libs["libiec60870.so"].get("DoublePointWithCP56Time2a_destroy", "cdecl")
    DoublePointWithCP56Time2a_destroy.argtypes = [DoublePointWithCP56Time2a]
    DoublePointWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 420
if _libs["libiec60870.so"].has("DoublePointWithCP56Time2a_getTimestamp", "cdecl"):
    DoublePointWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("DoublePointWithCP56Time2a_getTimestamp", "cdecl")
    DoublePointWithCP56Time2a_getTimestamp.argtypes = [DoublePointWithCP56Time2a]
    DoublePointWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 426
class struct_sStepPositionInformation(Structure):
    pass

StepPositionInformation = POINTER(struct_sStepPositionInformation)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 426

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 440
if _libs["libiec60870.so"].has("StepPositionInformation_create", "cdecl"):
    StepPositionInformation_create = _libs["libiec60870.so"].get("StepPositionInformation_create", "cdecl")
    StepPositionInformation_create.argtypes = [StepPositionInformation, c_int, c_int, c_bool, QualityDescriptor]
    StepPositionInformation_create.restype = StepPositionInformation

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 444
if _libs["libiec60870.so"].has("StepPositionInformation_destroy", "cdecl"):
    StepPositionInformation_destroy = _libs["libiec60870.so"].get("StepPositionInformation_destroy", "cdecl")
    StepPositionInformation_destroy.argtypes = [StepPositionInformation]
    StepPositionInformation_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 447
if _libs["libiec60870.so"].has("StepPositionInformation_getObjectAddress", "cdecl"):
    StepPositionInformation_getObjectAddress = _libs["libiec60870.so"].get("StepPositionInformation_getObjectAddress", "cdecl")
    StepPositionInformation_getObjectAddress.argtypes = [StepPositionInformation]
    StepPositionInformation_getObjectAddress.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 453
if _libs["libiec60870.so"].has("StepPositionInformation_getValue", "cdecl"):
    StepPositionInformation_getValue = _libs["libiec60870.so"].get("StepPositionInformation_getValue", "cdecl")
    StepPositionInformation_getValue.argtypes = [StepPositionInformation]
    StepPositionInformation_getValue.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 456
if _libs["libiec60870.so"].has("StepPositionInformation_isTransient", "cdecl"):
    StepPositionInformation_isTransient = _libs["libiec60870.so"].get("StepPositionInformation_isTransient", "cdecl")
    StepPositionInformation_isTransient.argtypes = [StepPositionInformation]
    StepPositionInformation_isTransient.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 459
if _libs["libiec60870.so"].has("StepPositionInformation_getQuality", "cdecl"):
    StepPositionInformation_getQuality = _libs["libiec60870.so"].get("StepPositionInformation_getQuality", "cdecl")
    StepPositionInformation_getQuality.argtypes = [StepPositionInformation]
    StepPositionInformation_getQuality.restype = QualityDescriptor

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 465
class struct_sStepPositionWithCP24Time2a(Structure):
    pass

StepPositionWithCP24Time2a = POINTER(struct_sStepPositionWithCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 465

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 468
if _libs["libiec60870.so"].has("StepPositionWithCP24Time2a_destroy", "cdecl"):
    StepPositionWithCP24Time2a_destroy = _libs["libiec60870.so"].get("StepPositionWithCP24Time2a_destroy", "cdecl")
    StepPositionWithCP24Time2a_destroy.argtypes = [StepPositionWithCP24Time2a]
    StepPositionWithCP24Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 471
if _libs["libiec60870.so"].has("StepPositionWithCP24Time2a_create", "cdecl"):
    StepPositionWithCP24Time2a_create = _libs["libiec60870.so"].get("StepPositionWithCP24Time2a_create", "cdecl")
    StepPositionWithCP24Time2a_create.argtypes = [StepPositionWithCP24Time2a, c_int, c_int, c_bool, QualityDescriptor, CP24Time2a]
    StepPositionWithCP24Time2a_create.restype = StepPositionWithCP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 475
if _libs["libiec60870.so"].has("StepPositionWithCP24Time2a_getTimestamp", "cdecl"):
    StepPositionWithCP24Time2a_getTimestamp = _libs["libiec60870.so"].get("StepPositionWithCP24Time2a_getTimestamp", "cdecl")
    StepPositionWithCP24Time2a_getTimestamp.argtypes = [StepPositionWithCP24Time2a]
    StepPositionWithCP24Time2a_getTimestamp.restype = CP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 482
class struct_sStepPositionWithCP56Time2a(Structure):
    pass

StepPositionWithCP56Time2a = POINTER(struct_sStepPositionWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 482

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 485
if _libs["libiec60870.so"].has("StepPositionWithCP56Time2a_destroy", "cdecl"):
    StepPositionWithCP56Time2a_destroy = _libs["libiec60870.so"].get("StepPositionWithCP56Time2a_destroy", "cdecl")
    StepPositionWithCP56Time2a_destroy.argtypes = [StepPositionWithCP56Time2a]
    StepPositionWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 488
if _libs["libiec60870.so"].has("StepPositionWithCP56Time2a_create", "cdecl"):
    StepPositionWithCP56Time2a_create = _libs["libiec60870.so"].get("StepPositionWithCP56Time2a_create", "cdecl")
    StepPositionWithCP56Time2a_create.argtypes = [StepPositionWithCP56Time2a, c_int, c_int, c_bool, QualityDescriptor, CP56Time2a]
    StepPositionWithCP56Time2a_create.restype = StepPositionWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 492
if _libs["libiec60870.so"].has("StepPositionWithCP56Time2a_getTimestamp", "cdecl"):
    StepPositionWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("StepPositionWithCP56Time2a_getTimestamp", "cdecl")
    StepPositionWithCP56Time2a_getTimestamp.argtypes = [StepPositionWithCP56Time2a]
    StepPositionWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 498
class struct_sBitString32(Structure):
    pass

BitString32 = POINTER(struct_sBitString32)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 498

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 501
if _libs["libiec60870.so"].has("BitString32_destroy", "cdecl"):
    BitString32_destroy = _libs["libiec60870.so"].get("BitString32_destroy", "cdecl")
    BitString32_destroy.argtypes = [BitString32]
    BitString32_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 504
if _libs["libiec60870.so"].has("BitString32_create", "cdecl"):
    BitString32_create = _libs["libiec60870.so"].get("BitString32_create", "cdecl")
    BitString32_create.argtypes = [BitString32, c_int, uint32_t]
    BitString32_create.restype = BitString32

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 507
if _libs["libiec60870.so"].has("BitString32_createEx", "cdecl"):
    BitString32_createEx = _libs["libiec60870.so"].get("BitString32_createEx", "cdecl")
    BitString32_createEx.argtypes = [BitString32, c_int, uint32_t, QualityDescriptor]
    BitString32_createEx.restype = BitString32

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 510
if _libs["libiec60870.so"].has("BitString32_getValue", "cdecl"):
    BitString32_getValue = _libs["libiec60870.so"].get("BitString32_getValue", "cdecl")
    BitString32_getValue.argtypes = [BitString32]
    BitString32_getValue.restype = uint32_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 513
if _libs["libiec60870.so"].has("BitString32_getQuality", "cdecl"):
    BitString32_getQuality = _libs["libiec60870.so"].get("BitString32_getQuality", "cdecl")
    BitString32_getQuality.argtypes = [BitString32]
    BitString32_getQuality.restype = QualityDescriptor

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 519
class struct_sBitstring32WithCP24Time2a(Structure):
    pass

Bitstring32WithCP24Time2a = POINTER(struct_sBitstring32WithCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 519

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 522
if _libs["libiec60870.so"].has("Bitstring32WithCP24Time2a_destroy", "cdecl"):
    Bitstring32WithCP24Time2a_destroy = _libs["libiec60870.so"].get("Bitstring32WithCP24Time2a_destroy", "cdecl")
    Bitstring32WithCP24Time2a_destroy.argtypes = [Bitstring32WithCP24Time2a]
    Bitstring32WithCP24Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 525
if _libs["libiec60870.so"].has("Bitstring32WithCP24Time2a_create", "cdecl"):
    Bitstring32WithCP24Time2a_create = _libs["libiec60870.so"].get("Bitstring32WithCP24Time2a_create", "cdecl")
    Bitstring32WithCP24Time2a_create.argtypes = [Bitstring32WithCP24Time2a, c_int, uint32_t, CP24Time2a]
    Bitstring32WithCP24Time2a_create.restype = Bitstring32WithCP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 528
if _libs["libiec60870.so"].has("Bitstring32WithCP24Time2a_createEx", "cdecl"):
    Bitstring32WithCP24Time2a_createEx = _libs["libiec60870.so"].get("Bitstring32WithCP24Time2a_createEx", "cdecl")
    Bitstring32WithCP24Time2a_createEx.argtypes = [Bitstring32WithCP24Time2a, c_int, uint32_t, QualityDescriptor, CP24Time2a]
    Bitstring32WithCP24Time2a_createEx.restype = Bitstring32WithCP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 531
if _libs["libiec60870.so"].has("Bitstring32WithCP24Time2a_getTimestamp", "cdecl"):
    Bitstring32WithCP24Time2a_getTimestamp = _libs["libiec60870.so"].get("Bitstring32WithCP24Time2a_getTimestamp", "cdecl")
    Bitstring32WithCP24Time2a_getTimestamp.argtypes = [Bitstring32WithCP24Time2a]
    Bitstring32WithCP24Time2a_getTimestamp.restype = CP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 537
class struct_sBitstring32WithCP56Time2a(Structure):
    pass

Bitstring32WithCP56Time2a = POINTER(struct_sBitstring32WithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 537

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 540
if _libs["libiec60870.so"].has("Bitstring32WithCP56Time2a_destroy", "cdecl"):
    Bitstring32WithCP56Time2a_destroy = _libs["libiec60870.so"].get("Bitstring32WithCP56Time2a_destroy", "cdecl")
    Bitstring32WithCP56Time2a_destroy.argtypes = [Bitstring32WithCP56Time2a]
    Bitstring32WithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 543
if _libs["libiec60870.so"].has("Bitstring32WithCP56Time2a_create", "cdecl"):
    Bitstring32WithCP56Time2a_create = _libs["libiec60870.so"].get("Bitstring32WithCP56Time2a_create", "cdecl")
    Bitstring32WithCP56Time2a_create.argtypes = [Bitstring32WithCP56Time2a, c_int, uint32_t, CP56Time2a]
    Bitstring32WithCP56Time2a_create.restype = Bitstring32WithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 546
if _libs["libiec60870.so"].has("Bitstring32WithCP56Time2a_createEx", "cdecl"):
    Bitstring32WithCP56Time2a_createEx = _libs["libiec60870.so"].get("Bitstring32WithCP56Time2a_createEx", "cdecl")
    Bitstring32WithCP56Time2a_createEx.argtypes = [Bitstring32WithCP56Time2a, c_int, uint32_t, QualityDescriptor, CP56Time2a]
    Bitstring32WithCP56Time2a_createEx.restype = Bitstring32WithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 549
if _libs["libiec60870.so"].has("Bitstring32WithCP56Time2a_getTimestamp", "cdecl"):
    Bitstring32WithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("Bitstring32WithCP56Time2a_getTimestamp", "cdecl")
    Bitstring32WithCP56Time2a_getTimestamp.argtypes = [Bitstring32WithCP56Time2a]
    Bitstring32WithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 555
class struct_sMeasuredValueNormalizedWithoutQuality(Structure):
    pass

MeasuredValueNormalizedWithoutQuality = POINTER(struct_sMeasuredValueNormalizedWithoutQuality)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 555

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 558
if _libs["libiec60870.so"].has("MeasuredValueNormalizedWithoutQuality_destroy", "cdecl"):
    MeasuredValueNormalizedWithoutQuality_destroy = _libs["libiec60870.so"].get("MeasuredValueNormalizedWithoutQuality_destroy", "cdecl")
    MeasuredValueNormalizedWithoutQuality_destroy.argtypes = [MeasuredValueNormalizedWithoutQuality]
    MeasuredValueNormalizedWithoutQuality_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 561
if _libs["libiec60870.so"].has("MeasuredValueNormalizedWithoutQuality_create", "cdecl"):
    MeasuredValueNormalizedWithoutQuality_create = _libs["libiec60870.so"].get("MeasuredValueNormalizedWithoutQuality_create", "cdecl")
    MeasuredValueNormalizedWithoutQuality_create.argtypes = [MeasuredValueNormalizedWithoutQuality, c_int, c_float]
    MeasuredValueNormalizedWithoutQuality_create.restype = MeasuredValueNormalizedWithoutQuality

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 564
if _libs["libiec60870.so"].has("MeasuredValueNormalizedWithoutQuality_getValue", "cdecl"):
    MeasuredValueNormalizedWithoutQuality_getValue = _libs["libiec60870.so"].get("MeasuredValueNormalizedWithoutQuality_getValue", "cdecl")
    MeasuredValueNormalizedWithoutQuality_getValue.argtypes = [MeasuredValueNormalizedWithoutQuality]
    MeasuredValueNormalizedWithoutQuality_getValue.restype = c_float

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 567
if _libs["libiec60870.so"].has("MeasuredValueNormalizedWithoutQuality_setValue", "cdecl"):
    MeasuredValueNormalizedWithoutQuality_setValue = _libs["libiec60870.so"].get("MeasuredValueNormalizedWithoutQuality_setValue", "cdecl")
    MeasuredValueNormalizedWithoutQuality_setValue.argtypes = [MeasuredValueNormalizedWithoutQuality, c_float]
    MeasuredValueNormalizedWithoutQuality_setValue.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 573
class struct_sMeasuredValueNormalized(Structure):
    pass

MeasuredValueNormalized = POINTER(struct_sMeasuredValueNormalized)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 573

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 576
if _libs["libiec60870.so"].has("MeasuredValueNormalized_destroy", "cdecl"):
    MeasuredValueNormalized_destroy = _libs["libiec60870.so"].get("MeasuredValueNormalized_destroy", "cdecl")
    MeasuredValueNormalized_destroy.argtypes = [MeasuredValueNormalized]
    MeasuredValueNormalized_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 579
if _libs["libiec60870.so"].has("MeasuredValueNormalized_create", "cdecl"):
    MeasuredValueNormalized_create = _libs["libiec60870.so"].get("MeasuredValueNormalized_create", "cdecl")
    MeasuredValueNormalized_create.argtypes = [MeasuredValueNormalized, c_int, c_float, QualityDescriptor]
    MeasuredValueNormalized_create.restype = MeasuredValueNormalized

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 582
if _libs["libiec60870.so"].has("MeasuredValueNormalized_getValue", "cdecl"):
    MeasuredValueNormalized_getValue = _libs["libiec60870.so"].get("MeasuredValueNormalized_getValue", "cdecl")
    MeasuredValueNormalized_getValue.argtypes = [MeasuredValueNormalized]
    MeasuredValueNormalized_getValue.restype = c_float

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 585
if _libs["libiec60870.so"].has("MeasuredValueNormalized_setValue", "cdecl"):
    MeasuredValueNormalized_setValue = _libs["libiec60870.so"].get("MeasuredValueNormalized_setValue", "cdecl")
    MeasuredValueNormalized_setValue.argtypes = [MeasuredValueNormalized, c_float]
    MeasuredValueNormalized_setValue.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 588
if _libs["libiec60870.so"].has("MeasuredValueNormalized_getQuality", "cdecl"):
    MeasuredValueNormalized_getQuality = _libs["libiec60870.so"].get("MeasuredValueNormalized_getQuality", "cdecl")
    MeasuredValueNormalized_getQuality.argtypes = [MeasuredValueNormalized]
    MeasuredValueNormalized_getQuality.restype = QualityDescriptor

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 594
class struct_sMeasuredValueNormalizedWithCP24Time2a(Structure):
    pass

MeasuredValueNormalizedWithCP24Time2a = POINTER(struct_sMeasuredValueNormalizedWithCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 594

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 597
if _libs["libiec60870.so"].has("MeasuredValueNormalizedWithCP24Time2a_destroy", "cdecl"):
    MeasuredValueNormalizedWithCP24Time2a_destroy = _libs["libiec60870.so"].get("MeasuredValueNormalizedWithCP24Time2a_destroy", "cdecl")
    MeasuredValueNormalizedWithCP24Time2a_destroy.argtypes = [MeasuredValueNormalizedWithCP24Time2a]
    MeasuredValueNormalizedWithCP24Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 600
if _libs["libiec60870.so"].has("MeasuredValueNormalizedWithCP24Time2a_create", "cdecl"):
    MeasuredValueNormalizedWithCP24Time2a_create = _libs["libiec60870.so"].get("MeasuredValueNormalizedWithCP24Time2a_create", "cdecl")
    MeasuredValueNormalizedWithCP24Time2a_create.argtypes = [MeasuredValueNormalizedWithCP24Time2a, c_int, c_float, QualityDescriptor, CP24Time2a]
    MeasuredValueNormalizedWithCP24Time2a_create.restype = MeasuredValueNormalizedWithCP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 604
if _libs["libiec60870.so"].has("MeasuredValueNormalizedWithCP24Time2a_getTimestamp", "cdecl"):
    MeasuredValueNormalizedWithCP24Time2a_getTimestamp = _libs["libiec60870.so"].get("MeasuredValueNormalizedWithCP24Time2a_getTimestamp", "cdecl")
    MeasuredValueNormalizedWithCP24Time2a_getTimestamp.argtypes = [MeasuredValueNormalizedWithCP24Time2a]
    MeasuredValueNormalizedWithCP24Time2a_getTimestamp.restype = CP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 607
if _libs["libiec60870.so"].has("MeasuredValueNormalizedWithCP24Time2a_setTimestamp", "cdecl"):
    MeasuredValueNormalizedWithCP24Time2a_setTimestamp = _libs["libiec60870.so"].get("MeasuredValueNormalizedWithCP24Time2a_setTimestamp", "cdecl")
    MeasuredValueNormalizedWithCP24Time2a_setTimestamp.argtypes = [MeasuredValueNormalizedWithCP24Time2a, CP24Time2a]
    MeasuredValueNormalizedWithCP24Time2a_setTimestamp.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 613
class struct_sMeasuredValueNormalizedWithCP56Time2a(Structure):
    pass

MeasuredValueNormalizedWithCP56Time2a = POINTER(struct_sMeasuredValueNormalizedWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 613

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 616
if _libs["libiec60870.so"].has("MeasuredValueNormalizedWithCP56Time2a_destroy", "cdecl"):
    MeasuredValueNormalizedWithCP56Time2a_destroy = _libs["libiec60870.so"].get("MeasuredValueNormalizedWithCP56Time2a_destroy", "cdecl")
    MeasuredValueNormalizedWithCP56Time2a_destroy.argtypes = [MeasuredValueNormalizedWithCP56Time2a]
    MeasuredValueNormalizedWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 619
if _libs["libiec60870.so"].has("MeasuredValueNormalizedWithCP56Time2a_create", "cdecl"):
    MeasuredValueNormalizedWithCP56Time2a_create = _libs["libiec60870.so"].get("MeasuredValueNormalizedWithCP56Time2a_create", "cdecl")
    MeasuredValueNormalizedWithCP56Time2a_create.argtypes = [MeasuredValueNormalizedWithCP56Time2a, c_int, c_float, QualityDescriptor, CP56Time2a]
    MeasuredValueNormalizedWithCP56Time2a_create.restype = MeasuredValueNormalizedWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 623
if _libs["libiec60870.so"].has("MeasuredValueNormalizedWithCP56Time2a_getTimestamp", "cdecl"):
    MeasuredValueNormalizedWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("MeasuredValueNormalizedWithCP56Time2a_getTimestamp", "cdecl")
    MeasuredValueNormalizedWithCP56Time2a_getTimestamp.argtypes = [MeasuredValueNormalizedWithCP56Time2a]
    MeasuredValueNormalizedWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 626
if _libs["libiec60870.so"].has("MeasuredValueNormalizedWithCP56Time2a_setTimestamp", "cdecl"):
    MeasuredValueNormalizedWithCP56Time2a_setTimestamp = _libs["libiec60870.so"].get("MeasuredValueNormalizedWithCP56Time2a_setTimestamp", "cdecl")
    MeasuredValueNormalizedWithCP56Time2a_setTimestamp.argtypes = [MeasuredValueNormalizedWithCP56Time2a, CP56Time2a]
    MeasuredValueNormalizedWithCP56Time2a_setTimestamp.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 633
class struct_sMeasuredValueScaled(Structure):
    pass

MeasuredValueScaled = POINTER(struct_sMeasuredValueScaled)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 633

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 646
if _libs["libiec60870.so"].has("MeasuredValueScaled_create", "cdecl"):
    MeasuredValueScaled_create = _libs["libiec60870.so"].get("MeasuredValueScaled_create", "cdecl")
    MeasuredValueScaled_create.argtypes = [MeasuredValueScaled, c_int, c_int, QualityDescriptor]
    MeasuredValueScaled_create.restype = MeasuredValueScaled

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 649
if _libs["libiec60870.so"].has("MeasuredValueScaled_destroy", "cdecl"):
    MeasuredValueScaled_destroy = _libs["libiec60870.so"].get("MeasuredValueScaled_destroy", "cdecl")
    MeasuredValueScaled_destroy.argtypes = [MeasuredValueScaled]
    MeasuredValueScaled_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 652
if _libs["libiec60870.so"].has("MeasuredValueScaled_getValue", "cdecl"):
    MeasuredValueScaled_getValue = _libs["libiec60870.so"].get("MeasuredValueScaled_getValue", "cdecl")
    MeasuredValueScaled_getValue.argtypes = [MeasuredValueScaled]
    MeasuredValueScaled_getValue.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 655
if _libs["libiec60870.so"].has("MeasuredValueScaled_setValue", "cdecl"):
    MeasuredValueScaled_setValue = _libs["libiec60870.so"].get("MeasuredValueScaled_setValue", "cdecl")
    MeasuredValueScaled_setValue.argtypes = [MeasuredValueScaled, c_int]
    MeasuredValueScaled_setValue.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 658
if _libs["libiec60870.so"].has("MeasuredValueScaled_getQuality", "cdecl"):
    MeasuredValueScaled_getQuality = _libs["libiec60870.so"].get("MeasuredValueScaled_getQuality", "cdecl")
    MeasuredValueScaled_getQuality.argtypes = [MeasuredValueScaled]
    MeasuredValueScaled_getQuality.restype = QualityDescriptor

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 661
if _libs["libiec60870.so"].has("MeasuredValueScaled_setQuality", "cdecl"):
    MeasuredValueScaled_setQuality = _libs["libiec60870.so"].get("MeasuredValueScaled_setQuality", "cdecl")
    MeasuredValueScaled_setQuality.argtypes = [MeasuredValueScaled, QualityDescriptor]
    MeasuredValueScaled_setQuality.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 667
class struct_sMeasuredValueScaledWithCP24Time2a(Structure):
    pass

MeasuredValueScaledWithCP24Time2a = POINTER(struct_sMeasuredValueScaledWithCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 667

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 670
if _libs["libiec60870.so"].has("MeasuredValueScaledWithCP24Time2a_destroy", "cdecl"):
    MeasuredValueScaledWithCP24Time2a_destroy = _libs["libiec60870.so"].get("MeasuredValueScaledWithCP24Time2a_destroy", "cdecl")
    MeasuredValueScaledWithCP24Time2a_destroy.argtypes = [MeasuredValueScaledWithCP24Time2a]
    MeasuredValueScaledWithCP24Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 673
if _libs["libiec60870.so"].has("MeasuredValueScaledWithCP24Time2a_create", "cdecl"):
    MeasuredValueScaledWithCP24Time2a_create = _libs["libiec60870.so"].get("MeasuredValueScaledWithCP24Time2a_create", "cdecl")
    MeasuredValueScaledWithCP24Time2a_create.argtypes = [MeasuredValueScaledWithCP24Time2a, c_int, c_int, QualityDescriptor, CP24Time2a]
    MeasuredValueScaledWithCP24Time2a_create.restype = MeasuredValueScaledWithCP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 677
if _libs["libiec60870.so"].has("MeasuredValueScaledWithCP24Time2a_getTimestamp", "cdecl"):
    MeasuredValueScaledWithCP24Time2a_getTimestamp = _libs["libiec60870.so"].get("MeasuredValueScaledWithCP24Time2a_getTimestamp", "cdecl")
    MeasuredValueScaledWithCP24Time2a_getTimestamp.argtypes = [MeasuredValueScaledWithCP24Time2a]
    MeasuredValueScaledWithCP24Time2a_getTimestamp.restype = CP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 680
if _libs["libiec60870.so"].has("MeasuredValueScaledWithCP24Time2a_setTimestamp", "cdecl"):
    MeasuredValueScaledWithCP24Time2a_setTimestamp = _libs["libiec60870.so"].get("MeasuredValueScaledWithCP24Time2a_setTimestamp", "cdecl")
    MeasuredValueScaledWithCP24Time2a_setTimestamp.argtypes = [MeasuredValueScaledWithCP24Time2a, CP24Time2a]
    MeasuredValueScaledWithCP24Time2a_setTimestamp.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 686
class struct_sMeasuredValueScaledWithCP56Time2a(Structure):
    pass

MeasuredValueScaledWithCP56Time2a = POINTER(struct_sMeasuredValueScaledWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 686

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 689
if _libs["libiec60870.so"].has("MeasuredValueScaledWithCP56Time2a_destroy", "cdecl"):
    MeasuredValueScaledWithCP56Time2a_destroy = _libs["libiec60870.so"].get("MeasuredValueScaledWithCP56Time2a_destroy", "cdecl")
    MeasuredValueScaledWithCP56Time2a_destroy.argtypes = [MeasuredValueScaledWithCP56Time2a]
    MeasuredValueScaledWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 692
if _libs["libiec60870.so"].has("MeasuredValueScaledWithCP56Time2a_create", "cdecl"):
    MeasuredValueScaledWithCP56Time2a_create = _libs["libiec60870.so"].get("MeasuredValueScaledWithCP56Time2a_create", "cdecl")
    MeasuredValueScaledWithCP56Time2a_create.argtypes = [MeasuredValueScaledWithCP56Time2a, c_int, c_int, QualityDescriptor, CP56Time2a]
    MeasuredValueScaledWithCP56Time2a_create.restype = MeasuredValueScaledWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 696
if _libs["libiec60870.so"].has("MeasuredValueScaledWithCP56Time2a_getTimestamp", "cdecl"):
    MeasuredValueScaledWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("MeasuredValueScaledWithCP56Time2a_getTimestamp", "cdecl")
    MeasuredValueScaledWithCP56Time2a_getTimestamp.argtypes = [MeasuredValueScaledWithCP56Time2a]
    MeasuredValueScaledWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 699
if _libs["libiec60870.so"].has("MeasuredValueScaledWithCP56Time2a_setTimestamp", "cdecl"):
    MeasuredValueScaledWithCP56Time2a_setTimestamp = _libs["libiec60870.so"].get("MeasuredValueScaledWithCP56Time2a_setTimestamp", "cdecl")
    MeasuredValueScaledWithCP56Time2a_setTimestamp.argtypes = [MeasuredValueScaledWithCP56Time2a, CP56Time2a]
    MeasuredValueScaledWithCP56Time2a_setTimestamp.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 705
class struct_sMeasuredValueShort(Structure):
    pass

MeasuredValueShort = POINTER(struct_sMeasuredValueShort)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 705

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 708
if _libs["libiec60870.so"].has("MeasuredValueShort_destroy", "cdecl"):
    MeasuredValueShort_destroy = _libs["libiec60870.so"].get("MeasuredValueShort_destroy", "cdecl")
    MeasuredValueShort_destroy.argtypes = [MeasuredValueShort]
    MeasuredValueShort_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 711
if _libs["libiec60870.so"].has("MeasuredValueShort_create", "cdecl"):
    MeasuredValueShort_create = _libs["libiec60870.so"].get("MeasuredValueShort_create", "cdecl")
    MeasuredValueShort_create.argtypes = [MeasuredValueShort, c_int, c_float, QualityDescriptor]
    MeasuredValueShort_create.restype = MeasuredValueShort

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 714
if _libs["libiec60870.so"].has("MeasuredValueShort_getValue", "cdecl"):
    MeasuredValueShort_getValue = _libs["libiec60870.so"].get("MeasuredValueShort_getValue", "cdecl")
    MeasuredValueShort_getValue.argtypes = [MeasuredValueShort]
    MeasuredValueShort_getValue.restype = c_float

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 717
if _libs["libiec60870.so"].has("MeasuredValueShort_setValue", "cdecl"):
    MeasuredValueShort_setValue = _libs["libiec60870.so"].get("MeasuredValueShort_setValue", "cdecl")
    MeasuredValueShort_setValue.argtypes = [MeasuredValueShort, c_float]
    MeasuredValueShort_setValue.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 720
if _libs["libiec60870.so"].has("MeasuredValueShort_getQuality", "cdecl"):
    MeasuredValueShort_getQuality = _libs["libiec60870.so"].get("MeasuredValueShort_getQuality", "cdecl")
    MeasuredValueShort_getQuality.argtypes = [MeasuredValueShort]
    MeasuredValueShort_getQuality.restype = QualityDescriptor

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 726
class struct_sMeasuredValueShortWithCP24Time2a(Structure):
    pass

MeasuredValueShortWithCP24Time2a = POINTER(struct_sMeasuredValueShortWithCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 726

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 729
if _libs["libiec60870.so"].has("MeasuredValueShortWithCP24Time2a_destroy", "cdecl"):
    MeasuredValueShortWithCP24Time2a_destroy = _libs["libiec60870.so"].get("MeasuredValueShortWithCP24Time2a_destroy", "cdecl")
    MeasuredValueShortWithCP24Time2a_destroy.argtypes = [MeasuredValueShortWithCP24Time2a]
    MeasuredValueShortWithCP24Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 732
if _libs["libiec60870.so"].has("MeasuredValueShortWithCP24Time2a_create", "cdecl"):
    MeasuredValueShortWithCP24Time2a_create = _libs["libiec60870.so"].get("MeasuredValueShortWithCP24Time2a_create", "cdecl")
    MeasuredValueShortWithCP24Time2a_create.argtypes = [MeasuredValueShortWithCP24Time2a, c_int, c_float, QualityDescriptor, CP24Time2a]
    MeasuredValueShortWithCP24Time2a_create.restype = MeasuredValueShortWithCP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 736
if _libs["libiec60870.so"].has("MeasuredValueShortWithCP24Time2a_getTimestamp", "cdecl"):
    MeasuredValueShortWithCP24Time2a_getTimestamp = _libs["libiec60870.so"].get("MeasuredValueShortWithCP24Time2a_getTimestamp", "cdecl")
    MeasuredValueShortWithCP24Time2a_getTimestamp.argtypes = [MeasuredValueShortWithCP24Time2a]
    MeasuredValueShortWithCP24Time2a_getTimestamp.restype = CP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 739
if _libs["libiec60870.so"].has("MeasuredValueShortWithCP24Time2a_setTimestamp", "cdecl"):
    MeasuredValueShortWithCP24Time2a_setTimestamp = _libs["libiec60870.so"].get("MeasuredValueShortWithCP24Time2a_setTimestamp", "cdecl")
    MeasuredValueShortWithCP24Time2a_setTimestamp.argtypes = [MeasuredValueShortWithCP24Time2a, CP24Time2a]
    MeasuredValueShortWithCP24Time2a_setTimestamp.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 746
class struct_sMeasuredValueShortWithCP56Time2a(Structure):
    pass

MeasuredValueShortWithCP56Time2a = POINTER(struct_sMeasuredValueShortWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 746

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 749
if _libs["libiec60870.so"].has("MeasuredValueShortWithCP56Time2a_destroy", "cdecl"):
    MeasuredValueShortWithCP56Time2a_destroy = _libs["libiec60870.so"].get("MeasuredValueShortWithCP56Time2a_destroy", "cdecl")
    MeasuredValueShortWithCP56Time2a_destroy.argtypes = [MeasuredValueShortWithCP56Time2a]
    MeasuredValueShortWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 752
if _libs["libiec60870.so"].has("MeasuredValueShortWithCP56Time2a_create", "cdecl"):
    MeasuredValueShortWithCP56Time2a_create = _libs["libiec60870.so"].get("MeasuredValueShortWithCP56Time2a_create", "cdecl")
    MeasuredValueShortWithCP56Time2a_create.argtypes = [MeasuredValueShortWithCP56Time2a, c_int, c_float, QualityDescriptor, CP56Time2a]
    MeasuredValueShortWithCP56Time2a_create.restype = MeasuredValueShortWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 756
if _libs["libiec60870.so"].has("MeasuredValueShortWithCP56Time2a_getTimestamp", "cdecl"):
    MeasuredValueShortWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("MeasuredValueShortWithCP56Time2a_getTimestamp", "cdecl")
    MeasuredValueShortWithCP56Time2a_getTimestamp.argtypes = [MeasuredValueShortWithCP56Time2a]
    MeasuredValueShortWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 759
if _libs["libiec60870.so"].has("MeasuredValueShortWithCP56Time2a_setTimestamp", "cdecl"):
    MeasuredValueShortWithCP56Time2a_setTimestamp = _libs["libiec60870.so"].get("MeasuredValueShortWithCP56Time2a_setTimestamp", "cdecl")
    MeasuredValueShortWithCP56Time2a_setTimestamp.argtypes = [MeasuredValueShortWithCP56Time2a, CP56Time2a]
    MeasuredValueShortWithCP56Time2a_setTimestamp.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 766
class struct_sIntegratedTotals(Structure):
    pass

IntegratedTotals = POINTER(struct_sIntegratedTotals)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 766

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 769
if _libs["libiec60870.so"].has("IntegratedTotals_destroy", "cdecl"):
    IntegratedTotals_destroy = _libs["libiec60870.so"].get("IntegratedTotals_destroy", "cdecl")
    IntegratedTotals_destroy.argtypes = [IntegratedTotals]
    IntegratedTotals_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 783
if _libs["libiec60870.so"].has("IntegratedTotals_create", "cdecl"):
    IntegratedTotals_create = _libs["libiec60870.so"].get("IntegratedTotals_create", "cdecl")
    IntegratedTotals_create.argtypes = [IntegratedTotals, c_int, BinaryCounterReading]
    IntegratedTotals_create.restype = IntegratedTotals

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 786
if _libs["libiec60870.so"].has("IntegratedTotals_getBCR", "cdecl"):
    IntegratedTotals_getBCR = _libs["libiec60870.so"].get("IntegratedTotals_getBCR", "cdecl")
    IntegratedTotals_getBCR.argtypes = [IntegratedTotals]
    IntegratedTotals_getBCR.restype = BinaryCounterReading

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 789
if _libs["libiec60870.so"].has("IntegratedTotals_setBCR", "cdecl"):
    IntegratedTotals_setBCR = _libs["libiec60870.so"].get("IntegratedTotals_setBCR", "cdecl")
    IntegratedTotals_setBCR.argtypes = [IntegratedTotals, BinaryCounterReading]
    IntegratedTotals_setBCR.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 795
class struct_sIntegratedTotalsWithCP24Time2a(Structure):
    pass

IntegratedTotalsWithCP24Time2a = POINTER(struct_sIntegratedTotalsWithCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 795

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 810
if _libs["libiec60870.so"].has("IntegratedTotalsWithCP24Time2a_create", "cdecl"):
    IntegratedTotalsWithCP24Time2a_create = _libs["libiec60870.so"].get("IntegratedTotalsWithCP24Time2a_create", "cdecl")
    IntegratedTotalsWithCP24Time2a_create.argtypes = [IntegratedTotalsWithCP24Time2a, c_int, BinaryCounterReading, CP24Time2a]
    IntegratedTotalsWithCP24Time2a_create.restype = IntegratedTotalsWithCP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 814
if _libs["libiec60870.so"].has("IntegratedTotalsWithCP24Time2a_destroy", "cdecl"):
    IntegratedTotalsWithCP24Time2a_destroy = _libs["libiec60870.so"].get("IntegratedTotalsWithCP24Time2a_destroy", "cdecl")
    IntegratedTotalsWithCP24Time2a_destroy.argtypes = [IntegratedTotalsWithCP24Time2a]
    IntegratedTotalsWithCP24Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 817
if _libs["libiec60870.so"].has("IntegratedTotalsWithCP24Time2a_getTimestamp", "cdecl"):
    IntegratedTotalsWithCP24Time2a_getTimestamp = _libs["libiec60870.so"].get("IntegratedTotalsWithCP24Time2a_getTimestamp", "cdecl")
    IntegratedTotalsWithCP24Time2a_getTimestamp.argtypes = [IntegratedTotalsWithCP24Time2a]
    IntegratedTotalsWithCP24Time2a_getTimestamp.restype = CP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 820
if _libs["libiec60870.so"].has("IntegratedTotalsWithCP24Time2a_setTimestamp", "cdecl"):
    IntegratedTotalsWithCP24Time2a_setTimestamp = _libs["libiec60870.so"].get("IntegratedTotalsWithCP24Time2a_setTimestamp", "cdecl")
    IntegratedTotalsWithCP24Time2a_setTimestamp.argtypes = [IntegratedTotalsWithCP24Time2a, CP24Time2a]
    IntegratedTotalsWithCP24Time2a_setTimestamp.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 827
class struct_sIntegratedTotalsWithCP56Time2a(Structure):
    pass

IntegratedTotalsWithCP56Time2a = POINTER(struct_sIntegratedTotalsWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 827

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 842
if _libs["libiec60870.so"].has("IntegratedTotalsWithCP56Time2a_create", "cdecl"):
    IntegratedTotalsWithCP56Time2a_create = _libs["libiec60870.so"].get("IntegratedTotalsWithCP56Time2a_create", "cdecl")
    IntegratedTotalsWithCP56Time2a_create.argtypes = [IntegratedTotalsWithCP56Time2a, c_int, BinaryCounterReading, CP56Time2a]
    IntegratedTotalsWithCP56Time2a_create.restype = IntegratedTotalsWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 846
if _libs["libiec60870.so"].has("IntegratedTotalsWithCP56Time2a_destroy", "cdecl"):
    IntegratedTotalsWithCP56Time2a_destroy = _libs["libiec60870.so"].get("IntegratedTotalsWithCP56Time2a_destroy", "cdecl")
    IntegratedTotalsWithCP56Time2a_destroy.argtypes = [IntegratedTotalsWithCP56Time2a]
    IntegratedTotalsWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 849
if _libs["libiec60870.so"].has("IntegratedTotalsWithCP56Time2a_getTimestamp", "cdecl"):
    IntegratedTotalsWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("IntegratedTotalsWithCP56Time2a_getTimestamp", "cdecl")
    IntegratedTotalsWithCP56Time2a_getTimestamp.argtypes = [IntegratedTotalsWithCP56Time2a]
    IntegratedTotalsWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 852
if _libs["libiec60870.so"].has("IntegratedTotalsWithCP56Time2a_setTimestamp", "cdecl"):
    IntegratedTotalsWithCP56Time2a_setTimestamp = _libs["libiec60870.so"].get("IntegratedTotalsWithCP56Time2a_setTimestamp", "cdecl")
    IntegratedTotalsWithCP56Time2a_setTimestamp.argtypes = [IntegratedTotalsWithCP56Time2a, CP56Time2a]
    IntegratedTotalsWithCP56Time2a_setTimestamp.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 859
class struct_sIntegratedTotalsForSecurityStatistics(Structure):
    pass

IntegratedTotalsForSecurityStatistics = POINTER(struct_sIntegratedTotalsForSecurityStatistics)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 859

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 862
if _libs["libiec60870.so"].has("IntegratedTotalsForSecurityStatistics_destroy", "cdecl"):
    IntegratedTotalsForSecurityStatistics_destroy = _libs["libiec60870.so"].get("IntegratedTotalsForSecurityStatistics_destroy", "cdecl")
    IntegratedTotalsForSecurityStatistics_destroy.argtypes = [IntegratedTotalsForSecurityStatistics]
    IntegratedTotalsForSecurityStatistics_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 878
if _libs["libiec60870.so"].has("IntegratedTotalsForSecurityStatistics_create", "cdecl"):
    IntegratedTotalsForSecurityStatistics_create = _libs["libiec60870.so"].get("IntegratedTotalsForSecurityStatistics_create", "cdecl")
    IntegratedTotalsForSecurityStatistics_create.argtypes = [IntegratedTotalsForSecurityStatistics, c_int, uint16_t, BinaryCounterReading, CP56Time2a]
    IntegratedTotalsForSecurityStatistics_create.restype = IntegratedTotalsForSecurityStatistics

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 882
for _lib in _libs.values():
    if not _lib.has("IntegratedTotalsForSecurityStatistics_getAID", "cdecl"):
        continue
    IntegratedTotalsForSecurityStatistics_getAID = _lib.get("IntegratedTotalsForSecurityStatistics_getAID", "cdecl")
    IntegratedTotalsForSecurityStatistics_getAID.argtypes = [IntegratedTotalsForSecurityStatistics]
    IntegratedTotalsForSecurityStatistics_getAID.restype = uint16_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 885
for _lib in _libs.values():
    if not _lib.has("IntegratedTotalsForSecurityStatistics_setAID", "cdecl"):
        continue
    IntegratedTotalsForSecurityStatistics_setAID = _lib.get("IntegratedTotalsForSecurityStatistics_setAID", "cdecl")
    IntegratedTotalsForSecurityStatistics_setAID.argtypes = [IntegratedTotalsForSecurityStatistics, uint16_t]
    IntegratedTotalsForSecurityStatistics_setAID.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 888
if _libs["libiec60870.so"].has("IntegratedTotalsForSecurityStatistics_getBCR", "cdecl"):
    IntegratedTotalsForSecurityStatistics_getBCR = _libs["libiec60870.so"].get("IntegratedTotalsForSecurityStatistics_getBCR", "cdecl")
    IntegratedTotalsForSecurityStatistics_getBCR.argtypes = [IntegratedTotalsForSecurityStatistics]
    IntegratedTotalsForSecurityStatistics_getBCR.restype = BinaryCounterReading

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 891
if _libs["libiec60870.so"].has("IntegratedTotalsForSecurityStatistics_setBCR", "cdecl"):
    IntegratedTotalsForSecurityStatistics_setBCR = _libs["libiec60870.so"].get("IntegratedTotalsForSecurityStatistics_setBCR", "cdecl")
    IntegratedTotalsForSecurityStatistics_setBCR.argtypes = [IntegratedTotalsForSecurityStatistics, BinaryCounterReading]
    IntegratedTotalsForSecurityStatistics_setBCR.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 894
if _libs["libiec60870.so"].has("IntegratedTotalsForSecurityStatistics_getTimestamp", "cdecl"):
    IntegratedTotalsForSecurityStatistics_getTimestamp = _libs["libiec60870.so"].get("IntegratedTotalsForSecurityStatistics_getTimestamp", "cdecl")
    IntegratedTotalsForSecurityStatistics_getTimestamp.argtypes = [IntegratedTotalsForSecurityStatistics]
    IntegratedTotalsForSecurityStatistics_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 897
if _libs["libiec60870.so"].has("IntegratedTotalsForSecurityStatistics_setTimestamp", "cdecl"):
    IntegratedTotalsForSecurityStatistics_setTimestamp = _libs["libiec60870.so"].get("IntegratedTotalsForSecurityStatistics_setTimestamp", "cdecl")
    IntegratedTotalsForSecurityStatistics_setTimestamp.argtypes = [IntegratedTotalsForSecurityStatistics, CP56Time2a]
    IntegratedTotalsForSecurityStatistics_setTimestamp.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 905
class struct_sEventOfProtectionEquipment(Structure):
    pass

EventOfProtectionEquipment = POINTER(struct_sEventOfProtectionEquipment)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 905

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 908
if _libs["libiec60870.so"].has("EventOfProtectionEquipment_destroy", "cdecl"):
    EventOfProtectionEquipment_destroy = _libs["libiec60870.so"].get("EventOfProtectionEquipment_destroy", "cdecl")
    EventOfProtectionEquipment_destroy.argtypes = [EventOfProtectionEquipment]
    EventOfProtectionEquipment_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 911
if _libs["libiec60870.so"].has("EventOfProtectionEquipment_create", "cdecl"):
    EventOfProtectionEquipment_create = _libs["libiec60870.so"].get("EventOfProtectionEquipment_create", "cdecl")
    EventOfProtectionEquipment_create.argtypes = [EventOfProtectionEquipment, c_int, SingleEvent, CP16Time2a, CP24Time2a]
    EventOfProtectionEquipment_create.restype = EventOfProtectionEquipment

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 915
if _libs["libiec60870.so"].has("EventOfProtectionEquipment_getEvent", "cdecl"):
    EventOfProtectionEquipment_getEvent = _libs["libiec60870.so"].get("EventOfProtectionEquipment_getEvent", "cdecl")
    EventOfProtectionEquipment_getEvent.argtypes = [EventOfProtectionEquipment]
    EventOfProtectionEquipment_getEvent.restype = SingleEvent

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 918
if _libs["libiec60870.so"].has("EventOfProtectionEquipment_getElapsedTime", "cdecl"):
    EventOfProtectionEquipment_getElapsedTime = _libs["libiec60870.so"].get("EventOfProtectionEquipment_getElapsedTime", "cdecl")
    EventOfProtectionEquipment_getElapsedTime.argtypes = [EventOfProtectionEquipment]
    EventOfProtectionEquipment_getElapsedTime.restype = CP16Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 921
if _libs["libiec60870.so"].has("EventOfProtectionEquipment_getTimestamp", "cdecl"):
    EventOfProtectionEquipment_getTimestamp = _libs["libiec60870.so"].get("EventOfProtectionEquipment_getTimestamp", "cdecl")
    EventOfProtectionEquipment_getTimestamp.argtypes = [EventOfProtectionEquipment]
    EventOfProtectionEquipment_getTimestamp.restype = CP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 927
class struct_sPackedStartEventsOfProtectionEquipment(Structure):
    pass

PackedStartEventsOfProtectionEquipment = POINTER(struct_sPackedStartEventsOfProtectionEquipment)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 927

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 930
if _libs["libiec60870.so"].has("PackedStartEventsOfProtectionEquipment_create", "cdecl"):
    PackedStartEventsOfProtectionEquipment_create = _libs["libiec60870.so"].get("PackedStartEventsOfProtectionEquipment_create", "cdecl")
    PackedStartEventsOfProtectionEquipment_create.argtypes = [PackedStartEventsOfProtectionEquipment, c_int, StartEvent, QualityDescriptorP, CP16Time2a, CP24Time2a]
    PackedStartEventsOfProtectionEquipment_create.restype = PackedStartEventsOfProtectionEquipment

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 934
if _libs["libiec60870.so"].has("PackedStartEventsOfProtectionEquipment_destroy", "cdecl"):
    PackedStartEventsOfProtectionEquipment_destroy = _libs["libiec60870.so"].get("PackedStartEventsOfProtectionEquipment_destroy", "cdecl")
    PackedStartEventsOfProtectionEquipment_destroy.argtypes = [PackedStartEventsOfProtectionEquipment]
    PackedStartEventsOfProtectionEquipment_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 937
if _libs["libiec60870.so"].has("PackedStartEventsOfProtectionEquipment_getEvent", "cdecl"):
    PackedStartEventsOfProtectionEquipment_getEvent = _libs["libiec60870.so"].get("PackedStartEventsOfProtectionEquipment_getEvent", "cdecl")
    PackedStartEventsOfProtectionEquipment_getEvent.argtypes = [PackedStartEventsOfProtectionEquipment]
    PackedStartEventsOfProtectionEquipment_getEvent.restype = StartEvent

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 940
if _libs["libiec60870.so"].has("PackedStartEventsOfProtectionEquipment_getQuality", "cdecl"):
    PackedStartEventsOfProtectionEquipment_getQuality = _libs["libiec60870.so"].get("PackedStartEventsOfProtectionEquipment_getQuality", "cdecl")
    PackedStartEventsOfProtectionEquipment_getQuality.argtypes = [PackedStartEventsOfProtectionEquipment]
    PackedStartEventsOfProtectionEquipment_getQuality.restype = QualityDescriptorP

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 943
if _libs["libiec60870.so"].has("PackedStartEventsOfProtectionEquipment_getElapsedTime", "cdecl"):
    PackedStartEventsOfProtectionEquipment_getElapsedTime = _libs["libiec60870.so"].get("PackedStartEventsOfProtectionEquipment_getElapsedTime", "cdecl")
    PackedStartEventsOfProtectionEquipment_getElapsedTime.argtypes = [PackedStartEventsOfProtectionEquipment]
    PackedStartEventsOfProtectionEquipment_getElapsedTime.restype = CP16Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 946
if _libs["libiec60870.so"].has("PackedStartEventsOfProtectionEquipment_getTimestamp", "cdecl"):
    PackedStartEventsOfProtectionEquipment_getTimestamp = _libs["libiec60870.so"].get("PackedStartEventsOfProtectionEquipment_getTimestamp", "cdecl")
    PackedStartEventsOfProtectionEquipment_getTimestamp.argtypes = [PackedStartEventsOfProtectionEquipment]
    PackedStartEventsOfProtectionEquipment_getTimestamp.restype = CP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 952
class struct_sPackedOutputCircuitInfo(Structure):
    pass

PackedOutputCircuitInfo = POINTER(struct_sPackedOutputCircuitInfo)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 952

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 955
if _libs["libiec60870.so"].has("PackedOutputCircuitInfo_destroy", "cdecl"):
    PackedOutputCircuitInfo_destroy = _libs["libiec60870.so"].get("PackedOutputCircuitInfo_destroy", "cdecl")
    PackedOutputCircuitInfo_destroy.argtypes = [PackedOutputCircuitInfo]
    PackedOutputCircuitInfo_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 958
if _libs["libiec60870.so"].has("PackedOutputCircuitInfo_create", "cdecl"):
    PackedOutputCircuitInfo_create = _libs["libiec60870.so"].get("PackedOutputCircuitInfo_create", "cdecl")
    PackedOutputCircuitInfo_create.argtypes = [PackedOutputCircuitInfo, c_int, OutputCircuitInfo, QualityDescriptorP, CP16Time2a, CP24Time2a]
    PackedOutputCircuitInfo_create.restype = PackedOutputCircuitInfo

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 962
if _libs["libiec60870.so"].has("PackedOutputCircuitInfo_getOCI", "cdecl"):
    PackedOutputCircuitInfo_getOCI = _libs["libiec60870.so"].get("PackedOutputCircuitInfo_getOCI", "cdecl")
    PackedOutputCircuitInfo_getOCI.argtypes = [PackedOutputCircuitInfo]
    PackedOutputCircuitInfo_getOCI.restype = OutputCircuitInfo

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 965
if _libs["libiec60870.so"].has("PackedOutputCircuitInfo_getQuality", "cdecl"):
    PackedOutputCircuitInfo_getQuality = _libs["libiec60870.so"].get("PackedOutputCircuitInfo_getQuality", "cdecl")
    PackedOutputCircuitInfo_getQuality.argtypes = [PackedOutputCircuitInfo]
    PackedOutputCircuitInfo_getQuality.restype = QualityDescriptorP

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 968
if _libs["libiec60870.so"].has("PackedOutputCircuitInfo_getOperatingTime", "cdecl"):
    PackedOutputCircuitInfo_getOperatingTime = _libs["libiec60870.so"].get("PackedOutputCircuitInfo_getOperatingTime", "cdecl")
    PackedOutputCircuitInfo_getOperatingTime.argtypes = [PackedOutputCircuitInfo]
    PackedOutputCircuitInfo_getOperatingTime.restype = CP16Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 971
if _libs["libiec60870.so"].has("PackedOutputCircuitInfo_getTimestamp", "cdecl"):
    PackedOutputCircuitInfo_getTimestamp = _libs["libiec60870.so"].get("PackedOutputCircuitInfo_getTimestamp", "cdecl")
    PackedOutputCircuitInfo_getTimestamp.argtypes = [PackedOutputCircuitInfo]
    PackedOutputCircuitInfo_getTimestamp.restype = CP24Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 977
class struct_sPackedSinglePointWithSCD(Structure):
    pass

PackedSinglePointWithSCD = POINTER(struct_sPackedSinglePointWithSCD)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 977

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 980
if _libs["libiec60870.so"].has("PackedSinglePointWithSCD_destroy", "cdecl"):
    PackedSinglePointWithSCD_destroy = _libs["libiec60870.so"].get("PackedSinglePointWithSCD_destroy", "cdecl")
    PackedSinglePointWithSCD_destroy.argtypes = [PackedSinglePointWithSCD]
    PackedSinglePointWithSCD_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 983
if _libs["libiec60870.so"].has("PackedSinglePointWithSCD_create", "cdecl"):
    PackedSinglePointWithSCD_create = _libs["libiec60870.so"].get("PackedSinglePointWithSCD_create", "cdecl")
    PackedSinglePointWithSCD_create.argtypes = [PackedSinglePointWithSCD, c_int, StatusAndStatusChangeDetection, QualityDescriptor]
    PackedSinglePointWithSCD_create.restype = PackedSinglePointWithSCD

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 987
if _libs["libiec60870.so"].has("PackedSinglePointWithSCD_getQuality", "cdecl"):
    PackedSinglePointWithSCD_getQuality = _libs["libiec60870.so"].get("PackedSinglePointWithSCD_getQuality", "cdecl")
    PackedSinglePointWithSCD_getQuality.argtypes = [PackedSinglePointWithSCD]
    PackedSinglePointWithSCD_getQuality.restype = QualityDescriptor

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 990
if _libs["libiec60870.so"].has("PackedSinglePointWithSCD_getSCD", "cdecl"):
    PackedSinglePointWithSCD_getSCD = _libs["libiec60870.so"].get("PackedSinglePointWithSCD_getSCD", "cdecl")
    PackedSinglePointWithSCD_getSCD.argtypes = [PackedSinglePointWithSCD]
    PackedSinglePointWithSCD_getSCD.restype = StatusAndStatusChangeDetection

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 997
class struct_sSingleCommand(Structure):
    pass

SingleCommand = POINTER(struct_sSingleCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 997

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1011
if _libs["libiec60870.so"].has("SingleCommand_create", "cdecl"):
    SingleCommand_create = _libs["libiec60870.so"].get("SingleCommand_create", "cdecl")
    SingleCommand_create.argtypes = [SingleCommand, c_int, c_bool, c_bool, c_int]
    SingleCommand_create.restype = SingleCommand

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1014
if _libs["libiec60870.so"].has("SingleCommand_destroy", "cdecl"):
    SingleCommand_destroy = _libs["libiec60870.so"].get("SingleCommand_destroy", "cdecl")
    SingleCommand_destroy.argtypes = [SingleCommand]
    SingleCommand_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1022
if _libs["libiec60870.so"].has("SingleCommand_getQU", "cdecl"):
    SingleCommand_getQU = _libs["libiec60870.so"].get("SingleCommand_getQU", "cdecl")
    SingleCommand_getQU.argtypes = [SingleCommand]
    SingleCommand_getQU.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1028
if _libs["libiec60870.so"].has("SingleCommand_getState", "cdecl"):
    SingleCommand_getState = _libs["libiec60870.so"].get("SingleCommand_getState", "cdecl")
    SingleCommand_getState.argtypes = [SingleCommand]
    SingleCommand_getState.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1036
if _libs["libiec60870.so"].has("SingleCommand_isSelect", "cdecl"):
    SingleCommand_isSelect = _libs["libiec60870.so"].get("SingleCommand_isSelect", "cdecl")
    SingleCommand_isSelect.argtypes = [SingleCommand]
    SingleCommand_isSelect.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1042
class struct_sSingleCommandWithCP56Time2a(Structure):
    pass

SingleCommandWithCP56Time2a = POINTER(struct_sSingleCommandWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1042

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1045
if _libs["libiec60870.so"].has("SingleCommandWithCP56Time2a_destroy", "cdecl"):
    SingleCommandWithCP56Time2a_destroy = _libs["libiec60870.so"].get("SingleCommandWithCP56Time2a_destroy", "cdecl")
    SingleCommandWithCP56Time2a_destroy.argtypes = [SingleCommandWithCP56Time2a]
    SingleCommandWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1060
if _libs["libiec60870.so"].has("SingleCommandWithCP56Time2a_create", "cdecl"):
    SingleCommandWithCP56Time2a_create = _libs["libiec60870.so"].get("SingleCommandWithCP56Time2a_create", "cdecl")
    SingleCommandWithCP56Time2a_create.argtypes = [SingleCommandWithCP56Time2a, c_int, c_bool, c_bool, c_int, CP56Time2a]
    SingleCommandWithCP56Time2a_create.restype = SingleCommandWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1071
if _libs["libiec60870.so"].has("SingleCommandWithCP56Time2a_getTimestamp", "cdecl"):
    SingleCommandWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("SingleCommandWithCP56Time2a_getTimestamp", "cdecl")
    SingleCommandWithCP56Time2a_getTimestamp.argtypes = [SingleCommandWithCP56Time2a]
    SingleCommandWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1077
class struct_sDoubleCommand(Structure):
    pass

DoubleCommand = POINTER(struct_sDoubleCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1077

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1080
if _libs["libiec60870.so"].has("DoubleCommand_destroy", "cdecl"):
    DoubleCommand_destroy = _libs["libiec60870.so"].get("DoubleCommand_destroy", "cdecl")
    DoubleCommand_destroy.argtypes = [DoubleCommand]
    DoubleCommand_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1094
if _libs["libiec60870.so"].has("DoubleCommand_create", "cdecl"):
    DoubleCommand_create = _libs["libiec60870.so"].get("DoubleCommand_create", "cdecl")
    DoubleCommand_create.argtypes = [DoubleCommand, c_int, c_int, c_bool, c_int]
    DoubleCommand_create.restype = DoubleCommand

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1102
if _libs["libiec60870.so"].has("DoubleCommand_getQU", "cdecl"):
    DoubleCommand_getQU = _libs["libiec60870.so"].get("DoubleCommand_getQU", "cdecl")
    DoubleCommand_getQU.argtypes = [DoubleCommand]
    DoubleCommand_getQU.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1110
if _libs["libiec60870.so"].has("DoubleCommand_getState", "cdecl"):
    DoubleCommand_getState = _libs["libiec60870.so"].get("DoubleCommand_getState", "cdecl")
    DoubleCommand_getState.argtypes = [DoubleCommand]
    DoubleCommand_getState.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1118
if _libs["libiec60870.so"].has("DoubleCommand_isSelect", "cdecl"):
    DoubleCommand_isSelect = _libs["libiec60870.so"].get("DoubleCommand_isSelect", "cdecl")
    DoubleCommand_isSelect.argtypes = [DoubleCommand]
    DoubleCommand_isSelect.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1124
class struct_sStepCommand(Structure):
    pass

StepCommand = POINTER(struct_sStepCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1124

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1127
if _libs["libiec60870.so"].has("StepCommand_destroy", "cdecl"):
    StepCommand_destroy = _libs["libiec60870.so"].get("StepCommand_destroy", "cdecl")
    StepCommand_destroy.argtypes = [StepCommand]
    StepCommand_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1130
if _libs["libiec60870.so"].has("StepCommand_create", "cdecl"):
    StepCommand_create = _libs["libiec60870.so"].get("StepCommand_create", "cdecl")
    StepCommand_create.argtypes = [StepCommand, c_int, StepCommandValue, c_bool, c_int]
    StepCommand_create.restype = StepCommand

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1138
if _libs["libiec60870.so"].has("StepCommand_getQU", "cdecl"):
    StepCommand_getQU = _libs["libiec60870.so"].get("StepCommand_getQU", "cdecl")
    StepCommand_getQU.argtypes = [StepCommand]
    StepCommand_getQU.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1141
if _libs["libiec60870.so"].has("StepCommand_getState", "cdecl"):
    StepCommand_getState = _libs["libiec60870.so"].get("StepCommand_getState", "cdecl")
    StepCommand_getState.argtypes = [StepCommand]
    StepCommand_getState.restype = StepCommandValue

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1149
if _libs["libiec60870.so"].has("StepCommand_isSelect", "cdecl"):
    StepCommand_isSelect = _libs["libiec60870.so"].get("StepCommand_isSelect", "cdecl")
    StepCommand_isSelect.argtypes = [StepCommand]
    StepCommand_isSelect.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1155
class struct_sSetpointCommandNormalized(Structure):
    pass

SetpointCommandNormalized = POINTER(struct_sSetpointCommandNormalized)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1155

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1158
if _libs["libiec60870.so"].has("SetpointCommandNormalized_destroy", "cdecl"):
    SetpointCommandNormalized_destroy = _libs["libiec60870.so"].get("SetpointCommandNormalized_destroy", "cdecl")
    SetpointCommandNormalized_destroy.argtypes = [SetpointCommandNormalized]
    SetpointCommandNormalized_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1172
if _libs["libiec60870.so"].has("SetpointCommandNormalized_create", "cdecl"):
    SetpointCommandNormalized_create = _libs["libiec60870.so"].get("SetpointCommandNormalized_create", "cdecl")
    SetpointCommandNormalized_create.argtypes = [SetpointCommandNormalized, c_int, c_float, c_bool, c_int]
    SetpointCommandNormalized_create.restype = SetpointCommandNormalized

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1175
if _libs["libiec60870.so"].has("SetpointCommandNormalized_getValue", "cdecl"):
    SetpointCommandNormalized_getValue = _libs["libiec60870.so"].get("SetpointCommandNormalized_getValue", "cdecl")
    SetpointCommandNormalized_getValue.argtypes = [SetpointCommandNormalized]
    SetpointCommandNormalized_getValue.restype = c_float

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1178
if _libs["libiec60870.so"].has("SetpointCommandNormalized_getQL", "cdecl"):
    SetpointCommandNormalized_getQL = _libs["libiec60870.so"].get("SetpointCommandNormalized_getQL", "cdecl")
    SetpointCommandNormalized_getQL.argtypes = [SetpointCommandNormalized]
    SetpointCommandNormalized_getQL.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1186
if _libs["libiec60870.so"].has("SetpointCommandNormalized_isSelect", "cdecl"):
    SetpointCommandNormalized_isSelect = _libs["libiec60870.so"].get("SetpointCommandNormalized_isSelect", "cdecl")
    SetpointCommandNormalized_isSelect.argtypes = [SetpointCommandNormalized]
    SetpointCommandNormalized_isSelect.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1192
class struct_sSetpointCommandScaled(Structure):
    pass

SetpointCommandScaled = POINTER(struct_sSetpointCommandScaled)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1192

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1195
if _libs["libiec60870.so"].has("SetpointCommandScaled_destroy", "cdecl"):
    SetpointCommandScaled_destroy = _libs["libiec60870.so"].get("SetpointCommandScaled_destroy", "cdecl")
    SetpointCommandScaled_destroy.argtypes = [SetpointCommandScaled]
    SetpointCommandScaled_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1209
if _libs["libiec60870.so"].has("SetpointCommandScaled_create", "cdecl"):
    SetpointCommandScaled_create = _libs["libiec60870.so"].get("SetpointCommandScaled_create", "cdecl")
    SetpointCommandScaled_create.argtypes = [SetpointCommandScaled, c_int, c_int, c_bool, c_int]
    SetpointCommandScaled_create.restype = SetpointCommandScaled

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1212
if _libs["libiec60870.so"].has("SetpointCommandScaled_getValue", "cdecl"):
    SetpointCommandScaled_getValue = _libs["libiec60870.so"].get("SetpointCommandScaled_getValue", "cdecl")
    SetpointCommandScaled_getValue.argtypes = [SetpointCommandScaled]
    SetpointCommandScaled_getValue.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1215
if _libs["libiec60870.so"].has("SetpointCommandScaled_getQL", "cdecl"):
    SetpointCommandScaled_getQL = _libs["libiec60870.so"].get("SetpointCommandScaled_getQL", "cdecl")
    SetpointCommandScaled_getQL.argtypes = [SetpointCommandScaled]
    SetpointCommandScaled_getQL.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1223
if _libs["libiec60870.so"].has("SetpointCommandScaled_isSelect", "cdecl"):
    SetpointCommandScaled_isSelect = _libs["libiec60870.so"].get("SetpointCommandScaled_isSelect", "cdecl")
    SetpointCommandScaled_isSelect.argtypes = [SetpointCommandScaled]
    SetpointCommandScaled_isSelect.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1229
class struct_sSetpointCommandShort(Structure):
    pass

SetpointCommandShort = POINTER(struct_sSetpointCommandShort)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1229

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1232
if _libs["libiec60870.so"].has("SetpointCommandShort_destroy", "cdecl"):
    SetpointCommandShort_destroy = _libs["libiec60870.so"].get("SetpointCommandShort_destroy", "cdecl")
    SetpointCommandShort_destroy.argtypes = [SetpointCommandShort]
    SetpointCommandShort_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1246
if _libs["libiec60870.so"].has("SetpointCommandShort_create", "cdecl"):
    SetpointCommandShort_create = _libs["libiec60870.so"].get("SetpointCommandShort_create", "cdecl")
    SetpointCommandShort_create.argtypes = [SetpointCommandShort, c_int, c_float, c_bool, c_int]
    SetpointCommandShort_create.restype = SetpointCommandShort

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1249
if _libs["libiec60870.so"].has("SetpointCommandShort_getValue", "cdecl"):
    SetpointCommandShort_getValue = _libs["libiec60870.so"].get("SetpointCommandShort_getValue", "cdecl")
    SetpointCommandShort_getValue.argtypes = [SetpointCommandShort]
    SetpointCommandShort_getValue.restype = c_float

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1252
if _libs["libiec60870.so"].has("SetpointCommandShort_getQL", "cdecl"):
    SetpointCommandShort_getQL = _libs["libiec60870.so"].get("SetpointCommandShort_getQL", "cdecl")
    SetpointCommandShort_getQL.argtypes = [SetpointCommandShort]
    SetpointCommandShort_getQL.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1260
if _libs["libiec60870.so"].has("SetpointCommandShort_isSelect", "cdecl"):
    SetpointCommandShort_isSelect = _libs["libiec60870.so"].get("SetpointCommandShort_isSelect", "cdecl")
    SetpointCommandShort_isSelect.argtypes = [SetpointCommandShort]
    SetpointCommandShort_isSelect.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1266
class struct_sBitstring32Command(Structure):
    pass

Bitstring32Command = POINTER(struct_sBitstring32Command)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1266

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1269
if _libs["libiec60870.so"].has("Bitstring32Command_create", "cdecl"):
    Bitstring32Command_create = _libs["libiec60870.so"].get("Bitstring32Command_create", "cdecl")
    Bitstring32Command_create.argtypes = [Bitstring32Command, c_int, uint32_t]
    Bitstring32Command_create.restype = Bitstring32Command

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1272
if _libs["libiec60870.so"].has("Bitstring32Command_destroy", "cdecl"):
    Bitstring32Command_destroy = _libs["libiec60870.so"].get("Bitstring32Command_destroy", "cdecl")
    Bitstring32Command_destroy.argtypes = [Bitstring32Command]
    Bitstring32Command_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1275
if _libs["libiec60870.so"].has("Bitstring32Command_getValue", "cdecl"):
    Bitstring32Command_getValue = _libs["libiec60870.so"].get("Bitstring32Command_getValue", "cdecl")
    Bitstring32Command_getValue.argtypes = [Bitstring32Command]
    Bitstring32Command_getValue.restype = uint32_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1281
class struct_sInterrogationCommand(Structure):
    pass

InterrogationCommand = POINTER(struct_sInterrogationCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1281

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1284
if _libs["libiec60870.so"].has("InterrogationCommand_create", "cdecl"):
    InterrogationCommand_create = _libs["libiec60870.so"].get("InterrogationCommand_create", "cdecl")
    InterrogationCommand_create.argtypes = [InterrogationCommand, c_int, uint8_t]
    InterrogationCommand_create.restype = InterrogationCommand

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1287
if _libs["libiec60870.so"].has("InterrogationCommand_destroy", "cdecl"):
    InterrogationCommand_destroy = _libs["libiec60870.so"].get("InterrogationCommand_destroy", "cdecl")
    InterrogationCommand_destroy.argtypes = [InterrogationCommand]
    InterrogationCommand_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1290
if _libs["libiec60870.so"].has("InterrogationCommand_getQOI", "cdecl"):
    InterrogationCommand_getQOI = _libs["libiec60870.so"].get("InterrogationCommand_getQOI", "cdecl")
    InterrogationCommand_getQOI.argtypes = [InterrogationCommand]
    InterrogationCommand_getQOI.restype = uint8_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1296
class struct_sReadCommand(Structure):
    pass

ReadCommand = POINTER(struct_sReadCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1296

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1299
if _libs["libiec60870.so"].has("ReadCommand_create", "cdecl"):
    ReadCommand_create = _libs["libiec60870.so"].get("ReadCommand_create", "cdecl")
    ReadCommand_create.argtypes = [ReadCommand, c_int]
    ReadCommand_create.restype = ReadCommand

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1302
if _libs["libiec60870.so"].has("ReadCommand_destroy", "cdecl"):
    ReadCommand_destroy = _libs["libiec60870.so"].get("ReadCommand_destroy", "cdecl")
    ReadCommand_destroy.argtypes = [ReadCommand]
    ReadCommand_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1308
class struct_sClockSynchronizationCommand(Structure):
    pass

ClockSynchronizationCommand = POINTER(struct_sClockSynchronizationCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1308

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1311
if _libs["libiec60870.so"].has("ClockSynchronizationCommand_create", "cdecl"):
    ClockSynchronizationCommand_create = _libs["libiec60870.so"].get("ClockSynchronizationCommand_create", "cdecl")
    ClockSynchronizationCommand_create.argtypes = [ClockSynchronizationCommand, c_int, CP56Time2a]
    ClockSynchronizationCommand_create.restype = ClockSynchronizationCommand

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1314
if _libs["libiec60870.so"].has("ClockSynchronizationCommand_destroy", "cdecl"):
    ClockSynchronizationCommand_destroy = _libs["libiec60870.so"].get("ClockSynchronizationCommand_destroy", "cdecl")
    ClockSynchronizationCommand_destroy.argtypes = [ClockSynchronizationCommand]
    ClockSynchronizationCommand_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1317
if _libs["libiec60870.so"].has("ClockSynchronizationCommand_getTime", "cdecl"):
    ClockSynchronizationCommand_getTime = _libs["libiec60870.so"].get("ClockSynchronizationCommand_getTime", "cdecl")
    ClockSynchronizationCommand_getTime.argtypes = [ClockSynchronizationCommand]
    ClockSynchronizationCommand_getTime.restype = CP56Time2a

ParameterNormalizedValue = POINTER(struct_sMeasuredValueNormalized)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1323

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1326
if _libs["libiec60870.so"].has("ParameterNormalizedValue_destroy", "cdecl"):
    ParameterNormalizedValue_destroy = _libs["libiec60870.so"].get("ParameterNormalizedValue_destroy", "cdecl")
    ParameterNormalizedValue_destroy.argtypes = [ParameterNormalizedValue]
    ParameterNormalizedValue_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1351
if _libs["libiec60870.so"].has("ParameterNormalizedValue_create", "cdecl"):
    ParameterNormalizedValue_create = _libs["libiec60870.so"].get("ParameterNormalizedValue_create", "cdecl")
    ParameterNormalizedValue_create.argtypes = [ParameterNormalizedValue, c_int, c_float, QualifierOfParameterMV]
    ParameterNormalizedValue_create.restype = ParameterNormalizedValue

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1354
if _libs["libiec60870.so"].has("ParameterNormalizedValue_getValue", "cdecl"):
    ParameterNormalizedValue_getValue = _libs["libiec60870.so"].get("ParameterNormalizedValue_getValue", "cdecl")
    ParameterNormalizedValue_getValue.argtypes = [ParameterNormalizedValue]
    ParameterNormalizedValue_getValue.restype = c_float

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1357
if _libs["libiec60870.so"].has("ParameterNormalizedValue_setValue", "cdecl"):
    ParameterNormalizedValue_setValue = _libs["libiec60870.so"].get("ParameterNormalizedValue_setValue", "cdecl")
    ParameterNormalizedValue_setValue.argtypes = [ParameterNormalizedValue, c_float]
    ParameterNormalizedValue_setValue.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1365
if _libs["libiec60870.so"].has("ParameterNormalizedValue_getQPM", "cdecl"):
    ParameterNormalizedValue_getQPM = _libs["libiec60870.so"].get("ParameterNormalizedValue_getQPM", "cdecl")
    ParameterNormalizedValue_getQPM.argtypes = [ParameterNormalizedValue]
    ParameterNormalizedValue_getQPM.restype = QualifierOfParameterMV

ParameterScaledValue = POINTER(struct_sMeasuredValueScaled)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1371

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1374
if _libs["libiec60870.so"].has("ParameterScaledValue_destroy", "cdecl"):
    ParameterScaledValue_destroy = _libs["libiec60870.so"].get("ParameterScaledValue_destroy", "cdecl")
    ParameterScaledValue_destroy.argtypes = [ParameterScaledValue]
    ParameterScaledValue_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1399
if _libs["libiec60870.so"].has("ParameterScaledValue_create", "cdecl"):
    ParameterScaledValue_create = _libs["libiec60870.so"].get("ParameterScaledValue_create", "cdecl")
    ParameterScaledValue_create.argtypes = [ParameterScaledValue, c_int, c_int, QualifierOfParameterMV]
    ParameterScaledValue_create.restype = ParameterScaledValue

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1402
if _libs["libiec60870.so"].has("ParameterScaledValue_getValue", "cdecl"):
    ParameterScaledValue_getValue = _libs["libiec60870.so"].get("ParameterScaledValue_getValue", "cdecl")
    ParameterScaledValue_getValue.argtypes = [ParameterScaledValue]
    ParameterScaledValue_getValue.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1405
if _libs["libiec60870.so"].has("ParameterScaledValue_setValue", "cdecl"):
    ParameterScaledValue_setValue = _libs["libiec60870.so"].get("ParameterScaledValue_setValue", "cdecl")
    ParameterScaledValue_setValue.argtypes = [ParameterScaledValue, c_int]
    ParameterScaledValue_setValue.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1413
if _libs["libiec60870.so"].has("ParameterScaledValue_getQPM", "cdecl"):
    ParameterScaledValue_getQPM = _libs["libiec60870.so"].get("ParameterScaledValue_getQPM", "cdecl")
    ParameterScaledValue_getQPM.argtypes = [ParameterScaledValue]
    ParameterScaledValue_getQPM.restype = QualifierOfParameterMV

ParameterFloatValue = POINTER(struct_sMeasuredValueShort)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1419

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1422
if _libs["libiec60870.so"].has("ParameterFloatValue_destroy", "cdecl"):
    ParameterFloatValue_destroy = _libs["libiec60870.so"].get("ParameterFloatValue_destroy", "cdecl")
    ParameterFloatValue_destroy.argtypes = [ParameterFloatValue]
    ParameterFloatValue_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1447
if _libs["libiec60870.so"].has("ParameterFloatValue_create", "cdecl"):
    ParameterFloatValue_create = _libs["libiec60870.so"].get("ParameterFloatValue_create", "cdecl")
    ParameterFloatValue_create.argtypes = [ParameterFloatValue, c_int, c_float, QualifierOfParameterMV]
    ParameterFloatValue_create.restype = ParameterFloatValue

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1450
if _libs["libiec60870.so"].has("ParameterFloatValue_getValue", "cdecl"):
    ParameterFloatValue_getValue = _libs["libiec60870.so"].get("ParameterFloatValue_getValue", "cdecl")
    ParameterFloatValue_getValue.argtypes = [ParameterFloatValue]
    ParameterFloatValue_getValue.restype = c_float

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1453
if _libs["libiec60870.so"].has("ParameterFloatValue_setValue", "cdecl"):
    ParameterFloatValue_setValue = _libs["libiec60870.so"].get("ParameterFloatValue_setValue", "cdecl")
    ParameterFloatValue_setValue.argtypes = [ParameterFloatValue, c_float]
    ParameterFloatValue_setValue.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1461
if _libs["libiec60870.so"].has("ParameterFloatValue_getQPM", "cdecl"):
    ParameterFloatValue_getQPM = _libs["libiec60870.so"].get("ParameterFloatValue_getQPM", "cdecl")
    ParameterFloatValue_getQPM.argtypes = [ParameterFloatValue]
    ParameterFloatValue_getQPM.restype = QualifierOfParameterMV

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1467
class struct_sParameterActivation(Structure):
    pass

ParameterActivation = POINTER(struct_sParameterActivation)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1467

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1470
if _libs["libiec60870.so"].has("ParameterActivation_destroy", "cdecl"):
    ParameterActivation_destroy = _libs["libiec60870.so"].get("ParameterActivation_destroy", "cdecl")
    ParameterActivation_destroy.argtypes = [ParameterActivation]
    ParameterActivation_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1482
if _libs["libiec60870.so"].has("ParameterActivation_create", "cdecl"):
    ParameterActivation_create = _libs["libiec60870.so"].get("ParameterActivation_create", "cdecl")
    ParameterActivation_create.argtypes = [ParameterActivation, c_int, QualifierOfParameterActivation]
    ParameterActivation_create.restype = ParameterActivation

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1490
if _libs["libiec60870.so"].has("ParameterActivation_getQuality", "cdecl"):
    ParameterActivation_getQuality = _libs["libiec60870.so"].get("ParameterActivation_getQuality", "cdecl")
    ParameterActivation_getQuality.argtypes = [ParameterActivation]
    ParameterActivation_getQuality.restype = QualifierOfParameterActivation

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1496
class struct_sEventOfProtectionEquipmentWithCP56Time2a(Structure):
    pass

EventOfProtectionEquipmentWithCP56Time2a = POINTER(struct_sEventOfProtectionEquipmentWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1496

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1499
if _libs["libiec60870.so"].has("EventOfProtectionEquipmentWithCP56Time2a_destroy", "cdecl"):
    EventOfProtectionEquipmentWithCP56Time2a_destroy = _libs["libiec60870.so"].get("EventOfProtectionEquipmentWithCP56Time2a_destroy", "cdecl")
    EventOfProtectionEquipmentWithCP56Time2a_destroy.argtypes = [EventOfProtectionEquipmentWithCP56Time2a]
    EventOfProtectionEquipmentWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1502
if _libs["libiec60870.so"].has("EventOfProtectionEquipmentWithCP56Time2a_create", "cdecl"):
    EventOfProtectionEquipmentWithCP56Time2a_create = _libs["libiec60870.so"].get("EventOfProtectionEquipmentWithCP56Time2a_create", "cdecl")
    EventOfProtectionEquipmentWithCP56Time2a_create.argtypes = [EventOfProtectionEquipmentWithCP56Time2a, c_int, SingleEvent, CP16Time2a, CP56Time2a]
    EventOfProtectionEquipmentWithCP56Time2a_create.restype = EventOfProtectionEquipmentWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1506
if _libs["libiec60870.so"].has("EventOfProtectionEquipmentWithCP56Time2a_getEvent", "cdecl"):
    EventOfProtectionEquipmentWithCP56Time2a_getEvent = _libs["libiec60870.so"].get("EventOfProtectionEquipmentWithCP56Time2a_getEvent", "cdecl")
    EventOfProtectionEquipmentWithCP56Time2a_getEvent.argtypes = [EventOfProtectionEquipmentWithCP56Time2a]
    EventOfProtectionEquipmentWithCP56Time2a_getEvent.restype = SingleEvent

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1509
if _libs["libiec60870.so"].has("EventOfProtectionEquipmentWithCP56Time2a_getElapsedTime", "cdecl"):
    EventOfProtectionEquipmentWithCP56Time2a_getElapsedTime = _libs["libiec60870.so"].get("EventOfProtectionEquipmentWithCP56Time2a_getElapsedTime", "cdecl")
    EventOfProtectionEquipmentWithCP56Time2a_getElapsedTime.argtypes = [EventOfProtectionEquipmentWithCP56Time2a]
    EventOfProtectionEquipmentWithCP56Time2a_getElapsedTime.restype = CP16Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1512
if _libs["libiec60870.so"].has("EventOfProtectionEquipmentWithCP56Time2a_getTimestamp", "cdecl"):
    EventOfProtectionEquipmentWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("EventOfProtectionEquipmentWithCP56Time2a_getTimestamp", "cdecl")
    EventOfProtectionEquipmentWithCP56Time2a_getTimestamp.argtypes = [EventOfProtectionEquipmentWithCP56Time2a]
    EventOfProtectionEquipmentWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1518
class struct_sPackedStartEventsOfProtectionEquipmentWithCP56Time2a(Structure):
    pass

PackedStartEventsOfProtectionEquipmentWithCP56Time2a = POINTER(struct_sPackedStartEventsOfProtectionEquipmentWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1518

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1521
if _libs["libiec60870.so"].has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_destroy", "cdecl"):
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_destroy = _libs["libiec60870.so"].get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_destroy", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_destroy.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1524
if _libs["libiec60870.so"].has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_create", "cdecl"):
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_create = _libs["libiec60870.so"].get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_create", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_create.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a, c_int, StartEvent, QualityDescriptorP, CP16Time2a, CP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_create.restype = PackedStartEventsOfProtectionEquipmentWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1528
if _libs["libiec60870.so"].has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getEvent", "cdecl"):
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getEvent = _libs["libiec60870.so"].get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getEvent", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getEvent.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getEvent.restype = StartEvent

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1531
if _libs["libiec60870.so"].has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getQuality", "cdecl"):
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getQuality = _libs["libiec60870.so"].get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getQuality", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getQuality.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getQuality.restype = QualityDescriptorP

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1534
if _libs["libiec60870.so"].has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getElapsedTime", "cdecl"):
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getElapsedTime = _libs["libiec60870.so"].get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getElapsedTime", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getElapsedTime.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getElapsedTime.restype = CP16Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1537
if _libs["libiec60870.so"].has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getTimestamp", "cdecl"):
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getTimestamp", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getTimestamp.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1543
class struct_sPackedOutputCircuitInfoWithCP56Time2a(Structure):
    pass

PackedOutputCircuitInfoWithCP56Time2a = POINTER(struct_sPackedOutputCircuitInfoWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1543

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1546
if _libs["libiec60870.so"].has("PackedOutputCircuitInfoWithCP56Time2a_destroy", "cdecl"):
    PackedOutputCircuitInfoWithCP56Time2a_destroy = _libs["libiec60870.so"].get("PackedOutputCircuitInfoWithCP56Time2a_destroy", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_destroy.argtypes = [PackedOutputCircuitInfoWithCP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1549
if _libs["libiec60870.so"].has("PackedOutputCircuitInfoWithCP56Time2a_create", "cdecl"):
    PackedOutputCircuitInfoWithCP56Time2a_create = _libs["libiec60870.so"].get("PackedOutputCircuitInfoWithCP56Time2a_create", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_create.argtypes = [PackedOutputCircuitInfoWithCP56Time2a, c_int, OutputCircuitInfo, QualityDescriptorP, CP16Time2a, CP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_create.restype = PackedOutputCircuitInfoWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1553
if _libs["libiec60870.so"].has("PackedOutputCircuitInfoWithCP56Time2a_getOCI", "cdecl"):
    PackedOutputCircuitInfoWithCP56Time2a_getOCI = _libs["libiec60870.so"].get("PackedOutputCircuitInfoWithCP56Time2a_getOCI", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_getOCI.argtypes = [PackedOutputCircuitInfoWithCP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_getOCI.restype = OutputCircuitInfo

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1556
if _libs["libiec60870.so"].has("PackedOutputCircuitInfoWithCP56Time2a_getQuality", "cdecl"):
    PackedOutputCircuitInfoWithCP56Time2a_getQuality = _libs["libiec60870.so"].get("PackedOutputCircuitInfoWithCP56Time2a_getQuality", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_getQuality.argtypes = [PackedOutputCircuitInfoWithCP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_getQuality.restype = QualityDescriptorP

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1559
if _libs["libiec60870.so"].has("PackedOutputCircuitInfoWithCP56Time2a_getOperatingTime", "cdecl"):
    PackedOutputCircuitInfoWithCP56Time2a_getOperatingTime = _libs["libiec60870.so"].get("PackedOutputCircuitInfoWithCP56Time2a_getOperatingTime", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_getOperatingTime.argtypes = [PackedOutputCircuitInfoWithCP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_getOperatingTime.restype = CP16Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1562
if _libs["libiec60870.so"].has("PackedOutputCircuitInfoWithCP56Time2a_getTimestamp", "cdecl"):
    PackedOutputCircuitInfoWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("PackedOutputCircuitInfoWithCP56Time2a_getTimestamp", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_getTimestamp.argtypes = [PackedOutputCircuitInfoWithCP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1568
class struct_sDoubleCommandWithCP56Time2a(Structure):
    pass

DoubleCommandWithCP56Time2a = POINTER(struct_sDoubleCommandWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1568

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1571
if _libs["libiec60870.so"].has("DoubleCommandWithCP56Time2a_destroy", "cdecl"):
    DoubleCommandWithCP56Time2a_destroy = _libs["libiec60870.so"].get("DoubleCommandWithCP56Time2a_destroy", "cdecl")
    DoubleCommandWithCP56Time2a_destroy.argtypes = [DoubleCommandWithCP56Time2a]
    DoubleCommandWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1574
if _libs["libiec60870.so"].has("DoubleCommandWithCP56Time2a_create", "cdecl"):
    DoubleCommandWithCP56Time2a_create = _libs["libiec60870.so"].get("DoubleCommandWithCP56Time2a_create", "cdecl")
    DoubleCommandWithCP56Time2a_create.argtypes = [DoubleCommandWithCP56Time2a, c_int, c_int, c_bool, c_int, CP56Time2a]
    DoubleCommandWithCP56Time2a_create.restype = DoubleCommandWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1577
if _libs["libiec60870.so"].has("DoubleCommandWithCP56Time2a_getQU", "cdecl"):
    DoubleCommandWithCP56Time2a_getQU = _libs["libiec60870.so"].get("DoubleCommandWithCP56Time2a_getQU", "cdecl")
    DoubleCommandWithCP56Time2a_getQU.argtypes = [DoubleCommandWithCP56Time2a]
    DoubleCommandWithCP56Time2a_getQU.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1580
if _libs["libiec60870.so"].has("DoubleCommandWithCP56Time2a_getState", "cdecl"):
    DoubleCommandWithCP56Time2a_getState = _libs["libiec60870.so"].get("DoubleCommandWithCP56Time2a_getState", "cdecl")
    DoubleCommandWithCP56Time2a_getState.argtypes = [DoubleCommandWithCP56Time2a]
    DoubleCommandWithCP56Time2a_getState.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1583
if _libs["libiec60870.so"].has("DoubleCommandWithCP56Time2a_isSelect", "cdecl"):
    DoubleCommandWithCP56Time2a_isSelect = _libs["libiec60870.so"].get("DoubleCommandWithCP56Time2a_isSelect", "cdecl")
    DoubleCommandWithCP56Time2a_isSelect.argtypes = [DoubleCommandWithCP56Time2a]
    DoubleCommandWithCP56Time2a_isSelect.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1586
if _libs["libiec60870.so"].has("DoubleCommandWithCP56Time2a_getTimestamp", "cdecl"):
    DoubleCommandWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("DoubleCommandWithCP56Time2a_getTimestamp", "cdecl")
    DoubleCommandWithCP56Time2a_getTimestamp.argtypes = [DoubleCommandWithCP56Time2a]
    DoubleCommandWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1592
class struct_sStepCommandWithCP56Time2a(Structure):
    pass

StepCommandWithCP56Time2a = POINTER(struct_sStepCommandWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1592

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1595
if _libs["libiec60870.so"].has("StepCommandWithCP56Time2a_destroy", "cdecl"):
    StepCommandWithCP56Time2a_destroy = _libs["libiec60870.so"].get("StepCommandWithCP56Time2a_destroy", "cdecl")
    StepCommandWithCP56Time2a_destroy.argtypes = [StepCommandWithCP56Time2a]
    StepCommandWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1598
if _libs["libiec60870.so"].has("StepCommandWithCP56Time2a_create", "cdecl"):
    StepCommandWithCP56Time2a_create = _libs["libiec60870.so"].get("StepCommandWithCP56Time2a_create", "cdecl")
    StepCommandWithCP56Time2a_create.argtypes = [StepCommandWithCP56Time2a, c_int, StepCommandValue, c_bool, c_int, CP56Time2a]
    StepCommandWithCP56Time2a_create.restype = StepCommandWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1601
if _libs["libiec60870.so"].has("StepCommandWithCP56Time2a_getQU", "cdecl"):
    StepCommandWithCP56Time2a_getQU = _libs["libiec60870.so"].get("StepCommandWithCP56Time2a_getQU", "cdecl")
    StepCommandWithCP56Time2a_getQU.argtypes = [StepCommandWithCP56Time2a]
    StepCommandWithCP56Time2a_getQU.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1604
if _libs["libiec60870.so"].has("StepCommandWithCP56Time2a_getState", "cdecl"):
    StepCommandWithCP56Time2a_getState = _libs["libiec60870.so"].get("StepCommandWithCP56Time2a_getState", "cdecl")
    StepCommandWithCP56Time2a_getState.argtypes = [StepCommandWithCP56Time2a]
    StepCommandWithCP56Time2a_getState.restype = StepCommandValue

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1607
if _libs["libiec60870.so"].has("StepCommandWithCP56Time2a_isSelect", "cdecl"):
    StepCommandWithCP56Time2a_isSelect = _libs["libiec60870.so"].get("StepCommandWithCP56Time2a_isSelect", "cdecl")
    StepCommandWithCP56Time2a_isSelect.argtypes = [StepCommandWithCP56Time2a]
    StepCommandWithCP56Time2a_isSelect.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1610
if _libs["libiec60870.so"].has("StepCommandWithCP56Time2a_getTimestamp", "cdecl"):
    StepCommandWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("StepCommandWithCP56Time2a_getTimestamp", "cdecl")
    StepCommandWithCP56Time2a_getTimestamp.argtypes = [StepCommandWithCP56Time2a]
    StepCommandWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1616
class struct_sSetpointCommandNormalizedWithCP56Time2a(Structure):
    pass

SetpointCommandNormalizedWithCP56Time2a = POINTER(struct_sSetpointCommandNormalizedWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1616

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1619
if _libs["libiec60870.so"].has("SetpointCommandNormalizedWithCP56Time2a_destroy", "cdecl"):
    SetpointCommandNormalizedWithCP56Time2a_destroy = _libs["libiec60870.so"].get("SetpointCommandNormalizedWithCP56Time2a_destroy", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_destroy.argtypes = [SetpointCommandNormalizedWithCP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1622
if _libs["libiec60870.so"].has("SetpointCommandNormalizedWithCP56Time2a_create", "cdecl"):
    SetpointCommandNormalizedWithCP56Time2a_create = _libs["libiec60870.so"].get("SetpointCommandNormalizedWithCP56Time2a_create", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_create.argtypes = [SetpointCommandNormalizedWithCP56Time2a, c_int, c_float, c_bool, c_int, CP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_create.restype = SetpointCommandNormalizedWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1625
if _libs["libiec60870.so"].has("SetpointCommandNormalizedWithCP56Time2a_getValue", "cdecl"):
    SetpointCommandNormalizedWithCP56Time2a_getValue = _libs["libiec60870.so"].get("SetpointCommandNormalizedWithCP56Time2a_getValue", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_getValue.argtypes = [SetpointCommandNormalizedWithCP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_getValue.restype = c_float

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1628
if _libs["libiec60870.so"].has("SetpointCommandNormalizedWithCP56Time2a_getQL", "cdecl"):
    SetpointCommandNormalizedWithCP56Time2a_getQL = _libs["libiec60870.so"].get("SetpointCommandNormalizedWithCP56Time2a_getQL", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_getQL.argtypes = [SetpointCommandNormalizedWithCP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_getQL.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1631
if _libs["libiec60870.so"].has("SetpointCommandNormalizedWithCP56Time2a_isSelect", "cdecl"):
    SetpointCommandNormalizedWithCP56Time2a_isSelect = _libs["libiec60870.so"].get("SetpointCommandNormalizedWithCP56Time2a_isSelect", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_isSelect.argtypes = [SetpointCommandNormalizedWithCP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_isSelect.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1634
if _libs["libiec60870.so"].has("SetpointCommandNormalizedWithCP56Time2a_getTimestamp", "cdecl"):
    SetpointCommandNormalizedWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("SetpointCommandNormalizedWithCP56Time2a_getTimestamp", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_getTimestamp.argtypes = [SetpointCommandNormalizedWithCP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1640
class struct_sSetpointCommandScaledWithCP56Time2a(Structure):
    pass

SetpointCommandScaledWithCP56Time2a = POINTER(struct_sSetpointCommandScaledWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1640

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1643
if _libs["libiec60870.so"].has("SetpointCommandScaledWithCP56Time2a_destroy", "cdecl"):
    SetpointCommandScaledWithCP56Time2a_destroy = _libs["libiec60870.so"].get("SetpointCommandScaledWithCP56Time2a_destroy", "cdecl")
    SetpointCommandScaledWithCP56Time2a_destroy.argtypes = [SetpointCommandScaledWithCP56Time2a]
    SetpointCommandScaledWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1646
if _libs["libiec60870.so"].has("SetpointCommandScaledWithCP56Time2a_create", "cdecl"):
    SetpointCommandScaledWithCP56Time2a_create = _libs["libiec60870.so"].get("SetpointCommandScaledWithCP56Time2a_create", "cdecl")
    SetpointCommandScaledWithCP56Time2a_create.argtypes = [SetpointCommandScaledWithCP56Time2a, c_int, c_int, c_bool, c_int, CP56Time2a]
    SetpointCommandScaledWithCP56Time2a_create.restype = SetpointCommandScaledWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1649
if _libs["libiec60870.so"].has("SetpointCommandScaledWithCP56Time2a_getValue", "cdecl"):
    SetpointCommandScaledWithCP56Time2a_getValue = _libs["libiec60870.so"].get("SetpointCommandScaledWithCP56Time2a_getValue", "cdecl")
    SetpointCommandScaledWithCP56Time2a_getValue.argtypes = [SetpointCommandScaledWithCP56Time2a]
    SetpointCommandScaledWithCP56Time2a_getValue.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1652
if _libs["libiec60870.so"].has("SetpointCommandScaledWithCP56Time2a_getQL", "cdecl"):
    SetpointCommandScaledWithCP56Time2a_getQL = _libs["libiec60870.so"].get("SetpointCommandScaledWithCP56Time2a_getQL", "cdecl")
    SetpointCommandScaledWithCP56Time2a_getQL.argtypes = [SetpointCommandScaledWithCP56Time2a]
    SetpointCommandScaledWithCP56Time2a_getQL.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1655
if _libs["libiec60870.so"].has("SetpointCommandScaledWithCP56Time2a_isSelect", "cdecl"):
    SetpointCommandScaledWithCP56Time2a_isSelect = _libs["libiec60870.so"].get("SetpointCommandScaledWithCP56Time2a_isSelect", "cdecl")
    SetpointCommandScaledWithCP56Time2a_isSelect.argtypes = [SetpointCommandScaledWithCP56Time2a]
    SetpointCommandScaledWithCP56Time2a_isSelect.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1658
if _libs["libiec60870.so"].has("SetpointCommandScaledWithCP56Time2a_getTimestamp", "cdecl"):
    SetpointCommandScaledWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("SetpointCommandScaledWithCP56Time2a_getTimestamp", "cdecl")
    SetpointCommandScaledWithCP56Time2a_getTimestamp.argtypes = [SetpointCommandScaledWithCP56Time2a]
    SetpointCommandScaledWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1664
class struct_sSetpointCommandShortWithCP56Time2a(Structure):
    pass

SetpointCommandShortWithCP56Time2a = POINTER(struct_sSetpointCommandShortWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1664

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1667
if _libs["libiec60870.so"].has("SetpointCommandShortWithCP56Time2a_destroy", "cdecl"):
    SetpointCommandShortWithCP56Time2a_destroy = _libs["libiec60870.so"].get("SetpointCommandShortWithCP56Time2a_destroy", "cdecl")
    SetpointCommandShortWithCP56Time2a_destroy.argtypes = [SetpointCommandShortWithCP56Time2a]
    SetpointCommandShortWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1670
if _libs["libiec60870.so"].has("SetpointCommandShortWithCP56Time2a_create", "cdecl"):
    SetpointCommandShortWithCP56Time2a_create = _libs["libiec60870.so"].get("SetpointCommandShortWithCP56Time2a_create", "cdecl")
    SetpointCommandShortWithCP56Time2a_create.argtypes = [SetpointCommandShortWithCP56Time2a, c_int, c_float, c_bool, c_int, CP56Time2a]
    SetpointCommandShortWithCP56Time2a_create.restype = SetpointCommandShortWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1673
if _libs["libiec60870.so"].has("SetpointCommandShortWithCP56Time2a_getValue", "cdecl"):
    SetpointCommandShortWithCP56Time2a_getValue = _libs["libiec60870.so"].get("SetpointCommandShortWithCP56Time2a_getValue", "cdecl")
    SetpointCommandShortWithCP56Time2a_getValue.argtypes = [SetpointCommandShortWithCP56Time2a]
    SetpointCommandShortWithCP56Time2a_getValue.restype = c_float

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1676
if _libs["libiec60870.so"].has("SetpointCommandShortWithCP56Time2a_getQL", "cdecl"):
    SetpointCommandShortWithCP56Time2a_getQL = _libs["libiec60870.so"].get("SetpointCommandShortWithCP56Time2a_getQL", "cdecl")
    SetpointCommandShortWithCP56Time2a_getQL.argtypes = [SetpointCommandShortWithCP56Time2a]
    SetpointCommandShortWithCP56Time2a_getQL.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1679
if _libs["libiec60870.so"].has("SetpointCommandShortWithCP56Time2a_isSelect", "cdecl"):
    SetpointCommandShortWithCP56Time2a_isSelect = _libs["libiec60870.so"].get("SetpointCommandShortWithCP56Time2a_isSelect", "cdecl")
    SetpointCommandShortWithCP56Time2a_isSelect.argtypes = [SetpointCommandShortWithCP56Time2a]
    SetpointCommandShortWithCP56Time2a_isSelect.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1682
if _libs["libiec60870.so"].has("SetpointCommandShortWithCP56Time2a_getTimestamp", "cdecl"):
    SetpointCommandShortWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("SetpointCommandShortWithCP56Time2a_getTimestamp", "cdecl")
    SetpointCommandShortWithCP56Time2a_getTimestamp.argtypes = [SetpointCommandShortWithCP56Time2a]
    SetpointCommandShortWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1688
class struct_sBitstring32CommandWithCP56Time2a(Structure):
    pass

Bitstring32CommandWithCP56Time2a = POINTER(struct_sBitstring32CommandWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1688

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1691
if _libs["libiec60870.so"].has("Bitstring32CommandWithCP56Time2a_create", "cdecl"):
    Bitstring32CommandWithCP56Time2a_create = _libs["libiec60870.so"].get("Bitstring32CommandWithCP56Time2a_create", "cdecl")
    Bitstring32CommandWithCP56Time2a_create.argtypes = [Bitstring32CommandWithCP56Time2a, c_int, uint32_t, CP56Time2a]
    Bitstring32CommandWithCP56Time2a_create.restype = Bitstring32CommandWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1694
if _libs["libiec60870.so"].has("Bitstring32CommandWithCP56Time2a_destroy", "cdecl"):
    Bitstring32CommandWithCP56Time2a_destroy = _libs["libiec60870.so"].get("Bitstring32CommandWithCP56Time2a_destroy", "cdecl")
    Bitstring32CommandWithCP56Time2a_destroy.argtypes = [Bitstring32CommandWithCP56Time2a]
    Bitstring32CommandWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1697
if _libs["libiec60870.so"].has("Bitstring32CommandWithCP56Time2a_getValue", "cdecl"):
    Bitstring32CommandWithCP56Time2a_getValue = _libs["libiec60870.so"].get("Bitstring32CommandWithCP56Time2a_getValue", "cdecl")
    Bitstring32CommandWithCP56Time2a_getValue.argtypes = [Bitstring32CommandWithCP56Time2a]
    Bitstring32CommandWithCP56Time2a_getValue.restype = uint32_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1700
if _libs["libiec60870.so"].has("Bitstring32CommandWithCP56Time2a_getTimestamp", "cdecl"):
    Bitstring32CommandWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("Bitstring32CommandWithCP56Time2a_getTimestamp", "cdecl")
    Bitstring32CommandWithCP56Time2a_getTimestamp.argtypes = [Bitstring32CommandWithCP56Time2a]
    Bitstring32CommandWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1707
class struct_sCounterInterrogationCommand(Structure):
    pass

CounterInterrogationCommand = POINTER(struct_sCounterInterrogationCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1707

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1710
if _libs["libiec60870.so"].has("CounterInterrogationCommand_create", "cdecl"):
    CounterInterrogationCommand_create = _libs["libiec60870.so"].get("CounterInterrogationCommand_create", "cdecl")
    CounterInterrogationCommand_create.argtypes = [CounterInterrogationCommand, c_int, QualifierOfCIC]
    CounterInterrogationCommand_create.restype = CounterInterrogationCommand

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1713
if _libs["libiec60870.so"].has("CounterInterrogationCommand_destroy", "cdecl"):
    CounterInterrogationCommand_destroy = _libs["libiec60870.so"].get("CounterInterrogationCommand_destroy", "cdecl")
    CounterInterrogationCommand_destroy.argtypes = [CounterInterrogationCommand]
    CounterInterrogationCommand_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1716
if _libs["libiec60870.so"].has("CounterInterrogationCommand_getQCC", "cdecl"):
    CounterInterrogationCommand_getQCC = _libs["libiec60870.so"].get("CounterInterrogationCommand_getQCC", "cdecl")
    CounterInterrogationCommand_getQCC.argtypes = [CounterInterrogationCommand]
    CounterInterrogationCommand_getQCC.restype = QualifierOfCIC

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1722
class struct_sTestCommand(Structure):
    pass

TestCommand = POINTER(struct_sTestCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1722

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1725
if _libs["libiec60870.so"].has("TestCommand_create", "cdecl"):
    TestCommand_create = _libs["libiec60870.so"].get("TestCommand_create", "cdecl")
    TestCommand_create.argtypes = [TestCommand]
    TestCommand_create.restype = TestCommand

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1728
if _libs["libiec60870.so"].has("TestCommand_destroy", "cdecl"):
    TestCommand_destroy = _libs["libiec60870.so"].get("TestCommand_destroy", "cdecl")
    TestCommand_destroy.argtypes = [TestCommand]
    TestCommand_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1731
if _libs["libiec60870.so"].has("TestCommand_isValid", "cdecl"):
    TestCommand_isValid = _libs["libiec60870.so"].get("TestCommand_isValid", "cdecl")
    TestCommand_isValid.argtypes = [TestCommand]
    TestCommand_isValid.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1737
class struct_sTestCommandWithCP56Time2a(Structure):
    pass

TestCommandWithCP56Time2a = POINTER(struct_sTestCommandWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1737

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1749
if _libs["libiec60870.so"].has("TestCommandWithCP56Time2a_create", "cdecl"):
    TestCommandWithCP56Time2a_create = _libs["libiec60870.so"].get("TestCommandWithCP56Time2a_create", "cdecl")
    TestCommandWithCP56Time2a_create.argtypes = [TestCommandWithCP56Time2a, uint16_t, CP56Time2a]
    TestCommandWithCP56Time2a_create.restype = TestCommandWithCP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1752
if _libs["libiec60870.so"].has("TestCommandWithCP56Time2a_destroy", "cdecl"):
    TestCommandWithCP56Time2a_destroy = _libs["libiec60870.so"].get("TestCommandWithCP56Time2a_destroy", "cdecl")
    TestCommandWithCP56Time2a_destroy.argtypes = [TestCommandWithCP56Time2a]
    TestCommandWithCP56Time2a_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1755
if _libs["libiec60870.so"].has("TestCommandWithCP56Time2a_getCounter", "cdecl"):
    TestCommandWithCP56Time2a_getCounter = _libs["libiec60870.so"].get("TestCommandWithCP56Time2a_getCounter", "cdecl")
    TestCommandWithCP56Time2a_getCounter.argtypes = [TestCommandWithCP56Time2a]
    TestCommandWithCP56Time2a_getCounter.restype = uint16_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1758
if _libs["libiec60870.so"].has("TestCommandWithCP56Time2a_getTimestamp", "cdecl"):
    TestCommandWithCP56Time2a_getTimestamp = _libs["libiec60870.so"].get("TestCommandWithCP56Time2a_getTimestamp", "cdecl")
    TestCommandWithCP56Time2a_getTimestamp.argtypes = [TestCommandWithCP56Time2a]
    TestCommandWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1764
class struct_sResetProcessCommand(Structure):
    pass

ResetProcessCommand = POINTER(struct_sResetProcessCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1764

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1767
if _libs["libiec60870.so"].has("ResetProcessCommand_create", "cdecl"):
    ResetProcessCommand_create = _libs["libiec60870.so"].get("ResetProcessCommand_create", "cdecl")
    ResetProcessCommand_create.argtypes = [ResetProcessCommand, c_int, QualifierOfRPC]
    ResetProcessCommand_create.restype = ResetProcessCommand

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1770
if _libs["libiec60870.so"].has("ResetProcessCommand_destroy", "cdecl"):
    ResetProcessCommand_destroy = _libs["libiec60870.so"].get("ResetProcessCommand_destroy", "cdecl")
    ResetProcessCommand_destroy.argtypes = [ResetProcessCommand]
    ResetProcessCommand_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1773
if _libs["libiec60870.so"].has("ResetProcessCommand_getQRP", "cdecl"):
    ResetProcessCommand_getQRP = _libs["libiec60870.so"].get("ResetProcessCommand_getQRP", "cdecl")
    ResetProcessCommand_getQRP.argtypes = [ResetProcessCommand]
    ResetProcessCommand_getQRP.restype = QualifierOfRPC

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1779
class struct_sDelayAcquisitionCommand(Structure):
    pass

DelayAcquisitionCommand = POINTER(struct_sDelayAcquisitionCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1779

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1782
if _libs["libiec60870.so"].has("DelayAcquisitionCommand_create", "cdecl"):
    DelayAcquisitionCommand_create = _libs["libiec60870.so"].get("DelayAcquisitionCommand_create", "cdecl")
    DelayAcquisitionCommand_create.argtypes = [DelayAcquisitionCommand, c_int, CP16Time2a]
    DelayAcquisitionCommand_create.restype = DelayAcquisitionCommand

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1785
if _libs["libiec60870.so"].has("DelayAcquisitionCommand_destroy", "cdecl"):
    DelayAcquisitionCommand_destroy = _libs["libiec60870.so"].get("DelayAcquisitionCommand_destroy", "cdecl")
    DelayAcquisitionCommand_destroy.argtypes = [DelayAcquisitionCommand]
    DelayAcquisitionCommand_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1788
if _libs["libiec60870.so"].has("DelayAcquisitionCommand_getDelay", "cdecl"):
    DelayAcquisitionCommand_getDelay = _libs["libiec60870.so"].get("DelayAcquisitionCommand_getDelay", "cdecl")
    DelayAcquisitionCommand_getDelay.argtypes = [DelayAcquisitionCommand]
    DelayAcquisitionCommand_getDelay.restype = CP16Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1794
class struct_sEndOfInitialization(Structure):
    pass

EndOfInitialization = POINTER(struct_sEndOfInitialization)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1794

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1797
if _libs["libiec60870.so"].has("EndOfInitialization_create", "cdecl"):
    EndOfInitialization_create = _libs["libiec60870.so"].get("EndOfInitialization_create", "cdecl")
    EndOfInitialization_create.argtypes = [EndOfInitialization, uint8_t]
    EndOfInitialization_create.restype = EndOfInitialization

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1800
if _libs["libiec60870.so"].has("EndOfInitialization_destroy", "cdecl"):
    EndOfInitialization_destroy = _libs["libiec60870.so"].get("EndOfInitialization_destroy", "cdecl")
    EndOfInitialization_destroy.argtypes = [EndOfInitialization]
    EndOfInitialization_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1803
if _libs["libiec60870.so"].has("EndOfInitialization_getCOI", "cdecl"):
    EndOfInitialization_getCOI = _libs["libiec60870.so"].get("EndOfInitialization_getCOI", "cdecl")
    EndOfInitialization_getCOI.argtypes = [EndOfInitialization]
    EndOfInitialization_getCOI.restype = uint8_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1935
class struct_sFileReady(Structure):
    pass

FileReady = POINTER(struct_sFileReady)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1935

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1949
if _libs["libiec60870.so"].has("FileReady_create", "cdecl"):
    FileReady_create = _libs["libiec60870.so"].get("FileReady_create", "cdecl")
    FileReady_create.argtypes = [FileReady, c_int, uint16_t, uint32_t, c_bool]
    FileReady_create.restype = FileReady

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1952
if _libs["libiec60870.so"].has("FileReady_getFRQ", "cdecl"):
    FileReady_getFRQ = _libs["libiec60870.so"].get("FileReady_getFRQ", "cdecl")
    FileReady_getFRQ.argtypes = [FileReady]
    FileReady_getFRQ.restype = uint8_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1955
if _libs["libiec60870.so"].has("FileReady_setFRQ", "cdecl"):
    FileReady_setFRQ = _libs["libiec60870.so"].get("FileReady_setFRQ", "cdecl")
    FileReady_setFRQ.argtypes = [FileReady, uint8_t]
    FileReady_setFRQ.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1958
if _libs["libiec60870.so"].has("FileReady_isPositive", "cdecl"):
    FileReady_isPositive = _libs["libiec60870.so"].get("FileReady_isPositive", "cdecl")
    FileReady_isPositive.argtypes = [FileReady]
    FileReady_isPositive.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1961
if _libs["libiec60870.so"].has("FileReady_getNOF", "cdecl"):
    FileReady_getNOF = _libs["libiec60870.so"].get("FileReady_getNOF", "cdecl")
    FileReady_getNOF.argtypes = [FileReady]
    FileReady_getNOF.restype = uint16_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1964
if _libs["libiec60870.so"].has("FileReady_getLengthOfFile", "cdecl"):
    FileReady_getLengthOfFile = _libs["libiec60870.so"].get("FileReady_getLengthOfFile", "cdecl")
    FileReady_getLengthOfFile.argtypes = [FileReady]
    FileReady_getLengthOfFile.restype = uint32_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1967
if _libs["libiec60870.so"].has("FileReady_destroy", "cdecl"):
    FileReady_destroy = _libs["libiec60870.so"].get("FileReady_destroy", "cdecl")
    FileReady_destroy.argtypes = [FileReady]
    FileReady_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1973
class struct_sSectionReady(Structure):
    pass

SectionReady = POINTER(struct_sSectionReady)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1973

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1976
if _libs["libiec60870.so"].has("SectionReady_create", "cdecl"):
    SectionReady_create = _libs["libiec60870.so"].get("SectionReady_create", "cdecl")
    SectionReady_create.argtypes = [SectionReady, c_int, uint16_t, uint8_t, uint32_t, c_bool]
    SectionReady_create.restype = SectionReady

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1980
if _libs["libiec60870.so"].has("SectionReady_isNotReady", "cdecl"):
    SectionReady_isNotReady = _libs["libiec60870.so"].get("SectionReady_isNotReady", "cdecl")
    SectionReady_isNotReady.argtypes = [SectionReady]
    SectionReady_isNotReady.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1983
if _libs["libiec60870.so"].has("SectionReady_getSRQ", "cdecl"):
    SectionReady_getSRQ = _libs["libiec60870.so"].get("SectionReady_getSRQ", "cdecl")
    SectionReady_getSRQ.argtypes = [SectionReady]
    SectionReady_getSRQ.restype = uint8_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1986
if _libs["libiec60870.so"].has("SectionReady_setSRQ", "cdecl"):
    SectionReady_setSRQ = _libs["libiec60870.so"].get("SectionReady_setSRQ", "cdecl")
    SectionReady_setSRQ.argtypes = [SectionReady, uint8_t]
    SectionReady_setSRQ.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1989
if _libs["libiec60870.so"].has("SectionReady_getNOF", "cdecl"):
    SectionReady_getNOF = _libs["libiec60870.so"].get("SectionReady_getNOF", "cdecl")
    SectionReady_getNOF.argtypes = [SectionReady]
    SectionReady_getNOF.restype = uint16_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1992
if _libs["libiec60870.so"].has("SectionReady_getNameOfSection", "cdecl"):
    SectionReady_getNameOfSection = _libs["libiec60870.so"].get("SectionReady_getNameOfSection", "cdecl")
    SectionReady_getNameOfSection.argtypes = [SectionReady]
    SectionReady_getNameOfSection.restype = uint8_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1995
if _libs["libiec60870.so"].has("SectionReady_getLengthOfSection", "cdecl"):
    SectionReady_getLengthOfSection = _libs["libiec60870.so"].get("SectionReady_getLengthOfSection", "cdecl")
    SectionReady_getLengthOfSection.argtypes = [SectionReady]
    SectionReady_getLengthOfSection.restype = uint32_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1998
if _libs["libiec60870.so"].has("SectionReady_destroy", "cdecl"):
    SectionReady_destroy = _libs["libiec60870.so"].get("SectionReady_destroy", "cdecl")
    SectionReady_destroy.argtypes = [SectionReady]
    SectionReady_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2005
class struct_sFileCallOrSelect(Structure):
    pass

FileCallOrSelect = POINTER(struct_sFileCallOrSelect)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2005

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2008
if _libs["libiec60870.so"].has("FileCallOrSelect_create", "cdecl"):
    FileCallOrSelect_create = _libs["libiec60870.so"].get("FileCallOrSelect_create", "cdecl")
    FileCallOrSelect_create.argtypes = [FileCallOrSelect, c_int, uint16_t, uint8_t, uint8_t]
    FileCallOrSelect_create.restype = FileCallOrSelect

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2011
if _libs["libiec60870.so"].has("FileCallOrSelect_getNOF", "cdecl"):
    FileCallOrSelect_getNOF = _libs["libiec60870.so"].get("FileCallOrSelect_getNOF", "cdecl")
    FileCallOrSelect_getNOF.argtypes = [FileCallOrSelect]
    FileCallOrSelect_getNOF.restype = uint16_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2014
if _libs["libiec60870.so"].has("FileCallOrSelect_getNameOfSection", "cdecl"):
    FileCallOrSelect_getNameOfSection = _libs["libiec60870.so"].get("FileCallOrSelect_getNameOfSection", "cdecl")
    FileCallOrSelect_getNameOfSection.argtypes = [FileCallOrSelect]
    FileCallOrSelect_getNameOfSection.restype = uint8_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2017
if _libs["libiec60870.so"].has("FileCallOrSelect_getSCQ", "cdecl"):
    FileCallOrSelect_getSCQ = _libs["libiec60870.so"].get("FileCallOrSelect_getSCQ", "cdecl")
    FileCallOrSelect_getSCQ.argtypes = [FileCallOrSelect]
    FileCallOrSelect_getSCQ.restype = uint8_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2020
if _libs["libiec60870.so"].has("FileCallOrSelect_destroy", "cdecl"):
    FileCallOrSelect_destroy = _libs["libiec60870.so"].get("FileCallOrSelect_destroy", "cdecl")
    FileCallOrSelect_destroy.argtypes = [FileCallOrSelect]
    FileCallOrSelect_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2026
class struct_sFileLastSegmentOrSection(Structure):
    pass

FileLastSegmentOrSection = POINTER(struct_sFileLastSegmentOrSection)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2026

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2029
if _libs["libiec60870.so"].has("FileLastSegmentOrSection_create", "cdecl"):
    FileLastSegmentOrSection_create = _libs["libiec60870.so"].get("FileLastSegmentOrSection_create", "cdecl")
    FileLastSegmentOrSection_create.argtypes = [FileLastSegmentOrSection, c_int, uint16_t, uint8_t, uint8_t, uint8_t]
    FileLastSegmentOrSection_create.restype = FileLastSegmentOrSection

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2032
if _libs["libiec60870.so"].has("FileLastSegmentOrSection_getNOF", "cdecl"):
    FileLastSegmentOrSection_getNOF = _libs["libiec60870.so"].get("FileLastSegmentOrSection_getNOF", "cdecl")
    FileLastSegmentOrSection_getNOF.argtypes = [FileLastSegmentOrSection]
    FileLastSegmentOrSection_getNOF.restype = uint16_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2035
if _libs["libiec60870.so"].has("FileLastSegmentOrSection_getNameOfSection", "cdecl"):
    FileLastSegmentOrSection_getNameOfSection = _libs["libiec60870.so"].get("FileLastSegmentOrSection_getNameOfSection", "cdecl")
    FileLastSegmentOrSection_getNameOfSection.argtypes = [FileLastSegmentOrSection]
    FileLastSegmentOrSection_getNameOfSection.restype = uint8_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2038
if _libs["libiec60870.so"].has("FileLastSegmentOrSection_getLSQ", "cdecl"):
    FileLastSegmentOrSection_getLSQ = _libs["libiec60870.so"].get("FileLastSegmentOrSection_getLSQ", "cdecl")
    FileLastSegmentOrSection_getLSQ.argtypes = [FileLastSegmentOrSection]
    FileLastSegmentOrSection_getLSQ.restype = uint8_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2041
if _libs["libiec60870.so"].has("FileLastSegmentOrSection_getCHS", "cdecl"):
    FileLastSegmentOrSection_getCHS = _libs["libiec60870.so"].get("FileLastSegmentOrSection_getCHS", "cdecl")
    FileLastSegmentOrSection_getCHS.argtypes = [FileLastSegmentOrSection]
    FileLastSegmentOrSection_getCHS.restype = uint8_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2044
if _libs["libiec60870.so"].has("FileLastSegmentOrSection_destroy", "cdecl"):
    FileLastSegmentOrSection_destroy = _libs["libiec60870.so"].get("FileLastSegmentOrSection_destroy", "cdecl")
    FileLastSegmentOrSection_destroy.argtypes = [FileLastSegmentOrSection]
    FileLastSegmentOrSection_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2050
class struct_sFileACK(Structure):
    pass

FileACK = POINTER(struct_sFileACK)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2050

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2053
if _libs["libiec60870.so"].has("FileACK_create", "cdecl"):
    FileACK_create = _libs["libiec60870.so"].get("FileACK_create", "cdecl")
    FileACK_create.argtypes = [FileACK, c_int, uint16_t, uint8_t, uint8_t]
    FileACK_create.restype = FileACK

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2056
if _libs["libiec60870.so"].has("FileACK_getNOF", "cdecl"):
    FileACK_getNOF = _libs["libiec60870.so"].get("FileACK_getNOF", "cdecl")
    FileACK_getNOF.argtypes = [FileACK]
    FileACK_getNOF.restype = uint16_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2059
if _libs["libiec60870.so"].has("FileACK_getNameOfSection", "cdecl"):
    FileACK_getNameOfSection = _libs["libiec60870.so"].get("FileACK_getNameOfSection", "cdecl")
    FileACK_getNameOfSection.argtypes = [FileACK]
    FileACK_getNameOfSection.restype = uint8_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2062
if _libs["libiec60870.so"].has("FileACK_getAFQ", "cdecl"):
    FileACK_getAFQ = _libs["libiec60870.so"].get("FileACK_getAFQ", "cdecl")
    FileACK_getAFQ.argtypes = [FileACK]
    FileACK_getAFQ.restype = uint8_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2065
if _libs["libiec60870.so"].has("FileACK_destroy", "cdecl"):
    FileACK_destroy = _libs["libiec60870.so"].get("FileACK_destroy", "cdecl")
    FileACK_destroy.argtypes = [FileACK]
    FileACK_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2071
class struct_sFileSegment(Structure):
    pass

FileSegment = POINTER(struct_sFileSegment)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2071

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2074
if _libs["libiec60870.so"].has("FileSegment_create", "cdecl"):
    FileSegment_create = _libs["libiec60870.so"].get("FileSegment_create", "cdecl")
    FileSegment_create.argtypes = [FileSegment, c_int, uint16_t, uint8_t, POINTER(uint8_t), uint8_t]
    FileSegment_create.restype = FileSegment

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2077
if _libs["libiec60870.so"].has("FileSegment_getNOF", "cdecl"):
    FileSegment_getNOF = _libs["libiec60870.so"].get("FileSegment_getNOF", "cdecl")
    FileSegment_getNOF.argtypes = [FileSegment]
    FileSegment_getNOF.restype = uint16_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2080
if _libs["libiec60870.so"].has("FileSegment_getNameOfSection", "cdecl"):
    FileSegment_getNameOfSection = _libs["libiec60870.so"].get("FileSegment_getNameOfSection", "cdecl")
    FileSegment_getNameOfSection.argtypes = [FileSegment]
    FileSegment_getNameOfSection.restype = uint8_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2083
if _libs["libiec60870.so"].has("FileSegment_getLengthOfSegment", "cdecl"):
    FileSegment_getLengthOfSegment = _libs["libiec60870.so"].get("FileSegment_getLengthOfSegment", "cdecl")
    FileSegment_getLengthOfSegment.argtypes = [FileSegment]
    FileSegment_getLengthOfSegment.restype = uint8_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2085
if _libs["libiec60870.so"].has("FileSegment_getSegmentData", "cdecl"):
    FileSegment_getSegmentData = _libs["libiec60870.so"].get("FileSegment_getSegmentData", "cdecl")
    FileSegment_getSegmentData.argtypes = [FileSegment]
    FileSegment_getSegmentData.restype = POINTER(uint8_t)

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2089
if _libs["libiec60870.so"].has("FileSegment_GetMaxDataSize", "cdecl"):
    FileSegment_GetMaxDataSize = _libs["libiec60870.so"].get("FileSegment_GetMaxDataSize", "cdecl")
    FileSegment_GetMaxDataSize.argtypes = [CS101_AppLayerParameters]
    FileSegment_GetMaxDataSize.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2092
if _libs["libiec60870.so"].has("FileSegment_destroy", "cdecl"):
    FileSegment_destroy = _libs["libiec60870.so"].get("FileSegment_destroy", "cdecl")
    FileSegment_destroy.argtypes = [FileSegment]
    FileSegment_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2098
class struct_sFileDirectory(Structure):
    pass

FileDirectory = POINTER(struct_sFileDirectory)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2098

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2101
if _libs["libiec60870.so"].has("FileDirectory_create", "cdecl"):
    FileDirectory_create = _libs["libiec60870.so"].get("FileDirectory_create", "cdecl")
    FileDirectory_create.argtypes = [FileDirectory, c_int, uint16_t, uint32_t, uint8_t, CP56Time2a]
    FileDirectory_create.restype = FileDirectory

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2104
if _libs["libiec60870.so"].has("FileDirectory_getNOF", "cdecl"):
    FileDirectory_getNOF = _libs["libiec60870.so"].get("FileDirectory_getNOF", "cdecl")
    FileDirectory_getNOF.argtypes = [FileDirectory]
    FileDirectory_getNOF.restype = uint16_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2107
if _libs["libiec60870.so"].has("FileDirectory_getSOF", "cdecl"):
    FileDirectory_getSOF = _libs["libiec60870.so"].get("FileDirectory_getSOF", "cdecl")
    FileDirectory_getSOF.argtypes = [FileDirectory]
    FileDirectory_getSOF.restype = uint8_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2110
if _libs["libiec60870.so"].has("FileDirectory_getSTATUS", "cdecl"):
    FileDirectory_getSTATUS = _libs["libiec60870.so"].get("FileDirectory_getSTATUS", "cdecl")
    FileDirectory_getSTATUS.argtypes = [FileDirectory]
    FileDirectory_getSTATUS.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2113
if _libs["libiec60870.so"].has("FileDirectory_getLFD", "cdecl"):
    FileDirectory_getLFD = _libs["libiec60870.so"].get("FileDirectory_getLFD", "cdecl")
    FileDirectory_getLFD.argtypes = [FileDirectory]
    FileDirectory_getLFD.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2116
if _libs["libiec60870.so"].has("FileDirectory_getFOR", "cdecl"):
    FileDirectory_getFOR = _libs["libiec60870.so"].get("FileDirectory_getFOR", "cdecl")
    FileDirectory_getFOR.argtypes = [FileDirectory]
    FileDirectory_getFOR.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2119
if _libs["libiec60870.so"].has("FileDirectory_getFA", "cdecl"):
    FileDirectory_getFA = _libs["libiec60870.so"].get("FileDirectory_getFA", "cdecl")
    FileDirectory_getFA.argtypes = [FileDirectory]
    FileDirectory_getFA.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2122
if _libs["libiec60870.so"].has("FileDirectory_getLengthOfFile", "cdecl"):
    FileDirectory_getLengthOfFile = _libs["libiec60870.so"].get("FileDirectory_getLengthOfFile", "cdecl")
    FileDirectory_getLengthOfFile.argtypes = [FileDirectory]
    FileDirectory_getLengthOfFile.restype = uint32_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2125
if _libs["libiec60870.so"].has("FileDirectory_getCreationTime", "cdecl"):
    FileDirectory_getCreationTime = _libs["libiec60870.so"].get("FileDirectory_getCreationTime", "cdecl")
    FileDirectory_getCreationTime.argtypes = [FileDirectory]
    FileDirectory_getCreationTime.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2128
if _libs["libiec60870.so"].has("FileDirectory_destroy", "cdecl"):
    FileDirectory_destroy = _libs["libiec60870.so"].get("FileDirectory_destroy", "cdecl")
    FileDirectory_destroy.argtypes = [FileDirectory]
    FileDirectory_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2134
class struct_sQueryLog(Structure):
    pass

QueryLog = POINTER(struct_sQueryLog)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2134

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2137
if _libs["libiec60870.so"].has("QueryLog_create", "cdecl"):
    QueryLog_create = _libs["libiec60870.so"].get("QueryLog_create", "cdecl")
    QueryLog_create.argtypes = [QueryLog, c_int, uint16_t, CP56Time2a, CP56Time2a]
    QueryLog_create.restype = QueryLog

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2140
if _libs["libiec60870.so"].has("QueryLog_getNOF", "cdecl"):
    QueryLog_getNOF = _libs["libiec60870.so"].get("QueryLog_getNOF", "cdecl")
    QueryLog_getNOF.argtypes = [QueryLog]
    QueryLog_getNOF.restype = uint16_t

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2143
if _libs["libiec60870.so"].has("QueryLog_getRangeStartTime", "cdecl"):
    QueryLog_getRangeStartTime = _libs["libiec60870.so"].get("QueryLog_getRangeStartTime", "cdecl")
    QueryLog_getRangeStartTime.argtypes = [QueryLog]
    QueryLog_getRangeStartTime.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2147
if _libs["libiec60870.so"].has("QueryLog_getRangeStopTime", "cdecl"):
    QueryLog_getRangeStopTime = _libs["libiec60870.so"].get("QueryLog_getRangeStopTime", "cdecl")
    QueryLog_getRangeStopTime.argtypes = [QueryLog]
    QueryLog_getRangeStopTime.restype = CP56Time2a

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2150
if _libs["libiec60870.so"].has("QueryLog_destroy", "cdecl"):
    QueryLog_destroy = _libs["libiec60870.so"].get("QueryLog_destroy", "cdecl")
    QueryLog_destroy.argtypes = [QueryLog]
    QueryLog_destroy.restype = None

CS101_ASDUReceivedHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), c_int, CS101_ASDU)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_master.h: 53

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_master.h: 71
class struct_sCS101_MasterPlugin(Structure):
    pass

CS101_MasterPlugin = POINTER(struct_sCS101_MasterPlugin)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_master.h: 58

enum_anon_31 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_master.h: 67

CS101_MASTER_PLUGIN_RESULT_NOT_HANDLED = 0# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_master.h: 67

CS101_MASTER_PLUGIN_RESULT_HANDLED = 1# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_master.h: 67

CS101_MASTER_PLUGIN_RESULT_INVALID_ASDU = 2# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_master.h: 67

CS101_MasterPlugin_Result = enum_anon_31# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_master.h: 67

CS101_MasterPluginForwardAsduFunc = CFUNCTYPE(UNCHECKED(None), CS101_MasterPlugin, POINTER(None), CS101_ASDU)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_master.h: 69

struct_sCS101_MasterPlugin.__slots__ = [
    'handleAsdu',
    'sendAsdu',
    'eventHandler',
    'runTask',
    'setForwardAsduFunction',
    'getNextAsduToSend',
    'parameter',
]
struct_sCS101_MasterPlugin._fields_ = [
    ('handleAsdu', CFUNCTYPE(UNCHECKED(CS101_MasterPlugin_Result), POINTER(None), IPeerConnection, CS101_ASDU)),
    ('sendAsdu', CFUNCTYPE(UNCHECKED(CS101_MasterPlugin_Result), POINTER(None), IPeerConnection, CS101_ASDU)),
    ('eventHandler', CFUNCTYPE(UNCHECKED(None), POINTER(None), IPeerConnection, c_int)),
    ('runTask', CFUNCTYPE(UNCHECKED(None), POINTER(None), IPeerConnection)),
    ('setForwardAsduFunction', CFUNCTYPE(UNCHECKED(None), POINTER(None), CS101_MasterPluginForwardAsduFunc, POINTER(None))),
    ('getNextAsduToSend', CFUNCTYPE(UNCHECKED(Frame), POINTER(None), Frame)),
    ('parameter', POINTER(None)),
]

# /home/user/lib60870/lib60870-C/src/inc/api/link_layer_parameters.h: 42
class struct_sLinkLayerParameters(Structure):
    pass

LinkLayerParameters = POINTER(struct_sLinkLayerParameters)# /home/user/lib60870/lib60870-C/src/inc/api/link_layer_parameters.h: 40

struct_sLinkLayerParameters.__slots__ = [
    'addressLength',
    'timeoutForAck',
    'timeoutRepeat',
    'useSingleCharACK',
    'timeoutLinkState',
]
struct_sLinkLayerParameters._fields_ = [
    ('addressLength', c_int),
    ('timeoutForAck', c_int),
    ('timeoutRepeat', c_int),
    ('useSingleCharACK', c_bool),
    ('timeoutLinkState', c_int),
]

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 60
class struct_sCS101_Master(Structure):
    pass

CS101_Master = POINTER(struct_sCS101_Master)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 60

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 73
if _libs["libiec60870.so"].has("CS101_Master_create", "cdecl"):
    CS101_Master_create = _libs["libiec60870.so"].get("CS101_Master_create", "cdecl")
    CS101_Master_create.argtypes = [SerialPort, LinkLayerParameters, CS101_AppLayerParameters, IEC60870_LinkLayerMode]
    CS101_Master_create.restype = CS101_Master

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 81
if _libs["libiec60870.so"].has("CS101_Master_addPlugin", "cdecl"):
    CS101_Master_addPlugin = _libs["libiec60870.so"].get("CS101_Master_addPlugin", "cdecl")
    CS101_Master_addPlugin.argtypes = [CS101_Master, CS101_MasterPlugin]
    CS101_Master_addPlugin.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 102
if _libs["libiec60870.so"].has("CS101_Master_createEx", "cdecl"):
    CS101_Master_createEx = _libs["libiec60870.so"].get("CS101_Master_createEx", "cdecl")
    CS101_Master_createEx.argtypes = [SerialPort, LinkLayerParameters, CS101_AppLayerParameters, IEC60870_LinkLayerMode, c_int]
    CS101_Master_createEx.restype = CS101_Master

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 112
if _libs["libiec60870.so"].has("CS101_Master_run", "cdecl"):
    CS101_Master_run = _libs["libiec60870.so"].get("CS101_Master_run", "cdecl")
    CS101_Master_run.argtypes = [CS101_Master]
    CS101_Master_run.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 124
if _libs["libiec60870.so"].has("CS101_Master_start", "cdecl"):
    CS101_Master_start = _libs["libiec60870.so"].get("CS101_Master_start", "cdecl")
    CS101_Master_start.argtypes = [CS101_Master]
    CS101_Master_start.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 132
if _libs["libiec60870.so"].has("CS101_Master_stop", "cdecl"):
    CS101_Master_stop = _libs["libiec60870.so"].get("CS101_Master_stop", "cdecl")
    CS101_Master_stop.argtypes = [CS101_Master]
    CS101_Master_stop.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 144
if _libs["libiec60870.so"].has("CS101_Master_addSlave", "cdecl"):
    CS101_Master_addSlave = _libs["libiec60870.so"].get("CS101_Master_addSlave", "cdecl")
    CS101_Master_addSlave.argtypes = [CS101_Master, c_int]
    CS101_Master_addSlave.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 157
if _libs["libiec60870.so"].has("CS101_Master_pollSingleSlave", "cdecl"):
    CS101_Master_pollSingleSlave = _libs["libiec60870.so"].get("CS101_Master_pollSingleSlave", "cdecl")
    CS101_Master_pollSingleSlave.argtypes = [CS101_Master, c_int]
    CS101_Master_pollSingleSlave.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 174
if _libs["libiec60870.so"].has("CS101_Master_pollSingleSlaveClass1", "cdecl"):
    CS101_Master_pollSingleSlaveClass1 = _libs["libiec60870.so"].get("CS101_Master_pollSingleSlaveClass1", "cdecl")
    CS101_Master_pollSingleSlaveClass1.argtypes = [CS101_Master, c_int]
    CS101_Master_pollSingleSlaveClass1.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 180
if _libs["libiec60870.so"].has("CS101_Master_destroy", "cdecl"):
    CS101_Master_destroy = _libs["libiec60870.so"].get("CS101_Master_destroy", "cdecl")
    CS101_Master_destroy.argtypes = [CS101_Master]
    CS101_Master_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 191
if _libs["libiec60870.so"].has("CS101_Master_setDIR", "cdecl"):
    CS101_Master_setDIR = _libs["libiec60870.so"].get("CS101_Master_setDIR", "cdecl")
    CS101_Master_setDIR.argtypes = [CS101_Master, c_bool]
    CS101_Master_setDIR.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 199
if _libs["libiec60870.so"].has("CS101_Master_setOwnAddress", "cdecl"):
    CS101_Master_setOwnAddress = _libs["libiec60870.so"].get("CS101_Master_setOwnAddress", "cdecl")
    CS101_Master_setOwnAddress.argtypes = [CS101_Master, c_int]
    CS101_Master_setOwnAddress.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 211
if _libs["libiec60870.so"].has("CS101_Master_useSlaveAddress", "cdecl"):
    CS101_Master_useSlaveAddress = _libs["libiec60870.so"].get("CS101_Master_useSlaveAddress", "cdecl")
    CS101_Master_useSlaveAddress.argtypes = [CS101_Master, c_int]
    CS101_Master_useSlaveAddress.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 219
if _libs["libiec60870.so"].has("CS101_Master_getAppLayerParameters", "cdecl"):
    CS101_Master_getAppLayerParameters = _libs["libiec60870.so"].get("CS101_Master_getAppLayerParameters", "cdecl")
    CS101_Master_getAppLayerParameters.argtypes = [CS101_Master]
    CS101_Master_getAppLayerParameters.restype = CS101_AppLayerParameters

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 227
if _libs["libiec60870.so"].has("CS101_Master_getLinkLayerParameters", "cdecl"):
    CS101_Master_getLinkLayerParameters = _libs["libiec60870.so"].get("CS101_Master_getLinkLayerParameters", "cdecl")
    CS101_Master_getLinkLayerParameters.argtypes = [CS101_Master]
    CS101_Master_getLinkLayerParameters.restype = LinkLayerParameters

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 240
if _libs["libiec60870.so"].has("CS101_Master_isChannelReady", "cdecl"):
    CS101_Master_isChannelReady = _libs["libiec60870.so"].get("CS101_Master_isChannelReady", "cdecl")
    CS101_Master_isChannelReady.argtypes = [CS101_Master, c_int]
    CS101_Master_isChannelReady.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 249
if _libs["libiec60870.so"].has("CS101_Master_sendLinkLayerTestFunction", "cdecl"):
    CS101_Master_sendLinkLayerTestFunction = _libs["libiec60870.so"].get("CS101_Master_sendLinkLayerTestFunction", "cdecl")
    CS101_Master_sendLinkLayerTestFunction.argtypes = [CS101_Master]
    CS101_Master_sendLinkLayerTestFunction.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 259
if _libs["libiec60870.so"].has("CS101_Master_sendInterrogationCommand", "cdecl"):
    CS101_Master_sendInterrogationCommand = _libs["libiec60870.so"].get("CS101_Master_sendInterrogationCommand", "cdecl")
    CS101_Master_sendInterrogationCommand.argtypes = [CS101_Master, CS101_CauseOfTransmission, c_int, QualifierOfInterrogation]
    CS101_Master_sendInterrogationCommand.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 269
if _libs["libiec60870.so"].has("CS101_Master_sendCounterInterrogationCommand", "cdecl"):
    CS101_Master_sendCounterInterrogationCommand = _libs["libiec60870.so"].get("CS101_Master_sendCounterInterrogationCommand", "cdecl")
    CS101_Master_sendCounterInterrogationCommand.argtypes = [CS101_Master, CS101_CauseOfTransmission, c_int, uint8_t]
    CS101_Master_sendCounterInterrogationCommand.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 281
if _libs["libiec60870.so"].has("CS101_Master_sendReadCommand", "cdecl"):
    CS101_Master_sendReadCommand = _libs["libiec60870.so"].get("CS101_Master_sendReadCommand", "cdecl")
    CS101_Master_sendReadCommand.argtypes = [CS101_Master, c_int, c_int]
    CS101_Master_sendReadCommand.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 290
if _libs["libiec60870.so"].has("CS101_Master_sendClockSyncCommand", "cdecl"):
    CS101_Master_sendClockSyncCommand = _libs["libiec60870.so"].get("CS101_Master_sendClockSyncCommand", "cdecl")
    CS101_Master_sendClockSyncCommand.argtypes = [CS101_Master, c_int, CP56Time2a]
    CS101_Master_sendClockSyncCommand.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 300
if _libs["libiec60870.so"].has("CS101_Master_sendTestCommand", "cdecl"):
    CS101_Master_sendTestCommand = _libs["libiec60870.so"].get("CS101_Master_sendTestCommand", "cdecl")
    CS101_Master_sendTestCommand.argtypes = [CS101_Master, c_int]
    CS101_Master_sendTestCommand.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 311
if _libs["libiec60870.so"].has("CS101_Master_sendProcessCommand", "cdecl"):
    CS101_Master_sendProcessCommand = _libs["libiec60870.so"].get("CS101_Master_sendProcessCommand", "cdecl")
    CS101_Master_sendProcessCommand.argtypes = [CS101_Master, CS101_CauseOfTransmission, c_int, InformationObject]
    CS101_Master_sendProcessCommand.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 327
if _libs["libiec60870.so"].has("CS101_Master_sendASDU", "cdecl"):
    CS101_Master_sendASDU = _libs["libiec60870.so"].get("CS101_Master_sendASDU", "cdecl")
    CS101_Master_sendASDU.argtypes = [CS101_Master, CS101_ASDU]
    CS101_Master_sendASDU.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 336
if _libs["libiec60870.so"].has("CS101_Master_setASDUReceivedHandler", "cdecl"):
    CS101_Master_setASDUReceivedHandler = _libs["libiec60870.so"].get("CS101_Master_setASDUReceivedHandler", "cdecl")
    CS101_Master_setASDUReceivedHandler.argtypes = [CS101_Master, CS101_ASDUReceivedHandler, POINTER(None)]
    CS101_Master_setASDUReceivedHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 342
if _libs["libiec60870.so"].has("CS101_Master_setLinkLayerStateChanged", "cdecl"):
    CS101_Master_setLinkLayerStateChanged = _libs["libiec60870.so"].get("CS101_Master_setLinkLayerStateChanged", "cdecl")
    CS101_Master_setLinkLayerStateChanged.argtypes = [CS101_Master, IEC60870_LinkLayerStateChangedHandler, POINTER(None)]
    CS101_Master_setLinkLayerStateChanged.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 351
if _libs["libiec60870.so"].has("CS101_Master_setRawMessageHandler", "cdecl"):
    CS101_Master_setRawMessageHandler = _libs["libiec60870.so"].get("CS101_Master_setRawMessageHandler", "cdecl")
    CS101_Master_setRawMessageHandler.argtypes = [CS101_Master, IEC60870_RawMessageHandler, POINTER(None)]
    CS101_Master_setRawMessageHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 362
if _libs["libiec60870.so"].has("CS101_Master_setIdleTimeout", "cdecl"):
    CS101_Master_setIdleTimeout = _libs["libiec60870.so"].get("CS101_Master_setIdleTimeout", "cdecl")
    CS101_Master_setIdleTimeout.argtypes = [CS101_Master, c_int]
    CS101_Master_setIdleTimeout.restype = None

IMasterConnection = POINTER(struct_sIPeerConnection)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 63

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 79
if _libs["libiec60870.so"].has("IMasterConnection_isReady", "cdecl"):
    IMasterConnection_isReady = _libs["libiec60870.so"].get("IMasterConnection_isReady", "cdecl")
    IMasterConnection_isReady.argtypes = [IMasterConnection]
    IMasterConnection_isReady.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 92
if _libs["libiec60870.so"].has("IMasterConnection_sendASDU", "cdecl"):
    IMasterConnection_sendASDU = _libs["libiec60870.so"].get("IMasterConnection_sendASDU", "cdecl")
    IMasterConnection_sendASDU.argtypes = [IMasterConnection, CS101_ASDU]
    IMasterConnection_sendASDU.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 106
if _libs["libiec60870.so"].has("IMasterConnection_sendASDUEx", "cdecl"):
    IMasterConnection_sendASDUEx = _libs["libiec60870.so"].get("IMasterConnection_sendASDUEx", "cdecl")
    IMasterConnection_sendASDUEx.argtypes = [IMasterConnection, CS101_ASDU, c_bool]
    IMasterConnection_sendASDUEx.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 119
if _libs["libiec60870.so"].has("IMasterConnection_sendACT_CON", "cdecl"):
    IMasterConnection_sendACT_CON = _libs["libiec60870.so"].get("IMasterConnection_sendACT_CON", "cdecl")
    IMasterConnection_sendACT_CON.argtypes = [IMasterConnection, CS101_ASDU, c_bool]
    IMasterConnection_sendACT_CON.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 131
if _libs["libiec60870.so"].has("IMasterConnection_sendACT_TERM", "cdecl"):
    IMasterConnection_sendACT_TERM = _libs["libiec60870.so"].get("IMasterConnection_sendACT_TERM", "cdecl")
    IMasterConnection_sendACT_TERM.argtypes = [IMasterConnection, CS101_ASDU]
    IMasterConnection_sendACT_TERM.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 142
if _libs["libiec60870.so"].has("IMasterConnection_getPeerAddress", "cdecl"):
    IMasterConnection_getPeerAddress = _libs["libiec60870.so"].get("IMasterConnection_getPeerAddress", "cdecl")
    IMasterConnection_getPeerAddress.argtypes = [IMasterConnection, String, c_int]
    IMasterConnection_getPeerAddress.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 150
if _libs["libiec60870.so"].has("IMasterConnection_close", "cdecl"):
    IMasterConnection_close = _libs["libiec60870.so"].get("IMasterConnection_close", "cdecl")
    IMasterConnection_close.argtypes = [IMasterConnection]
    IMasterConnection_close.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 156
if _libs["libiec60870.so"].has("IMasterConnection_getApplicationLayerParameters", "cdecl"):
    IMasterConnection_getApplicationLayerParameters = _libs["libiec60870.so"].get("IMasterConnection_getApplicationLayerParameters", "cdecl")
    IMasterConnection_getApplicationLayerParameters.argtypes = [IMasterConnection]
    IMasterConnection_getApplicationLayerParameters.restype = CS101_AppLayerParameters

enum_anon_32 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 174

CS101_PLUGIN_RESULT_NOT_HANDLED = 0# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 174

CS101_PLUGIN_RESULT_HANDLED = 1# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 174

CS101_PLUGIN_RESULT_INVALID_ASDU = 2# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 174

CS101_SlavePlugin_Result = enum_anon_32# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 174

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 185
class struct_sCS101_SlavePlugin(Structure):
    pass

CS101_SlavePlugin = POINTER(struct_sCS101_SlavePlugin)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 179

CS101_PluginEnqueueFunc = CFUNCTYPE(UNCHECKED(None), POINTER(None), CS101_ASDU)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 181

CS101_PluginForwardAsduFunc = CFUNCTYPE(UNCHECKED(None), CS101_SlavePlugin, POINTER(None), CS101_ASDU, POINTER(None))# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 183

struct_sCS101_SlavePlugin.__slots__ = [
    'handleAsdu',
    'sendAsdu',
    'setEnqueueFunction',
    'hasAsduToSend',
    'getNextAsduToSend',
    'setForwardAsduFunction',
    'runTask',
    'eventHandler',
    'checkIfAsduAllowed',
    'parameter',
]
struct_sCS101_SlavePlugin._fields_ = [
    ('handleAsdu', CFUNCTYPE(UNCHECKED(CS101_SlavePlugin_Result), POINTER(None), IMasterConnection, CS101_ASDU)),
    ('sendAsdu', CFUNCTYPE(UNCHECKED(CS101_SlavePlugin_Result), POINTER(None), IMasterConnection, CS101_ASDU)),
    ('setEnqueueFunction', CFUNCTYPE(UNCHECKED(None), POINTER(None), CS101_PluginEnqueueFunc, POINTER(None))),
    ('hasAsduToSend', CFUNCTYPE(UNCHECKED(c_bool), POINTER(None))),
    ('getNextAsduToSend', CFUNCTYPE(UNCHECKED(Frame), POINTER(None), Frame)),
    ('setForwardAsduFunction', CFUNCTYPE(UNCHECKED(None), POINTER(None), CS101_PluginForwardAsduFunc, POINTER(None))),
    ('runTask', CFUNCTYPE(UNCHECKED(None), POINTER(None), IMasterConnection)),
    ('eventHandler', CFUNCTYPE(UNCHECKED(None), POINTER(None), IPeerConnection, c_int)),
    ('checkIfAsduAllowed', CFUNCTYPE(UNCHECKED(c_bool), POINTER(None))),
    ('parameter', POINTER(None)),
]

CS101_ResetCUHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None))# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 230

CS101_InterrogationHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, uint8_t)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 235

CS101_CounterInterrogationHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, QualifierOfCIC)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 240

CS101_ReadHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, c_int)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 245

CS101_ClockSynchronizationHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, CP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 260

CS101_ResetProcessHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, uint8_t)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 265

CS101_DelayAcquisitionHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, CP16Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 270

CS101_ASDUHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 275

CS101_GetNextInterrogationASDUHandler = CFUNCTYPE(UNCHECKED(CS101_ASDU), POINTER(None), IMasterConnection)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 290

CS101_IsCAAllowedHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), c_int)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 302

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 63
class struct_sCS101_Slave(Structure):
    pass

CS101_Slave = POINTER(struct_sCS101_Slave)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 63

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 79
if _libs["libiec60870.so"].has("CS101_Slave_create", "cdecl"):
    CS101_Slave_create = _libs["libiec60870.so"].get("CS101_Slave_create", "cdecl")
    CS101_Slave_create.argtypes = [SerialPort, LinkLayerParameters, CS101_AppLayerParameters, IEC60870_LinkLayerMode]
    CS101_Slave_create.restype = CS101_Slave

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 96
if _libs["libiec60870.so"].has("CS101_Slave_createEx", "cdecl"):
    CS101_Slave_createEx = _libs["libiec60870.so"].get("CS101_Slave_createEx", "cdecl")
    CS101_Slave_createEx.argtypes = [SerialPort, LinkLayerParameters, CS101_AppLayerParameters, IEC60870_LinkLayerMode, c_int, c_int]
    CS101_Slave_createEx.restype = CS101_Slave

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 105
if _libs["libiec60870.so"].has("CS101_Slave_destroy", "cdecl"):
    CS101_Slave_destroy = _libs["libiec60870.so"].get("CS101_Slave_destroy", "cdecl")
    CS101_Slave_destroy.argtypes = [CS101_Slave]
    CS101_Slave_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 131
if _libs["libiec60870.so"].has("CS101_Slave_setDIR", "cdecl"):
    CS101_Slave_setDIR = _libs["libiec60870.so"].get("CS101_Slave_setDIR", "cdecl")
    CS101_Slave_setDIR.argtypes = [CS101_Slave, c_bool]
    CS101_Slave_setDIR.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 139
if _libs["libiec60870.so"].has("CS101_Slave_addPlugin", "cdecl"):
    CS101_Slave_addPlugin = _libs["libiec60870.so"].get("CS101_Slave_addPlugin", "cdecl")
    CS101_Slave_addPlugin.argtypes = [CS101_Slave, CS101_SlavePlugin]
    CS101_Slave_addPlugin.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 150
if _libs["libiec60870.so"].has("CS101_Slave_setIdleTimeout", "cdecl"):
    CS101_Slave_setIdleTimeout = _libs["libiec60870.so"].get("CS101_Slave_setIdleTimeout", "cdecl")
    CS101_Slave_setIdleTimeout.argtypes = [CS101_Slave, c_int]
    CS101_Slave_setIdleTimeout.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 156
if _libs["libiec60870.so"].has("CS101_Slave_setLinkLayerStateChanged", "cdecl"):
    CS101_Slave_setLinkLayerStateChanged = _libs["libiec60870.so"].get("CS101_Slave_setLinkLayerStateChanged", "cdecl")
    CS101_Slave_setLinkLayerStateChanged.argtypes = [CS101_Slave, IEC60870_LinkLayerStateChangedHandler, POINTER(None)]
    CS101_Slave_setLinkLayerStateChanged.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 166
if _libs["libiec60870.so"].has("CS101_Slave_setLinkLayerAddress", "cdecl"):
    CS101_Slave_setLinkLayerAddress = _libs["libiec60870.so"].get("CS101_Slave_setLinkLayerAddress", "cdecl")
    CS101_Slave_setLinkLayerAddress.argtypes = [CS101_Slave, c_int]
    CS101_Slave_setLinkLayerAddress.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 175
if _libs["libiec60870.so"].has("CS101_Slave_setLinkLayerAddressOtherStation", "cdecl"):
    CS101_Slave_setLinkLayerAddressOtherStation = _libs["libiec60870.so"].get("CS101_Slave_setLinkLayerAddressOtherStation", "cdecl")
    CS101_Slave_setLinkLayerAddressOtherStation.argtypes = [CS101_Slave, c_int]
    CS101_Slave_setLinkLayerAddressOtherStation.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 185
if _libs["libiec60870.so"].has("CS101_Slave_isClass1QueueFull", "cdecl"):
    CS101_Slave_isClass1QueueFull = _libs["libiec60870.so"].get("CS101_Slave_isClass1QueueFull", "cdecl")
    CS101_Slave_isClass1QueueFull.argtypes = [CS101_Slave]
    CS101_Slave_isClass1QueueFull.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 194
if _libs["libiec60870.so"].has("CS101_Slave_enqueueUserDataClass1", "cdecl"):
    CS101_Slave_enqueueUserDataClass1 = _libs["libiec60870.so"].get("CS101_Slave_enqueueUserDataClass1", "cdecl")
    CS101_Slave_enqueueUserDataClass1.argtypes = [CS101_Slave, CS101_ASDU]
    CS101_Slave_enqueueUserDataClass1.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 204
if _libs["libiec60870.so"].has("CS101_Slave_isClass2QueueFull", "cdecl"):
    CS101_Slave_isClass2QueueFull = _libs["libiec60870.so"].get("CS101_Slave_isClass2QueueFull", "cdecl")
    CS101_Slave_isClass2QueueFull.argtypes = [CS101_Slave]
    CS101_Slave_isClass2QueueFull.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 213
if _libs["libiec60870.so"].has("CS101_Slave_enqueueUserDataClass2", "cdecl"):
    CS101_Slave_enqueueUserDataClass2 = _libs["libiec60870.so"].get("CS101_Slave_enqueueUserDataClass2", "cdecl")
    CS101_Slave_enqueueUserDataClass2.argtypes = [CS101_Slave, CS101_ASDU]
    CS101_Slave_enqueueUserDataClass2.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 221
if _libs["libiec60870.so"].has("CS101_Slave_flushQueues", "cdecl"):
    CS101_Slave_flushQueues = _libs["libiec60870.so"].get("CS101_Slave_flushQueues", "cdecl")
    CS101_Slave_flushQueues.argtypes = [CS101_Slave]
    CS101_Slave_flushQueues.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 232
if _libs["libiec60870.so"].has("CS101_Slave_run", "cdecl"):
    CS101_Slave_run = _libs["libiec60870.so"].get("CS101_Slave_run", "cdecl")
    CS101_Slave_run.argtypes = [CS101_Slave]
    CS101_Slave_run.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 244
if _libs["libiec60870.so"].has("CS101_Slave_start", "cdecl"):
    CS101_Slave_start = _libs["libiec60870.so"].get("CS101_Slave_start", "cdecl")
    CS101_Slave_start.argtypes = [CS101_Slave]
    CS101_Slave_start.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 252
if _libs["libiec60870.so"].has("CS101_Slave_stop", "cdecl"):
    CS101_Slave_stop = _libs["libiec60870.so"].get("CS101_Slave_stop", "cdecl")
    CS101_Slave_stop.argtypes = [CS101_Slave]
    CS101_Slave_stop.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 262
if _libs["libiec60870.so"].has("CS101_Slave_getAppLayerParameters", "cdecl"):
    CS101_Slave_getAppLayerParameters = _libs["libiec60870.so"].get("CS101_Slave_getAppLayerParameters", "cdecl")
    CS101_Slave_getAppLayerParameters.argtypes = [CS101_Slave]
    CS101_Slave_getAppLayerParameters.restype = CS101_AppLayerParameters

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 272
if _libs["libiec60870.so"].has("CS101_Slave_getLinkLayerParameters", "cdecl"):
    CS101_Slave_getLinkLayerParameters = _libs["libiec60870.so"].get("CS101_Slave_getLinkLayerParameters", "cdecl")
    CS101_Slave_getLinkLayerParameters.argtypes = [CS101_Slave]
    CS101_Slave_getLinkLayerParameters.restype = LinkLayerParameters

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 282
if _libs["libiec60870.so"].has("CS101_Slave_setAllowedCAHandler", "cdecl"):
    CS101_Slave_setAllowedCAHandler = _libs["libiec60870.so"].get("CS101_Slave_setAllowedCAHandler", "cdecl")
    CS101_Slave_setAllowedCAHandler.argtypes = [CS101_Slave, CS101_IsCAAllowedHandler, POINTER(None)]
    CS101_Slave_setAllowedCAHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 291
if _libs["libiec60870.so"].has("CS101_Slave_setResetCUHandler", "cdecl"):
    CS101_Slave_setResetCUHandler = _libs["libiec60870.so"].get("CS101_Slave_setResetCUHandler", "cdecl")
    CS101_Slave_setResetCUHandler.argtypes = [CS101_Slave, CS101_ResetCUHandler, POINTER(None)]
    CS101_Slave_setResetCUHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 300
if _libs["libiec60870.so"].has("CS101_Slave_setInterrogationHandler", "cdecl"):
    CS101_Slave_setInterrogationHandler = _libs["libiec60870.so"].get("CS101_Slave_setInterrogationHandler", "cdecl")
    CS101_Slave_setInterrogationHandler.argtypes = [CS101_Slave, CS101_InterrogationHandler, POINTER(None)]
    CS101_Slave_setInterrogationHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 309
if _libs["libiec60870.so"].has("CS101_Slave_setCounterInterrogationHandler", "cdecl"):
    CS101_Slave_setCounterInterrogationHandler = _libs["libiec60870.so"].get("CS101_Slave_setCounterInterrogationHandler", "cdecl")
    CS101_Slave_setCounterInterrogationHandler.argtypes = [CS101_Slave, CS101_CounterInterrogationHandler, POINTER(None)]
    CS101_Slave_setCounterInterrogationHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 318
if _libs["libiec60870.so"].has("CS101_Slave_setReadHandler", "cdecl"):
    CS101_Slave_setReadHandler = _libs["libiec60870.so"].get("CS101_Slave_setReadHandler", "cdecl")
    CS101_Slave_setReadHandler.argtypes = [CS101_Slave, CS101_ReadHandler, POINTER(None)]
    CS101_Slave_setReadHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 327
if _libs["libiec60870.so"].has("CS101_Slave_setClockSyncHandler", "cdecl"):
    CS101_Slave_setClockSyncHandler = _libs["libiec60870.so"].get("CS101_Slave_setClockSyncHandler", "cdecl")
    CS101_Slave_setClockSyncHandler.argtypes = [CS101_Slave, CS101_ClockSynchronizationHandler, POINTER(None)]
    CS101_Slave_setClockSyncHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 336
if _libs["libiec60870.so"].has("CS101_Slave_setResetProcessHandler", "cdecl"):
    CS101_Slave_setResetProcessHandler = _libs["libiec60870.so"].get("CS101_Slave_setResetProcessHandler", "cdecl")
    CS101_Slave_setResetProcessHandler.argtypes = [CS101_Slave, CS101_ResetProcessHandler, POINTER(None)]
    CS101_Slave_setResetProcessHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 345
if _libs["libiec60870.so"].has("CS101_Slave_setDelayAcquisitionHandler", "cdecl"):
    CS101_Slave_setDelayAcquisitionHandler = _libs["libiec60870.so"].get("CS101_Slave_setDelayAcquisitionHandler", "cdecl")
    CS101_Slave_setDelayAcquisitionHandler.argtypes = [CS101_Slave, CS101_DelayAcquisitionHandler, POINTER(None)]
    CS101_Slave_setDelayAcquisitionHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 357
if _libs["libiec60870.so"].has("CS101_Slave_setASDUHandler", "cdecl"):
    CS101_Slave_setASDUHandler = _libs["libiec60870.so"].get("CS101_Slave_setASDUHandler", "cdecl")
    CS101_Slave_setASDUHandler.argtypes = [CS101_Slave, CS101_ASDUHandler, POINTER(None)]
    CS101_Slave_setASDUHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 366
if _libs["libiec60870.so"].has("CS101_Slave_setRawMessageHandler", "cdecl"):
    CS101_Slave_setRawMessageHandler = _libs["libiec60870.so"].get("CS101_Slave_setRawMessageHandler", "cdecl")
    CS101_Slave_setRawMessageHandler.argtypes = [CS101_Slave, IEC60870_RawMessageHandler, POINTER(None)]
    CS101_Slave_setRawMessageHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 375
if _libs["libiec60870.so"].has("CS101_Slave_setGetNextInterrogationASDUHandler", "cdecl"):
    CS101_Slave_setGetNextInterrogationASDUHandler = _libs["libiec60870.so"].get("CS101_Slave_setGetNextInterrogationASDUHandler", "cdecl")
    CS101_Slave_setGetNextInterrogationASDUHandler.argtypes = [CS101_Slave, CS101_GetNextInterrogationASDUHandler, POINTER(None)]
    CS101_Slave_setGetNextInterrogationASDUHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 56
class struct_sCS104_Connection(Structure):
    pass

CS104_Connection = POINTER(struct_sCS104_Connection)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 56

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 67
if _libs["libiec60870.so"].has("CS104_Connection_create", "cdecl"):
    CS104_Connection_create = _libs["libiec60870.so"].get("CS104_Connection_create", "cdecl")
    CS104_Connection_create.argtypes = [String, c_int]
    CS104_Connection_create.restype = CS104_Connection

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 79
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_createSecure", "cdecl"):
        continue
    CS104_Connection_createSecure = _lib.get("CS104_Connection_createSecure", "cdecl")
    CS104_Connection_createSecure.argtypes = [String, c_int, TLSConfiguration]
    CS104_Connection_createSecure.restype = CS104_Connection
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 87
if _libs["libiec60870.so"].has("CS104_Connection_addPlugin", "cdecl"):
    CS104_Connection_addPlugin = _libs["libiec60870.so"].get("CS104_Connection_addPlugin", "cdecl")
    CS104_Connection_addPlugin.argtypes = [CS104_Connection, CS101_MasterPlugin]
    CS104_Connection_addPlugin.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 111
if _libs["libiec60870.so"].has("CS104_Connection_setLocalAddress", "cdecl"):
    CS104_Connection_setLocalAddress = _libs["libiec60870.so"].get("CS104_Connection_setLocalAddress", "cdecl")
    CS104_Connection_setLocalAddress.argtypes = [CS104_Connection, String, c_int]
    CS104_Connection_setLocalAddress.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 124
if _libs["libiec60870.so"].has("CS104_Connection_setAPCIParameters", "cdecl"):
    CS104_Connection_setAPCIParameters = _libs["libiec60870.so"].get("CS104_Connection_setAPCIParameters", "cdecl")
    CS104_Connection_setAPCIParameters.argtypes = [CS104_Connection, CS104_APCIParameters]
    CS104_Connection_setAPCIParameters.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 130
if _libs["libiec60870.so"].has("CS104_Connection_getAPCIParameters", "cdecl"):
    CS104_Connection_getAPCIParameters = _libs["libiec60870.so"].get("CS104_Connection_getAPCIParameters", "cdecl")
    CS104_Connection_getAPCIParameters.argtypes = [CS104_Connection]
    CS104_Connection_getAPCIParameters.restype = CS104_APCIParameters

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 143
if _libs["libiec60870.so"].has("CS104_Connection_setAppLayerParameters", "cdecl"):
    CS104_Connection_setAppLayerParameters = _libs["libiec60870.so"].get("CS104_Connection_setAppLayerParameters", "cdecl")
    CS104_Connection_setAppLayerParameters.argtypes = [CS104_Connection, CS101_AppLayerParameters]
    CS104_Connection_setAppLayerParameters.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 155
if _libs["libiec60870.so"].has("CS104_Connection_getAppLayerParameters", "cdecl"):
    CS104_Connection_getAppLayerParameters = _libs["libiec60870.so"].get("CS104_Connection_getAppLayerParameters", "cdecl")
    CS104_Connection_getAppLayerParameters.argtypes = [CS104_Connection]
    CS104_Connection_getAppLayerParameters.restype = CS101_AppLayerParameters

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 166
if _libs["libiec60870.so"].has("CS104_Connection_setOriginatorAddress", "cdecl"):
    CS104_Connection_setOriginatorAddress = _libs["libiec60870.so"].get("CS104_Connection_setOriginatorAddress", "cdecl")
    CS104_Connection_setOriginatorAddress.argtypes = [CS104_Connection, uint8_t]
    CS104_Connection_setOriginatorAddress.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 177
if _libs["libiec60870.so"].has("CS104_Connection_setConnectTimeout", "cdecl"):
    CS104_Connection_setConnectTimeout = _libs["libiec60870.so"].get("CS104_Connection_setConnectTimeout", "cdecl")
    CS104_Connection_setConnectTimeout.argtypes = [CS104_Connection, c_int]
    CS104_Connection_setConnectTimeout.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 187
if _libs["libiec60870.so"].has("CS104_Connection_connectAsync", "cdecl"):
    CS104_Connection_connectAsync = _libs["libiec60870.so"].get("CS104_Connection_connectAsync", "cdecl")
    CS104_Connection_connectAsync.argtypes = [CS104_Connection]
    CS104_Connection_connectAsync.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 199
if _libs["libiec60870.so"].has("CS104_Connection_connect", "cdecl"):
    CS104_Connection_connect = _libs["libiec60870.so"].get("CS104_Connection_connect", "cdecl")
    CS104_Connection_connect.argtypes = [CS104_Connection]
    CS104_Connection_connect.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 208
if _libs["libiec60870.so"].has("CS104_Connection_isConnected", "cdecl"):
    CS104_Connection_isConnected = _libs["libiec60870.so"].get("CS104_Connection_isConnected", "cdecl")
    CS104_Connection_isConnected.argtypes = [CS104_Connection]
    CS104_Connection_isConnected.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 217
if _libs["libiec60870.so"].has("CS104_Connection_sendStartDT", "cdecl"):
    CS104_Connection_sendStartDT = _libs["libiec60870.so"].get("CS104_Connection_sendStartDT", "cdecl")
    CS104_Connection_sendStartDT.argtypes = [CS104_Connection]
    CS104_Connection_sendStartDT.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 223
if _libs["libiec60870.so"].has("CS104_Connection_sendStopDT", "cdecl"):
    CS104_Connection_sendStopDT = _libs["libiec60870.so"].get("CS104_Connection_sendStopDT", "cdecl")
    CS104_Connection_sendStopDT.argtypes = [CS104_Connection]
    CS104_Connection_sendStopDT.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 233
if _libs["libiec60870.so"].has("CS104_Connection_isTransmitBufferFull", "cdecl"):
    CS104_Connection_isTransmitBufferFull = _libs["libiec60870.so"].get("CS104_Connection_isTransmitBufferFull", "cdecl")
    CS104_Connection_isTransmitBufferFull.argtypes = [CS104_Connection]
    CS104_Connection_isTransmitBufferFull.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 245
if _libs["libiec60870.so"].has("CS104_Connection_sendInterrogationCommand", "cdecl"):
    CS104_Connection_sendInterrogationCommand = _libs["libiec60870.so"].get("CS104_Connection_sendInterrogationCommand", "cdecl")
    CS104_Connection_sendInterrogationCommand.argtypes = [CS104_Connection, CS101_CauseOfTransmission, c_int, QualifierOfInterrogation]
    CS104_Connection_sendInterrogationCommand.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 257
if _libs["libiec60870.so"].has("CS104_Connection_sendCounterInterrogationCommand", "cdecl"):
    CS104_Connection_sendCounterInterrogationCommand = _libs["libiec60870.so"].get("CS104_Connection_sendCounterInterrogationCommand", "cdecl")
    CS104_Connection_sendCounterInterrogationCommand.argtypes = [CS104_Connection, CS101_CauseOfTransmission, c_int, uint8_t]
    CS104_Connection_sendCounterInterrogationCommand.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 271
if _libs["libiec60870.so"].has("CS104_Connection_sendReadCommand", "cdecl"):
    CS104_Connection_sendReadCommand = _libs["libiec60870.so"].get("CS104_Connection_sendReadCommand", "cdecl")
    CS104_Connection_sendReadCommand.argtypes = [CS104_Connection, c_int, c_int]
    CS104_Connection_sendReadCommand.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 282
if _libs["libiec60870.so"].has("CS104_Connection_sendClockSyncCommand", "cdecl"):
    CS104_Connection_sendClockSyncCommand = _libs["libiec60870.so"].get("CS104_Connection_sendClockSyncCommand", "cdecl")
    CS104_Connection_sendClockSyncCommand.argtypes = [CS104_Connection, c_int, CP56Time2a]
    CS104_Connection_sendClockSyncCommand.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 294
if _libs["libiec60870.so"].has("CS104_Connection_sendTestCommand", "cdecl"):
    CS104_Connection_sendTestCommand = _libs["libiec60870.so"].get("CS104_Connection_sendTestCommand", "cdecl")
    CS104_Connection_sendTestCommand.argtypes = [CS104_Connection, c_int]
    CS104_Connection_sendTestCommand.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 306
if _libs["libiec60870.so"].has("CS104_Connection_sendTestCommandWithTimestamp", "cdecl"):
    CS104_Connection_sendTestCommandWithTimestamp = _libs["libiec60870.so"].get("CS104_Connection_sendTestCommandWithTimestamp", "cdecl")
    CS104_Connection_sendTestCommandWithTimestamp.argtypes = [CS104_Connection, c_int, uint16_t, CP56Time2a]
    CS104_Connection_sendTestCommandWithTimestamp.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 321
if _libs["libiec60870.so"].has("CS104_Connection_sendProcessCommand", "cdecl"):
    CS104_Connection_sendProcessCommand = _libs["libiec60870.so"].get("CS104_Connection_sendProcessCommand", "cdecl")
    CS104_Connection_sendProcessCommand.argtypes = [CS104_Connection, TypeID, CS101_CauseOfTransmission, c_int, InformationObject]
    CS104_Connection_sendProcessCommand.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 334
if _libs["libiec60870.so"].has("CS104_Connection_sendProcessCommandEx", "cdecl"):
    CS104_Connection_sendProcessCommandEx = _libs["libiec60870.so"].get("CS104_Connection_sendProcessCommandEx", "cdecl")
    CS104_Connection_sendProcessCommandEx.argtypes = [CS104_Connection, CS101_CauseOfTransmission, c_int, InformationObject]
    CS104_Connection_sendProcessCommandEx.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 345
if _libs["libiec60870.so"].has("CS104_Connection_sendASDU", "cdecl"):
    CS104_Connection_sendASDU = _libs["libiec60870.so"].get("CS104_Connection_sendASDU", "cdecl")
    CS104_Connection_sendASDU.argtypes = [CS104_Connection, CS101_ASDU]
    CS104_Connection_sendASDU.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 354
if _libs["libiec60870.so"].has("CS104_Connection_setASDUReceivedHandler", "cdecl"):
    CS104_Connection_setASDUReceivedHandler = _libs["libiec60870.so"].get("CS104_Connection_setASDUReceivedHandler", "cdecl")
    CS104_Connection_setASDUReceivedHandler.argtypes = [CS104_Connection, CS101_ASDUReceivedHandler, POINTER(None)]
    CS104_Connection_setASDUReceivedHandler.restype = None

enum_anon_33 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 362

CS104_CONNECTION_OPENED = 0# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 362

CS104_CONNECTION_CLOSED = 1# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 362

CS104_CONNECTION_STARTDT_CON_RECEIVED = 2# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 362

CS104_CONNECTION_STOPDT_CON_RECEIVED = 3# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 362

CS104_CONNECTION_FAILED = 4# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 362

CS104_ConnectionEvent = enum_anon_33# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 362

CS104_ConnectionHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), CS104_Connection, CS104_ConnectionEvent)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 374

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 383
if _libs["libiec60870.so"].has("CS104_Connection_setConnectionHandler", "cdecl"):
    CS104_Connection_setConnectionHandler = _libs["libiec60870.so"].get("CS104_Connection_setConnectionHandler", "cdecl")
    CS104_Connection_setConnectionHandler.argtypes = [CS104_Connection, CS104_ConnectionHandler, POINTER(None)]
    CS104_Connection_setConnectionHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 393
if _libs["libiec60870.so"].has("CS104_Connection_setRawMessageHandler", "cdecl"):
    CS104_Connection_setRawMessageHandler = _libs["libiec60870.so"].get("CS104_Connection_setRawMessageHandler", "cdecl")
    CS104_Connection_setRawMessageHandler.argtypes = [CS104_Connection, IEC60870_RawMessageHandler, POINTER(None)]
    CS104_Connection_setRawMessageHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 399
if _libs["libiec60870.so"].has("CS104_Connection_close", "cdecl"):
    CS104_Connection_close = _libs["libiec60870.so"].get("CS104_Connection_close", "cdecl")
    CS104_Connection_close.argtypes = [CS104_Connection]
    CS104_Connection_close.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 405
if _libs["libiec60870.so"].has("CS104_Connection_destroy", "cdecl"):
    CS104_Connection_destroy = _libs["libiec60870.so"].get("CS104_Connection_destroy", "cdecl")
    CS104_Connection_destroy.argtypes = [CS104_Connection]
    CS104_Connection_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 417
if _libs["libiec60870.so"].has("CS104_Connection_startThreadless", "cdecl"):
    CS104_Connection_startThreadless = _libs["libiec60870.so"].get("CS104_Connection_startThreadless", "cdecl")
    CS104_Connection_startThreadless.argtypes = [CS104_Connection]
    CS104_Connection_startThreadless.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 423
if _libs["libiec60870.so"].has("CS104_Connection_stopThreadless", "cdecl"):
    CS104_Connection_stopThreadless = _libs["libiec60870.so"].get("CS104_Connection_stopThreadless", "cdecl")
    CS104_Connection_stopThreadless.argtypes = [CS104_Connection]
    CS104_Connection_stopThreadless.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 431
if _libs["libiec60870.so"].has("CS104_Connection_isThreadless", "cdecl"):
    CS104_Connection_isThreadless = _libs["libiec60870.so"].get("CS104_Connection_isThreadless", "cdecl")
    CS104_Connection_isThreadless.argtypes = [CS104_Connection]
    CS104_Connection_isThreadless.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 444
if _libs["libiec60870.so"].has("CS104_Connection_run", "cdecl"):
    CS104_Connection_run = _libs["libiec60870.so"].get("CS104_Connection_run", "cdecl")
    CS104_Connection_run.argtypes = [CS104_Connection, c_int]
    CS104_Connection_run.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 457
if _libs["libiec60870.so"].has("CS104_Connection_sendMessage", "cdecl"):
    CS104_Connection_sendMessage = _libs["libiec60870.so"].get("CS104_Connection_sendMessage", "cdecl")
    CS104_Connection_sendMessage.argtypes = [CS104_Connection, POINTER(uint8_t), c_int]
    CS104_Connection_sendMessage.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 54
class struct_sCS104_Slave(Structure):
    pass

CS104_Slave = POINTER(struct_sCS104_Slave)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 54

enum_anon_34 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 60

CS104_MODE_SINGLE_REDUNDANCY_GROUP = 0# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 60

CS104_MODE_CONNECTION_IS_REDUNDANCY_GROUP = (CS104_MODE_SINGLE_REDUNDANCY_GROUP + 1)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 60

CS104_MODE_MULTIPLE_REDUNDANCY_GROUPS = (CS104_MODE_CONNECTION_IS_REDUNDANCY_GROUP + 1)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 60

CS104_ServerMode = enum_anon_34# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 60

enum_anon_35 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 66

IP_ADDRESS_TYPE_IPV4 = 0# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 66

IP_ADDRESS_TYPE_IPV6 = (IP_ADDRESS_TYPE_IPV4 + 1)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 66

eCS104_IPAddressType = enum_anon_35# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 66

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 68
class struct_sCS104_RedundancyGroup(Structure):
    pass

CS104_RedundancyGroup = POINTER(struct_sCS104_RedundancyGroup)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 68

CS104_ConnectionRequestHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), String)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 78

enum_anon_36 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 85

CS104_CON_EVENT_CONNECTION_OPENED = 0# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 85

CS104_CON_EVENT_CONNECTION_CLOSED = 1# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 85

CS104_CON_EVENT_ACTIVATED = 2# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 85

CS104_CON_EVENT_DEACTIVATED = 3# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 85

CS104_PeerConnectionEvent = enum_anon_36# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 85

CS104_ConnectionEventHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), IMasterConnection, CS104_PeerConnectionEvent)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 94

CS104_SlaveRawMessageHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), IMasterConnection, POINTER(uint8_t), c_int, c_bool)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 109

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 120
if _libs["libiec60870.so"].has("CS104_Slave_create", "cdecl"):
    CS104_Slave_create = _libs["libiec60870.so"].get("CS104_Slave_create", "cdecl")
    CS104_Slave_create.argtypes = [c_int, c_int]
    CS104_Slave_create.restype = CS104_Slave

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 132
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_createSecure", "cdecl"):
        continue
    CS104_Slave_createSecure = _lib.get("CS104_Slave_createSecure", "cdecl")
    CS104_Slave_createSecure.argtypes = [c_int, c_int, TLSConfiguration]
    CS104_Slave_createSecure.restype = CS104_Slave
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 135
if _libs["libiec60870.so"].has("CS104_Slave_addPlugin", "cdecl"):
    CS104_Slave_addPlugin = _libs["libiec60870.so"].get("CS104_Slave_addPlugin", "cdecl")
    CS104_Slave_addPlugin.argtypes = [CS104_Slave, CS101_SlavePlugin]
    CS104_Slave_addPlugin.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 150
if _libs["libiec60870.so"].has("CS104_Slave_setLocalAddress", "cdecl"):
    CS104_Slave_setLocalAddress = _libs["libiec60870.so"].get("CS104_Slave_setLocalAddress", "cdecl")
    CS104_Slave_setLocalAddress.argtypes = [CS104_Slave, String]
    CS104_Slave_setLocalAddress.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 159
if _libs["libiec60870.so"].has("CS104_Slave_setLocalPort", "cdecl"):
    CS104_Slave_setLocalPort = _libs["libiec60870.so"].get("CS104_Slave_setLocalPort", "cdecl")
    CS104_Slave_setLocalPort.argtypes = [CS104_Slave, c_int]
    CS104_Slave_setLocalPort.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 167
if _libs["libiec60870.so"].has("CS104_Slave_getOpenConnections", "cdecl"):
    CS104_Slave_getOpenConnections = _libs["libiec60870.so"].get("CS104_Slave_getOpenConnections", "cdecl")
    CS104_Slave_getOpenConnections.argtypes = [CS104_Slave]
    CS104_Slave_getOpenConnections.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 178
if _libs["libiec60870.so"].has("CS104_Slave_setMaxOpenConnections", "cdecl"):
    CS104_Slave_setMaxOpenConnections = _libs["libiec60870.so"].get("CS104_Slave_setMaxOpenConnections", "cdecl")
    CS104_Slave_setMaxOpenConnections.argtypes = [CS104_Slave, c_int]
    CS104_Slave_setMaxOpenConnections.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 187
if _libs["libiec60870.so"].has("CS104_Slave_setServerMode", "cdecl"):
    CS104_Slave_setServerMode = _libs["libiec60870.so"].get("CS104_Slave_setServerMode", "cdecl")
    CS104_Slave_setServerMode.argtypes = [CS104_Slave, CS104_ServerMode]
    CS104_Slave_setServerMode.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 197
if _libs["libiec60870.so"].has("CS104_Slave_setAllowedCAHandler", "cdecl"):
    CS104_Slave_setAllowedCAHandler = _libs["libiec60870.so"].get("CS104_Slave_setAllowedCAHandler", "cdecl")
    CS104_Slave_setAllowedCAHandler.argtypes = [CS104_Slave, CS101_IsCAAllowedHandler, POINTER(None)]
    CS104_Slave_setAllowedCAHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 211
if _libs["libiec60870.so"].has("CS104_Slave_setConnectionRequestHandler", "cdecl"):
    CS104_Slave_setConnectionRequestHandler = _libs["libiec60870.so"].get("CS104_Slave_setConnectionRequestHandler", "cdecl")
    CS104_Slave_setConnectionRequestHandler.argtypes = [CS104_Slave, CS104_ConnectionRequestHandler, POINTER(None)]
    CS104_Slave_setConnectionRequestHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 224
if _libs["libiec60870.so"].has("CS104_Slave_setConnectionEventHandler", "cdecl"):
    CS104_Slave_setConnectionEventHandler = _libs["libiec60870.so"].get("CS104_Slave_setConnectionEventHandler", "cdecl")
    CS104_Slave_setConnectionEventHandler.argtypes = [CS104_Slave, CS104_ConnectionEventHandler, POINTER(None)]
    CS104_Slave_setConnectionEventHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 233
if _libs["libiec60870.so"].has("CS104_Slave_setInterrogationHandler", "cdecl"):
    CS104_Slave_setInterrogationHandler = _libs["libiec60870.so"].get("CS104_Slave_setInterrogationHandler", "cdecl")
    CS104_Slave_setInterrogationHandler.argtypes = [CS104_Slave, CS101_InterrogationHandler, POINTER(None)]
    CS104_Slave_setInterrogationHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 242
if _libs["libiec60870.so"].has("CS104_Slave_setCounterInterrogationHandler", "cdecl"):
    CS104_Slave_setCounterInterrogationHandler = _libs["libiec60870.so"].get("CS104_Slave_setCounterInterrogationHandler", "cdecl")
    CS104_Slave_setCounterInterrogationHandler.argtypes = [CS104_Slave, CS101_CounterInterrogationHandler, POINTER(None)]
    CS104_Slave_setCounterInterrogationHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 251
if _libs["libiec60870.so"].has("CS104_Slave_setReadHandler", "cdecl"):
    CS104_Slave_setReadHandler = _libs["libiec60870.so"].get("CS104_Slave_setReadHandler", "cdecl")
    CS104_Slave_setReadHandler.argtypes = [CS104_Slave, CS101_ReadHandler, POINTER(None)]
    CS104_Slave_setReadHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 263
if _libs["libiec60870.so"].has("CS104_Slave_setASDUHandler", "cdecl"):
    CS104_Slave_setASDUHandler = _libs["libiec60870.so"].get("CS104_Slave_setASDUHandler", "cdecl")
    CS104_Slave_setASDUHandler.argtypes = [CS104_Slave, CS101_ASDUHandler, POINTER(None)]
    CS104_Slave_setASDUHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 272
if _libs["libiec60870.so"].has("CS104_Slave_setClockSyncHandler", "cdecl"):
    CS104_Slave_setClockSyncHandler = _libs["libiec60870.so"].get("CS104_Slave_setClockSyncHandler", "cdecl")
    CS104_Slave_setClockSyncHandler.argtypes = [CS104_Slave, CS101_ClockSynchronizationHandler, POINTER(None)]
    CS104_Slave_setClockSyncHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 281
if _libs["libiec60870.so"].has("CS104_Slave_setResetProcessHandler", "cdecl"):
    CS104_Slave_setResetProcessHandler = _libs["libiec60870.so"].get("CS104_Slave_setResetProcessHandler", "cdecl")
    CS104_Slave_setResetProcessHandler.argtypes = [CS104_Slave, CS101_ResetProcessHandler, POINTER(None)]
    CS104_Slave_setResetProcessHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 292
if _libs["libiec60870.so"].has("CS104_Slave_setDelayAcquisitionHandler", "cdecl"):
    CS104_Slave_setDelayAcquisitionHandler = _libs["libiec60870.so"].get("CS104_Slave_setDelayAcquisitionHandler", "cdecl")
    CS104_Slave_setDelayAcquisitionHandler.argtypes = [CS104_Slave, CS101_DelayAcquisitionHandler, POINTER(None)]
    CS104_Slave_setDelayAcquisitionHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 301
if _libs["libiec60870.so"].has("CS104_Slave_setRawMessageHandler", "cdecl"):
    CS104_Slave_setRawMessageHandler = _libs["libiec60870.so"].get("CS104_Slave_setRawMessageHandler", "cdecl")
    CS104_Slave_setRawMessageHandler.argtypes = [CS104_Slave, CS104_SlaveRawMessageHandler, POINTER(None)]
    CS104_Slave_setRawMessageHandler.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 307
if _libs["libiec60870.so"].has("CS104_Slave_getConnectionParameters", "cdecl"):
    CS104_Slave_getConnectionParameters = _libs["libiec60870.so"].get("CS104_Slave_getConnectionParameters", "cdecl")
    CS104_Slave_getConnectionParameters.argtypes = [CS104_Slave]
    CS104_Slave_getConnectionParameters.restype = CS104_APCIParameters

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 313
if _libs["libiec60870.so"].has("CS104_Slave_getAppLayerParameters", "cdecl"):
    CS104_Slave_getAppLayerParameters = _libs["libiec60870.so"].get("CS104_Slave_getAppLayerParameters", "cdecl")
    CS104_Slave_getAppLayerParameters.argtypes = [CS104_Slave]
    CS104_Slave_getAppLayerParameters.restype = CS101_AppLayerParameters

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 324
if _libs["libiec60870.so"].has("CS104_Slave_start", "cdecl"):
    CS104_Slave_start = _libs["libiec60870.so"].get("CS104_Slave_start", "cdecl")
    CS104_Slave_start.argtypes = [CS104_Slave]
    CS104_Slave_start.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 334
if _libs["libiec60870.so"].has("CS104_Slave_isRunning", "cdecl"):
    CS104_Slave_isRunning = _libs["libiec60870.so"].get("CS104_Slave_isRunning", "cdecl")
    CS104_Slave_isRunning.argtypes = [CS104_Slave]
    CS104_Slave_isRunning.restype = c_bool

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 343
if _libs["libiec60870.so"].has("CS104_Slave_stop", "cdecl"):
    CS104_Slave_stop = _libs["libiec60870.so"].get("CS104_Slave_stop", "cdecl")
    CS104_Slave_stop.argtypes = [CS104_Slave]
    CS104_Slave_stop.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 353
if _libs["libiec60870.so"].has("CS104_Slave_startThreadless", "cdecl"):
    CS104_Slave_startThreadless = _libs["libiec60870.so"].get("CS104_Slave_startThreadless", "cdecl")
    CS104_Slave_startThreadless.argtypes = [CS104_Slave]
    CS104_Slave_startThreadless.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 362
if _libs["libiec60870.so"].has("CS104_Slave_stopThreadless", "cdecl"):
    CS104_Slave_stopThreadless = _libs["libiec60870.so"].get("CS104_Slave_stopThreadless", "cdecl")
    CS104_Slave_stopThreadless.argtypes = [CS104_Slave]
    CS104_Slave_stopThreadless.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 373
if _libs["libiec60870.so"].has("CS104_Slave_tick", "cdecl"):
    CS104_Slave_tick = _libs["libiec60870.so"].get("CS104_Slave_tick", "cdecl")
    CS104_Slave_tick.argtypes = [CS104_Slave]
    CS104_Slave_tick.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 385
if _libs["libiec60870.so"].has("CS104_Slave_getNumberOfQueueEntries", "cdecl"):
    CS104_Slave_getNumberOfQueueEntries = _libs["libiec60870.so"].get("CS104_Slave_getNumberOfQueueEntries", "cdecl")
    CS104_Slave_getNumberOfQueueEntries.argtypes = [CS104_Slave, CS104_RedundancyGroup]
    CS104_Slave_getNumberOfQueueEntries.restype = c_int

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 393
if _libs["libiec60870.so"].has("CS104_Slave_enqueueASDU", "cdecl"):
    CS104_Slave_enqueueASDU = _libs["libiec60870.so"].get("CS104_Slave_enqueueASDU", "cdecl")
    CS104_Slave_enqueueASDU.argtypes = [CS104_Slave, CS101_ASDU]
    CS104_Slave_enqueueASDU.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 406
if _libs["libiec60870.so"].has("CS104_Slave_addRedundancyGroup", "cdecl"):
    CS104_Slave_addRedundancyGroup = _libs["libiec60870.so"].get("CS104_Slave_addRedundancyGroup", "cdecl")
    CS104_Slave_addRedundancyGroup.argtypes = [CS104_Slave, CS104_RedundancyGroup]
    CS104_Slave_addRedundancyGroup.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 412
if _libs["libiec60870.so"].has("CS104_Slave_destroy", "cdecl"):
    CS104_Slave_destroy = _libs["libiec60870.so"].get("CS104_Slave_destroy", "cdecl")
    CS104_Slave_destroy.argtypes = [CS104_Slave]
    CS104_Slave_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 421
if _libs["libiec60870.so"].has("CS104_RedundancyGroup_create", "cdecl"):
    CS104_RedundancyGroup_create = _libs["libiec60870.so"].get("CS104_RedundancyGroup_create", "cdecl")
    CS104_RedundancyGroup_create.argtypes = [String]
    CS104_RedundancyGroup_create.restype = CS104_RedundancyGroup

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 429
if _libs["libiec60870.so"].has("CS104_RedundancyGroup_addAllowedClient", "cdecl"):
    CS104_RedundancyGroup_addAllowedClient = _libs["libiec60870.so"].get("CS104_RedundancyGroup_addAllowedClient", "cdecl")
    CS104_RedundancyGroup_addAllowedClient.argtypes = [CS104_RedundancyGroup, String]
    CS104_RedundancyGroup_addAllowedClient.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 438
if _libs["libiec60870.so"].has("CS104_RedundancyGroup_addAllowedClientEx", "cdecl"):
    CS104_RedundancyGroup_addAllowedClientEx = _libs["libiec60870.so"].get("CS104_RedundancyGroup_addAllowedClientEx", "cdecl")
    CS104_RedundancyGroup_addAllowedClientEx.argtypes = [CS104_RedundancyGroup, POINTER(uint8_t), eCS104_IPAddressType]
    CS104_RedundancyGroup_addAllowedClientEx.restype = None

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 458
if _libs["libiec60870.so"].has("CS104_RedundancyGroup_destroy", "cdecl"):
    CS104_RedundancyGroup_destroy = _libs["libiec60870.so"].get("CS104_RedundancyGroup_destroy", "cdecl")
    CS104_RedundancyGroup_destroy.argtypes = [CS104_RedundancyGroup]
    CS104_RedundancyGroup_destroy.restype = None

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 15
def CALLOC(nmemb, size):
    return (Memory_calloc (nmemb, size))

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 16
def MALLOC(size):
    return (Memory_malloc (size))

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 17
def REALLOC(oldptr, size):
    return (Memory_realloc (oldptr, size))

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 18
def FREEMEM(ptr):
    return (Memory_free (ptr))

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 20
def GLOBAL_CALLOC(nmemb, size):
    return (Memory_calloc (nmemb, size))

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 21
def GLOBAL_MALLOC(size):
    return (Memory_malloc (size))

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 22
def GLOBAL_REALLOC(oldptr, size):
    return (Memory_realloc (oldptr, size))

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 23
def GLOBAL_FREEMEM(ptr):
    return (Memory_free (ptr))

# /home/user/lib60870/lib60870-C/src/hal/inc/platform_endian.h: 34
try:
    ORDER_LITTLE_ENDIAN = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 8
try:
    TLS_NULL_WITH_NULL_NULL = 0x0000
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 9
try:
    TLS_RSA_WITH_NULL_MD5 = 0x0001
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 10
try:
    TLS_RSA_WITH_NULL_SHA = 0x0002
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 11
try:
    TLS_RSA_EXPORT_WITH_RC4_40_MD5 = 0x0003
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 12
try:
    TLS_RSA_WITH_RC4_128_MD5 = 0x0004
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 13
try:
    TLS_RSA_WITH_RC4_128_SHA = 0x0005
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 14
try:
    TLS_RSA_EXPORT_WITH_RC2_CBC_40_MD5 = 0x0006
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 15
try:
    TLS_RSA_WITH_IDEA_CBC_SHA = 0x0007
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 16
try:
    TLS_RSA_EXPORT_WITH_DES40_CBC_SHA = 0x0008
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 17
try:
    TLS_RSA_WITH_DES_CBC_SHA = 0x0009
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 18
try:
    TLS_RSA_WITH_3DES_EDE_CBC_SHA = 0x000A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 19
try:
    TLS_DH_DSS_EXPORT_WITH_DES40_CBC_SHA = 0x000B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 20
try:
    TLS_DH_DSS_WITH_DES_CBC_SHA = 0x000C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 21
try:
    TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA = 0x000D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 22
try:
    TLS_DH_RSA_EXPORT_WITH_DES40_CBC_SHA = 0x000E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 23
try:
    TLS_DH_RSA_WITH_DES_CBC_SHA = 0x000F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 24
try:
    TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA = 0x0010
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 25
try:
    TLS_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA = 0x0011
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 26
try:
    TLS_DHE_DSS_WITH_DES_CBC_SHA = 0x0012
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 27
try:
    TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA = 0x0013
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 28
try:
    TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA = 0x0014
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 29
try:
    TLS_DHE_RSA_WITH_DES_CBC_SHA = 0x0015
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 30
try:
    TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA = 0x0016
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 31
try:
    TLS_DH_anon_EXPORT_WITH_RC4_40_MD5 = 0x0017
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 32
try:
    TLS_DH_anon_WITH_RC4_128_MD5 = 0x0018
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 33
try:
    TLS_DH_anon_EXPORT_WITH_DES40_CBC_SHA = 0x0019
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 34
try:
    TLS_DH_anon_WITH_DES_CBC_SHA = 0x001A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 35
try:
    TLS_DH_anon_WITH_3DES_EDE_CBC_SHA = 0x001B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 36
try:
    TLS_RSA_WITH_AES_128_CBC_SHA = 0x002F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 37
try:
    TLS_DH_DSS_WITH_AES_128_CBC_SHA = 0x0030
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 38
try:
    TLS_DH_RSA_WITH_AES_128_CBC_SHA = 0x0031
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 39
try:
    TLS_DHE_DSS_WITH_AES_128_CBC_SHA = 0x0032
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 40
try:
    TLS_DHE_RSA_WITH_AES_128_CBC_SHA = 0x0033
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 41
try:
    TLS_DH_anon_WITH_AES_128_CBC_SHA = 0x0034
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 42
try:
    TLS_RSA_WITH_AES_256_CBC_SHA = 0x0035
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 43
try:
    TLS_DH_DSS_WITH_AES_256_CBC_SHA = 0x0036
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 44
try:
    TLS_DH_RSA_WITH_AES_256_CBC_SHA = 0x0037
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 45
try:
    TLS_DHE_DSS_WITH_AES_256_CBC_SHA = 0x0038
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 46
try:
    TLS_DHE_RSA_WITH_AES_256_CBC_SHA = 0x0039
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 47
try:
    TLS_DH_anon_WITH_AES_256_CBC_SHA = 0x003A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 48
try:
    TLS_RSA_WITH_NULL_SHA256 = 0x003B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 49
try:
    TLS_RSA_WITH_AES_128_CBC_SHA256 = 0x003C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 50
try:
    TLS_RSA_WITH_AES_256_CBC_SHA256 = 0x003D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 51
try:
    TLS_DH_DSS_WITH_AES_128_CBC_SHA256 = 0x003E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 52
try:
    TLS_DH_RSA_WITH_AES_128_CBC_SHA256 = 0x003F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 53
try:
    TLS_DHE_DSS_WITH_AES_128_CBC_SHA256 = 0x0040
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 54
try:
    TLS_RSA_WITH_CAMELLIA_128_CBC_SHA = 0x0041
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 55
try:
    TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA = 0x0042
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 56
try:
    TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA = 0x0043
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 57
try:
    TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA = 0x0044
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 58
try:
    TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA = 0x0045
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 59
try:
    TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA = 0x0046
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 60
try:
    TLS_DHE_RSA_WITH_AES_128_CBC_SHA256 = 0x0067
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 61
try:
    TLS_DH_DSS_WITH_AES_256_CBC_SHA256 = 0x0068
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 62
try:
    TLS_DH_RSA_WITH_AES_256_CBC_SHA256 = 0x0069
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 63
try:
    TLS_DHE_DSS_WITH_AES_256_CBC_SHA256 = 0x006A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 64
try:
    TLS_DHE_RSA_WITH_AES_256_CBC_SHA256 = 0x006B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 65
try:
    TLS_DH_anon_WITH_AES_128_CBC_SHA256 = 0x006C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 66
try:
    TLS_DH_anon_WITH_AES_256_CBC_SHA256 = 0x006D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 67
try:
    TLS_RSA_WITH_CAMELLIA_256_CBC_SHA = 0x0084
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 68
try:
    TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA = 0x0085
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 69
try:
    TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA = 0x0086
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 70
try:
    TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA = 0x0087
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 71
try:
    TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA = 0x0088
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 72
try:
    TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA = 0x0089
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 73
try:
    TLS_RSA_WITH_SEED_CBC_SHA = 0x0096
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 74
try:
    TLS_DH_DSS_WITH_SEED_CBC_SHA = 0x0097
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 75
try:
    TLS_DH_RSA_WITH_SEED_CBC_SHA = 0x0098
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 76
try:
    TLS_DHE_DSS_WITH_SEED_CBC_SHA = 0x0099
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 77
try:
    TLS_DHE_RSA_WITH_SEED_CBC_SHA = 0x009A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 78
try:
    TLS_DH_anon_WITH_SEED_CBC_SHA = 0x009B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 79
try:
    TLS_RSA_WITH_AES_128_GCM_SHA256 = 0x009C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 80
try:
    TLS_RSA_WITH_AES_256_GCM_SHA384 = 0x009D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 81
try:
    TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 = 0x009E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 82
try:
    TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 = 0x009F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 83
try:
    TLS_DH_RSA_WITH_AES_128_GCM_SHA256 = 0x00A0
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 84
try:
    TLS_DH_RSA_WITH_AES_256_GCM_SHA384 = 0x00A1
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 85
try:
    TLS_DHE_DSS_WITH_AES_128_GCM_SHA256 = 0x00A2
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 86
try:
    TLS_DHE_DSS_WITH_AES_256_GCM_SHA384 = 0x00A3
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 87
try:
    TLS_DH_DSS_WITH_AES_128_GCM_SHA256 = 0x00A4
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 88
try:
    TLS_DH_DSS_WITH_AES_256_GCM_SHA384 = 0x00A5
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 89
try:
    TLS_DH_anon_WITH_AES_128_GCM_SHA256 = 0x00A6
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 90
try:
    TLS_DH_anon_WITH_AES_256_GCM_SHA384 = 0x00A7
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 91
try:
    TLS_PSK_WITH_AES_128_CBC_SHA = 0x008C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 92
try:
    TLS_PSK_WITH_AES_256_CBC_SHA = 0x008D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 93
try:
    TLS_DHE_PSK_WITH_AES_128_CBC_SHA = 0x008E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 94
try:
    TLS_DHE_PSK_WITH_AES_256_CBC_SHA = 0x008F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 95
try:
    TLS_RSA_PSK_WITH_AES_128_CBC_SHA = 0x0090
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 96
try:
    TLS_RSA_PSK_WITH_AES_256_CBC_SHA = 0x0091
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 97
try:
    TLS_PSK_WITH_AES_256_GCM_SHA384 = 0x00A9
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 98
try:
    TLS_PSK_WITH_AES_128_CBC_SHA256 = 0x00AE
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 99
try:
    TLS_PSK_WITH_AES_256_CBC_SHA384 = 0x00AF
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 100
try:
    TLS_DHE_PSK_WITH_AES_128_CBC_SHA256 = 0x00B0
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 101
try:
    TLS_DHE_PSK_WITH_AES_256_CBC_SHA384 = 0x00B1
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 102
try:
    TLS_RSA_PSK_WITH_AES_128_CBC_SHA256 = 0x00B2
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 103
try:
    TLS_RSA_PSK_WITH_AES_256_CBC_SHA384 = 0x00B3
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 104
try:
    TLS_PSK_WITH_NULL_SHA = 0x002C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 105
try:
    TLS_DHE_PSK_WITH_NULL_SHA = 0x002D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 106
try:
    TLS_RSA_PSK_WITH_NULL_SHA = 0x002E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 107
try:
    TLS_PSK_WITH_NULL_SHA256 = 0x00B4
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 108
try:
    TLS_PSK_WITH_NULL_SHA384 = 0x00B5
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 109
try:
    TLS_DHE_PSK_WITH_NULL_SHA256 = 0x00B6
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 110
try:
    TLS_DHE_PSK_WITH_NULL_SHA384 = 0x00B7
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 111
try:
    TLS_RSA_PSK_WITH_NULL_SHA256 = 0x00B8
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 112
try:
    TLS_RSA_PSK_WITH_NULL_SHA384 = 0x00B9
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 113
try:
    TLS_ECDH_ECDSA_WITH_NULL_SHA = 0xC001
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 114
try:
    TLS_ECDH_ECDSA_WITH_RC4_128_SHA = 0xC002
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 115
try:
    TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA = 0xC003
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 116
try:
    TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA = 0xC004
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 117
try:
    TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA = 0xC005
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 118
try:
    TLS_ECDHE_ECDSA_WITH_NULL_SHA = 0xC006
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 119
try:
    TLS_ECDHE_ECDSA_WITH_RC4_128_SHA = 0xC007
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 120
try:
    TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA = 0xC008
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 121
try:
    TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA = 0xC009
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 122
try:
    TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA = 0xC00A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 123
try:
    TLS_ECDH_RSA_WITH_NULL_SHA = 0xC00B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 124
try:
    TLS_ECDH_RSA_WITH_RC4_128_SHA = 0xC00C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 125
try:
    TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA = 0xC00D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 126
try:
    TLS_ECDH_RSA_WITH_AES_128_CBC_SHA = 0xC00E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 127
try:
    TLS_ECDH_RSA_WITH_AES_256_CBC_SHA = 0xC00F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 128
try:
    TLS_ECDHE_RSA_WITH_NULL_SHA = 0xC010
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 129
try:
    TLS_ECDHE_RSA_WITH_RC4_128_SHA = 0xC011
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 130
try:
    TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA = 0xC012
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 131
try:
    TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA = 0xC013
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 132
try:
    TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA = 0xC014
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 133
try:
    TLS_ECDH_anon_WITH_NULL_SHA = 0xC015
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 134
try:
    TLS_ECDH_anon_WITH_RC4_128_SHA = 0xC016
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 135
try:
    TLS_ECDH_anon_WITH_3DES_EDE_CBC_SHA = 0xC017
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 136
try:
    TLS_ECDH_anon_WITH_AES_128_CBC_SHA = 0xC018
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 137
try:
    TLS_ECDH_anon_WITH_AES_256_CBC_SHA = 0xC019
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 138
try:
    TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 = 0xC023
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 139
try:
    TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384 = 0xC024
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 140
try:
    TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256 = 0xC025
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 141
try:
    TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384 = 0xC026
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 142
try:
    TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 = 0xC027
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 143
try:
    TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 = 0xC028
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 144
try:
    TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256 = 0xC029
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 145
try:
    TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384 = 0xC02A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 146
try:
    TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 = 0xC02B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 147
try:
    TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 = 0xC02C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 148
try:
    TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256 = 0xC02D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 149
try:
    TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384 = 0xC02E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 150
try:
    TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 = 0xC02F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 151
try:
    TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 = 0xC030
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 152
try:
    TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256 = 0xC031
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 153
try:
    TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384 = 0xC032
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 154
try:
    TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA = 0xC035
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 155
try:
    TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA = 0xC036
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 156
try:
    TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA256 = 0xC037
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 157
try:
    TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384 = 0xC038
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 158
try:
    TLS_ECDHE_PSK_WITH_NULL_SHA = 0xC039
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 159
try:
    TLS_ECDHE_PSK_WITH_NULL_SHA256 = 0xC03A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 160
try:
    TLS_ECDHE_PSK_WITH_NULL_SHA384 = 0xC03B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 161
try:
    TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_CBC_SHA256 = 0xC072
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 162
try:
    TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_CBC_SHA384 = 0xC073
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 163
try:
    TLS_ECDH_ECDSA_WITH_CAMELLIA_128_CBC_SHA256 = 0xC074
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 164
try:
    TLS_ECDH_ECDSA_WITH_CAMELLIA_256_CBC_SHA384 = 0xC075
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 165
try:
    TLS_ECDHE_RSA_WITH_CAMELLIA_128_CBC_SHA256 = 0xC076
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 166
try:
    TLS_ECDHE_RSA_WITH_CAMELLIA_256_CBC_SHA384 = 0xC077
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 167
try:
    TLS_ECDH_RSA_WITH_CAMELLIA_128_CBC_SHA256 = 0xC078
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 168
try:
    TLS_ECDH_RSA_WITH_CAMELLIA_256_CBC_SHA384 = 0xC079
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 169
try:
    TLS_RSA_WITH_ARIA_128_CBC_SHA256 = 0xC03C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 170
try:
    TLS_RSA_WITH_ARIA_256_CBC_SHA384 = 0xC03D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 171
try:
    TLS_DH_DSS_WITH_ARIA_128_CBC_SHA256 = 0xC03E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 172
try:
    TLS_DH_DSS_WITH_ARIA_256_CBC_SHA384 = 0xC03F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 173
try:
    TLS_DH_RSA_WITH_ARIA_128_CBC_SHA256 = 0xC040
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 174
try:
    TLS_DH_RSA_WITH_ARIA_256_CBC_SHA384 = 0xC041
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 175
try:
    TLS_DHE_DSS_WITH_ARIA_128_CBC_SHA256 = 0xC042
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 176
try:
    TLS_DHE_DSS_WITH_ARIA_256_CBC_SHA384 = 0xC043
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 177
try:
    TLS_DHE_RSA_WITH_ARIA_128_CBC_SHA256 = 0xC044
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 178
try:
    TLS_DHE_RSA_WITH_ARIA_256_CBC_SHA384 = 0xC045
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 179
try:
    TLS_DH_anon_WITH_ARIA_128_CBC_SHA256 = 0xC046
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 180
try:
    TLS_DH_anon_WITH_ARIA_256_CBC_SHA384 = 0xC047
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 181
try:
    TLS_ECDHE_ECDSA_WITH_ARIA_128_CBC_SHA256 = 0xC048
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 182
try:
    TLS_ECDHE_ECDSA_WITH_ARIA_256_CBC_SHA384 = 0xC049
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 183
try:
    TLS_ECDH_ECDSA_WITH_ARIA_128_CBC_SHA256 = 0xC04A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 184
try:
    TLS_ECDH_ECDSA_WITH_ARIA_256_CBC_SHA384 = 0xC04B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 185
try:
    TLS_ECDHE_RSA_WITH_ARIA_128_CBC_SHA256 = 0xC04C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 186
try:
    TLS_ECDHE_RSA_WITH_ARIA_256_CBC_SHA384 = 0xC04D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 187
try:
    TLS_ECDH_RSA_WITH_ARIA_128_CBC_SHA256 = 0xC04E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 188
try:
    TLS_ECDH_RSA_WITH_ARIA_256_CBC_SHA384 = 0xC04F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 189
try:
    TLS_RSA_WITH_ARIA_128_GCM_SHA256 = 0xC050
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 190
try:
    TLS_RSA_WITH_ARIA_256_GCM_SHA384 = 0xC051
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 191
try:
    TLS_DHE_RSA_WITH_ARIA_128_GCM_SHA256 = 0xC052
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 192
try:
    TLS_DHE_RSA_WITH_ARIA_256_GCM_SHA384 = 0xC053
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 193
try:
    TLS_DH_RSA_WITH_ARIA_128_GCM_SHA256 = 0xC054
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 194
try:
    TLS_DH_RSA_WITH_ARIA_256_GCM_SHA384 = 0xC055
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 195
try:
    TLS_DHE_DSS_WITH_ARIA_128_GCM_SHA256 = 0xC056
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 196
try:
    TLS_DHE_DSS_WITH_ARIA_256_GCM_SHA384 = 0xC057
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 197
try:
    TLS_DH_DSS_WITH_ARIA_128_GCM_SHA256 = 0xC058
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 198
try:
    TLS_DH_DSS_WITH_ARIA_256_GCM_SHA384 = 0xC059
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 199
try:
    TLS_DH_anon_WITH_ARIA_128_GCM_SHA256 = 0xC05A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 200
try:
    TLS_DH_anon_WITH_ARIA_256_GCM_SHA384 = 0xC05B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 201
try:
    TLS_ECDHE_ECDSA_WITH_ARIA_128_GCM_SHA256 = 0xC05C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 202
try:
    TLS_ECDHE_ECDSA_WITH_ARIA_256_GCM_SHA384 = 0xC05D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 203
try:
    TLS_ECDH_ECDSA_WITH_ARIA_128_GCM_SHA256 = 0xC05E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 204
try:
    TLS_ECDH_ECDSA_WITH_ARIA_256_GCM_SHA384 = 0xC05F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 205
try:
    TLS_ECDHE_RSA_WITH_ARIA_128_GCM_SHA256 = 0xC060
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 206
try:
    TLS_ECDHE_RSA_WITH_ARIA_256_GCM_SHA384 = 0xC061
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 207
try:
    TLS_ECDH_RSA_WITH_ARIA_128_GCM_SHA256 = 0xC062
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 208
try:
    TLS_ECDH_RSA_WITH_ARIA_256_GCM_SHA384 = 0xC063
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 209
try:
    TLS_PSK_WITH_ARIA_128_CBC_SHA256 = 0xC064
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 210
try:
    TLS_PSK_WITH_ARIA_256_CBC_SHA384 = 0xC065
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 211
try:
    TLS_DHE_PSK_WITH_ARIA_128_CBC_SHA256 = 0xC066
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 212
try:
    TLS_DHE_PSK_WITH_ARIA_256_CBC_SHA384 = 0xC067
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 213
try:
    TLS_RSA_PSK_WITH_ARIA_128_CBC_SHA256 = 0xC068
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 214
try:
    TLS_RSA_PSK_WITH_ARIA_256_CBC_SHA384 = 0xC069
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 215
try:
    TLS_PSK_WITH_ARIA_128_GCM_SHA256 = 0xC06A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 216
try:
    TLS_PSK_WITH_ARIA_256_GCM_SHA384 = 0xC06B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 217
try:
    TLS_DHE_PSK_WITH_ARIA_128_GCM_SHA256 = 0xC06C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 218
try:
    TLS_DHE_PSK_WITH_ARIA_256_GCM_SHA384 = 0xC06D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 219
try:
    TLS_RSA_PSK_WITH_ARIA_128_GCM_SHA256 = 0xC06E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 220
try:
    TLS_RSA_PSK_WITH_ARIA_256_GCM_SHA384 = 0xC06F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 221
try:
    TLS_ECDHE_PSK_WITH_ARIA_128_CBC_SHA256 = 0xC070
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 222
try:
    TLS_ECDHE_PSK_WITH_ARIA_256_CBC_SHA384 = 0xC071
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 223
try:
    TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_GCM_SHA256 = 0xC076
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 224
try:
    TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_GCM_SHA384 = 0xC077
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 225
try:
    TLS_ECDH_ECDSA_WITH_CAMELLIA_128_GCM_SHA256 = 0xC078
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 226
try:
    TLS_ECDH_ECDSA_WITH_CAMELLIA_256_GCM_SHA384 = 0xC079
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 227
try:
    TLS_ECDHE_RSA_WITH_CAMELLIA_128_GCM_SHA256 = 0xC07A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 228
try:
    TLS_ECDHE_RSA_WITH_CAMELLIA_256_GCM_SHA384 = 0xC07B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 229
try:
    TLS_ECDH_RSA_WITH_CAMELLIA_128_GCM_SHA256 = 0xC07C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 230
try:
    TLS_ECDH_RSA_WITH_CAMELLIA_256_GCM_SHA384 = 0xC07D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 231
try:
    TLS_PSK_WITH_CAMELLIA_128_GCM_SHA256 = 0xC07E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 232
try:
    TLS_PSK_WITH_CAMELLIA_256_GCM_SHA384 = 0xC07F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 233
try:
    TLS_DHE_PSK_WITH_CAMELLIA_128_GCM_SHA256 = 0xC080
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 234
try:
    TLS_DHE_PSK_WITH_CAMELLIA_256_GCM_SHA384 = 0xC081
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 235
try:
    TLS_RSA_PSK_WITH_CAMELLIA_128_GCM_SHA256 = 0xC082
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 236
try:
    TLS_RSA_PSK_WITH_CAMELLIA_256_GCM_SHA384 = 0xC083
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 237
try:
    TLS_ECDHE_PSK_WITH_CAMELLIA_128_GCM_SHA256 = 0xC084
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 238
try:
    TLS_ECDHE_PSK_WITH_CAMELLIA_256_GCM_SHA384 = 0xC085
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 239
try:
    TLS_RSA_WITH_AES_128_CCM = 0xC09C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 240
try:
    TLS_RSA_WITH_AES_256_CCM = 0xC09D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 241
try:
    TLS_DHE_RSA_WITH_AES_128_CCM = 0xC09E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 242
try:
    TLS_DHE_RSA_WITH_AES_256_CCM = 0xC09F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 243
try:
    TLS_RSA_WITH_AES_128_CCM_8 = 0xC0A0
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 244
try:
    TLS_RSA_WITH_AES_256_CCM_8 = 0xC0A1
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 245
try:
    TLS_DHE_RSA_WITH_AES_128_CCM_8 = 0xC0A2
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 246
try:
    TLS_DHE_RSA_WITH_AES_256_CCM_8 = 0xC0A3
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 247
try:
    TLS_PSK_WITH_AES_128_CCM = 0xC0A4
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 248
try:
    TLS_PSK_WITH_AES_256_CCM = 0xC0A5
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 249
try:
    TLS_DHE_PSK_WITH_AES_128_CCM = 0xC0A6
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 250
try:
    TLS_DHE_PSK_WITH_AES_256_CCM = 0xC0A7
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 251
try:
    TLS_PSK_WITH_AES_128_CCM_8 = 0xC0A8
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 252
try:
    TLS_PSK_WITH_AES_256_CCM_8 = 0xC0A9
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 253
try:
    TLS_PSK_DHE_WITH_AES_128_CCM_8 = 0xC0AA
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 254
try:
    TLS_PSK_DHE_WITH_AES_256_CCM_8 = 0xC0AB
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 255
try:
    TLS_ECDHE_ECDSA_WITH_AES_128_CCM = 0xC0AC
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 79
try:
    TLS_EVENT_CODE_ALM_ALGO_NOT_SUPPORTED = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 80
try:
    TLS_EVENT_CODE_ALM_UNSECURE_COMMUNICATION = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 81
try:
    TLS_EVENT_CODE_ALM_CERT_UNAVAILABLE = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 82
try:
    TLS_EVENT_CODE_ALM_BAD_CERT = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 83
try:
    TLS_EVENT_CODE_ALM_CERT_SIZE_EXCEEDED = 5
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 84
try:
    TLS_EVENT_CODE_ALM_CERT_VALIDATION_FAILED = 6
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 85
try:
    TLS_EVENT_CODE_ALM_CERT_REQUIRED = 7
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 86
try:
    TLS_EVENT_CODE_ALM_HANDSHAKE_FAILED_UNKNOWN_REASON = 8
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 87
try:
    TLS_EVENT_CODE_WRN_INSECURE_TLS_VERSION = 9
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 88
try:
    TLS_EVENT_CODE_INF_SESSION_RENEGOTIATION = 10
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 89
try:
    TLS_EVENT_CODE_ALM_CERT_EXPIRED = 11
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 90
try:
    TLS_EVENT_CODE_ALM_CERT_REVOKED = 12
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 91
try:
    TLS_EVENT_CODE_ALM_CERT_NOT_CONFIGURED = 13
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 92
try:
    TLS_EVENT_CODE_ALM_CERT_NOT_TRUSTED = 14
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 93
try:
    TLS_EVENT_CODE_ALM_NO_CIPHER = 15
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 94
try:
    TLS_EVENT_CODE_INF_SESSION_ESTABLISHED = 16
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 95
try:
    TLS_EVENT_CODE_WRN_CERT_EXPIRED = 17
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 96
try:
    TLS_EVENT_CODE_WRN_CERT_NOT_YET_VALID = 18
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 97
try:
    TLS_EVENT_CODE_WRN_CRL_EXPIRED = 19
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 98
try:
    TLS_EVENT_CODE_WRN_CRL_NOT_YET_VALID = 20
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 99
try:
    TLS_EVENT_CODE_ALM_TLS_VERSION_CHANGE = 21
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 100
try:
    TLS_EVENT_CODE_WRN_MIN_KEY_LENGTH = 22
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 101
try:
    TLS_EVENT_CODE_ALM_INSUFFICIENT_KEY_LENGTH = 23
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 102
try:
    TLS_EVENT_CODE_WRN_CRL_NOT_ACCESSIBLE = 24
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 103
try:
    TLS_EVENT_CODE_ALM_CA_CERT_NOT_AVAILABLE = 25
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 104
try:
    TLS_EVENT_CODE_ALM_RENEGOTIATION_TIMEOUT = 26
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 105
try:
    TLS_EVENT_CODE_INF_SESSION_RESUMED = 27
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 106
try:
    TLS_EVENT_CODE_INF_SESSION_EXPIRED = 28
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 45
try:
    IEC_60870_5_104_DEFAULT_PORT = 2404
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 46
try:
    IEC_60870_5_104_DEFAULT_TLS_PORT = 19998
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 48
try:
    LIB60870_VERSION_MAJOR = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 49
try:
    LIB60870_VERSION_MINOR = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 50
try:
    LIB60870_VERSION_PATCH = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 53
try:
    IEC60870_QUALITY_GOOD = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 54
try:
    IEC60870_QUALITY_OVERFLOW = 0x01
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 55
try:
    IEC60870_QUALITY_RESERVED = 0x04
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 56
try:
    IEC60870_QUALITY_ELAPSED_TIME_INVALID = 0x08
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 57
try:
    IEC60870_QUALITY_BLOCKED = 0x10
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 58
try:
    IEC60870_QUALITY_SUBSTITUTED = 0x20
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 59
try:
    IEC60870_QUALITY_NON_TOPICAL = 0x40
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 60
try:
    IEC60870_QUALITY_INVALID = 0x80
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 67
try:
    IEC60870_START_EVENT_NONE = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 68
try:
    IEC60870_START_EVENT_GS = 0x01
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 69
try:
    IEC60870_START_EVENT_SL1 = 0x02
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 70
try:
    IEC60870_START_EVENT_SL2 = 0x04
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 71
try:
    IEC60870_START_EVENT_SL3 = 0x08
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 72
try:
    IEC60870_START_EVENT_SIE = 0x10
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 73
try:
    IEC60870_START_EVENT_SRD = 0x20
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 74
try:
    IEC60870_START_EVENT_RES1 = 0x40
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 75
try:
    IEC60870_START_EVENT_RES2 = 0x80
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 82
try:
    IEC60870_OUTPUT_CI_GC = 0x01
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 83
try:
    IEC60870_OUTPUT_CI_CL1 = 0x02
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 84
try:
    IEC60870_OUTPUT_CI_CL2 = 0x04
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 85
try:
    IEC60870_OUTPUT_CI_CL3 = 0x08
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 101
try:
    IEC60870_QPM_NOT_USED = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 102
try:
    IEC60870_QPM_THRESHOLD_VALUE = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 103
try:
    IEC60870_QPM_SMOOTHING_FACTOR = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 104
try:
    IEC60870_QPM_LOW_LIMIT_FOR_TRANSMISSION = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 105
try:
    IEC60870_QPM_HIGH_LIMIT_FOR_TRANSMISSION = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 113
try:
    IEC60870_COI_LOCAL_SWITCH_ON = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 114
try:
    IEC60870_COI_LOCAL_MANUAL_RESET = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 115
try:
    IEC60870_COI_REMOTE_RESET = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 122
try:
    IEC60870_QOC_NO_ADDITIONAL_DEFINITION = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 123
try:
    IEC60870_QOC_SHORT_PULSE_DURATION = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 124
try:
    IEC60870_QOC_LONG_PULSE_DURATION = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 125
try:
    IEC60870_QOC_PERSISTANT_OUTPUT = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 133
try:
    IEC60870_SCQ_DEFAULT = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 134
try:
    IEC60870_SCQ_SELECT_FILE = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 135
try:
    IEC60870_SCQ_REQUEST_FILE = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 136
try:
    IEC60870_SCQ_DEACTIVATE_FILE = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 137
try:
    IEC60870_SCQ_DELETE_FILE = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 138
try:
    IEC60870_SCQ_SELECT_SECTION = 5
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 139
try:
    IEC60870_SCQ_REQUEST_SECTION = 6
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 140
try:
    IEC60870_SCQ_DEACTIVATE_SECTION = 7
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 148
try:
    IEC60870_QOI_STATION = 20
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 149
try:
    IEC60870_QOI_GROUP_1 = 21
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 150
try:
    IEC60870_QOI_GROUP_2 = 22
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 151
try:
    IEC60870_QOI_GROUP_3 = 23
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 152
try:
    IEC60870_QOI_GROUP_4 = 24
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 153
try:
    IEC60870_QOI_GROUP_5 = 25
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 154
try:
    IEC60870_QOI_GROUP_6 = 26
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 155
try:
    IEC60870_QOI_GROUP_7 = 27
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 156
try:
    IEC60870_QOI_GROUP_8 = 28
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 157
try:
    IEC60870_QOI_GROUP_9 = 29
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 158
try:
    IEC60870_QOI_GROUP_10 = 30
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 159
try:
    IEC60870_QOI_GROUP_11 = 31
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 160
try:
    IEC60870_QOI_GROUP_12 = 32
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 161
try:
    IEC60870_QOI_GROUP_13 = 33
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 162
try:
    IEC60870_QOI_GROUP_14 = 34
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 163
try:
    IEC60870_QOI_GROUP_15 = 35
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 164
try:
    IEC60870_QOI_GROUP_16 = 36
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 187
try:
    IEC60870_QCC_RQT_GROUP_1 = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 188
try:
    IEC60870_QCC_RQT_GROUP_2 = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 189
try:
    IEC60870_QCC_RQT_GROUP_3 = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 190
try:
    IEC60870_QCC_RQT_GROUP_4 = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 191
try:
    IEC60870_QCC_RQT_GENERAL = 5
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 193
try:
    IEC60870_QCC_FRZ_READ = 0x00
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 194
try:
    IEC60870_QCC_FRZ_FREEZE_WITHOUT_RESET = 0x40
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 195
try:
    IEC60870_QCC_FRZ_FREEZE_WITH_RESET = 0x80
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 196
try:
    IEC60870_QCC_FRZ_COUNTER_RESET = 0xc0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 203
try:
    IEC60870_QRP_NOT_USED = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 204
try:
    IEC60870_QRP_GENERAL_RESET = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 205
try:
    IEC60870_QRP_RESET_PENDING_INFO_WITH_TIME_TAG = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 213
try:
    IEC60870_QPA_NOT_USED = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 214
try:
    IEC60870_QPA_DE_ACT_PREV_LOADED_PARAMETER = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 215
try:
    IEC60870_QPA_DE_ACT_OBJECT_PARAMETER = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 216
try:
    IEC60870_QPA_DE_ACT_OBJECT_TRANSMISSION = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1817
try:
    CS101_NOF_DEFAULT = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1818
try:
    CS101_NOF_TRANSPARENT_FILE = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1819
try:
    CS101_NOF_DISTURBANCE_DATA = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1820
try:
    CS101_NOF_SEQUENCES_OF_EVENTS = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1821
try:
    CS101_NOF_SEQUENCES_OF_ANALOGUE_VALUES = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1833
try:
    CS101_SCQ_DEFAULT = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1834
try:
    CS101_SCQ_SELECT_FILE = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1835
try:
    CS101_SCQ_REQUEST_FILE = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1836
try:
    CS101_SCQ_DEACTIVATE_FILE = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1837
try:
    CS101_SCQ_DELETE_FILE = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1838
try:
    CS101_SCQ_SELECT_SECTION = 5
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1839
try:
    CS101_SCQ_REQUEST_SECTION = 6
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1840
try:
    CS101_SCQ_DEACTIVATE_SECTION = 7
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1853
try:
    CS101_LSQ_FILE_TRANSFER_WITHOUT_DEACT = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1854
try:
    CS101_LSQ_FILE_TRANSFER_WITH_DEACT = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1855
try:
    CS101_LSQ_SECTION_TRANSFER_WITHOUT_DEACT = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1856
try:
    CS101_LSQ_SECTION_TRANSFER_WITH_DEACT = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1869
try:
    CS101_AFQ_NOT_USED = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1872
try:
    CS101_AFQ_POS_ACK_FILE = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1875
try:
    CS101_AFQ_NEG_ACK_FILE = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1878
try:
    CS101_AFQ_POS_ACK_SECTION = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1881
try:
    CS101_AFQ_NEG_ACK_SECTION = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1894
try:
    CS101_FILE_ERROR_DEFAULT = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1897
try:
    CS101_FILE_ERROR_REQ_MEMORY_NOT_AVAILABLE = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1900
try:
    CS101_FILE_ERROR_CHECKSUM_FAILED = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1903
try:
    CS101_FILE_ERROR_UNEXPECTED_COMM_SERVICE = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1906
try:
    CS101_FILE_ERROR_UNEXPECTED_NAME_OF_FILE = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1909
try:
    CS101_FILE_ERROR_UNEXPECTED_NAME_OF_SECTION = 5
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1922
try:
    CS101_SOF_STATUS = 0x1f
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1925
try:
    CS101_SOF_LFD = 0x20
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1928
try:
    CS101_SOF_FOR = 0x40
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1931
try:
    CS101_SOF_FA = 0x80
except:
    pass

sSerialPort = struct_sSerialPort# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 39

sServerSocket = struct_sServerSocket# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 44

sUdpSocket = struct_sUdpSocket# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 46

sSocket = struct_sSocket# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 49

sHandleSet = struct_sHandleSet# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 52

sThread = struct_sThread# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 38

sTLSConfiguration = struct_sTLSConfiguration# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 38

sTLSConnection = struct_sTLSConnection# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 108

sTLSSocket = struct_sTLSSocket# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 48

sCS101_AppLayerParameters = struct_sCS101_AppLayerParameters# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 112

sInformationObject = struct_sInformationObject# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 211

sCS101_ASDU = struct_sCS101_ASDU# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 216

sCP16Time2a = struct_sCP16Time2a# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 231

sCP24Time2a = struct_sCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 237

sCP32Time2a = struct_sCP32Time2a# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 246

sCP56Time2a = struct_sCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 255

sBinaryCounterReading = struct_sBinaryCounterReading# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 264

sCS104_APCIParameters = struct_sCS104_APCIParameters# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 273

sIPeerConnection = struct_sIPeerConnection# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 883

sFrame = struct_sFrame# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 940

sStatusAndStatusChangeDetection = struct_sStatusAndStatusChangeDetection# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 266

sSinglePointInformation = struct_sSinglePointInformation# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 323

sSinglePointWithCP24Time2a = struct_sSinglePointWithCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 342

sSinglePointWithCP56Time2a = struct_sSinglePointWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 358

sDoublePointInformation = struct_sDoublePointInformation# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 375

sDoublePointWithCP24Time2a = struct_sDoublePointWithCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 394

sDoublePointWithCP56Time2a = struct_sDoublePointWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 410

sStepPositionInformation = struct_sStepPositionInformation# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 426

sStepPositionWithCP24Time2a = struct_sStepPositionWithCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 465

sStepPositionWithCP56Time2a = struct_sStepPositionWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 482

sBitString32 = struct_sBitString32# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 498

sBitstring32WithCP24Time2a = struct_sBitstring32WithCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 519

sBitstring32WithCP56Time2a = struct_sBitstring32WithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 537

sMeasuredValueNormalizedWithoutQuality = struct_sMeasuredValueNormalizedWithoutQuality# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 555

sMeasuredValueNormalized = struct_sMeasuredValueNormalized# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 573

sMeasuredValueNormalizedWithCP24Time2a = struct_sMeasuredValueNormalizedWithCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 594

sMeasuredValueNormalizedWithCP56Time2a = struct_sMeasuredValueNormalizedWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 613

sMeasuredValueScaled = struct_sMeasuredValueScaled# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 633

sMeasuredValueScaledWithCP24Time2a = struct_sMeasuredValueScaledWithCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 667

sMeasuredValueScaledWithCP56Time2a = struct_sMeasuredValueScaledWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 686

sMeasuredValueShort = struct_sMeasuredValueShort# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 705

sMeasuredValueShortWithCP24Time2a = struct_sMeasuredValueShortWithCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 726

sMeasuredValueShortWithCP56Time2a = struct_sMeasuredValueShortWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 746

sIntegratedTotals = struct_sIntegratedTotals# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 766

sIntegratedTotalsWithCP24Time2a = struct_sIntegratedTotalsWithCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 795

sIntegratedTotalsWithCP56Time2a = struct_sIntegratedTotalsWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 827

sIntegratedTotalsForSecurityStatistics = struct_sIntegratedTotalsForSecurityStatistics# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 859

sEventOfProtectionEquipment = struct_sEventOfProtectionEquipment# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 905

sPackedStartEventsOfProtectionEquipment = struct_sPackedStartEventsOfProtectionEquipment# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 927

sPackedOutputCircuitInfo = struct_sPackedOutputCircuitInfo# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 952

sPackedSinglePointWithSCD = struct_sPackedSinglePointWithSCD# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 977

sSingleCommand = struct_sSingleCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 997

sSingleCommandWithCP56Time2a = struct_sSingleCommandWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1042

sDoubleCommand = struct_sDoubleCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1077

sStepCommand = struct_sStepCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1124

sSetpointCommandNormalized = struct_sSetpointCommandNormalized# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1155

sSetpointCommandScaled = struct_sSetpointCommandScaled# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1192

sSetpointCommandShort = struct_sSetpointCommandShort# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1229

sBitstring32Command = struct_sBitstring32Command# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1266

sInterrogationCommand = struct_sInterrogationCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1281

sReadCommand = struct_sReadCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1296

sClockSynchronizationCommand = struct_sClockSynchronizationCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1308

sParameterActivation = struct_sParameterActivation# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1467

sEventOfProtectionEquipmentWithCP56Time2a = struct_sEventOfProtectionEquipmentWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1496

sPackedStartEventsOfProtectionEquipmentWithCP56Time2a = struct_sPackedStartEventsOfProtectionEquipmentWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1518

sPackedOutputCircuitInfoWithCP56Time2a = struct_sPackedOutputCircuitInfoWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1543

sDoubleCommandWithCP56Time2a = struct_sDoubleCommandWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1568

sStepCommandWithCP56Time2a = struct_sStepCommandWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1592

sSetpointCommandNormalizedWithCP56Time2a = struct_sSetpointCommandNormalizedWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1616

sSetpointCommandScaledWithCP56Time2a = struct_sSetpointCommandScaledWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1640

sSetpointCommandShortWithCP56Time2a = struct_sSetpointCommandShortWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1664

sBitstring32CommandWithCP56Time2a = struct_sBitstring32CommandWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1688

sCounterInterrogationCommand = struct_sCounterInterrogationCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1707

sTestCommand = struct_sTestCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1722

sTestCommandWithCP56Time2a = struct_sTestCommandWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1737

sResetProcessCommand = struct_sResetProcessCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1764

sDelayAcquisitionCommand = struct_sDelayAcquisitionCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1779

sEndOfInitialization = struct_sEndOfInitialization# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1794

sFileReady = struct_sFileReady# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1935

sSectionReady = struct_sSectionReady# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1973

sFileCallOrSelect = struct_sFileCallOrSelect# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2005

sFileLastSegmentOrSection = struct_sFileLastSegmentOrSection# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2026

sFileACK = struct_sFileACK# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2050

sFileSegment = struct_sFileSegment# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2071

sFileDirectory = struct_sFileDirectory# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2098

sQueryLog = struct_sQueryLog# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2134

sCS101_MasterPlugin = struct_sCS101_MasterPlugin# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_master.h: 71

sLinkLayerParameters = struct_sLinkLayerParameters# /home/user/lib60870/lib60870-C/src/inc/api/link_layer_parameters.h: 42

sCS101_Master = struct_sCS101_Master# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 60

sCS101_SlavePlugin = struct_sCS101_SlavePlugin# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 185

sCS101_Slave = struct_sCS101_Slave# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 63

sCS104_Connection = struct_sCS104_Connection# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 56

sCS104_Slave = struct_sCS104_Slave# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 54

sCS104_RedundancyGroup = struct_sCS104_RedundancyGroup# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 68

# No inserted files

# No prefix-stripping

