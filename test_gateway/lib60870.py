r"""Wrapper for hal_serial.h

Generated with:
/usr/local/bin/ctypesgen -l /usr/local/lib/lib60870.so -I ./lib60870-C/src/hal/inc/ ./lib60870-C/src/hal/inc/hal_serial.h ./lib60870-C/src/hal/inc/hal_time.h ./lib60870-C/src/hal/inc/hal_thread.h ./lib60870-C/src/hal/inc/hal_socket.h ./lib60870-C/src/hal/inc/hal_base.h ./lib60870-C/src/hal/inc/lib_memory.h ./lib60870-C/src/common/inc/linked_list.h ./lib60870-C/src/inc/api/iec60870_common.h ./lib60870-C/src/inc/api/cs101_information_objects.h ./lib60870-C/src/inc/api/cs104_slave.h ./lib60870-C/src/inc/api/cs104_connection.h ./lib60870-C/src/inc/api/cs101_master.h ./lib60870-C/src/inc/api/cs101_slave.h ./lib60870-C/src/inc/api/iec60870_slave.h ./lib60870-C/src/inc/api/iec60870_master.h ./lib60870-C/src/inc/api/link_layer_parameters.h -o lib60870.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python v(3, 2)

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
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

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)

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


class String(MutableString, Union):

    _fields_ = [("raw", POINTER(c_char)), ("data", c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

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
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from c_char array
        elif isinstance(obj, c_char * len(obj)):
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
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return c_void_p


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

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util


def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []


class LibraryLoader(object):
    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup(object):
        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
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
            try:
                return self.Lookup(path)
            except:
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

            # then we search the directory where the generated python interface is stored
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

    def getplatformpaths(self, libname):
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
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
        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir, name)

    def getdirs(self, libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser("~/lib"), "/usr/local/lib", "/usr/lib"]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        if hasattr(sys, "frozen") and sys.frozen == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    class _Directories(dict):
        def __init__(self):
            self.order = 0

        def add(self, directory):
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            o = self.setdefault(directory, self.order)
            if o == self.order:
                self.order += 1

        def extend(self, directories):
            for d in directories:
                self.add(d)

        def ordered(self):
            return (i[0] for i in sorted(self.items(), key=lambda D: D[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive funtion to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as f:
                for D in f:
                    D = D.strip()
                    if not D:
                        continue

                    m = self._include.match(D)
                    if not m:
                        dirs.add(D)
                    else:
                        for D2 in glob.glob(m.group("pattern")):
                            self._get_ld_so_conf_dirs(D2, dirs)
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
            "SHLIB_PATH",  # HPUX
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
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/x86_64-linux-gnu", "/usr/lib/x86_64-linux-gnu"]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        ext_re = re.compile(r"\.s[ol]$")
        for dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
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
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
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
    for F in other_dirs:
        if not os.path.isabs(F):
            F = os.path.abspath(F)
        load_library.other_dirs.append(F)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["/usr/local/lib/lib60870.so"] = load_library("/usr/local/lib/lib60870.so")

# 1 libraries
# End libraries

# No modules

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 39
class struct_sSerialPort(Structure):
    pass

SerialPort = POINTER(struct_sSerialPort)# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 39

enum_anon_20 = c_int# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_NONE = 0# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_INVALID_ARGUMENT = 1# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_INVALID_BAUDRATE = 2# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_OPEN_FAILED = 3# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_UNKNOWN = 99# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SerialPortError = enum_anon_20# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 61
if _libs["/usr/local/lib/lib60870.so"].has("SerialPort_create", "cdecl"):
    SerialPort_create = _libs["/usr/local/lib/lib60870.so"].get("SerialPort_create", "cdecl")
    SerialPort_create.argtypes = [String, c_int, c_uint8, c_char, c_uint8]
    SerialPort_create.restype = SerialPort

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 67
if _libs["/usr/local/lib/lib60870.so"].has("SerialPort_destroy", "cdecl"):
    SerialPort_destroy = _libs["/usr/local/lib/lib60870.so"].get("SerialPort_destroy", "cdecl")
    SerialPort_destroy.argtypes = [SerialPort]
    SerialPort_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 75
if _libs["/usr/local/lib/lib60870.so"].has("SerialPort_open", "cdecl"):
    SerialPort_open = _libs["/usr/local/lib/lib60870.so"].get("SerialPort_open", "cdecl")
    SerialPort_open.argtypes = [SerialPort]
    SerialPort_open.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 81
if _libs["/usr/local/lib/lib60870.so"].has("SerialPort_close", "cdecl"):
    SerialPort_close = _libs["/usr/local/lib/lib60870.so"].get("SerialPort_close", "cdecl")
    SerialPort_close.argtypes = [SerialPort]
    SerialPort_close.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 89
if _libs["/usr/local/lib/lib60870.so"].has("SerialPort_getBaudRate", "cdecl"):
    SerialPort_getBaudRate = _libs["/usr/local/lib/lib60870.so"].get("SerialPort_getBaudRate", "cdecl")
    SerialPort_getBaudRate.argtypes = [SerialPort]
    SerialPort_getBaudRate.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 97
if _libs["/usr/local/lib/lib60870.so"].has("SerialPort_setTimeout", "cdecl"):
    SerialPort_setTimeout = _libs["/usr/local/lib/lib60870.so"].get("SerialPort_setTimeout", "cdecl")
    SerialPort_setTimeout.argtypes = [SerialPort, c_int]
    SerialPort_setTimeout.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 103
if _libs["/usr/local/lib/lib60870.so"].has("SerialPort_discardInBuffer", "cdecl"):
    SerialPort_discardInBuffer = _libs["/usr/local/lib/lib60870.so"].get("SerialPort_discardInBuffer", "cdecl")
    SerialPort_discardInBuffer.argtypes = [SerialPort]
    SerialPort_discardInBuffer.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 111
if _libs["/usr/local/lib/lib60870.so"].has("SerialPort_readByte", "cdecl"):
    SerialPort_readByte = _libs["/usr/local/lib/lib60870.so"].get("SerialPort_readByte", "cdecl")
    SerialPort_readByte.argtypes = [SerialPort]
    SerialPort_readByte.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 123
if _libs["/usr/local/lib/lib60870.so"].has("SerialPort_write", "cdecl"):
    SerialPort_write = _libs["/usr/local/lib/lib60870.so"].get("SerialPort_write", "cdecl")
    SerialPort_write.argtypes = [SerialPort, POINTER(c_uint8), c_int, c_int]
    SerialPort_write.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 129
if _libs["/usr/local/lib/lib60870.so"].has("SerialPort_getLastError", "cdecl"):
    SerialPort_getLastError = _libs["/usr/local/lib/lib60870.so"].get("SerialPort_getLastError", "cdecl")
    SerialPort_getLastError.argtypes = [SerialPort]
    SerialPort_getLastError.restype = SerialPortError

nsSinceEpoch = c_uint64# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_time.h: 35

msSinceEpoch = c_uint64# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_time.h: 36

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_time.h: 47
if _libs["/usr/local/lib/lib60870.so"].has("Hal_getTimeInMs", "cdecl"):
    Hal_getTimeInMs = _libs["/usr/local/lib/lib60870.so"].get("Hal_getTimeInMs", "cdecl")
    Hal_getTimeInMs.argtypes = []
    Hal_getTimeInMs.restype = msSinceEpoch

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_time.h: 58
if _libs["/usr/local/lib/lib60870.so"].has("Hal_getTimeInNs", "cdecl"):
    Hal_getTimeInNs = _libs["/usr/local/lib/lib60870.so"].get("Hal_getTimeInNs", "cdecl")
    Hal_getTimeInNs.argtypes = []
    Hal_getTimeInNs.restype = nsSinceEpoch

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_time.h: 69
if _libs["/usr/local/lib/lib60870.so"].has("Hal_setTimeInNs", "cdecl"):
    Hal_setTimeInNs = _libs["/usr/local/lib/lib60870.so"].get("Hal_setTimeInNs", "cdecl")
    Hal_setTimeInNs.argtypes = [nsSinceEpoch]
    Hal_setTimeInNs.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 38
class struct_sThread(Structure):
    pass

Thread = POINTER(struct_sThread)# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 38

Semaphore = POINTER(None)# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 41

ThreadExecutionFunction = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(None))# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 44

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 56
if _libs["/usr/local/lib/lib60870.so"].has("Thread_create", "cdecl"):
    Thread_create = _libs["/usr/local/lib/lib60870.so"].get("Thread_create", "cdecl")
    Thread_create.argtypes = [ThreadExecutionFunction, POINTER(None), c_bool]
    Thread_create.restype = Thread

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 67
if _libs["/usr/local/lib/lib60870.so"].has("Thread_start", "cdecl"):
    Thread_start = _libs["/usr/local/lib/lib60870.so"].get("Thread_start", "cdecl")
    Thread_start.argtypes = [Thread]
    Thread_start.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 75
if _libs["/usr/local/lib/lib60870.so"].has("Thread_destroy", "cdecl"):
    Thread_destroy = _libs["/usr/local/lib/lib60870.so"].get("Thread_destroy", "cdecl")
    Thread_destroy.argtypes = [Thread]
    Thread_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 81
if _libs["/usr/local/lib/lib60870.so"].has("Thread_sleep", "cdecl"):
    Thread_sleep = _libs["/usr/local/lib/lib60870.so"].get("Thread_sleep", "cdecl")
    Thread_sleep.argtypes = [c_int]
    Thread_sleep.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 84
if _libs["/usr/local/lib/lib60870.so"].has("Semaphore_create", "cdecl"):
    Semaphore_create = _libs["/usr/local/lib/lib60870.so"].get("Semaphore_create", "cdecl")
    Semaphore_create.argtypes = [c_int]
    Semaphore_create.restype = Semaphore

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 88
if _libs["/usr/local/lib/lib60870.so"].has("Semaphore_wait", "cdecl"):
    Semaphore_wait = _libs["/usr/local/lib/lib60870.so"].get("Semaphore_wait", "cdecl")
    Semaphore_wait.argtypes = [Semaphore]
    Semaphore_wait.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 91
if _libs["/usr/local/lib/lib60870.so"].has("Semaphore_post", "cdecl"):
    Semaphore_post = _libs["/usr/local/lib/lib60870.so"].get("Semaphore_post", "cdecl")
    Semaphore_post.argtypes = [Semaphore]
    Semaphore_post.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 94
if _libs["/usr/local/lib/lib60870.so"].has("Semaphore_destroy", "cdecl"):
    Semaphore_destroy = _libs["/usr/local/lib/lib60870.so"].get("Semaphore_destroy", "cdecl")
    Semaphore_destroy.argtypes = [Semaphore]
    Semaphore_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 44
class struct_sServerSocket(Structure):
    pass

ServerSocket = POINTER(struct_sServerSocket)# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 44

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 46
class struct_sUdpSocket(Structure):
    pass

UdpSocket = POINTER(struct_sUdpSocket)# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 46

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 49
class struct_sSocket(Structure):
    pass

Socket = POINTER(struct_sSocket)# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 49

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 52
class struct_sHandleSet(Structure):
    pass

HandleSet = POINTER(struct_sHandleSet)# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 52

enum_anon_21 = c_int# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 60

SOCKET_STATE_CONNECTING = 0# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 60

SOCKET_STATE_FAILED = 1# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 60

SOCKET_STATE_CONNECTED = 2# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 60

SocketState = enum_anon_21# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 60

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 69
if _libs["/usr/local/lib/lib60870.so"].has("Handleset_new", "cdecl"):
    Handleset_new = _libs["/usr/local/lib/lib60870.so"].get("Handleset_new", "cdecl")
    Handleset_new.argtypes = []
    Handleset_new.restype = HandleSet

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 75
if _libs["/usr/local/lib/lib60870.so"].has("Handleset_reset", "cdecl"):
    Handleset_reset = _libs["/usr/local/lib/lib60870.so"].get("Handleset_reset", "cdecl")
    Handleset_reset.argtypes = [HandleSet]
    Handleset_reset.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 84
if _libs["/usr/local/lib/lib60870.so"].has("Handleset_addSocket", "cdecl"):
    Handleset_addSocket = _libs["/usr/local/lib/lib60870.so"].get("Handleset_addSocket", "cdecl")
    Handleset_addSocket.argtypes = [HandleSet, Socket]
    Handleset_addSocket.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 90
if _libs["/usr/local/lib/lib60870.so"].has("Handleset_removeSocket", "cdecl"):
    Handleset_removeSocket = _libs["/usr/local/lib/lib60870.so"].get("Handleset_removeSocket", "cdecl")
    Handleset_removeSocket.argtypes = [HandleSet, Socket]
    Handleset_removeSocket.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 108
if _libs["/usr/local/lib/lib60870.so"].has("Handleset_waitReady", "cdecl"):
    Handleset_waitReady = _libs["/usr/local/lib/lib60870.so"].get("Handleset_waitReady", "cdecl")
    Handleset_waitReady.argtypes = [HandleSet, c_uint]
    Handleset_waitReady.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 116
if _libs["/usr/local/lib/lib60870.so"].has("Handleset_destroy", "cdecl"):
    Handleset_destroy = _libs["/usr/local/lib/lib60870.so"].get("Handleset_destroy", "cdecl")
    Handleset_destroy.argtypes = [HandleSet]
    Handleset_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 129
if _libs["/usr/local/lib/lib60870.so"].has("TcpServerSocket_create", "cdecl"):
    TcpServerSocket_create = _libs["/usr/local/lib/lib60870.so"].get("TcpServerSocket_create", "cdecl")
    TcpServerSocket_create.argtypes = [String, c_int]
    TcpServerSocket_create.restype = ServerSocket

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 132
if _libs["/usr/local/lib/lib60870.so"].has("UdpSocket_create", "cdecl"):
    UdpSocket_create = _libs["/usr/local/lib/lib60870.so"].get("UdpSocket_create", "cdecl")
    UdpSocket_create.argtypes = []
    UdpSocket_create.restype = UdpSocket

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 135
if _libs["/usr/local/lib/lib60870.so"].has("UdpSocket_bind", "cdecl"):
    UdpSocket_bind = _libs["/usr/local/lib/lib60870.so"].get("UdpSocket_bind", "cdecl")
    UdpSocket_bind.argtypes = [UdpSocket, String, c_int]
    UdpSocket_bind.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 138
if _libs["/usr/local/lib/lib60870.so"].has("UdpSocket_sendTo", "cdecl"):
    UdpSocket_sendTo = _libs["/usr/local/lib/lib60870.so"].get("UdpSocket_sendTo", "cdecl")
    UdpSocket_sendTo.argtypes = [UdpSocket, String, c_int, POINTER(c_uint8), c_int]
    UdpSocket_sendTo.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 152
if _libs["/usr/local/lib/lib60870.so"].has("UdpSocket_receiveFrom", "cdecl"):
    UdpSocket_receiveFrom = _libs["/usr/local/lib/lib60870.so"].get("UdpSocket_receiveFrom", "cdecl")
    UdpSocket_receiveFrom.argtypes = [UdpSocket, String, c_int, POINTER(c_uint8), c_int]
    UdpSocket_receiveFrom.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 156
if _libs["/usr/local/lib/lib60870.so"].has("ServerSocket_listen", "cdecl"):
    ServerSocket_listen = _libs["/usr/local/lib/lib60870.so"].get("ServerSocket_listen", "cdecl")
    ServerSocket_listen.argtypes = [ServerSocket]
    ServerSocket_listen.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 173
if _libs["/usr/local/lib/lib60870.so"].has("ServerSocket_accept", "cdecl"):
    ServerSocket_accept = _libs["/usr/local/lib/lib60870.so"].get("ServerSocket_accept", "cdecl")
    ServerSocket_accept.argtypes = [ServerSocket]
    ServerSocket_accept.restype = Socket

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 186
if _libs["/usr/local/lib/lib60870.so"].has("Socket_activateTcpKeepAlive", "cdecl"):
    Socket_activateTcpKeepAlive = _libs["/usr/local/lib/lib60870.so"].get("Socket_activateTcpKeepAlive", "cdecl")
    Socket_activateTcpKeepAlive.argtypes = [Socket, c_int, c_int, c_int]
    Socket_activateTcpKeepAlive.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 198
if _libs["/usr/local/lib/lib60870.so"].has("ServerSocket_setBacklog", "cdecl"):
    ServerSocket_setBacklog = _libs["/usr/local/lib/lib60870.so"].get("ServerSocket_setBacklog", "cdecl")
    ServerSocket_setBacklog.argtypes = [ServerSocket, c_int]
    ServerSocket_setBacklog.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 210
if _libs["/usr/local/lib/lib60870.so"].has("ServerSocket_destroy", "cdecl"):
    ServerSocket_destroy = _libs["/usr/local/lib/lib60870.so"].get("ServerSocket_destroy", "cdecl")
    ServerSocket_destroy.argtypes = [ServerSocket]
    ServerSocket_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 220
if _libs["/usr/local/lib/lib60870.so"].has("TcpSocket_create", "cdecl"):
    TcpSocket_create = _libs["/usr/local/lib/lib60870.so"].get("TcpSocket_create", "cdecl")
    TcpSocket_create.argtypes = []
    TcpSocket_create.restype = Socket

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 229
if _libs["/usr/local/lib/lib60870.so"].has("Socket_setConnectTimeout", "cdecl"):
    Socket_setConnectTimeout = _libs["/usr/local/lib/lib60870.so"].get("Socket_setConnectTimeout", "cdecl")
    Socket_setConnectTimeout.argtypes = [Socket, c_uint32]
    Socket_setConnectTimeout.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 243
if _libs["/usr/local/lib/lib60870.so"].has("Socket_bind", "cdecl"):
    Socket_bind = _libs["/usr/local/lib/lib60870.so"].get("Socket_bind", "cdecl")
    Socket_bind.argtypes = [Socket, String, c_int]
    Socket_bind.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 264
if _libs["/usr/local/lib/lib60870.so"].has("Socket_connect", "cdecl"):
    Socket_connect = _libs["/usr/local/lib/lib60870.so"].get("Socket_connect", "cdecl")
    Socket_connect.argtypes = [Socket, String, c_int]
    Socket_connect.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 267
if _libs["/usr/local/lib/lib60870.so"].has("Socket_connectAsync", "cdecl"):
    Socket_connectAsync = _libs["/usr/local/lib/lib60870.so"].get("Socket_connectAsync", "cdecl")
    Socket_connectAsync.argtypes = [Socket, String, c_int]
    Socket_connectAsync.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 270
if _libs["/usr/local/lib/lib60870.so"].has("Socket_checkAsyncConnectState", "cdecl"):
    Socket_checkAsyncConnectState = _libs["/usr/local/lib/lib60870.so"].get("Socket_checkAsyncConnectState", "cdecl")
    Socket_checkAsyncConnectState.argtypes = [Socket]
    Socket_checkAsyncConnectState.restype = SocketState

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 289
if _libs["/usr/local/lib/lib60870.so"].has("Socket_read", "cdecl"):
    Socket_read = _libs["/usr/local/lib/lib60870.so"].get("Socket_read", "cdecl")
    Socket_read.argtypes = [Socket, POINTER(c_uint8), c_int]
    Socket_read.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 301
if _libs["/usr/local/lib/lib60870.so"].has("Socket_write", "cdecl"):
    Socket_write = _libs["/usr/local/lib/lib60870.so"].get("Socket_write", "cdecl")
    Socket_write.argtypes = [Socket, POINTER(c_uint8), c_int]
    Socket_write.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 303
if _libs["/usr/local/lib/lib60870.so"].has("Socket_getLocalAddress", "cdecl"):
    Socket_getLocalAddress = _libs["/usr/local/lib/lib60870.so"].get("Socket_getLocalAddress", "cdecl")
    Socket_getLocalAddress.argtypes = [Socket]
    if sizeof(c_int) == sizeof(c_void_p):
        Socket_getLocalAddress.restype = ReturnString
    else:
        Socket_getLocalAddress.restype = String
        Socket_getLocalAddress.errcheck = ReturnString

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 317
if _libs["/usr/local/lib/lib60870.so"].has("Socket_getPeerAddress", "cdecl"):
    Socket_getPeerAddress = _libs["/usr/local/lib/lib60870.so"].get("Socket_getPeerAddress", "cdecl")
    Socket_getPeerAddress.argtypes = [Socket]
    if sizeof(c_int) == sizeof(c_void_p):
        Socket_getPeerAddress.restype = ReturnString
    else:
        Socket_getPeerAddress.restype = String
        Socket_getPeerAddress.errcheck = ReturnString

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 334
if _libs["/usr/local/lib/lib60870.so"].has("Socket_getPeerAddressStatic", "cdecl"):
    Socket_getPeerAddressStatic = _libs["/usr/local/lib/lib60870.so"].get("Socket_getPeerAddressStatic", "cdecl")
    Socket_getPeerAddressStatic.argtypes = [Socket, String]
    if sizeof(c_int) == sizeof(c_void_p):
        Socket_getPeerAddressStatic.restype = ReturnString
    else:
        Socket_getPeerAddressStatic.restype = String
        Socket_getPeerAddressStatic.errcheck = ReturnString

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 348
if _libs["/usr/local/lib/lib60870.so"].has("Socket_destroy", "cdecl"):
    Socket_destroy = _libs["/usr/local/lib/lib60870.so"].get("Socket_destroy", "cdecl")
    Socket_destroy.argtypes = [Socket]
    Socket_destroy.restype = None

MemoryExceptionHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None))# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 32

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 35
if _libs["/usr/local/lib/lib60870.so"].has("Memory_installExceptionHandler", "cdecl"):
    Memory_installExceptionHandler = _libs["/usr/local/lib/lib60870.so"].get("Memory_installExceptionHandler", "cdecl")
    Memory_installExceptionHandler.argtypes = [MemoryExceptionHandler, POINTER(None)]
    Memory_installExceptionHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 37
if _libs["/usr/local/lib/lib60870.so"].has("Memory_malloc", "cdecl"):
    Memory_malloc = _libs["/usr/local/lib/lib60870.so"].get("Memory_malloc", "cdecl")
    Memory_malloc.argtypes = [c_size_t]
    Memory_malloc.restype = POINTER(c_ubyte)
    Memory_malloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 40
if _libs["/usr/local/lib/lib60870.so"].has("Memory_calloc", "cdecl"):
    Memory_calloc = _libs["/usr/local/lib/lib60870.so"].get("Memory_calloc", "cdecl")
    Memory_calloc.argtypes = [c_size_t, c_size_t]
    Memory_calloc.restype = POINTER(c_ubyte)
    Memory_calloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 43
if _libs["/usr/local/lib/lib60870.so"].has("Memory_realloc", "cdecl"):
    Memory_realloc = _libs["/usr/local/lib/lib60870.so"].get("Memory_realloc", "cdecl")
    Memory_realloc.argtypes = [POINTER(None), c_size_t]
    Memory_realloc.restype = POINTER(c_ubyte)
    Memory_realloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 47
if _libs["/usr/local/lib/lib60870.so"].has("Memory_free", "cdecl"):
    Memory_free = _libs["/usr/local/lib/lib60870.so"].get("Memory_free", "cdecl")
    Memory_free.argtypes = [POINTER(None)]
    Memory_free.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/common/inc/linked_list.h: 42
class struct_sLinkedList(Structure):
    pass

struct_sLinkedList.__slots__ = [
    'data',
    'next',
]
struct_sLinkedList._fields_ = [
    ('data', POINTER(None)),
    ('next', POINTER(struct_sLinkedList)),
]

LinkedList = POINTER(struct_sLinkedList)# /home/user/Desktop/scada/lib60870/lib60870-C/src/common/inc/linked_list.h: 50

# /home/user/Desktop/scada/lib60870/lib60870-C/src/common/inc/linked_list.h: 58
if _libs["/usr/local/lib/lib60870.so"].has("LinkedList_create", "cdecl"):
    LinkedList_create = _libs["/usr/local/lib/lib60870.so"].get("LinkedList_create", "cdecl")
    LinkedList_create.argtypes = []
    LinkedList_create.restype = LinkedList

# /home/user/Desktop/scada/lib60870/lib60870-C/src/common/inc/linked_list.h: 70
if _libs["/usr/local/lib/lib60870.so"].has("LinkedList_destroy", "cdecl"):
    LinkedList_destroy = _libs["/usr/local/lib/lib60870.so"].get("LinkedList_destroy", "cdecl")
    LinkedList_destroy.argtypes = [LinkedList]
    LinkedList_destroy.restype = None

LinkedListValueDeleteFunction = CFUNCTYPE(UNCHECKED(None), POINTER(None))# /home/user/Desktop/scada/lib60870/lib60870-C/src/common/inc/linked_list.h: 73

# /home/user/Desktop/scada/lib60870/lib60870-C/src/common/inc/linked_list.h: 87
if _libs["/usr/local/lib/lib60870.so"].has("LinkedList_destroyDeep", "cdecl"):
    LinkedList_destroyDeep = _libs["/usr/local/lib/lib60870.so"].get("LinkedList_destroyDeep", "cdecl")
    LinkedList_destroyDeep.argtypes = [LinkedList, LinkedListValueDeleteFunction]
    LinkedList_destroyDeep.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/common/inc/linked_list.h: 98
if _libs["/usr/local/lib/lib60870.so"].has("LinkedList_destroyStatic", "cdecl"):
    LinkedList_destroyStatic = _libs["/usr/local/lib/lib60870.so"].get("LinkedList_destroyStatic", "cdecl")
    LinkedList_destroyStatic.argtypes = [LinkedList]
    LinkedList_destroyStatic.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/common/inc/linked_list.h: 110
if _libs["/usr/local/lib/lib60870.so"].has("LinkedList_add", "cdecl"):
    LinkedList_add = _libs["/usr/local/lib/lib60870.so"].get("LinkedList_add", "cdecl")
    LinkedList_add.argtypes = [LinkedList, POINTER(None)]
    LinkedList_add.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/common/inc/linked_list.h: 119
if _libs["/usr/local/lib/lib60870.so"].has("LinkedList_remove", "cdecl"):
    LinkedList_remove = _libs["/usr/local/lib/lib60870.so"].get("LinkedList_remove", "cdecl")
    LinkedList_remove.argtypes = [LinkedList, POINTER(None)]
    LinkedList_remove.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/common/inc/linked_list.h: 128
if _libs["/usr/local/lib/lib60870.so"].has("LinkedList_get", "cdecl"):
    LinkedList_get = _libs["/usr/local/lib/lib60870.so"].get("LinkedList_get", "cdecl")
    LinkedList_get.argtypes = [LinkedList, c_int]
    LinkedList_get.restype = LinkedList

# /home/user/Desktop/scada/lib60870/lib60870-C/src/common/inc/linked_list.h: 136
if _libs["/usr/local/lib/lib60870.so"].has("LinkedList_getNext", "cdecl"):
    LinkedList_getNext = _libs["/usr/local/lib/lib60870.so"].get("LinkedList_getNext", "cdecl")
    LinkedList_getNext.argtypes = [LinkedList]
    LinkedList_getNext.restype = LinkedList

# /home/user/Desktop/scada/lib60870/lib60870-C/src/common/inc/linked_list.h: 144
if _libs["/usr/local/lib/lib60870.so"].has("LinkedList_getLastElement", "cdecl"):
    LinkedList_getLastElement = _libs["/usr/local/lib/lib60870.so"].get("LinkedList_getLastElement", "cdecl")
    LinkedList_getLastElement.argtypes = [LinkedList]
    LinkedList_getLastElement.restype = LinkedList

# /home/user/Desktop/scada/lib60870/lib60870-C/src/common/inc/linked_list.h: 152
if _libs["/usr/local/lib/lib60870.so"].has("LinkedList_insertAfter", "cdecl"):
    LinkedList_insertAfter = _libs["/usr/local/lib/lib60870.so"].get("LinkedList_insertAfter", "cdecl")
    LinkedList_insertAfter.argtypes = [LinkedList, POINTER(None)]
    LinkedList_insertAfter.restype = LinkedList

# /home/user/Desktop/scada/lib60870/lib60870-C/src/common/inc/linked_list.h: 162
if _libs["/usr/local/lib/lib60870.so"].has("LinkedList_size", "cdecl"):
    LinkedList_size = _libs["/usr/local/lib/lib60870.so"].get("LinkedList_size", "cdecl")
    LinkedList_size.argtypes = [LinkedList]
    LinkedList_size.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/common/inc/linked_list.h: 164
if _libs["/usr/local/lib/lib60870.so"].has("LinkedList_getData", "cdecl"):
    LinkedList_getData = _libs["/usr/local/lib/lib60870.so"].get("LinkedList_getData", "cdecl")
    LinkedList_getData.argtypes = [LinkedList]
    LinkedList_getData.restype = POINTER(c_ubyte)
    LinkedList_getData.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 59
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

Lib60870VersionInfo = struct_anon_22# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 59

enum_anon_23 = c_int# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 67

IEC60870_LINK_LAYER_BALANCED = 0# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 67

IEC60870_LINK_LAYER_UNBALANCED = 1# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 67

IEC60870_LinkLayerMode = enum_anon_23# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 67

enum_anon_24 = c_int# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

LL_STATE_IDLE = 0# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

LL_STATE_ERROR = (LL_STATE_IDLE + 1)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

LL_STATE_BUSY = (LL_STATE_ERROR + 1)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

LL_STATE_AVAILABLE = (LL_STATE_BUSY + 1)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

LinkLayerState = enum_anon_24# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

IEC60870_LinkLayerStateChangedHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, LinkLayerState)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 91

IEC60870_RawMessageHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(c_uint8), c_int, c_bool)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 105

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 112
class struct_sCS101_AppLayerParameters(Structure):
    pass

CS101_AppLayerParameters = POINTER(struct_sCS101_AppLayerParameters)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 110

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

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 125
class struct_sCS101_ASDU(Structure):
    pass

CS101_ASDU = POINTER(struct_sCS101_ASDU)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 125

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 134
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'parameters',
    'asdu',
    'asduHeaderLength',
    'payload',
    'payloadSize',
    'encodedData',
]
struct_anon_25._fields_ = [
    ('parameters', CS101_AppLayerParameters),
    ('asdu', POINTER(c_uint8)),
    ('asduHeaderLength', c_int),
    ('payload', POINTER(c_uint8)),
    ('payloadSize', c_int),
    ('encodedData', c_uint8 * int(256)),
]

sCS101_StaticASDU = struct_anon_25# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 134

CS101_StaticASDU = POINTER(sCS101_StaticASDU)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 136

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 140
class struct_sCP16Time2a(Structure):
    pass

CP16Time2a = POINTER(struct_sCP16Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 138

struct_sCP16Time2a.__slots__ = [
    'encodedValue',
]
struct_sCP16Time2a._fields_ = [
    ('encodedValue', c_uint8 * int(2)),
]

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 146
class struct_sCP24Time2a(Structure):
    pass

CP24Time2a = POINTER(struct_sCP24Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 144

struct_sCP24Time2a.__slots__ = [
    'encodedValue',
]
struct_sCP24Time2a._fields_ = [
    ('encodedValue', c_uint8 * int(3)),
]

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 155
class struct_sCP32Time2a(Structure):
    pass

CP32Time2a = POINTER(struct_sCP32Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 150

struct_sCP32Time2a.__slots__ = [
    'encodedValue',
]
struct_sCP32Time2a._fields_ = [
    ('encodedValue', c_uint8 * int(4)),
]

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 164
class struct_sCP56Time2a(Structure):
    pass

CP56Time2a = POINTER(struct_sCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 162

struct_sCP56Time2a.__slots__ = [
    'encodedValue',
]
struct_sCP56Time2a._fields_ = [
    ('encodedValue', c_uint8 * int(7)),
]

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 173
class struct_sBinaryCounterReading(Structure):
    pass

BinaryCounterReading = POINTER(struct_sBinaryCounterReading)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 171

struct_sBinaryCounterReading.__slots__ = [
    'encodedValue',
]
struct_sBinaryCounterReading._fields_ = [
    ('encodedValue', c_uint8 * int(5)),
]

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 182
class struct_sCS104_APCIParameters(Structure):
    pass

CS104_APCIParameters = POINTER(struct_sCS104_APCIParameters)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 180

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

enum_anon_26 = c_int# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_SP_NA_1 = 1# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_SP_TA_1 = 2# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_DP_NA_1 = 3# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_DP_TA_1 = 4# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_ST_NA_1 = 5# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_ST_TA_1 = 6# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_BO_NA_1 = 7# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_BO_TA_1 = 8# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_ME_NA_1 = 9# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_ME_TA_1 = 10# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_ME_NB_1 = 11# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_ME_TB_1 = 12# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_ME_NC_1 = 13# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_ME_TC_1 = 14# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_IT_NA_1 = 15# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_IT_TA_1 = 16# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_EP_TA_1 = 17# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_EP_TB_1 = 18# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_EP_TC_1 = 19# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_PS_NA_1 = 20# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_ME_ND_1 = 21# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_SP_TB_1 = 30# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_DP_TB_1 = 31# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_ST_TB_1 = 32# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_BO_TB_1 = 33# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_ME_TD_1 = 34# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_ME_TE_1 = 35# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_ME_TF_1 = 36# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_IT_TB_1 = 37# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_EP_TD_1 = 38# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_EP_TE_1 = 39# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_EP_TF_1 = 40# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

S_IT_TC_1 = 41# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_SC_NA_1 = 45# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_DC_NA_1 = 46# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_RC_NA_1 = 47# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_SE_NA_1 = 48# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_SE_NB_1 = 49# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_SE_NC_1 = 50# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_BO_NA_1 = 51# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_SC_TA_1 = 58# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_DC_TA_1 = 59# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_RC_TA_1 = 60# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_SE_TA_1 = 61# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_SE_TB_1 = 62# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_SE_TC_1 = 63# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_BO_TA_1 = 64# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

M_EI_NA_1 = 70# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

S_CH_NA_1 = 81# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

S_RP_NA_1 = 82# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

S_AR_NA_1 = 83# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

S_KR_NA_1 = 84# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

S_KS_NA_1 = 85# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

S_KC_NA_1 = 86# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

S_ER_NA_1 = 87# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

S_US_NA_1 = 90# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

S_UQ_NA_1 = 91# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

S_UR_NA_1 = 92# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

S_UK_NA_1 = 93# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

S_UA_NA_1 = 94# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

S_UC_NA_1 = 95# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_IC_NA_1 = 100# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_CI_NA_1 = 101# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_RD_NA_1 = 102# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_CS_NA_1 = 103# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_TS_NA_1 = 104# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_RP_NA_1 = 105# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_CD_NA_1 = 106# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

C_TS_TA_1 = 107# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

P_ME_NA_1 = 110# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

P_ME_NB_1 = 111# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

P_ME_NC_1 = 112# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

P_AC_NA_1 = 113# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

F_FR_NA_1 = 120# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

F_SR_NA_1 = 121# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

F_SC_NA_1 = 122# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

F_LS_NA_1 = 123# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

F_AF_NA_1 = 124# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

F_SG_NA_1 = 125# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

F_DR_TA_1 = 126# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

F_SC_NB_1 = 127# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

IEC60870_5_TypeID = enum_anon_26# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 126

TypeID = IEC60870_5_TypeID# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 128

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 130
if _libs["/usr/local/lib/lib60870.so"].has("TypeID_toString", "cdecl"):
    TypeID_toString = _libs["/usr/local/lib/lib60870.so"].get("TypeID_toString", "cdecl")
    TypeID_toString.argtypes = [TypeID]
    TypeID_toString.restype = c_char_p

QualityDescriptor = c_uint8# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 133

QualityDescriptorP = c_uint8# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 138

StartEvent = c_uint8# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 152

OutputCircuitInfo = c_uint8# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 167

QualifierOfParameterMV = c_uint8# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 186

CauseOfInitialization = c_uint8# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 198

QualifierOfCommand = c_uint8# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 207

SelectAndCallQualifier = c_uint8# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 218

QualifierOfInterrogation = c_uint8# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 233

QualifierOfCIC = c_uint8# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 272

QualifierOfRPC = c_uint8# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 288

QualifierOfParameterActivation = c_uint8# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 298

SetpointCommandQualifier = c_uint8# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 306

enum_anon_27 = c_int# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 313

IEC60870_DOUBLE_POINT_INTERMEDIATE = 0# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 313

IEC60870_DOUBLE_POINT_OFF = 1# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 313

IEC60870_DOUBLE_POINT_ON = 2# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 313

IEC60870_DOUBLE_POINT_INDETERMINATE = 3# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 313

DoublePointValue = enum_anon_27# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 313

enum_anon_28 = c_int# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 320

IEC60870_EVENTSTATE_INDETERMINATE_0 = 0# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 320

IEC60870_EVENTSTATE_OFF = 1# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 320

IEC60870_EVENTSTATE_ON = 2# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 320

IEC60870_EVENTSTATE_INDETERMINATE_3 = 3# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 320

EventState = enum_anon_28# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 320

enum_anon_29 = c_int# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 330

IEC60870_STEP_INVALID_0 = 0# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 330

IEC60870_STEP_LOWER = 1# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 330

IEC60870_STEP_HIGHER = 2# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 330

IEC60870_STEP_INVALID_3 = 3# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 330

StepCommandValue = enum_anon_29# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 330

tSingleEvent = c_uint8# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 332

SingleEvent = POINTER(tSingleEvent)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 334

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 337
if _libs["/usr/local/lib/lib60870.so"].has("SingleEvent_setEventState", "cdecl"):
    SingleEvent_setEventState = _libs["/usr/local/lib/lib60870.so"].get("SingleEvent_setEventState", "cdecl")
    SingleEvent_setEventState.argtypes = [SingleEvent, EventState]
    SingleEvent_setEventState.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 340
if _libs["/usr/local/lib/lib60870.so"].has("SingleEvent_getEventState", "cdecl"):
    SingleEvent_getEventState = _libs["/usr/local/lib/lib60870.so"].get("SingleEvent_getEventState", "cdecl")
    SingleEvent_getEventState.argtypes = [SingleEvent]
    SingleEvent_getEventState.restype = EventState

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 343
if _libs["/usr/local/lib/lib60870.so"].has("SingleEvent_setQDP", "cdecl"):
    SingleEvent_setQDP = _libs["/usr/local/lib/lib60870.so"].get("SingleEvent_setQDP", "cdecl")
    SingleEvent_setQDP.argtypes = [SingleEvent, QualityDescriptorP]
    SingleEvent_setQDP.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 346
if _libs["/usr/local/lib/lib60870.so"].has("SingleEvent_getQDP", "cdecl"):
    SingleEvent_getQDP = _libs["/usr/local/lib/lib60870.so"].get("SingleEvent_getQDP", "cdecl")
    SingleEvent_getQDP.argtypes = [SingleEvent]
    SingleEvent_getQDP.restype = QualityDescriptorP

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 353
class struct_sStatusAndStatusChangeDetection(Structure):
    pass

tStatusAndStatusChangeDetection = struct_sStatusAndStatusChangeDetection# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 349

StatusAndStatusChangeDetection = POINTER(tStatusAndStatusChangeDetection)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 351

struct_sStatusAndStatusChangeDetection.__slots__ = [
    'encodedValue',
]
struct_sStatusAndStatusChangeDetection._fields_ = [
    ('encodedValue', c_uint8 * int(4)),
]

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 358
if _libs["/usr/local/lib/lib60870.so"].has("StatusAndStatusChangeDetection_getSTn", "cdecl"):
    StatusAndStatusChangeDetection_getSTn = _libs["/usr/local/lib/lib60870.so"].get("StatusAndStatusChangeDetection_getSTn", "cdecl")
    StatusAndStatusChangeDetection_getSTn.argtypes = [StatusAndStatusChangeDetection]
    StatusAndStatusChangeDetection_getSTn.restype = c_uint16

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 361
if _libs["/usr/local/lib/lib60870.so"].has("StatusAndStatusChangeDetection_getCDn", "cdecl"):
    StatusAndStatusChangeDetection_getCDn = _libs["/usr/local/lib/lib60870.so"].get("StatusAndStatusChangeDetection_getCDn", "cdecl")
    StatusAndStatusChangeDetection_getCDn.argtypes = [StatusAndStatusChangeDetection]
    StatusAndStatusChangeDetection_getCDn.restype = c_uint16

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 364
if _libs["/usr/local/lib/lib60870.so"].has("StatusAndStatusChangeDetection_setSTn", "cdecl"):
    StatusAndStatusChangeDetection_setSTn = _libs["/usr/local/lib/lib60870.so"].get("StatusAndStatusChangeDetection_setSTn", "cdecl")
    StatusAndStatusChangeDetection_setSTn.argtypes = [StatusAndStatusChangeDetection, c_uint16]
    StatusAndStatusChangeDetection_setSTn.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 367
if _libs["/usr/local/lib/lib60870.so"].has("StatusAndStatusChangeDetection_getST", "cdecl"):
    StatusAndStatusChangeDetection_getST = _libs["/usr/local/lib/lib60870.so"].get("StatusAndStatusChangeDetection_getST", "cdecl")
    StatusAndStatusChangeDetection_getST.argtypes = [StatusAndStatusChangeDetection, c_int]
    StatusAndStatusChangeDetection_getST.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 370
if _libs["/usr/local/lib/lib60870.so"].has("StatusAndStatusChangeDetection_getCD", "cdecl"):
    StatusAndStatusChangeDetection_getCD = _libs["/usr/local/lib/lib60870.so"].get("StatusAndStatusChangeDetection_getCD", "cdecl")
    StatusAndStatusChangeDetection_getCD.argtypes = [StatusAndStatusChangeDetection, c_int]
    StatusAndStatusChangeDetection_getCD.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 377
class struct_sInformationObject(Structure):
    pass

InformationObject = POINTER(struct_sInformationObject)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 377

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 385
if _libs["/usr/local/lib/lib60870.so"].has("InformationObject_getMaxSizeInMemory", "cdecl"):
    InformationObject_getMaxSizeInMemory = _libs["/usr/local/lib/lib60870.so"].get("InformationObject_getMaxSizeInMemory", "cdecl")
    InformationObject_getMaxSizeInMemory.argtypes = []
    InformationObject_getMaxSizeInMemory.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 388
if _libs["/usr/local/lib/lib60870.so"].has("InformationObject_getObjectAddress", "cdecl"):
    InformationObject_getObjectAddress = _libs["/usr/local/lib/lib60870.so"].get("InformationObject_getObjectAddress", "cdecl")
    InformationObject_getObjectAddress.argtypes = [InformationObject]
    InformationObject_getObjectAddress.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 391
if _libs["/usr/local/lib/lib60870.so"].has("InformationObject_getType", "cdecl"):
    InformationObject_getType = _libs["/usr/local/lib/lib60870.so"].get("InformationObject_getType", "cdecl")
    InformationObject_getType.argtypes = [InformationObject]
    InformationObject_getType.restype = TypeID

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 401
if _libs["/usr/local/lib/lib60870.so"].has("InformationObject_destroy", "cdecl"):
    InformationObject_destroy = _libs["/usr/local/lib/lib60870.so"].get("InformationObject_destroy", "cdecl")
    InformationObject_destroy.argtypes = [InformationObject]
    InformationObject_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 407
class struct_sSinglePointInformation(Structure):
    pass

SinglePointInformation = POINTER(struct_sSinglePointInformation)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 407

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 410
if _libs["/usr/local/lib/lib60870.so"].has("SinglePointInformation_create", "cdecl"):
    SinglePointInformation_create = _libs["/usr/local/lib/lib60870.so"].get("SinglePointInformation_create", "cdecl")
    SinglePointInformation_create.argtypes = [SinglePointInformation, c_int, c_bool, QualityDescriptor]
    SinglePointInformation_create.restype = SinglePointInformation

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 414
if _libs["/usr/local/lib/lib60870.so"].has("SinglePointInformation_getValue", "cdecl"):
    SinglePointInformation_getValue = _libs["/usr/local/lib/lib60870.so"].get("SinglePointInformation_getValue", "cdecl")
    SinglePointInformation_getValue.argtypes = [SinglePointInformation]
    SinglePointInformation_getValue.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 417
if _libs["/usr/local/lib/lib60870.so"].has("SinglePointInformation_getQuality", "cdecl"):
    SinglePointInformation_getQuality = _libs["/usr/local/lib/lib60870.so"].get("SinglePointInformation_getQuality", "cdecl")
    SinglePointInformation_getQuality.argtypes = [SinglePointInformation]
    SinglePointInformation_getQuality.restype = QualityDescriptor

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 420
if _libs["/usr/local/lib/lib60870.so"].has("SinglePointInformation_destroy", "cdecl"):
    SinglePointInformation_destroy = _libs["/usr/local/lib/lib60870.so"].get("SinglePointInformation_destroy", "cdecl")
    SinglePointInformation_destroy.argtypes = [SinglePointInformation]
    SinglePointInformation_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 426
class struct_sSinglePointWithCP24Time2a(Structure):
    pass

SinglePointWithCP24Time2a = POINTER(struct_sSinglePointWithCP24Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 426

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 429
if _libs["/usr/local/lib/lib60870.so"].has("SinglePointWithCP24Time2a_create", "cdecl"):
    SinglePointWithCP24Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("SinglePointWithCP24Time2a_create", "cdecl")
    SinglePointWithCP24Time2a_create.argtypes = [SinglePointWithCP24Time2a, c_int, c_bool, QualityDescriptor, CP24Time2a]
    SinglePointWithCP24Time2a_create.restype = SinglePointWithCP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 433
if _libs["/usr/local/lib/lib60870.so"].has("SinglePointWithCP24Time2a_destroy", "cdecl"):
    SinglePointWithCP24Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("SinglePointWithCP24Time2a_destroy", "cdecl")
    SinglePointWithCP24Time2a_destroy.argtypes = [SinglePointWithCP24Time2a]
    SinglePointWithCP24Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 436
if _libs["/usr/local/lib/lib60870.so"].has("SinglePointWithCP24Time2a_getTimestamp", "cdecl"):
    SinglePointWithCP24Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("SinglePointWithCP24Time2a_getTimestamp", "cdecl")
    SinglePointWithCP24Time2a_getTimestamp.argtypes = [SinglePointWithCP24Time2a]
    SinglePointWithCP24Time2a_getTimestamp.restype = CP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 442
class struct_sSinglePointWithCP56Time2a(Structure):
    pass

SinglePointWithCP56Time2a = POINTER(struct_sSinglePointWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 442

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 445
if _libs["/usr/local/lib/lib60870.so"].has("SinglePointWithCP56Time2a_create", "cdecl"):
    SinglePointWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("SinglePointWithCP56Time2a_create", "cdecl")
    SinglePointWithCP56Time2a_create.argtypes = [SinglePointWithCP56Time2a, c_int, c_bool, QualityDescriptor, CP56Time2a]
    SinglePointWithCP56Time2a_create.restype = SinglePointWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 449
if _libs["/usr/local/lib/lib60870.so"].has("SinglePointWithCP56Time2a_destroy", "cdecl"):
    SinglePointWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("SinglePointWithCP56Time2a_destroy", "cdecl")
    SinglePointWithCP56Time2a_destroy.argtypes = [SinglePointWithCP56Time2a]
    SinglePointWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 452
if _libs["/usr/local/lib/lib60870.so"].has("SinglePointWithCP56Time2a_getTimestamp", "cdecl"):
    SinglePointWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("SinglePointWithCP56Time2a_getTimestamp", "cdecl")
    SinglePointWithCP56Time2a_getTimestamp.argtypes = [SinglePointWithCP56Time2a]
    SinglePointWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 459
class struct_sDoublePointInformation(Structure):
    pass

DoublePointInformation = POINTER(struct_sDoublePointInformation)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 459

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 462
if _libs["/usr/local/lib/lib60870.so"].has("DoublePointInformation_destroy", "cdecl"):
    DoublePointInformation_destroy = _libs["/usr/local/lib/lib60870.so"].get("DoublePointInformation_destroy", "cdecl")
    DoublePointInformation_destroy.argtypes = [DoublePointInformation]
    DoublePointInformation_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 465
if _libs["/usr/local/lib/lib60870.so"].has("DoublePointInformation_create", "cdecl"):
    DoublePointInformation_create = _libs["/usr/local/lib/lib60870.so"].get("DoublePointInformation_create", "cdecl")
    DoublePointInformation_create.argtypes = [DoublePointInformation, c_int, DoublePointValue, QualityDescriptor]
    DoublePointInformation_create.restype = DoublePointInformation

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 469
if _libs["/usr/local/lib/lib60870.so"].has("DoublePointInformation_getValue", "cdecl"):
    DoublePointInformation_getValue = _libs["/usr/local/lib/lib60870.so"].get("DoublePointInformation_getValue", "cdecl")
    DoublePointInformation_getValue.argtypes = [DoublePointInformation]
    DoublePointInformation_getValue.restype = DoublePointValue

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 472
if _libs["/usr/local/lib/lib60870.so"].has("DoublePointInformation_getQuality", "cdecl"):
    DoublePointInformation_getQuality = _libs["/usr/local/lib/lib60870.so"].get("DoublePointInformation_getQuality", "cdecl")
    DoublePointInformation_getQuality.argtypes = [DoublePointInformation]
    DoublePointInformation_getQuality.restype = QualityDescriptor

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 478
class struct_sDoublePointWithCP24Time2a(Structure):
    pass

DoublePointWithCP24Time2a = POINTER(struct_sDoublePointWithCP24Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 478

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 481
if _libs["/usr/local/lib/lib60870.so"].has("DoublePointWithCP24Time2a_destroy", "cdecl"):
    DoublePointWithCP24Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("DoublePointWithCP24Time2a_destroy", "cdecl")
    DoublePointWithCP24Time2a_destroy.argtypes = [DoublePointWithCP24Time2a]
    DoublePointWithCP24Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 484
if _libs["/usr/local/lib/lib60870.so"].has("DoublePointWithCP24Time2a_create", "cdecl"):
    DoublePointWithCP24Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("DoublePointWithCP24Time2a_create", "cdecl")
    DoublePointWithCP24Time2a_create.argtypes = [DoublePointWithCP24Time2a, c_int, DoublePointValue, QualityDescriptor, CP24Time2a]
    DoublePointWithCP24Time2a_create.restype = DoublePointWithCP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 488
if _libs["/usr/local/lib/lib60870.so"].has("DoublePointWithCP24Time2a_getTimestamp", "cdecl"):
    DoublePointWithCP24Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("DoublePointWithCP24Time2a_getTimestamp", "cdecl")
    DoublePointWithCP24Time2a_getTimestamp.argtypes = [DoublePointWithCP24Time2a]
    DoublePointWithCP24Time2a_getTimestamp.restype = CP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 494
class struct_sDoublePointWithCP56Time2a(Structure):
    pass

DoublePointWithCP56Time2a = POINTER(struct_sDoublePointWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 494

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 497
if _libs["/usr/local/lib/lib60870.so"].has("DoublePointWithCP56Time2a_create", "cdecl"):
    DoublePointWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("DoublePointWithCP56Time2a_create", "cdecl")
    DoublePointWithCP56Time2a_create.argtypes = [DoublePointWithCP56Time2a, c_int, DoublePointValue, QualityDescriptor, CP56Time2a]
    DoublePointWithCP56Time2a_create.restype = DoublePointWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 501
if _libs["/usr/local/lib/lib60870.so"].has("DoublePointWithCP56Time2a_destroy", "cdecl"):
    DoublePointWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("DoublePointWithCP56Time2a_destroy", "cdecl")
    DoublePointWithCP56Time2a_destroy.argtypes = [DoublePointWithCP56Time2a]
    DoublePointWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 504
if _libs["/usr/local/lib/lib60870.so"].has("DoublePointWithCP56Time2a_getTimestamp", "cdecl"):
    DoublePointWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("DoublePointWithCP56Time2a_getTimestamp", "cdecl")
    DoublePointWithCP56Time2a_getTimestamp.argtypes = [DoublePointWithCP56Time2a]
    DoublePointWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 510
class struct_sStepPositionInformation(Structure):
    pass

StepPositionInformation = POINTER(struct_sStepPositionInformation)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 510

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 524
if _libs["/usr/local/lib/lib60870.so"].has("StepPositionInformation_create", "cdecl"):
    StepPositionInformation_create = _libs["/usr/local/lib/lib60870.so"].get("StepPositionInformation_create", "cdecl")
    StepPositionInformation_create.argtypes = [StepPositionInformation, c_int, c_int, c_bool, QualityDescriptor]
    StepPositionInformation_create.restype = StepPositionInformation

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 528
if _libs["/usr/local/lib/lib60870.so"].has("StepPositionInformation_destroy", "cdecl"):
    StepPositionInformation_destroy = _libs["/usr/local/lib/lib60870.so"].get("StepPositionInformation_destroy", "cdecl")
    StepPositionInformation_destroy.argtypes = [StepPositionInformation]
    StepPositionInformation_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 531
if _libs["/usr/local/lib/lib60870.so"].has("StepPositionInformation_getObjectAddress", "cdecl"):
    StepPositionInformation_getObjectAddress = _libs["/usr/local/lib/lib60870.so"].get("StepPositionInformation_getObjectAddress", "cdecl")
    StepPositionInformation_getObjectAddress.argtypes = [StepPositionInformation]
    StepPositionInformation_getObjectAddress.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 537
if _libs["/usr/local/lib/lib60870.so"].has("StepPositionInformation_getValue", "cdecl"):
    StepPositionInformation_getValue = _libs["/usr/local/lib/lib60870.so"].get("StepPositionInformation_getValue", "cdecl")
    StepPositionInformation_getValue.argtypes = [StepPositionInformation]
    StepPositionInformation_getValue.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 540
if _libs["/usr/local/lib/lib60870.so"].has("StepPositionInformation_isTransient", "cdecl"):
    StepPositionInformation_isTransient = _libs["/usr/local/lib/lib60870.so"].get("StepPositionInformation_isTransient", "cdecl")
    StepPositionInformation_isTransient.argtypes = [StepPositionInformation]
    StepPositionInformation_isTransient.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 543
if _libs["/usr/local/lib/lib60870.so"].has("StepPositionInformation_getQuality", "cdecl"):
    StepPositionInformation_getQuality = _libs["/usr/local/lib/lib60870.so"].get("StepPositionInformation_getQuality", "cdecl")
    StepPositionInformation_getQuality.argtypes = [StepPositionInformation]
    StepPositionInformation_getQuality.restype = QualityDescriptor

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 549
class struct_sStepPositionWithCP24Time2a(Structure):
    pass

StepPositionWithCP24Time2a = POINTER(struct_sStepPositionWithCP24Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 549

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 552
if _libs["/usr/local/lib/lib60870.so"].has("StepPositionWithCP24Time2a_destroy", "cdecl"):
    StepPositionWithCP24Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("StepPositionWithCP24Time2a_destroy", "cdecl")
    StepPositionWithCP24Time2a_destroy.argtypes = [StepPositionWithCP24Time2a]
    StepPositionWithCP24Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 555
if _libs["/usr/local/lib/lib60870.so"].has("StepPositionWithCP24Time2a_create", "cdecl"):
    StepPositionWithCP24Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("StepPositionWithCP24Time2a_create", "cdecl")
    StepPositionWithCP24Time2a_create.argtypes = [StepPositionWithCP24Time2a, c_int, c_int, c_bool, QualityDescriptor, CP24Time2a]
    StepPositionWithCP24Time2a_create.restype = StepPositionWithCP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 559
if _libs["/usr/local/lib/lib60870.so"].has("StepPositionWithCP24Time2a_getTimestamp", "cdecl"):
    StepPositionWithCP24Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("StepPositionWithCP24Time2a_getTimestamp", "cdecl")
    StepPositionWithCP24Time2a_getTimestamp.argtypes = [StepPositionWithCP24Time2a]
    StepPositionWithCP24Time2a_getTimestamp.restype = CP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 566
class struct_sStepPositionWithCP56Time2a(Structure):
    pass

StepPositionWithCP56Time2a = POINTER(struct_sStepPositionWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 566

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 569
if _libs["/usr/local/lib/lib60870.so"].has("StepPositionWithCP56Time2a_destroy", "cdecl"):
    StepPositionWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("StepPositionWithCP56Time2a_destroy", "cdecl")
    StepPositionWithCP56Time2a_destroy.argtypes = [StepPositionWithCP56Time2a]
    StepPositionWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 572
if _libs["/usr/local/lib/lib60870.so"].has("StepPositionWithCP56Time2a_create", "cdecl"):
    StepPositionWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("StepPositionWithCP56Time2a_create", "cdecl")
    StepPositionWithCP56Time2a_create.argtypes = [StepPositionWithCP56Time2a, c_int, c_int, c_bool, QualityDescriptor, CP56Time2a]
    StepPositionWithCP56Time2a_create.restype = StepPositionWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 576
if _libs["/usr/local/lib/lib60870.so"].has("StepPositionWithCP56Time2a_getTimestamp", "cdecl"):
    StepPositionWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("StepPositionWithCP56Time2a_getTimestamp", "cdecl")
    StepPositionWithCP56Time2a_getTimestamp.argtypes = [StepPositionWithCP56Time2a]
    StepPositionWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 582
class struct_sBitString32(Structure):
    pass

BitString32 = POINTER(struct_sBitString32)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 582

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 585
if _libs["/usr/local/lib/lib60870.so"].has("BitString32_destroy", "cdecl"):
    BitString32_destroy = _libs["/usr/local/lib/lib60870.so"].get("BitString32_destroy", "cdecl")
    BitString32_destroy.argtypes = [BitString32]
    BitString32_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 588
if _libs["/usr/local/lib/lib60870.so"].has("BitString32_create", "cdecl"):
    BitString32_create = _libs["/usr/local/lib/lib60870.so"].get("BitString32_create", "cdecl")
    BitString32_create.argtypes = [BitString32, c_int, c_uint32]
    BitString32_create.restype = BitString32

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 591
if _libs["/usr/local/lib/lib60870.so"].has("BitString32_createEx", "cdecl"):
    BitString32_createEx = _libs["/usr/local/lib/lib60870.so"].get("BitString32_createEx", "cdecl")
    BitString32_createEx.argtypes = [BitString32, c_int, c_uint32, QualityDescriptor]
    BitString32_createEx.restype = BitString32

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 594
if _libs["/usr/local/lib/lib60870.so"].has("BitString32_getValue", "cdecl"):
    BitString32_getValue = _libs["/usr/local/lib/lib60870.so"].get("BitString32_getValue", "cdecl")
    BitString32_getValue.argtypes = [BitString32]
    BitString32_getValue.restype = c_uint32

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 597
if _libs["/usr/local/lib/lib60870.so"].has("BitString32_getQuality", "cdecl"):
    BitString32_getQuality = _libs["/usr/local/lib/lib60870.so"].get("BitString32_getQuality", "cdecl")
    BitString32_getQuality.argtypes = [BitString32]
    BitString32_getQuality.restype = QualityDescriptor

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 603
class struct_sBitstring32WithCP24Time2a(Structure):
    pass

Bitstring32WithCP24Time2a = POINTER(struct_sBitstring32WithCP24Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 603

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 606
if _libs["/usr/local/lib/lib60870.so"].has("Bitstring32WithCP24Time2a_destroy", "cdecl"):
    Bitstring32WithCP24Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("Bitstring32WithCP24Time2a_destroy", "cdecl")
    Bitstring32WithCP24Time2a_destroy.argtypes = [Bitstring32WithCP24Time2a]
    Bitstring32WithCP24Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 609
if _libs["/usr/local/lib/lib60870.so"].has("Bitstring32WithCP24Time2a_create", "cdecl"):
    Bitstring32WithCP24Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("Bitstring32WithCP24Time2a_create", "cdecl")
    Bitstring32WithCP24Time2a_create.argtypes = [Bitstring32WithCP24Time2a, c_int, c_uint32, CP24Time2a]
    Bitstring32WithCP24Time2a_create.restype = Bitstring32WithCP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 612
if _libs["/usr/local/lib/lib60870.so"].has("Bitstring32WithCP24Time2a_createEx", "cdecl"):
    Bitstring32WithCP24Time2a_createEx = _libs["/usr/local/lib/lib60870.so"].get("Bitstring32WithCP24Time2a_createEx", "cdecl")
    Bitstring32WithCP24Time2a_createEx.argtypes = [Bitstring32WithCP24Time2a, c_int, c_uint32, QualityDescriptor, CP24Time2a]
    Bitstring32WithCP24Time2a_createEx.restype = Bitstring32WithCP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 615
if _libs["/usr/local/lib/lib60870.so"].has("Bitstring32WithCP24Time2a_getTimestamp", "cdecl"):
    Bitstring32WithCP24Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("Bitstring32WithCP24Time2a_getTimestamp", "cdecl")
    Bitstring32WithCP24Time2a_getTimestamp.argtypes = [Bitstring32WithCP24Time2a]
    Bitstring32WithCP24Time2a_getTimestamp.restype = CP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 621
class struct_sBitstring32WithCP56Time2a(Structure):
    pass

Bitstring32WithCP56Time2a = POINTER(struct_sBitstring32WithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 621

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 624
if _libs["/usr/local/lib/lib60870.so"].has("Bitstring32WithCP56Time2a_destroy", "cdecl"):
    Bitstring32WithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("Bitstring32WithCP56Time2a_destroy", "cdecl")
    Bitstring32WithCP56Time2a_destroy.argtypes = [Bitstring32WithCP56Time2a]
    Bitstring32WithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 627
if _libs["/usr/local/lib/lib60870.so"].has("Bitstring32WithCP56Time2a_create", "cdecl"):
    Bitstring32WithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("Bitstring32WithCP56Time2a_create", "cdecl")
    Bitstring32WithCP56Time2a_create.argtypes = [Bitstring32WithCP56Time2a, c_int, c_uint32, CP56Time2a]
    Bitstring32WithCP56Time2a_create.restype = Bitstring32WithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 630
if _libs["/usr/local/lib/lib60870.so"].has("Bitstring32WithCP56Time2a_createEx", "cdecl"):
    Bitstring32WithCP56Time2a_createEx = _libs["/usr/local/lib/lib60870.so"].get("Bitstring32WithCP56Time2a_createEx", "cdecl")
    Bitstring32WithCP56Time2a_createEx.argtypes = [Bitstring32WithCP56Time2a, c_int, c_uint32, QualityDescriptor, CP56Time2a]
    Bitstring32WithCP56Time2a_createEx.restype = Bitstring32WithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 633
if _libs["/usr/local/lib/lib60870.so"].has("Bitstring32WithCP56Time2a_getTimestamp", "cdecl"):
    Bitstring32WithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("Bitstring32WithCP56Time2a_getTimestamp", "cdecl")
    Bitstring32WithCP56Time2a_getTimestamp.argtypes = [Bitstring32WithCP56Time2a]
    Bitstring32WithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 639
class struct_sMeasuredValueNormalizedWithoutQuality(Structure):
    pass

MeasuredValueNormalizedWithoutQuality = POINTER(struct_sMeasuredValueNormalizedWithoutQuality)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 639

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 642
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueNormalizedWithoutQuality_destroy", "cdecl"):
    MeasuredValueNormalizedWithoutQuality_destroy = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueNormalizedWithoutQuality_destroy", "cdecl")
    MeasuredValueNormalizedWithoutQuality_destroy.argtypes = [MeasuredValueNormalizedWithoutQuality]
    MeasuredValueNormalizedWithoutQuality_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 645
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueNormalizedWithoutQuality_create", "cdecl"):
    MeasuredValueNormalizedWithoutQuality_create = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueNormalizedWithoutQuality_create", "cdecl")
    MeasuredValueNormalizedWithoutQuality_create.argtypes = [MeasuredValueNormalizedWithoutQuality, c_int, c_float]
    MeasuredValueNormalizedWithoutQuality_create.restype = MeasuredValueNormalizedWithoutQuality

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 648
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueNormalizedWithoutQuality_getValue", "cdecl"):
    MeasuredValueNormalizedWithoutQuality_getValue = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueNormalizedWithoutQuality_getValue", "cdecl")
    MeasuredValueNormalizedWithoutQuality_getValue.argtypes = [MeasuredValueNormalizedWithoutQuality]
    MeasuredValueNormalizedWithoutQuality_getValue.restype = c_float

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 651
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueNormalizedWithoutQuality_setValue", "cdecl"):
    MeasuredValueNormalizedWithoutQuality_setValue = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueNormalizedWithoutQuality_setValue", "cdecl")
    MeasuredValueNormalizedWithoutQuality_setValue.argtypes = [MeasuredValueNormalizedWithoutQuality, c_float]
    MeasuredValueNormalizedWithoutQuality_setValue.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 657
class struct_sMeasuredValueNormalized(Structure):
    pass

MeasuredValueNormalized = POINTER(struct_sMeasuredValueNormalized)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 657

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 660
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueNormalized_destroy", "cdecl"):
    MeasuredValueNormalized_destroy = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueNormalized_destroy", "cdecl")
    MeasuredValueNormalized_destroy.argtypes = [MeasuredValueNormalized]
    MeasuredValueNormalized_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 663
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueNormalized_create", "cdecl"):
    MeasuredValueNormalized_create = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueNormalized_create", "cdecl")
    MeasuredValueNormalized_create.argtypes = [MeasuredValueNormalized, c_int, c_float, QualityDescriptor]
    MeasuredValueNormalized_create.restype = MeasuredValueNormalized

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 666
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueNormalized_getValue", "cdecl"):
    MeasuredValueNormalized_getValue = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueNormalized_getValue", "cdecl")
    MeasuredValueNormalized_getValue.argtypes = [MeasuredValueNormalized]
    MeasuredValueNormalized_getValue.restype = c_float

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 669
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueNormalized_setValue", "cdecl"):
    MeasuredValueNormalized_setValue = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueNormalized_setValue", "cdecl")
    MeasuredValueNormalized_setValue.argtypes = [MeasuredValueNormalized, c_float]
    MeasuredValueNormalized_setValue.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 672
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueNormalized_getQuality", "cdecl"):
    MeasuredValueNormalized_getQuality = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueNormalized_getQuality", "cdecl")
    MeasuredValueNormalized_getQuality.argtypes = [MeasuredValueNormalized]
    MeasuredValueNormalized_getQuality.restype = QualityDescriptor

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 678
class struct_sMeasuredValueNormalizedWithCP24Time2a(Structure):
    pass

MeasuredValueNormalizedWithCP24Time2a = POINTER(struct_sMeasuredValueNormalizedWithCP24Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 678

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 681
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueNormalizedWithCP24Time2a_destroy", "cdecl"):
    MeasuredValueNormalizedWithCP24Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueNormalizedWithCP24Time2a_destroy", "cdecl")
    MeasuredValueNormalizedWithCP24Time2a_destroy.argtypes = [MeasuredValueNormalizedWithCP24Time2a]
    MeasuredValueNormalizedWithCP24Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 684
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueNormalizedWithCP24Time2a_create", "cdecl"):
    MeasuredValueNormalizedWithCP24Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueNormalizedWithCP24Time2a_create", "cdecl")
    MeasuredValueNormalizedWithCP24Time2a_create.argtypes = [MeasuredValueNormalizedWithCP24Time2a, c_int, c_float, QualityDescriptor, CP24Time2a]
    MeasuredValueNormalizedWithCP24Time2a_create.restype = MeasuredValueNormalizedWithCP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 688
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueNormalizedWithCP24Time2a_getTimestamp", "cdecl"):
    MeasuredValueNormalizedWithCP24Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueNormalizedWithCP24Time2a_getTimestamp", "cdecl")
    MeasuredValueNormalizedWithCP24Time2a_getTimestamp.argtypes = [MeasuredValueNormalizedWithCP24Time2a]
    MeasuredValueNormalizedWithCP24Time2a_getTimestamp.restype = CP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 691
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueNormalizedWithCP24Time2a_setTimestamp", "cdecl"):
    MeasuredValueNormalizedWithCP24Time2a_setTimestamp = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueNormalizedWithCP24Time2a_setTimestamp", "cdecl")
    MeasuredValueNormalizedWithCP24Time2a_setTimestamp.argtypes = [MeasuredValueNormalizedWithCP24Time2a, CP24Time2a]
    MeasuredValueNormalizedWithCP24Time2a_setTimestamp.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 697
class struct_sMeasuredValueNormalizedWithCP56Time2a(Structure):
    pass

MeasuredValueNormalizedWithCP56Time2a = POINTER(struct_sMeasuredValueNormalizedWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 697

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 700
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueNormalizedWithCP56Time2a_destroy", "cdecl"):
    MeasuredValueNormalizedWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueNormalizedWithCP56Time2a_destroy", "cdecl")
    MeasuredValueNormalizedWithCP56Time2a_destroy.argtypes = [MeasuredValueNormalizedWithCP56Time2a]
    MeasuredValueNormalizedWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 703
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueNormalizedWithCP56Time2a_create", "cdecl"):
    MeasuredValueNormalizedWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueNormalizedWithCP56Time2a_create", "cdecl")
    MeasuredValueNormalizedWithCP56Time2a_create.argtypes = [MeasuredValueNormalizedWithCP56Time2a, c_int, c_float, QualityDescriptor, CP56Time2a]
    MeasuredValueNormalizedWithCP56Time2a_create.restype = MeasuredValueNormalizedWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 707
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueNormalizedWithCP56Time2a_getTimestamp", "cdecl"):
    MeasuredValueNormalizedWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueNormalizedWithCP56Time2a_getTimestamp", "cdecl")
    MeasuredValueNormalizedWithCP56Time2a_getTimestamp.argtypes = [MeasuredValueNormalizedWithCP56Time2a]
    MeasuredValueNormalizedWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 710
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueNormalizedWithCP56Time2a_setTimestamp", "cdecl"):
    MeasuredValueNormalizedWithCP56Time2a_setTimestamp = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueNormalizedWithCP56Time2a_setTimestamp", "cdecl")
    MeasuredValueNormalizedWithCP56Time2a_setTimestamp.argtypes = [MeasuredValueNormalizedWithCP56Time2a, CP56Time2a]
    MeasuredValueNormalizedWithCP56Time2a_setTimestamp.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 717
class struct_sMeasuredValueScaled(Structure):
    pass

MeasuredValueScaled = POINTER(struct_sMeasuredValueScaled)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 717

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 730
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueScaled_create", "cdecl"):
    MeasuredValueScaled_create = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueScaled_create", "cdecl")
    MeasuredValueScaled_create.argtypes = [MeasuredValueScaled, c_int, c_int, QualityDescriptor]
    MeasuredValueScaled_create.restype = MeasuredValueScaled

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 733
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueScaled_destroy", "cdecl"):
    MeasuredValueScaled_destroy = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueScaled_destroy", "cdecl")
    MeasuredValueScaled_destroy.argtypes = [MeasuredValueScaled]
    MeasuredValueScaled_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 736
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueScaled_getValue", "cdecl"):
    MeasuredValueScaled_getValue = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueScaled_getValue", "cdecl")
    MeasuredValueScaled_getValue.argtypes = [MeasuredValueScaled]
    MeasuredValueScaled_getValue.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 739
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueScaled_setValue", "cdecl"):
    MeasuredValueScaled_setValue = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueScaled_setValue", "cdecl")
    MeasuredValueScaled_setValue.argtypes = [MeasuredValueScaled, c_int]
    MeasuredValueScaled_setValue.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 742
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueScaled_getQuality", "cdecl"):
    MeasuredValueScaled_getQuality = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueScaled_getQuality", "cdecl")
    MeasuredValueScaled_getQuality.argtypes = [MeasuredValueScaled]
    MeasuredValueScaled_getQuality.restype = QualityDescriptor

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 745
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueScaled_setQuality", "cdecl"):
    MeasuredValueScaled_setQuality = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueScaled_setQuality", "cdecl")
    MeasuredValueScaled_setQuality.argtypes = [MeasuredValueScaled, QualityDescriptor]
    MeasuredValueScaled_setQuality.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 751
class struct_sMeasuredValueScaledWithCP24Time2a(Structure):
    pass

MeasuredValueScaledWithCP24Time2a = POINTER(struct_sMeasuredValueScaledWithCP24Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 751

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 754
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueScaledWithCP24Time2a_destroy", "cdecl"):
    MeasuredValueScaledWithCP24Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueScaledWithCP24Time2a_destroy", "cdecl")
    MeasuredValueScaledWithCP24Time2a_destroy.argtypes = [MeasuredValueScaledWithCP24Time2a]
    MeasuredValueScaledWithCP24Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 757
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueScaledWithCP24Time2a_create", "cdecl"):
    MeasuredValueScaledWithCP24Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueScaledWithCP24Time2a_create", "cdecl")
    MeasuredValueScaledWithCP24Time2a_create.argtypes = [MeasuredValueScaledWithCP24Time2a, c_int, c_int, QualityDescriptor, CP24Time2a]
    MeasuredValueScaledWithCP24Time2a_create.restype = MeasuredValueScaledWithCP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 761
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueScaledWithCP24Time2a_getTimestamp", "cdecl"):
    MeasuredValueScaledWithCP24Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueScaledWithCP24Time2a_getTimestamp", "cdecl")
    MeasuredValueScaledWithCP24Time2a_getTimestamp.argtypes = [MeasuredValueScaledWithCP24Time2a]
    MeasuredValueScaledWithCP24Time2a_getTimestamp.restype = CP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 764
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueScaledWithCP24Time2a_setTimestamp", "cdecl"):
    MeasuredValueScaledWithCP24Time2a_setTimestamp = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueScaledWithCP24Time2a_setTimestamp", "cdecl")
    MeasuredValueScaledWithCP24Time2a_setTimestamp.argtypes = [MeasuredValueScaledWithCP24Time2a, CP24Time2a]
    MeasuredValueScaledWithCP24Time2a_setTimestamp.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 770
class struct_sMeasuredValueScaledWithCP56Time2a(Structure):
    pass

MeasuredValueScaledWithCP56Time2a = POINTER(struct_sMeasuredValueScaledWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 770

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 773
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueScaledWithCP56Time2a_destroy", "cdecl"):
    MeasuredValueScaledWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueScaledWithCP56Time2a_destroy", "cdecl")
    MeasuredValueScaledWithCP56Time2a_destroy.argtypes = [MeasuredValueScaledWithCP56Time2a]
    MeasuredValueScaledWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 776
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueScaledWithCP56Time2a_create", "cdecl"):
    MeasuredValueScaledWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueScaledWithCP56Time2a_create", "cdecl")
    MeasuredValueScaledWithCP56Time2a_create.argtypes = [MeasuredValueScaledWithCP56Time2a, c_int, c_int, QualityDescriptor, CP56Time2a]
    MeasuredValueScaledWithCP56Time2a_create.restype = MeasuredValueScaledWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 780
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueScaledWithCP56Time2a_getTimestamp", "cdecl"):
    MeasuredValueScaledWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueScaledWithCP56Time2a_getTimestamp", "cdecl")
    MeasuredValueScaledWithCP56Time2a_getTimestamp.argtypes = [MeasuredValueScaledWithCP56Time2a]
    MeasuredValueScaledWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 783
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueScaledWithCP56Time2a_setTimestamp", "cdecl"):
    MeasuredValueScaledWithCP56Time2a_setTimestamp = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueScaledWithCP56Time2a_setTimestamp", "cdecl")
    MeasuredValueScaledWithCP56Time2a_setTimestamp.argtypes = [MeasuredValueScaledWithCP56Time2a, CP56Time2a]
    MeasuredValueScaledWithCP56Time2a_setTimestamp.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 789
class struct_sMeasuredValueShort(Structure):
    pass

MeasuredValueShort = POINTER(struct_sMeasuredValueShort)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 789

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 792
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueShort_destroy", "cdecl"):
    MeasuredValueShort_destroy = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueShort_destroy", "cdecl")
    MeasuredValueShort_destroy.argtypes = [MeasuredValueShort]
    MeasuredValueShort_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 795
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueShort_create", "cdecl"):
    MeasuredValueShort_create = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueShort_create", "cdecl")
    MeasuredValueShort_create.argtypes = [MeasuredValueShort, c_int, c_float, QualityDescriptor]
    MeasuredValueShort_create.restype = MeasuredValueShort

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 798
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueShort_getValue", "cdecl"):
    MeasuredValueShort_getValue = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueShort_getValue", "cdecl")
    MeasuredValueShort_getValue.argtypes = [MeasuredValueShort]
    MeasuredValueShort_getValue.restype = c_float

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 801
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueShort_setValue", "cdecl"):
    MeasuredValueShort_setValue = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueShort_setValue", "cdecl")
    MeasuredValueShort_setValue.argtypes = [MeasuredValueShort, c_float]
    MeasuredValueShort_setValue.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 804
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueShort_getQuality", "cdecl"):
    MeasuredValueShort_getQuality = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueShort_getQuality", "cdecl")
    MeasuredValueShort_getQuality.argtypes = [MeasuredValueShort]
    MeasuredValueShort_getQuality.restype = QualityDescriptor

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 810
class struct_sMeasuredValueShortWithCP24Time2a(Structure):
    pass

MeasuredValueShortWithCP24Time2a = POINTER(struct_sMeasuredValueShortWithCP24Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 810

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 813
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueShortWithCP24Time2a_destroy", "cdecl"):
    MeasuredValueShortWithCP24Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueShortWithCP24Time2a_destroy", "cdecl")
    MeasuredValueShortWithCP24Time2a_destroy.argtypes = [MeasuredValueShortWithCP24Time2a]
    MeasuredValueShortWithCP24Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 816
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueShortWithCP24Time2a_create", "cdecl"):
    MeasuredValueShortWithCP24Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueShortWithCP24Time2a_create", "cdecl")
    MeasuredValueShortWithCP24Time2a_create.argtypes = [MeasuredValueShortWithCP24Time2a, c_int, c_float, QualityDescriptor, CP24Time2a]
    MeasuredValueShortWithCP24Time2a_create.restype = MeasuredValueShortWithCP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 820
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueShortWithCP24Time2a_getTimestamp", "cdecl"):
    MeasuredValueShortWithCP24Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueShortWithCP24Time2a_getTimestamp", "cdecl")
    MeasuredValueShortWithCP24Time2a_getTimestamp.argtypes = [MeasuredValueShortWithCP24Time2a]
    MeasuredValueShortWithCP24Time2a_getTimestamp.restype = CP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 823
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueShortWithCP24Time2a_setTimestamp", "cdecl"):
    MeasuredValueShortWithCP24Time2a_setTimestamp = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueShortWithCP24Time2a_setTimestamp", "cdecl")
    MeasuredValueShortWithCP24Time2a_setTimestamp.argtypes = [MeasuredValueShortWithCP24Time2a, CP24Time2a]
    MeasuredValueShortWithCP24Time2a_setTimestamp.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 830
class struct_sMeasuredValueShortWithCP56Time2a(Structure):
    pass

MeasuredValueShortWithCP56Time2a = POINTER(struct_sMeasuredValueShortWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 830

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 833
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueShortWithCP56Time2a_destroy", "cdecl"):
    MeasuredValueShortWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueShortWithCP56Time2a_destroy", "cdecl")
    MeasuredValueShortWithCP56Time2a_destroy.argtypes = [MeasuredValueShortWithCP56Time2a]
    MeasuredValueShortWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 836
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueShortWithCP56Time2a_create", "cdecl"):
    MeasuredValueShortWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueShortWithCP56Time2a_create", "cdecl")
    MeasuredValueShortWithCP56Time2a_create.argtypes = [MeasuredValueShortWithCP56Time2a, c_int, c_float, QualityDescriptor, CP56Time2a]
    MeasuredValueShortWithCP56Time2a_create.restype = MeasuredValueShortWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 840
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueShortWithCP56Time2a_getTimestamp", "cdecl"):
    MeasuredValueShortWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueShortWithCP56Time2a_getTimestamp", "cdecl")
    MeasuredValueShortWithCP56Time2a_getTimestamp.argtypes = [MeasuredValueShortWithCP56Time2a]
    MeasuredValueShortWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 843
if _libs["/usr/local/lib/lib60870.so"].has("MeasuredValueShortWithCP56Time2a_setTimestamp", "cdecl"):
    MeasuredValueShortWithCP56Time2a_setTimestamp = _libs["/usr/local/lib/lib60870.so"].get("MeasuredValueShortWithCP56Time2a_setTimestamp", "cdecl")
    MeasuredValueShortWithCP56Time2a_setTimestamp.argtypes = [MeasuredValueShortWithCP56Time2a, CP56Time2a]
    MeasuredValueShortWithCP56Time2a_setTimestamp.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 850
class struct_sIntegratedTotals(Structure):
    pass

IntegratedTotals = POINTER(struct_sIntegratedTotals)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 850

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 853
if _libs["/usr/local/lib/lib60870.so"].has("IntegratedTotals_destroy", "cdecl"):
    IntegratedTotals_destroy = _libs["/usr/local/lib/lib60870.so"].get("IntegratedTotals_destroy", "cdecl")
    IntegratedTotals_destroy.argtypes = [IntegratedTotals]
    IntegratedTotals_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 867
if _libs["/usr/local/lib/lib60870.so"].has("IntegratedTotals_create", "cdecl"):
    IntegratedTotals_create = _libs["/usr/local/lib/lib60870.so"].get("IntegratedTotals_create", "cdecl")
    IntegratedTotals_create.argtypes = [IntegratedTotals, c_int, BinaryCounterReading]
    IntegratedTotals_create.restype = IntegratedTotals

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 870
if _libs["/usr/local/lib/lib60870.so"].has("IntegratedTotals_getBCR", "cdecl"):
    IntegratedTotals_getBCR = _libs["/usr/local/lib/lib60870.so"].get("IntegratedTotals_getBCR", "cdecl")
    IntegratedTotals_getBCR.argtypes = [IntegratedTotals]
    IntegratedTotals_getBCR.restype = BinaryCounterReading

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 873
if _libs["/usr/local/lib/lib60870.so"].has("IntegratedTotals_setBCR", "cdecl"):
    IntegratedTotals_setBCR = _libs["/usr/local/lib/lib60870.so"].get("IntegratedTotals_setBCR", "cdecl")
    IntegratedTotals_setBCR.argtypes = [IntegratedTotals, BinaryCounterReading]
    IntegratedTotals_setBCR.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 879
class struct_sIntegratedTotalsWithCP24Time2a(Structure):
    pass

IntegratedTotalsWithCP24Time2a = POINTER(struct_sIntegratedTotalsWithCP24Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 879

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 894
if _libs["/usr/local/lib/lib60870.so"].has("IntegratedTotalsWithCP24Time2a_create", "cdecl"):
    IntegratedTotalsWithCP24Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("IntegratedTotalsWithCP24Time2a_create", "cdecl")
    IntegratedTotalsWithCP24Time2a_create.argtypes = [IntegratedTotalsWithCP24Time2a, c_int, BinaryCounterReading, CP24Time2a]
    IntegratedTotalsWithCP24Time2a_create.restype = IntegratedTotalsWithCP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 898
if _libs["/usr/local/lib/lib60870.so"].has("IntegratedTotalsWithCP24Time2a_destroy", "cdecl"):
    IntegratedTotalsWithCP24Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("IntegratedTotalsWithCP24Time2a_destroy", "cdecl")
    IntegratedTotalsWithCP24Time2a_destroy.argtypes = [IntegratedTotalsWithCP24Time2a]
    IntegratedTotalsWithCP24Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 901
if _libs["/usr/local/lib/lib60870.so"].has("IntegratedTotalsWithCP24Time2a_getTimestamp", "cdecl"):
    IntegratedTotalsWithCP24Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("IntegratedTotalsWithCP24Time2a_getTimestamp", "cdecl")
    IntegratedTotalsWithCP24Time2a_getTimestamp.argtypes = [IntegratedTotalsWithCP24Time2a]
    IntegratedTotalsWithCP24Time2a_getTimestamp.restype = CP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 904
if _libs["/usr/local/lib/lib60870.so"].has("IntegratedTotalsWithCP24Time2a_setTimestamp", "cdecl"):
    IntegratedTotalsWithCP24Time2a_setTimestamp = _libs["/usr/local/lib/lib60870.so"].get("IntegratedTotalsWithCP24Time2a_setTimestamp", "cdecl")
    IntegratedTotalsWithCP24Time2a_setTimestamp.argtypes = [IntegratedTotalsWithCP24Time2a, CP24Time2a]
    IntegratedTotalsWithCP24Time2a_setTimestamp.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 911
class struct_sIntegratedTotalsWithCP56Time2a(Structure):
    pass

IntegratedTotalsWithCP56Time2a = POINTER(struct_sIntegratedTotalsWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 911

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 926
if _libs["/usr/local/lib/lib60870.so"].has("IntegratedTotalsWithCP56Time2a_create", "cdecl"):
    IntegratedTotalsWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("IntegratedTotalsWithCP56Time2a_create", "cdecl")
    IntegratedTotalsWithCP56Time2a_create.argtypes = [IntegratedTotalsWithCP56Time2a, c_int, BinaryCounterReading, CP56Time2a]
    IntegratedTotalsWithCP56Time2a_create.restype = IntegratedTotalsWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 930
if _libs["/usr/local/lib/lib60870.so"].has("IntegratedTotalsWithCP56Time2a_destroy", "cdecl"):
    IntegratedTotalsWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("IntegratedTotalsWithCP56Time2a_destroy", "cdecl")
    IntegratedTotalsWithCP56Time2a_destroy.argtypes = [IntegratedTotalsWithCP56Time2a]
    IntegratedTotalsWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 933
if _libs["/usr/local/lib/lib60870.so"].has("IntegratedTotalsWithCP56Time2a_getTimestamp", "cdecl"):
    IntegratedTotalsWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("IntegratedTotalsWithCP56Time2a_getTimestamp", "cdecl")
    IntegratedTotalsWithCP56Time2a_getTimestamp.argtypes = [IntegratedTotalsWithCP56Time2a]
    IntegratedTotalsWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 936
if _libs["/usr/local/lib/lib60870.so"].has("IntegratedTotalsWithCP56Time2a_setTimestamp", "cdecl"):
    IntegratedTotalsWithCP56Time2a_setTimestamp = _libs["/usr/local/lib/lib60870.so"].get("IntegratedTotalsWithCP56Time2a_setTimestamp", "cdecl")
    IntegratedTotalsWithCP56Time2a_setTimestamp.argtypes = [IntegratedTotalsWithCP56Time2a, CP56Time2a]
    IntegratedTotalsWithCP56Time2a_setTimestamp.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 943
class struct_sEventOfProtectionEquipment(Structure):
    pass

EventOfProtectionEquipment = POINTER(struct_sEventOfProtectionEquipment)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 943

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 946
if _libs["/usr/local/lib/lib60870.so"].has("EventOfProtectionEquipment_destroy", "cdecl"):
    EventOfProtectionEquipment_destroy = _libs["/usr/local/lib/lib60870.so"].get("EventOfProtectionEquipment_destroy", "cdecl")
    EventOfProtectionEquipment_destroy.argtypes = [EventOfProtectionEquipment]
    EventOfProtectionEquipment_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 949
if _libs["/usr/local/lib/lib60870.so"].has("EventOfProtectionEquipment_create", "cdecl"):
    EventOfProtectionEquipment_create = _libs["/usr/local/lib/lib60870.so"].get("EventOfProtectionEquipment_create", "cdecl")
    EventOfProtectionEquipment_create.argtypes = [EventOfProtectionEquipment, c_int, SingleEvent, CP16Time2a, CP24Time2a]
    EventOfProtectionEquipment_create.restype = EventOfProtectionEquipment

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 953
if _libs["/usr/local/lib/lib60870.so"].has("EventOfProtectionEquipment_getEvent", "cdecl"):
    EventOfProtectionEquipment_getEvent = _libs["/usr/local/lib/lib60870.so"].get("EventOfProtectionEquipment_getEvent", "cdecl")
    EventOfProtectionEquipment_getEvent.argtypes = [EventOfProtectionEquipment]
    EventOfProtectionEquipment_getEvent.restype = SingleEvent

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 956
if _libs["/usr/local/lib/lib60870.so"].has("EventOfProtectionEquipment_getElapsedTime", "cdecl"):
    EventOfProtectionEquipment_getElapsedTime = _libs["/usr/local/lib/lib60870.so"].get("EventOfProtectionEquipment_getElapsedTime", "cdecl")
    EventOfProtectionEquipment_getElapsedTime.argtypes = [EventOfProtectionEquipment]
    EventOfProtectionEquipment_getElapsedTime.restype = CP16Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 959
if _libs["/usr/local/lib/lib60870.so"].has("EventOfProtectionEquipment_getTimestamp", "cdecl"):
    EventOfProtectionEquipment_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("EventOfProtectionEquipment_getTimestamp", "cdecl")
    EventOfProtectionEquipment_getTimestamp.argtypes = [EventOfProtectionEquipment]
    EventOfProtectionEquipment_getTimestamp.restype = CP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 965
class struct_sPackedStartEventsOfProtectionEquipment(Structure):
    pass

PackedStartEventsOfProtectionEquipment = POINTER(struct_sPackedStartEventsOfProtectionEquipment)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 965

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 968
if _libs["/usr/local/lib/lib60870.so"].has("PackedStartEventsOfProtectionEquipment_create", "cdecl"):
    PackedStartEventsOfProtectionEquipment_create = _libs["/usr/local/lib/lib60870.so"].get("PackedStartEventsOfProtectionEquipment_create", "cdecl")
    PackedStartEventsOfProtectionEquipment_create.argtypes = [PackedStartEventsOfProtectionEquipment, c_int, StartEvent, QualityDescriptorP, CP16Time2a, CP24Time2a]
    PackedStartEventsOfProtectionEquipment_create.restype = PackedStartEventsOfProtectionEquipment

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 972
if _libs["/usr/local/lib/lib60870.so"].has("PackedStartEventsOfProtectionEquipment_destroy", "cdecl"):
    PackedStartEventsOfProtectionEquipment_destroy = _libs["/usr/local/lib/lib60870.so"].get("PackedStartEventsOfProtectionEquipment_destroy", "cdecl")
    PackedStartEventsOfProtectionEquipment_destroy.argtypes = [PackedStartEventsOfProtectionEquipment]
    PackedStartEventsOfProtectionEquipment_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 975
if _libs["/usr/local/lib/lib60870.so"].has("PackedStartEventsOfProtectionEquipment_getEvent", "cdecl"):
    PackedStartEventsOfProtectionEquipment_getEvent = _libs["/usr/local/lib/lib60870.so"].get("PackedStartEventsOfProtectionEquipment_getEvent", "cdecl")
    PackedStartEventsOfProtectionEquipment_getEvent.argtypes = [PackedStartEventsOfProtectionEquipment]
    PackedStartEventsOfProtectionEquipment_getEvent.restype = StartEvent

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 978
if _libs["/usr/local/lib/lib60870.so"].has("PackedStartEventsOfProtectionEquipment_getQuality", "cdecl"):
    PackedStartEventsOfProtectionEquipment_getQuality = _libs["/usr/local/lib/lib60870.so"].get("PackedStartEventsOfProtectionEquipment_getQuality", "cdecl")
    PackedStartEventsOfProtectionEquipment_getQuality.argtypes = [PackedStartEventsOfProtectionEquipment]
    PackedStartEventsOfProtectionEquipment_getQuality.restype = QualityDescriptorP

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 981
if _libs["/usr/local/lib/lib60870.so"].has("PackedStartEventsOfProtectionEquipment_getElapsedTime", "cdecl"):
    PackedStartEventsOfProtectionEquipment_getElapsedTime = _libs["/usr/local/lib/lib60870.so"].get("PackedStartEventsOfProtectionEquipment_getElapsedTime", "cdecl")
    PackedStartEventsOfProtectionEquipment_getElapsedTime.argtypes = [PackedStartEventsOfProtectionEquipment]
    PackedStartEventsOfProtectionEquipment_getElapsedTime.restype = CP16Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 984
if _libs["/usr/local/lib/lib60870.so"].has("PackedStartEventsOfProtectionEquipment_getTimestamp", "cdecl"):
    PackedStartEventsOfProtectionEquipment_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("PackedStartEventsOfProtectionEquipment_getTimestamp", "cdecl")
    PackedStartEventsOfProtectionEquipment_getTimestamp.argtypes = [PackedStartEventsOfProtectionEquipment]
    PackedStartEventsOfProtectionEquipment_getTimestamp.restype = CP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 990
class struct_sPackedOutputCircuitInfo(Structure):
    pass

PackedOutputCircuitInfo = POINTER(struct_sPackedOutputCircuitInfo)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 990

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 993
if _libs["/usr/local/lib/lib60870.so"].has("PackedOutputCircuitInfo_destroy", "cdecl"):
    PackedOutputCircuitInfo_destroy = _libs["/usr/local/lib/lib60870.so"].get("PackedOutputCircuitInfo_destroy", "cdecl")
    PackedOutputCircuitInfo_destroy.argtypes = [PackedOutputCircuitInfo]
    PackedOutputCircuitInfo_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 996
if _libs["/usr/local/lib/lib60870.so"].has("PackedOutputCircuitInfo_create", "cdecl"):
    PackedOutputCircuitInfo_create = _libs["/usr/local/lib/lib60870.so"].get("PackedOutputCircuitInfo_create", "cdecl")
    PackedOutputCircuitInfo_create.argtypes = [PackedOutputCircuitInfo, c_int, OutputCircuitInfo, QualityDescriptorP, CP16Time2a, CP24Time2a]
    PackedOutputCircuitInfo_create.restype = PackedOutputCircuitInfo

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1000
if _libs["/usr/local/lib/lib60870.so"].has("PackedOutputCircuitInfo_getOCI", "cdecl"):
    PackedOutputCircuitInfo_getOCI = _libs["/usr/local/lib/lib60870.so"].get("PackedOutputCircuitInfo_getOCI", "cdecl")
    PackedOutputCircuitInfo_getOCI.argtypes = [PackedOutputCircuitInfo]
    PackedOutputCircuitInfo_getOCI.restype = OutputCircuitInfo

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1003
if _libs["/usr/local/lib/lib60870.so"].has("PackedOutputCircuitInfo_getQuality", "cdecl"):
    PackedOutputCircuitInfo_getQuality = _libs["/usr/local/lib/lib60870.so"].get("PackedOutputCircuitInfo_getQuality", "cdecl")
    PackedOutputCircuitInfo_getQuality.argtypes = [PackedOutputCircuitInfo]
    PackedOutputCircuitInfo_getQuality.restype = QualityDescriptorP

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1006
if _libs["/usr/local/lib/lib60870.so"].has("PackedOutputCircuitInfo_getOperatingTime", "cdecl"):
    PackedOutputCircuitInfo_getOperatingTime = _libs["/usr/local/lib/lib60870.so"].get("PackedOutputCircuitInfo_getOperatingTime", "cdecl")
    PackedOutputCircuitInfo_getOperatingTime.argtypes = [PackedOutputCircuitInfo]
    PackedOutputCircuitInfo_getOperatingTime.restype = CP16Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1009
if _libs["/usr/local/lib/lib60870.so"].has("PackedOutputCircuitInfo_getTimestamp", "cdecl"):
    PackedOutputCircuitInfo_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("PackedOutputCircuitInfo_getTimestamp", "cdecl")
    PackedOutputCircuitInfo_getTimestamp.argtypes = [PackedOutputCircuitInfo]
    PackedOutputCircuitInfo_getTimestamp.restype = CP24Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1015
class struct_sPackedSinglePointWithSCD(Structure):
    pass

PackedSinglePointWithSCD = POINTER(struct_sPackedSinglePointWithSCD)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1015

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1018
if _libs["/usr/local/lib/lib60870.so"].has("PackedSinglePointWithSCD_destroy", "cdecl"):
    PackedSinglePointWithSCD_destroy = _libs["/usr/local/lib/lib60870.so"].get("PackedSinglePointWithSCD_destroy", "cdecl")
    PackedSinglePointWithSCD_destroy.argtypes = [PackedSinglePointWithSCD]
    PackedSinglePointWithSCD_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1021
if _libs["/usr/local/lib/lib60870.so"].has("PackedSinglePointWithSCD_create", "cdecl"):
    PackedSinglePointWithSCD_create = _libs["/usr/local/lib/lib60870.so"].get("PackedSinglePointWithSCD_create", "cdecl")
    PackedSinglePointWithSCD_create.argtypes = [PackedSinglePointWithSCD, c_int, StatusAndStatusChangeDetection, QualityDescriptor]
    PackedSinglePointWithSCD_create.restype = PackedSinglePointWithSCD

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1025
if _libs["/usr/local/lib/lib60870.so"].has("PackedSinglePointWithSCD_getQuality", "cdecl"):
    PackedSinglePointWithSCD_getQuality = _libs["/usr/local/lib/lib60870.so"].get("PackedSinglePointWithSCD_getQuality", "cdecl")
    PackedSinglePointWithSCD_getQuality.argtypes = [PackedSinglePointWithSCD]
    PackedSinglePointWithSCD_getQuality.restype = QualityDescriptor

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1028
if _libs["/usr/local/lib/lib60870.so"].has("PackedSinglePointWithSCD_getSCD", "cdecl"):
    PackedSinglePointWithSCD_getSCD = _libs["/usr/local/lib/lib60870.so"].get("PackedSinglePointWithSCD_getSCD", "cdecl")
    PackedSinglePointWithSCD_getSCD.argtypes = [PackedSinglePointWithSCD]
    PackedSinglePointWithSCD_getSCD.restype = StatusAndStatusChangeDetection

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1035
class struct_sSingleCommand(Structure):
    pass

SingleCommand = POINTER(struct_sSingleCommand)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1035

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1049
if _libs["/usr/local/lib/lib60870.so"].has("SingleCommand_create", "cdecl"):
    SingleCommand_create = _libs["/usr/local/lib/lib60870.so"].get("SingleCommand_create", "cdecl")
    SingleCommand_create.argtypes = [SingleCommand, c_int, c_bool, c_bool, c_int]
    SingleCommand_create.restype = SingleCommand

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1052
if _libs["/usr/local/lib/lib60870.so"].has("SingleCommand_destroy", "cdecl"):
    SingleCommand_destroy = _libs["/usr/local/lib/lib60870.so"].get("SingleCommand_destroy", "cdecl")
    SingleCommand_destroy.argtypes = [SingleCommand]
    SingleCommand_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1060
if _libs["/usr/local/lib/lib60870.so"].has("SingleCommand_getQU", "cdecl"):
    SingleCommand_getQU = _libs["/usr/local/lib/lib60870.so"].get("SingleCommand_getQU", "cdecl")
    SingleCommand_getQU.argtypes = [SingleCommand]
    SingleCommand_getQU.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1066
if _libs["/usr/local/lib/lib60870.so"].has("SingleCommand_getState", "cdecl"):
    SingleCommand_getState = _libs["/usr/local/lib/lib60870.so"].get("SingleCommand_getState", "cdecl")
    SingleCommand_getState.argtypes = [SingleCommand]
    SingleCommand_getState.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1074
if _libs["/usr/local/lib/lib60870.so"].has("SingleCommand_isSelect", "cdecl"):
    SingleCommand_isSelect = _libs["/usr/local/lib/lib60870.so"].get("SingleCommand_isSelect", "cdecl")
    SingleCommand_isSelect.argtypes = [SingleCommand]
    SingleCommand_isSelect.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1080
class struct_sSingleCommandWithCP56Time2a(Structure):
    pass

SingleCommandWithCP56Time2a = POINTER(struct_sSingleCommandWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1080

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1083
if _libs["/usr/local/lib/lib60870.so"].has("SingleCommandWithCP56Time2a_destroy", "cdecl"):
    SingleCommandWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("SingleCommandWithCP56Time2a_destroy", "cdecl")
    SingleCommandWithCP56Time2a_destroy.argtypes = [SingleCommandWithCP56Time2a]
    SingleCommandWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1098
if _libs["/usr/local/lib/lib60870.so"].has("SingleCommandWithCP56Time2a_create", "cdecl"):
    SingleCommandWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("SingleCommandWithCP56Time2a_create", "cdecl")
    SingleCommandWithCP56Time2a_create.argtypes = [SingleCommandWithCP56Time2a, c_int, c_bool, c_bool, c_int, CP56Time2a]
    SingleCommandWithCP56Time2a_create.restype = SingleCommandWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1109
if _libs["/usr/local/lib/lib60870.so"].has("SingleCommandWithCP56Time2a_getTimestamp", "cdecl"):
    SingleCommandWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("SingleCommandWithCP56Time2a_getTimestamp", "cdecl")
    SingleCommandWithCP56Time2a_getTimestamp.argtypes = [SingleCommandWithCP56Time2a]
    SingleCommandWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1115
class struct_sDoubleCommand(Structure):
    pass

DoubleCommand = POINTER(struct_sDoubleCommand)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1115

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1118
if _libs["/usr/local/lib/lib60870.so"].has("DoubleCommand_destroy", "cdecl"):
    DoubleCommand_destroy = _libs["/usr/local/lib/lib60870.so"].get("DoubleCommand_destroy", "cdecl")
    DoubleCommand_destroy.argtypes = [DoubleCommand]
    DoubleCommand_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1132
if _libs["/usr/local/lib/lib60870.so"].has("DoubleCommand_create", "cdecl"):
    DoubleCommand_create = _libs["/usr/local/lib/lib60870.so"].get("DoubleCommand_create", "cdecl")
    DoubleCommand_create.argtypes = [DoubleCommand, c_int, c_int, c_bool, c_int]
    DoubleCommand_create.restype = DoubleCommand

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1140
if _libs["/usr/local/lib/lib60870.so"].has("DoubleCommand_getQU", "cdecl"):
    DoubleCommand_getQU = _libs["/usr/local/lib/lib60870.so"].get("DoubleCommand_getQU", "cdecl")
    DoubleCommand_getQU.argtypes = [DoubleCommand]
    DoubleCommand_getQU.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1148
if _libs["/usr/local/lib/lib60870.so"].has("DoubleCommand_getState", "cdecl"):
    DoubleCommand_getState = _libs["/usr/local/lib/lib60870.so"].get("DoubleCommand_getState", "cdecl")
    DoubleCommand_getState.argtypes = [DoubleCommand]
    DoubleCommand_getState.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1156
if _libs["/usr/local/lib/lib60870.so"].has("DoubleCommand_isSelect", "cdecl"):
    DoubleCommand_isSelect = _libs["/usr/local/lib/lib60870.so"].get("DoubleCommand_isSelect", "cdecl")
    DoubleCommand_isSelect.argtypes = [DoubleCommand]
    DoubleCommand_isSelect.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1162
class struct_sStepCommand(Structure):
    pass

StepCommand = POINTER(struct_sStepCommand)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1162

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1165
if _libs["/usr/local/lib/lib60870.so"].has("StepCommand_destroy", "cdecl"):
    StepCommand_destroy = _libs["/usr/local/lib/lib60870.so"].get("StepCommand_destroy", "cdecl")
    StepCommand_destroy.argtypes = [StepCommand]
    StepCommand_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1168
if _libs["/usr/local/lib/lib60870.so"].has("StepCommand_create", "cdecl"):
    StepCommand_create = _libs["/usr/local/lib/lib60870.so"].get("StepCommand_create", "cdecl")
    StepCommand_create.argtypes = [StepCommand, c_int, StepCommandValue, c_bool, c_int]
    StepCommand_create.restype = StepCommand

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1176
if _libs["/usr/local/lib/lib60870.so"].has("StepCommand_getQU", "cdecl"):
    StepCommand_getQU = _libs["/usr/local/lib/lib60870.so"].get("StepCommand_getQU", "cdecl")
    StepCommand_getQU.argtypes = [StepCommand]
    StepCommand_getQU.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1179
if _libs["/usr/local/lib/lib60870.so"].has("StepCommand_getState", "cdecl"):
    StepCommand_getState = _libs["/usr/local/lib/lib60870.so"].get("StepCommand_getState", "cdecl")
    StepCommand_getState.argtypes = [StepCommand]
    StepCommand_getState.restype = StepCommandValue

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1187
if _libs["/usr/local/lib/lib60870.so"].has("StepCommand_isSelect", "cdecl"):
    StepCommand_isSelect = _libs["/usr/local/lib/lib60870.so"].get("StepCommand_isSelect", "cdecl")
    StepCommand_isSelect.argtypes = [StepCommand]
    StepCommand_isSelect.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1193
class struct_sSetpointCommandNormalized(Structure):
    pass

SetpointCommandNormalized = POINTER(struct_sSetpointCommandNormalized)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1193

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1196
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandNormalized_destroy", "cdecl"):
    SetpointCommandNormalized_destroy = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandNormalized_destroy", "cdecl")
    SetpointCommandNormalized_destroy.argtypes = [SetpointCommandNormalized]
    SetpointCommandNormalized_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1210
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandNormalized_create", "cdecl"):
    SetpointCommandNormalized_create = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandNormalized_create", "cdecl")
    SetpointCommandNormalized_create.argtypes = [SetpointCommandNormalized, c_int, c_float, c_bool, c_int]
    SetpointCommandNormalized_create.restype = SetpointCommandNormalized

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1213
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandNormalized_getValue", "cdecl"):
    SetpointCommandNormalized_getValue = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandNormalized_getValue", "cdecl")
    SetpointCommandNormalized_getValue.argtypes = [SetpointCommandNormalized]
    SetpointCommandNormalized_getValue.restype = c_float

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1216
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandNormalized_getQL", "cdecl"):
    SetpointCommandNormalized_getQL = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandNormalized_getQL", "cdecl")
    SetpointCommandNormalized_getQL.argtypes = [SetpointCommandNormalized]
    SetpointCommandNormalized_getQL.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1224
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandNormalized_isSelect", "cdecl"):
    SetpointCommandNormalized_isSelect = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandNormalized_isSelect", "cdecl")
    SetpointCommandNormalized_isSelect.argtypes = [SetpointCommandNormalized]
    SetpointCommandNormalized_isSelect.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1230
class struct_sSetpointCommandScaled(Structure):
    pass

SetpointCommandScaled = POINTER(struct_sSetpointCommandScaled)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1230

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1233
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandScaled_destroy", "cdecl"):
    SetpointCommandScaled_destroy = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandScaled_destroy", "cdecl")
    SetpointCommandScaled_destroy.argtypes = [SetpointCommandScaled]
    SetpointCommandScaled_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1247
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandScaled_create", "cdecl"):
    SetpointCommandScaled_create = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandScaled_create", "cdecl")
    SetpointCommandScaled_create.argtypes = [SetpointCommandScaled, c_int, c_int, c_bool, c_int]
    SetpointCommandScaled_create.restype = SetpointCommandScaled

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1250
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandScaled_getValue", "cdecl"):
    SetpointCommandScaled_getValue = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandScaled_getValue", "cdecl")
    SetpointCommandScaled_getValue.argtypes = [SetpointCommandScaled]
    SetpointCommandScaled_getValue.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1253
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandScaled_getQL", "cdecl"):
    SetpointCommandScaled_getQL = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandScaled_getQL", "cdecl")
    SetpointCommandScaled_getQL.argtypes = [SetpointCommandScaled]
    SetpointCommandScaled_getQL.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1261
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandScaled_isSelect", "cdecl"):
    SetpointCommandScaled_isSelect = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandScaled_isSelect", "cdecl")
    SetpointCommandScaled_isSelect.argtypes = [SetpointCommandScaled]
    SetpointCommandScaled_isSelect.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1267
class struct_sSetpointCommandShort(Structure):
    pass

SetpointCommandShort = POINTER(struct_sSetpointCommandShort)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1267

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1270
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandShort_destroy", "cdecl"):
    SetpointCommandShort_destroy = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandShort_destroy", "cdecl")
    SetpointCommandShort_destroy.argtypes = [SetpointCommandShort]
    SetpointCommandShort_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1284
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandShort_create", "cdecl"):
    SetpointCommandShort_create = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandShort_create", "cdecl")
    SetpointCommandShort_create.argtypes = [SetpointCommandShort, c_int, c_float, c_bool, c_int]
    SetpointCommandShort_create.restype = SetpointCommandShort

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1287
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandShort_getValue", "cdecl"):
    SetpointCommandShort_getValue = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandShort_getValue", "cdecl")
    SetpointCommandShort_getValue.argtypes = [SetpointCommandShort]
    SetpointCommandShort_getValue.restype = c_float

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1290
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandShort_getQL", "cdecl"):
    SetpointCommandShort_getQL = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandShort_getQL", "cdecl")
    SetpointCommandShort_getQL.argtypes = [SetpointCommandShort]
    SetpointCommandShort_getQL.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1298
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandShort_isSelect", "cdecl"):
    SetpointCommandShort_isSelect = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandShort_isSelect", "cdecl")
    SetpointCommandShort_isSelect.argtypes = [SetpointCommandShort]
    SetpointCommandShort_isSelect.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1304
class struct_sBitstring32Command(Structure):
    pass

Bitstring32Command = POINTER(struct_sBitstring32Command)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1304

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1307
if _libs["/usr/local/lib/lib60870.so"].has("Bitstring32Command_create", "cdecl"):
    Bitstring32Command_create = _libs["/usr/local/lib/lib60870.so"].get("Bitstring32Command_create", "cdecl")
    Bitstring32Command_create.argtypes = [Bitstring32Command, c_int, c_uint32]
    Bitstring32Command_create.restype = Bitstring32Command

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1310
if _libs["/usr/local/lib/lib60870.so"].has("Bitstring32Command_destroy", "cdecl"):
    Bitstring32Command_destroy = _libs["/usr/local/lib/lib60870.so"].get("Bitstring32Command_destroy", "cdecl")
    Bitstring32Command_destroy.argtypes = [Bitstring32Command]
    Bitstring32Command_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1313
if _libs["/usr/local/lib/lib60870.so"].has("Bitstring32Command_getValue", "cdecl"):
    Bitstring32Command_getValue = _libs["/usr/local/lib/lib60870.so"].get("Bitstring32Command_getValue", "cdecl")
    Bitstring32Command_getValue.argtypes = [Bitstring32Command]
    Bitstring32Command_getValue.restype = c_uint32

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1319
class struct_sInterrogationCommand(Structure):
    pass

InterrogationCommand = POINTER(struct_sInterrogationCommand)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1319

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1322
if _libs["/usr/local/lib/lib60870.so"].has("InterrogationCommand_create", "cdecl"):
    InterrogationCommand_create = _libs["/usr/local/lib/lib60870.so"].get("InterrogationCommand_create", "cdecl")
    InterrogationCommand_create.argtypes = [InterrogationCommand, c_int, c_uint8]
    InterrogationCommand_create.restype = InterrogationCommand

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1325
if _libs["/usr/local/lib/lib60870.so"].has("InterrogationCommand_destroy", "cdecl"):
    InterrogationCommand_destroy = _libs["/usr/local/lib/lib60870.so"].get("InterrogationCommand_destroy", "cdecl")
    InterrogationCommand_destroy.argtypes = [InterrogationCommand]
    InterrogationCommand_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1328
if _libs["/usr/local/lib/lib60870.so"].has("InterrogationCommand_getQOI", "cdecl"):
    InterrogationCommand_getQOI = _libs["/usr/local/lib/lib60870.so"].get("InterrogationCommand_getQOI", "cdecl")
    InterrogationCommand_getQOI.argtypes = [InterrogationCommand]
    InterrogationCommand_getQOI.restype = c_uint8

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1334
class struct_sReadCommand(Structure):
    pass

ReadCommand = POINTER(struct_sReadCommand)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1334

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1337
if _libs["/usr/local/lib/lib60870.so"].has("ReadCommand_create", "cdecl"):
    ReadCommand_create = _libs["/usr/local/lib/lib60870.so"].get("ReadCommand_create", "cdecl")
    ReadCommand_create.argtypes = [ReadCommand, c_int]
    ReadCommand_create.restype = ReadCommand

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1340
if _libs["/usr/local/lib/lib60870.so"].has("ReadCommand_destroy", "cdecl"):
    ReadCommand_destroy = _libs["/usr/local/lib/lib60870.so"].get("ReadCommand_destroy", "cdecl")
    ReadCommand_destroy.argtypes = [ReadCommand]
    ReadCommand_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1346
class struct_sClockSynchronizationCommand(Structure):
    pass

ClockSynchronizationCommand = POINTER(struct_sClockSynchronizationCommand)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1346

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1349
if _libs["/usr/local/lib/lib60870.so"].has("ClockSynchronizationCommand_create", "cdecl"):
    ClockSynchronizationCommand_create = _libs["/usr/local/lib/lib60870.so"].get("ClockSynchronizationCommand_create", "cdecl")
    ClockSynchronizationCommand_create.argtypes = [ClockSynchronizationCommand, c_int, CP56Time2a]
    ClockSynchronizationCommand_create.restype = ClockSynchronizationCommand

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1352
if _libs["/usr/local/lib/lib60870.so"].has("ClockSynchronizationCommand_destroy", "cdecl"):
    ClockSynchronizationCommand_destroy = _libs["/usr/local/lib/lib60870.so"].get("ClockSynchronizationCommand_destroy", "cdecl")
    ClockSynchronizationCommand_destroy.argtypes = [ClockSynchronizationCommand]
    ClockSynchronizationCommand_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1355
if _libs["/usr/local/lib/lib60870.so"].has("ClockSynchronizationCommand_getTime", "cdecl"):
    ClockSynchronizationCommand_getTime = _libs["/usr/local/lib/lib60870.so"].get("ClockSynchronizationCommand_getTime", "cdecl")
    ClockSynchronizationCommand_getTime.argtypes = [ClockSynchronizationCommand]
    ClockSynchronizationCommand_getTime.restype = CP56Time2a

ParameterNormalizedValue = POINTER(struct_sMeasuredValueNormalized)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1361

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1364
if _libs["/usr/local/lib/lib60870.so"].has("ParameterNormalizedValue_destroy", "cdecl"):
    ParameterNormalizedValue_destroy = _libs["/usr/local/lib/lib60870.so"].get("ParameterNormalizedValue_destroy", "cdecl")
    ParameterNormalizedValue_destroy.argtypes = [ParameterNormalizedValue]
    ParameterNormalizedValue_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1389
if _libs["/usr/local/lib/lib60870.so"].has("ParameterNormalizedValue_create", "cdecl"):
    ParameterNormalizedValue_create = _libs["/usr/local/lib/lib60870.so"].get("ParameterNormalizedValue_create", "cdecl")
    ParameterNormalizedValue_create.argtypes = [ParameterNormalizedValue, c_int, c_float, QualifierOfParameterMV]
    ParameterNormalizedValue_create.restype = ParameterNormalizedValue

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1392
if _libs["/usr/local/lib/lib60870.so"].has("ParameterNormalizedValue_getValue", "cdecl"):
    ParameterNormalizedValue_getValue = _libs["/usr/local/lib/lib60870.so"].get("ParameterNormalizedValue_getValue", "cdecl")
    ParameterNormalizedValue_getValue.argtypes = [ParameterNormalizedValue]
    ParameterNormalizedValue_getValue.restype = c_float

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1395
if _libs["/usr/local/lib/lib60870.so"].has("ParameterNormalizedValue_setValue", "cdecl"):
    ParameterNormalizedValue_setValue = _libs["/usr/local/lib/lib60870.so"].get("ParameterNormalizedValue_setValue", "cdecl")
    ParameterNormalizedValue_setValue.argtypes = [ParameterNormalizedValue, c_float]
    ParameterNormalizedValue_setValue.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1403
if _libs["/usr/local/lib/lib60870.so"].has("ParameterNormalizedValue_getQPM", "cdecl"):
    ParameterNormalizedValue_getQPM = _libs["/usr/local/lib/lib60870.so"].get("ParameterNormalizedValue_getQPM", "cdecl")
    ParameterNormalizedValue_getQPM.argtypes = [ParameterNormalizedValue]
    ParameterNormalizedValue_getQPM.restype = QualifierOfParameterMV

ParameterScaledValue = POINTER(struct_sMeasuredValueScaled)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1409

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1412
if _libs["/usr/local/lib/lib60870.so"].has("ParameterScaledValue_destroy", "cdecl"):
    ParameterScaledValue_destroy = _libs["/usr/local/lib/lib60870.so"].get("ParameterScaledValue_destroy", "cdecl")
    ParameterScaledValue_destroy.argtypes = [ParameterScaledValue]
    ParameterScaledValue_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1437
if _libs["/usr/local/lib/lib60870.so"].has("ParameterScaledValue_create", "cdecl"):
    ParameterScaledValue_create = _libs["/usr/local/lib/lib60870.so"].get("ParameterScaledValue_create", "cdecl")
    ParameterScaledValue_create.argtypes = [ParameterScaledValue, c_int, c_int, QualifierOfParameterMV]
    ParameterScaledValue_create.restype = ParameterScaledValue

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1440
if _libs["/usr/local/lib/lib60870.so"].has("ParameterScaledValue_getValue", "cdecl"):
    ParameterScaledValue_getValue = _libs["/usr/local/lib/lib60870.so"].get("ParameterScaledValue_getValue", "cdecl")
    ParameterScaledValue_getValue.argtypes = [ParameterScaledValue]
    ParameterScaledValue_getValue.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1443
if _libs["/usr/local/lib/lib60870.so"].has("ParameterScaledValue_setValue", "cdecl"):
    ParameterScaledValue_setValue = _libs["/usr/local/lib/lib60870.so"].get("ParameterScaledValue_setValue", "cdecl")
    ParameterScaledValue_setValue.argtypes = [ParameterScaledValue, c_int]
    ParameterScaledValue_setValue.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1451
if _libs["/usr/local/lib/lib60870.so"].has("ParameterScaledValue_getQPM", "cdecl"):
    ParameterScaledValue_getQPM = _libs["/usr/local/lib/lib60870.so"].get("ParameterScaledValue_getQPM", "cdecl")
    ParameterScaledValue_getQPM.argtypes = [ParameterScaledValue]
    ParameterScaledValue_getQPM.restype = QualifierOfParameterMV

ParameterFloatValue = POINTER(struct_sMeasuredValueShort)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1457

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1460
if _libs["/usr/local/lib/lib60870.so"].has("ParameterFloatValue_destroy", "cdecl"):
    ParameterFloatValue_destroy = _libs["/usr/local/lib/lib60870.so"].get("ParameterFloatValue_destroy", "cdecl")
    ParameterFloatValue_destroy.argtypes = [ParameterFloatValue]
    ParameterFloatValue_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1485
if _libs["/usr/local/lib/lib60870.so"].has("ParameterFloatValue_create", "cdecl"):
    ParameterFloatValue_create = _libs["/usr/local/lib/lib60870.so"].get("ParameterFloatValue_create", "cdecl")
    ParameterFloatValue_create.argtypes = [ParameterFloatValue, c_int, c_float, QualifierOfParameterMV]
    ParameterFloatValue_create.restype = ParameterFloatValue

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1488
if _libs["/usr/local/lib/lib60870.so"].has("ParameterFloatValue_getValue", "cdecl"):
    ParameterFloatValue_getValue = _libs["/usr/local/lib/lib60870.so"].get("ParameterFloatValue_getValue", "cdecl")
    ParameterFloatValue_getValue.argtypes = [ParameterFloatValue]
    ParameterFloatValue_getValue.restype = c_float

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1491
if _libs["/usr/local/lib/lib60870.so"].has("ParameterFloatValue_setValue", "cdecl"):
    ParameterFloatValue_setValue = _libs["/usr/local/lib/lib60870.so"].get("ParameterFloatValue_setValue", "cdecl")
    ParameterFloatValue_setValue.argtypes = [ParameterFloatValue, c_float]
    ParameterFloatValue_setValue.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1499
if _libs["/usr/local/lib/lib60870.so"].has("ParameterFloatValue_getQPM", "cdecl"):
    ParameterFloatValue_getQPM = _libs["/usr/local/lib/lib60870.so"].get("ParameterFloatValue_getQPM", "cdecl")
    ParameterFloatValue_getQPM.argtypes = [ParameterFloatValue]
    ParameterFloatValue_getQPM.restype = QualifierOfParameterMV

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1505
class struct_sParameterActivation(Structure):
    pass

ParameterActivation = POINTER(struct_sParameterActivation)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1505

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1508
if _libs["/usr/local/lib/lib60870.so"].has("ParameterActivation_destroy", "cdecl"):
    ParameterActivation_destroy = _libs["/usr/local/lib/lib60870.so"].get("ParameterActivation_destroy", "cdecl")
    ParameterActivation_destroy.argtypes = [ParameterActivation]
    ParameterActivation_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1520
if _libs["/usr/local/lib/lib60870.so"].has("ParameterActivation_create", "cdecl"):
    ParameterActivation_create = _libs["/usr/local/lib/lib60870.so"].get("ParameterActivation_create", "cdecl")
    ParameterActivation_create.argtypes = [ParameterActivation, c_int, QualifierOfParameterActivation]
    ParameterActivation_create.restype = ParameterActivation

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1528
if _libs["/usr/local/lib/lib60870.so"].has("ParameterActivation_getQuality", "cdecl"):
    ParameterActivation_getQuality = _libs["/usr/local/lib/lib60870.so"].get("ParameterActivation_getQuality", "cdecl")
    ParameterActivation_getQuality.argtypes = [ParameterActivation]
    ParameterActivation_getQuality.restype = QualifierOfParameterActivation

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1534
class struct_sEventOfProtectionEquipmentWithCP56Time2a(Structure):
    pass

EventOfProtectionEquipmentWithCP56Time2a = POINTER(struct_sEventOfProtectionEquipmentWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1534

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1537
if _libs["/usr/local/lib/lib60870.so"].has("EventOfProtectionEquipmentWithCP56Time2a_destroy", "cdecl"):
    EventOfProtectionEquipmentWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("EventOfProtectionEquipmentWithCP56Time2a_destroy", "cdecl")
    EventOfProtectionEquipmentWithCP56Time2a_destroy.argtypes = [EventOfProtectionEquipmentWithCP56Time2a]
    EventOfProtectionEquipmentWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1540
if _libs["/usr/local/lib/lib60870.so"].has("EventOfProtectionEquipmentWithCP56Time2a_create", "cdecl"):
    EventOfProtectionEquipmentWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("EventOfProtectionEquipmentWithCP56Time2a_create", "cdecl")
    EventOfProtectionEquipmentWithCP56Time2a_create.argtypes = [EventOfProtectionEquipmentWithCP56Time2a, c_int, SingleEvent, CP16Time2a, CP56Time2a]
    EventOfProtectionEquipmentWithCP56Time2a_create.restype = EventOfProtectionEquipmentWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1544
if _libs["/usr/local/lib/lib60870.so"].has("EventOfProtectionEquipmentWithCP56Time2a_getEvent", "cdecl"):
    EventOfProtectionEquipmentWithCP56Time2a_getEvent = _libs["/usr/local/lib/lib60870.so"].get("EventOfProtectionEquipmentWithCP56Time2a_getEvent", "cdecl")
    EventOfProtectionEquipmentWithCP56Time2a_getEvent.argtypes = [EventOfProtectionEquipmentWithCP56Time2a]
    EventOfProtectionEquipmentWithCP56Time2a_getEvent.restype = SingleEvent

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1547
if _libs["/usr/local/lib/lib60870.so"].has("EventOfProtectionEquipmentWithCP56Time2a_getElapsedTime", "cdecl"):
    EventOfProtectionEquipmentWithCP56Time2a_getElapsedTime = _libs["/usr/local/lib/lib60870.so"].get("EventOfProtectionEquipmentWithCP56Time2a_getElapsedTime", "cdecl")
    EventOfProtectionEquipmentWithCP56Time2a_getElapsedTime.argtypes = [EventOfProtectionEquipmentWithCP56Time2a]
    EventOfProtectionEquipmentWithCP56Time2a_getElapsedTime.restype = CP16Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1550
if _libs["/usr/local/lib/lib60870.so"].has("EventOfProtectionEquipmentWithCP56Time2a_getTimestamp", "cdecl"):
    EventOfProtectionEquipmentWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("EventOfProtectionEquipmentWithCP56Time2a_getTimestamp", "cdecl")
    EventOfProtectionEquipmentWithCP56Time2a_getTimestamp.argtypes = [EventOfProtectionEquipmentWithCP56Time2a]
    EventOfProtectionEquipmentWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1556
class struct_sPackedStartEventsOfProtectionEquipmentWithCP56Time2a(Structure):
    pass

PackedStartEventsOfProtectionEquipmentWithCP56Time2a = POINTER(struct_sPackedStartEventsOfProtectionEquipmentWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1556

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1559
if _libs["/usr/local/lib/lib60870.so"].has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_destroy", "cdecl"):
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_destroy", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_destroy.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1562
if _libs["/usr/local/lib/lib60870.so"].has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_create", "cdecl"):
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_create", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_create.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a, c_int, StartEvent, QualityDescriptorP, CP16Time2a, CP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_create.restype = PackedStartEventsOfProtectionEquipmentWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1566
if _libs["/usr/local/lib/lib60870.so"].has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getEvent", "cdecl"):
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getEvent = _libs["/usr/local/lib/lib60870.so"].get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getEvent", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getEvent.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getEvent.restype = StartEvent

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1569
if _libs["/usr/local/lib/lib60870.so"].has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getQuality", "cdecl"):
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getQuality = _libs["/usr/local/lib/lib60870.so"].get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getQuality", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getQuality.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getQuality.restype = QualityDescriptorP

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1572
if _libs["/usr/local/lib/lib60870.so"].has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getElapsedTime", "cdecl"):
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getElapsedTime = _libs["/usr/local/lib/lib60870.so"].get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getElapsedTime", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getElapsedTime.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getElapsedTime.restype = CP16Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1575
if _libs["/usr/local/lib/lib60870.so"].has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getTimestamp", "cdecl"):
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getTimestamp", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getTimestamp.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1581
class struct_sPackedOutputCircuitInfoWithCP56Time2a(Structure):
    pass

PackedOutputCircuitInfoWithCP56Time2a = POINTER(struct_sPackedOutputCircuitInfoWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1581

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1584
if _libs["/usr/local/lib/lib60870.so"].has("PackedOutputCircuitInfoWithCP56Time2a_destroy", "cdecl"):
    PackedOutputCircuitInfoWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("PackedOutputCircuitInfoWithCP56Time2a_destroy", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_destroy.argtypes = [PackedOutputCircuitInfoWithCP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1587
if _libs["/usr/local/lib/lib60870.so"].has("PackedOutputCircuitInfoWithCP56Time2a_create", "cdecl"):
    PackedOutputCircuitInfoWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("PackedOutputCircuitInfoWithCP56Time2a_create", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_create.argtypes = [PackedOutputCircuitInfoWithCP56Time2a, c_int, OutputCircuitInfo, QualityDescriptorP, CP16Time2a, CP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_create.restype = PackedOutputCircuitInfoWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1591
if _libs["/usr/local/lib/lib60870.so"].has("PackedOutputCircuitInfoWithCP56Time2a_getOCI", "cdecl"):
    PackedOutputCircuitInfoWithCP56Time2a_getOCI = _libs["/usr/local/lib/lib60870.so"].get("PackedOutputCircuitInfoWithCP56Time2a_getOCI", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_getOCI.argtypes = [PackedOutputCircuitInfoWithCP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_getOCI.restype = OutputCircuitInfo

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1594
if _libs["/usr/local/lib/lib60870.so"].has("PackedOutputCircuitInfoWithCP56Time2a_getQuality", "cdecl"):
    PackedOutputCircuitInfoWithCP56Time2a_getQuality = _libs["/usr/local/lib/lib60870.so"].get("PackedOutputCircuitInfoWithCP56Time2a_getQuality", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_getQuality.argtypes = [PackedOutputCircuitInfoWithCP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_getQuality.restype = QualityDescriptorP

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1597
if _libs["/usr/local/lib/lib60870.so"].has("PackedOutputCircuitInfoWithCP56Time2a_getOperatingTime", "cdecl"):
    PackedOutputCircuitInfoWithCP56Time2a_getOperatingTime = _libs["/usr/local/lib/lib60870.so"].get("PackedOutputCircuitInfoWithCP56Time2a_getOperatingTime", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_getOperatingTime.argtypes = [PackedOutputCircuitInfoWithCP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_getOperatingTime.restype = CP16Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1600
if _libs["/usr/local/lib/lib60870.so"].has("PackedOutputCircuitInfoWithCP56Time2a_getTimestamp", "cdecl"):
    PackedOutputCircuitInfoWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("PackedOutputCircuitInfoWithCP56Time2a_getTimestamp", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_getTimestamp.argtypes = [PackedOutputCircuitInfoWithCP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1606
class struct_sDoubleCommandWithCP56Time2a(Structure):
    pass

DoubleCommandWithCP56Time2a = POINTER(struct_sDoubleCommandWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1606

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1609
if _libs["/usr/local/lib/lib60870.so"].has("DoubleCommandWithCP56Time2a_destroy", "cdecl"):
    DoubleCommandWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("DoubleCommandWithCP56Time2a_destroy", "cdecl")
    DoubleCommandWithCP56Time2a_destroy.argtypes = [DoubleCommandWithCP56Time2a]
    DoubleCommandWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1612
if _libs["/usr/local/lib/lib60870.so"].has("DoubleCommandWithCP56Time2a_create", "cdecl"):
    DoubleCommandWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("DoubleCommandWithCP56Time2a_create", "cdecl")
    DoubleCommandWithCP56Time2a_create.argtypes = [DoubleCommandWithCP56Time2a, c_int, c_int, c_bool, c_int, CP56Time2a]
    DoubleCommandWithCP56Time2a_create.restype = DoubleCommandWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1615
if _libs["/usr/local/lib/lib60870.so"].has("DoubleCommandWithCP56Time2a_getQU", "cdecl"):
    DoubleCommandWithCP56Time2a_getQU = _libs["/usr/local/lib/lib60870.so"].get("DoubleCommandWithCP56Time2a_getQU", "cdecl")
    DoubleCommandWithCP56Time2a_getQU.argtypes = [DoubleCommandWithCP56Time2a]
    DoubleCommandWithCP56Time2a_getQU.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1618
if _libs["/usr/local/lib/lib60870.so"].has("DoubleCommandWithCP56Time2a_getState", "cdecl"):
    DoubleCommandWithCP56Time2a_getState = _libs["/usr/local/lib/lib60870.so"].get("DoubleCommandWithCP56Time2a_getState", "cdecl")
    DoubleCommandWithCP56Time2a_getState.argtypes = [DoubleCommandWithCP56Time2a]
    DoubleCommandWithCP56Time2a_getState.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1621
if _libs["/usr/local/lib/lib60870.so"].has("DoubleCommandWithCP56Time2a_isSelect", "cdecl"):
    DoubleCommandWithCP56Time2a_isSelect = _libs["/usr/local/lib/lib60870.so"].get("DoubleCommandWithCP56Time2a_isSelect", "cdecl")
    DoubleCommandWithCP56Time2a_isSelect.argtypes = [DoubleCommandWithCP56Time2a]
    DoubleCommandWithCP56Time2a_isSelect.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1624
if _libs["/usr/local/lib/lib60870.so"].has("DoubleCommandWithCP56Time2a_getTimestamp", "cdecl"):
    DoubleCommandWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("DoubleCommandWithCP56Time2a_getTimestamp", "cdecl")
    DoubleCommandWithCP56Time2a_getTimestamp.argtypes = [DoubleCommandWithCP56Time2a]
    DoubleCommandWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1630
class struct_sStepCommandWithCP56Time2a(Structure):
    pass

StepCommandWithCP56Time2a = POINTER(struct_sStepCommandWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1630

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1633
if _libs["/usr/local/lib/lib60870.so"].has("StepCommandWithCP56Time2a_destroy", "cdecl"):
    StepCommandWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("StepCommandWithCP56Time2a_destroy", "cdecl")
    StepCommandWithCP56Time2a_destroy.argtypes = [StepCommandWithCP56Time2a]
    StepCommandWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1636
if _libs["/usr/local/lib/lib60870.so"].has("StepCommandWithCP56Time2a_create", "cdecl"):
    StepCommandWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("StepCommandWithCP56Time2a_create", "cdecl")
    StepCommandWithCP56Time2a_create.argtypes = [StepCommandWithCP56Time2a, c_int, StepCommandValue, c_bool, c_int, CP56Time2a]
    StepCommandWithCP56Time2a_create.restype = StepCommandWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1639
if _libs["/usr/local/lib/lib60870.so"].has("StepCommandWithCP56Time2a_getQU", "cdecl"):
    StepCommandWithCP56Time2a_getQU = _libs["/usr/local/lib/lib60870.so"].get("StepCommandWithCP56Time2a_getQU", "cdecl")
    StepCommandWithCP56Time2a_getQU.argtypes = [StepCommandWithCP56Time2a]
    StepCommandWithCP56Time2a_getQU.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1642
if _libs["/usr/local/lib/lib60870.so"].has("StepCommandWithCP56Time2a_getState", "cdecl"):
    StepCommandWithCP56Time2a_getState = _libs["/usr/local/lib/lib60870.so"].get("StepCommandWithCP56Time2a_getState", "cdecl")
    StepCommandWithCP56Time2a_getState.argtypes = [StepCommandWithCP56Time2a]
    StepCommandWithCP56Time2a_getState.restype = StepCommandValue

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1645
if _libs["/usr/local/lib/lib60870.so"].has("StepCommandWithCP56Time2a_isSelect", "cdecl"):
    StepCommandWithCP56Time2a_isSelect = _libs["/usr/local/lib/lib60870.so"].get("StepCommandWithCP56Time2a_isSelect", "cdecl")
    StepCommandWithCP56Time2a_isSelect.argtypes = [StepCommandWithCP56Time2a]
    StepCommandWithCP56Time2a_isSelect.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1648
if _libs["/usr/local/lib/lib60870.so"].has("StepCommandWithCP56Time2a_getTimestamp", "cdecl"):
    StepCommandWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("StepCommandWithCP56Time2a_getTimestamp", "cdecl")
    StepCommandWithCP56Time2a_getTimestamp.argtypes = [StepCommandWithCP56Time2a]
    StepCommandWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1654
class struct_sSetpointCommandNormalizedWithCP56Time2a(Structure):
    pass

SetpointCommandNormalizedWithCP56Time2a = POINTER(struct_sSetpointCommandNormalizedWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1654

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1657
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandNormalizedWithCP56Time2a_destroy", "cdecl"):
    SetpointCommandNormalizedWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandNormalizedWithCP56Time2a_destroy", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_destroy.argtypes = [SetpointCommandNormalizedWithCP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1660
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandNormalizedWithCP56Time2a_create", "cdecl"):
    SetpointCommandNormalizedWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandNormalizedWithCP56Time2a_create", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_create.argtypes = [SetpointCommandNormalizedWithCP56Time2a, c_int, c_float, c_bool, c_int, CP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_create.restype = SetpointCommandNormalizedWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1663
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandNormalizedWithCP56Time2a_getValue", "cdecl"):
    SetpointCommandNormalizedWithCP56Time2a_getValue = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandNormalizedWithCP56Time2a_getValue", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_getValue.argtypes = [SetpointCommandNormalizedWithCP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_getValue.restype = c_float

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1666
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandNormalizedWithCP56Time2a_getQL", "cdecl"):
    SetpointCommandNormalizedWithCP56Time2a_getQL = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandNormalizedWithCP56Time2a_getQL", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_getQL.argtypes = [SetpointCommandNormalizedWithCP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_getQL.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1669
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandNormalizedWithCP56Time2a_isSelect", "cdecl"):
    SetpointCommandNormalizedWithCP56Time2a_isSelect = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandNormalizedWithCP56Time2a_isSelect", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_isSelect.argtypes = [SetpointCommandNormalizedWithCP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_isSelect.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1672
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandNormalizedWithCP56Time2a_getTimestamp", "cdecl"):
    SetpointCommandNormalizedWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandNormalizedWithCP56Time2a_getTimestamp", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_getTimestamp.argtypes = [SetpointCommandNormalizedWithCP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1678
class struct_sSetpointCommandScaledWithCP56Time2a(Structure):
    pass

SetpointCommandScaledWithCP56Time2a = POINTER(struct_sSetpointCommandScaledWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1678

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1681
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandScaledWithCP56Time2a_destroy", "cdecl"):
    SetpointCommandScaledWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandScaledWithCP56Time2a_destroy", "cdecl")
    SetpointCommandScaledWithCP56Time2a_destroy.argtypes = [SetpointCommandScaledWithCP56Time2a]
    SetpointCommandScaledWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1684
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandScaledWithCP56Time2a_create", "cdecl"):
    SetpointCommandScaledWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandScaledWithCP56Time2a_create", "cdecl")
    SetpointCommandScaledWithCP56Time2a_create.argtypes = [SetpointCommandScaledWithCP56Time2a, c_int, c_int, c_bool, c_int, CP56Time2a]
    SetpointCommandScaledWithCP56Time2a_create.restype = SetpointCommandScaledWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1687
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandScaledWithCP56Time2a_getValue", "cdecl"):
    SetpointCommandScaledWithCP56Time2a_getValue = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandScaledWithCP56Time2a_getValue", "cdecl")
    SetpointCommandScaledWithCP56Time2a_getValue.argtypes = [SetpointCommandScaledWithCP56Time2a]
    SetpointCommandScaledWithCP56Time2a_getValue.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1690
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandScaledWithCP56Time2a_getQL", "cdecl"):
    SetpointCommandScaledWithCP56Time2a_getQL = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandScaledWithCP56Time2a_getQL", "cdecl")
    SetpointCommandScaledWithCP56Time2a_getQL.argtypes = [SetpointCommandScaledWithCP56Time2a]
    SetpointCommandScaledWithCP56Time2a_getQL.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1693
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandScaledWithCP56Time2a_isSelect", "cdecl"):
    SetpointCommandScaledWithCP56Time2a_isSelect = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandScaledWithCP56Time2a_isSelect", "cdecl")
    SetpointCommandScaledWithCP56Time2a_isSelect.argtypes = [SetpointCommandScaledWithCP56Time2a]
    SetpointCommandScaledWithCP56Time2a_isSelect.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1696
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandScaledWithCP56Time2a_getTimestamp", "cdecl"):
    SetpointCommandScaledWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandScaledWithCP56Time2a_getTimestamp", "cdecl")
    SetpointCommandScaledWithCP56Time2a_getTimestamp.argtypes = [SetpointCommandScaledWithCP56Time2a]
    SetpointCommandScaledWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1702
class struct_sSetpointCommandShortWithCP56Time2a(Structure):
    pass

SetpointCommandShortWithCP56Time2a = POINTER(struct_sSetpointCommandShortWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1702

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1705
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandShortWithCP56Time2a_destroy", "cdecl"):
    SetpointCommandShortWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandShortWithCP56Time2a_destroy", "cdecl")
    SetpointCommandShortWithCP56Time2a_destroy.argtypes = [SetpointCommandShortWithCP56Time2a]
    SetpointCommandShortWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1708
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandShortWithCP56Time2a_create", "cdecl"):
    SetpointCommandShortWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandShortWithCP56Time2a_create", "cdecl")
    SetpointCommandShortWithCP56Time2a_create.argtypes = [SetpointCommandShortWithCP56Time2a, c_int, c_float, c_bool, c_int, CP56Time2a]
    SetpointCommandShortWithCP56Time2a_create.restype = SetpointCommandShortWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1711
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandShortWithCP56Time2a_getValue", "cdecl"):
    SetpointCommandShortWithCP56Time2a_getValue = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandShortWithCP56Time2a_getValue", "cdecl")
    SetpointCommandShortWithCP56Time2a_getValue.argtypes = [SetpointCommandShortWithCP56Time2a]
    SetpointCommandShortWithCP56Time2a_getValue.restype = c_float

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1714
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandShortWithCP56Time2a_getQL", "cdecl"):
    SetpointCommandShortWithCP56Time2a_getQL = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandShortWithCP56Time2a_getQL", "cdecl")
    SetpointCommandShortWithCP56Time2a_getQL.argtypes = [SetpointCommandShortWithCP56Time2a]
    SetpointCommandShortWithCP56Time2a_getQL.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1717
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandShortWithCP56Time2a_isSelect", "cdecl"):
    SetpointCommandShortWithCP56Time2a_isSelect = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandShortWithCP56Time2a_isSelect", "cdecl")
    SetpointCommandShortWithCP56Time2a_isSelect.argtypes = [SetpointCommandShortWithCP56Time2a]
    SetpointCommandShortWithCP56Time2a_isSelect.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1720
if _libs["/usr/local/lib/lib60870.so"].has("SetpointCommandShortWithCP56Time2a_getTimestamp", "cdecl"):
    SetpointCommandShortWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("SetpointCommandShortWithCP56Time2a_getTimestamp", "cdecl")
    SetpointCommandShortWithCP56Time2a_getTimestamp.argtypes = [SetpointCommandShortWithCP56Time2a]
    SetpointCommandShortWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1726
class struct_sBitstring32CommandWithCP56Time2a(Structure):
    pass

Bitstring32CommandWithCP56Time2a = POINTER(struct_sBitstring32CommandWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1726

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1729
if _libs["/usr/local/lib/lib60870.so"].has("Bitstring32CommandWithCP56Time2a_create", "cdecl"):
    Bitstring32CommandWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("Bitstring32CommandWithCP56Time2a_create", "cdecl")
    Bitstring32CommandWithCP56Time2a_create.argtypes = [Bitstring32CommandWithCP56Time2a, c_int, c_uint32, CP56Time2a]
    Bitstring32CommandWithCP56Time2a_create.restype = Bitstring32CommandWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1732
if _libs["/usr/local/lib/lib60870.so"].has("Bitstring32CommandWithCP56Time2a_destroy", "cdecl"):
    Bitstring32CommandWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("Bitstring32CommandWithCP56Time2a_destroy", "cdecl")
    Bitstring32CommandWithCP56Time2a_destroy.argtypes = [Bitstring32CommandWithCP56Time2a]
    Bitstring32CommandWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1735
if _libs["/usr/local/lib/lib60870.so"].has("Bitstring32CommandWithCP56Time2a_getValue", "cdecl"):
    Bitstring32CommandWithCP56Time2a_getValue = _libs["/usr/local/lib/lib60870.so"].get("Bitstring32CommandWithCP56Time2a_getValue", "cdecl")
    Bitstring32CommandWithCP56Time2a_getValue.argtypes = [Bitstring32CommandWithCP56Time2a]
    Bitstring32CommandWithCP56Time2a_getValue.restype = c_uint32

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1738
if _libs["/usr/local/lib/lib60870.so"].has("Bitstring32CommandWithCP56Time2a_getTimestamp", "cdecl"):
    Bitstring32CommandWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("Bitstring32CommandWithCP56Time2a_getTimestamp", "cdecl")
    Bitstring32CommandWithCP56Time2a_getTimestamp.argtypes = [Bitstring32CommandWithCP56Time2a]
    Bitstring32CommandWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1745
class struct_sCounterInterrogationCommand(Structure):
    pass

CounterInterrogationCommand = POINTER(struct_sCounterInterrogationCommand)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1745

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1748
if _libs["/usr/local/lib/lib60870.so"].has("CounterInterrogationCommand_create", "cdecl"):
    CounterInterrogationCommand_create = _libs["/usr/local/lib/lib60870.so"].get("CounterInterrogationCommand_create", "cdecl")
    CounterInterrogationCommand_create.argtypes = [CounterInterrogationCommand, c_int, QualifierOfCIC]
    CounterInterrogationCommand_create.restype = CounterInterrogationCommand

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1751
if _libs["/usr/local/lib/lib60870.so"].has("CounterInterrogationCommand_destroy", "cdecl"):
    CounterInterrogationCommand_destroy = _libs["/usr/local/lib/lib60870.so"].get("CounterInterrogationCommand_destroy", "cdecl")
    CounterInterrogationCommand_destroy.argtypes = [CounterInterrogationCommand]
    CounterInterrogationCommand_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1754
if _libs["/usr/local/lib/lib60870.so"].has("CounterInterrogationCommand_getQCC", "cdecl"):
    CounterInterrogationCommand_getQCC = _libs["/usr/local/lib/lib60870.so"].get("CounterInterrogationCommand_getQCC", "cdecl")
    CounterInterrogationCommand_getQCC.argtypes = [CounterInterrogationCommand]
    CounterInterrogationCommand_getQCC.restype = QualifierOfCIC

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1760
class struct_sTestCommand(Structure):
    pass

TestCommand = POINTER(struct_sTestCommand)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1760

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1763
if _libs["/usr/local/lib/lib60870.so"].has("TestCommand_create", "cdecl"):
    TestCommand_create = _libs["/usr/local/lib/lib60870.so"].get("TestCommand_create", "cdecl")
    TestCommand_create.argtypes = [TestCommand]
    TestCommand_create.restype = TestCommand

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1766
if _libs["/usr/local/lib/lib60870.so"].has("TestCommand_destroy", "cdecl"):
    TestCommand_destroy = _libs["/usr/local/lib/lib60870.so"].get("TestCommand_destroy", "cdecl")
    TestCommand_destroy.argtypes = [TestCommand]
    TestCommand_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1769
if _libs["/usr/local/lib/lib60870.so"].has("TestCommand_isValid", "cdecl"):
    TestCommand_isValid = _libs["/usr/local/lib/lib60870.so"].get("TestCommand_isValid", "cdecl")
    TestCommand_isValid.argtypes = [TestCommand]
    TestCommand_isValid.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1775
class struct_sTestCommandWithCP56Time2a(Structure):
    pass

TestCommandWithCP56Time2a = POINTER(struct_sTestCommandWithCP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1775

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1787
if _libs["/usr/local/lib/lib60870.so"].has("TestCommandWithCP56Time2a_create", "cdecl"):
    TestCommandWithCP56Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("TestCommandWithCP56Time2a_create", "cdecl")
    TestCommandWithCP56Time2a_create.argtypes = [TestCommandWithCP56Time2a, c_uint16, CP56Time2a]
    TestCommandWithCP56Time2a_create.restype = TestCommandWithCP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1790
if _libs["/usr/local/lib/lib60870.so"].has("TestCommandWithCP56Time2a_destroy", "cdecl"):
    TestCommandWithCP56Time2a_destroy = _libs["/usr/local/lib/lib60870.so"].get("TestCommandWithCP56Time2a_destroy", "cdecl")
    TestCommandWithCP56Time2a_destroy.argtypes = [TestCommandWithCP56Time2a]
    TestCommandWithCP56Time2a_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1793
if _libs["/usr/local/lib/lib60870.so"].has("TestCommandWithCP56Time2a_getCounter", "cdecl"):
    TestCommandWithCP56Time2a_getCounter = _libs["/usr/local/lib/lib60870.so"].get("TestCommandWithCP56Time2a_getCounter", "cdecl")
    TestCommandWithCP56Time2a_getCounter.argtypes = [TestCommandWithCP56Time2a]
    TestCommandWithCP56Time2a_getCounter.restype = c_uint16

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1796
if _libs["/usr/local/lib/lib60870.so"].has("TestCommandWithCP56Time2a_getTimestamp", "cdecl"):
    TestCommandWithCP56Time2a_getTimestamp = _libs["/usr/local/lib/lib60870.so"].get("TestCommandWithCP56Time2a_getTimestamp", "cdecl")
    TestCommandWithCP56Time2a_getTimestamp.argtypes = [TestCommandWithCP56Time2a]
    TestCommandWithCP56Time2a_getTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1802
class struct_sResetProcessCommand(Structure):
    pass

ResetProcessCommand = POINTER(struct_sResetProcessCommand)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1802

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1805
if _libs["/usr/local/lib/lib60870.so"].has("ResetProcessCommand_create", "cdecl"):
    ResetProcessCommand_create = _libs["/usr/local/lib/lib60870.so"].get("ResetProcessCommand_create", "cdecl")
    ResetProcessCommand_create.argtypes = [ResetProcessCommand, c_int, QualifierOfRPC]
    ResetProcessCommand_create.restype = ResetProcessCommand

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1808
if _libs["/usr/local/lib/lib60870.so"].has("ResetProcessCommand_destroy", "cdecl"):
    ResetProcessCommand_destroy = _libs["/usr/local/lib/lib60870.so"].get("ResetProcessCommand_destroy", "cdecl")
    ResetProcessCommand_destroy.argtypes = [ResetProcessCommand]
    ResetProcessCommand_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1811
if _libs["/usr/local/lib/lib60870.so"].has("ResetProcessCommand_getQRP", "cdecl"):
    ResetProcessCommand_getQRP = _libs["/usr/local/lib/lib60870.so"].get("ResetProcessCommand_getQRP", "cdecl")
    ResetProcessCommand_getQRP.argtypes = [ResetProcessCommand]
    ResetProcessCommand_getQRP.restype = QualifierOfRPC

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1817
class struct_sDelayAcquisitionCommand(Structure):
    pass

DelayAcquisitionCommand = POINTER(struct_sDelayAcquisitionCommand)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1817

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1820
if _libs["/usr/local/lib/lib60870.so"].has("DelayAcquisitionCommand_create", "cdecl"):
    DelayAcquisitionCommand_create = _libs["/usr/local/lib/lib60870.so"].get("DelayAcquisitionCommand_create", "cdecl")
    DelayAcquisitionCommand_create.argtypes = [DelayAcquisitionCommand, c_int, CP16Time2a]
    DelayAcquisitionCommand_create.restype = DelayAcquisitionCommand

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1823
if _libs["/usr/local/lib/lib60870.so"].has("DelayAcquisitionCommand_destroy", "cdecl"):
    DelayAcquisitionCommand_destroy = _libs["/usr/local/lib/lib60870.so"].get("DelayAcquisitionCommand_destroy", "cdecl")
    DelayAcquisitionCommand_destroy.argtypes = [DelayAcquisitionCommand]
    DelayAcquisitionCommand_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1826
if _libs["/usr/local/lib/lib60870.so"].has("DelayAcquisitionCommand_getDelay", "cdecl"):
    DelayAcquisitionCommand_getDelay = _libs["/usr/local/lib/lib60870.so"].get("DelayAcquisitionCommand_getDelay", "cdecl")
    DelayAcquisitionCommand_getDelay.argtypes = [DelayAcquisitionCommand]
    DelayAcquisitionCommand_getDelay.restype = CP16Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1832
class struct_sEndOfInitialization(Structure):
    pass

EndOfInitialization = POINTER(struct_sEndOfInitialization)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1832

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1835
if _libs["/usr/local/lib/lib60870.so"].has("EndOfInitialization_create", "cdecl"):
    EndOfInitialization_create = _libs["/usr/local/lib/lib60870.so"].get("EndOfInitialization_create", "cdecl")
    EndOfInitialization_create.argtypes = [EndOfInitialization, c_uint8]
    EndOfInitialization_create.restype = EndOfInitialization

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1838
if _libs["/usr/local/lib/lib60870.so"].has("EndOfInitialization_destroy", "cdecl"):
    EndOfInitialization_destroy = _libs["/usr/local/lib/lib60870.so"].get("EndOfInitialization_destroy", "cdecl")
    EndOfInitialization_destroy.argtypes = [EndOfInitialization]
    EndOfInitialization_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1841
if _libs["/usr/local/lib/lib60870.so"].has("EndOfInitialization_getCOI", "cdecl"):
    EndOfInitialization_getCOI = _libs["/usr/local/lib/lib60870.so"].get("EndOfInitialization_getCOI", "cdecl")
    EndOfInitialization_getCOI.argtypes = [EndOfInitialization]
    EndOfInitialization_getCOI.restype = c_uint8

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1973
class struct_sFileReady(Structure):
    pass

FileReady = POINTER(struct_sFileReady)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1973

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1987
if _libs["/usr/local/lib/lib60870.so"].has("FileReady_create", "cdecl"):
    FileReady_create = _libs["/usr/local/lib/lib60870.so"].get("FileReady_create", "cdecl")
    FileReady_create.argtypes = [FileReady, c_int, c_uint16, c_uint32, c_bool]
    FileReady_create.restype = FileReady

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1990
if _libs["/usr/local/lib/lib60870.so"].has("FileReady_destroy", "cdecl"):
    FileReady_destroy = _libs["/usr/local/lib/lib60870.so"].get("FileReady_destroy", "cdecl")
    FileReady_destroy.argtypes = [FileReady]
    FileReady_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1993
if _libs["/usr/local/lib/lib60870.so"].has("FileReady_getFRQ", "cdecl"):
    FileReady_getFRQ = _libs["/usr/local/lib/lib60870.so"].get("FileReady_getFRQ", "cdecl")
    FileReady_getFRQ.argtypes = [FileReady]
    FileReady_getFRQ.restype = c_uint8

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1996
if _libs["/usr/local/lib/lib60870.so"].has("FileReady_setFRQ", "cdecl"):
    FileReady_setFRQ = _libs["/usr/local/lib/lib60870.so"].get("FileReady_setFRQ", "cdecl")
    FileReady_setFRQ.argtypes = [FileReady, c_uint8]
    FileReady_setFRQ.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1999
if _libs["/usr/local/lib/lib60870.so"].has("FileReady_isPositive", "cdecl"):
    FileReady_isPositive = _libs["/usr/local/lib/lib60870.so"].get("FileReady_isPositive", "cdecl")
    FileReady_isPositive.argtypes = [FileReady]
    FileReady_isPositive.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2002
if _libs["/usr/local/lib/lib60870.so"].has("FileReady_getNOF", "cdecl"):
    FileReady_getNOF = _libs["/usr/local/lib/lib60870.so"].get("FileReady_getNOF", "cdecl")
    FileReady_getNOF.argtypes = [FileReady]
    FileReady_getNOF.restype = c_uint16

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2005
if _libs["/usr/local/lib/lib60870.so"].has("FileReady_getLengthOfFile", "cdecl"):
    FileReady_getLengthOfFile = _libs["/usr/local/lib/lib60870.so"].get("FileReady_getLengthOfFile", "cdecl")
    FileReady_getLengthOfFile.argtypes = [FileReady]
    FileReady_getLengthOfFile.restype = c_uint32

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2008
if _libs["/usr/local/lib/lib60870.so"].has("FileReady_destroy", "cdecl"):
    FileReady_destroy = _libs["/usr/local/lib/lib60870.so"].get("FileReady_destroy", "cdecl")
    FileReady_destroy.argtypes = [FileReady]
    FileReady_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2014
class struct_sSectionReady(Structure):
    pass

SectionReady = POINTER(struct_sSectionReady)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2014

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2017
if _libs["/usr/local/lib/lib60870.so"].has("SectionReady_create", "cdecl"):
    SectionReady_create = _libs["/usr/local/lib/lib60870.so"].get("SectionReady_create", "cdecl")
    SectionReady_create.argtypes = [SectionReady, c_int, c_uint16, c_uint8, c_uint32, c_bool]
    SectionReady_create.restype = SectionReady

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2021
if _libs["/usr/local/lib/lib60870.so"].has("SectionReady_isNotReady", "cdecl"):
    SectionReady_isNotReady = _libs["/usr/local/lib/lib60870.so"].get("SectionReady_isNotReady", "cdecl")
    SectionReady_isNotReady.argtypes = [SectionReady]
    SectionReady_isNotReady.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2024
if _libs["/usr/local/lib/lib60870.so"].has("SectionReady_getSRQ", "cdecl"):
    SectionReady_getSRQ = _libs["/usr/local/lib/lib60870.so"].get("SectionReady_getSRQ", "cdecl")
    SectionReady_getSRQ.argtypes = [SectionReady]
    SectionReady_getSRQ.restype = c_uint8

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2027
if _libs["/usr/local/lib/lib60870.so"].has("SectionReady_setSRQ", "cdecl"):
    SectionReady_setSRQ = _libs["/usr/local/lib/lib60870.so"].get("SectionReady_setSRQ", "cdecl")
    SectionReady_setSRQ.argtypes = [SectionReady, c_uint8]
    SectionReady_setSRQ.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2030
if _libs["/usr/local/lib/lib60870.so"].has("SectionReady_getNOF", "cdecl"):
    SectionReady_getNOF = _libs["/usr/local/lib/lib60870.so"].get("SectionReady_getNOF", "cdecl")
    SectionReady_getNOF.argtypes = [SectionReady]
    SectionReady_getNOF.restype = c_uint16

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2033
if _libs["/usr/local/lib/lib60870.so"].has("SectionReady_getNameOfSection", "cdecl"):
    SectionReady_getNameOfSection = _libs["/usr/local/lib/lib60870.so"].get("SectionReady_getNameOfSection", "cdecl")
    SectionReady_getNameOfSection.argtypes = [SectionReady]
    SectionReady_getNameOfSection.restype = c_uint8

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2036
if _libs["/usr/local/lib/lib60870.so"].has("SectionReady_getLengthOfSection", "cdecl"):
    SectionReady_getLengthOfSection = _libs["/usr/local/lib/lib60870.so"].get("SectionReady_getLengthOfSection", "cdecl")
    SectionReady_getLengthOfSection.argtypes = [SectionReady]
    SectionReady_getLengthOfSection.restype = c_uint32

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2039
if _libs["/usr/local/lib/lib60870.so"].has("SectionReady_destroy", "cdecl"):
    SectionReady_destroy = _libs["/usr/local/lib/lib60870.so"].get("SectionReady_destroy", "cdecl")
    SectionReady_destroy.argtypes = [SectionReady]
    SectionReady_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2046
class struct_sFileCallOrSelect(Structure):
    pass

FileCallOrSelect = POINTER(struct_sFileCallOrSelect)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2046

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2049
if _libs["/usr/local/lib/lib60870.so"].has("FileCallOrSelect_create", "cdecl"):
    FileCallOrSelect_create = _libs["/usr/local/lib/lib60870.so"].get("FileCallOrSelect_create", "cdecl")
    FileCallOrSelect_create.argtypes = [FileCallOrSelect, c_int, c_uint16, c_uint8, c_uint8]
    FileCallOrSelect_create.restype = FileCallOrSelect

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2052
if _libs["/usr/local/lib/lib60870.so"].has("FileCallOrSelect_getNOF", "cdecl"):
    FileCallOrSelect_getNOF = _libs["/usr/local/lib/lib60870.so"].get("FileCallOrSelect_getNOF", "cdecl")
    FileCallOrSelect_getNOF.argtypes = [FileCallOrSelect]
    FileCallOrSelect_getNOF.restype = c_uint16

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2055
if _libs["/usr/local/lib/lib60870.so"].has("FileCallOrSelect_getNameOfSection", "cdecl"):
    FileCallOrSelect_getNameOfSection = _libs["/usr/local/lib/lib60870.so"].get("FileCallOrSelect_getNameOfSection", "cdecl")
    FileCallOrSelect_getNameOfSection.argtypes = [FileCallOrSelect]
    FileCallOrSelect_getNameOfSection.restype = c_uint8

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2058
if _libs["/usr/local/lib/lib60870.so"].has("FileCallOrSelect_getSCQ", "cdecl"):
    FileCallOrSelect_getSCQ = _libs["/usr/local/lib/lib60870.so"].get("FileCallOrSelect_getSCQ", "cdecl")
    FileCallOrSelect_getSCQ.argtypes = [FileCallOrSelect]
    FileCallOrSelect_getSCQ.restype = c_uint8

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2061
if _libs["/usr/local/lib/lib60870.so"].has("FileCallOrSelect_destroy", "cdecl"):
    FileCallOrSelect_destroy = _libs["/usr/local/lib/lib60870.so"].get("FileCallOrSelect_destroy", "cdecl")
    FileCallOrSelect_destroy.argtypes = [FileCallOrSelect]
    FileCallOrSelect_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2067
class struct_sFileLastSegmentOrSection(Structure):
    pass

FileLastSegmentOrSection = POINTER(struct_sFileLastSegmentOrSection)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2067

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2070
if _libs["/usr/local/lib/lib60870.so"].has("FileLastSegmentOrSection_create", "cdecl"):
    FileLastSegmentOrSection_create = _libs["/usr/local/lib/lib60870.so"].get("FileLastSegmentOrSection_create", "cdecl")
    FileLastSegmentOrSection_create.argtypes = [FileLastSegmentOrSection, c_int, c_uint16, c_uint8, c_uint8, c_uint8]
    FileLastSegmentOrSection_create.restype = FileLastSegmentOrSection

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2073
if _libs["/usr/local/lib/lib60870.so"].has("FileLastSegmentOrSection_getNOF", "cdecl"):
    FileLastSegmentOrSection_getNOF = _libs["/usr/local/lib/lib60870.so"].get("FileLastSegmentOrSection_getNOF", "cdecl")
    FileLastSegmentOrSection_getNOF.argtypes = [FileLastSegmentOrSection]
    FileLastSegmentOrSection_getNOF.restype = c_uint16

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2076
if _libs["/usr/local/lib/lib60870.so"].has("FileLastSegmentOrSection_getNameOfSection", "cdecl"):
    FileLastSegmentOrSection_getNameOfSection = _libs["/usr/local/lib/lib60870.so"].get("FileLastSegmentOrSection_getNameOfSection", "cdecl")
    FileLastSegmentOrSection_getNameOfSection.argtypes = [FileLastSegmentOrSection]
    FileLastSegmentOrSection_getNameOfSection.restype = c_uint8

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2079
if _libs["/usr/local/lib/lib60870.so"].has("FileLastSegmentOrSection_getLSQ", "cdecl"):
    FileLastSegmentOrSection_getLSQ = _libs["/usr/local/lib/lib60870.so"].get("FileLastSegmentOrSection_getLSQ", "cdecl")
    FileLastSegmentOrSection_getLSQ.argtypes = [FileLastSegmentOrSection]
    FileLastSegmentOrSection_getLSQ.restype = c_uint8

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2082
if _libs["/usr/local/lib/lib60870.so"].has("FileLastSegmentOrSection_getCHS", "cdecl"):
    FileLastSegmentOrSection_getCHS = _libs["/usr/local/lib/lib60870.so"].get("FileLastSegmentOrSection_getCHS", "cdecl")
    FileLastSegmentOrSection_getCHS.argtypes = [FileLastSegmentOrSection]
    FileLastSegmentOrSection_getCHS.restype = c_uint8

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2085
if _libs["/usr/local/lib/lib60870.so"].has("FileLastSegmentOrSection_destroy", "cdecl"):
    FileLastSegmentOrSection_destroy = _libs["/usr/local/lib/lib60870.so"].get("FileLastSegmentOrSection_destroy", "cdecl")
    FileLastSegmentOrSection_destroy.argtypes = [FileLastSegmentOrSection]
    FileLastSegmentOrSection_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2091
class struct_sFileACK(Structure):
    pass

FileACK = POINTER(struct_sFileACK)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2091

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2094
if _libs["/usr/local/lib/lib60870.so"].has("FileACK_create", "cdecl"):
    FileACK_create = _libs["/usr/local/lib/lib60870.so"].get("FileACK_create", "cdecl")
    FileACK_create.argtypes = [FileACK, c_int, c_uint16, c_uint8, c_uint8]
    FileACK_create.restype = FileACK

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2097
if _libs["/usr/local/lib/lib60870.so"].has("FileACK_getNOF", "cdecl"):
    FileACK_getNOF = _libs["/usr/local/lib/lib60870.so"].get("FileACK_getNOF", "cdecl")
    FileACK_getNOF.argtypes = [FileACK]
    FileACK_getNOF.restype = c_uint16

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2100
if _libs["/usr/local/lib/lib60870.so"].has("FileACK_getNameOfSection", "cdecl"):
    FileACK_getNameOfSection = _libs["/usr/local/lib/lib60870.so"].get("FileACK_getNameOfSection", "cdecl")
    FileACK_getNameOfSection.argtypes = [FileACK]
    FileACK_getNameOfSection.restype = c_uint8

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2103
if _libs["/usr/local/lib/lib60870.so"].has("FileACK_getAFQ", "cdecl"):
    FileACK_getAFQ = _libs["/usr/local/lib/lib60870.so"].get("FileACK_getAFQ", "cdecl")
    FileACK_getAFQ.argtypes = [FileACK]
    FileACK_getAFQ.restype = c_uint8

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2106
if _libs["/usr/local/lib/lib60870.so"].has("FileACK_destroy", "cdecl"):
    FileACK_destroy = _libs["/usr/local/lib/lib60870.so"].get("FileACK_destroy", "cdecl")
    FileACK_destroy.argtypes = [FileACK]
    FileACK_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2112
class struct_sFileSegment(Structure):
    pass

FileSegment = POINTER(struct_sFileSegment)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2112

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2115
if _libs["/usr/local/lib/lib60870.so"].has("FileSegment_create", "cdecl"):
    FileSegment_create = _libs["/usr/local/lib/lib60870.so"].get("FileSegment_create", "cdecl")
    FileSegment_create.argtypes = [FileSegment, c_int, c_uint16, c_uint8, POINTER(c_uint8), c_uint8]
    FileSegment_create.restype = FileSegment

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2118
if _libs["/usr/local/lib/lib60870.so"].has("FileSegment_getNOF", "cdecl"):
    FileSegment_getNOF = _libs["/usr/local/lib/lib60870.so"].get("FileSegment_getNOF", "cdecl")
    FileSegment_getNOF.argtypes = [FileSegment]
    FileSegment_getNOF.restype = c_uint16

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2121
if _libs["/usr/local/lib/lib60870.so"].has("FileSegment_getNameOfSection", "cdecl"):
    FileSegment_getNameOfSection = _libs["/usr/local/lib/lib60870.so"].get("FileSegment_getNameOfSection", "cdecl")
    FileSegment_getNameOfSection.argtypes = [FileSegment]
    FileSegment_getNameOfSection.restype = c_uint8

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2124
if _libs["/usr/local/lib/lib60870.so"].has("FileSegment_getLengthOfSegment", "cdecl"):
    FileSegment_getLengthOfSegment = _libs["/usr/local/lib/lib60870.so"].get("FileSegment_getLengthOfSegment", "cdecl")
    FileSegment_getLengthOfSegment.argtypes = [FileSegment]
    FileSegment_getLengthOfSegment.restype = c_uint8

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2126
if _libs["/usr/local/lib/lib60870.so"].has("FileSegment_getSegmentData", "cdecl"):
    FileSegment_getSegmentData = _libs["/usr/local/lib/lib60870.so"].get("FileSegment_getSegmentData", "cdecl")
    FileSegment_getSegmentData.argtypes = [FileSegment]
    FileSegment_getSegmentData.restype = POINTER(c_uint8)

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2130
if _libs["/usr/local/lib/lib60870.so"].has("FileSegment_GetMaxDataSize", "cdecl"):
    FileSegment_GetMaxDataSize = _libs["/usr/local/lib/lib60870.so"].get("FileSegment_GetMaxDataSize", "cdecl")
    FileSegment_GetMaxDataSize.argtypes = [CS101_AppLayerParameters]
    FileSegment_GetMaxDataSize.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2133
if _libs["/usr/local/lib/lib60870.so"].has("FileSegment_destroy", "cdecl"):
    FileSegment_destroy = _libs["/usr/local/lib/lib60870.so"].get("FileSegment_destroy", "cdecl")
    FileSegment_destroy.argtypes = [FileSegment]
    FileSegment_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2139
class struct_sFileDirectory(Structure):
    pass

FileDirectory = POINTER(struct_sFileDirectory)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2139

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2142
if _libs["/usr/local/lib/lib60870.so"].has("FileDirectory_create", "cdecl"):
    FileDirectory_create = _libs["/usr/local/lib/lib60870.so"].get("FileDirectory_create", "cdecl")
    FileDirectory_create.argtypes = [FileDirectory, c_int, c_uint16, c_int, c_uint8, CP56Time2a]
    FileDirectory_create.restype = FileDirectory

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2145
if _libs["/usr/local/lib/lib60870.so"].has("FileDirectory_getNOF", "cdecl"):
    FileDirectory_getNOF = _libs["/usr/local/lib/lib60870.so"].get("FileDirectory_getNOF", "cdecl")
    FileDirectory_getNOF.argtypes = [FileDirectory]
    FileDirectory_getNOF.restype = c_uint16

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2148
if _libs["/usr/local/lib/lib60870.so"].has("FileDirectory_getSOF", "cdecl"):
    FileDirectory_getSOF = _libs["/usr/local/lib/lib60870.so"].get("FileDirectory_getSOF", "cdecl")
    FileDirectory_getSOF.argtypes = [FileDirectory]
    FileDirectory_getSOF.restype = c_uint8

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2151
if _libs["/usr/local/lib/lib60870.so"].has("FileDirectory_getSTATUS", "cdecl"):
    FileDirectory_getSTATUS = _libs["/usr/local/lib/lib60870.so"].get("FileDirectory_getSTATUS", "cdecl")
    FileDirectory_getSTATUS.argtypes = [FileDirectory]
    FileDirectory_getSTATUS.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2154
if _libs["/usr/local/lib/lib60870.so"].has("FileDirectory_getLFD", "cdecl"):
    FileDirectory_getLFD = _libs["/usr/local/lib/lib60870.so"].get("FileDirectory_getLFD", "cdecl")
    FileDirectory_getLFD.argtypes = [FileDirectory]
    FileDirectory_getLFD.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2157
if _libs["/usr/local/lib/lib60870.so"].has("FileDirectory_getFOR", "cdecl"):
    FileDirectory_getFOR = _libs["/usr/local/lib/lib60870.so"].get("FileDirectory_getFOR", "cdecl")
    FileDirectory_getFOR.argtypes = [FileDirectory]
    FileDirectory_getFOR.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2160
if _libs["/usr/local/lib/lib60870.so"].has("FileDirectory_getFA", "cdecl"):
    FileDirectory_getFA = _libs["/usr/local/lib/lib60870.so"].get("FileDirectory_getFA", "cdecl")
    FileDirectory_getFA.argtypes = [FileDirectory]
    FileDirectory_getFA.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2163
if _libs["/usr/local/lib/lib60870.so"].has("FileDirectory_getLengthOfFile", "cdecl"):
    FileDirectory_getLengthOfFile = _libs["/usr/local/lib/lib60870.so"].get("FileDirectory_getLengthOfFile", "cdecl")
    FileDirectory_getLengthOfFile.argtypes = [FileDirectory]
    FileDirectory_getLengthOfFile.restype = c_uint8

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2166
if _libs["/usr/local/lib/lib60870.so"].has("FileDirectory_getCreationTime", "cdecl"):
    FileDirectory_getCreationTime = _libs["/usr/local/lib/lib60870.so"].get("FileDirectory_getCreationTime", "cdecl")
    FileDirectory_getCreationTime.argtypes = [FileDirectory]
    FileDirectory_getCreationTime.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2169
if _libs["/usr/local/lib/lib60870.so"].has("FileDirectory_destroy", "cdecl"):
    FileDirectory_destroy = _libs["/usr/local/lib/lib60870.so"].get("FileDirectory_destroy", "cdecl")
    FileDirectory_destroy.argtypes = [FileDirectory]
    FileDirectory_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2175
class struct_sQueryLog(Structure):
    pass

QueryLog = POINTER(struct_sQueryLog)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2175

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2178
if _libs["/usr/local/lib/lib60870.so"].has("QueryLog_create", "cdecl"):
    QueryLog_create = _libs["/usr/local/lib/lib60870.so"].get("QueryLog_create", "cdecl")
    QueryLog_create.argtypes = [QueryLog, c_int, c_uint16, CP56Time2a, CP56Time2a]
    QueryLog_create.restype = QueryLog

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2181
if _libs["/usr/local/lib/lib60870.so"].has("QueryLog_getNOF", "cdecl"):
    QueryLog_getNOF = _libs["/usr/local/lib/lib60870.so"].get("QueryLog_getNOF", "cdecl")
    QueryLog_getNOF.argtypes = [QueryLog]
    QueryLog_getNOF.restype = c_uint16

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2184
if _libs["/usr/local/lib/lib60870.so"].has("QueryLog_getRangeStartTime", "cdecl"):
    QueryLog_getRangeStartTime = _libs["/usr/local/lib/lib60870.so"].get("QueryLog_getRangeStartTime", "cdecl")
    QueryLog_getRangeStartTime.argtypes = [QueryLog]
    QueryLog_getRangeStartTime.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2188
if _libs["/usr/local/lib/lib60870.so"].has("QueryLog_getRangeStopTime", "cdecl"):
    QueryLog_getRangeStopTime = _libs["/usr/local/lib/lib60870.so"].get("QueryLog_getRangeStopTime", "cdecl")
    QueryLog_getRangeStopTime.argtypes = [QueryLog]
    QueryLog_getRangeStopTime.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2191
if _libs["/usr/local/lib/lib60870.so"].has("QueryLog_destroy", "cdecl"):
    QueryLog_destroy = _libs["/usr/local/lib/lib60870.so"].get("QueryLog_destroy", "cdecl")
    QueryLog_destroy.argtypes = [QueryLog]
    QueryLog_destroy.restype = None

enum_anon_30 = c_int# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_PERIODIC = 1# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_BACKGROUND_SCAN = 2# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_SPONTANEOUS = 3# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INITIALIZED = 4# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_REQUEST = 5# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_ACTIVATION = 6# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_ACTIVATION_CON = 7# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_DEACTIVATION = 8# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_DEACTIVATION_CON = 9# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_ACTIVATION_TERMINATION = 10# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_RETURN_INFO_REMOTE = 11# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_RETURN_INFO_LOCAL = 12# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_FILE_TRANSFER = 13# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_AUTHENTICATION = 14# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_MAINTENANCE_OF_AUTH_SESSION_KEY = 15# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_MAINTENANCE_OF_USER_ROLE_AND_UPDATE_KEY = 16# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INTERROGATED_BY_STATION = 20# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INTERROGATED_BY_GROUP_1 = 21# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INTERROGATED_BY_GROUP_2 = 22# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INTERROGATED_BY_GROUP_3 = 23# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INTERROGATED_BY_GROUP_4 = 24# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INTERROGATED_BY_GROUP_5 = 25# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INTERROGATED_BY_GROUP_6 = 26# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INTERROGATED_BY_GROUP_7 = 27# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INTERROGATED_BY_GROUP_8 = 28# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INTERROGATED_BY_GROUP_9 = 29# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INTERROGATED_BY_GROUP_10 = 30# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INTERROGATED_BY_GROUP_11 = 31# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INTERROGATED_BY_GROUP_12 = 32# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INTERROGATED_BY_GROUP_13 = 33# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INTERROGATED_BY_GROUP_14 = 34# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INTERROGATED_BY_GROUP_15 = 35# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_INTERROGATED_BY_GROUP_16 = 36# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_REQUESTED_BY_GENERAL_COUNTER = 37# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_REQUESTED_BY_GROUP_1_COUNTER = 38# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_REQUESTED_BY_GROUP_2_COUNTER = 39# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_REQUESTED_BY_GROUP_3_COUNTER = 40# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_REQUESTED_BY_GROUP_4_COUNTER = 41# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_UNKNOWN_TYPE_ID = 44# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_UNKNOWN_COT = 45# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_UNKNOWN_CA = 46# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_COT_UNKNOWN_IOA = 47# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

CS101_CauseOfTransmission = enum_anon_30# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 236

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 238
if _libs["/usr/local/lib/lib60870.so"].has("CS101_CauseOfTransmission_toString", "cdecl"):
    CS101_CauseOfTransmission_toString = _libs["/usr/local/lib/lib60870.so"].get("CS101_CauseOfTransmission_toString", "cdecl")
    CS101_CauseOfTransmission_toString.argtypes = [CS101_CauseOfTransmission]
    CS101_CauseOfTransmission_toString.restype = c_char_p

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 242
if _libs["/usr/local/lib/lib60870.so"].has("Lib60870_enableDebugOutput", "cdecl"):
    Lib60870_enableDebugOutput = _libs["/usr/local/lib/lib60870.so"].get("Lib60870_enableDebugOutput", "cdecl")
    Lib60870_enableDebugOutput.argtypes = [c_bool]
    Lib60870_enableDebugOutput.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 245
if _libs["/usr/local/lib/lib60870.so"].has("Lib60870_getLibraryVersionInfo", "cdecl"):
    Lib60870_getLibraryVersionInfo = _libs["/usr/local/lib/lib60870.so"].get("Lib60870_getLibraryVersionInfo", "cdecl")
    Lib60870_getLibraryVersionInfo.argtypes = []
    Lib60870_getLibraryVersionInfo.restype = Lib60870VersionInfo

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 251
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_isTest", "cdecl"):
    CS101_ASDU_isTest = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_isTest", "cdecl")
    CS101_ASDU_isTest.argtypes = [CS101_ASDU]
    CS101_ASDU_isTest.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 257
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_setTest", "cdecl"):
    CS101_ASDU_setTest = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_setTest", "cdecl")
    CS101_ASDU_setTest.argtypes = [CS101_ASDU, c_bool]
    CS101_ASDU_setTest.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 263
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_isNegative", "cdecl"):
    CS101_ASDU_isNegative = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_isNegative", "cdecl")
    CS101_ASDU_isNegative.argtypes = [CS101_ASDU]
    CS101_ASDU_isNegative.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 269
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_setNegative", "cdecl"):
    CS101_ASDU_setNegative = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_setNegative", "cdecl")
    CS101_ASDU_setNegative.argtypes = [CS101_ASDU, c_bool]
    CS101_ASDU_setNegative.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 275
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_getOA", "cdecl"):
    CS101_ASDU_getOA = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_getOA", "cdecl")
    CS101_ASDU_getOA.argtypes = [CS101_ASDU]
    CS101_ASDU_getOA.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 281
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_getCOT", "cdecl"):
    CS101_ASDU_getCOT = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_getCOT", "cdecl")
    CS101_ASDU_getCOT.argtypes = [CS101_ASDU]
    CS101_ASDU_getCOT.restype = CS101_CauseOfTransmission

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 287
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_setCOT", "cdecl"):
    CS101_ASDU_setCOT = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_setCOT", "cdecl")
    CS101_ASDU_setCOT.argtypes = [CS101_ASDU, CS101_CauseOfTransmission]
    CS101_ASDU_setCOT.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 293
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_getCA", "cdecl"):
    CS101_ASDU_getCA = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_getCA", "cdecl")
    CS101_ASDU_getCA.argtypes = [CS101_ASDU]
    CS101_ASDU_getCA.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 301
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_setCA", "cdecl"):
    CS101_ASDU_setCA = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_setCA", "cdecl")
    CS101_ASDU_setCA.argtypes = [CS101_ASDU, c_int]
    CS101_ASDU_setCA.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 310
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_getTypeID", "cdecl"):
    CS101_ASDU_getTypeID = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_getTypeID", "cdecl")
    CS101_ASDU_getTypeID.argtypes = [CS101_ASDU]
    CS101_ASDU_getTypeID.restype = IEC60870_5_TypeID

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 322
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_setTypeID", "cdecl"):
    CS101_ASDU_setTypeID = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_setTypeID", "cdecl")
    CS101_ASDU_setTypeID.argtypes = [CS101_ASDU, IEC60870_5_TypeID]
    CS101_ASDU_setTypeID.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 333
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_isSequence", "cdecl"):
    CS101_ASDU_isSequence = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_isSequence", "cdecl")
    CS101_ASDU_isSequence.argtypes = [CS101_ASDU]
    CS101_ASDU_isSequence.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 344
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_setSequence", "cdecl"):
    CS101_ASDU_setSequence = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_setSequence", "cdecl")
    CS101_ASDU_setSequence.argtypes = [CS101_ASDU, c_bool]
    CS101_ASDU_setSequence.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 352
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_getNumberOfElements", "cdecl"):
    CS101_ASDU_getNumberOfElements = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_getNumberOfElements", "cdecl")
    CS101_ASDU_getNumberOfElements.argtypes = [CS101_ASDU]
    CS101_ASDU_getNumberOfElements.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 364
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_setNumberOfElements", "cdecl"):
    CS101_ASDU_setNumberOfElements = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_setNumberOfElements", "cdecl")
    CS101_ASDU_setNumberOfElements.argtypes = [CS101_ASDU, c_int]
    CS101_ASDU_setNumberOfElements.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 374
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_getElement", "cdecl"):
    CS101_ASDU_getElement = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_getElement", "cdecl")
    CS101_ASDU_getElement.argtypes = [CS101_ASDU, c_int]
    CS101_ASDU_getElement.restype = InformationObject

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 385
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_getElementEx", "cdecl"):
    CS101_ASDU_getElementEx = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_getElementEx", "cdecl")
    CS101_ASDU_getElementEx.argtypes = [CS101_ASDU, InformationObject, c_int]
    CS101_ASDU_getElementEx.restype = InformationObject

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 401
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_create", "cdecl"):
    CS101_ASDU_create = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_create", "cdecl")
    CS101_ASDU_create.argtypes = [CS101_AppLayerParameters, c_bool, CS101_CauseOfTransmission, c_int, c_int, c_bool, c_bool]
    CS101_ASDU_create.restype = CS101_ASDU

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 421
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_initializeStatic", "cdecl"):
    CS101_ASDU_initializeStatic = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_initializeStatic", "cdecl")
    CS101_ASDU_initializeStatic.argtypes = [CS101_StaticASDU, CS101_AppLayerParameters, c_bool, CS101_CauseOfTransmission, c_int, c_int, c_bool, c_bool]
    CS101_ASDU_initializeStatic.restype = CS101_ASDU

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 431
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_getPayload", "cdecl"):
    CS101_ASDU_getPayload = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_getPayload", "cdecl")
    CS101_ASDU_getPayload.argtypes = [CS101_ASDU]
    CS101_ASDU_getPayload.restype = POINTER(c_uint8)

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 447
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_addPayload", "cdecl"):
    CS101_ASDU_addPayload = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_addPayload", "cdecl")
    CS101_ASDU_addPayload.argtypes = [CS101_ASDU, POINTER(c_uint8), c_int]
    CS101_ASDU_addPayload.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 457
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_getPayloadSize", "cdecl"):
    CS101_ASDU_getPayloadSize = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_getPayloadSize", "cdecl")
    CS101_ASDU_getPayloadSize.argtypes = [CS101_ASDU]
    CS101_ASDU_getPayloadSize.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 463
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_destroy", "cdecl"):
    CS101_ASDU_destroy = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_destroy", "cdecl")
    CS101_ASDU_destroy.argtypes = [CS101_ASDU]
    CS101_ASDU_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 476
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_addInformationObject", "cdecl"):
    CS101_ASDU_addInformationObject = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_addInformationObject", "cdecl")
    CS101_ASDU_addInformationObject.argtypes = [CS101_ASDU, InformationObject]
    CS101_ASDU_addInformationObject.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 484
if _libs["/usr/local/lib/lib60870.so"].has("CS101_ASDU_removeAllElements", "cdecl"):
    CS101_ASDU_removeAllElements = _libs["/usr/local/lib/lib60870.so"].get("CS101_ASDU_removeAllElements", "cdecl")
    CS101_ASDU_removeAllElements.argtypes = [CS101_ASDU]
    CS101_ASDU_removeAllElements.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 490
if _libs["/usr/local/lib/lib60870.so"].has("CP16Time2a_getEplapsedTimeInMs", "cdecl"):
    CP16Time2a_getEplapsedTimeInMs = _libs["/usr/local/lib/lib60870.so"].get("CP16Time2a_getEplapsedTimeInMs", "cdecl")
    CP16Time2a_getEplapsedTimeInMs.argtypes = [CP16Time2a]
    CP16Time2a_getEplapsedTimeInMs.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 496
if _libs["/usr/local/lib/lib60870.so"].has("CP16Time2a_setEplapsedTimeInMs", "cdecl"):
    CP16Time2a_setEplapsedTimeInMs = _libs["/usr/local/lib/lib60870.so"].get("CP16Time2a_setEplapsedTimeInMs", "cdecl")
    CP16Time2a_setEplapsedTimeInMs.argtypes = [CP16Time2a, c_int]
    CP16Time2a_setEplapsedTimeInMs.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 502
if _libs["/usr/local/lib/lib60870.so"].has("CP24Time2a_getMillisecond", "cdecl"):
    CP24Time2a_getMillisecond = _libs["/usr/local/lib/lib60870.so"].get("CP24Time2a_getMillisecond", "cdecl")
    CP24Time2a_getMillisecond.argtypes = [CP24Time2a]
    CP24Time2a_getMillisecond.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 508
if _libs["/usr/local/lib/lib60870.so"].has("CP24Time2a_setMillisecond", "cdecl"):
    CP24Time2a_setMillisecond = _libs["/usr/local/lib/lib60870.so"].get("CP24Time2a_setMillisecond", "cdecl")
    CP24Time2a_setMillisecond.argtypes = [CP24Time2a, c_int]
    CP24Time2a_setMillisecond.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 514
if _libs["/usr/local/lib/lib60870.so"].has("CP24Time2a_getSecond", "cdecl"):
    CP24Time2a_getSecond = _libs["/usr/local/lib/lib60870.so"].get("CP24Time2a_getSecond", "cdecl")
    CP24Time2a_getSecond.argtypes = [CP24Time2a]
    CP24Time2a_getSecond.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 520
if _libs["/usr/local/lib/lib60870.so"].has("CP24Time2a_setSecond", "cdecl"):
    CP24Time2a_setSecond = _libs["/usr/local/lib/lib60870.so"].get("CP24Time2a_setSecond", "cdecl")
    CP24Time2a_setSecond.argtypes = [CP24Time2a, c_int]
    CP24Time2a_setSecond.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 526
if _libs["/usr/local/lib/lib60870.so"].has("CP24Time2a_getMinute", "cdecl"):
    CP24Time2a_getMinute = _libs["/usr/local/lib/lib60870.so"].get("CP24Time2a_getMinute", "cdecl")
    CP24Time2a_getMinute.argtypes = [CP24Time2a]
    CP24Time2a_getMinute.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 532
if _libs["/usr/local/lib/lib60870.so"].has("CP24Time2a_setMinute", "cdecl"):
    CP24Time2a_setMinute = _libs["/usr/local/lib/lib60870.so"].get("CP24Time2a_setMinute", "cdecl")
    CP24Time2a_setMinute.argtypes = [CP24Time2a, c_int]
    CP24Time2a_setMinute.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 538
if _libs["/usr/local/lib/lib60870.so"].has("CP24Time2a_isInvalid", "cdecl"):
    CP24Time2a_isInvalid = _libs["/usr/local/lib/lib60870.so"].get("CP24Time2a_isInvalid", "cdecl")
    CP24Time2a_isInvalid.argtypes = [CP24Time2a]
    CP24Time2a_isInvalid.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 544
if _libs["/usr/local/lib/lib60870.so"].has("CP24Time2a_setInvalid", "cdecl"):
    CP24Time2a_setInvalid = _libs["/usr/local/lib/lib60870.so"].get("CP24Time2a_setInvalid", "cdecl")
    CP24Time2a_setInvalid.argtypes = [CP24Time2a, c_bool]
    CP24Time2a_setInvalid.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 550
if _libs["/usr/local/lib/lib60870.so"].has("CP24Time2a_isSubstituted", "cdecl"):
    CP24Time2a_isSubstituted = _libs["/usr/local/lib/lib60870.so"].get("CP24Time2a_isSubstituted", "cdecl")
    CP24Time2a_isSubstituted.argtypes = [CP24Time2a]
    CP24Time2a_isSubstituted.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 556
if _libs["/usr/local/lib/lib60870.so"].has("CP24Time2a_setSubstituted", "cdecl"):
    CP24Time2a_setSubstituted = _libs["/usr/local/lib/lib60870.so"].get("CP24Time2a_setSubstituted", "cdecl")
    CP24Time2a_setSubstituted.argtypes = [CP24Time2a, c_bool]
    CP24Time2a_setSubstituted.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 562
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_createFromMsTimestamp", "cdecl"):
    CP56Time2a_createFromMsTimestamp = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_createFromMsTimestamp", "cdecl")
    CP56Time2a_createFromMsTimestamp.argtypes = [CP56Time2a, c_uint64]
    CP56Time2a_createFromMsTimestamp.restype = CP56Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 566
if _libs["/usr/local/lib/lib60870.so"].has("CP32Time2a_create", "cdecl"):
    CP32Time2a_create = _libs["/usr/local/lib/lib60870.so"].get("CP32Time2a_create", "cdecl")
    CP32Time2a_create.argtypes = [CP32Time2a]
    CP32Time2a_create.restype = CP32Time2a

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 569
if _libs["/usr/local/lib/lib60870.so"].has("CP32Time2a_setFromMsTimestamp", "cdecl"):
    CP32Time2a_setFromMsTimestamp = _libs["/usr/local/lib/lib60870.so"].get("CP32Time2a_setFromMsTimestamp", "cdecl")
    CP32Time2a_setFromMsTimestamp.argtypes = [CP32Time2a, c_uint64]
    CP32Time2a_setFromMsTimestamp.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 572
if _libs["/usr/local/lib/lib60870.so"].has("CP32Time2a_getMillisecond", "cdecl"):
    CP32Time2a_getMillisecond = _libs["/usr/local/lib/lib60870.so"].get("CP32Time2a_getMillisecond", "cdecl")
    CP32Time2a_getMillisecond.argtypes = [CP32Time2a]
    CP32Time2a_getMillisecond.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 575
if _libs["/usr/local/lib/lib60870.so"].has("CP32Time2a_setMillisecond", "cdecl"):
    CP32Time2a_setMillisecond = _libs["/usr/local/lib/lib60870.so"].get("CP32Time2a_setMillisecond", "cdecl")
    CP32Time2a_setMillisecond.argtypes = [CP32Time2a, c_int]
    CP32Time2a_setMillisecond.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 578
if _libs["/usr/local/lib/lib60870.so"].has("CP32Time2a_getSecond", "cdecl"):
    CP32Time2a_getSecond = _libs["/usr/local/lib/lib60870.so"].get("CP32Time2a_getSecond", "cdecl")
    CP32Time2a_getSecond.argtypes = [CP32Time2a]
    CP32Time2a_getSecond.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 581
if _libs["/usr/local/lib/lib60870.so"].has("CP32Time2a_setSecond", "cdecl"):
    CP32Time2a_setSecond = _libs["/usr/local/lib/lib60870.so"].get("CP32Time2a_setSecond", "cdecl")
    CP32Time2a_setSecond.argtypes = [CP32Time2a, c_int]
    CP32Time2a_setSecond.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 584
if _libs["/usr/local/lib/lib60870.so"].has("CP32Time2a_getMinute", "cdecl"):
    CP32Time2a_getMinute = _libs["/usr/local/lib/lib60870.so"].get("CP32Time2a_getMinute", "cdecl")
    CP32Time2a_getMinute.argtypes = [CP32Time2a]
    CP32Time2a_getMinute.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 588
if _libs["/usr/local/lib/lib60870.so"].has("CP32Time2a_setMinute", "cdecl"):
    CP32Time2a_setMinute = _libs["/usr/local/lib/lib60870.so"].get("CP32Time2a_setMinute", "cdecl")
    CP32Time2a_setMinute.argtypes = [CP32Time2a, c_int]
    CP32Time2a_setMinute.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 591
if _libs["/usr/local/lib/lib60870.so"].has("CP32Time2a_isInvalid", "cdecl"):
    CP32Time2a_isInvalid = _libs["/usr/local/lib/lib60870.so"].get("CP32Time2a_isInvalid", "cdecl")
    CP32Time2a_isInvalid.argtypes = [CP32Time2a]
    CP32Time2a_isInvalid.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 594
if _libs["/usr/local/lib/lib60870.so"].has("CP32Time2a_setInvalid", "cdecl"):
    CP32Time2a_setInvalid = _libs["/usr/local/lib/lib60870.so"].get("CP32Time2a_setInvalid", "cdecl")
    CP32Time2a_setInvalid.argtypes = [CP32Time2a, c_bool]
    CP32Time2a_setInvalid.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 597
if _libs["/usr/local/lib/lib60870.so"].has("CP32Time2a_isSubstituted", "cdecl"):
    CP32Time2a_isSubstituted = _libs["/usr/local/lib/lib60870.so"].get("CP32Time2a_isSubstituted", "cdecl")
    CP32Time2a_isSubstituted.argtypes = [CP32Time2a]
    CP32Time2a_isSubstituted.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 600
if _libs["/usr/local/lib/lib60870.so"].has("CP32Time2a_setSubstituted", "cdecl"):
    CP32Time2a_setSubstituted = _libs["/usr/local/lib/lib60870.so"].get("CP32Time2a_setSubstituted", "cdecl")
    CP32Time2a_setSubstituted.argtypes = [CP32Time2a, c_bool]
    CP32Time2a_setSubstituted.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 603
if _libs["/usr/local/lib/lib60870.so"].has("CP32Time2a_getHour", "cdecl"):
    CP32Time2a_getHour = _libs["/usr/local/lib/lib60870.so"].get("CP32Time2a_getHour", "cdecl")
    CP32Time2a_getHour.argtypes = [CP32Time2a]
    CP32Time2a_getHour.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 606
if _libs["/usr/local/lib/lib60870.so"].has("CP32Time2a_setHour", "cdecl"):
    CP32Time2a_setHour = _libs["/usr/local/lib/lib60870.so"].get("CP32Time2a_setHour", "cdecl")
    CP32Time2a_setHour.argtypes = [CP32Time2a, c_int]
    CP32Time2a_setHour.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 609
if _libs["/usr/local/lib/lib60870.so"].has("CP32Time2a_isSummerTime", "cdecl"):
    CP32Time2a_isSummerTime = _libs["/usr/local/lib/lib60870.so"].get("CP32Time2a_isSummerTime", "cdecl")
    CP32Time2a_isSummerTime.argtypes = [CP32Time2a]
    CP32Time2a_isSummerTime.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 612
if _libs["/usr/local/lib/lib60870.so"].has("CP32Time2a_setSummerTime", "cdecl"):
    CP32Time2a_setSummerTime = _libs["/usr/local/lib/lib60870.so"].get("CP32Time2a_setSummerTime", "cdecl")
    CP32Time2a_setSummerTime.argtypes = [CP32Time2a, c_bool]
    CP32Time2a_setSummerTime.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 618
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_setFromMsTimestamp", "cdecl"):
    CP56Time2a_setFromMsTimestamp = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_setFromMsTimestamp", "cdecl")
    CP56Time2a_setFromMsTimestamp.argtypes = [CP56Time2a, c_uint64]
    CP56Time2a_setFromMsTimestamp.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 624
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_toMsTimestamp", "cdecl"):
    CP56Time2a_toMsTimestamp = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_toMsTimestamp", "cdecl")
    CP56Time2a_toMsTimestamp.argtypes = [CP56Time2a]
    CP56Time2a_toMsTimestamp.restype = c_uint64

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 630
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_getMillisecond", "cdecl"):
    CP56Time2a_getMillisecond = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_getMillisecond", "cdecl")
    CP56Time2a_getMillisecond.argtypes = [CP56Time2a]
    CP56Time2a_getMillisecond.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 636
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_setMillisecond", "cdecl"):
    CP56Time2a_setMillisecond = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_setMillisecond", "cdecl")
    CP56Time2a_setMillisecond.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setMillisecond.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 639
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_getSecond", "cdecl"):
    CP56Time2a_getSecond = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_getSecond", "cdecl")
    CP56Time2a_getSecond.argtypes = [CP56Time2a]
    CP56Time2a_getSecond.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 642
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_setSecond", "cdecl"):
    CP56Time2a_setSecond = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_setSecond", "cdecl")
    CP56Time2a_setSecond.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setSecond.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 645
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_getMinute", "cdecl"):
    CP56Time2a_getMinute = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_getMinute", "cdecl")
    CP56Time2a_getMinute.argtypes = [CP56Time2a]
    CP56Time2a_getMinute.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 648
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_setMinute", "cdecl"):
    CP56Time2a_setMinute = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_setMinute", "cdecl")
    CP56Time2a_setMinute.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setMinute.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 651
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_getHour", "cdecl"):
    CP56Time2a_getHour = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_getHour", "cdecl")
    CP56Time2a_getHour.argtypes = [CP56Time2a]
    CP56Time2a_getHour.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 654
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_setHour", "cdecl"):
    CP56Time2a_setHour = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_setHour", "cdecl")
    CP56Time2a_setHour.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setHour.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 657
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_getDayOfWeek", "cdecl"):
    CP56Time2a_getDayOfWeek = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_getDayOfWeek", "cdecl")
    CP56Time2a_getDayOfWeek.argtypes = [CP56Time2a]
    CP56Time2a_getDayOfWeek.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 660
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_setDayOfWeek", "cdecl"):
    CP56Time2a_setDayOfWeek = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_setDayOfWeek", "cdecl")
    CP56Time2a_setDayOfWeek.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setDayOfWeek.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 663
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_getDayOfMonth", "cdecl"):
    CP56Time2a_getDayOfMonth = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_getDayOfMonth", "cdecl")
    CP56Time2a_getDayOfMonth.argtypes = [CP56Time2a]
    CP56Time2a_getDayOfMonth.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 666
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_setDayOfMonth", "cdecl"):
    CP56Time2a_setDayOfMonth = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_setDayOfMonth", "cdecl")
    CP56Time2a_setDayOfMonth.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setDayOfMonth.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 674
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_getMonth", "cdecl"):
    CP56Time2a_getMonth = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_getMonth", "cdecl")
    CP56Time2a_getMonth.argtypes = [CP56Time2a]
    CP56Time2a_getMonth.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 682
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_setMonth", "cdecl"):
    CP56Time2a_setMonth = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_setMonth", "cdecl")
    CP56Time2a_setMonth.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setMonth.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 690
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_getYear", "cdecl"):
    CP56Time2a_getYear = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_getYear", "cdecl")
    CP56Time2a_getYear.argtypes = [CP56Time2a]
    CP56Time2a_getYear.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 698
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_setYear", "cdecl"):
    CP56Time2a_setYear = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_setYear", "cdecl")
    CP56Time2a_setYear.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setYear.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 701
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_isSummerTime", "cdecl"):
    CP56Time2a_isSummerTime = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_isSummerTime", "cdecl")
    CP56Time2a_isSummerTime.argtypes = [CP56Time2a]
    CP56Time2a_isSummerTime.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 704
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_setSummerTime", "cdecl"):
    CP56Time2a_setSummerTime = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_setSummerTime", "cdecl")
    CP56Time2a_setSummerTime.argtypes = [CP56Time2a, c_bool]
    CP56Time2a_setSummerTime.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 707
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_isInvalid", "cdecl"):
    CP56Time2a_isInvalid = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_isInvalid", "cdecl")
    CP56Time2a_isInvalid.argtypes = [CP56Time2a]
    CP56Time2a_isInvalid.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 710
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_setInvalid", "cdecl"):
    CP56Time2a_setInvalid = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_setInvalid", "cdecl")
    CP56Time2a_setInvalid.argtypes = [CP56Time2a, c_bool]
    CP56Time2a_setInvalid.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 713
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_isSubstituted", "cdecl"):
    CP56Time2a_isSubstituted = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_isSubstituted", "cdecl")
    CP56Time2a_isSubstituted.argtypes = [CP56Time2a]
    CP56Time2a_isSubstituted.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 716
if _libs["/usr/local/lib/lib60870.so"].has("CP56Time2a_setSubstituted", "cdecl"):
    CP56Time2a_setSubstituted = _libs["/usr/local/lib/lib60870.so"].get("CP56Time2a_setSubstituted", "cdecl")
    CP56Time2a_setSubstituted.argtypes = [CP56Time2a, c_bool]
    CP56Time2a_setSubstituted.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 719
if _libs["/usr/local/lib/lib60870.so"].has("BinaryCounterReading_create", "cdecl"):
    BinaryCounterReading_create = _libs["/usr/local/lib/lib60870.so"].get("BinaryCounterReading_create", "cdecl")
    BinaryCounterReading_create.argtypes = [BinaryCounterReading, c_int32, c_int, c_bool, c_bool, c_bool]
    BinaryCounterReading_create.restype = BinaryCounterReading

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 723
if _libs["/usr/local/lib/lib60870.so"].has("BinaryCounterReading_destroy", "cdecl"):
    BinaryCounterReading_destroy = _libs["/usr/local/lib/lib60870.so"].get("BinaryCounterReading_destroy", "cdecl")
    BinaryCounterReading_destroy.argtypes = [BinaryCounterReading]
    BinaryCounterReading_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 726
if _libs["/usr/local/lib/lib60870.so"].has("BinaryCounterReading_getValue", "cdecl"):
    BinaryCounterReading_getValue = _libs["/usr/local/lib/lib60870.so"].get("BinaryCounterReading_getValue", "cdecl")
    BinaryCounterReading_getValue.argtypes = [BinaryCounterReading]
    BinaryCounterReading_getValue.restype = c_int32

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 729
if _libs["/usr/local/lib/lib60870.so"].has("BinaryCounterReading_setValue", "cdecl"):
    BinaryCounterReading_setValue = _libs["/usr/local/lib/lib60870.so"].get("BinaryCounterReading_setValue", "cdecl")
    BinaryCounterReading_setValue.argtypes = [BinaryCounterReading, c_int32]
    BinaryCounterReading_setValue.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 732
if _libs["/usr/local/lib/lib60870.so"].has("BinaryCounterReading_getSequenceNumber", "cdecl"):
    BinaryCounterReading_getSequenceNumber = _libs["/usr/local/lib/lib60870.so"].get("BinaryCounterReading_getSequenceNumber", "cdecl")
    BinaryCounterReading_getSequenceNumber.argtypes = [BinaryCounterReading]
    BinaryCounterReading_getSequenceNumber.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 735
if _libs["/usr/local/lib/lib60870.so"].has("BinaryCounterReading_hasCarry", "cdecl"):
    BinaryCounterReading_hasCarry = _libs["/usr/local/lib/lib60870.so"].get("BinaryCounterReading_hasCarry", "cdecl")
    BinaryCounterReading_hasCarry.argtypes = [BinaryCounterReading]
    BinaryCounterReading_hasCarry.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 738
if _libs["/usr/local/lib/lib60870.so"].has("BinaryCounterReading_isAdjusted", "cdecl"):
    BinaryCounterReading_isAdjusted = _libs["/usr/local/lib/lib60870.so"].get("BinaryCounterReading_isAdjusted", "cdecl")
    BinaryCounterReading_isAdjusted.argtypes = [BinaryCounterReading]
    BinaryCounterReading_isAdjusted.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 741
if _libs["/usr/local/lib/lib60870.so"].has("BinaryCounterReading_isInvalid", "cdecl"):
    BinaryCounterReading_isInvalid = _libs["/usr/local/lib/lib60870.so"].get("BinaryCounterReading_isInvalid", "cdecl")
    BinaryCounterReading_isInvalid.argtypes = [BinaryCounterReading]
    BinaryCounterReading_isInvalid.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 744
if _libs["/usr/local/lib/lib60870.so"].has("BinaryCounterReading_setSequenceNumber", "cdecl"):
    BinaryCounterReading_setSequenceNumber = _libs["/usr/local/lib/lib60870.so"].get("BinaryCounterReading_setSequenceNumber", "cdecl")
    BinaryCounterReading_setSequenceNumber.argtypes = [BinaryCounterReading, c_int]
    BinaryCounterReading_setSequenceNumber.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 747
if _libs["/usr/local/lib/lib60870.so"].has("BinaryCounterReading_setCarry", "cdecl"):
    BinaryCounterReading_setCarry = _libs["/usr/local/lib/lib60870.so"].get("BinaryCounterReading_setCarry", "cdecl")
    BinaryCounterReading_setCarry.argtypes = [BinaryCounterReading, c_bool]
    BinaryCounterReading_setCarry.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 750
if _libs["/usr/local/lib/lib60870.so"].has("BinaryCounterReading_setAdjusted", "cdecl"):
    BinaryCounterReading_setAdjusted = _libs["/usr/local/lib/lib60870.so"].get("BinaryCounterReading_setAdjusted", "cdecl")
    BinaryCounterReading_setAdjusted.argtypes = [BinaryCounterReading, c_bool]
    BinaryCounterReading_setAdjusted.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 753
if _libs["/usr/local/lib/lib60870.so"].has("BinaryCounterReading_setInvalid", "cdecl"):
    BinaryCounterReading_setInvalid = _libs["/usr/local/lib/lib60870.so"].get("BinaryCounterReading_setInvalid", "cdecl")
    BinaryCounterReading_setInvalid.argtypes = [BinaryCounterReading, c_bool]
    BinaryCounterReading_setInvalid.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 759
class struct_sFrame(Structure):
    pass

Frame = POINTER(struct_sFrame)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 759

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 762
if _libs["/usr/local/lib/lib60870.so"].has("Frame_destroy", "cdecl"):
    Frame_destroy = _libs["/usr/local/lib/lib60870.so"].get("Frame_destroy", "cdecl")
    Frame_destroy.argtypes = [Frame]
    Frame_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 765
if _libs["/usr/local/lib/lib60870.so"].has("Frame_resetFrame", "cdecl"):
    Frame_resetFrame = _libs["/usr/local/lib/lib60870.so"].get("Frame_resetFrame", "cdecl")
    Frame_resetFrame.argtypes = [Frame]
    Frame_resetFrame.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 768
if _libs["/usr/local/lib/lib60870.so"].has("Frame_setNextByte", "cdecl"):
    Frame_setNextByte = _libs["/usr/local/lib/lib60870.so"].get("Frame_setNextByte", "cdecl")
    Frame_setNextByte.argtypes = [Frame, c_uint8]
    Frame_setNextByte.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 771
if _libs["/usr/local/lib/lib60870.so"].has("Frame_appendBytes", "cdecl"):
    Frame_appendBytes = _libs["/usr/local/lib/lib60870.so"].get("Frame_appendBytes", "cdecl")
    Frame_appendBytes.argtypes = [Frame, POINTER(c_uint8), c_int]
    Frame_appendBytes.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 774
if _libs["/usr/local/lib/lib60870.so"].has("Frame_getMsgSize", "cdecl"):
    Frame_getMsgSize = _libs["/usr/local/lib/lib60870.so"].get("Frame_getMsgSize", "cdecl")
    Frame_getMsgSize.argtypes = [Frame]
    Frame_getMsgSize.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 776
if _libs["/usr/local/lib/lib60870.so"].has("Frame_getBuffer", "cdecl"):
    Frame_getBuffer = _libs["/usr/local/lib/lib60870.so"].get("Frame_getBuffer", "cdecl")
    Frame_getBuffer.argtypes = [Frame]
    Frame_getBuffer.restype = POINTER(c_uint8)

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 780
if _libs["/usr/local/lib/lib60870.so"].has("Frame_getSpaceLeft", "cdecl"):
    Frame_getSpaceLeft = _libs["/usr/local/lib/lib60870.so"].get("Frame_getSpaceLeft", "cdecl")
    Frame_getSpaceLeft.argtypes = [Frame]
    Frame_getSpaceLeft.restype = c_int

# ./lib60870-C/src/hal/inc/tls_config.h: 37
class struct_sTLSConfiguration(Structure):
    pass

TLSConfiguration = POINTER(struct_sTLSConfiguration)# ./lib60870-C/src/hal/inc/tls_config.h: 37

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 65
class struct_sIMasterConnection(Structure):
    pass

IMasterConnection = POINTER(struct_sIMasterConnection)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 63

struct_sIMasterConnection.__slots__ = [
    'isReady',
    'sendASDU',
    'sendACT_CON',
    'sendACT_TERM',
    'close',
    'getPeerAddress',
    'getApplicationLayerParameters',
    'object',
]
struct_sIMasterConnection._fields_ = [
    ('isReady', CFUNCTYPE(UNCHECKED(c_bool), IMasterConnection)),
    ('sendASDU', CFUNCTYPE(UNCHECKED(c_bool), IMasterConnection, CS101_ASDU)),
    ('sendACT_CON', CFUNCTYPE(UNCHECKED(c_bool), IMasterConnection, CS101_ASDU, c_bool)),
    ('sendACT_TERM', CFUNCTYPE(UNCHECKED(c_bool), IMasterConnection, CS101_ASDU)),
    ('close', CFUNCTYPE(UNCHECKED(None), IMasterConnection)),
    ('getPeerAddress', CFUNCTYPE(UNCHECKED(c_int), IMasterConnection, String, c_int)),
    ('getApplicationLayerParameters', CFUNCTYPE(UNCHECKED(CS101_AppLayerParameters), IMasterConnection)),
    ('object', POINTER(None)),
]

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 90
if _libs["/usr/local/lib/lib60870.so"].has("IMasterConnection_isReady", "cdecl"):
    IMasterConnection_isReady = _libs["/usr/local/lib/lib60870.so"].get("IMasterConnection_isReady", "cdecl")
    IMasterConnection_isReady.argtypes = [IMasterConnection]
    IMasterConnection_isReady.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 103
if _libs["/usr/local/lib/lib60870.so"].has("IMasterConnection_sendASDU", "cdecl"):
    IMasterConnection_sendASDU = _libs["/usr/local/lib/lib60870.so"].get("IMasterConnection_sendASDU", "cdecl")
    IMasterConnection_sendASDU.argtypes = [IMasterConnection, CS101_ASDU]
    IMasterConnection_sendASDU.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 116
if _libs["/usr/local/lib/lib60870.so"].has("IMasterConnection_sendACT_CON", "cdecl"):
    IMasterConnection_sendACT_CON = _libs["/usr/local/lib/lib60870.so"].get("IMasterConnection_sendACT_CON", "cdecl")
    IMasterConnection_sendACT_CON.argtypes = [IMasterConnection, CS101_ASDU, c_bool]
    IMasterConnection_sendACT_CON.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 128
if _libs["/usr/local/lib/lib60870.so"].has("IMasterConnection_sendACT_TERM", "cdecl"):
    IMasterConnection_sendACT_TERM = _libs["/usr/local/lib/lib60870.so"].get("IMasterConnection_sendACT_TERM", "cdecl")
    IMasterConnection_sendACT_TERM.argtypes = [IMasterConnection, CS101_ASDU]
    IMasterConnection_sendACT_TERM.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 139
if _libs["/usr/local/lib/lib60870.so"].has("IMasterConnection_getPeerAddress", "cdecl"):
    IMasterConnection_getPeerAddress = _libs["/usr/local/lib/lib60870.so"].get("IMasterConnection_getPeerAddress", "cdecl")
    IMasterConnection_getPeerAddress.argtypes = [IMasterConnection, String, c_int]
    IMasterConnection_getPeerAddress.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 147
if _libs["/usr/local/lib/lib60870.so"].has("IMasterConnection_close", "cdecl"):
    IMasterConnection_close = _libs["/usr/local/lib/lib60870.so"].get("IMasterConnection_close", "cdecl")
    IMasterConnection_close.argtypes = [IMasterConnection]
    IMasterConnection_close.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 153
if _libs["/usr/local/lib/lib60870.so"].has("IMasterConnection_getApplicationLayerParameters", "cdecl"):
    IMasterConnection_getApplicationLayerParameters = _libs["/usr/local/lib/lib60870.so"].get("IMasterConnection_getApplicationLayerParameters", "cdecl")
    IMasterConnection_getApplicationLayerParameters.argtypes = [IMasterConnection]
    IMasterConnection_getApplicationLayerParameters.restype = CS101_AppLayerParameters

enum_anon_32 = c_int# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 171

CS101_PLUGIN_RESULT_NOT_HANDLED = 0# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 171

CS101_PLUGIN_RESULT_HANDLED = 1# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 171

CS101_PLUGIN_RESULT_INVALID_ASDU = 2# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 171

CS101_SlavePlugin_Result = enum_anon_32# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 171

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 178
class struct_sCS101_SlavePlugin(Structure):
    pass

CS101_SlavePlugin = POINTER(struct_sCS101_SlavePlugin)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 176

struct_sCS101_SlavePlugin.__slots__ = [
    'handleAsdu',
    'runTask',
    'parameter',
]
struct_sCS101_SlavePlugin._fields_ = [
    ('handleAsdu', CFUNCTYPE(UNCHECKED(CS101_SlavePlugin_Result), POINTER(None), IMasterConnection, CS101_ASDU)),
    ('runTask', CFUNCTYPE(UNCHECKED(None), POINTER(None), IMasterConnection)),
    ('parameter', POINTER(None)),
]

CS101_ResetCUHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None))# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 203

CS101_InterrogationHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, c_uint8)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 208

CS101_CounterInterrogationHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, QualifierOfCIC)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 213

CS101_ReadHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, c_int)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 218

CS101_ClockSynchronizationHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, CP56Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 233

CS101_ResetProcessHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, c_uint8)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 238

CS101_DelayAcquisitionHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, CP16Time2a)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 243

CS101_ASDUHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 248

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 50
class struct_sCS104_Slave(Structure):
    pass

CS104_Slave = POINTER(struct_sCS104_Slave)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 50

enum_anon_33 = c_int# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 56

CS104_MODE_SINGLE_REDUNDANCY_GROUP = 0# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 56

CS104_MODE_CONNECTION_IS_REDUNDANCY_GROUP = (CS104_MODE_SINGLE_REDUNDANCY_GROUP + 1)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 56

CS104_MODE_MULTIPLE_REDUNDANCY_GROUPS = (CS104_MODE_CONNECTION_IS_REDUNDANCY_GROUP + 1)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 56

CS104_ServerMode = enum_anon_33# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 56

enum_anon_34 = c_int# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 62

IP_ADDRESS_TYPE_IPV4 = 0# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 62

IP_ADDRESS_TYPE_IPV6 = (IP_ADDRESS_TYPE_IPV4 + 1)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 62

eCS104_IPAddressType = enum_anon_34# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 62

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 64
class struct_sCS104_RedundancyGroup(Structure):
    pass

CS104_RedundancyGroup = POINTER(struct_sCS104_RedundancyGroup)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 64

CS104_ConnectionRequestHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), c_char_p)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 74

enum_anon_35 = c_int# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 81

CS104_CON_EVENT_CONNECTION_OPENED = 0# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 81

CS104_CON_EVENT_CONNECTION_CLOSED = 1# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 81

CS104_CON_EVENT_ACTIVATED = 2# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 81

CS104_CON_EVENT_DEACTIVATED = 3# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 81

CS104_PeerConnectionEvent = enum_anon_35# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 81

CS104_ConnectionEventHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), IMasterConnection, CS104_PeerConnectionEvent)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 91

CS104_SlaveRawMessageHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), IMasterConnection, POINTER(c_uint8), c_int, c_bool)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 106

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 118
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_create", "cdecl"):
    CS104_Slave_create = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_create", "cdecl")
    CS104_Slave_create.argtypes = [c_int, c_int]
    CS104_Slave_create.restype = CS104_Slave

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 130
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_createSecure", "cdecl"):
        continue
    CS104_Slave_createSecure = _lib.get("CS104_Slave_createSecure", "cdecl")
    CS104_Slave_createSecure.argtypes = [c_int, c_int, TLSConfiguration]
    CS104_Slave_createSecure.restype = CS104_Slave
    break

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 133
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_addPlugin", "cdecl"):
    CS104_Slave_addPlugin = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_addPlugin", "cdecl")
    CS104_Slave_addPlugin.argtypes = [CS104_Slave, CS101_SlavePlugin]
    CS104_Slave_addPlugin.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 143
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_setLocalAddress", "cdecl"):
    CS104_Slave_setLocalAddress = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_setLocalAddress", "cdecl")
    CS104_Slave_setLocalAddress.argtypes = [CS104_Slave, String]
    CS104_Slave_setLocalAddress.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 152
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_setLocalPort", "cdecl"):
    CS104_Slave_setLocalPort = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_setLocalPort", "cdecl")
    CS104_Slave_setLocalPort.argtypes = [CS104_Slave, c_int]
    CS104_Slave_setLocalPort.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 160
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_getOpenConnections", "cdecl"):
    CS104_Slave_getOpenConnections = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_getOpenConnections", "cdecl")
    CS104_Slave_getOpenConnections.argtypes = [CS104_Slave]
    CS104_Slave_getOpenConnections.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 171
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_setMaxOpenConnections", "cdecl"):
    CS104_Slave_setMaxOpenConnections = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_setMaxOpenConnections", "cdecl")
    CS104_Slave_setMaxOpenConnections.argtypes = [CS104_Slave, c_int]
    CS104_Slave_setMaxOpenConnections.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 180
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_setServerMode", "cdecl"):
    CS104_Slave_setServerMode = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_setServerMode", "cdecl")
    CS104_Slave_setServerMode.argtypes = [CS104_Slave, CS104_ServerMode]
    CS104_Slave_setServerMode.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 194
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_setConnectionRequestHandler", "cdecl"):
    CS104_Slave_setConnectionRequestHandler = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_setConnectionRequestHandler", "cdecl")
    CS104_Slave_setConnectionRequestHandler.argtypes = [CS104_Slave, CS104_ConnectionRequestHandler, POINTER(None)]
    CS104_Slave_setConnectionRequestHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 207
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_setConnectionEventHandler", "cdecl"):
    CS104_Slave_setConnectionEventHandler = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_setConnectionEventHandler", "cdecl")
    CS104_Slave_setConnectionEventHandler.argtypes = [CS104_Slave, CS104_ConnectionEventHandler, POINTER(None)]
    CS104_Slave_setConnectionEventHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 210
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_setInterrogationHandler", "cdecl"):
    CS104_Slave_setInterrogationHandler = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_setInterrogationHandler", "cdecl")
    CS104_Slave_setInterrogationHandler.argtypes = [CS104_Slave, CS101_InterrogationHandler, POINTER(None)]
    CS104_Slave_setInterrogationHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 213
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_setCounterInterrogationHandler", "cdecl"):
    CS104_Slave_setCounterInterrogationHandler = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_setCounterInterrogationHandler", "cdecl")
    CS104_Slave_setCounterInterrogationHandler.argtypes = [CS104_Slave, CS101_CounterInterrogationHandler, POINTER(None)]
    CS104_Slave_setCounterInterrogationHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 219
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_setReadHandler", "cdecl"):
    CS104_Slave_setReadHandler = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_setReadHandler", "cdecl")
    CS104_Slave_setReadHandler.argtypes = [CS104_Slave, CS101_ReadHandler, POINTER(None)]
    CS104_Slave_setReadHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 222
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_setASDUHandler", "cdecl"):
    CS104_Slave_setASDUHandler = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_setASDUHandler", "cdecl")
    CS104_Slave_setASDUHandler.argtypes = [CS104_Slave, CS101_ASDUHandler, POINTER(None)]
    CS104_Slave_setASDUHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 225
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_setClockSyncHandler", "cdecl"):
    CS104_Slave_setClockSyncHandler = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_setClockSyncHandler", "cdecl")
    CS104_Slave_setClockSyncHandler.argtypes = [CS104_Slave, CS101_ClockSynchronizationHandler, POINTER(None)]
    CS104_Slave_setClockSyncHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 234
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_setRawMessageHandler", "cdecl"):
    CS104_Slave_setRawMessageHandler = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_setRawMessageHandler", "cdecl")
    CS104_Slave_setRawMessageHandler.argtypes = [CS104_Slave, CS104_SlaveRawMessageHandler, POINTER(None)]
    CS104_Slave_setRawMessageHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 240
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_getConnectionParameters", "cdecl"):
    CS104_Slave_getConnectionParameters = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_getConnectionParameters", "cdecl")
    CS104_Slave_getConnectionParameters.argtypes = [CS104_Slave]
    CS104_Slave_getConnectionParameters.restype = CS104_APCIParameters

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 246
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_getAppLayerParameters", "cdecl"):
    CS104_Slave_getAppLayerParameters = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_getAppLayerParameters", "cdecl")
    CS104_Slave_getAppLayerParameters.argtypes = [CS104_Slave]
    CS104_Slave_getAppLayerParameters.restype = CS101_AppLayerParameters

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 257
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_start", "cdecl"):
    CS104_Slave_start = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_start", "cdecl")
    CS104_Slave_start.argtypes = [CS104_Slave]
    CS104_Slave_start.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 267
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_isRunning", "cdecl"):
    CS104_Slave_isRunning = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_isRunning", "cdecl")
    CS104_Slave_isRunning.argtypes = [CS104_Slave]
    CS104_Slave_isRunning.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 276
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_stop", "cdecl"):
    CS104_Slave_stop = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_stop", "cdecl")
    CS104_Slave_stop.argtypes = [CS104_Slave]
    CS104_Slave_stop.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 286
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_startThreadless", "cdecl"):
    CS104_Slave_startThreadless = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_startThreadless", "cdecl")
    CS104_Slave_startThreadless.argtypes = [CS104_Slave]
    CS104_Slave_startThreadless.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 295
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_stopThreadless", "cdecl"):
    CS104_Slave_stopThreadless = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_stopThreadless", "cdecl")
    CS104_Slave_stopThreadless.argtypes = [CS104_Slave]
    CS104_Slave_stopThreadless.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 306
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_tick", "cdecl"):
    CS104_Slave_tick = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_tick", "cdecl")
    CS104_Slave_tick.argtypes = [CS104_Slave]
    CS104_Slave_tick.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 318
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_getNumberOfQueueEntries", "cdecl"):
    CS104_Slave_getNumberOfQueueEntries = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_getNumberOfQueueEntries", "cdecl")
    CS104_Slave_getNumberOfQueueEntries.argtypes = [CS104_Slave, CS104_RedundancyGroup]
    CS104_Slave_getNumberOfQueueEntries.restype = c_int

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 326
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_enqueueASDU", "cdecl"):
    CS104_Slave_enqueueASDU = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_enqueueASDU", "cdecl")
    CS104_Slave_enqueueASDU.argtypes = [CS104_Slave, CS101_ASDU]
    CS104_Slave_enqueueASDU.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 339
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_addRedundancyGroup", "cdecl"):
    CS104_Slave_addRedundancyGroup = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_addRedundancyGroup", "cdecl")
    CS104_Slave_addRedundancyGroup.argtypes = [CS104_Slave, CS104_RedundancyGroup]
    CS104_Slave_addRedundancyGroup.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 345
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Slave_destroy", "cdecl"):
    CS104_Slave_destroy = _libs["/usr/local/lib/lib60870.so"].get("CS104_Slave_destroy", "cdecl")
    CS104_Slave_destroy.argtypes = [CS104_Slave]
    CS104_Slave_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 354
if _libs["/usr/local/lib/lib60870.so"].has("CS104_RedundancyGroup_create", "cdecl"):
    CS104_RedundancyGroup_create = _libs["/usr/local/lib/lib60870.so"].get("CS104_RedundancyGroup_create", "cdecl")
    CS104_RedundancyGroup_create.argtypes = [String]
    CS104_RedundancyGroup_create.restype = CS104_RedundancyGroup

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 362
if _libs["/usr/local/lib/lib60870.so"].has("CS104_RedundancyGroup_addAllowedClient", "cdecl"):
    CS104_RedundancyGroup_addAllowedClient = _libs["/usr/local/lib/lib60870.so"].get("CS104_RedundancyGroup_addAllowedClient", "cdecl")
    CS104_RedundancyGroup_addAllowedClient.argtypes = [CS104_RedundancyGroup, String]
    CS104_RedundancyGroup_addAllowedClient.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 371
if _libs["/usr/local/lib/lib60870.so"].has("CS104_RedundancyGroup_addAllowedClientEx", "cdecl"):
    CS104_RedundancyGroup_addAllowedClientEx = _libs["/usr/local/lib/lib60870.so"].get("CS104_RedundancyGroup_addAllowedClientEx", "cdecl")
    CS104_RedundancyGroup_addAllowedClientEx.argtypes = [CS104_RedundancyGroup, POINTER(c_uint8), eCS104_IPAddressType]
    CS104_RedundancyGroup_addAllowedClientEx.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 381
if _libs["/usr/local/lib/lib60870.so"].has("CS104_RedundancyGroup_destroy", "cdecl"):
    CS104_RedundancyGroup_destroy = _libs["/usr/local/lib/lib60870.so"].get("CS104_RedundancyGroup_destroy", "cdecl")
    CS104_RedundancyGroup_destroy.argtypes = [CS104_RedundancyGroup]
    CS104_RedundancyGroup_destroy.restype = None

CS101_ASDUReceivedHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), c_int, CS101_ASDU)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_master.h: 53

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 52
class struct_sCS104_Connection(Structure):
    pass

CS104_Connection = POINTER(struct_sCS104_Connection)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 52

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 63
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_create", "cdecl"):
    CS104_Connection_create = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_create", "cdecl")
    CS104_Connection_create.argtypes = [String, c_int]
    CS104_Connection_create.restype = CS104_Connection

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 75
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_createSecure", "cdecl"):
        continue
    CS104_Connection_createSecure = _lib.get("CS104_Connection_createSecure", "cdecl")
    CS104_Connection_createSecure.argtypes = [String, c_int, TLSConfiguration]
    CS104_Connection_createSecure.restype = CS104_Connection
    break

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 88
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_setLocalAddress", "cdecl"):
    CS104_Connection_setLocalAddress = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_setLocalAddress", "cdecl")
    CS104_Connection_setLocalAddress.argtypes = [CS104_Connection, String, c_int]
    CS104_Connection_setLocalAddress.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 100
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_setAPCIParameters", "cdecl"):
    CS104_Connection_setAPCIParameters = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_setAPCIParameters", "cdecl")
    CS104_Connection_setAPCIParameters.argtypes = [CS104_Connection, CS104_APCIParameters]
    CS104_Connection_setAPCIParameters.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 106
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_getAPCIParameters", "cdecl"):
    CS104_Connection_getAPCIParameters = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_getAPCIParameters", "cdecl")
    CS104_Connection_getAPCIParameters.argtypes = [CS104_Connection]
    CS104_Connection_getAPCIParameters.restype = CS104_APCIParameters

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 119
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_setAppLayerParameters", "cdecl"):
    CS104_Connection_setAppLayerParameters = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_setAppLayerParameters", "cdecl")
    CS104_Connection_setAppLayerParameters.argtypes = [CS104_Connection, CS101_AppLayerParameters]
    CS104_Connection_setAppLayerParameters.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 131
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_getAppLayerParameters", "cdecl"):
    CS104_Connection_getAppLayerParameters = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_getAppLayerParameters", "cdecl")
    CS104_Connection_getAppLayerParameters.argtypes = [CS104_Connection]
    CS104_Connection_getAppLayerParameters.restype = CS101_AppLayerParameters

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 140
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_setConnectTimeout", "cdecl"):
    CS104_Connection_setConnectTimeout = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_setConnectTimeout", "cdecl")
    CS104_Connection_setConnectTimeout.argtypes = [CS104_Connection, c_int]
    CS104_Connection_setConnectTimeout.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 150
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_connectAsync", "cdecl"):
    CS104_Connection_connectAsync = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_connectAsync", "cdecl")
    CS104_Connection_connectAsync.argtypes = [CS104_Connection]
    CS104_Connection_connectAsync.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 162
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_connect", "cdecl"):
    CS104_Connection_connect = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_connect", "cdecl")
    CS104_Connection_connect.argtypes = [CS104_Connection]
    CS104_Connection_connect.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 171
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_sendStartDT", "cdecl"):
    CS104_Connection_sendStartDT = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_sendStartDT", "cdecl")
    CS104_Connection_sendStartDT.argtypes = [CS104_Connection]
    CS104_Connection_sendStartDT.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 177
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_sendStopDT", "cdecl"):
    CS104_Connection_sendStopDT = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_sendStopDT", "cdecl")
    CS104_Connection_sendStopDT.argtypes = [CS104_Connection]
    CS104_Connection_sendStopDT.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 187
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_isTransmitBufferFull", "cdecl"):
    CS104_Connection_isTransmitBufferFull = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_isTransmitBufferFull", "cdecl")
    CS104_Connection_isTransmitBufferFull.argtypes = [CS104_Connection]
    CS104_Connection_isTransmitBufferFull.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 199
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_sendInterrogationCommand", "cdecl"):
    CS104_Connection_sendInterrogationCommand = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_sendInterrogationCommand", "cdecl")
    CS104_Connection_sendInterrogationCommand.argtypes = [CS104_Connection, CS101_CauseOfTransmission, c_int, QualifierOfInterrogation]
    CS104_Connection_sendInterrogationCommand.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 211
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_sendCounterInterrogationCommand", "cdecl"):
    CS104_Connection_sendCounterInterrogationCommand = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_sendCounterInterrogationCommand", "cdecl")
    CS104_Connection_sendCounterInterrogationCommand.argtypes = [CS104_Connection, CS101_CauseOfTransmission, c_int, c_uint8]
    CS104_Connection_sendCounterInterrogationCommand.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 225
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_sendReadCommand", "cdecl"):
    CS104_Connection_sendReadCommand = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_sendReadCommand", "cdecl")
    CS104_Connection_sendReadCommand.argtypes = [CS104_Connection, c_int, c_int]
    CS104_Connection_sendReadCommand.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 236
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_sendClockSyncCommand", "cdecl"):
    CS104_Connection_sendClockSyncCommand = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_sendClockSyncCommand", "cdecl")
    CS104_Connection_sendClockSyncCommand.argtypes = [CS104_Connection, c_int, CP56Time2a]
    CS104_Connection_sendClockSyncCommand.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 248
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_sendTestCommand", "cdecl"):
    CS104_Connection_sendTestCommand = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_sendTestCommand", "cdecl")
    CS104_Connection_sendTestCommand.argtypes = [CS104_Connection, c_int]
    CS104_Connection_sendTestCommand.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 260
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_sendTestCommandWithTimestamp", "cdecl"):
    CS104_Connection_sendTestCommandWithTimestamp = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_sendTestCommandWithTimestamp", "cdecl")
    CS104_Connection_sendTestCommandWithTimestamp.argtypes = [CS104_Connection, c_int, c_uint16, CP56Time2a]
    CS104_Connection_sendTestCommandWithTimestamp.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 275
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_sendProcessCommand", "cdecl"):
    CS104_Connection_sendProcessCommand = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_sendProcessCommand", "cdecl")
    CS104_Connection_sendProcessCommand.argtypes = [CS104_Connection, TypeID, CS101_CauseOfTransmission, c_int, InformationObject]
    CS104_Connection_sendProcessCommand.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 288
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_sendProcessCommandEx", "cdecl"):
    CS104_Connection_sendProcessCommandEx = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_sendProcessCommandEx", "cdecl")
    CS104_Connection_sendProcessCommandEx.argtypes = [CS104_Connection, CS101_CauseOfTransmission, c_int, InformationObject]
    CS104_Connection_sendProcessCommandEx.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 299
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_sendASDU", "cdecl"):
    CS104_Connection_sendASDU = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_sendASDU", "cdecl")
    CS104_Connection_sendASDU.argtypes = [CS104_Connection, CS101_ASDU]
    CS104_Connection_sendASDU.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 308
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_setASDUReceivedHandler", "cdecl"):
    CS104_Connection_setASDUReceivedHandler = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_setASDUReceivedHandler", "cdecl")
    CS104_Connection_setASDUReceivedHandler.argtypes = [CS104_Connection, CS101_ASDUReceivedHandler, POINTER(None)]
    CS104_Connection_setASDUReceivedHandler.restype = None

enum_anon_36 = c_int# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 316

CS104_CONNECTION_OPENED = 0# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 316

CS104_CONNECTION_CLOSED = 1# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 316

CS104_CONNECTION_STARTDT_CON_RECEIVED = 2# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 316

CS104_CONNECTION_STOPDT_CON_RECEIVED = 3# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 316

CS104_ConnectionEvent = enum_anon_36# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 316

CS104_ConnectionHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), CS104_Connection, CS104_ConnectionEvent)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 325

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 334
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_setConnectionHandler", "cdecl"):
    CS104_Connection_setConnectionHandler = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_setConnectionHandler", "cdecl")
    CS104_Connection_setConnectionHandler.argtypes = [CS104_Connection, CS104_ConnectionHandler, POINTER(None)]
    CS104_Connection_setConnectionHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 344
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_setRawMessageHandler", "cdecl"):
    CS104_Connection_setRawMessageHandler = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_setRawMessageHandler", "cdecl")
    CS104_Connection_setRawMessageHandler.argtypes = [CS104_Connection, IEC60870_RawMessageHandler, POINTER(None)]
    CS104_Connection_setRawMessageHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 350
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_close", "cdecl"):
    CS104_Connection_close = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_close", "cdecl")
    CS104_Connection_close.argtypes = [CS104_Connection]
    CS104_Connection_close.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 356
if _libs["/usr/local/lib/lib60870.so"].has("CS104_Connection_destroy", "cdecl"):
    CS104_Connection_destroy = _libs["/usr/local/lib/lib60870.so"].get("CS104_Connection_destroy", "cdecl")
    CS104_Connection_destroy.argtypes = [CS104_Connection]
    CS104_Connection_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/link_layer_parameters.h: 42
class struct_sLinkLayerParameters(Structure):
    pass

LinkLayerParameters = POINTER(struct_sLinkLayerParameters)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/link_layer_parameters.h: 40

struct_sLinkLayerParameters.__slots__ = [
    'addressLength',
    'timeoutForAck',
    'timeoutRepeat',
    'useSingleCharACK',
]
struct_sLinkLayerParameters._fields_ = [
    ('addressLength', c_int),
    ('timeoutForAck', c_int),
    ('timeoutRepeat', c_int),
    ('useSingleCharACK', c_bool),
]

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 55
class struct_sCS101_Master(Structure):
    pass

CS101_Master = POINTER(struct_sCS101_Master)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 55

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 68
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_create", "cdecl"):
    CS101_Master_create = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_create", "cdecl")
    CS101_Master_create.argtypes = [SerialPort, LinkLayerParameters, CS101_AppLayerParameters, IEC60870_LinkLayerMode]
    CS101_Master_create.restype = CS101_Master

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 82
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_createEx", "cdecl"):
    CS101_Master_createEx = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_createEx", "cdecl")
    CS101_Master_createEx.argtypes = [SerialPort, LinkLayerParameters, CS101_AppLayerParameters, IEC60870_LinkLayerMode, c_int]
    CS101_Master_createEx.restype = CS101_Master

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 92
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_run", "cdecl"):
    CS101_Master_run = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_run", "cdecl")
    CS101_Master_run.argtypes = [CS101_Master]
    CS101_Master_run.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 104
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_start", "cdecl"):
    CS101_Master_start = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_start", "cdecl")
    CS101_Master_start.argtypes = [CS101_Master]
    CS101_Master_start.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 112
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_stop", "cdecl"):
    CS101_Master_stop = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_stop", "cdecl")
    CS101_Master_stop.argtypes = [CS101_Master]
    CS101_Master_stop.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 124
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_addSlave", "cdecl"):
    CS101_Master_addSlave = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_addSlave", "cdecl")
    CS101_Master_addSlave.argtypes = [CS101_Master, c_int]
    CS101_Master_addSlave.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 138
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_pollSingleSlave", "cdecl"):
    CS101_Master_pollSingleSlave = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_pollSingleSlave", "cdecl")
    CS101_Master_pollSingleSlave.argtypes = [CS101_Master, c_int]
    CS101_Master_pollSingleSlave.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 144
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_destroy", "cdecl"):
    CS101_Master_destroy = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_destroy", "cdecl")
    CS101_Master_destroy.argtypes = [CS101_Master]
    CS101_Master_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 155
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_setDIR", "cdecl"):
    CS101_Master_setDIR = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_setDIR", "cdecl")
    CS101_Master_setDIR.argtypes = [CS101_Master, c_bool]
    CS101_Master_setDIR.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 163
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_setOwnAddress", "cdecl"):
    CS101_Master_setOwnAddress = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_setOwnAddress", "cdecl")
    CS101_Master_setOwnAddress.argtypes = [CS101_Master, c_int]
    CS101_Master_setOwnAddress.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 175
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_useSlaveAddress", "cdecl"):
    CS101_Master_useSlaveAddress = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_useSlaveAddress", "cdecl")
    CS101_Master_useSlaveAddress.argtypes = [CS101_Master, c_int]
    CS101_Master_useSlaveAddress.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 185
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_getAppLayerParameters", "cdecl"):
    CS101_Master_getAppLayerParameters = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_getAppLayerParameters", "cdecl")
    CS101_Master_getAppLayerParameters.argtypes = [CS101_Master]
    CS101_Master_getAppLayerParameters.restype = CS101_AppLayerParameters

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 193
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_getLinkLayerParameters", "cdecl"):
    CS101_Master_getLinkLayerParameters = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_getLinkLayerParameters", "cdecl")
    CS101_Master_getLinkLayerParameters.argtypes = [CS101_Master]
    CS101_Master_getLinkLayerParameters.restype = LinkLayerParameters

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 206
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_isChannelReady", "cdecl"):
    CS101_Master_isChannelReady = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_isChannelReady", "cdecl")
    CS101_Master_isChannelReady.argtypes = [CS101_Master, c_int]
    CS101_Master_isChannelReady.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 215
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_sendLinkLayerTestFunction", "cdecl"):
    CS101_Master_sendLinkLayerTestFunction = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_sendLinkLayerTestFunction", "cdecl")
    CS101_Master_sendLinkLayerTestFunction.argtypes = [CS101_Master]
    CS101_Master_sendLinkLayerTestFunction.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 225
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_sendInterrogationCommand", "cdecl"):
    CS101_Master_sendInterrogationCommand = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_sendInterrogationCommand", "cdecl")
    CS101_Master_sendInterrogationCommand.argtypes = [CS101_Master, CS101_CauseOfTransmission, c_int, QualifierOfInterrogation]
    CS101_Master_sendInterrogationCommand.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 235
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_sendCounterInterrogationCommand", "cdecl"):
    CS101_Master_sendCounterInterrogationCommand = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_sendCounterInterrogationCommand", "cdecl")
    CS101_Master_sendCounterInterrogationCommand.argtypes = [CS101_Master, CS101_CauseOfTransmission, c_int, c_uint8]
    CS101_Master_sendCounterInterrogationCommand.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 247
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_sendReadCommand", "cdecl"):
    CS101_Master_sendReadCommand = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_sendReadCommand", "cdecl")
    CS101_Master_sendReadCommand.argtypes = [CS101_Master, c_int, c_int]
    CS101_Master_sendReadCommand.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 256
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_sendClockSyncCommand", "cdecl"):
    CS101_Master_sendClockSyncCommand = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_sendClockSyncCommand", "cdecl")
    CS101_Master_sendClockSyncCommand.argtypes = [CS101_Master, c_int, CP56Time2a]
    CS101_Master_sendClockSyncCommand.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 266
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_sendTestCommand", "cdecl"):
    CS101_Master_sendTestCommand = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_sendTestCommand", "cdecl")
    CS101_Master_sendTestCommand.argtypes = [CS101_Master, c_int]
    CS101_Master_sendTestCommand.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 277
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_sendProcessCommand", "cdecl"):
    CS101_Master_sendProcessCommand = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_sendProcessCommand", "cdecl")
    CS101_Master_sendProcessCommand.argtypes = [CS101_Master, CS101_CauseOfTransmission, c_int, InformationObject]
    CS101_Master_sendProcessCommand.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 293
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_sendASDU", "cdecl"):
    CS101_Master_sendASDU = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_sendASDU", "cdecl")
    CS101_Master_sendASDU.argtypes = [CS101_Master, CS101_ASDU]
    CS101_Master_sendASDU.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 302
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_setASDUReceivedHandler", "cdecl"):
    CS101_Master_setASDUReceivedHandler = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_setASDUReceivedHandler", "cdecl")
    CS101_Master_setASDUReceivedHandler.argtypes = [CS101_Master, CS101_ASDUReceivedHandler, POINTER(None)]
    CS101_Master_setASDUReceivedHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 308
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_setLinkLayerStateChanged", "cdecl"):
    CS101_Master_setLinkLayerStateChanged = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_setLinkLayerStateChanged", "cdecl")
    CS101_Master_setLinkLayerStateChanged.argtypes = [CS101_Master, IEC60870_LinkLayerStateChangedHandler, POINTER(None)]
    CS101_Master_setLinkLayerStateChanged.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 317
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_setRawMessageHandler", "cdecl"):
    CS101_Master_setRawMessageHandler = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_setRawMessageHandler", "cdecl")
    CS101_Master_setRawMessageHandler.argtypes = [CS101_Master, IEC60870_RawMessageHandler, POINTER(None)]
    CS101_Master_setRawMessageHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 328
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Master_setIdleTimeout", "cdecl"):
    CS101_Master_setIdleTimeout = _libs["/usr/local/lib/lib60870.so"].get("CS101_Master_setIdleTimeout", "cdecl")
    CS101_Master_setIdleTimeout.argtypes = [CS101_Master, c_int]
    CS101_Master_setIdleTimeout.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 59
class struct_sCS101_Slave(Structure):
    pass

CS101_Slave = POINTER(struct_sCS101_Slave)# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 59

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 75
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_create", "cdecl"):
    CS101_Slave_create = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_create", "cdecl")
    CS101_Slave_create.argtypes = [SerialPort, LinkLayerParameters, CS101_AppLayerParameters, IEC60870_LinkLayerMode]
    CS101_Slave_create.restype = CS101_Slave

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 92
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_createEx", "cdecl"):
    CS101_Slave_createEx = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_createEx", "cdecl")
    CS101_Slave_createEx.argtypes = [SerialPort, LinkLayerParameters, CS101_AppLayerParameters, IEC60870_LinkLayerMode, c_int, c_int]
    CS101_Slave_createEx.restype = CS101_Slave

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 101
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_destroy", "cdecl"):
    CS101_Slave_destroy = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_destroy", "cdecl")
    CS101_Slave_destroy.argtypes = [CS101_Slave]
    CS101_Slave_destroy.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 112
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_setDIR", "cdecl"):
    CS101_Slave_setDIR = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_setDIR", "cdecl")
    CS101_Slave_setDIR.argtypes = [CS101_Slave, c_bool]
    CS101_Slave_setDIR.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 120
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_addPlugin", "cdecl"):
    CS101_Slave_addPlugin = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_addPlugin", "cdecl")
    CS101_Slave_addPlugin.argtypes = [CS101_Slave, CS101_SlavePlugin]
    CS101_Slave_addPlugin.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 131
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_setIdleTimeout", "cdecl"):
    CS101_Slave_setIdleTimeout = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_setIdleTimeout", "cdecl")
    CS101_Slave_setIdleTimeout.argtypes = [CS101_Slave, c_int]
    CS101_Slave_setIdleTimeout.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 137
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_setLinkLayerStateChanged", "cdecl"):
    CS101_Slave_setLinkLayerStateChanged = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_setLinkLayerStateChanged", "cdecl")
    CS101_Slave_setLinkLayerStateChanged.argtypes = [CS101_Slave, IEC60870_LinkLayerStateChangedHandler, POINTER(None)]
    CS101_Slave_setLinkLayerStateChanged.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 147
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_setLinkLayerAddress", "cdecl"):
    CS101_Slave_setLinkLayerAddress = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_setLinkLayerAddress", "cdecl")
    CS101_Slave_setLinkLayerAddress.argtypes = [CS101_Slave, c_int]
    CS101_Slave_setLinkLayerAddress.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 156
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_setLinkLayerAddressOtherStation", "cdecl"):
    CS101_Slave_setLinkLayerAddressOtherStation = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_setLinkLayerAddressOtherStation", "cdecl")
    CS101_Slave_setLinkLayerAddressOtherStation.argtypes = [CS101_Slave, c_int]
    CS101_Slave_setLinkLayerAddressOtherStation.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 166
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_isClass1QueueFull", "cdecl"):
    CS101_Slave_isClass1QueueFull = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_isClass1QueueFull", "cdecl")
    CS101_Slave_isClass1QueueFull.argtypes = [CS101_Slave]
    CS101_Slave_isClass1QueueFull.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 175
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_enqueueUserDataClass1", "cdecl"):
    CS101_Slave_enqueueUserDataClass1 = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_enqueueUserDataClass1", "cdecl")
    CS101_Slave_enqueueUserDataClass1.argtypes = [CS101_Slave, CS101_ASDU]
    CS101_Slave_enqueueUserDataClass1.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 185
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_isClass2QueueFull", "cdecl"):
    CS101_Slave_isClass2QueueFull = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_isClass2QueueFull", "cdecl")
    CS101_Slave_isClass2QueueFull.argtypes = [CS101_Slave]
    CS101_Slave_isClass2QueueFull.restype = c_bool

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 194
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_enqueueUserDataClass2", "cdecl"):
    CS101_Slave_enqueueUserDataClass2 = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_enqueueUserDataClass2", "cdecl")
    CS101_Slave_enqueueUserDataClass2.argtypes = [CS101_Slave, CS101_ASDU]
    CS101_Slave_enqueueUserDataClass2.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 202
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_flushQueues", "cdecl"):
    CS101_Slave_flushQueues = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_flushQueues", "cdecl")
    CS101_Slave_flushQueues.argtypes = [CS101_Slave]
    CS101_Slave_flushQueues.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 213
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_run", "cdecl"):
    CS101_Slave_run = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_run", "cdecl")
    CS101_Slave_run.argtypes = [CS101_Slave]
    CS101_Slave_run.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 225
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_start", "cdecl"):
    CS101_Slave_start = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_start", "cdecl")
    CS101_Slave_start.argtypes = [CS101_Slave]
    CS101_Slave_start.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 233
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_stop", "cdecl"):
    CS101_Slave_stop = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_stop", "cdecl")
    CS101_Slave_stop.argtypes = [CS101_Slave]
    CS101_Slave_stop.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 243
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_getAppLayerParameters", "cdecl"):
    CS101_Slave_getAppLayerParameters = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_getAppLayerParameters", "cdecl")
    CS101_Slave_getAppLayerParameters.argtypes = [CS101_Slave]
    CS101_Slave_getAppLayerParameters.restype = CS101_AppLayerParameters

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 253
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_getLinkLayerParameters", "cdecl"):
    CS101_Slave_getLinkLayerParameters = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_getLinkLayerParameters", "cdecl")
    CS101_Slave_getLinkLayerParameters.argtypes = [CS101_Slave]
    CS101_Slave_getLinkLayerParameters.restype = LinkLayerParameters

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 262
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_setResetCUHandler", "cdecl"):
    CS101_Slave_setResetCUHandler = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_setResetCUHandler", "cdecl")
    CS101_Slave_setResetCUHandler.argtypes = [CS101_Slave, CS101_ResetCUHandler, POINTER(None)]
    CS101_Slave_setResetCUHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 271
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_setInterrogationHandler", "cdecl"):
    CS101_Slave_setInterrogationHandler = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_setInterrogationHandler", "cdecl")
    CS101_Slave_setInterrogationHandler.argtypes = [CS101_Slave, CS101_InterrogationHandler, POINTER(None)]
    CS101_Slave_setInterrogationHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 280
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_setCounterInterrogationHandler", "cdecl"):
    CS101_Slave_setCounterInterrogationHandler = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_setCounterInterrogationHandler", "cdecl")
    CS101_Slave_setCounterInterrogationHandler.argtypes = [CS101_Slave, CS101_CounterInterrogationHandler, POINTER(None)]
    CS101_Slave_setCounterInterrogationHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 289
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_setReadHandler", "cdecl"):
    CS101_Slave_setReadHandler = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_setReadHandler", "cdecl")
    CS101_Slave_setReadHandler.argtypes = [CS101_Slave, CS101_ReadHandler, POINTER(None)]
    CS101_Slave_setReadHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 298
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_setClockSyncHandler", "cdecl"):
    CS101_Slave_setClockSyncHandler = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_setClockSyncHandler", "cdecl")
    CS101_Slave_setClockSyncHandler.argtypes = [CS101_Slave, CS101_ClockSynchronizationHandler, POINTER(None)]
    CS101_Slave_setClockSyncHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 307
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_setResetProcessHandler", "cdecl"):
    CS101_Slave_setResetProcessHandler = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_setResetProcessHandler", "cdecl")
    CS101_Slave_setResetProcessHandler.argtypes = [CS101_Slave, CS101_ResetProcessHandler, POINTER(None)]
    CS101_Slave_setResetProcessHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 316
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_setDelayAcquisitionHandler", "cdecl"):
    CS101_Slave_setDelayAcquisitionHandler = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_setDelayAcquisitionHandler", "cdecl")
    CS101_Slave_setDelayAcquisitionHandler.argtypes = [CS101_Slave, CS101_DelayAcquisitionHandler, POINTER(None)]
    CS101_Slave_setDelayAcquisitionHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 328
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_setASDUHandler", "cdecl"):
    CS101_Slave_setASDUHandler = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_setASDUHandler", "cdecl")
    CS101_Slave_setASDUHandler.argtypes = [CS101_Slave, CS101_ASDUHandler, POINTER(None)]
    CS101_Slave_setASDUHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 337
if _libs["/usr/local/lib/lib60870.so"].has("CS101_Slave_setRawMessageHandler", "cdecl"):
    CS101_Slave_setRawMessageHandler = _libs["/usr/local/lib/lib60870.so"].get("CS101_Slave_setRawMessageHandler", "cdecl")
    CS101_Slave_setRawMessageHandler.argtypes = [CS101_Slave, IEC60870_RawMessageHandler, POINTER(None)]
    CS101_Slave_setRawMessageHandler.restype = None

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 15
def CALLOC(nmemb, size):
    return (Memory_calloc (nmemb, size))

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 16
def MALLOC(size):
    return (Memory_malloc (size))

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 17
def REALLOC(oldptr, size):
    return (Memory_realloc (oldptr, size))

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 18
def FREEMEM(ptr):
    return (Memory_free (ptr))

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 20
def GLOBAL_CALLOC(nmemb, size):
    return (Memory_calloc (nmemb, size))

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 21
def GLOBAL_MALLOC(size):
    return (Memory_malloc (size))

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 22
def GLOBAL_REALLOC(oldptr, size):
    return (Memory_realloc (oldptr, size))

# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 23
def GLOBAL_FREEMEM(ptr):
    return (Memory_free (ptr))

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 45
try:
    IEC_60870_5_104_DEFAULT_PORT = 2404
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 46
try:
    IEC_60870_5_104_DEFAULT_TLS_PORT = 19998
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 48
try:
    LIB60870_VERSION_MAJOR = 2
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 49
try:
    LIB60870_VERSION_MINOR = 3
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 50
try:
    LIB60870_VERSION_PATCH = 1
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 140
try:
    IEC60870_QUALITY_GOOD = 0
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 141
try:
    IEC60870_QUALITY_OVERFLOW = 1
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 142
try:
    IEC60870_QUALITY_RESERVED = 4
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 143
try:
    IEC60870_QUALITY_ELAPSED_TIME_INVALID = 8
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 144
try:
    IEC60870_QUALITY_BLOCKED = 16
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 145
try:
    IEC60870_QUALITY_SUBSTITUTED = 32
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 146
try:
    IEC60870_QUALITY_NON_TOPICAL = 64
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 147
try:
    IEC60870_QUALITY_INVALID = 128
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 154
try:
    IEC60870_START_EVENT_NONE = 0
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 155
try:
    IEC60870_START_EVENT_GS = 1
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 156
try:
    IEC60870_START_EVENT_SL1 = 2
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 157
try:
    IEC60870_START_EVENT_SL2 = 4
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 158
try:
    IEC60870_START_EVENT_SL3 = 8
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 159
try:
    IEC60870_START_EVENT_SIE = 16
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 160
try:
    IEC60870_START_EVENT_SRD = 32
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 161
try:
    IEC60870_START_EVENT_RES1 = 64
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 162
try:
    IEC60870_START_EVENT_RES2 = 128
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 169
try:
    IEC60870_OUTPUT_CI_GC = 1
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 170
try:
    IEC60870_OUTPUT_CI_CL1 = 2
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 171
try:
    IEC60870_OUTPUT_CI_CL2 = 4
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 172
try:
    IEC60870_OUTPUT_CI_CL3 = 8
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 188
try:
    IEC60870_QPM_NOT_USED = 0
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 189
try:
    IEC60870_QPM_THRESHOLD_VALUE = 1
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 190
try:
    IEC60870_QPM_SMOOTHING_FACTOR = 2
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 191
try:
    IEC60870_QPM_LOW_LIMIT_FOR_TRANSMISSION = 3
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 192
try:
    IEC60870_QPM_HIGH_LIMIT_FOR_TRANSMISSION = 4
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 200
try:
    IEC60870_COI_LOCAL_SWITCH_ON = 0
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 201
try:
    IEC60870_COI_LOCAL_MANUAL_RESET = 1
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 202
try:
    IEC60870_COI_REMOTE_RESET = 2
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 209
try:
    IEC60870_QOC_NO_ADDITIONAL_DEFINITION = 0
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 210
try:
    IEC60870_QOC_SHORT_PULSE_DURATION = 1
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 211
try:
    IEC60870_QOC_LONG_PULSE_DURATION = 2
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 212
try:
    IEC60870_QOC_PERSISTANT_OUTPUT = 3
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 220
try:
    IEC60870_SCQ_DEFAULT = 0
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 221
try:
    IEC60870_SCQ_SELECT_FILE = 1
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 222
try:
    IEC60870_SCQ_REQUEST_FILE = 2
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 223
try:
    IEC60870_SCQ_DEACTIVATE_FILE = 3
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 224
try:
    IEC60870_SCQ_DELETE_FILE = 4
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 225
try:
    IEC60870_SCQ_SELECT_SECTION = 5
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 226
try:
    IEC60870_SCQ_REQUEST_SECTION = 6
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 227
try:
    IEC60870_SCQ_DEACTIVATE_SECTION = 7
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 235
try:
    IEC60870_QOI_STATION = 20
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 236
try:
    IEC60870_QOI_GROUP_1 = 21
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 237
try:
    IEC60870_QOI_GROUP_2 = 22
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 238
try:
    IEC60870_QOI_GROUP_3 = 23
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 239
try:
    IEC60870_QOI_GROUP_4 = 24
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 240
try:
    IEC60870_QOI_GROUP_5 = 25
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 241
try:
    IEC60870_QOI_GROUP_6 = 26
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 242
try:
    IEC60870_QOI_GROUP_7 = 27
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 243
try:
    IEC60870_QOI_GROUP_8 = 28
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 244
try:
    IEC60870_QOI_GROUP_9 = 29
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 245
try:
    IEC60870_QOI_GROUP_10 = 30
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 246
try:
    IEC60870_QOI_GROUP_11 = 31
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 247
try:
    IEC60870_QOI_GROUP_12 = 32
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 248
try:
    IEC60870_QOI_GROUP_13 = 33
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 249
try:
    IEC60870_QOI_GROUP_14 = 34
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 250
try:
    IEC60870_QOI_GROUP_15 = 35
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 251
try:
    IEC60870_QOI_GROUP_16 = 36
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 274
try:
    IEC60870_QCC_RQT_GROUP_1 = 1
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 275
try:
    IEC60870_QCC_RQT_GROUP_2 = 2
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 276
try:
    IEC60870_QCC_RQT_GROUP_3 = 3
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 277
try:
    IEC60870_QCC_RQT_GROUP_4 = 4
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 278
try:
    IEC60870_QCC_RQT_GENERAL = 5
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 280
try:
    IEC60870_QCC_FRZ_READ = 0
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 281
try:
    IEC60870_QCC_FRZ_FREEZE_WITHOUT_RESET = 64
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 282
try:
    IEC60870_QCC_FRZ_FREEZE_WITH_RESET = 128
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 283
try:
    IEC60870_QCC_FRZ_COUNTER_RESET = 192
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 290
try:
    IEC60870_QRP_NOT_USED = 0
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 291
try:
    IEC60870_QRP_GENERAL_RESET = 1
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 292
try:
    IEC60870_QRP_RESET_PENDING_INFO_WITH_TIME_TAG = 2
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 300
try:
    IEC60870_QPA_NOT_USED = 0
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 301
try:
    IEC60870_QPA_DE_ACT_PREV_LOADED_PARAMETER = 1
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 302
try:
    IEC60870_QPA_DE_ACT_OBJECT_PARAMETER = 2
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 303
try:
    IEC60870_QPA_DE_ACT_OBJECT_TRANSMISSION = 4
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1855
try:
    CS101_NOF_DEFAULT = 0
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1856
try:
    CS101_NOF_TRANSPARENT_FILE = 1
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1857
try:
    CS101_NOF_DISTURBANCE_DATA = 2
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1858
try:
    CS101_NOF_SEQUENCES_OF_EVENTS = 3
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1859
try:
    CS101_NOF_SEQUENCES_OF_ANALOGUE_VALUES = 4
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1871
try:
    CS101_SCQ_DEFAULT = 0
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1872
try:
    CS101_SCQ_SELECT_FILE = 1
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1873
try:
    CS101_SCQ_REQUEST_FILE = 2
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1874
try:
    CS101_SCQ_DEACTIVATE_FILE = 3
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1875
try:
    CS101_SCQ_DELETE_FILE = 4
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1876
try:
    CS101_SCQ_SELECT_SECTION = 5
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1877
try:
    CS101_SCQ_REQUEST_SECTION = 6
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1878
try:
    CS101_SCQ_DEACTIVATE_SECTION = 7
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1891
try:
    CS101_LSQ_FILE_TRANSFER_WITHOUT_DEACT = 1
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1892
try:
    CS101_LSQ_FILE_TRANSFER_WITH_DEACT = 2
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1893
try:
    CS101_LSQ_SECTION_TRANSFER_WITHOUT_DEACT = 3
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1894
try:
    CS101_LSQ_SECTION_TRANSFER_WITH_DEACT = 4
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1907
try:
    CS101_AFQ_NOT_USED = 0
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1910
try:
    CS101_AFQ_POS_ACK_FILE = 1
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1913
try:
    CS101_AFQ_NEG_ACK_FILE = 2
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1916
try:
    CS101_AFQ_POS_ACK_SECTION = 3
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1919
try:
    CS101_AFQ_NEG_ACK_SECTION = 4
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1932
try:
    CS101_FILE_ERROR_DEFAULT = 0
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1935
try:
    CS101_FILE_ERROR_REQ_MEMORY_NOT_AVAILABLE = 1
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1938
try:
    CS101_FILE_ERROR_CHECKSUM_FAILED = 2
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1941
try:
    CS101_FILE_ERROR_UNEXPECTED_COMM_SERVICE = 3
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1944
try:
    CS101_FILE_ERROR_UNEXPECTED_NAME_OF_FILE = 4
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1947
try:
    CS101_FILE_ERROR_UNEXPECTED_NAME_OF_SECTION = 5
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1960
try:
    CS101_SOF_STATUS = 31
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1963
try:
    CS101_SOF_LFD = 32
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1966
try:
    CS101_SOF_FOR = 64
except:
    pass

# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1969
try:
    CS101_SOF_FA = 128
except:
    pass

sSerialPort = struct_sSerialPort# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 39

sThread = struct_sThread# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 38

sServerSocket = struct_sServerSocket# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 44

sUdpSocket = struct_sUdpSocket# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 46

sSocket = struct_sSocket# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 49

sHandleSet = struct_sHandleSet# /home/user/Desktop/scada/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 52

sLinkedList = struct_sLinkedList# /home/user/Desktop/scada/lib60870/lib60870-C/src/common/inc/linked_list.h: 42

sCS101_AppLayerParameters = struct_sCS101_AppLayerParameters# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 112

sCS101_ASDU = struct_sCS101_ASDU# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 125

sCP16Time2a = struct_sCP16Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 140

sCP24Time2a = struct_sCP24Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 146

sCP32Time2a = struct_sCP32Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 155

sCP56Time2a = struct_sCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 164

sBinaryCounterReading = struct_sBinaryCounterReading# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 173

sCS104_APCIParameters = struct_sCS104_APCIParameters# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 182

sStatusAndStatusChangeDetection = struct_sStatusAndStatusChangeDetection# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 353

sInformationObject = struct_sInformationObject# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 377

sSinglePointInformation = struct_sSinglePointInformation# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 407

sSinglePointWithCP24Time2a = struct_sSinglePointWithCP24Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 426

sSinglePointWithCP56Time2a = struct_sSinglePointWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 442

sDoublePointInformation = struct_sDoublePointInformation# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 459

sDoublePointWithCP24Time2a = struct_sDoublePointWithCP24Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 478

sDoublePointWithCP56Time2a = struct_sDoublePointWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 494

sStepPositionInformation = struct_sStepPositionInformation# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 510

sStepPositionWithCP24Time2a = struct_sStepPositionWithCP24Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 549

sStepPositionWithCP56Time2a = struct_sStepPositionWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 566

sBitString32 = struct_sBitString32# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 582

sBitstring32WithCP24Time2a = struct_sBitstring32WithCP24Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 603

sBitstring32WithCP56Time2a = struct_sBitstring32WithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 621

sMeasuredValueNormalizedWithoutQuality = struct_sMeasuredValueNormalizedWithoutQuality# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 639

sMeasuredValueNormalized = struct_sMeasuredValueNormalized# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 657

sMeasuredValueNormalizedWithCP24Time2a = struct_sMeasuredValueNormalizedWithCP24Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 678

sMeasuredValueNormalizedWithCP56Time2a = struct_sMeasuredValueNormalizedWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 697

sMeasuredValueScaled = struct_sMeasuredValueScaled# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 717

sMeasuredValueScaledWithCP24Time2a = struct_sMeasuredValueScaledWithCP24Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 751

sMeasuredValueScaledWithCP56Time2a = struct_sMeasuredValueScaledWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 770

sMeasuredValueShort = struct_sMeasuredValueShort# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 789

sMeasuredValueShortWithCP24Time2a = struct_sMeasuredValueShortWithCP24Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 810

sMeasuredValueShortWithCP56Time2a = struct_sMeasuredValueShortWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 830

sIntegratedTotals = struct_sIntegratedTotals# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 850

sIntegratedTotalsWithCP24Time2a = struct_sIntegratedTotalsWithCP24Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 879

sIntegratedTotalsWithCP56Time2a = struct_sIntegratedTotalsWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 911

sEventOfProtectionEquipment = struct_sEventOfProtectionEquipment# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 943

sPackedStartEventsOfProtectionEquipment = struct_sPackedStartEventsOfProtectionEquipment# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 965

sPackedOutputCircuitInfo = struct_sPackedOutputCircuitInfo# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 990

sPackedSinglePointWithSCD = struct_sPackedSinglePointWithSCD# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1015

sSingleCommand = struct_sSingleCommand# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1035

sSingleCommandWithCP56Time2a = struct_sSingleCommandWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1080

sDoubleCommand = struct_sDoubleCommand# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1115

sStepCommand = struct_sStepCommand# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1162

sSetpointCommandNormalized = struct_sSetpointCommandNormalized# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1193

sSetpointCommandScaled = struct_sSetpointCommandScaled# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1230

sSetpointCommandShort = struct_sSetpointCommandShort# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1267

sBitstring32Command = struct_sBitstring32Command# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1304

sInterrogationCommand = struct_sInterrogationCommand# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1319

sReadCommand = struct_sReadCommand# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1334

sClockSynchronizationCommand = struct_sClockSynchronizationCommand# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1346

sParameterActivation = struct_sParameterActivation# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1505

sEventOfProtectionEquipmentWithCP56Time2a = struct_sEventOfProtectionEquipmentWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1534

sPackedStartEventsOfProtectionEquipmentWithCP56Time2a = struct_sPackedStartEventsOfProtectionEquipmentWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1556

sPackedOutputCircuitInfoWithCP56Time2a = struct_sPackedOutputCircuitInfoWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1581

sDoubleCommandWithCP56Time2a = struct_sDoubleCommandWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1606

sStepCommandWithCP56Time2a = struct_sStepCommandWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1630

sSetpointCommandNormalizedWithCP56Time2a = struct_sSetpointCommandNormalizedWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1654

sSetpointCommandScaledWithCP56Time2a = struct_sSetpointCommandScaledWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1678

sSetpointCommandShortWithCP56Time2a = struct_sSetpointCommandShortWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1702

sBitstring32CommandWithCP56Time2a = struct_sBitstring32CommandWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1726

sCounterInterrogationCommand = struct_sCounterInterrogationCommand# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1745

sTestCommand = struct_sTestCommand# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1760

sTestCommandWithCP56Time2a = struct_sTestCommandWithCP56Time2a# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1775

sResetProcessCommand = struct_sResetProcessCommand# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1802

sDelayAcquisitionCommand = struct_sDelayAcquisitionCommand# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1817

sEndOfInitialization = struct_sEndOfInitialization# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1832

sFileReady = struct_sFileReady# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1973

sSectionReady = struct_sSectionReady# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2014

sFileCallOrSelect = struct_sFileCallOrSelect# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2046

sFileLastSegmentOrSection = struct_sFileLastSegmentOrSection# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2067

sFileACK = struct_sFileACK# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2091

sFileSegment = struct_sFileSegment# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2112

sFileDirectory = struct_sFileDirectory# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2139

sQueryLog = struct_sQueryLog# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2175

sFrame = struct_sFrame# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 759

sIMasterConnection = struct_sIMasterConnection# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 65

sCS101_SlavePlugin = struct_sCS101_SlavePlugin# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 178

sCS104_Slave = struct_sCS104_Slave# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 50

sCS104_RedundancyGroup = struct_sCS104_RedundancyGroup# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 64

sCS104_Connection = struct_sCS104_Connection# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 52

sLinkLayerParameters = struct_sLinkLayerParameters# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/link_layer_parameters.h: 42

sCS101_Master = struct_sCS101_Master# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_master.h: 55

sCS101_Slave = struct_sCS101_Slave# /home/user/Desktop/scada/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 59

# No inserted files

# No prefix-stripping

