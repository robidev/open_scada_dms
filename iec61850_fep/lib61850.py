r"""Wrapper for stack_config.h

Generated with:
/home/user/iec61850_open_gateway/.venv/bin/ctypesgen -l libiec61850.so -I ../libiec61850/config/ ../libiec61850/config/stack_config.h -I ../libiec61850/src/iec61850/inc/ ../libiec61850/src/iec61850/inc/iec61850_cdc.h ../libiec61850/src/iec61850/inc/iec61850_client.h ../libiec61850/src/iec61850/inc/iec61850_common.h ../libiec61850/src/iec61850/inc/iec61850_config_file_parser.h ../libiec61850/src/iec61850/inc/iec61850_dynamic_model.h ../libiec61850/src/iec61850/inc/iec61850_model.h ../libiec61850/src/iec61850/inc/iec61850_server.h -I ../libiec61850/src/common/inc/ ../libiec61850/src/common/inc/buffer_chain.h ../libiec61850/src/common/inc/byte_buffer.h ../libiec61850/src/common/inc/conversions.h ../libiec61850/src/common/inc/libiec61850_common_api.h ../libiec61850/src/common/inc/libiec61850_platform_includes.h ../libiec61850/src/common/inc/linked_list.h ../libiec61850/src/common/inc/map.h ../libiec61850/src/common/inc/mem_alloc_linked_list.h ../libiec61850/src/common/inc/simple_allocator.h ../libiec61850/src/common/inc/sntp_client.h ../libiec61850/src/common/inc/string_map.h ../libiec61850/src/common/inc/string_utilities.h -I ../libiec61850/src/mms/inc/ ../libiec61850/src/mms/inc/iso_connection_parameters.h ../libiec61850/src/mms/inc/mms_client_connection.h ../libiec61850/src/mms/inc/mms_common.h ../libiec61850/src/mms/inc/mms_server.h ../libiec61850/src/mms/inc/mms_types.h ../libiec61850/src/mms/inc/mms_type_spec.h ../libiec61850/src/mms/inc/mms_value.h -I ../libiec61850/src/goose/ ../libiec61850/src/goose/goose_publisher.h ../libiec61850/src/goose/goose_receiver.h ../libiec61850/src/goose/goose_receiver_internal.h ../libiec61850/src/goose/goose_subscriber.h -I ../libiec61850/src/logging/ ../libiec61850/src/logging/logging_api.h -I ../libiec61850/src/r_session/ ../libiec61850/src/r_session/r_session_crypto.h ../libiec61850/src/r_session/r_session.h ../libiec61850/src/r_session/r_session_internal.h -I ../libiec61850/src/sampled_values/ ../libiec61850/src/sampled_values/sv_publisher.h ../libiec61850/src/sampled_values/sv_subscriber.h -I ../libiec61850/hal/inc/ ../libiec61850/hal/inc/hal_base.h ../libiec61850/hal/inc/hal_ethernet.h ../libiec61850/hal/inc/hal_filesystem.h ../libiec61850/hal/inc/hal_serial.h ../libiec61850/hal/inc/hal_socket.h ../libiec61850/hal/inc/hal_thread.h ../libiec61850/hal/inc/hal_time.h ../libiec61850/hal/inc/lib_memory.h ../libiec61850/hal/inc/platform_endian.h ../libiec61850/hal/inc/tls_ciphers.h ../libiec61850/hal/inc/tls_config.h ../libiec61850/hal/inc/tls_socket.h -o _lib61850.py

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
_libs["libiec61850.so"] = load_library("libiec61850.so")

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

nsSinceEpoch = uint64_t# ../libiec61850/hal/inc/hal_time.h: 35

msSinceEpoch = uint64_t# ../libiec61850/hal/inc/hal_time.h: 36

# ../libiec61850/hal/inc/hal_time.h: 47
if _libs["libiec61850.so"].has("Hal_getTimeInMs", "cdecl"):
    Hal_getTimeInMs = _libs["libiec61850.so"].get("Hal_getTimeInMs", "cdecl")
    Hal_getTimeInMs.argtypes = []
    Hal_getTimeInMs.restype = msSinceEpoch

# ../libiec61850/hal/inc/hal_time.h: 58
if _libs["libiec61850.so"].has("Hal_getTimeInNs", "cdecl"):
    Hal_getTimeInNs = _libs["libiec61850.so"].get("Hal_getTimeInNs", "cdecl")
    Hal_getTimeInNs.argtypes = []
    Hal_getTimeInNs.restype = nsSinceEpoch

# ../libiec61850/hal/inc/hal_time.h: 69
if _libs["libiec61850.so"].has("Hal_setTimeInNs", "cdecl"):
    Hal_setTimeInNs = _libs["libiec61850.so"].get("Hal_setTimeInNs", "cdecl")
    Hal_setTimeInNs.argtypes = [nsSinceEpoch]
    Hal_setTimeInNs.restype = c_bool

enum_anon_18 = c_int# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_NONE = 0# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_CONNECTION_REJECTED = 1# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_CONNECTION_LOST = 2# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_SERVICE_TIMEOUT = 3# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_PARSING_RESPONSE = 4# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_HARDWARE_FAULT = 5# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_CONCLUDE_REJECTED = 6# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_INVALID_ARGUMENTS = 7# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_OUTSTANDING_CALL_LIMIT = 8# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_OTHER = 9# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_VMDSTATE_OTHER = 10# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_APPLICATION_REFERENCE_OTHER = 20# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_DEFINITION_OTHER = 30# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_DEFINITION_INVALID_ADDRESS = 31# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_DEFINITION_TYPE_UNSUPPORTED = 32# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_DEFINITION_TYPE_INCONSISTENT = 33# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_DEFINITION_OBJECT_UNDEFINED = 34# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_DEFINITION_OBJECT_EXISTS = 35# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_DEFINITION_OBJECT_ATTRIBUTE_INCONSISTENT = 36# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_RESOURCE_OTHER = 40# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_RESOURCE_CAPABILITY_UNAVAILABLE = 41# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_SERVICE_OTHER = 50# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_SERVICE_OBJECT_CONSTRAINT_CONFLICT = 55# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_SERVICE_PREEMPT_OTHER = 60# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_TIME_RESOLUTION_OTHER = 70# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_ACCESS_OTHER = 80# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_ACCESS_OBJECT_NON_EXISTENT = 81# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_ACCESS_OBJECT_ACCESS_UNSUPPORTED = 82# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_ACCESS_OBJECT_ACCESS_DENIED = 83# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_ACCESS_OBJECT_INVALIDATED = 84# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_ACCESS_OBJECT_VALUE_INVALID = 85# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_ACCESS_TEMPORARILY_UNAVAILABLE = 86# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_FILE_OTHER = 90# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_FILE_FILENAME_AMBIGUOUS = 91# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_FILE_FILE_BUSY = 92# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_FILE_FILENAME_SYNTAX_ERROR = 93# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_FILE_CONTENT_TYPE_INVALID = 94# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_FILE_POSITION_INVALID = 95# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_FILE_FILE_ACCESS_DENIED = 96# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_FILE_FILE_NON_EXISTENT = 97# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_FILE_DUPLICATE_FILENAME = 98# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_FILE_INSUFFICIENT_SPACE_IN_FILESTORE = 99# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_REJECT_OTHER = 100# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_REJECT_UNKNOWN_PDU_TYPE = 101# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_REJECT_INVALID_PDU = 102# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_REJECT_UNRECOGNIZED_SERVICE = 103# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_REJECT_UNRECOGNIZED_MODIFIER = 104# ../libiec61850/src/mms/inc/mms_common.h: 103

MMS_ERROR_REJECT_REQUEST_INVALID_ARGUMENT = 105# ../libiec61850/src/mms/inc/mms_common.h: 103

MmsError = enum_anon_18# ../libiec61850/src/mms/inc/mms_common.h: 103

enum_anon_19 = c_int# ../libiec61850/src/mms/inc/mms_common.h: 135

MMS_ARRAY = 0# ../libiec61850/src/mms/inc/mms_common.h: 135

MMS_STRUCTURE = 1# ../libiec61850/src/mms/inc/mms_common.h: 135

MMS_BOOLEAN = 2# ../libiec61850/src/mms/inc/mms_common.h: 135

MMS_BIT_STRING = 3# ../libiec61850/src/mms/inc/mms_common.h: 135

MMS_INTEGER = 4# ../libiec61850/src/mms/inc/mms_common.h: 135

MMS_UNSIGNED = 5# ../libiec61850/src/mms/inc/mms_common.h: 135

MMS_FLOAT = 6# ../libiec61850/src/mms/inc/mms_common.h: 135

MMS_OCTET_STRING = 7# ../libiec61850/src/mms/inc/mms_common.h: 135

MMS_VISIBLE_STRING = 8# ../libiec61850/src/mms/inc/mms_common.h: 135

MMS_GENERALIZED_TIME = 9# ../libiec61850/src/mms/inc/mms_common.h: 135

MMS_BINARY_TIME = 10# ../libiec61850/src/mms/inc/mms_common.h: 135

MMS_BCD = 11# ../libiec61850/src/mms/inc/mms_common.h: 135

MMS_OBJ_ID = 12# ../libiec61850/src/mms/inc/mms_common.h: 135

MMS_STRING = 13# ../libiec61850/src/mms/inc/mms_common.h: 135

MMS_UTC_TIME = 14# ../libiec61850/src/mms/inc/mms_common.h: 135

MMS_DATA_ACCESS_ERROR = 15# ../libiec61850/src/mms/inc/mms_common.h: 135

MmsType = enum_anon_19# ../libiec61850/src/mms/inc/mms_common.h: 135

# ../libiec61850/src/mms/inc/mms_common.h: 137
class struct_sMmsDomain(Structure):
    pass

MmsDomain = struct_sMmsDomain# ../libiec61850/src/mms/inc/mms_common.h: 137

# ../libiec61850/src/mms/inc/mms_common.h: 145
class struct_sMmsAccessSpecifier(Structure):
    pass

struct_sMmsAccessSpecifier.__slots__ = [
    'domain',
    'variableName',
    'arrayIndex',
    'componentName',
]
struct_sMmsAccessSpecifier._fields_ = [
    ('domain', POINTER(MmsDomain)),
    ('variableName', String),
    ('arrayIndex', c_int),
    ('componentName', String),
]

MmsAccessSpecifier = struct_sMmsAccessSpecifier# ../libiec61850/src/mms/inc/mms_common.h: 145

# ../libiec61850/src/mms/inc/mms_common.h: 153
class struct_anon_20(Structure):
    pass

struct_anon_20.__slots__ = [
    'domainId',
    'itemId',
    'arrayIndex',
    'componentName',
]
struct_anon_20._fields_ = [
    ('domainId', String),
    ('itemId', String),
    ('arrayIndex', c_int32),
    ('componentName', String),
]

MmsVariableAccessSpecification = struct_anon_20# ../libiec61850/src/mms/inc/mms_common.h: 153

# ../libiec61850/src/mms/inc/mms_common.h: 155
class struct_sMmsNamedVariableList(Structure):
    pass

MmsNamedVariableList = POINTER(struct_sMmsNamedVariableList)# ../libiec61850/src/mms/inc/mms_common.h: 155

MmsNamedVariableListEntry = POINTER(struct_sMmsAccessSpecifier)# ../libiec61850/src/mms/inc/mms_common.h: 156

# ../libiec61850/src/mms/inc/mms_common.h: 164
class struct_anon_21(Structure):
    pass

struct_anon_21.__slots__ = [
    'arc',
    'arcCount',
]
struct_anon_21._fields_ = [
    ('arc', uint16_t * int(10)),
    ('arcCount', c_int),
]

ItuObjectIdentifier = struct_anon_21# ../libiec61850/src/mms/inc/mms_common.h: 164

# ../libiec61850/src/mms/inc/mms_common.h: 172
class struct_anon_22(Structure):
    pass

struct_anon_22.__slots__ = [
    'apTitle',
    'aeQualifier',
]
struct_anon_22._fields_ = [
    ('apTitle', ItuObjectIdentifier),
    ('aeQualifier', c_int),
]

IsoApplicationReference = struct_anon_22# ../libiec61850/src/mms/inc/mms_common.h: 172

enum_anon_23 = c_int# ../libiec61850/src/mms/inc/mms_types.h: 36

MMS_VALUE_NO_RESPONSE = 0# ../libiec61850/src/mms/inc/mms_types.h: 36

MMS_VALUE_OK = (MMS_VALUE_NO_RESPONSE + 1)# ../libiec61850/src/mms/inc/mms_types.h: 36

MMS_VALUE_ACCESS_DENIED = (MMS_VALUE_OK + 1)# ../libiec61850/src/mms/inc/mms_types.h: 36

MMS_VALUE_VALUE_INVALID = (MMS_VALUE_ACCESS_DENIED + 1)# ../libiec61850/src/mms/inc/mms_types.h: 36

MMS_VALUE_TEMPORARILY_UNAVAILABLE = (MMS_VALUE_VALUE_INVALID + 1)# ../libiec61850/src/mms/inc/mms_types.h: 36

MMS_VALUE_OBJECT_ACCESS_UNSUPPORTED = (MMS_VALUE_TEMPORARILY_UNAVAILABLE + 1)# ../libiec61850/src/mms/inc/mms_types.h: 36

MmsValueIndication = enum_anon_23# ../libiec61850/src/mms/inc/mms_types.h: 36

# ../libiec61850/src/mms/inc/mms_types.h: 50
class struct_sMmsVariableSpecification(Structure):
    pass

MmsVariableSpecification = struct_sMmsVariableSpecification# ../libiec61850/src/mms/inc/mms_types.h: 46

# ../libiec61850/src/mms/inc/mms_types.h: 55
class struct_sMmsArray(Structure):
    pass

struct_sMmsArray.__slots__ = [
    'elementCount',
    'elementTypeSpec',
]
struct_sMmsArray._fields_ = [
    ('elementCount', c_int),
    ('elementTypeSpec', POINTER(MmsVariableSpecification)),
]

# ../libiec61850/src/mms/inc/mms_types.h: 59
class struct_sMmsStructure(Structure):
    pass

struct_sMmsStructure.__slots__ = [
    'elementCount',
    'elements',
]
struct_sMmsStructure._fields_ = [
    ('elementCount', c_int),
    ('elements', POINTER(POINTER(MmsVariableSpecification))),
]

# ../libiec61850/src/mms/inc/mms_types.h: 66
class struct_sMmsFloat(Structure):
    pass

struct_sMmsFloat.__slots__ = [
    'exponentWidth',
    'formatWidth',
]
struct_sMmsFloat._fields_ = [
    ('exponentWidth', uint8_t),
    ('formatWidth', uint8_t),
]

# ../libiec61850/src/mms/inc/mms_types.h: 53
class union_uMmsTypeSpecification(Union):
    pass

union_uMmsTypeSpecification.__slots__ = [
    'array',
    'structure',
    'boolean',
    'integer',
    'unsignedInteger',
    'floatingpoint',
    'bitString',
    'octetString',
    'visibleString',
    'mmsString',
    'utctime',
    'binaryTime',
]
union_uMmsTypeSpecification._fields_ = [
    ('array', struct_sMmsArray),
    ('structure', struct_sMmsStructure),
    ('boolean', c_int),
    ('integer', c_int),
    ('unsignedInteger', c_int),
    ('floatingpoint', struct_sMmsFloat),
    ('bitString', c_int),
    ('octetString', c_int),
    ('visibleString', c_int),
    ('mmsString', c_int),
    ('utctime', c_int),
    ('binaryTime', c_int),
]

struct_sMmsVariableSpecification.__slots__ = [
    'type',
    'name',
    'typeSpec',
]
struct_sMmsVariableSpecification._fields_ = [
    ('type', MmsType),
    ('name', String),
    ('typeSpec', union_uMmsTypeSpecification),
]

enum_anon_24 = c_int# ../libiec61850/src/mms/inc/mms_value.h: 63

DATA_ACCESS_ERROR_SUCCESS_NO_UPDATE = (-3)# ../libiec61850/src/mms/inc/mms_value.h: 63

DATA_ACCESS_ERROR_NO_RESPONSE = (-2)# ../libiec61850/src/mms/inc/mms_value.h: 63

DATA_ACCESS_ERROR_SUCCESS = (-1)# ../libiec61850/src/mms/inc/mms_value.h: 63

DATA_ACCESS_ERROR_OBJECT_INVALIDATED = 0# ../libiec61850/src/mms/inc/mms_value.h: 63

DATA_ACCESS_ERROR_HARDWARE_FAULT = 1# ../libiec61850/src/mms/inc/mms_value.h: 63

DATA_ACCESS_ERROR_TEMPORARILY_UNAVAILABLE = 2# ../libiec61850/src/mms/inc/mms_value.h: 63

DATA_ACCESS_ERROR_OBJECT_ACCESS_DENIED = 3# ../libiec61850/src/mms/inc/mms_value.h: 63

DATA_ACCESS_ERROR_OBJECT_UNDEFINED = 4# ../libiec61850/src/mms/inc/mms_value.h: 63

DATA_ACCESS_ERROR_INVALID_ADDRESS = 5# ../libiec61850/src/mms/inc/mms_value.h: 63

DATA_ACCESS_ERROR_TYPE_UNSUPPORTED = 6# ../libiec61850/src/mms/inc/mms_value.h: 63

DATA_ACCESS_ERROR_TYPE_INCONSISTENT = 7# ../libiec61850/src/mms/inc/mms_value.h: 63

DATA_ACCESS_ERROR_OBJECT_ATTRIBUTE_INCONSISTENT = 8# ../libiec61850/src/mms/inc/mms_value.h: 63

DATA_ACCESS_ERROR_OBJECT_ACCESS_UNSUPPORTED = 9# ../libiec61850/src/mms/inc/mms_value.h: 63

DATA_ACCESS_ERROR_OBJECT_NONE_EXISTENT = 10# ../libiec61850/src/mms/inc/mms_value.h: 63

DATA_ACCESS_ERROR_OBJECT_VALUE_INVALID = 11# ../libiec61850/src/mms/inc/mms_value.h: 63

DATA_ACCESS_ERROR_UNKNOWN = 12# ../libiec61850/src/mms/inc/mms_value.h: 63

MmsDataAccessError = enum_anon_24# ../libiec61850/src/mms/inc/mms_value.h: 63

# ../libiec61850/src/mms/inc/mms_value.h: 68
class struct_sMmsValue(Structure):
    pass

MmsValue = struct_sMmsValue# ../libiec61850/src/mms/inc/mms_value.h: 68

# ../libiec61850/src/mms/inc/mms_value.h: 82
if _libs["libiec61850.so"].has("MmsValue_createArray", "cdecl"):
    MmsValue_createArray = _libs["libiec61850.so"].get("MmsValue_createArray", "cdecl")
    MmsValue_createArray.argtypes = [POINTER(MmsVariableSpecification), c_int]
    MmsValue_createArray.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 93
if _libs["libiec61850.so"].has("MmsValue_getArraySize", "cdecl"):
    MmsValue_getArraySize = _libs["libiec61850.so"].get("MmsValue_getArraySize", "cdecl")
    MmsValue_getArraySize.argtypes = [POINTER(MmsValue)]
    MmsValue_getArraySize.restype = uint32_t

# ../libiec61850/src/mms/inc/mms_value.h: 103
if _libs["libiec61850.so"].has("MmsValue_getElement", "cdecl"):
    MmsValue_getElement = _libs["libiec61850.so"].get("MmsValue_getElement", "cdecl")
    MmsValue_getElement.argtypes = [POINTER(MmsValue), c_int]
    MmsValue_getElement.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 113
if _libs["libiec61850.so"].has("MmsValue_createEmptyArray", "cdecl"):
    MmsValue_createEmptyArray = _libs["libiec61850.so"].get("MmsValue_createEmptyArray", "cdecl")
    MmsValue_createEmptyArray.argtypes = [c_int]
    MmsValue_createEmptyArray.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 127
if _libs["libiec61850.so"].has("MmsValue_setElement", "cdecl"):
    MmsValue_setElement = _libs["libiec61850.so"].get("MmsValue_setElement", "cdecl")
    MmsValue_setElement.argtypes = [POINTER(MmsValue), c_int, POINTER(MmsValue)]
    MmsValue_setElement.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 135
if _libs["libiec61850.so"].has("MmsValue_getDataAccessError", "cdecl"):
    MmsValue_getDataAccessError = _libs["libiec61850.so"].get("MmsValue_getDataAccessError", "cdecl")
    MmsValue_getDataAccessError.argtypes = [POINTER(MmsValue)]
    MmsValue_getDataAccessError.restype = MmsDataAccessError

# ../libiec61850/src/mms/inc/mms_value.h: 145
if _libs["libiec61850.so"].has("MmsValue_toInt64", "cdecl"):
    MmsValue_toInt64 = _libs["libiec61850.so"].get("MmsValue_toInt64", "cdecl")
    MmsValue_toInt64.argtypes = [POINTER(MmsValue)]
    MmsValue_toInt64.restype = c_int64

# ../libiec61850/src/mms/inc/mms_value.h: 155
if _libs["libiec61850.so"].has("MmsValue_toInt32", "cdecl"):
    MmsValue_toInt32 = _libs["libiec61850.so"].get("MmsValue_toInt32", "cdecl")
    MmsValue_toInt32.argtypes = [POINTER(MmsValue)]
    MmsValue_toInt32.restype = c_int32

# ../libiec61850/src/mms/inc/mms_value.h: 165
if _libs["libiec61850.so"].has("MmsValue_toUint32", "cdecl"):
    MmsValue_toUint32 = _libs["libiec61850.so"].get("MmsValue_toUint32", "cdecl")
    MmsValue_toUint32.argtypes = [POINTER(MmsValue)]
    MmsValue_toUint32.restype = uint32_t

# ../libiec61850/src/mms/inc/mms_value.h: 175
if _libs["libiec61850.so"].has("MmsValue_toDouble", "cdecl"):
    MmsValue_toDouble = _libs["libiec61850.so"].get("MmsValue_toDouble", "cdecl")
    MmsValue_toDouble.argtypes = [POINTER(MmsValue)]
    MmsValue_toDouble.restype = c_double

# ../libiec61850/src/mms/inc/mms_value.h: 185
if _libs["libiec61850.so"].has("MmsValue_toFloat", "cdecl"):
    MmsValue_toFloat = _libs["libiec61850.so"].get("MmsValue_toFloat", "cdecl")
    MmsValue_toFloat.argtypes = [POINTER(MmsValue)]
    MmsValue_toFloat.restype = c_float

# ../libiec61850/src/mms/inc/mms_value.h: 195
if _libs["libiec61850.so"].has("MmsValue_toUnixTimestamp", "cdecl"):
    MmsValue_toUnixTimestamp = _libs["libiec61850.so"].get("MmsValue_toUnixTimestamp", "cdecl")
    MmsValue_toUnixTimestamp.argtypes = [POINTER(MmsValue)]
    MmsValue_toUnixTimestamp.restype = uint32_t

# ../libiec61850/src/mms/inc/mms_value.h: 203
if _libs["libiec61850.so"].has("MmsValue_setFloat", "cdecl"):
    MmsValue_setFloat = _libs["libiec61850.so"].get("MmsValue_setFloat", "cdecl")
    MmsValue_setFloat.argtypes = [POINTER(MmsValue), c_float]
    MmsValue_setFloat.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 211
if _libs["libiec61850.so"].has("MmsValue_setDouble", "cdecl"):
    MmsValue_setDouble = _libs["libiec61850.so"].get("MmsValue_setDouble", "cdecl")
    MmsValue_setDouble.argtypes = [POINTER(MmsValue), c_double]
    MmsValue_setDouble.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 220
if _libs["libiec61850.so"].has("MmsValue_setInt8", "cdecl"):
    MmsValue_setInt8 = _libs["libiec61850.so"].get("MmsValue_setInt8", "cdecl")
    MmsValue_setInt8.argtypes = [POINTER(MmsValue), c_int8]
    MmsValue_setInt8.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 229
if _libs["libiec61850.so"].has("MmsValue_setInt16", "cdecl"):
    MmsValue_setInt16 = _libs["libiec61850.so"].get("MmsValue_setInt16", "cdecl")
    MmsValue_setInt16.argtypes = [POINTER(MmsValue), c_int16]
    MmsValue_setInt16.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 238
if _libs["libiec61850.so"].has("MmsValue_setInt32", "cdecl"):
    MmsValue_setInt32 = _libs["libiec61850.so"].get("MmsValue_setInt32", "cdecl")
    MmsValue_setInt32.argtypes = [POINTER(MmsValue), c_int32]
    MmsValue_setInt32.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 247
if _libs["libiec61850.so"].has("MmsValue_setInt64", "cdecl"):
    MmsValue_setInt64 = _libs["libiec61850.so"].get("MmsValue_setInt64", "cdecl")
    MmsValue_setInt64.argtypes = [POINTER(MmsValue), c_int64]
    MmsValue_setInt64.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 256
if _libs["libiec61850.so"].has("MmsValue_setUint8", "cdecl"):
    MmsValue_setUint8 = _libs["libiec61850.so"].get("MmsValue_setUint8", "cdecl")
    MmsValue_setUint8.argtypes = [POINTER(MmsValue), uint8_t]
    MmsValue_setUint8.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 265
if _libs["libiec61850.so"].has("MmsValue_setUint16", "cdecl"):
    MmsValue_setUint16 = _libs["libiec61850.so"].get("MmsValue_setUint16", "cdecl")
    MmsValue_setUint16.argtypes = [POINTER(MmsValue), uint16_t]
    MmsValue_setUint16.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 274
if _libs["libiec61850.so"].has("MmsValue_setUint32", "cdecl"):
    MmsValue_setUint32 = _libs["libiec61850.so"].get("MmsValue_setUint32", "cdecl")
    MmsValue_setUint32.argtypes = [POINTER(MmsValue), uint32_t]
    MmsValue_setUint32.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 284
if _libs["libiec61850.so"].has("MmsValue_setBoolean", "cdecl"):
    MmsValue_setBoolean = _libs["libiec61850.so"].get("MmsValue_setBoolean", "cdecl")
    MmsValue_setBoolean.argtypes = [POINTER(MmsValue), c_bool]
    MmsValue_setBoolean.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 293
if _libs["libiec61850.so"].has("MmsValue_getBoolean", "cdecl"):
    MmsValue_getBoolean = _libs["libiec61850.so"].get("MmsValue_getBoolean", "cdecl")
    MmsValue_getBoolean.argtypes = [POINTER(MmsValue)]
    MmsValue_getBoolean.restype = c_bool

# ../libiec61850/src/mms/inc/mms_value.h: 302
if _libs["libiec61850.so"].has("MmsValue_toString", "cdecl"):
    MmsValue_toString = _libs["libiec61850.so"].get("MmsValue_toString", "cdecl")
    MmsValue_toString.argtypes = [POINTER(MmsValue)]
    MmsValue_toString.restype = c_char_p

# ../libiec61850/src/mms/inc/mms_value.h: 313
if _libs["libiec61850.so"].has("MmsValue_getStringSize", "cdecl"):
    MmsValue_getStringSize = _libs["libiec61850.so"].get("MmsValue_getStringSize", "cdecl")
    MmsValue_getStringSize.argtypes = [POINTER(MmsValue)]
    MmsValue_getStringSize.restype = c_int

# ../libiec61850/src/mms/inc/mms_value.h: 316
if _libs["libiec61850.so"].has("MmsValue_setVisibleString", "cdecl"):
    MmsValue_setVisibleString = _libs["libiec61850.so"].get("MmsValue_setVisibleString", "cdecl")
    MmsValue_setVisibleString.argtypes = [POINTER(MmsValue), String]
    MmsValue_setVisibleString.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 328
if _libs["libiec61850.so"].has("MmsValue_setBitStringBit", "cdecl"):
    MmsValue_setBitStringBit = _libs["libiec61850.so"].get("MmsValue_setBitStringBit", "cdecl")
    MmsValue_setBitStringBit.argtypes = [POINTER(MmsValue), c_int, c_bool]
    MmsValue_setBitStringBit.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 339
if _libs["libiec61850.so"].has("MmsValue_getBitStringBit", "cdecl"):
    MmsValue_getBitStringBit = _libs["libiec61850.so"].get("MmsValue_getBitStringBit", "cdecl")
    MmsValue_getBitStringBit.argtypes = [POINTER(MmsValue), c_int]
    MmsValue_getBitStringBit.restype = c_bool

# ../libiec61850/src/mms/inc/mms_value.h: 347
if _libs["libiec61850.so"].has("MmsValue_deleteAllBitStringBits", "cdecl"):
    MmsValue_deleteAllBitStringBits = _libs["libiec61850.so"].get("MmsValue_deleteAllBitStringBits", "cdecl")
    MmsValue_deleteAllBitStringBits.argtypes = [POINTER(MmsValue)]
    MmsValue_deleteAllBitStringBits.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 356
if _libs["libiec61850.so"].has("MmsValue_getBitStringSize", "cdecl"):
    MmsValue_getBitStringSize = _libs["libiec61850.so"].get("MmsValue_getBitStringSize", "cdecl")
    MmsValue_getBitStringSize.argtypes = [POINTER(MmsValue)]
    MmsValue_getBitStringSize.restype = c_int

# ../libiec61850/src/mms/inc/mms_value.h: 364
if _libs["libiec61850.so"].has("MmsValue_getBitStringByteSize", "cdecl"):
    MmsValue_getBitStringByteSize = _libs["libiec61850.so"].get("MmsValue_getBitStringByteSize", "cdecl")
    MmsValue_getBitStringByteSize.argtypes = [POINTER(MmsValue)]
    MmsValue_getBitStringByteSize.restype = c_int

# ../libiec61850/src/mms/inc/mms_value.h: 372
if _libs["libiec61850.so"].has("MmsValue_getNumberOfSetBits", "cdecl"):
    MmsValue_getNumberOfSetBits = _libs["libiec61850.so"].get("MmsValue_getNumberOfSetBits", "cdecl")
    MmsValue_getNumberOfSetBits.argtypes = [POINTER(MmsValue)]
    MmsValue_getNumberOfSetBits.restype = c_int

# ../libiec61850/src/mms/inc/mms_value.h: 380
if _libs["libiec61850.so"].has("MmsValue_setAllBitStringBits", "cdecl"):
    MmsValue_setAllBitStringBits = _libs["libiec61850.so"].get("MmsValue_setAllBitStringBits", "cdecl")
    MmsValue_setAllBitStringBits.argtypes = [POINTER(MmsValue)]
    MmsValue_setAllBitStringBits.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 391
if _libs["libiec61850.so"].has("MmsValue_getBitStringAsInteger", "cdecl"):
    MmsValue_getBitStringAsInteger = _libs["libiec61850.so"].get("MmsValue_getBitStringAsInteger", "cdecl")
    MmsValue_getBitStringAsInteger.argtypes = [POINTER(MmsValue)]
    MmsValue_getBitStringAsInteger.restype = uint32_t

# ../libiec61850/src/mms/inc/mms_value.h: 403
if _libs["libiec61850.so"].has("MmsValue_setBitStringFromInteger", "cdecl"):
    MmsValue_setBitStringFromInteger = _libs["libiec61850.so"].get("MmsValue_setBitStringFromInteger", "cdecl")
    MmsValue_setBitStringFromInteger.argtypes = [POINTER(MmsValue), uint32_t]
    MmsValue_setBitStringFromInteger.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 414
if _libs["libiec61850.so"].has("MmsValue_getBitStringAsIntegerBigEndian", "cdecl"):
    MmsValue_getBitStringAsIntegerBigEndian = _libs["libiec61850.so"].get("MmsValue_getBitStringAsIntegerBigEndian", "cdecl")
    MmsValue_getBitStringAsIntegerBigEndian.argtypes = [POINTER(MmsValue)]
    MmsValue_getBitStringAsIntegerBigEndian.restype = uint32_t

# ../libiec61850/src/mms/inc/mms_value.h: 426
if _libs["libiec61850.so"].has("MmsValue_setBitStringFromIntegerBigEndian", "cdecl"):
    MmsValue_setBitStringFromIntegerBigEndian = _libs["libiec61850.so"].get("MmsValue_setBitStringFromIntegerBigEndian", "cdecl")
    MmsValue_setBitStringFromIntegerBigEndian.argtypes = [POINTER(MmsValue), uint32_t]
    MmsValue_setBitStringFromIntegerBigEndian.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 434
if _libs["libiec61850.so"].has("MmsValue_setUtcTime", "cdecl"):
    MmsValue_setUtcTime = _libs["libiec61850.so"].get("MmsValue_setUtcTime", "cdecl")
    MmsValue_setUtcTime.argtypes = [POINTER(MmsValue), uint32_t]
    MmsValue_setUtcTime.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 443
if _libs["libiec61850.so"].has("MmsValue_setUtcTimeMs", "cdecl"):
    MmsValue_setUtcTimeMs = _libs["libiec61850.so"].get("MmsValue_setUtcTimeMs", "cdecl")
    MmsValue_setUtcTimeMs.argtypes = [POINTER(MmsValue), uint64_t]
    MmsValue_setUtcTimeMs.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 455
if _libs["libiec61850.so"].has("MmsValue_setUtcTimeByBuffer", "cdecl"):
    MmsValue_setUtcTimeByBuffer = _libs["libiec61850.so"].get("MmsValue_setUtcTimeByBuffer", "cdecl")
    MmsValue_setUtcTimeByBuffer.argtypes = [POINTER(MmsValue), POINTER(uint8_t)]
    MmsValue_setUtcTimeByBuffer.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 466
if _libs["libiec61850.so"].has("MmsValue_getUtcTimeBuffer", "cdecl"):
    MmsValue_getUtcTimeBuffer = _libs["libiec61850.so"].get("MmsValue_getUtcTimeBuffer", "cdecl")
    MmsValue_getUtcTimeBuffer.argtypes = [POINTER(MmsValue)]
    MmsValue_getUtcTimeBuffer.restype = POINTER(uint8_t)

# ../libiec61850/src/mms/inc/mms_value.h: 477
if _libs["libiec61850.so"].has("MmsValue_getUtcTimeInMs", "cdecl"):
    MmsValue_getUtcTimeInMs = _libs["libiec61850.so"].get("MmsValue_getUtcTimeInMs", "cdecl")
    MmsValue_getUtcTimeInMs.argtypes = [POINTER(MmsValue)]
    MmsValue_getUtcTimeInMs.restype = uint64_t

# ../libiec61850/src/mms/inc/mms_value.h: 488
if _libs["libiec61850.so"].has("MmsValue_getUtcTimeInMsWithUs", "cdecl"):
    MmsValue_getUtcTimeInMsWithUs = _libs["libiec61850.so"].get("MmsValue_getUtcTimeInMsWithUs", "cdecl")
    MmsValue_getUtcTimeInMsWithUs.argtypes = [POINTER(MmsValue), POINTER(uint32_t)]
    MmsValue_getUtcTimeInMsWithUs.restype = uint64_t

# ../libiec61850/src/mms/inc/mms_value.h: 504
if _libs["libiec61850.so"].has("MmsValue_setUtcTimeQuality", "cdecl"):
    MmsValue_setUtcTimeQuality = _libs["libiec61850.so"].get("MmsValue_setUtcTimeQuality", "cdecl")
    MmsValue_setUtcTimeQuality.argtypes = [POINTER(MmsValue), uint8_t]
    MmsValue_setUtcTimeQuality.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 522
if _libs["libiec61850.so"].has("MmsValue_setUtcTimeMsEx", "cdecl"):
    MmsValue_setUtcTimeMsEx = _libs["libiec61850.so"].get("MmsValue_setUtcTimeMsEx", "cdecl")
    MmsValue_setUtcTimeMsEx.argtypes = [POINTER(MmsValue), uint64_t, uint8_t]
    MmsValue_setUtcTimeMsEx.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 540
if _libs["libiec61850.so"].has("MmsValue_getUtcTimeQuality", "cdecl"):
    MmsValue_getUtcTimeQuality = _libs["libiec61850.so"].get("MmsValue_getUtcTimeQuality", "cdecl")
    MmsValue_getUtcTimeQuality.argtypes = [POINTER(MmsValue)]
    MmsValue_getUtcTimeQuality.restype = uint8_t

# ../libiec61850/src/mms/inc/mms_value.h: 549
if _libs["libiec61850.so"].has("MmsValue_setBinaryTime", "cdecl"):
    MmsValue_setBinaryTime = _libs["libiec61850.so"].get("MmsValue_setBinaryTime", "cdecl")
    MmsValue_setBinaryTime.argtypes = [POINTER(MmsValue), uint64_t]
    MmsValue_setBinaryTime.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 559
if _libs["libiec61850.so"].has("MmsValue_getBinaryTimeAsUtcMs", "cdecl"):
    MmsValue_getBinaryTimeAsUtcMs = _libs["libiec61850.so"].get("MmsValue_getBinaryTimeAsUtcMs", "cdecl")
    MmsValue_getBinaryTimeAsUtcMs.argtypes = [POINTER(MmsValue)]
    MmsValue_getBinaryTimeAsUtcMs.restype = uint64_t

# ../libiec61850/src/mms/inc/mms_value.h: 573
if _libs["libiec61850.so"].has("MmsValue_setOctetString", "cdecl"):
    MmsValue_setOctetString = _libs["libiec61850.so"].get("MmsValue_setOctetString", "cdecl")
    MmsValue_setOctetString.argtypes = [POINTER(MmsValue), POINTER(uint8_t), c_int]
    MmsValue_setOctetString.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 588
if _libs["libiec61850.so"].has("MmsValue_setOctetStringOctet", "cdecl"):
    MmsValue_setOctetStringOctet = _libs["libiec61850.so"].get("MmsValue_setOctetStringOctet", "cdecl")
    MmsValue_setOctetStringOctet.argtypes = [POINTER(MmsValue), c_int, uint8_t]
    MmsValue_setOctetStringOctet.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 601
if _libs["libiec61850.so"].has("MmsValue_getOctetStringSize", "cdecl"):
    MmsValue_getOctetStringSize = _libs["libiec61850.so"].get("MmsValue_getOctetStringSize", "cdecl")
    MmsValue_getOctetStringSize.argtypes = [POINTER(MmsValue)]
    MmsValue_getOctetStringSize.restype = uint16_t

# ../libiec61850/src/mms/inc/mms_value.h: 614
if _libs["libiec61850.so"].has("MmsValue_getOctetStringMaxSize", "cdecl"):
    MmsValue_getOctetStringMaxSize = _libs["libiec61850.so"].get("MmsValue_getOctetStringMaxSize", "cdecl")
    MmsValue_getOctetStringMaxSize.argtypes = [POINTER(MmsValue)]
    MmsValue_getOctetStringMaxSize.restype = uint16_t

# ../libiec61850/src/mms/inc/mms_value.h: 625
if _libs["libiec61850.so"].has("MmsValue_getOctetStringBuffer", "cdecl"):
    MmsValue_getOctetStringBuffer = _libs["libiec61850.so"].get("MmsValue_getOctetStringBuffer", "cdecl")
    MmsValue_getOctetStringBuffer.argtypes = [POINTER(MmsValue)]
    MmsValue_getOctetStringBuffer.restype = POINTER(uint8_t)

# ../libiec61850/src/mms/inc/mms_value.h: 640
if _libs["libiec61850.so"].has("MmsValue_getOctetStringOctet", "cdecl"):
    MmsValue_getOctetStringOctet = _libs["libiec61850.so"].get("MmsValue_getOctetStringOctet", "cdecl")
    MmsValue_getOctetStringOctet.argtypes = [POINTER(MmsValue), c_int]
    MmsValue_getOctetStringOctet.restype = uint8_t

# ../libiec61850/src/mms/inc/mms_value.h: 654
if _libs["libiec61850.so"].has("MmsValue_update", "cdecl"):
    MmsValue_update = _libs["libiec61850.so"].get("MmsValue_update", "cdecl")
    MmsValue_update.argtypes = [POINTER(MmsValue), POINTER(MmsValue)]
    MmsValue_update.restype = c_bool

# ../libiec61850/src/mms/inc/mms_value.h: 668
if _libs["libiec61850.so"].has("MmsValue_equals", "cdecl"):
    MmsValue_equals = _libs["libiec61850.so"].get("MmsValue_equals", "cdecl")
    MmsValue_equals.argtypes = [POINTER(MmsValue), POINTER(MmsValue)]
    MmsValue_equals.restype = c_bool

# ../libiec61850/src/mms/inc/mms_value.h: 683
if _libs["libiec61850.so"].has("MmsValue_equalTypes", "cdecl"):
    MmsValue_equalTypes = _libs["libiec61850.so"].get("MmsValue_equalTypes", "cdecl")
    MmsValue_equalTypes.argtypes = [POINTER(MmsValue), POINTER(MmsValue)]
    MmsValue_equalTypes.restype = c_bool

# ../libiec61850/src/mms/inc/mms_value.h: 690
if _libs["libiec61850.so"].has("MmsValue_newDataAccessError", "cdecl"):
    MmsValue_newDataAccessError = _libs["libiec61850.so"].get("MmsValue_newDataAccessError", "cdecl")
    MmsValue_newDataAccessError.argtypes = [MmsDataAccessError]
    MmsValue_newDataAccessError.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 693
if _libs["libiec61850.so"].has("MmsValue_newInteger", "cdecl"):
    MmsValue_newInteger = _libs["libiec61850.so"].get("MmsValue_newInteger", "cdecl")
    MmsValue_newInteger.argtypes = [c_int]
    MmsValue_newInteger.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 696
if _libs["libiec61850.so"].has("MmsValue_newUnsigned", "cdecl"):
    MmsValue_newUnsigned = _libs["libiec61850.so"].get("MmsValue_newUnsigned", "cdecl")
    MmsValue_newUnsigned.argtypes = [c_int]
    MmsValue_newUnsigned.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 699
if _libs["libiec61850.so"].has("MmsValue_newBoolean", "cdecl"):
    MmsValue_newBoolean = _libs["libiec61850.so"].get("MmsValue_newBoolean", "cdecl")
    MmsValue_newBoolean.argtypes = [c_bool]
    MmsValue_newBoolean.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 709
if _libs["libiec61850.so"].has("MmsValue_newBitString", "cdecl"):
    MmsValue_newBitString = _libs["libiec61850.so"].get("MmsValue_newBitString", "cdecl")
    MmsValue_newBitString.argtypes = [c_int]
    MmsValue_newBitString.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 712
if _libs["libiec61850.so"].has("MmsValue_newOctetString", "cdecl"):
    MmsValue_newOctetString = _libs["libiec61850.so"].get("MmsValue_newOctetString", "cdecl")
    MmsValue_newOctetString.argtypes = [c_int, c_int]
    MmsValue_newOctetString.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 715
if _libs["libiec61850.so"].has("MmsValue_newStructure", "cdecl"):
    MmsValue_newStructure = _libs["libiec61850.so"].get("MmsValue_newStructure", "cdecl")
    MmsValue_newStructure.argtypes = [POINTER(MmsVariableSpecification)]
    MmsValue_newStructure.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 718
if _libs["libiec61850.so"].has("MmsValue_createEmptyStructure", "cdecl"):
    MmsValue_createEmptyStructure = _libs["libiec61850.so"].get("MmsValue_createEmptyStructure", "cdecl")
    MmsValue_createEmptyStructure.argtypes = [c_int]
    MmsValue_createEmptyStructure.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 721
if _libs["libiec61850.so"].has("MmsValue_newDefaultValue", "cdecl"):
    MmsValue_newDefaultValue = _libs["libiec61850.so"].get("MmsValue_newDefaultValue", "cdecl")
    MmsValue_newDefaultValue.argtypes = [POINTER(MmsVariableSpecification)]
    MmsValue_newDefaultValue.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 724
if _libs["libiec61850.so"].has("MmsValue_newIntegerFromInt8", "cdecl"):
    MmsValue_newIntegerFromInt8 = _libs["libiec61850.so"].get("MmsValue_newIntegerFromInt8", "cdecl")
    MmsValue_newIntegerFromInt8.argtypes = [c_int8]
    MmsValue_newIntegerFromInt8.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 727
if _libs["libiec61850.so"].has("MmsValue_newIntegerFromInt16", "cdecl"):
    MmsValue_newIntegerFromInt16 = _libs["libiec61850.so"].get("MmsValue_newIntegerFromInt16", "cdecl")
    MmsValue_newIntegerFromInt16.argtypes = [c_int16]
    MmsValue_newIntegerFromInt16.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 730
if _libs["libiec61850.so"].has("MmsValue_newIntegerFromInt32", "cdecl"):
    MmsValue_newIntegerFromInt32 = _libs["libiec61850.so"].get("MmsValue_newIntegerFromInt32", "cdecl")
    MmsValue_newIntegerFromInt32.argtypes = [c_int32]
    MmsValue_newIntegerFromInt32.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 733
if _libs["libiec61850.so"].has("MmsValue_newIntegerFromInt64", "cdecl"):
    MmsValue_newIntegerFromInt64 = _libs["libiec61850.so"].get("MmsValue_newIntegerFromInt64", "cdecl")
    MmsValue_newIntegerFromInt64.argtypes = [c_int64]
    MmsValue_newIntegerFromInt64.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 736
if _libs["libiec61850.so"].has("MmsValue_newUnsignedFromUint32", "cdecl"):
    MmsValue_newUnsignedFromUint32 = _libs["libiec61850.so"].get("MmsValue_newUnsignedFromUint32", "cdecl")
    MmsValue_newUnsignedFromUint32.argtypes = [uint32_t]
    MmsValue_newUnsignedFromUint32.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 746
if _libs["libiec61850.so"].has("MmsValue_newFloat", "cdecl"):
    MmsValue_newFloat = _libs["libiec61850.so"].get("MmsValue_newFloat", "cdecl")
    MmsValue_newFloat.argtypes = [c_float]
    MmsValue_newFloat.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 756
if _libs["libiec61850.so"].has("MmsValue_newDouble", "cdecl"):
    MmsValue_newDouble = _libs["libiec61850.so"].get("MmsValue_newDouble", "cdecl")
    MmsValue_newDouble.argtypes = [c_double]
    MmsValue_newDouble.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 769
if _libs["libiec61850.so"].has("MmsValue_clone", "cdecl"):
    MmsValue_clone = _libs["libiec61850.so"].get("MmsValue_clone", "cdecl")
    MmsValue_clone.argtypes = [POINTER(MmsValue)]
    MmsValue_clone.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 782
if _libs["libiec61850.so"].has("MmsValue_cloneToBuffer", "cdecl"):
    MmsValue_cloneToBuffer = _libs["libiec61850.so"].get("MmsValue_cloneToBuffer", "cdecl")
    MmsValue_cloneToBuffer.argtypes = [POINTER(MmsValue), POINTER(uint8_t)]
    MmsValue_cloneToBuffer.restype = POINTER(uint8_t)

# ../libiec61850/src/mms/inc/mms_value.h: 796
if _libs["libiec61850.so"].has("MmsValue_getSizeInMemory", "cdecl"):
    MmsValue_getSizeInMemory = _libs["libiec61850.so"].get("MmsValue_getSizeInMemory", "cdecl")
    MmsValue_getSizeInMemory.argtypes = [POINTER(MmsValue)]
    MmsValue_getSizeInMemory.restype = c_int

# ../libiec61850/src/mms/inc/mms_value.h: 808
if _libs["libiec61850.so"].has("MmsValue_delete", "cdecl"):
    MmsValue_delete = _libs["libiec61850.so"].get("MmsValue_delete", "cdecl")
    MmsValue_delete.argtypes = [POINTER(MmsValue)]
    MmsValue_delete.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 823
if _libs["libiec61850.so"].has("MmsValue_deleteConditional", "cdecl"):
    MmsValue_deleteConditional = _libs["libiec61850.so"].get("MmsValue_deleteConditional", "cdecl")
    MmsValue_deleteConditional.argtypes = [POINTER(MmsValue)]
    MmsValue_deleteConditional.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 835
if _libs["libiec61850.so"].has("MmsValue_newVisibleString", "cdecl"):
    MmsValue_newVisibleString = _libs["libiec61850.so"].get("MmsValue_newVisibleString", "cdecl")
    MmsValue_newVisibleString.argtypes = [String]
    MmsValue_newVisibleString.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 849
if _libs["libiec61850.so"].has("MmsValue_newVisibleStringWithSize", "cdecl"):
    MmsValue_newVisibleStringWithSize = _libs["libiec61850.so"].get("MmsValue_newVisibleStringWithSize", "cdecl")
    MmsValue_newVisibleStringWithSize.argtypes = [c_int]
    MmsValue_newVisibleStringWithSize.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 863
if _libs["libiec61850.so"].has("MmsValue_newMmsStringWithSize", "cdecl"):
    MmsValue_newMmsStringWithSize = _libs["libiec61850.so"].get("MmsValue_newMmsStringWithSize", "cdecl")
    MmsValue_newMmsStringWithSize.argtypes = [c_int]
    MmsValue_newMmsStringWithSize.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 877
if _libs["libiec61850.so"].has("MmsValue_newBinaryTime", "cdecl"):
    MmsValue_newBinaryTime = _libs["libiec61850.so"].get("MmsValue_newBinaryTime", "cdecl")
    MmsValue_newBinaryTime.argtypes = [c_bool]
    MmsValue_newBinaryTime.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 888
if _libs["libiec61850.so"].has("MmsValue_newVisibleStringFromByteArray", "cdecl"):
    MmsValue_newVisibleStringFromByteArray = _libs["libiec61850.so"].get("MmsValue_newVisibleStringFromByteArray", "cdecl")
    MmsValue_newVisibleStringFromByteArray.argtypes = [POINTER(uint8_t), c_int]
    MmsValue_newVisibleStringFromByteArray.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 899
if _libs["libiec61850.so"].has("MmsValue_newMmsStringFromByteArray", "cdecl"):
    MmsValue_newMmsStringFromByteArray = _libs["libiec61850.so"].get("MmsValue_newMmsStringFromByteArray", "cdecl")
    MmsValue_newMmsStringFromByteArray.argtypes = [POINTER(uint8_t), c_int]
    MmsValue_newMmsStringFromByteArray.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 909
if _libs["libiec61850.so"].has("MmsValue_newMmsString", "cdecl"):
    MmsValue_newMmsString = _libs["libiec61850.so"].get("MmsValue_newMmsString", "cdecl")
    MmsValue_newMmsString.argtypes = [String]
    MmsValue_newMmsString.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 918
if _libs["libiec61850.so"].has("MmsValue_setMmsString", "cdecl"):
    MmsValue_setMmsString = _libs["libiec61850.so"].get("MmsValue_setMmsString", "cdecl")
    MmsValue_setMmsString.argtypes = [POINTER(MmsValue), String]
    MmsValue_setMmsString.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 927
if _libs["libiec61850.so"].has("MmsValue_newUtcTime", "cdecl"):
    MmsValue_newUtcTime = _libs["libiec61850.so"].get("MmsValue_newUtcTime", "cdecl")
    MmsValue_newUtcTime.argtypes = [uint32_t]
    MmsValue_newUtcTime.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 937
if _libs["libiec61850.so"].has("MmsValue_newUtcTimeByMsTime", "cdecl"):
    MmsValue_newUtcTimeByMsTime = _libs["libiec61850.so"].get("MmsValue_newUtcTimeByMsTime", "cdecl")
    MmsValue_newUtcTimeByMsTime.argtypes = [uint64_t]
    MmsValue_newUtcTimeByMsTime.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 942
if _libs["libiec61850.so"].has("MmsValue_setDeletable", "cdecl"):
    MmsValue_setDeletable = _libs["libiec61850.so"].get("MmsValue_setDeletable", "cdecl")
    MmsValue_setDeletable.argtypes = [POINTER(MmsValue)]
    MmsValue_setDeletable.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 945
if _libs["libiec61850.so"].has("MmsValue_setDeletableRecursive", "cdecl"):
    MmsValue_setDeletableRecursive = _libs["libiec61850.so"].get("MmsValue_setDeletableRecursive", "cdecl")
    MmsValue_setDeletableRecursive.argtypes = [POINTER(MmsValue)]
    MmsValue_setDeletableRecursive.restype = None

# ../libiec61850/src/mms/inc/mms_value.h: 959
if _libs["libiec61850.so"].has("MmsValue_isDeletable", "cdecl"):
    MmsValue_isDeletable = _libs["libiec61850.so"].get("MmsValue_isDeletable", "cdecl")
    MmsValue_isDeletable.argtypes = [POINTER(MmsValue)]
    MmsValue_isDeletable.restype = c_int

# ../libiec61850/src/mms/inc/mms_value.h: 967
if _libs["libiec61850.so"].has("MmsValue_getType", "cdecl"):
    MmsValue_getType = _libs["libiec61850.so"].get("MmsValue_getType", "cdecl")
    MmsValue_getType.argtypes = [POINTER(MmsValue)]
    MmsValue_getType.restype = MmsType

# ../libiec61850/src/mms/inc/mms_value.h: 978
if _libs["libiec61850.so"].has("MmsValue_getSubElement", "cdecl"):
    MmsValue_getSubElement = _libs["libiec61850.so"].get("MmsValue_getSubElement", "cdecl")
    MmsValue_getSubElement.argtypes = [POINTER(MmsValue), POINTER(MmsVariableSpecification), String]
    MmsValue_getSubElement.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 988
if _libs["libiec61850.so"].has("MmsValue_getTypeString", "cdecl"):
    MmsValue_getTypeString = _libs["libiec61850.so"].get("MmsValue_getTypeString", "cdecl")
    MmsValue_getTypeString.argtypes = [POINTER(MmsValue)]
    if sizeof(c_int) == sizeof(c_void_p):
        MmsValue_getTypeString.restype = ReturnString
    else:
        MmsValue_getTypeString.restype = String
        MmsValue_getTypeString.errcheck = ReturnString

# ../libiec61850/src/mms/inc/mms_value.h: 1003
if _libs["libiec61850.so"].has("MmsValue_printToBuffer", "cdecl"):
    MmsValue_printToBuffer = _libs["libiec61850.so"].get("MmsValue_printToBuffer", "cdecl")
    MmsValue_printToBuffer.argtypes = [POINTER(MmsValue), String, c_int]
    MmsValue_printToBuffer.restype = c_char_p

# ../libiec61850/src/mms/inc/mms_value.h: 1018
if _libs["libiec61850.so"].has("MmsValue_decodeMmsData", "cdecl"):
    MmsValue_decodeMmsData = _libs["libiec61850.so"].get("MmsValue_decodeMmsData", "cdecl")
    MmsValue_decodeMmsData.argtypes = [POINTER(uint8_t), c_int, c_int, POINTER(c_int)]
    MmsValue_decodeMmsData.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 1032
if _libs["libiec61850.so"].has("MmsValue_decodeMmsDataMaxRecursion", "cdecl"):
    MmsValue_decodeMmsDataMaxRecursion = _libs["libiec61850.so"].get("MmsValue_decodeMmsDataMaxRecursion", "cdecl")
    MmsValue_decodeMmsDataMaxRecursion.argtypes = [POINTER(uint8_t), c_int, c_int, POINTER(c_int), c_int]
    MmsValue_decodeMmsDataMaxRecursion.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_value.h: 1047
if _libs["libiec61850.so"].has("MmsValue_encodeMmsData", "cdecl"):
    MmsValue_encodeMmsData = _libs["libiec61850.so"].get("MmsValue_encodeMmsData", "cdecl")
    MmsValue_encodeMmsData.argtypes = [POINTER(MmsValue), POINTER(uint8_t), c_int, c_bool]
    MmsValue_encodeMmsData.restype = c_int

# ../libiec61850/src/mms/inc/mms_value.h: 1057
if _libs["libiec61850.so"].has("MmsValue_getMaxEncodedSize", "cdecl"):
    MmsValue_getMaxEncodedSize = _libs["libiec61850.so"].get("MmsValue_getMaxEncodedSize", "cdecl")
    MmsValue_getMaxEncodedSize.argtypes = [POINTER(MmsValue)]
    MmsValue_getMaxEncodedSize.restype = c_int

# ../libiec61850/src/mms/inc/mms_value.h: 1065
if _libs["libiec61850.so"].has("MmsVariableSpecification_getMaxEncodedSize", "cdecl"):
    MmsVariableSpecification_getMaxEncodedSize = _libs["libiec61850.so"].get("MmsVariableSpecification_getMaxEncodedSize", "cdecl")
    MmsVariableSpecification_getMaxEncodedSize.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getMaxEncodedSize.restype = c_int

# ../libiec61850/src/logging/logging_api.h: 78
class struct_sLogStorage(Structure):
    pass

LogStorage = POINTER(struct_sLogStorage)# ../libiec61850/src/logging/logging_api.h: 50

LogEntryCallback = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), uint64_t, uint64_t, c_bool)# ../libiec61850/src/logging/logging_api.h: 62

LogEntryDataCallback = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), String, POINTER(uint8_t), c_int, uint8_t, c_bool)# ../libiec61850/src/logging/logging_api.h: 76

struct_sLogStorage.__slots__ = [
    'instanceData',
    'maxLogEntries',
    'addEntry',
    'addEntryData',
    'getEntries',
    'getEntriesAfter',
    'getOldestAndNewestEntries',
    'destroy',
]
struct_sLogStorage._fields_ = [
    ('instanceData', POINTER(None)),
    ('maxLogEntries', c_int),
    ('addEntry', CFUNCTYPE(UNCHECKED(uint64_t), LogStorage, uint64_t)),
    ('addEntryData', CFUNCTYPE(UNCHECKED(c_bool), LogStorage, uint64_t, String, POINTER(uint8_t), c_int, uint8_t)),
    ('getEntries', CFUNCTYPE(UNCHECKED(c_bool), LogStorage, uint64_t, uint64_t, LogEntryCallback, LogEntryDataCallback, POINTER(None))),
    ('getEntriesAfter', CFUNCTYPE(UNCHECKED(c_bool), LogStorage, uint64_t, uint64_t, LogEntryCallback, LogEntryDataCallback, POINTER(None))),
    ('getOldestAndNewestEntries', CFUNCTYPE(UNCHECKED(c_bool), LogStorage, POINTER(uint64_t), POINTER(uint64_t), POINTER(uint64_t), POINTER(uint64_t))),
    ('destroy', CFUNCTYPE(UNCHECKED(None), LogStorage)),
]

# ../libiec61850/src/logging/logging_api.h: 108
if _libs["libiec61850.so"].has("LogStorage_setMaxLogEntries", "cdecl"):
    LogStorage_setMaxLogEntries = _libs["libiec61850.so"].get("LogStorage_setMaxLogEntries", "cdecl")
    LogStorage_setMaxLogEntries.argtypes = [LogStorage, c_int]
    LogStorage_setMaxLogEntries.restype = None

# ../libiec61850/src/logging/logging_api.h: 118
if _libs["libiec61850.so"].has("LogStorage_getMaxLogEntries", "cdecl"):
    LogStorage_getMaxLogEntries = _libs["libiec61850.so"].get("LogStorage_getMaxLogEntries", "cdecl")
    LogStorage_getMaxLogEntries.argtypes = [LogStorage]
    LogStorage_getMaxLogEntries.restype = c_int

# ../libiec61850/src/logging/logging_api.h: 129
if _libs["libiec61850.so"].has("LogStorage_addEntry", "cdecl"):
    LogStorage_addEntry = _libs["libiec61850.so"].get("LogStorage_addEntry", "cdecl")
    LogStorage_addEntry.argtypes = [LogStorage, uint64_t]
    LogStorage_addEntry.restype = uint64_t

# ../libiec61850/src/logging/logging_api.h: 144
if _libs["libiec61850.so"].has("LogStorage_addEntryData", "cdecl"):
    LogStorage_addEntryData = _libs["libiec61850.so"].get("LogStorage_addEntryData", "cdecl")
    LogStorage_addEntryData.argtypes = [LogStorage, uint64_t, String, POINTER(uint8_t), c_int, uint8_t]
    LogStorage_addEntryData.restype = c_bool

# ../libiec61850/src/logging/logging_api.h: 159
if _libs["libiec61850.so"].has("LogStorage_getEntries", "cdecl"):
    LogStorage_getEntries = _libs["libiec61850.so"].get("LogStorage_getEntries", "cdecl")
    LogStorage_getEntries.argtypes = [LogStorage, uint64_t, uint64_t, LogEntryCallback, LogEntryDataCallback, POINTER(None)]
    LogStorage_getEntries.restype = c_bool

# ../libiec61850/src/logging/logging_api.h: 178
if _libs["libiec61850.so"].has("LogStorage_getEntriesAfter", "cdecl"):
    LogStorage_getEntriesAfter = _libs["libiec61850.so"].get("LogStorage_getEntriesAfter", "cdecl")
    LogStorage_getEntriesAfter.argtypes = [LogStorage, uint64_t, uint64_t, LogEntryCallback, LogEntryDataCallback, POINTER(None)]
    LogStorage_getEntriesAfter.restype = c_bool

# ../libiec61850/src/logging/logging_api.h: 194
if _libs["libiec61850.so"].has("LogStorage_getOldestAndNewestEntries", "cdecl"):
    LogStorage_getOldestAndNewestEntries = _libs["libiec61850.so"].get("LogStorage_getOldestAndNewestEntries", "cdecl")
    LogStorage_getOldestAndNewestEntries.argtypes = [LogStorage, POINTER(uint64_t), POINTER(uint64_t), POINTER(uint64_t), POINTER(uint64_t)]
    LogStorage_getOldestAndNewestEntries.restype = c_bool

# ../libiec61850/src/logging/logging_api.h: 203
if _libs["libiec61850.so"].has("LogStorage_destroy", "cdecl"):
    LogStorage_destroy = _libs["libiec61850.so"].get("LogStorage_destroy", "cdecl")
    LogStorage_destroy.argtypes = [LogStorage]
    LogStorage_destroy.restype = None

# ../libiec61850/src/common/inc/linked_list.h: 44
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

LinkedList = POINTER(struct_sLinkedList)# ../libiec61850/src/common/inc/linked_list.h: 52

# ../libiec61850/src/common/inc/linked_list.h: 60
if _libs["libiec61850.so"].has("LinkedList_create", "cdecl"):
    LinkedList_create = _libs["libiec61850.so"].get("LinkedList_create", "cdecl")
    LinkedList_create.argtypes = []
    LinkedList_create.restype = LinkedList

# ../libiec61850/src/common/inc/linked_list.h: 72
if _libs["libiec61850.so"].has("LinkedList_destroy", "cdecl"):
    LinkedList_destroy = _libs["libiec61850.so"].get("LinkedList_destroy", "cdecl")
    LinkedList_destroy.argtypes = [LinkedList]
    LinkedList_destroy.restype = None

LinkedListValueDeleteFunction = CFUNCTYPE(UNCHECKED(None), POINTER(None))# ../libiec61850/src/common/inc/linked_list.h: 75

# ../libiec61850/src/common/inc/linked_list.h: 89
if _libs["libiec61850.so"].has("LinkedList_destroyDeep", "cdecl"):
    LinkedList_destroyDeep = _libs["libiec61850.so"].get("LinkedList_destroyDeep", "cdecl")
    LinkedList_destroyDeep.argtypes = [LinkedList, LinkedListValueDeleteFunction]
    LinkedList_destroyDeep.restype = None

# ../libiec61850/src/common/inc/linked_list.h: 100
if _libs["libiec61850.so"].has("LinkedList_destroyStatic", "cdecl"):
    LinkedList_destroyStatic = _libs["libiec61850.so"].get("LinkedList_destroyStatic", "cdecl")
    LinkedList_destroyStatic.argtypes = [LinkedList]
    LinkedList_destroyStatic.restype = None

# ../libiec61850/src/common/inc/linked_list.h: 112
if _libs["libiec61850.so"].has("LinkedList_add", "cdecl"):
    LinkedList_add = _libs["libiec61850.so"].get("LinkedList_add", "cdecl")
    LinkedList_add.argtypes = [LinkedList, POINTER(None)]
    LinkedList_add.restype = None

# ../libiec61850/src/common/inc/linked_list.h: 123
if _libs["libiec61850.so"].has("LinkedList_contains", "cdecl"):
    LinkedList_contains = _libs["libiec61850.so"].get("LinkedList_contains", "cdecl")
    LinkedList_contains.argtypes = [LinkedList, POINTER(None)]
    LinkedList_contains.restype = c_bool

# ../libiec61850/src/common/inc/linked_list.h: 134
if _libs["libiec61850.so"].has("LinkedList_remove", "cdecl"):
    LinkedList_remove = _libs["libiec61850.so"].get("LinkedList_remove", "cdecl")
    LinkedList_remove.argtypes = [LinkedList, POINTER(None)]
    LinkedList_remove.restype = c_bool

# ../libiec61850/src/common/inc/linked_list.h: 143
if _libs["libiec61850.so"].has("LinkedList_get", "cdecl"):
    LinkedList_get = _libs["libiec61850.so"].get("LinkedList_get", "cdecl")
    LinkedList_get.argtypes = [LinkedList, c_int]
    LinkedList_get.restype = LinkedList

# ../libiec61850/src/common/inc/linked_list.h: 151
if _libs["libiec61850.so"].has("LinkedList_getNext", "cdecl"):
    LinkedList_getNext = _libs["libiec61850.so"].get("LinkedList_getNext", "cdecl")
    LinkedList_getNext.argtypes = [LinkedList]
    LinkedList_getNext.restype = LinkedList

# ../libiec61850/src/common/inc/linked_list.h: 159
if _libs["libiec61850.so"].has("LinkedList_getLastElement", "cdecl"):
    LinkedList_getLastElement = _libs["libiec61850.so"].get("LinkedList_getLastElement", "cdecl")
    LinkedList_getLastElement.argtypes = [LinkedList]
    LinkedList_getLastElement.restype = LinkedList

# ../libiec61850/src/common/inc/linked_list.h: 167
if _libs["libiec61850.so"].has("LinkedList_insertAfter", "cdecl"):
    LinkedList_insertAfter = _libs["libiec61850.so"].get("LinkedList_insertAfter", "cdecl")
    LinkedList_insertAfter.argtypes = [LinkedList, POINTER(None)]
    LinkedList_insertAfter.restype = LinkedList

# ../libiec61850/src/common/inc/linked_list.h: 177
if _libs["libiec61850.so"].has("LinkedList_size", "cdecl"):
    LinkedList_size = _libs["libiec61850.so"].get("LinkedList_size", "cdecl")
    LinkedList_size.argtypes = [LinkedList]
    LinkedList_size.restype = c_int

# ../libiec61850/src/common/inc/linked_list.h: 179
if _libs["libiec61850.so"].has("LinkedList_getData", "cdecl"):
    LinkedList_getData = _libs["libiec61850.so"].get("LinkedList_getData", "cdecl")
    LinkedList_getData.argtypes = [LinkedList]
    LinkedList_getData.restype = POINTER(c_ubyte)
    LinkedList_getData.errcheck = lambda v,*a : cast(v, c_void_p)

# ../libiec61850/src/common/inc/linked_list.h: 183
if _libs["libiec61850.so"].has("LinkedList_printStringList", "cdecl"):
    LinkedList_printStringList = _libs["libiec61850.so"].get("LinkedList_printStringList", "cdecl")
    LinkedList_printStringList.argtypes = [LinkedList]
    LinkedList_printStringList.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 56
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'vlanPriority',
    'vlanId',
    'appId',
    'dstAddress',
]
struct_anon_25._fields_ = [
    ('vlanPriority', uint8_t),
    ('vlanId', uint16_t),
    ('appId', uint16_t),
    ('dstAddress', uint8_t * int(6)),
]

PhyComAddress = struct_anon_25# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 56

enum_anon_26 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 71

ACSI_CLASS_DATA_OBJECT = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 71

ACSI_CLASS_DATA_SET = (ACSI_CLASS_DATA_OBJECT + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 71

ACSI_CLASS_BRCB = (ACSI_CLASS_DATA_SET + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 71

ACSI_CLASS_URCB = (ACSI_CLASS_BRCB + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 71

ACSI_CLASS_LCB = (ACSI_CLASS_URCB + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 71

ACSI_CLASS_LOG = (ACSI_CLASS_LCB + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 71

ACSI_CLASS_SGCB = (ACSI_CLASS_LOG + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 71

ACSI_CLASS_GoCB = (ACSI_CLASS_SGCB + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 71

ACSI_CLASS_GsCB = (ACSI_CLASS_GoCB + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 71

ACSI_CLASS_MSVCB = (ACSI_CLASS_GsCB + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 71

ACSI_CLASS_USVCB = (ACSI_CLASS_MSVCB + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 71

ACSIClass = enum_anon_26# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 71

enum_anon_27 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 103

CONTROL_MODEL_STATUS_ONLY = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 103

CONTROL_MODEL_DIRECT_NORMAL = 1# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 103

CONTROL_MODEL_SBO_NORMAL = 2# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 103

CONTROL_MODEL_DIRECT_ENHANCED = 3# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 103

CONTROL_MODEL_SBO_ENHANCED = 4# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 103

ControlModel = enum_anon_27# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 103

enum_anon_28 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_UNKNOWN = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_NOT_SUPPORTED = 1# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_BLOCKED_BY_SWITCHING_HIERARCHY = 2# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_SELECT_FAILED = 3# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_INVALID_POSITION = 4# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_POSITION_REACHED = 5# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_PARAMETER_CHANGE_IN_EXECUTION = 6# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_STEP_LIMIT = 7# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_BLOCKED_BY_MODE = 8# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_BLOCKED_BY_PROCESS = 9# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_BLOCKED_BY_INTERLOCKING = 10# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_BLOCKED_BY_SYNCHROCHECK = 11# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_COMMAND_ALREADY_IN_EXECUTION = 12# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_BLOCKED_BY_HEALTH = 13# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_1_OF_N_CONTROL = 14# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_ABORTION_BY_CANCEL = 15# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_TIME_LIMIT_OVER = 16# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_ABORTION_BY_TRIP = 17# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_OBJECT_NOT_SELECTED = 18# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_OBJECT_ALREADY_SELECTED = 19# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_NO_ACCESS_AUTHORITY = 20# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_ENDED_WITH_OVERSHOOT = 21# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_ABORTION_DUE_TO_DEVIATION = 22# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_ABORTION_BY_COMMUNICATION_LOSS = 23# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_ABORTION_BY_COMMAND = 24# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_NONE = 25# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_INCONSISTENT_PARAMETERS = 26# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ADD_CAUSE_LOCKED_BY_OTHER_CLIENT = 27# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

ControlAddCause = enum_anon_28# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 234

enum_anon_29 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 249

CONTROL_ERROR_NO_ERROR = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 249

CONTROL_ERROR_UNKNOWN = 1# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 249

CONTROL_ERROR_TIMEOUT_TEST = 2# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 249

CONTROL_ERROR_OPERATOR_TEST = 3# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 249

ControlLastApplError = enum_anon_29# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 249

enum_eFunctionalConstraint = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_ST = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_MX = 1# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_SP = 2# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_SV = 3# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_CF = 4# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_DC = 5# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_SG = 6# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_SE = 7# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_SR = 8# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_OR = 9# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_BL = 10# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_EX = 11# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_CO = 12# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_US = 13# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_MS = 14# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_RP = 15# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_BR = 16# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_LG = 17# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_GO = 18# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_ALL = 99# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

IEC61850_FC_NONE = (-1)# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

FunctionalConstraint = enum_eFunctionalConstraint# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 303

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 308
if _libs["libiec61850.so"].has("FunctionalConstraint_toString", "cdecl"):
    FunctionalConstraint_toString = _libs["libiec61850.so"].get("FunctionalConstraint_toString", "cdecl")
    FunctionalConstraint_toString.argtypes = [FunctionalConstraint]
    if sizeof(c_int) == sizeof(c_void_p):
        FunctionalConstraint_toString.restype = ReturnString
    else:
        FunctionalConstraint_toString.restype = String
        FunctionalConstraint_toString.errcheck = ReturnString

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 315
if _libs["libiec61850.so"].has("FunctionalConstraint_fromString", "cdecl"):
    FunctionalConstraint_fromString = _libs["libiec61850.so"].get("FunctionalConstraint_fromString", "cdecl")
    FunctionalConstraint_fromString.argtypes = [String]
    FunctionalConstraint_fromString.restype = FunctionalConstraint

Quality = uint16_t# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 326

Validity = uint16_t# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 327

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 352
if _libs["libiec61850.so"].has("Quality_getValidity", "cdecl"):
    Quality_getValidity = _libs["libiec61850.so"].get("Quality_getValidity", "cdecl")
    Quality_getValidity.argtypes = [POINTER(Quality)]
    Quality_getValidity.restype = Validity

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 355
if _libs["libiec61850.so"].has("Quality_setValidity", "cdecl"):
    Quality_setValidity = _libs["libiec61850.so"].get("Quality_setValidity", "cdecl")
    Quality_setValidity.argtypes = [POINTER(Quality), Validity]
    Quality_setValidity.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 358
if _libs["libiec61850.so"].has("Quality_setFlag", "cdecl"):
    Quality_setFlag = _libs["libiec61850.so"].get("Quality_setFlag", "cdecl")
    Quality_setFlag.argtypes = [POINTER(Quality), c_int]
    Quality_setFlag.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 361
if _libs["libiec61850.so"].has("Quality_unsetFlag", "cdecl"):
    Quality_unsetFlag = _libs["libiec61850.so"].get("Quality_unsetFlag", "cdecl")
    Quality_unsetFlag.argtypes = [POINTER(Quality), c_int]
    Quality_unsetFlag.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 364
if _libs["libiec61850.so"].has("Quality_isFlagSet", "cdecl"):
    Quality_isFlagSet = _libs["libiec61850.so"].get("Quality_isFlagSet", "cdecl")
    Quality_isFlagSet.argtypes = [POINTER(Quality), c_int]
    Quality_isFlagSet.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 367
if _libs["libiec61850.so"].has("Quality_fromMmsValue", "cdecl"):
    Quality_fromMmsValue = _libs["libiec61850.so"].get("Quality_fromMmsValue", "cdecl")
    Quality_fromMmsValue.argtypes = [POINTER(MmsValue)]
    Quality_fromMmsValue.restype = Quality

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 369
if _libs["libiec61850.so"].has("Quality_toMmsValue", "cdecl"):
    Quality_toMmsValue = _libs["libiec61850.so"].get("Quality_toMmsValue", "cdecl")
    Quality_toMmsValue.argtypes = [POINTER(Quality), POINTER(MmsValue)]
    Quality_toMmsValue.restype = POINTER(MmsValue)

enum_anon_30 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 385

DBPOS_INTERMEDIATE_STATE = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 385

DBPOS_OFF = 1# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 385

DBPOS_ON = 2# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 385

DBPOS_BAD_STATE = 3# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 385

Dbpos = enum_anon_30# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 385

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 396
if _libs["libiec61850.so"].has("Dbpos_fromMmsValue", "cdecl"):
    Dbpos_fromMmsValue = _libs["libiec61850.so"].get("Dbpos_fromMmsValue", "cdecl")
    Dbpos_fromMmsValue.argtypes = [POINTER(MmsValue)]
    Dbpos_fromMmsValue.restype = Dbpos

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 406
if _libs["libiec61850.so"].has("Dbpos_toMmsValue", "cdecl"):
    Dbpos_toMmsValue = _libs["libiec61850.so"].get("Dbpos_toMmsValue", "cdecl")
    Dbpos_toMmsValue.argtypes = [POINTER(MmsValue), Dbpos]
    Dbpos_toMmsValue.restype = POINTER(MmsValue)

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 419
class union_anon_31(Union):
    pass

union_anon_31.__slots__ = [
    'val',
]
union_anon_31._fields_ = [
    ('val', uint8_t * int(8)),
]

Timestamp = union_anon_31# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 419

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 421
if _libs["libiec61850.so"].has("Timestamp_create", "cdecl"):
    Timestamp_create = _libs["libiec61850.so"].get("Timestamp_create", "cdecl")
    Timestamp_create.argtypes = []
    Timestamp_create.restype = POINTER(Timestamp)

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 424
if _libs["libiec61850.so"].has("Timestamp_createFromByteArray", "cdecl"):
    Timestamp_createFromByteArray = _libs["libiec61850.so"].get("Timestamp_createFromByteArray", "cdecl")
    Timestamp_createFromByteArray.argtypes = [POINTER(uint8_t)]
    Timestamp_createFromByteArray.restype = POINTER(Timestamp)

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 428
if _libs["libiec61850.so"].has("Timestamp_destroy", "cdecl"):
    Timestamp_destroy = _libs["libiec61850.so"].get("Timestamp_destroy", "cdecl")
    Timestamp_destroy.argtypes = [POINTER(Timestamp)]
    Timestamp_destroy.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 431
if _libs["libiec61850.so"].has("Timestamp_clearFlags", "cdecl"):
    Timestamp_clearFlags = _libs["libiec61850.so"].get("Timestamp_clearFlags", "cdecl")
    Timestamp_clearFlags.argtypes = [POINTER(Timestamp)]
    Timestamp_clearFlags.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 434
if _libs["libiec61850.so"].has("Timestamp_getTimeInSeconds", "cdecl"):
    Timestamp_getTimeInSeconds = _libs["libiec61850.so"].get("Timestamp_getTimeInSeconds", "cdecl")
    Timestamp_getTimeInSeconds.argtypes = [POINTER(Timestamp)]
    Timestamp_getTimeInSeconds.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 437
if _libs["libiec61850.so"].has("Timestamp_getTimeInMs", "cdecl"):
    Timestamp_getTimeInMs = _libs["libiec61850.so"].get("Timestamp_getTimeInMs", "cdecl")
    Timestamp_getTimeInMs.argtypes = [POINTER(Timestamp)]
    Timestamp_getTimeInMs.restype = msSinceEpoch

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 440
if _libs["libiec61850.so"].has("Timestamp_getTimeInNs", "cdecl"):
    Timestamp_getTimeInNs = _libs["libiec61850.so"].get("Timestamp_getTimeInNs", "cdecl")
    Timestamp_getTimeInNs.argtypes = [POINTER(Timestamp)]
    Timestamp_getTimeInNs.restype = nsSinceEpoch

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 443
if _libs["libiec61850.so"].has("Timestamp_isLeapSecondKnown", "cdecl"):
    Timestamp_isLeapSecondKnown = _libs["libiec61850.so"].get("Timestamp_isLeapSecondKnown", "cdecl")
    Timestamp_isLeapSecondKnown.argtypes = [POINTER(Timestamp)]
    Timestamp_isLeapSecondKnown.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 446
if _libs["libiec61850.so"].has("Timestamp_setLeapSecondKnown", "cdecl"):
    Timestamp_setLeapSecondKnown = _libs["libiec61850.so"].get("Timestamp_setLeapSecondKnown", "cdecl")
    Timestamp_setLeapSecondKnown.argtypes = [POINTER(Timestamp), c_bool]
    Timestamp_setLeapSecondKnown.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 449
if _libs["libiec61850.so"].has("Timestamp_hasClockFailure", "cdecl"):
    Timestamp_hasClockFailure = _libs["libiec61850.so"].get("Timestamp_hasClockFailure", "cdecl")
    Timestamp_hasClockFailure.argtypes = [POINTER(Timestamp)]
    Timestamp_hasClockFailure.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 452
if _libs["libiec61850.so"].has("Timestamp_setClockFailure", "cdecl"):
    Timestamp_setClockFailure = _libs["libiec61850.so"].get("Timestamp_setClockFailure", "cdecl")
    Timestamp_setClockFailure.argtypes = [POINTER(Timestamp), c_bool]
    Timestamp_setClockFailure.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 455
if _libs["libiec61850.so"].has("Timestamp_isClockNotSynchronized", "cdecl"):
    Timestamp_isClockNotSynchronized = _libs["libiec61850.so"].get("Timestamp_isClockNotSynchronized", "cdecl")
    Timestamp_isClockNotSynchronized.argtypes = [POINTER(Timestamp)]
    Timestamp_isClockNotSynchronized.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 458
if _libs["libiec61850.so"].has("Timestamp_setClockNotSynchronized", "cdecl"):
    Timestamp_setClockNotSynchronized = _libs["libiec61850.so"].get("Timestamp_setClockNotSynchronized", "cdecl")
    Timestamp_setClockNotSynchronized.argtypes = [POINTER(Timestamp), c_bool]
    Timestamp_setClockNotSynchronized.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 461
if _libs["libiec61850.so"].has("Timestamp_getSubsecondPrecision", "cdecl"):
    Timestamp_getSubsecondPrecision = _libs["libiec61850.so"].get("Timestamp_getSubsecondPrecision", "cdecl")
    Timestamp_getSubsecondPrecision.argtypes = [POINTER(Timestamp)]
    Timestamp_getSubsecondPrecision.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 464
if _libs["libiec61850.so"].has("Timestamp_setFractionOfSecondPart", "cdecl"):
    Timestamp_setFractionOfSecondPart = _libs["libiec61850.so"].get("Timestamp_setFractionOfSecondPart", "cdecl")
    Timestamp_setFractionOfSecondPart.argtypes = [POINTER(Timestamp), uint32_t]
    Timestamp_setFractionOfSecondPart.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 467
if _libs["libiec61850.so"].has("Timestamp_getFractionOfSecondPart", "cdecl"):
    Timestamp_getFractionOfSecondPart = _libs["libiec61850.so"].get("Timestamp_getFractionOfSecondPart", "cdecl")
    Timestamp_getFractionOfSecondPart.argtypes = [POINTER(Timestamp)]
    Timestamp_getFractionOfSecondPart.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 470
if _libs["libiec61850.so"].has("Timestamp_getFractionOfSecond", "cdecl"):
    Timestamp_getFractionOfSecond = _libs["libiec61850.so"].get("Timestamp_getFractionOfSecond", "cdecl")
    Timestamp_getFractionOfSecond.argtypes = [POINTER(Timestamp)]
    Timestamp_getFractionOfSecond.restype = c_float

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 478
if _libs["libiec61850.so"].has("Timestamp_setSubsecondPrecision", "cdecl"):
    Timestamp_setSubsecondPrecision = _libs["libiec61850.so"].get("Timestamp_setSubsecondPrecision", "cdecl")
    Timestamp_setSubsecondPrecision.argtypes = [POINTER(Timestamp), c_int]
    Timestamp_setSubsecondPrecision.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 490
if _libs["libiec61850.so"].has("Timestamp_setTimeInSeconds", "cdecl"):
    Timestamp_setTimeInSeconds = _libs["libiec61850.so"].get("Timestamp_setTimeInSeconds", "cdecl")
    Timestamp_setTimeInSeconds.argtypes = [POINTER(Timestamp), uint32_t]
    Timestamp_setTimeInSeconds.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 501
if _libs["libiec61850.so"].has("Timestamp_setTimeInMilliseconds", "cdecl"):
    Timestamp_setTimeInMilliseconds = _libs["libiec61850.so"].get("Timestamp_setTimeInMilliseconds", "cdecl")
    Timestamp_setTimeInMilliseconds.argtypes = [POINTER(Timestamp), msSinceEpoch]
    Timestamp_setTimeInMilliseconds.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 512
if _libs["libiec61850.so"].has("Timestamp_setTimeInNanoseconds", "cdecl"):
    Timestamp_setTimeInNanoseconds = _libs["libiec61850.so"].get("Timestamp_setTimeInNanoseconds", "cdecl")
    Timestamp_setTimeInNanoseconds.argtypes = [POINTER(Timestamp), nsSinceEpoch]
    Timestamp_setTimeInNanoseconds.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 515
if _libs["libiec61850.so"].has("Timestamp_setByMmsUtcTime", "cdecl"):
    Timestamp_setByMmsUtcTime = _libs["libiec61850.so"].get("Timestamp_setByMmsUtcTime", "cdecl")
    Timestamp_setByMmsUtcTime.argtypes = [POINTER(Timestamp), POINTER(MmsValue)]
    Timestamp_setByMmsUtcTime.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 523
if _libs["libiec61850.so"].has("Timestamp_toMmsValue", "cdecl"):
    Timestamp_toMmsValue = _libs["libiec61850.so"].get("Timestamp_toMmsValue", "cdecl")
    Timestamp_toMmsValue.argtypes = [POINTER(Timestamp), POINTER(MmsValue)]
    Timestamp_toMmsValue.restype = POINTER(MmsValue)

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 534
if _libs["libiec61850.so"].has("Timestamp_fromMmsValue", "cdecl"):
    Timestamp_fromMmsValue = _libs["libiec61850.so"].get("Timestamp_fromMmsValue", "cdecl")
    Timestamp_fromMmsValue.argtypes = [POINTER(Timestamp), POINTER(MmsValue)]
    Timestamp_fromMmsValue.restype = POINTER(Timestamp)

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 542
if _libs["libiec61850.so"].has("LibIEC61850_getVersionString", "cdecl"):
    LibIEC61850_getVersionString = _libs["libiec61850.so"].get("LibIEC61850_getVersionString", "cdecl")
    LibIEC61850_getVersionString.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        LibIEC61850_getVersionString.restype = ReturnString
    else:
        LibIEC61850_getVersionString.restype = String
        LibIEC61850_getVersionString.errcheck = ReturnString

# ../libiec61850/src/mms/inc/mms_type_spec.h: 56
if _libs["libiec61850.so"].has("MmsVariableSpecification_destroy", "cdecl"):
    MmsVariableSpecification_destroy = _libs["libiec61850.so"].get("MmsVariableSpecification_destroy", "cdecl")
    MmsVariableSpecification_destroy.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_destroy.restype = None

# ../libiec61850/src/mms/inc/mms_type_spec.h: 71
if _libs["libiec61850.so"].has("MmsVariableSpecification_getChildValue", "cdecl"):
    MmsVariableSpecification_getChildValue = _libs["libiec61850.so"].get("MmsVariableSpecification_getChildValue", "cdecl")
    MmsVariableSpecification_getChildValue.argtypes = [POINTER(MmsVariableSpecification), POINTER(MmsValue), String]
    MmsVariableSpecification_getChildValue.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_type_spec.h: 82
if _libs["libiec61850.so"].has("MmsVariableSpecification_getNamedVariableRecursive", "cdecl"):
    MmsVariableSpecification_getNamedVariableRecursive = _libs["libiec61850.so"].get("MmsVariableSpecification_getNamedVariableRecursive", "cdecl")
    MmsVariableSpecification_getNamedVariableRecursive.argtypes = [POINTER(MmsVariableSpecification), String]
    MmsVariableSpecification_getNamedVariableRecursive.restype = POINTER(MmsVariableSpecification)

# ../libiec61850/src/mms/inc/mms_type_spec.h: 93
if _libs["libiec61850.so"].has("MmsVariableSpecification_getType", "cdecl"):
    MmsVariableSpecification_getType = _libs["libiec61850.so"].get("MmsVariableSpecification_getType", "cdecl")
    MmsVariableSpecification_getType.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getType.restype = MmsType

# ../libiec61850/src/mms/inc/mms_type_spec.h: 104
if _libs["libiec61850.so"].has("MmsVariableSpecification_isValueOfType", "cdecl"):
    MmsVariableSpecification_isValueOfType = _libs["libiec61850.so"].get("MmsVariableSpecification_isValueOfType", "cdecl")
    MmsVariableSpecification_isValueOfType.argtypes = [POINTER(MmsVariableSpecification), POINTER(MmsValue)]
    MmsVariableSpecification_isValueOfType.restype = c_bool

# ../libiec61850/src/mms/inc/mms_type_spec.h: 116
if _libs["libiec61850.so"].has("MmsVariableSpecification_getName", "cdecl"):
    MmsVariableSpecification_getName = _libs["libiec61850.so"].get("MmsVariableSpecification_getName", "cdecl")
    MmsVariableSpecification_getName.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getName.restype = c_char_p

# ../libiec61850/src/mms/inc/mms_type_spec.h: 120
if _libs["libiec61850.so"].has("MmsVariableSpecification_getStructureElements", "cdecl"):
    MmsVariableSpecification_getStructureElements = _libs["libiec61850.so"].get("MmsVariableSpecification_getStructureElements", "cdecl")
    MmsVariableSpecification_getStructureElements.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getStructureElements.restype = LinkedList

# ../libiec61850/src/mms/inc/mms_type_spec.h: 133
if _libs["libiec61850.so"].has("MmsVariableSpecification_getSize", "cdecl"):
    MmsVariableSpecification_getSize = _libs["libiec61850.so"].get("MmsVariableSpecification_getSize", "cdecl")
    MmsVariableSpecification_getSize.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getSize.restype = c_int

# ../libiec61850/src/mms/inc/mms_type_spec.h: 135
if _libs["libiec61850.so"].has("MmsVariableSpecification_getChildSpecificationByIndex", "cdecl"):
    MmsVariableSpecification_getChildSpecificationByIndex = _libs["libiec61850.so"].get("MmsVariableSpecification_getChildSpecificationByIndex", "cdecl")
    MmsVariableSpecification_getChildSpecificationByIndex.argtypes = [POINTER(MmsVariableSpecification), c_int]
    MmsVariableSpecification_getChildSpecificationByIndex.restype = POINTER(MmsVariableSpecification)

# ../libiec61850/src/mms/inc/mms_type_spec.h: 147
if _libs["libiec61850.so"].has("MmsVariableSpecification_getChildSpecificationByName", "cdecl"):
    MmsVariableSpecification_getChildSpecificationByName = _libs["libiec61850.so"].get("MmsVariableSpecification_getChildSpecificationByName", "cdecl")
    MmsVariableSpecification_getChildSpecificationByName.argtypes = [POINTER(MmsVariableSpecification), String, POINTER(c_int)]
    MmsVariableSpecification_getChildSpecificationByName.restype = POINTER(MmsVariableSpecification)

# ../libiec61850/src/mms/inc/mms_type_spec.h: 150
if _libs["libiec61850.so"].has("MmsVariableSpecification_getArrayElementSpecification", "cdecl"):
    MmsVariableSpecification_getArrayElementSpecification = _libs["libiec61850.so"].get("MmsVariableSpecification_getArrayElementSpecification", "cdecl")
    MmsVariableSpecification_getArrayElementSpecification.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getArrayElementSpecification.restype = POINTER(MmsVariableSpecification)

# ../libiec61850/src/mms/inc/mms_type_spec.h: 154
if _libs["libiec61850.so"].has("MmsVariableSpecification_getExponentWidth", "cdecl"):
    MmsVariableSpecification_getExponentWidth = _libs["libiec61850.so"].get("MmsVariableSpecification_getExponentWidth", "cdecl")
    MmsVariableSpecification_getExponentWidth.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getExponentWidth.restype = c_int

# ../libiec61850/hal/inc/tls_config.h: 38
class struct_sTLSConfiguration(Structure):
    pass

TLSConfiguration = POINTER(struct_sTLSConfiguration)# ../libiec61850/hal/inc/tls_config.h: 38

# ../libiec61850/hal/inc/tls_config.h: 48
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_create", "cdecl"):
        continue
    TLSConfiguration_create = _lib.get("TLSConfiguration_create", "cdecl")
    TLSConfiguration_create.argtypes = []
    TLSConfiguration_create.restype = TLSConfiguration
    break

# ../libiec61850/hal/inc/tls_config.h: 52
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setClientMode", "cdecl"):
        continue
    TLSConfiguration_setClientMode = _lib.get("TLSConfiguration_setClientMode", "cdecl")
    TLSConfiguration_setClientMode.argtypes = [TLSConfiguration]
    TLSConfiguration_setClientMode.restype = None
    break

enum_anon_32 = c_int# ../libiec61850/hal/inc/tls_config.h: 61

TLS_VERSION_NOT_SELECTED = 0# ../libiec61850/hal/inc/tls_config.h: 61

TLS_VERSION_SSL_3_0 = 3# ../libiec61850/hal/inc/tls_config.h: 61

TLS_VERSION_TLS_1_0 = 4# ../libiec61850/hal/inc/tls_config.h: 61

TLS_VERSION_TLS_1_1 = 5# ../libiec61850/hal/inc/tls_config.h: 61

TLS_VERSION_TLS_1_2 = 6# ../libiec61850/hal/inc/tls_config.h: 61

TLS_VERSION_TLS_1_3 = 7# ../libiec61850/hal/inc/tls_config.h: 61

TLSConfigVersion = enum_anon_32# ../libiec61850/hal/inc/tls_config.h: 61

# ../libiec61850/hal/inc/tls_config.h: 70
for _lib in _libs.values():
    if not _lib.has("TLSConfigVersion_toString", "cdecl"):
        continue
    TLSConfigVersion_toString = _lib.get("TLSConfigVersion_toString", "cdecl")
    TLSConfigVersion_toString.argtypes = [TLSConfigVersion]
    TLSConfigVersion_toString.restype = c_char_p
    break

enum_anon_33 = c_int# ../libiec61850/hal/inc/tls_config.h: 77

TLS_SEC_EVT_INFO = 0# ../libiec61850/hal/inc/tls_config.h: 77

TLS_SEC_EVT_WARNING = 1# ../libiec61850/hal/inc/tls_config.h: 77

TLS_SEC_EVT_INCIDENT = 2# ../libiec61850/hal/inc/tls_config.h: 77

TLSEventLevel = enum_anon_33# ../libiec61850/hal/inc/tls_config.h: 77

# ../libiec61850/hal/inc/tls_config.h: 96
class struct_sTLSConnection(Structure):
    pass

TLSConnection = POINTER(struct_sTLSConnection)# ../libiec61850/hal/inc/tls_config.h: 96

# ../libiec61850/hal/inc/tls_config.h: 106
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

# ../libiec61850/hal/inc/tls_config.h: 117
for _lib in _libs.values():
    if not _lib.has("TLSConnection_getPeerCertificate", "cdecl"):
        continue
    TLSConnection_getPeerCertificate = _lib.get("TLSConnection_getPeerCertificate", "cdecl")
    TLSConnection_getPeerCertificate.argtypes = [TLSConnection, POINTER(c_int)]
    TLSConnection_getPeerCertificate.restype = POINTER(uint8_t)
    break

# ../libiec61850/hal/inc/tls_config.h: 128
for _lib in _libs.values():
    if not _lib.has("TLSConnection_getTLSVersion", "cdecl"):
        continue
    TLSConnection_getTLSVersion = _lib.get("TLSConnection_getTLSVersion", "cdecl")
    TLSConnection_getTLSVersion.argtypes = [TLSConnection]
    TLSConnection_getTLSVersion.restype = TLSConfigVersion
    break

TLSConfiguration_EventHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), TLSEventLevel, c_int, String, TLSConnection)# ../libiec61850/hal/inc/tls_config.h: 130

# ../libiec61850/hal/inc/tls_config.h: 139
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setEventHandler", "cdecl"):
        continue
    TLSConfiguration_setEventHandler = _lib.get("TLSConfiguration_setEventHandler", "cdecl")
    TLSConfiguration_setEventHandler.argtypes = [TLSConfiguration, TLSConfiguration_EventHandler, POINTER(None)]
    TLSConfiguration_setEventHandler.restype = None
    break

# ../libiec61850/hal/inc/tls_config.h: 150
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_enableSessionResumption", "cdecl"):
        continue
    TLSConfiguration_enableSessionResumption = _lib.get("TLSConfiguration_enableSessionResumption", "cdecl")
    TLSConfiguration_enableSessionResumption.argtypes = [TLSConfiguration, c_bool]
    TLSConfiguration_enableSessionResumption.restype = None
    break

# ../libiec61850/hal/inc/tls_config.h: 158
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setSessionResumptionInterval", "cdecl"):
        continue
    TLSConfiguration_setSessionResumptionInterval = _lib.get("TLSConfiguration_setSessionResumptionInterval", "cdecl")
    TLSConfiguration_setSessionResumptionInterval.argtypes = [TLSConfiguration, c_int]
    TLSConfiguration_setSessionResumptionInterval.restype = None
    break

# ../libiec61850/hal/inc/tls_config.h: 166
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setChainValidation", "cdecl"):
        continue
    TLSConfiguration_setChainValidation = _lib.get("TLSConfiguration_setChainValidation", "cdecl")
    TLSConfiguration_setChainValidation.argtypes = [TLSConfiguration, c_bool]
    TLSConfiguration_setChainValidation.restype = None
    break

# ../libiec61850/hal/inc/tls_config.h: 177
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setAllowOnlyKnownCertificates", "cdecl"):
        continue
    TLSConfiguration_setAllowOnlyKnownCertificates = _lib.get("TLSConfiguration_setAllowOnlyKnownCertificates", "cdecl")
    TLSConfiguration_setAllowOnlyKnownCertificates.argtypes = [TLSConfiguration, c_bool]
    TLSConfiguration_setAllowOnlyKnownCertificates.restype = None
    break

# ../libiec61850/hal/inc/tls_config.h: 188
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setOwnCertificate", "cdecl"):
        continue
    TLSConfiguration_setOwnCertificate = _lib.get("TLSConfiguration_setOwnCertificate", "cdecl")
    TLSConfiguration_setOwnCertificate.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int]
    TLSConfiguration_setOwnCertificate.restype = c_bool
    break

# ../libiec61850/hal/inc/tls_config.h: 198
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setOwnCertificateFromFile", "cdecl"):
        continue
    TLSConfiguration_setOwnCertificateFromFile = _lib.get("TLSConfiguration_setOwnCertificateFromFile", "cdecl")
    TLSConfiguration_setOwnCertificateFromFile.argtypes = [TLSConfiguration, String]
    TLSConfiguration_setOwnCertificateFromFile.restype = c_bool
    break

# ../libiec61850/hal/inc/tls_config.h: 210
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setOwnKey", "cdecl"):
        continue
    TLSConfiguration_setOwnKey = _lib.get("TLSConfiguration_setOwnKey", "cdecl")
    TLSConfiguration_setOwnKey.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int, String]
    TLSConfiguration_setOwnKey.restype = c_bool
    break

# ../libiec61850/hal/inc/tls_config.h: 221
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setOwnKeyFromFile", "cdecl"):
        continue
    TLSConfiguration_setOwnKeyFromFile = _lib.get("TLSConfiguration_setOwnKeyFromFile", "cdecl")
    TLSConfiguration_setOwnKeyFromFile.argtypes = [TLSConfiguration, String, String]
    TLSConfiguration_setOwnKeyFromFile.restype = c_bool
    break

# ../libiec61850/hal/inc/tls_config.h: 231
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addAllowedCertificate", "cdecl"):
        continue
    TLSConfiguration_addAllowedCertificate = _lib.get("TLSConfiguration_addAllowedCertificate", "cdecl")
    TLSConfiguration_addAllowedCertificate.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int]
    TLSConfiguration_addAllowedCertificate.restype = c_bool
    break

# ../libiec61850/hal/inc/tls_config.h: 240
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addAllowedCertificateFromFile", "cdecl"):
        continue
    TLSConfiguration_addAllowedCertificateFromFile = _lib.get("TLSConfiguration_addAllowedCertificateFromFile", "cdecl")
    TLSConfiguration_addAllowedCertificateFromFile.argtypes = [TLSConfiguration, String]
    TLSConfiguration_addAllowedCertificateFromFile.restype = c_bool
    break

# ../libiec61850/hal/inc/tls_config.h: 250
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCACertificate", "cdecl"):
        continue
    TLSConfiguration_addCACertificate = _lib.get("TLSConfiguration_addCACertificate", "cdecl")
    TLSConfiguration_addCACertificate.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int]
    TLSConfiguration_addCACertificate.restype = c_bool
    break

# ../libiec61850/hal/inc/tls_config.h: 259
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCACertificateFromFile", "cdecl"):
        continue
    TLSConfiguration_addCACertificateFromFile = _lib.get("TLSConfiguration_addCACertificateFromFile", "cdecl")
    TLSConfiguration_addCACertificateFromFile.argtypes = [TLSConfiguration, String]
    TLSConfiguration_addCACertificateFromFile.restype = c_bool
    break

# ../libiec61850/hal/inc/tls_config.h: 269
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setRenegotiationTime", "cdecl"):
        continue
    TLSConfiguration_setRenegotiationTime = _lib.get("TLSConfiguration_setRenegotiationTime", "cdecl")
    TLSConfiguration_setRenegotiationTime.argtypes = [TLSConfiguration, c_int]
    TLSConfiguration_setRenegotiationTime.restype = None
    break

# ../libiec61850/hal/inc/tls_config.h: 275
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setMinTlsVersion", "cdecl"):
        continue
    TLSConfiguration_setMinTlsVersion = _lib.get("TLSConfiguration_setMinTlsVersion", "cdecl")
    TLSConfiguration_setMinTlsVersion.argtypes = [TLSConfiguration, TLSConfigVersion]
    TLSConfiguration_setMinTlsVersion.restype = None
    break

# ../libiec61850/hal/inc/tls_config.h: 281
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setMaxTlsVersion", "cdecl"):
        continue
    TLSConfiguration_setMaxTlsVersion = _lib.get("TLSConfiguration_setMaxTlsVersion", "cdecl")
    TLSConfiguration_setMaxTlsVersion.argtypes = [TLSConfiguration, TLSConfigVersion]
    TLSConfiguration_setMaxTlsVersion.restype = None
    break

# ../libiec61850/hal/inc/tls_config.h: 291
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCRL", "cdecl"):
        continue
    TLSConfiguration_addCRL = _lib.get("TLSConfiguration_addCRL", "cdecl")
    TLSConfiguration_addCRL.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int]
    TLSConfiguration_addCRL.restype = c_bool
    break

# ../libiec61850/hal/inc/tls_config.h: 300
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCRLFromFile", "cdecl"):
        continue
    TLSConfiguration_addCRLFromFile = _lib.get("TLSConfiguration_addCRLFromFile", "cdecl")
    TLSConfiguration_addCRLFromFile.argtypes = [TLSConfiguration, String]
    TLSConfiguration_addCRLFromFile.restype = c_bool
    break

# ../libiec61850/hal/inc/tls_config.h: 306
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_resetCRL", "cdecl"):
        continue
    TLSConfiguration_resetCRL = _lib.get("TLSConfiguration_resetCRL", "cdecl")
    TLSConfiguration_resetCRL.argtypes = [TLSConfiguration]
    TLSConfiguration_resetCRL.restype = None
    break

# ../libiec61850/hal/inc/tls_config.h: 315
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCipherSuite", "cdecl"):
        continue
    TLSConfiguration_addCipherSuite = _lib.get("TLSConfiguration_addCipherSuite", "cdecl")
    TLSConfiguration_addCipherSuite.argtypes = [TLSConfiguration, c_int]
    TLSConfiguration_addCipherSuite.restype = None
    break

# ../libiec61850/hal/inc/tls_config.h: 323
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_clearCipherSuiteList", "cdecl"):
        continue
    TLSConfiguration_clearCipherSuiteList = _lib.get("TLSConfiguration_clearCipherSuiteList", "cdecl")
    TLSConfiguration_clearCipherSuiteList.argtypes = [TLSConfiguration]
    TLSConfiguration_clearCipherSuiteList.restype = None
    break

# ../libiec61850/hal/inc/tls_config.h: 331
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_destroy", "cdecl"):
        continue
    TLSConfiguration_destroy = _lib.get("TLSConfiguration_destroy", "cdecl")
    TLSConfiguration_destroy.argtypes = [TLSConfiguration]
    TLSConfiguration_destroy.restype = None
    break

enum_anon_34 = c_int# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 59

ACSE_AUTH_NONE = 0# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 59

ACSE_AUTH_PASSWORD = 1# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 59

ACSE_AUTH_CERTIFICATE = 2# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 59

ACSE_AUTH_TLS = 3# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 59

AcseAuthenticationMechanism = enum_anon_34# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 59

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 64
class struct_sAcseAuthenticationParameter(Structure):
    pass

AcseAuthenticationParameter = POINTER(struct_sAcseAuthenticationParameter)# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 62

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 70
class struct_anon_35(Structure):
    pass

struct_anon_35.__slots__ = [
    'octetString',
    'passwordLength',
]
struct_anon_35._fields_ = [
    ('octetString', POINTER(uint8_t)),
    ('passwordLength', c_int),
]

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 76
class struct_anon_36(Structure):
    pass

struct_anon_36.__slots__ = [
    'buf',
    'length',
]
struct_anon_36._fields_ = [
    ('buf', POINTER(uint8_t)),
    ('length', c_int),
]

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 68
class union_anon_37(Union):
    pass

union_anon_37.__slots__ = [
    'password',
    'certificate',
]
union_anon_37._fields_ = [
    ('password', struct_anon_35),
    ('certificate', struct_anon_36),
]

struct_sAcseAuthenticationParameter.__slots__ = [
    'mechanism',
    'value',
]
struct_sAcseAuthenticationParameter._fields_ = [
    ('mechanism', AcseAuthenticationMechanism),
    ('value', union_anon_37),
]

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 86
if _libs["libiec61850.so"].has("AcseAuthenticationParameter_create", "cdecl"):
    AcseAuthenticationParameter_create = _libs["libiec61850.so"].get("AcseAuthenticationParameter_create", "cdecl")
    AcseAuthenticationParameter_create.argtypes = []
    AcseAuthenticationParameter_create.restype = AcseAuthenticationParameter

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 89
if _libs["libiec61850.so"].has("AcseAuthenticationParameter_destroy", "cdecl"):
    AcseAuthenticationParameter_destroy = _libs["libiec61850.so"].get("AcseAuthenticationParameter_destroy", "cdecl")
    AcseAuthenticationParameter_destroy.argtypes = [AcseAuthenticationParameter]
    AcseAuthenticationParameter_destroy.restype = None

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 92
if _libs["libiec61850.so"].has("AcseAuthenticationParameter_setAuthMechanism", "cdecl"):
    AcseAuthenticationParameter_setAuthMechanism = _libs["libiec61850.so"].get("AcseAuthenticationParameter_setAuthMechanism", "cdecl")
    AcseAuthenticationParameter_setAuthMechanism.argtypes = [AcseAuthenticationParameter, AcseAuthenticationMechanism]
    AcseAuthenticationParameter_setAuthMechanism.restype = None

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 95
if _libs["libiec61850.so"].has("AcseAuthenticationParameter_setPassword", "cdecl"):
    AcseAuthenticationParameter_setPassword = _libs["libiec61850.so"].get("AcseAuthenticationParameter_setPassword", "cdecl")
    AcseAuthenticationParameter_setPassword.argtypes = [AcseAuthenticationParameter, String]
    AcseAuthenticationParameter_setPassword.restype = None

AcseAuthenticator = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), AcseAuthenticationParameter, POINTER(POINTER(None)), POINTER(IsoApplicationReference))# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 109

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 119
class struct_anon_38(Structure):
    pass

struct_anon_38.__slots__ = [
    'size',
    'value',
]
struct_anon_38._fields_ = [
    ('size', uint8_t),
    ('value', uint8_t * int(4)),
]

TSelector = struct_anon_38# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 119

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 129
class struct_anon_39(Structure):
    pass

struct_anon_39.__slots__ = [
    'size',
    'value',
]
struct_anon_39._fields_ = [
    ('size', uint8_t),
    ('value', uint8_t * int(16)),
]

SSelector = struct_anon_39# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 129

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 139
class struct_anon_40(Structure):
    pass

struct_anon_40.__slots__ = [
    'size',
    'value',
]
struct_anon_40._fields_ = [
    ('size', uint8_t),
    ('value', uint8_t * int(16)),
]

PSelector = struct_anon_40# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 139

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 141
class struct_sIsoConnectionParameters(Structure):
    pass

struct_sIsoConnectionParameters.__slots__ = [
    'acseAuthParameter',
    'hostname',
    'tcpPort',
    'localIpAddress',
    'localTcpPort',
    'remoteApTitle',
    'remoteApTitleLen',
    'remoteAEQualifier',
    'remotePSelector',
    'remoteSSelector',
    'remoteTSelector',
    'localApTitle',
    'localApTitleLen',
    'localAEQualifier',
    'localPSelector',
    'localSSelector',
    'localTSelector',
]
struct_sIsoConnectionParameters._fields_ = [
    ('acseAuthParameter', AcseAuthenticationParameter),
    ('hostname', String),
    ('tcpPort', c_int),
    ('localIpAddress', String),
    ('localTcpPort', c_int),
    ('remoteApTitle', uint8_t * int(10)),
    ('remoteApTitleLen', c_int),
    ('remoteAEQualifier', c_int),
    ('remotePSelector', PSelector),
    ('remoteSSelector', SSelector),
    ('remoteTSelector', TSelector),
    ('localApTitle', uint8_t * int(10)),
    ('localApTitleLen', c_int),
    ('localAEQualifier', c_int),
    ('localPSelector', PSelector),
    ('localSSelector', SSelector),
    ('localTSelector', TSelector),
]

IsoConnectionParameters = POINTER(struct_sIsoConnectionParameters)# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 172

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 183
if _libs["libiec61850.so"].has("IsoConnectionParameters_create", "cdecl"):
    IsoConnectionParameters_create = _libs["libiec61850.so"].get("IsoConnectionParameters_create", "cdecl")
    IsoConnectionParameters_create.argtypes = []
    IsoConnectionParameters_create.restype = IsoConnectionParameters

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 194
if _libs["libiec61850.so"].has("IsoConnectionParameters_destroy", "cdecl"):
    IsoConnectionParameters_destroy = _libs["libiec61850.so"].get("IsoConnectionParameters_destroy", "cdecl")
    IsoConnectionParameters_destroy.argtypes = [IsoConnectionParameters]
    IsoConnectionParameters_destroy.restype = None

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 198
if _libs["libiec61850.so"].has("IsoConnectionParameters_setTlsConfiguration", "cdecl"):
    IsoConnectionParameters_setTlsConfiguration = _libs["libiec61850.so"].get("IsoConnectionParameters_setTlsConfiguration", "cdecl")
    IsoConnectionParameters_setTlsConfiguration.argtypes = [IsoConnectionParameters, TLSConfiguration]
    IsoConnectionParameters_setTlsConfiguration.restype = None

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 209
if _libs["libiec61850.so"].has("IsoConnectionParameters_setAcseAuthenticationParameter", "cdecl"):
    IsoConnectionParameters_setAcseAuthenticationParameter = _libs["libiec61850.so"].get("IsoConnectionParameters_setAcseAuthenticationParameter", "cdecl")
    IsoConnectionParameters_setAcseAuthenticationParameter.argtypes = [IsoConnectionParameters, AcseAuthenticationParameter]
    IsoConnectionParameters_setAcseAuthenticationParameter.restype = None

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 223
if _libs["libiec61850.so"].has("IsoConnectionParameters_setTcpParameters", "cdecl"):
    IsoConnectionParameters_setTcpParameters = _libs["libiec61850.so"].get("IsoConnectionParameters_setTcpParameters", "cdecl")
    IsoConnectionParameters_setTcpParameters.argtypes = [IsoConnectionParameters, String, c_int]
    IsoConnectionParameters_setTcpParameters.restype = None

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 236
if _libs["libiec61850.so"].has("IsoConnectionParameters_setLocalTcpParameters", "cdecl"):
    IsoConnectionParameters_setLocalTcpParameters = _libs["libiec61850.so"].get("IsoConnectionParameters_setLocalTcpParameters", "cdecl")
    IsoConnectionParameters_setLocalTcpParameters.argtypes = [IsoConnectionParameters, String, c_int]
    IsoConnectionParameters_setLocalTcpParameters.restype = None

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 251
if _libs["libiec61850.so"].has("IsoConnectionParameters_setRemoteApTitle", "cdecl"):
    IsoConnectionParameters_setRemoteApTitle = _libs["libiec61850.so"].get("IsoConnectionParameters_setRemoteApTitle", "cdecl")
    IsoConnectionParameters_setRemoteApTitle.argtypes = [IsoConnectionParameters, String, c_int]
    IsoConnectionParameters_setRemoteApTitle.restype = None

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 266
if _libs["libiec61850.so"].has("IsoConnectionParameters_setRemoteAddresses", "cdecl"):
    IsoConnectionParameters_setRemoteAddresses = _libs["libiec61850.so"].get("IsoConnectionParameters_setRemoteAddresses", "cdecl")
    IsoConnectionParameters_setRemoteAddresses.argtypes = [IsoConnectionParameters, PSelector, SSelector, TSelector]
    IsoConnectionParameters_setRemoteAddresses.restype = None

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 281
if _libs["libiec61850.so"].has("IsoConnectionParameters_setLocalApTitle", "cdecl"):
    IsoConnectionParameters_setLocalApTitle = _libs["libiec61850.so"].get("IsoConnectionParameters_setLocalApTitle", "cdecl")
    IsoConnectionParameters_setLocalApTitle.argtypes = [IsoConnectionParameters, String, c_int]
    IsoConnectionParameters_setLocalApTitle.restype = None

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 296
if _libs["libiec61850.so"].has("IsoConnectionParameters_setLocalAddresses", "cdecl"):
    IsoConnectionParameters_setLocalAddresses = _libs["libiec61850.so"].get("IsoConnectionParameters_setLocalAddresses", "cdecl")
    IsoConnectionParameters_setLocalAddresses.argtypes = [IsoConnectionParameters, PSelector, SSelector, TSelector]
    IsoConnectionParameters_setLocalAddresses.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 54
class struct_sMmsConnectionParameters(Structure):
    pass

struct_sMmsConnectionParameters.__slots__ = [
    'maxServOutstandingCalling',
    'maxServOutstandingCalled',
    'dataStructureNestingLevel',
    'maxPduSize',
    'servicesSupported',
]
struct_sMmsConnectionParameters._fields_ = [
    ('maxServOutstandingCalling', c_int),
    ('maxServOutstandingCalled', c_int),
    ('dataStructureNestingLevel', c_int),
    ('maxPduSize', c_int),
    ('servicesSupported', uint8_t * int(11)),
]

MmsConnectionParameters = struct_sMmsConnectionParameters# ../libiec61850/src/mms/inc/mms_client_connection.h: 54

# ../libiec61850/src/mms/inc/mms_client_connection.h: 60
class struct_anon_41(Structure):
    pass

struct_anon_41.__slots__ = [
    'vendorName',
    'modelName',
    'revision',
]
struct_anon_41._fields_ = [
    ('vendorName', String),
    ('modelName', String),
    ('revision', String),
]

MmsServerIdentity = struct_anon_41# ../libiec61850/src/mms/inc/mms_client_connection.h: 60

enum_anon_42 = c_int# ../libiec61850/src/mms/inc/mms_client_connection.h: 67

MMS_CONNECTION_STATE_CLOSED = 0# ../libiec61850/src/mms/inc/mms_client_connection.h: 67

MMS_CONNECTION_STATE_CONNECTING = (MMS_CONNECTION_STATE_CLOSED + 1)# ../libiec61850/src/mms/inc/mms_client_connection.h: 67

MMS_CONNECTION_STATE_CONNECTED = (MMS_CONNECTION_STATE_CONNECTING + 1)# ../libiec61850/src/mms/inc/mms_client_connection.h: 67

MMS_CONNECTION_STATE_CLOSING = (MMS_CONNECTION_STATE_CONNECTED + 1)# ../libiec61850/src/mms/inc/mms_client_connection.h: 67

MmsConnectionState = enum_anon_42# ../libiec61850/src/mms/inc/mms_client_connection.h: 67

MmsInformationReportHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), String, String, POINTER(MmsValue), c_bool)# ../libiec61850/src/mms/inc/mms_client_connection.h: 69

# ../libiec61850/src/mms/inc/mms_client_connection.h: 75
class struct_sMmsConnection(Structure):
    pass

MmsConnection = POINTER(struct_sMmsConnection)# ../libiec61850/src/mms/inc/mms_client_connection.h: 75

# ../libiec61850/src/mms/inc/mms_client_connection.h: 88
if _libs["libiec61850.so"].has("MmsConnection_create", "cdecl"):
    MmsConnection_create = _libs["libiec61850.so"].get("MmsConnection_create", "cdecl")
    MmsConnection_create.argtypes = []
    MmsConnection_create.restype = MmsConnection

# ../libiec61850/src/mms/inc/mms_client_connection.h: 98
if _libs["libiec61850.so"].has("MmsConnection_createSecure", "cdecl"):
    MmsConnection_createSecure = _libs["libiec61850.so"].get("MmsConnection_createSecure", "cdecl")
    MmsConnection_createSecure.argtypes = [TLSConfiguration]
    MmsConnection_createSecure.restype = MmsConnection

# ../libiec61850/src/mms/inc/mms_client_connection.h: 112
if _libs["libiec61850.so"].has("MmsConnection_createNonThreaded", "cdecl"):
    MmsConnection_createNonThreaded = _libs["libiec61850.so"].get("MmsConnection_createNonThreaded", "cdecl")
    MmsConnection_createNonThreaded.argtypes = [TLSConfiguration]
    MmsConnection_createNonThreaded.restype = MmsConnection

MmsRawMessageHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(uint8_t), c_int, c_bool)# ../libiec61850/src/mms/inc/mms_client_connection.h: 125

# ../libiec61850/src/mms/inc/mms_client_connection.h: 139
if _libs["libiec61850.so"].has("MmsConnection_setRawMessageHandler", "cdecl"):
    MmsConnection_setRawMessageHandler = _libs["libiec61850.so"].get("MmsConnection_setRawMessageHandler", "cdecl")
    MmsConnection_setRawMessageHandler.argtypes = [MmsConnection, MmsRawMessageHandler, POINTER(None)]
    MmsConnection_setRawMessageHandler.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 152
if _libs["libiec61850.so"].has("MmsConnection_setFilestoreBasepath", "cdecl"):
    MmsConnection_setFilestoreBasepath = _libs["libiec61850.so"].get("MmsConnection_setFilestoreBasepath", "cdecl")
    MmsConnection_setFilestoreBasepath.argtypes = [MmsConnection, String]
    MmsConnection_setFilestoreBasepath.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 161
if _libs["libiec61850.so"].has("MmsConnection_setRequestTimeout", "cdecl"):
    MmsConnection_setRequestTimeout = _libs["libiec61850.so"].get("MmsConnection_setRequestTimeout", "cdecl")
    MmsConnection_setRequestTimeout.argtypes = [MmsConnection, uint32_t]
    MmsConnection_setRequestTimeout.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 171
if _libs["libiec61850.so"].has("MmsConnnection_setMaxOutstandingCalls", "cdecl"):
    MmsConnnection_setMaxOutstandingCalls = _libs["libiec61850.so"].get("MmsConnnection_setMaxOutstandingCalls", "cdecl")
    MmsConnnection_setMaxOutstandingCalls.argtypes = [MmsConnection, c_int, c_int]
    MmsConnnection_setMaxOutstandingCalls.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 181
if _libs["libiec61850.so"].has("MmsConnection_getRequestTimeout", "cdecl"):
    MmsConnection_getRequestTimeout = _libs["libiec61850.so"].get("MmsConnection_getRequestTimeout", "cdecl")
    MmsConnection_getRequestTimeout.argtypes = [MmsConnection]
    MmsConnection_getRequestTimeout.restype = uint32_t

# ../libiec61850/src/mms/inc/mms_client_connection.h: 190
if _libs["libiec61850.so"].has("MmsConnection_setConnectTimeout", "cdecl"):
    MmsConnection_setConnectTimeout = _libs["libiec61850.so"].get("MmsConnection_setConnectTimeout", "cdecl")
    MmsConnection_setConnectTimeout.argtypes = [MmsConnection, uint32_t]
    MmsConnection_setConnectTimeout.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 204
if _libs["libiec61850.so"].has("MmsConnection_setInformationReportHandler", "cdecl"):
    MmsConnection_setInformationReportHandler = _libs["libiec61850.so"].get("MmsConnection_setInformationReportHandler", "cdecl")
    MmsConnection_setInformationReportHandler.argtypes = [MmsConnection, MmsInformationReportHandler, POINTER(None)]
    MmsConnection_setInformationReportHandler.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 214
if _libs["libiec61850.so"].has("MmsConnection_getIsoConnectionParameters", "cdecl"):
    MmsConnection_getIsoConnectionParameters = _libs["libiec61850.so"].get("MmsConnection_getIsoConnectionParameters", "cdecl")
    MmsConnection_getIsoConnectionParameters.argtypes = [MmsConnection]
    MmsConnection_getIsoConnectionParameters.restype = IsoConnectionParameters

# ../libiec61850/src/mms/inc/mms_client_connection.h: 223
if _libs["libiec61850.so"].has("MmsConnection_getMmsConnectionParameters", "cdecl"):
    MmsConnection_getMmsConnectionParameters = _libs["libiec61850.so"].get("MmsConnection_getMmsConnectionParameters", "cdecl")
    MmsConnection_getMmsConnectionParameters.argtypes = [MmsConnection]
    MmsConnection_getMmsConnectionParameters.restype = MmsConnectionParameters

MmsConnectionStateChangedHandler = CFUNCTYPE(UNCHECKED(None), MmsConnection, POINTER(None), MmsConnectionState)# ../libiec61850/src/mms/inc/mms_client_connection.h: 225

# ../libiec61850/src/mms/inc/mms_client_connection.h: 228
if _libs["libiec61850.so"].has("MmsConnection_setConnectionStateChangedHandler", "cdecl"):
    MmsConnection_setConnectionStateChangedHandler = _libs["libiec61850.so"].get("MmsConnection_setConnectionStateChangedHandler", "cdecl")
    MmsConnection_setConnectionStateChangedHandler.argtypes = [MmsConnection, MmsConnectionStateChangedHandler, POINTER(None)]
    MmsConnection_setConnectionStateChangedHandler.restype = None

MmsConnectionLostHandler = CFUNCTYPE(UNCHECKED(None), MmsConnection, POINTER(None))# ../libiec61850/src/mms/inc/mms_client_connection.h: 236

# ../libiec61850/src/mms/inc/mms_client_connection.h: 245
if _libs["libiec61850.so"].has("MmsConnection_setConnectionLostHandler", "cdecl"):
    MmsConnection_setConnectionLostHandler = _libs["libiec61850.so"].get("MmsConnection_setConnectionLostHandler", "cdecl")
    MmsConnection_setConnectionLostHandler.argtypes = [MmsConnection, MmsConnectionLostHandler, POINTER(None)]
    MmsConnection_setConnectionLostHandler.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 254
for _lib in _libs.values():
    if not _lib.has("MmsConnection_setIsoConnectionParameters", "cdecl"):
        continue
    MmsConnection_setIsoConnectionParameters = _lib.get("MmsConnection_setIsoConnectionParameters", "cdecl")
    MmsConnection_setIsoConnectionParameters.argtypes = [MmsConnection, POINTER(IsoConnectionParameters)]
    MmsConnection_setIsoConnectionParameters.restype = None
    break

# ../libiec61850/src/mms/inc/mms_client_connection.h: 262
if _libs["libiec61850.so"].has("MmsConnection_destroy", "cdecl"):
    MmsConnection_destroy = _libs["libiec61850.so"].get("MmsConnection_destroy", "cdecl")
    MmsConnection_destroy.argtypes = [MmsConnection]
    MmsConnection_destroy.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 282
if _libs["libiec61850.so"].has("MmsConnection_connect", "cdecl"):
    MmsConnection_connect = _libs["libiec61850.so"].get("MmsConnection_connect", "cdecl")
    MmsConnection_connect.argtypes = [MmsConnection, POINTER(MmsError), String, c_int]
    MmsConnection_connect.restype = c_bool

# ../libiec61850/src/mms/inc/mms_client_connection.h: 287
if _libs["libiec61850.so"].has("MmsConnection_connectAsync", "cdecl"):
    MmsConnection_connectAsync = _libs["libiec61850.so"].get("MmsConnection_connectAsync", "cdecl")
    MmsConnection_connectAsync.argtypes = [MmsConnection, POINTER(MmsError), String, c_int]
    MmsConnection_connectAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 298
if _libs["libiec61850.so"].has("MmsConnection_tick", "cdecl"):
    MmsConnection_tick = _libs["libiec61850.so"].get("MmsConnection_tick", "cdecl")
    MmsConnection_tick.argtypes = [MmsConnection]
    MmsConnection_tick.restype = c_bool

# ../libiec61850/src/mms/inc/mms_client_connection.h: 302
if _libs["libiec61850.so"].has("MmsConnection_sendRawData", "cdecl"):
    MmsConnection_sendRawData = _libs["libiec61850.so"].get("MmsConnection_sendRawData", "cdecl")
    MmsConnection_sendRawData.argtypes = [MmsConnection, POINTER(MmsError), POINTER(uint8_t), c_int]
    MmsConnection_sendRawData.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 313
if _libs["libiec61850.so"].has("MmsConnection_close", "cdecl"):
    MmsConnection_close = _libs["libiec61850.so"].get("MmsConnection_close", "cdecl")
    MmsConnection_close.argtypes = [MmsConnection]
    MmsConnection_close.restype = None

MmsConnection_ConcludeAbortHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), MmsError, c_bool)# ../libiec61850/src/mms/inc/mms_client_connection.h: 316

# ../libiec61850/src/mms/inc/mms_client_connection.h: 330
if _libs["libiec61850.so"].has("MmsConnection_abort", "cdecl"):
    MmsConnection_abort = _libs["libiec61850.so"].get("MmsConnection_abort", "cdecl")
    MmsConnection_abort.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_abort.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 333
if _libs["libiec61850.so"].has("MmsConnection_abortAsync", "cdecl"):
    MmsConnection_abortAsync = _libs["libiec61850.so"].get("MmsConnection_abortAsync", "cdecl")
    MmsConnection_abortAsync.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_abortAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 347
if _libs["libiec61850.so"].has("MmsConnection_conclude", "cdecl"):
    MmsConnection_conclude = _libs["libiec61850.so"].get("MmsConnection_conclude", "cdecl")
    MmsConnection_conclude.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_conclude.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 350
if _libs["libiec61850.so"].has("MmsConnection_concludeAsync", "cdecl"):
    MmsConnection_concludeAsync = _libs["libiec61850.so"].get("MmsConnection_concludeAsync", "cdecl")
    MmsConnection_concludeAsync.argtypes = [MmsConnection, POINTER(MmsError), MmsConnection_ConcludeAbortHandler, POINTER(None)]
    MmsConnection_concludeAsync.restype = None

MmsConnection_GenericServiceHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, c_bool)# ../libiec61850/src/mms/inc/mms_client_connection.h: 353

MmsConnection_GetNameListHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, LinkedList, c_bool)# ../libiec61850/src/mms/inc/mms_client_connection.h: 356

# ../libiec61850/src/mms/inc/mms_client_connection.h: 369
if _libs["libiec61850.so"].has("MmsConnection_getVMDVariableNames", "cdecl"):
    MmsConnection_getVMDVariableNames = _libs["libiec61850.so"].get("MmsConnection_getVMDVariableNames", "cdecl")
    MmsConnection_getVMDVariableNames.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_getVMDVariableNames.restype = LinkedList

# ../libiec61850/src/mms/inc/mms_client_connection.h: 372
if _libs["libiec61850.so"].has("MmsConnection_getVMDVariableNamesAsync", "cdecl"):
    MmsConnection_getVMDVariableNamesAsync = _libs["libiec61850.so"].get("MmsConnection_getVMDVariableNamesAsync", "cdecl")
    MmsConnection_getVMDVariableNamesAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getVMDVariableNamesAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 387
if _libs["libiec61850.so"].has("MmsConnection_getDomainNames", "cdecl"):
    MmsConnection_getDomainNames = _libs["libiec61850.so"].get("MmsConnection_getDomainNames", "cdecl")
    MmsConnection_getDomainNames.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_getDomainNames.restype = LinkedList

# ../libiec61850/src/mms/inc/mms_client_connection.h: 401
if _libs["libiec61850.so"].has("MmsConnection_getDomainNamesAsync", "cdecl"):
    MmsConnection_getDomainNamesAsync = _libs["libiec61850.so"].get("MmsConnection_getDomainNamesAsync", "cdecl")
    MmsConnection_getDomainNamesAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, LinkedList, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getDomainNamesAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 416
if _libs["libiec61850.so"].has("MmsConnection_getDomainVariableNames", "cdecl"):
    MmsConnection_getDomainVariableNames = _libs["libiec61850.so"].get("MmsConnection_getDomainVariableNames", "cdecl")
    MmsConnection_getDomainVariableNames.argtypes = [MmsConnection, POINTER(MmsError), String]
    MmsConnection_getDomainVariableNames.restype = LinkedList

# ../libiec61850/src/mms/inc/mms_client_connection.h: 433
if _libs["libiec61850.so"].has("MmsConnection_getDomainVariableNamesAsync", "cdecl"):
    MmsConnection_getDomainVariableNamesAsync = _libs["libiec61850.so"].get("MmsConnection_getDomainVariableNamesAsync", "cdecl")
    MmsConnection_getDomainVariableNamesAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, LinkedList, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getDomainVariableNamesAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 448
if _libs["libiec61850.so"].has("MmsConnection_getDomainVariableListNames", "cdecl"):
    MmsConnection_getDomainVariableListNames = _libs["libiec61850.so"].get("MmsConnection_getDomainVariableListNames", "cdecl")
    MmsConnection_getDomainVariableListNames.argtypes = [MmsConnection, POINTER(MmsError), String]
    MmsConnection_getDomainVariableListNames.restype = LinkedList

# ../libiec61850/src/mms/inc/mms_client_connection.h: 451
if _libs["libiec61850.so"].has("MmsConnection_getDomainVariableListNamesAsync", "cdecl"):
    MmsConnection_getDomainVariableListNamesAsync = _libs["libiec61850.so"].get("MmsConnection_getDomainVariableListNamesAsync", "cdecl")
    MmsConnection_getDomainVariableListNamesAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, LinkedList, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getDomainVariableListNamesAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 466
if _libs["libiec61850.so"].has("MmsConnection_getDomainJournals", "cdecl"):
    MmsConnection_getDomainJournals = _libs["libiec61850.so"].get("MmsConnection_getDomainJournals", "cdecl")
    MmsConnection_getDomainJournals.argtypes = [MmsConnection, POINTER(MmsError), String]
    MmsConnection_getDomainJournals.restype = LinkedList

# ../libiec61850/src/mms/inc/mms_client_connection.h: 469
if _libs["libiec61850.so"].has("MmsConnection_getDomainJournalsAsync", "cdecl"):
    MmsConnection_getDomainJournalsAsync = _libs["libiec61850.so"].get("MmsConnection_getDomainJournalsAsync", "cdecl")
    MmsConnection_getDomainJournalsAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getDomainJournalsAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 483
if _libs["libiec61850.so"].has("MmsConnection_getVariableListNamesAssociationSpecific", "cdecl"):
    MmsConnection_getVariableListNamesAssociationSpecific = _libs["libiec61850.so"].get("MmsConnection_getVariableListNamesAssociationSpecific", "cdecl")
    MmsConnection_getVariableListNamesAssociationSpecific.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_getVariableListNamesAssociationSpecific.restype = LinkedList

# ../libiec61850/src/mms/inc/mms_client_connection.h: 486
if _libs["libiec61850.so"].has("MmsConnection_getVariableListNamesAssociationSpecificAsync", "cdecl"):
    MmsConnection_getVariableListNamesAssociationSpecificAsync = _libs["libiec61850.so"].get("MmsConnection_getVariableListNamesAssociationSpecificAsync", "cdecl")
    MmsConnection_getVariableListNamesAssociationSpecificAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getVariableListNamesAssociationSpecificAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 502
if _libs["libiec61850.so"].has("MmsConnection_readVariable", "cdecl"):
    MmsConnection_readVariable = _libs["libiec61850.so"].get("MmsConnection_readVariable", "cdecl")
    MmsConnection_readVariable.argtypes = [MmsConnection, POINTER(MmsError), String, String]
    MmsConnection_readVariable.restype = POINTER(MmsValue)

MmsConnection_ReadVariableHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, POINTER(MmsValue))# ../libiec61850/src/mms/inc/mms_client_connection.h: 507

# ../libiec61850/src/mms/inc/mms_client_connection.h: 519
if _libs["libiec61850.so"].has("MmsConnection_readVariableAsync", "cdecl"):
    MmsConnection_readVariableAsync = _libs["libiec61850.so"].get("MmsConnection_readVariableAsync", "cdecl")
    MmsConnection_readVariableAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readVariableAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 535
if _libs["libiec61850.so"].has("MmsConnection_readVariableComponent", "cdecl"):
    MmsConnection_readVariableComponent = _libs["libiec61850.so"].get("MmsConnection_readVariableComponent", "cdecl")
    MmsConnection_readVariableComponent.argtypes = [MmsConnection, POINTER(MmsError), String, String, String]
    MmsConnection_readVariableComponent.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_client_connection.h: 552
if _libs["libiec61850.so"].has("MmsConnection_readVariableComponentAsync", "cdecl"):
    MmsConnection_readVariableComponentAsync = _libs["libiec61850.so"].get("MmsConnection_readVariableComponentAsync", "cdecl")
    MmsConnection_readVariableComponentAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, String, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readVariableComponentAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 570
if _libs["libiec61850.so"].has("MmsConnection_readArrayElements", "cdecl"):
    MmsConnection_readArrayElements = _libs["libiec61850.so"].get("MmsConnection_readArrayElements", "cdecl")
    MmsConnection_readArrayElements.argtypes = [MmsConnection, POINTER(MmsError), String, String, uint32_t, uint32_t]
    MmsConnection_readArrayElements.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_client_connection.h: 589
if _libs["libiec61850.so"].has("MmsConnection_readArrayElementsAsync", "cdecl"):
    MmsConnection_readArrayElementsAsync = _libs["libiec61850.so"].get("MmsConnection_readArrayElementsAsync", "cdecl")
    MmsConnection_readArrayElementsAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, uint32_t, uint32_t, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readArrayElementsAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 606
if _libs["libiec61850.so"].has("MmsConnection_readSingleArrayElementWithComponent", "cdecl"):
    MmsConnection_readSingleArrayElementWithComponent = _libs["libiec61850.so"].get("MmsConnection_readSingleArrayElementWithComponent", "cdecl")
    MmsConnection_readSingleArrayElementWithComponent.argtypes = [MmsConnection, POINTER(MmsError), String, String, uint32_t, String]
    MmsConnection_readSingleArrayElementWithComponent.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_client_connection.h: 611
if _libs["libiec61850.so"].has("MmsConnection_readSingleArrayElementWithComponentAsync", "cdecl"):
    MmsConnection_readSingleArrayElementWithComponentAsync = _libs["libiec61850.so"].get("MmsConnection_readSingleArrayElementWithComponentAsync", "cdecl")
    MmsConnection_readSingleArrayElementWithComponentAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, uint32_t, String, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readSingleArrayElementWithComponentAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 628
if _libs["libiec61850.so"].has("MmsConnection_readMultipleVariables", "cdecl"):
    MmsConnection_readMultipleVariables = _libs["libiec61850.so"].get("MmsConnection_readMultipleVariables", "cdecl")
    MmsConnection_readMultipleVariables.argtypes = [MmsConnection, POINTER(MmsError), String, LinkedList]
    MmsConnection_readMultipleVariables.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_client_connection.h: 633
if _libs["libiec61850.so"].has("MmsConnection_readMultipleVariablesAsync", "cdecl"):
    MmsConnection_readMultipleVariablesAsync = _libs["libiec61850.so"].get("MmsConnection_readMultipleVariablesAsync", "cdecl")
    MmsConnection_readMultipleVariablesAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, LinkedList, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readMultipleVariablesAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 651
if _libs["libiec61850.so"].has("MmsConnection_writeVariable", "cdecl"):
    MmsConnection_writeVariable = _libs["libiec61850.so"].get("MmsConnection_writeVariable", "cdecl")
    MmsConnection_writeVariable.argtypes = [MmsConnection, POINTER(MmsError), String, String, POINTER(MmsValue)]
    MmsConnection_writeVariable.restype = MmsDataAccessError

MmsConnection_WriteVariableHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, MmsDataAccessError)# ../libiec61850/src/mms/inc/mms_client_connection.h: 655

# ../libiec61850/src/mms/inc/mms_client_connection.h: 658
if _libs["libiec61850.so"].has("MmsConnection_writeVariableAsync", "cdecl"):
    MmsConnection_writeVariableAsync = _libs["libiec61850.so"].get("MmsConnection_writeVariableAsync", "cdecl")
    MmsConnection_writeVariableAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, POINTER(MmsValue), MmsConnection_WriteVariableHandler, POINTER(None)]
    MmsConnection_writeVariableAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 676
if _libs["libiec61850.so"].has("MmsConnection_writeVariableComponent", "cdecl"):
    MmsConnection_writeVariableComponent = _libs["libiec61850.so"].get("MmsConnection_writeVariableComponent", "cdecl")
    MmsConnection_writeVariableComponent.argtypes = [MmsConnection, POINTER(MmsError), String, String, String, POINTER(MmsValue)]
    MmsConnection_writeVariableComponent.restype = MmsDataAccessError

# ../libiec61850/src/mms/inc/mms_client_connection.h: 694
if _libs["libiec61850.so"].has("MmsConnection_writeSingleArrayElementWithComponent", "cdecl"):
    MmsConnection_writeSingleArrayElementWithComponent = _libs["libiec61850.so"].get("MmsConnection_writeSingleArrayElementWithComponent", "cdecl")
    MmsConnection_writeSingleArrayElementWithComponent.argtypes = [MmsConnection, POINTER(MmsError), String, String, uint32_t, String, POINTER(MmsValue)]
    MmsConnection_writeSingleArrayElementWithComponent.restype = MmsDataAccessError

# ../libiec61850/src/mms/inc/mms_client_connection.h: 699
if _libs["libiec61850.so"].has("MmsConnection_writeSingleArrayElementWithComponentAsync", "cdecl"):
    MmsConnection_writeSingleArrayElementWithComponentAsync = _libs["libiec61850.so"].get("MmsConnection_writeSingleArrayElementWithComponentAsync", "cdecl")
    MmsConnection_writeSingleArrayElementWithComponentAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, uint32_t, String, POINTER(MmsValue), MmsConnection_WriteVariableHandler, POINTER(None)]
    MmsConnection_writeSingleArrayElementWithComponentAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 705
if _libs["libiec61850.so"].has("MmsConnection_writeVariableComponentAsync", "cdecl"):
    MmsConnection_writeVariableComponentAsync = _libs["libiec61850.so"].get("MmsConnection_writeVariableComponentAsync", "cdecl")
    MmsConnection_writeVariableComponentAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, String, POINTER(MmsValue), MmsConnection_WriteVariableHandler, POINTER(None)]
    MmsConnection_writeVariableComponentAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 728
if _libs["libiec61850.so"].has("MmsConnection_writeArrayElements", "cdecl"):
    MmsConnection_writeArrayElements = _libs["libiec61850.so"].get("MmsConnection_writeArrayElements", "cdecl")
    MmsConnection_writeArrayElements.argtypes = [MmsConnection, POINTER(MmsError), String, String, c_int, c_int, POINTER(MmsValue)]
    MmsConnection_writeArrayElements.restype = MmsDataAccessError

# ../libiec61850/src/mms/inc/mms_client_connection.h: 733
if _libs["libiec61850.so"].has("MmsConnection_writeArrayElementsAsync", "cdecl"):
    MmsConnection_writeArrayElementsAsync = _libs["libiec61850.so"].get("MmsConnection_writeArrayElementsAsync", "cdecl")
    MmsConnection_writeArrayElementsAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, c_int, c_int, POINTER(MmsValue), MmsConnection_WriteVariableHandler, POINTER(None)]
    MmsConnection_writeArrayElementsAsync.restype = None

MmsConnection_WriteMultipleVariablesHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, LinkedList)# ../libiec61850/src/mms/inc/mms_client_connection.h: 740

# ../libiec61850/src/mms/inc/mms_client_connection.h: 761
if _libs["libiec61850.so"].has("MmsConnection_writeMultipleVariables", "cdecl"):
    MmsConnection_writeMultipleVariables = _libs["libiec61850.so"].get("MmsConnection_writeMultipleVariables", "cdecl")
    MmsConnection_writeMultipleVariables.argtypes = [MmsConnection, POINTER(MmsError), String, LinkedList, LinkedList, POINTER(LinkedList)]
    MmsConnection_writeMultipleVariables.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 766
if _libs["libiec61850.so"].has("MmsConnection_writeMultipleVariablesAsync", "cdecl"):
    MmsConnection_writeMultipleVariablesAsync = _libs["libiec61850.so"].get("MmsConnection_writeMultipleVariablesAsync", "cdecl")
    MmsConnection_writeMultipleVariablesAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, LinkedList, LinkedList, MmsConnection_WriteMultipleVariablesHandler, POINTER(None)]
    MmsConnection_writeMultipleVariablesAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 787
if _libs["libiec61850.so"].has("MmsConnection_writeNamedVariableList", "cdecl"):
    MmsConnection_writeNamedVariableList = _libs["libiec61850.so"].get("MmsConnection_writeNamedVariableList", "cdecl")
    MmsConnection_writeNamedVariableList.argtypes = [MmsConnection, POINTER(MmsError), c_bool, String, String, LinkedList, POINTER(LinkedList)]
    MmsConnection_writeNamedVariableList.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 793
if _libs["libiec61850.so"].has("MmsConnection_writeNamedVariableListAsync", "cdecl"):
    MmsConnection_writeNamedVariableListAsync = _libs["libiec61850.so"].get("MmsConnection_writeNamedVariableListAsync", "cdecl")
    MmsConnection_writeNamedVariableListAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), c_bool, String, String, LinkedList, MmsConnection_WriteMultipleVariablesHandler, POINTER(None)]
    MmsConnection_writeNamedVariableListAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 807
if _libs["libiec61850.so"].has("MmsConnection_getVariableAccessAttributes", "cdecl"):
    MmsConnection_getVariableAccessAttributes = _libs["libiec61850.so"].get("MmsConnection_getVariableAccessAttributes", "cdecl")
    MmsConnection_getVariableAccessAttributes.argtypes = [MmsConnection, POINTER(MmsError), String, String]
    MmsConnection_getVariableAccessAttributes.restype = POINTER(MmsVariableSpecification)

MmsConnection_GetVariableAccessAttributesHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, POINTER(MmsVariableSpecification))# ../libiec61850/src/mms/inc/mms_client_connection.h: 812

# ../libiec61850/src/mms/inc/mms_client_connection.h: 816
if _libs["libiec61850.so"].has("MmsConnection_getVariableAccessAttributesAsync", "cdecl"):
    MmsConnection_getVariableAccessAttributesAsync = _libs["libiec61850.so"].get("MmsConnection_getVariableAccessAttributesAsync", "cdecl")
    MmsConnection_getVariableAccessAttributesAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, MmsConnection_GetVariableAccessAttributesHandler, POINTER(None)]
    MmsConnection_getVariableAccessAttributesAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 836
if _libs["libiec61850.so"].has("MmsConnection_readNamedVariableListValues", "cdecl"):
    MmsConnection_readNamedVariableListValues = _libs["libiec61850.so"].get("MmsConnection_readNamedVariableListValues", "cdecl")
    MmsConnection_readNamedVariableListValues.argtypes = [MmsConnection, POINTER(MmsError), String, String, c_bool]
    MmsConnection_readNamedVariableListValues.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_client_connection.h: 841
if _libs["libiec61850.so"].has("MmsConnection_readNamedVariableListValuesAsync", "cdecl"):
    MmsConnection_readNamedVariableListValuesAsync = _libs["libiec61850.so"].get("MmsConnection_readNamedVariableListValuesAsync", "cdecl")
    MmsConnection_readNamedVariableListValuesAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, c_bool, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readNamedVariableListValuesAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 858
if _libs["libiec61850.so"].has("MmsConnection_readNamedVariableListValuesAssociationSpecific", "cdecl"):
    MmsConnection_readNamedVariableListValuesAssociationSpecific = _libs["libiec61850.so"].get("MmsConnection_readNamedVariableListValuesAssociationSpecific", "cdecl")
    MmsConnection_readNamedVariableListValuesAssociationSpecific.argtypes = [MmsConnection, POINTER(MmsError), String, c_bool]
    MmsConnection_readNamedVariableListValuesAssociationSpecific.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_client_connection.h: 863
if _libs["libiec61850.so"].has("MmsConnection_readNamedVariableListValuesAssociationSpecificAsync", "cdecl"):
    MmsConnection_readNamedVariableListValuesAssociationSpecificAsync = _libs["libiec61850.so"].get("MmsConnection_readNamedVariableListValuesAssociationSpecificAsync", "cdecl")
    MmsConnection_readNamedVariableListValuesAssociationSpecificAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, c_bool, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readNamedVariableListValuesAssociationSpecificAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 881
if _libs["libiec61850.so"].has("MmsConnection_defineNamedVariableList", "cdecl"):
    MmsConnection_defineNamedVariableList = _libs["libiec61850.so"].get("MmsConnection_defineNamedVariableList", "cdecl")
    MmsConnection_defineNamedVariableList.argtypes = [MmsConnection, POINTER(MmsError), String, String, LinkedList]
    MmsConnection_defineNamedVariableList.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 885
if _libs["libiec61850.so"].has("MmsConnection_defineNamedVariableListAsync", "cdecl"):
    MmsConnection_defineNamedVariableListAsync = _libs["libiec61850.so"].get("MmsConnection_defineNamedVariableListAsync", "cdecl")
    MmsConnection_defineNamedVariableListAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, LinkedList, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_defineNamedVariableListAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 901
if _libs["libiec61850.so"].has("MmsConnection_defineNamedVariableListAssociationSpecific", "cdecl"):
    MmsConnection_defineNamedVariableListAssociationSpecific = _libs["libiec61850.so"].get("MmsConnection_defineNamedVariableListAssociationSpecific", "cdecl")
    MmsConnection_defineNamedVariableListAssociationSpecific.argtypes = [MmsConnection, POINTER(MmsError), String, LinkedList]
    MmsConnection_defineNamedVariableListAssociationSpecific.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 905
if _libs["libiec61850.so"].has("MmsConnection_defineNamedVariableListAssociationSpecificAsync", "cdecl"):
    MmsConnection_defineNamedVariableListAssociationSpecificAsync = _libs["libiec61850.so"].get("MmsConnection_defineNamedVariableListAssociationSpecificAsync", "cdecl")
    MmsConnection_defineNamedVariableListAssociationSpecificAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, LinkedList, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_defineNamedVariableListAssociationSpecificAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 925
if _libs["libiec61850.so"].has("MmsConnection_readNamedVariableListDirectory", "cdecl"):
    MmsConnection_readNamedVariableListDirectory = _libs["libiec61850.so"].get("MmsConnection_readNamedVariableListDirectory", "cdecl")
    MmsConnection_readNamedVariableListDirectory.argtypes = [MmsConnection, POINTER(MmsError), String, String, POINTER(c_bool)]
    MmsConnection_readNamedVariableListDirectory.restype = LinkedList

MmsConnection_ReadNVLDirectoryHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, LinkedList, c_bool)# ../libiec61850/src/mms/inc/mms_client_connection.h: 930

# ../libiec61850/src/mms/inc/mms_client_connection.h: 934
if _libs["libiec61850.so"].has("MmsConnection_readNamedVariableListDirectoryAsync", "cdecl"):
    MmsConnection_readNamedVariableListDirectoryAsync = _libs["libiec61850.so"].get("MmsConnection_readNamedVariableListDirectoryAsync", "cdecl")
    MmsConnection_readNamedVariableListDirectoryAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, MmsConnection_ReadNVLDirectoryHandler, POINTER(None)]
    MmsConnection_readNamedVariableListDirectoryAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 949
if _libs["libiec61850.so"].has("MmsConnection_readNamedVariableListDirectoryAssociationSpecific", "cdecl"):
    MmsConnection_readNamedVariableListDirectoryAssociationSpecific = _libs["libiec61850.so"].get("MmsConnection_readNamedVariableListDirectoryAssociationSpecific", "cdecl")
    MmsConnection_readNamedVariableListDirectoryAssociationSpecific.argtypes = [MmsConnection, POINTER(MmsError), String, POINTER(c_bool)]
    MmsConnection_readNamedVariableListDirectoryAssociationSpecific.restype = LinkedList

# ../libiec61850/src/mms/inc/mms_client_connection.h: 953
if _libs["libiec61850.so"].has("MmsConnection_readNamedVariableListDirectoryAssociationSpecificAsync", "cdecl"):
    MmsConnection_readNamedVariableListDirectoryAssociationSpecificAsync = _libs["libiec61850.so"].get("MmsConnection_readNamedVariableListDirectoryAssociationSpecificAsync", "cdecl")
    MmsConnection_readNamedVariableListDirectoryAssociationSpecificAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, MmsConnection_ReadNVLDirectoryHandler, POINTER(None)]
    MmsConnection_readNamedVariableListDirectoryAssociationSpecificAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 971
if _libs["libiec61850.so"].has("MmsConnection_deleteNamedVariableList", "cdecl"):
    MmsConnection_deleteNamedVariableList = _libs["libiec61850.so"].get("MmsConnection_deleteNamedVariableList", "cdecl")
    MmsConnection_deleteNamedVariableList.argtypes = [MmsConnection, POINTER(MmsError), String, String]
    MmsConnection_deleteNamedVariableList.restype = c_bool

# ../libiec61850/src/mms/inc/mms_client_connection.h: 975
if _libs["libiec61850.so"].has("MmsConnection_deleteNamedVariableListAsync", "cdecl"):
    MmsConnection_deleteNamedVariableListAsync = _libs["libiec61850.so"].get("MmsConnection_deleteNamedVariableListAsync", "cdecl")
    MmsConnection_deleteNamedVariableListAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_deleteNamedVariableListAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 988
if _libs["libiec61850.so"].has("MmsConnection_deleteAssociationSpecificNamedVariableList", "cdecl"):
    MmsConnection_deleteAssociationSpecificNamedVariableList = _libs["libiec61850.so"].get("MmsConnection_deleteAssociationSpecificNamedVariableList", "cdecl")
    MmsConnection_deleteAssociationSpecificNamedVariableList.argtypes = [MmsConnection, POINTER(MmsError), String]
    MmsConnection_deleteAssociationSpecificNamedVariableList.restype = c_bool

# ../libiec61850/src/mms/inc/mms_client_connection.h: 993
if _libs["libiec61850.so"].has("MmsConnection_deleteAssociationSpecificNamedVariableListAsync", "cdecl"):
    MmsConnection_deleteAssociationSpecificNamedVariableListAsync = _libs["libiec61850.so"].get("MmsConnection_deleteAssociationSpecificNamedVariableListAsync", "cdecl")
    MmsConnection_deleteAssociationSpecificNamedVariableListAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_deleteAssociationSpecificNamedVariableListAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1007
if _libs["libiec61850.so"].has("MmsVariableAccessSpecification_create", "cdecl"):
    MmsVariableAccessSpecification_create = _libs["libiec61850.so"].get("MmsVariableAccessSpecification_create", "cdecl")
    MmsVariableAccessSpecification_create.argtypes = [String, String]
    MmsVariableAccessSpecification_create.restype = POINTER(MmsVariableAccessSpecification)

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1026
if _libs["libiec61850.so"].has("MmsVariableAccessSpecification_createAlternateAccess", "cdecl"):
    MmsVariableAccessSpecification_createAlternateAccess = _libs["libiec61850.so"].get("MmsVariableAccessSpecification_createAlternateAccess", "cdecl")
    MmsVariableAccessSpecification_createAlternateAccess.argtypes = [String, String, c_int32, String]
    MmsVariableAccessSpecification_createAlternateAccess.restype = POINTER(MmsVariableAccessSpecification)

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1036
if _libs["libiec61850.so"].has("MmsVariableAccessSpecification_destroy", "cdecl"):
    MmsVariableAccessSpecification_destroy = _libs["libiec61850.so"].get("MmsVariableAccessSpecification_destroy", "cdecl")
    MmsVariableAccessSpecification_destroy.argtypes = [POINTER(MmsVariableAccessSpecification)]
    MmsVariableAccessSpecification_destroy.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1048
if _libs["libiec61850.so"].has("MmsConnection_setLocalDetail", "cdecl"):
    MmsConnection_setLocalDetail = _libs["libiec61850.so"].get("MmsConnection_setLocalDetail", "cdecl")
    MmsConnection_setLocalDetail.argtypes = [MmsConnection, c_int32]
    MmsConnection_setLocalDetail.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1051
if _libs["libiec61850.so"].has("MmsConnection_getLocalDetail", "cdecl"):
    MmsConnection_getLocalDetail = _libs["libiec61850.so"].get("MmsConnection_getLocalDetail", "cdecl")
    MmsConnection_getLocalDetail.argtypes = [MmsConnection]
    MmsConnection_getLocalDetail.restype = c_int32

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1062
if _libs["libiec61850.so"].has("MmsConnection_identify", "cdecl"):
    MmsConnection_identify = _libs["libiec61850.so"].get("MmsConnection_identify", "cdecl")
    MmsConnection_identify.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_identify.restype = POINTER(MmsServerIdentity)

MmsConnection_IdentifyHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, String, String, String)# ../libiec61850/src/mms/inc/mms_client_connection.h: 1066

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1070
if _libs["libiec61850.so"].has("MmsConnection_identifyAsync", "cdecl"):
    MmsConnection_identifyAsync = _libs["libiec61850.so"].get("MmsConnection_identifyAsync", "cdecl")
    MmsConnection_identifyAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), MmsConnection_IdentifyHandler, POINTER(None)]
    MmsConnection_identifyAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1079
if _libs["libiec61850.so"].has("MmsServerIdentity_destroy", "cdecl"):
    MmsServerIdentity_destroy = _libs["libiec61850.so"].get("MmsServerIdentity_destroy", "cdecl")
    MmsServerIdentity_destroy.argtypes = [POINTER(MmsServerIdentity)]
    MmsServerIdentity_destroy.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1094
if _libs["libiec61850.so"].has("MmsConnection_getServerStatus", "cdecl"):
    MmsConnection_getServerStatus = _libs["libiec61850.so"].get("MmsConnection_getServerStatus", "cdecl")
    MmsConnection_getServerStatus.argtypes = [MmsConnection, POINTER(MmsError), POINTER(c_int), POINTER(c_int), c_bool]
    MmsConnection_getServerStatus.restype = None

MmsConnection_GetServerStatusHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, c_int, c_int)# ../libiec61850/src/mms/inc/mms_client_connection.h: 1098

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1101
if _libs["libiec61850.so"].has("MmsConnection_getServerStatusAsync", "cdecl"):
    MmsConnection_getServerStatusAsync = _libs["libiec61850.so"].get("MmsConnection_getServerStatusAsync", "cdecl")
    MmsConnection_getServerStatusAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), c_bool, MmsConnection_GetServerStatusHandler, POINTER(None)]
    MmsConnection_getServerStatusAsync.restype = None

MmsFileDirectoryHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), String, uint32_t, uint64_t)# ../libiec61850/src/mms/inc/mms_client_connection.h: 1109

MmsConnection_FileDirectoryHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, String, uint32_t, uint64_t, c_bool)# ../libiec61850/src/mms/inc/mms_client_connection.h: 1119

MmsFileReadHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int32, POINTER(uint8_t), uint32_t)# ../libiec61850/src/mms/inc/mms_client_connection.h: 1123

MmsConnection_FileReadHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, c_int32, POINTER(uint8_t), uint32_t, c_bool)# ../libiec61850/src/mms/inc/mms_client_connection.h: 1139

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1152
if _libs["libiec61850.so"].has("MmsConnection_fileOpen", "cdecl"):
    MmsConnection_fileOpen = _libs["libiec61850.so"].get("MmsConnection_fileOpen", "cdecl")
    MmsConnection_fileOpen.argtypes = [MmsConnection, POINTER(MmsError), String, uint32_t, POINTER(uint32_t), POINTER(uint64_t)]
    MmsConnection_fileOpen.restype = c_int32

MmsConnection_FileOpenHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, c_int32, uint32_t, uint64_t)# ../libiec61850/src/mms/inc/mms_client_connection.h: 1156

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1159
if _libs["libiec61850.so"].has("MmsConnection_fileOpenAsync", "cdecl"):
    MmsConnection_fileOpenAsync = _libs["libiec61850.so"].get("MmsConnection_fileOpenAsync", "cdecl")
    MmsConnection_fileOpenAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, uint32_t, MmsConnection_FileOpenHandler, POINTER(None)]
    MmsConnection_fileOpenAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1175
if _libs["libiec61850.so"].has("MmsConnection_fileRead", "cdecl"):
    MmsConnection_fileRead = _libs["libiec61850.so"].get("MmsConnection_fileRead", "cdecl")
    MmsConnection_fileRead.argtypes = [MmsConnection, POINTER(MmsError), c_int32, MmsFileReadHandler, POINTER(None)]
    MmsConnection_fileRead.restype = c_bool

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1178
if _libs["libiec61850.so"].has("MmsConnection_fileReadAsync", "cdecl"):
    MmsConnection_fileReadAsync = _libs["libiec61850.so"].get("MmsConnection_fileReadAsync", "cdecl")
    MmsConnection_fileReadAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), c_int32, MmsConnection_FileReadHandler, POINTER(None)]
    MmsConnection_fileReadAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1188
if _libs["libiec61850.so"].has("MmsConnection_fileClose", "cdecl"):
    MmsConnection_fileClose = _libs["libiec61850.so"].get("MmsConnection_fileClose", "cdecl")
    MmsConnection_fileClose.argtypes = [MmsConnection, POINTER(MmsError), c_int32]
    MmsConnection_fileClose.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1191
if _libs["libiec61850.so"].has("MmsConnection_fileCloseAsync", "cdecl"):
    MmsConnection_fileCloseAsync = _libs["libiec61850.so"].get("MmsConnection_fileCloseAsync", "cdecl")
    MmsConnection_fileCloseAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), uint32_t, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_fileCloseAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1201
if _libs["libiec61850.so"].has("MmsConnection_fileDelete", "cdecl"):
    MmsConnection_fileDelete = _libs["libiec61850.so"].get("MmsConnection_fileDelete", "cdecl")
    MmsConnection_fileDelete.argtypes = [MmsConnection, POINTER(MmsError), String]
    MmsConnection_fileDelete.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1204
if _libs["libiec61850.so"].has("MmsConnection_fileDeleteAsync", "cdecl"):
    MmsConnection_fileDeleteAsync = _libs["libiec61850.so"].get("MmsConnection_fileDeleteAsync", "cdecl")
    MmsConnection_fileDeleteAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_fileDeleteAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1216
if _libs["libiec61850.so"].has("MmsConnection_fileRename", "cdecl"):
    MmsConnection_fileRename = _libs["libiec61850.so"].get("MmsConnection_fileRename", "cdecl")
    MmsConnection_fileRename.argtypes = [MmsConnection, POINTER(MmsError), String, String]
    MmsConnection_fileRename.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1219
if _libs["libiec61850.so"].has("MmsConnection_fileRenameAsync", "cdecl"):
    MmsConnection_fileRenameAsync = _libs["libiec61850.so"].get("MmsConnection_fileRenameAsync", "cdecl")
    MmsConnection_fileRenameAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_fileRenameAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1231
if _libs["libiec61850.so"].has("MmsConnection_obtainFile", "cdecl"):
    MmsConnection_obtainFile = _libs["libiec61850.so"].get("MmsConnection_obtainFile", "cdecl")
    MmsConnection_obtainFile.argtypes = [MmsConnection, POINTER(MmsError), String, String]
    MmsConnection_obtainFile.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1234
if _libs["libiec61850.so"].has("MmsConnection_obtainFileAsync", "cdecl"):
    MmsConnection_obtainFileAsync = _libs["libiec61850.so"].get("MmsConnection_obtainFileAsync", "cdecl")
    MmsConnection_obtainFileAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_obtainFileAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1254
if _libs["libiec61850.so"].has("MmsConnection_getFileDirectory", "cdecl"):
    MmsConnection_getFileDirectory = _libs["libiec61850.so"].get("MmsConnection_getFileDirectory", "cdecl")
    MmsConnection_getFileDirectory.argtypes = [MmsConnection, POINTER(MmsError), String, String, MmsFileDirectoryHandler, POINTER(None)]
    MmsConnection_getFileDirectory.restype = c_bool

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1258
if _libs["libiec61850.so"].has("MmsConnection_getFileDirectoryAsync", "cdecl"):
    MmsConnection_getFileDirectoryAsync = _libs["libiec61850.so"].get("MmsConnection_getFileDirectoryAsync", "cdecl")
    MmsConnection_getFileDirectoryAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, MmsConnection_FileDirectoryHandler, POINTER(None)]
    MmsConnection_getFileDirectoryAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1265
class struct_sMmsJournalEntry(Structure):
    pass

MmsJournalEntry = POINTER(struct_sMmsJournalEntry)# ../libiec61850/src/mms/inc/mms_client_connection.h: 1261

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1271
class struct_sMmsJournalVariable(Structure):
    pass

MmsJournalVariable = POINTER(struct_sMmsJournalVariable)# ../libiec61850/src/mms/inc/mms_client_connection.h: 1263

struct_sMmsJournalEntry.__slots__ = [
    'entryID',
    'occurenceTime',
    'journalVariables',
]
struct_sMmsJournalEntry._fields_ = [
    ('entryID', POINTER(MmsValue)),
    ('occurenceTime', POINTER(MmsValue)),
    ('journalVariables', LinkedList),
]

struct_sMmsJournalVariable.__slots__ = [
    'tag',
    'value',
]
struct_sMmsJournalVariable._fields_ = [
    ('tag', String),
    ('value', POINTER(MmsValue)),
]

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1290
if _libs["libiec61850.so"].has("MmsJournalEntry_destroy", "cdecl"):
    MmsJournalEntry_destroy = _libs["libiec61850.so"].get("MmsJournalEntry_destroy", "cdecl")
    MmsJournalEntry_destroy.argtypes = [MmsJournalEntry]
    MmsJournalEntry_destroy.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1292
if _libs["libiec61850.so"].has("MmsJournalEntry_getEntryID", "cdecl"):
    MmsJournalEntry_getEntryID = _libs["libiec61850.so"].get("MmsJournalEntry_getEntryID", "cdecl")
    MmsJournalEntry_getEntryID.argtypes = [MmsJournalEntry]
    MmsJournalEntry_getEntryID.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1295
if _libs["libiec61850.so"].has("MmsJournalEntry_getOccurenceTime", "cdecl"):
    MmsJournalEntry_getOccurenceTime = _libs["libiec61850.so"].get("MmsJournalEntry_getOccurenceTime", "cdecl")
    MmsJournalEntry_getOccurenceTime.argtypes = [MmsJournalEntry]
    MmsJournalEntry_getOccurenceTime.restype = POINTER(MmsValue)

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1299
if _libs["libiec61850.so"].has("MmsJournalEntry_getJournalVariables", "cdecl"):
    MmsJournalEntry_getJournalVariables = _libs["libiec61850.so"].get("MmsJournalEntry_getJournalVariables", "cdecl")
    MmsJournalEntry_getJournalVariables.argtypes = [MmsJournalEntry]
    MmsJournalEntry_getJournalVariables.restype = LinkedList

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1301
if _libs["libiec61850.so"].has("MmsJournalVariable_getTag", "cdecl"):
    MmsJournalVariable_getTag = _libs["libiec61850.so"].get("MmsJournalVariable_getTag", "cdecl")
    MmsJournalVariable_getTag.argtypes = [MmsJournalVariable]
    MmsJournalVariable_getTag.restype = c_char_p

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1304
if _libs["libiec61850.so"].has("MmsJournalVariable_getValue", "cdecl"):
    MmsJournalVariable_getValue = _libs["libiec61850.so"].get("MmsJournalVariable_getValue", "cdecl")
    MmsJournalVariable_getValue.argtypes = [MmsJournalVariable]
    MmsJournalVariable_getValue.restype = POINTER(MmsValue)

MmsConnection_ReadJournalHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, LinkedList, c_bool)# ../libiec61850/src/mms/inc/mms_client_connection.h: 1308

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1312
if _libs["libiec61850.so"].has("MmsConnection_readJournalTimeRange", "cdecl"):
    MmsConnection_readJournalTimeRange = _libs["libiec61850.so"].get("MmsConnection_readJournalTimeRange", "cdecl")
    MmsConnection_readJournalTimeRange.argtypes = [MmsConnection, POINTER(MmsError), String, String, POINTER(MmsValue), POINTER(MmsValue), POINTER(c_bool)]
    MmsConnection_readJournalTimeRange.restype = LinkedList

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1316
if _libs["libiec61850.so"].has("MmsConnection_readJournalTimeRangeAsync", "cdecl"):
    MmsConnection_readJournalTimeRangeAsync = _libs["libiec61850.so"].get("MmsConnection_readJournalTimeRangeAsync", "cdecl")
    MmsConnection_readJournalTimeRangeAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, POINTER(MmsValue), POINTER(MmsValue), MmsConnection_ReadJournalHandler, POINTER(None)]
    MmsConnection_readJournalTimeRangeAsync.restype = None

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1320
if _libs["libiec61850.so"].has("MmsConnection_readJournalStartAfter", "cdecl"):
    MmsConnection_readJournalStartAfter = _libs["libiec61850.so"].get("MmsConnection_readJournalStartAfter", "cdecl")
    MmsConnection_readJournalStartAfter.argtypes = [MmsConnection, POINTER(MmsError), String, String, POINTER(MmsValue), POINTER(MmsValue), POINTER(c_bool)]
    MmsConnection_readJournalStartAfter.restype = LinkedList

# ../libiec61850/src/mms/inc/mms_client_connection.h: 1324
if _libs["libiec61850.so"].has("MmsConnection_readJournalStartAfterAsync", "cdecl"):
    MmsConnection_readJournalStartAfterAsync = _libs["libiec61850.so"].get("MmsConnection_readJournalStartAfterAsync", "cdecl")
    MmsConnection_readJournalStartAfterAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, POINTER(MmsValue), POINTER(MmsValue), MmsConnection_ReadJournalHandler, POINTER(None)]
    MmsConnection_readJournalStartAfterAsync.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 43
class struct_sClientDataSet(Structure):
    pass

ClientDataSet = POINTER(struct_sClientDataSet)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 43

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 46
class struct_sClientReport(Structure):
    pass

ClientReport = POINTER(struct_sClientReport)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 46

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 49
class struct_sClientReportControlBlock(Structure):
    pass

ClientReportControlBlock = POINTER(struct_sClientReportControlBlock)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 49

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 52
class struct_sClientGooseControlBlock(Structure):
    pass

ClientGooseControlBlock = POINTER(struct_sClientGooseControlBlock)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 52

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 61
class struct_sIedConnection(Structure):
    pass

IedConnection = POINTER(struct_sIedConnection)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 61

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 69
class struct_anon_43(Structure):
    pass

struct_anon_43.__slots__ = [
    'ctlNum',
    'error',
    'addCause',
]
struct_anon_43._fields_ = [
    ('ctlNum', c_int),
    ('error', ControlLastApplError),
    ('addCause', ControlAddCause),
]

LastApplError = struct_anon_43# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 69

enum_anon_44 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 78

IED_STATE_CLOSED = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 78

IED_STATE_CONNECTING = (IED_STATE_CLOSED + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 78

IED_STATE_CONNECTED = (IED_STATE_CONNECTING + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 78

IED_STATE_CLOSING = (IED_STATE_CONNECTED + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 78

IedConnectionState = enum_anon_44# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 78

enum_anon_45 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_OK = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_NOT_CONNECTED = 1# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_ALREADY_CONNECTED = 2# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_CONNECTION_LOST = 3# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_SERVICE_NOT_SUPPORTED = 4# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_CONNECTION_REJECTED = 5# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_OUTSTANDING_CALL_LIMIT_REACHED = 6# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_USER_PROVIDED_INVALID_ARGUMENT = 10# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_ENABLE_REPORT_FAILED_DATASET_MISMATCH = 11# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_OBJECT_REFERENCE_INVALID = 12# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_UNEXPECTED_VALUE_RECEIVED = 13# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_TIMEOUT = 20# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_ACCESS_DENIED = 21# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_OBJECT_DOES_NOT_EXIST = 22# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_OBJECT_EXISTS = 23# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_OBJECT_ACCESS_UNSUPPORTED = 24# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_TYPE_INCONSISTENT = 25# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_TEMPORARILY_UNAVAILABLE = 26# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_OBJECT_UNDEFINED = 27# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_INVALID_ADDRESS = 28# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_HARDWARE_FAULT = 29# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_TYPE_UNSUPPORTED = 30# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_OBJECT_ATTRIBUTE_INCONSISTENT = 31# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_OBJECT_VALUE_INVALID = 32# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_OBJECT_INVALIDATED = 33# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_MALFORMED_MESSAGE = 34# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_OBJECT_CONSTRAINT_CONFLICT = 35# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_SERVICE_NOT_IMPLEMENTED = 98# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IED_ERROR_UNKNOWN = 99# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

IedClientError = enum_anon_45# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 173

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 180
if _libs["libiec61850.so"].has("IedClientError_toString", "cdecl"):
    IedClientError_toString = _libs["libiec61850.so"].get("IedClientError_toString", "cdecl")
    IedClientError_toString.argtypes = [IedClientError]
    IedClientError_toString.restype = c_char_p

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 197
if _libs["libiec61850.so"].has("IedConnection_create", "cdecl"):
    IedConnection_create = _libs["libiec61850.so"].get("IedConnection_create", "cdecl")
    IedConnection_create.argtypes = []
    IedConnection_create.restype = IedConnection

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 215
if _libs["libiec61850.so"].has("IedConnection_createEx", "cdecl"):
    IedConnection_createEx = _libs["libiec61850.so"].get("IedConnection_createEx", "cdecl")
    IedConnection_createEx.argtypes = [TLSConfiguration, c_bool]
    IedConnection_createEx.restype = IedConnection

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 232
if _libs["libiec61850.so"].has("IedConnection_createWithTlsSupport", "cdecl"):
    IedConnection_createWithTlsSupport = _libs["libiec61850.so"].get("IedConnection_createWithTlsSupport", "cdecl")
    IedConnection_createWithTlsSupport.argtypes = [TLSConfiguration]
    IedConnection_createWithTlsSupport.restype = IedConnection

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 243
if _libs["libiec61850.so"].has("IedConnection_destroy", "cdecl"):
    IedConnection_destroy = _libs["libiec61850.so"].get("IedConnection_destroy", "cdecl")
    IedConnection_destroy.argtypes = [IedConnection]
    IedConnection_destroy.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 255
if _libs["libiec61850.so"].has("IedConnection_setLocalAddress", "cdecl"):
    IedConnection_setLocalAddress = _libs["libiec61850.so"].get("IedConnection_setLocalAddress", "cdecl")
    IedConnection_setLocalAddress.argtypes = [IedConnection, String, c_int]
    IedConnection_setLocalAddress.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 267
if _libs["libiec61850.so"].has("IedConnection_setConnectTimeout", "cdecl"):
    IedConnection_setConnectTimeout = _libs["libiec61850.so"].get("IedConnection_setConnectTimeout", "cdecl")
    IedConnection_setConnectTimeout.argtypes = [IedConnection, uint32_t]
    IedConnection_setConnectTimeout.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 277
if _libs["libiec61850.so"].has("IedConnection_setMaxOutstandingCalls", "cdecl"):
    IedConnection_setMaxOutstandingCalls = _libs["libiec61850.so"].get("IedConnection_setMaxOutstandingCalls", "cdecl")
    IedConnection_setMaxOutstandingCalls.argtypes = [IedConnection, c_int, c_int]
    IedConnection_setMaxOutstandingCalls.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 289
if _libs["libiec61850.so"].has("IedConnection_setRequestTimeout", "cdecl"):
    IedConnection_setRequestTimeout = _libs["libiec61850.so"].get("IedConnection_setRequestTimeout", "cdecl")
    IedConnection_setRequestTimeout.argtypes = [IedConnection, uint32_t]
    IedConnection_setRequestTimeout.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 299
if _libs["libiec61850.so"].has("IedConnection_getRequestTimeout", "cdecl"):
    IedConnection_getRequestTimeout = _libs["libiec61850.so"].get("IedConnection_getRequestTimeout", "cdecl")
    IedConnection_getRequestTimeout.argtypes = [IedConnection]
    IedConnection_getRequestTimeout.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 311
if _libs["libiec61850.so"].has("IedConnection_setTimeQuality", "cdecl"):
    IedConnection_setTimeQuality = _libs["libiec61850.so"].get("IedConnection_setTimeQuality", "cdecl")
    IedConnection_setTimeQuality.argtypes = [IedConnection, c_bool, c_bool, c_bool, c_int]
    IedConnection_setTimeQuality.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 326
if _libs["libiec61850.so"].has("IedConnection_tick", "cdecl"):
    IedConnection_tick = _libs["libiec61850.so"].get("IedConnection_tick", "cdecl")
    IedConnection_tick.argtypes = [IedConnection]
    IedConnection_tick.restype = c_bool

IedConnection_GenericServiceHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 339

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 356
if _libs["libiec61850.so"].has("IedConnection_connect", "cdecl"):
    IedConnection_connect = _libs["libiec61850.so"].get("IedConnection_connect", "cdecl")
    IedConnection_connect.argtypes = [IedConnection, POINTER(IedClientError), String, c_int]
    IedConnection_connect.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 372
if _libs["libiec61850.so"].has("IedConnection_connectAsync", "cdecl"):
    IedConnection_connectAsync = _libs["libiec61850.so"].get("IedConnection_connectAsync", "cdecl")
    IedConnection_connectAsync.argtypes = [IedConnection, POINTER(IedClientError), String, c_int]
    IedConnection_connectAsync.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 387
if _libs["libiec61850.so"].has("IedConnection_abort", "cdecl"):
    IedConnection_abort = _libs["libiec61850.so"].get("IedConnection_abort", "cdecl")
    IedConnection_abort.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_abort.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 403
if _libs["libiec61850.so"].has("IedConnection_abortAsync", "cdecl"):
    IedConnection_abortAsync = _libs["libiec61850.so"].get("IedConnection_abortAsync", "cdecl")
    IedConnection_abortAsync.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_abortAsync.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 418
if _libs["libiec61850.so"].has("IedConnection_release", "cdecl"):
    IedConnection_release = _libs["libiec61850.so"].get("IedConnection_release", "cdecl")
    IedConnection_release.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_release.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 433
if _libs["libiec61850.so"].has("IedConnection_releaseAsync", "cdecl"):
    IedConnection_releaseAsync = _libs["libiec61850.so"].get("IedConnection_releaseAsync", "cdecl")
    IedConnection_releaseAsync.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_releaseAsync.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 443
if _libs["libiec61850.so"].has("IedConnection_close", "cdecl"):
    IedConnection_close = _libs["libiec61850.so"].get("IedConnection_close", "cdecl")
    IedConnection_close.argtypes = [IedConnection]
    IedConnection_close.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 455
if _libs["libiec61850.so"].has("IedConnection_getState", "cdecl"):
    IedConnection_getState = _libs["libiec61850.so"].get("IedConnection_getState", "cdecl")
    IedConnection_getState.argtypes = [IedConnection]
    IedConnection_getState.restype = IedConnectionState

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 465
if _libs["libiec61850.so"].has("IedConnection_getLastApplError", "cdecl"):
    IedConnection_getLastApplError = _libs["libiec61850.so"].get("IedConnection_getLastApplError", "cdecl")
    IedConnection_getLastApplError.argtypes = [IedConnection]
    IedConnection_getLastApplError.restype = LastApplError

IedConnectionClosedHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), IedConnection)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 476

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 488
if _libs["libiec61850.so"].has("IedConnection_installConnectionClosedHandler", "cdecl"):
    IedConnection_installConnectionClosedHandler = _libs["libiec61850.so"].get("IedConnection_installConnectionClosedHandler", "cdecl")
    IedConnection_installConnectionClosedHandler.argtypes = [IedConnection, IedConnectionClosedHandler, POINTER(None)]
    IedConnection_installConnectionClosedHandler.restype = None

IedConnection_StateChangedHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), IedConnection, IedConnectionState)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 499

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 509
if _libs["libiec61850.so"].has("IedConnection_installStateChangedHandler", "cdecl"):
    IedConnection_installStateChangedHandler = _libs["libiec61850.so"].get("IedConnection_installStateChangedHandler", "cdecl")
    IedConnection_installStateChangedHandler.argtypes = [IedConnection, IedConnection_StateChangedHandler, POINTER(None)]
    IedConnection_installStateChangedHandler.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 522
if _libs["libiec61850.so"].has("IedConnection_getMmsConnection", "cdecl"):
    IedConnection_getMmsConnection = _libs["libiec61850.so"].get("IedConnection_getMmsConnection", "cdecl")
    IedConnection_getMmsConnection.argtypes = [IedConnection]
    IedConnection_getMmsConnection.restype = MmsConnection

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 555
class struct_sClientSVControlBlock(Structure):
    pass

ClientSVControlBlock = POINTER(struct_sClientSVControlBlock)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 555

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 573
if _libs["libiec61850.so"].has("ClientSVControlBlock_create", "cdecl"):
    ClientSVControlBlock_create = _libs["libiec61850.so"].get("ClientSVControlBlock_create", "cdecl")
    ClientSVControlBlock_create.argtypes = [IedConnection, String]
    ClientSVControlBlock_create.restype = ClientSVControlBlock

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 581
if _libs["libiec61850.so"].has("ClientSVControlBlock_destroy", "cdecl"):
    ClientSVControlBlock_destroy = _libs["libiec61850.so"].get("ClientSVControlBlock_destroy", "cdecl")
    ClientSVControlBlock_destroy.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_destroy.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 591
if _libs["libiec61850.so"].has("ClientSVControlBlock_isMulticast", "cdecl"):
    ClientSVControlBlock_isMulticast = _libs["libiec61850.so"].get("ClientSVControlBlock_isMulticast", "cdecl")
    ClientSVControlBlock_isMulticast.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_isMulticast.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 601
if _libs["libiec61850.so"].has("ClientSVControlBlock_getLastComError", "cdecl"):
    ClientSVControlBlock_getLastComError = _libs["libiec61850.so"].get("ClientSVControlBlock_getLastComError", "cdecl")
    ClientSVControlBlock_getLastComError.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getLastComError.restype = IedClientError

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 605
if _libs["libiec61850.so"].has("ClientSVControlBlock_setSvEna", "cdecl"):
    ClientSVControlBlock_setSvEna = _libs["libiec61850.so"].get("ClientSVControlBlock_setSvEna", "cdecl")
    ClientSVControlBlock_setSvEna.argtypes = [ClientSVControlBlock, c_bool]
    ClientSVControlBlock_setSvEna.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 608
if _libs["libiec61850.so"].has("ClientSVControlBlock_getSvEna", "cdecl"):
    ClientSVControlBlock_getSvEna = _libs["libiec61850.so"].get("ClientSVControlBlock_getSvEna", "cdecl")
    ClientSVControlBlock_getSvEna.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getSvEna.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 611
if _libs["libiec61850.so"].has("ClientSVControlBlock_setResv", "cdecl"):
    ClientSVControlBlock_setResv = _libs["libiec61850.so"].get("ClientSVControlBlock_setResv", "cdecl")
    ClientSVControlBlock_setResv.argtypes = [ClientSVControlBlock, c_bool]
    ClientSVControlBlock_setResv.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 614
if _libs["libiec61850.so"].has("ClientSVControlBlock_getResv", "cdecl"):
    ClientSVControlBlock_getResv = _libs["libiec61850.so"].get("ClientSVControlBlock_getResv", "cdecl")
    ClientSVControlBlock_getResv.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getResv.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 616
if _libs["libiec61850.so"].has("ClientSVControlBlock_getMsvID", "cdecl"):
    ClientSVControlBlock_getMsvID = _libs["libiec61850.so"].get("ClientSVControlBlock_getMsvID", "cdecl")
    ClientSVControlBlock_getMsvID.argtypes = [ClientSVControlBlock]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientSVControlBlock_getMsvID.restype = ReturnString
    else:
        ClientSVControlBlock_getMsvID.restype = String
        ClientSVControlBlock_getMsvID.errcheck = ReturnString

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 630
if _libs["libiec61850.so"].has("ClientSVControlBlock_getDatSet", "cdecl"):
    ClientSVControlBlock_getDatSet = _libs["libiec61850.so"].get("ClientSVControlBlock_getDatSet", "cdecl")
    ClientSVControlBlock_getDatSet.argtypes = [ClientSVControlBlock]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientSVControlBlock_getDatSet.restype = ReturnString
    else:
        ClientSVControlBlock_getDatSet.restype = String
        ClientSVControlBlock_getDatSet.errcheck = ReturnString

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 634
if _libs["libiec61850.so"].has("ClientSVControlBlock_getConfRev", "cdecl"):
    ClientSVControlBlock_getConfRev = _libs["libiec61850.so"].get("ClientSVControlBlock_getConfRev", "cdecl")
    ClientSVControlBlock_getConfRev.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getConfRev.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 637
if _libs["libiec61850.so"].has("ClientSVControlBlock_getSmpRate", "cdecl"):
    ClientSVControlBlock_getSmpRate = _libs["libiec61850.so"].get("ClientSVControlBlock_getSmpRate", "cdecl")
    ClientSVControlBlock_getSmpRate.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getSmpRate.restype = uint16_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 646
if _libs["libiec61850.so"].has("ClientSVControlBlock_getDstAddress", "cdecl"):
    ClientSVControlBlock_getDstAddress = _libs["libiec61850.so"].get("ClientSVControlBlock_getDstAddress", "cdecl")
    ClientSVControlBlock_getDstAddress.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getDstAddress.restype = PhyComAddress

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 655
if _libs["libiec61850.so"].has("ClientSVControlBlock_getOptFlds", "cdecl"):
    ClientSVControlBlock_getOptFlds = _libs["libiec61850.so"].get("ClientSVControlBlock_getOptFlds", "cdecl")
    ClientSVControlBlock_getOptFlds.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getOptFlds.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 663
if _libs["libiec61850.so"].has("ClientSVControlBlock_getSmpMod", "cdecl"):
    ClientSVControlBlock_getSmpMod = _libs["libiec61850.so"].get("ClientSVControlBlock_getSmpMod", "cdecl")
    ClientSVControlBlock_getSmpMod.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getSmpMod.restype = uint8_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 673
if _libs["libiec61850.so"].has("ClientSVControlBlock_getNoASDU", "cdecl"):
    ClientSVControlBlock_getNoASDU = _libs["libiec61850.so"].get("ClientSVControlBlock_getNoASDU", "cdecl")
    ClientSVControlBlock_getNoASDU.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getNoASDU.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 724
if _libs["libiec61850.so"].has("ClientGooseControlBlock_create", "cdecl"):
    ClientGooseControlBlock_create = _libs["libiec61850.so"].get("ClientGooseControlBlock_create", "cdecl")
    ClientGooseControlBlock_create.argtypes = [String]
    ClientGooseControlBlock_create.restype = ClientGooseControlBlock

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 727
if _libs["libiec61850.so"].has("ClientGooseControlBlock_destroy", "cdecl"):
    ClientGooseControlBlock_destroy = _libs["libiec61850.so"].get("ClientGooseControlBlock_destroy", "cdecl")
    ClientGooseControlBlock_destroy.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_destroy.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 730
if _libs["libiec61850.so"].has("ClientGooseControlBlock_getGoEna", "cdecl"):
    ClientGooseControlBlock_getGoEna = _libs["libiec61850.so"].get("ClientGooseControlBlock_getGoEna", "cdecl")
    ClientGooseControlBlock_getGoEna.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getGoEna.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 733
if _libs["libiec61850.so"].has("ClientGooseControlBlock_setGoEna", "cdecl"):
    ClientGooseControlBlock_setGoEna = _libs["libiec61850.so"].get("ClientGooseControlBlock_setGoEna", "cdecl")
    ClientGooseControlBlock_setGoEna.argtypes = [ClientGooseControlBlock, c_bool]
    ClientGooseControlBlock_setGoEna.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 735
if _libs["libiec61850.so"].has("ClientGooseControlBlock_getGoID", "cdecl"):
    ClientGooseControlBlock_getGoID = _libs["libiec61850.so"].get("ClientGooseControlBlock_getGoID", "cdecl")
    ClientGooseControlBlock_getGoID.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getGoID.restype = c_char_p

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 739
if _libs["libiec61850.so"].has("ClientGooseControlBlock_setGoID", "cdecl"):
    ClientGooseControlBlock_setGoID = _libs["libiec61850.so"].get("ClientGooseControlBlock_setGoID", "cdecl")
    ClientGooseControlBlock_setGoID.argtypes = [ClientGooseControlBlock, String]
    ClientGooseControlBlock_setGoID.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 741
if _libs["libiec61850.so"].has("ClientGooseControlBlock_getDatSet", "cdecl"):
    ClientGooseControlBlock_getDatSet = _libs["libiec61850.so"].get("ClientGooseControlBlock_getDatSet", "cdecl")
    ClientGooseControlBlock_getDatSet.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDatSet.restype = c_char_p

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 745
if _libs["libiec61850.so"].has("ClientGooseControlBlock_setDatSet", "cdecl"):
    ClientGooseControlBlock_setDatSet = _libs["libiec61850.so"].get("ClientGooseControlBlock_setDatSet", "cdecl")
    ClientGooseControlBlock_setDatSet.argtypes = [ClientGooseControlBlock, String]
    ClientGooseControlBlock_setDatSet.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 748
if _libs["libiec61850.so"].has("ClientGooseControlBlock_getConfRev", "cdecl"):
    ClientGooseControlBlock_getConfRev = _libs["libiec61850.so"].get("ClientGooseControlBlock_getConfRev", "cdecl")
    ClientGooseControlBlock_getConfRev.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getConfRev.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 751
if _libs["libiec61850.so"].has("ClientGooseControlBlock_getNdsComm", "cdecl"):
    ClientGooseControlBlock_getNdsComm = _libs["libiec61850.so"].get("ClientGooseControlBlock_getNdsComm", "cdecl")
    ClientGooseControlBlock_getNdsComm.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getNdsComm.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 754
if _libs["libiec61850.so"].has("ClientGooseControlBlock_getMinTime", "cdecl"):
    ClientGooseControlBlock_getMinTime = _libs["libiec61850.so"].get("ClientGooseControlBlock_getMinTime", "cdecl")
    ClientGooseControlBlock_getMinTime.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getMinTime.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 757
if _libs["libiec61850.so"].has("ClientGooseControlBlock_getMaxTime", "cdecl"):
    ClientGooseControlBlock_getMaxTime = _libs["libiec61850.so"].get("ClientGooseControlBlock_getMaxTime", "cdecl")
    ClientGooseControlBlock_getMaxTime.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getMaxTime.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 760
if _libs["libiec61850.so"].has("ClientGooseControlBlock_getFixedOffs", "cdecl"):
    ClientGooseControlBlock_getFixedOffs = _libs["libiec61850.so"].get("ClientGooseControlBlock_getFixedOffs", "cdecl")
    ClientGooseControlBlock_getFixedOffs.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getFixedOffs.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 763
if _libs["libiec61850.so"].has("ClientGooseControlBlock_getDstAddress", "cdecl"):
    ClientGooseControlBlock_getDstAddress = _libs["libiec61850.so"].get("ClientGooseControlBlock_getDstAddress", "cdecl")
    ClientGooseControlBlock_getDstAddress.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDstAddress.restype = PhyComAddress

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 766
if _libs["libiec61850.so"].has("ClientGooseControlBlock_setDstAddress", "cdecl"):
    ClientGooseControlBlock_setDstAddress = _libs["libiec61850.so"].get("ClientGooseControlBlock_setDstAddress", "cdecl")
    ClientGooseControlBlock_setDstAddress.argtypes = [ClientGooseControlBlock, PhyComAddress]
    ClientGooseControlBlock_setDstAddress.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 768
if _libs["libiec61850.so"].has("ClientGooseControlBlock_getDstAddress_addr", "cdecl"):
    ClientGooseControlBlock_getDstAddress_addr = _libs["libiec61850.so"].get("ClientGooseControlBlock_getDstAddress_addr", "cdecl")
    ClientGooseControlBlock_getDstAddress_addr.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDstAddress_addr.restype = POINTER(MmsValue)

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 772
if _libs["libiec61850.so"].has("ClientGooseControlBlock_setDstAddress_addr", "cdecl"):
    ClientGooseControlBlock_setDstAddress_addr = _libs["libiec61850.so"].get("ClientGooseControlBlock_setDstAddress_addr", "cdecl")
    ClientGooseControlBlock_setDstAddress_addr.argtypes = [ClientGooseControlBlock, POINTER(MmsValue)]
    ClientGooseControlBlock_setDstAddress_addr.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 775
if _libs["libiec61850.so"].has("ClientGooseControlBlock_getDstAddress_priority", "cdecl"):
    ClientGooseControlBlock_getDstAddress_priority = _libs["libiec61850.so"].get("ClientGooseControlBlock_getDstAddress_priority", "cdecl")
    ClientGooseControlBlock_getDstAddress_priority.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDstAddress_priority.restype = uint8_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 778
if _libs["libiec61850.so"].has("ClientGooseControlBlock_setDstAddress_priority", "cdecl"):
    ClientGooseControlBlock_setDstAddress_priority = _libs["libiec61850.so"].get("ClientGooseControlBlock_setDstAddress_priority", "cdecl")
    ClientGooseControlBlock_setDstAddress_priority.argtypes = [ClientGooseControlBlock, uint8_t]
    ClientGooseControlBlock_setDstAddress_priority.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 781
if _libs["libiec61850.so"].has("ClientGooseControlBlock_getDstAddress_vid", "cdecl"):
    ClientGooseControlBlock_getDstAddress_vid = _libs["libiec61850.so"].get("ClientGooseControlBlock_getDstAddress_vid", "cdecl")
    ClientGooseControlBlock_getDstAddress_vid.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDstAddress_vid.restype = uint16_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 784
if _libs["libiec61850.so"].has("ClientGooseControlBlock_setDstAddress_vid", "cdecl"):
    ClientGooseControlBlock_setDstAddress_vid = _libs["libiec61850.so"].get("ClientGooseControlBlock_setDstAddress_vid", "cdecl")
    ClientGooseControlBlock_setDstAddress_vid.argtypes = [ClientGooseControlBlock, uint16_t]
    ClientGooseControlBlock_setDstAddress_vid.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 787
if _libs["libiec61850.so"].has("ClientGooseControlBlock_getDstAddress_appid", "cdecl"):
    ClientGooseControlBlock_getDstAddress_appid = _libs["libiec61850.so"].get("ClientGooseControlBlock_getDstAddress_appid", "cdecl")
    ClientGooseControlBlock_getDstAddress_appid.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDstAddress_appid.restype = uint16_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 790
if _libs["libiec61850.so"].has("ClientGooseControlBlock_setDstAddress_appid", "cdecl"):
    ClientGooseControlBlock_setDstAddress_appid = _libs["libiec61850.so"].get("ClientGooseControlBlock_setDstAddress_appid", "cdecl")
    ClientGooseControlBlock_setDstAddress_appid.argtypes = [ClientGooseControlBlock, uint16_t]
    ClientGooseControlBlock_setDstAddress_appid.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 826
if _libs["libiec61850.so"].has("IedConnection_getGoCBValues", "cdecl"):
    IedConnection_getGoCBValues = _libs["libiec61850.so"].get("IedConnection_getGoCBValues", "cdecl")
    IedConnection_getGoCBValues.argtypes = [IedConnection, POINTER(IedClientError), String, ClientGooseControlBlock]
    IedConnection_getGoCBValues.restype = ClientGooseControlBlock

IedConnection_GetGoCBValuesHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, ClientGooseControlBlock)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 829

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 861
if _libs["libiec61850.so"].has("IedConnection_getGoCBValuesAsync", "cdecl"):
    IedConnection_getGoCBValuesAsync = _libs["libiec61850.so"].get("IedConnection_getGoCBValuesAsync", "cdecl")
    IedConnection_getGoCBValuesAsync.argtypes = [IedConnection, POINTER(IedClientError), String, ClientGooseControlBlock, IedConnection_GetGoCBValuesHandler, POINTER(None)]
    IedConnection_getGoCBValuesAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 886
if _libs["libiec61850.so"].has("IedConnection_setGoCBValues", "cdecl"):
    IedConnection_setGoCBValues = _libs["libiec61850.so"].get("IedConnection_setGoCBValues", "cdecl")
    IedConnection_setGoCBValues.argtypes = [IedConnection, POINTER(IedClientError), ClientGooseControlBlock, uint32_t, c_bool]
    IedConnection_setGoCBValues.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 915
if _libs["libiec61850.so"].has("IedConnection_setGoCBValuesAsync", "cdecl"):
    IedConnection_setGoCBValuesAsync = _libs["libiec61850.so"].get("IedConnection_setGoCBValuesAsync", "cdecl")
    IedConnection_setGoCBValuesAsync.argtypes = [IedConnection, POINTER(IedClientError), ClientGooseControlBlock, uint32_t, c_bool, IedConnection_GenericServiceHandler, POINTER(None)]
    IedConnection_setGoCBValuesAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 941
if _libs["libiec61850.so"].has("IedConnection_readObject", "cdecl"):
    IedConnection_readObject = _libs["libiec61850.so"].get("IedConnection_readObject", "cdecl")
    IedConnection_readObject.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readObject.restype = POINTER(MmsValue)

IedConnection_ReadObjectHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, POINTER(MmsValue))# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 945

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 960
if _libs["libiec61850.so"].has("IedConnection_readObjectAsync", "cdecl"):
    IedConnection_readObjectAsync = _libs["libiec61850.so"].get("IedConnection_readObjectAsync", "cdecl")
    IedConnection_readObjectAsync.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, IedConnection_ReadObjectHandler, POINTER(None)]
    IedConnection_readObjectAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 973
if _libs["libiec61850.so"].has("IedConnection_writeObject", "cdecl"):
    IedConnection_writeObject = _libs["libiec61850.so"].get("IedConnection_writeObject", "cdecl")
    IedConnection_writeObject.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, POINTER(MmsValue)]
    IedConnection_writeObject.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 990
if _libs["libiec61850.so"].has("IedConnection_writeObjectAsync", "cdecl"):
    IedConnection_writeObjectAsync = _libs["libiec61850.so"].get("IedConnection_writeObjectAsync", "cdecl")
    IedConnection_writeObjectAsync.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, POINTER(MmsValue), IedConnection_GenericServiceHandler, POINTER(None)]
    IedConnection_writeObjectAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1002
if _libs["libiec61850.so"].has("IedConnection_readBooleanValue", "cdecl"):
    IedConnection_readBooleanValue = _libs["libiec61850.so"].get("IedConnection_readBooleanValue", "cdecl")
    IedConnection_readBooleanValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readBooleanValue.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1013
if _libs["libiec61850.so"].has("IedConnection_readFloatValue", "cdecl"):
    IedConnection_readFloatValue = _libs["libiec61850.so"].get("IedConnection_readFloatValue", "cdecl")
    IedConnection_readFloatValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readFloatValue.restype = c_float

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1027
if _libs["libiec61850.so"].has("IedConnection_readStringValue", "cdecl"):
    IedConnection_readStringValue = _libs["libiec61850.so"].get("IedConnection_readStringValue", "cdecl")
    IedConnection_readStringValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    if sizeof(c_int) == sizeof(c_void_p):
        IedConnection_readStringValue.restype = ReturnString
    else:
        IedConnection_readStringValue.restype = String
        IedConnection_readStringValue.errcheck = ReturnString

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1041
if _libs["libiec61850.so"].has("IedConnection_readInt32Value", "cdecl"):
    IedConnection_readInt32Value = _libs["libiec61850.so"].get("IedConnection_readInt32Value", "cdecl")
    IedConnection_readInt32Value.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readInt32Value.restype = c_int32

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1054
if _libs["libiec61850.so"].has("IedConnection_readInt64Value", "cdecl"):
    IedConnection_readInt64Value = _libs["libiec61850.so"].get("IedConnection_readInt64Value", "cdecl")
    IedConnection_readInt64Value.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readInt64Value.restype = c_int64

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1067
if _libs["libiec61850.so"].has("IedConnection_readUnsigned32Value", "cdecl"):
    IedConnection_readUnsigned32Value = _libs["libiec61850.so"].get("IedConnection_readUnsigned32Value", "cdecl")
    IedConnection_readUnsigned32Value.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readUnsigned32Value.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1084
if _libs["libiec61850.so"].has("IedConnection_readTimestampValue", "cdecl"):
    IedConnection_readTimestampValue = _libs["libiec61850.so"].get("IedConnection_readTimestampValue", "cdecl")
    IedConnection_readTimestampValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, POINTER(Timestamp)]
    IedConnection_readTimestampValue.restype = POINTER(Timestamp)

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1099
if _libs["libiec61850.so"].has("IedConnection_readQualityValue", "cdecl"):
    IedConnection_readQualityValue = _libs["libiec61850.so"].get("IedConnection_readQualityValue", "cdecl")
    IedConnection_readQualityValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readQualityValue.restype = Quality

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1111
if _libs["libiec61850.so"].has("IedConnection_writeBooleanValue", "cdecl"):
    IedConnection_writeBooleanValue = _libs["libiec61850.so"].get("IedConnection_writeBooleanValue", "cdecl")
    IedConnection_writeBooleanValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, c_bool]
    IedConnection_writeBooleanValue.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1124
if _libs["libiec61850.so"].has("IedConnection_writeInt32Value", "cdecl"):
    IedConnection_writeInt32Value = _libs["libiec61850.so"].get("IedConnection_writeInt32Value", "cdecl")
    IedConnection_writeInt32Value.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, c_int32]
    IedConnection_writeInt32Value.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1137
if _libs["libiec61850.so"].has("IedConnection_writeUnsigned32Value", "cdecl"):
    IedConnection_writeUnsigned32Value = _libs["libiec61850.so"].get("IedConnection_writeUnsigned32Value", "cdecl")
    IedConnection_writeUnsigned32Value.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, uint32_t]
    IedConnection_writeUnsigned32Value.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1150
if _libs["libiec61850.so"].has("IedConnection_writeFloatValue", "cdecl"):
    IedConnection_writeFloatValue = _libs["libiec61850.so"].get("IedConnection_writeFloatValue", "cdecl")
    IedConnection_writeFloatValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, c_float]
    IedConnection_writeFloatValue.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1154
if _libs["libiec61850.so"].has("IedConnection_writeVisibleStringValue", "cdecl"):
    IedConnection_writeVisibleStringValue = _libs["libiec61850.so"].get("IedConnection_writeVisibleStringValue", "cdecl")
    IedConnection_writeVisibleStringValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, String]
    IedConnection_writeVisibleStringValue.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1158
if _libs["libiec61850.so"].has("IedConnection_writeOctetString", "cdecl"):
    IedConnection_writeOctetString = _libs["libiec61850.so"].get("IedConnection_writeOctetString", "cdecl")
    IedConnection_writeOctetString.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, POINTER(uint8_t), c_int]
    IedConnection_writeOctetString.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1207
if _libs["libiec61850.so"].has("IedConnection_getRCBValues", "cdecl"):
    IedConnection_getRCBValues = _libs["libiec61850.so"].get("IedConnection_getRCBValues", "cdecl")
    IedConnection_getRCBValues.argtypes = [IedConnection, POINTER(IedClientError), String, ClientReportControlBlock]
    IedConnection_getRCBValues.restype = ClientReportControlBlock

IedConnection_GetRCBValuesHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, ClientReportControlBlock)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1211

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1214
if _libs["libiec61850.so"].has("IedConnection_getRCBValuesAsync", "cdecl"):
    IedConnection_getRCBValuesAsync = _libs["libiec61850.so"].get("IedConnection_getRCBValuesAsync", "cdecl")
    IedConnection_getRCBValuesAsync.argtypes = [IedConnection, POINTER(IedClientError), String, ClientReportControlBlock, IedConnection_GetRCBValuesHandler, POINTER(None)]
    IedConnection_getRCBValuesAsync.restype = uint32_t

ReasonForInclusion = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1218

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1313
if _libs["libiec61850.so"].has("IedConnection_setRCBValues", "cdecl"):
    IedConnection_setRCBValues = _libs["libiec61850.so"].get("IedConnection_setRCBValues", "cdecl")
    IedConnection_setRCBValues.argtypes = [IedConnection, POINTER(IedClientError), ClientReportControlBlock, uint32_t, c_bool]
    IedConnection_setRCBValues.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1317
if _libs["libiec61850.so"].has("IedConnection_setRCBValuesAsync", "cdecl"):
    IedConnection_setRCBValuesAsync = _libs["libiec61850.so"].get("IedConnection_setRCBValuesAsync", "cdecl")
    IedConnection_setRCBValuesAsync.argtypes = [IedConnection, POINTER(IedClientError), ClientReportControlBlock, uint32_t, c_bool, IedConnection_GenericServiceHandler, POINTER(None)]
    IedConnection_setRCBValuesAsync.restype = uint32_t

ReportCallbackFunction = CFUNCTYPE(UNCHECKED(None), POINTER(None), ClientReport)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1326

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1350
if _libs["libiec61850.so"].has("IedConnection_installReportHandler", "cdecl"):
    IedConnection_installReportHandler = _libs["libiec61850.so"].get("IedConnection_installReportHandler", "cdecl")
    IedConnection_installReportHandler.argtypes = [IedConnection, String, String, ReportCallbackFunction, POINTER(None)]
    IedConnection_installReportHandler.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1362
if _libs["libiec61850.so"].has("IedConnection_uninstallReportHandler", "cdecl"):
    IedConnection_uninstallReportHandler = _libs["libiec61850.so"].get("IedConnection_uninstallReportHandler", "cdecl")
    IedConnection_uninstallReportHandler.argtypes = [IedConnection, String]
    IedConnection_uninstallReportHandler.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1376
if _libs["libiec61850.so"].has("IedConnection_triggerGIReport", "cdecl"):
    IedConnection_triggerGIReport = _libs["libiec61850.so"].get("IedConnection_triggerGIReport", "cdecl")
    IedConnection_triggerGIReport.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_triggerGIReport.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1390
if _libs["libiec61850.so"].has("ClientReport_getDataSetName", "cdecl"):
    ClientReport_getDataSetName = _libs["libiec61850.so"].get("ClientReport_getDataSetName", "cdecl")
    ClientReport_getDataSetName.argtypes = [ClientReport]
    ClientReport_getDataSetName.restype = c_char_p

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1403
if _libs["libiec61850.so"].has("ClientReport_getDataSetValues", "cdecl"):
    ClientReport_getDataSetValues = _libs["libiec61850.so"].get("ClientReport_getDataSetValues", "cdecl")
    ClientReport_getDataSetValues.argtypes = [ClientReport]
    ClientReport_getDataSetValues.restype = POINTER(MmsValue)

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1412
if _libs["libiec61850.so"].has("ClientReport_getRcbReference", "cdecl"):
    ClientReport_getRcbReference = _libs["libiec61850.so"].get("ClientReport_getRcbReference", "cdecl")
    ClientReport_getRcbReference.argtypes = [ClientReport]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientReport_getRcbReference.restype = ReturnString
    else:
        ClientReport_getRcbReference.restype = String
        ClientReport_getRcbReference.errcheck = ReturnString

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1421
if _libs["libiec61850.so"].has("ClientReport_getRptId", "cdecl"):
    ClientReport_getRptId = _libs["libiec61850.so"].get("ClientReport_getRptId", "cdecl")
    ClientReport_getRptId.argtypes = [ClientReport]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientReport_getRptId.restype = ReturnString
    else:
        ClientReport_getRptId.restype = String
        ClientReport_getRptId.errcheck = ReturnString

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1433
if _libs["libiec61850.so"].has("ClientReport_getReasonForInclusion", "cdecl"):
    ClientReport_getReasonForInclusion = _libs["libiec61850.so"].get("ClientReport_getReasonForInclusion", "cdecl")
    ClientReport_getReasonForInclusion.argtypes = [ClientReport, c_int]
    ClientReport_getReasonForInclusion.restype = ReasonForInclusion

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1444
if _libs["libiec61850.so"].has("ClientReport_getEntryId", "cdecl"):
    ClientReport_getEntryId = _libs["libiec61850.so"].get("ClientReport_getEntryId", "cdecl")
    ClientReport_getEntryId.argtypes = [ClientReport]
    ClientReport_getEntryId.restype = POINTER(MmsValue)

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1455
if _libs["libiec61850.so"].has("ClientReport_hasTimestamp", "cdecl"):
    ClientReport_hasTimestamp = _libs["libiec61850.so"].get("ClientReport_hasTimestamp", "cdecl")
    ClientReport_hasTimestamp.argtypes = [ClientReport]
    ClientReport_hasTimestamp.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1465
if _libs["libiec61850.so"].has("ClientReport_hasSeqNum", "cdecl"):
    ClientReport_hasSeqNum = _libs["libiec61850.so"].get("ClientReport_hasSeqNum", "cdecl")
    ClientReport_hasSeqNum.argtypes = [ClientReport]
    ClientReport_hasSeqNum.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1477
if _libs["libiec61850.so"].has("ClientReport_getSeqNum", "cdecl"):
    ClientReport_getSeqNum = _libs["libiec61850.so"].get("ClientReport_getSeqNum", "cdecl")
    ClientReport_getSeqNum.argtypes = [ClientReport]
    ClientReport_getSeqNum.restype = uint16_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1487
if _libs["libiec61850.so"].has("ClientReport_hasDataSetName", "cdecl"):
    ClientReport_hasDataSetName = _libs["libiec61850.so"].get("ClientReport_hasDataSetName", "cdecl")
    ClientReport_hasDataSetName.argtypes = [ClientReport]
    ClientReport_hasDataSetName.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1497
if _libs["libiec61850.so"].has("ClientReport_hasReasonForInclusion", "cdecl"):
    ClientReport_hasReasonForInclusion = _libs["libiec61850.so"].get("ClientReport_hasReasonForInclusion", "cdecl")
    ClientReport_hasReasonForInclusion.argtypes = [ClientReport]
    ClientReport_hasReasonForInclusion.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1507
if _libs["libiec61850.so"].has("ClientReport_hasConfRev", "cdecl"):
    ClientReport_hasConfRev = _libs["libiec61850.so"].get("ClientReport_hasConfRev", "cdecl")
    ClientReport_hasConfRev.argtypes = [ClientReport]
    ClientReport_hasConfRev.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1519
if _libs["libiec61850.so"].has("ClientReport_getConfRev", "cdecl"):
    ClientReport_getConfRev = _libs["libiec61850.so"].get("ClientReport_getConfRev", "cdecl")
    ClientReport_getConfRev.argtypes = [ClientReport]
    ClientReport_getConfRev.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1529
if _libs["libiec61850.so"].has("ClientReport_hasBufOvfl", "cdecl"):
    ClientReport_hasBufOvfl = _libs["libiec61850.so"].get("ClientReport_hasBufOvfl", "cdecl")
    ClientReport_hasBufOvfl.argtypes = [ClientReport]
    ClientReport_hasBufOvfl.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1539
if _libs["libiec61850.so"].has("ClientReport_getBufOvfl", "cdecl"):
    ClientReport_getBufOvfl = _libs["libiec61850.so"].get("ClientReport_getBufOvfl", "cdecl")
    ClientReport_getBufOvfl.argtypes = [ClientReport]
    ClientReport_getBufOvfl.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1549
if _libs["libiec61850.so"].has("ClientReport_hasDataReference", "cdecl"):
    ClientReport_hasDataReference = _libs["libiec61850.so"].get("ClientReport_hasDataReference", "cdecl")
    ClientReport_hasDataReference.argtypes = [ClientReport]
    ClientReport_hasDataReference.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1564
if _libs["libiec61850.so"].has("ClientReport_getDataReference", "cdecl"):
    ClientReport_getDataReference = _libs["libiec61850.so"].get("ClientReport_getDataReference", "cdecl")
    ClientReport_getDataReference.argtypes = [ClientReport, c_int]
    ClientReport_getDataReference.restype = c_char_p

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1579
if _libs["libiec61850.so"].has("ClientReport_getTimestamp", "cdecl"):
    ClientReport_getTimestamp = _libs["libiec61850.so"].get("ClientReport_getTimestamp", "cdecl")
    ClientReport_getTimestamp.argtypes = [ClientReport]
    ClientReport_getTimestamp.restype = uint64_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1589
if _libs["libiec61850.so"].has("ClientReport_hasSubSeqNum", "cdecl"):
    ClientReport_hasSubSeqNum = _libs["libiec61850.so"].get("ClientReport_hasSubSeqNum", "cdecl")
    ClientReport_hasSubSeqNum.argtypes = [ClientReport]
    ClientReport_hasSubSeqNum.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1602
if _libs["libiec61850.so"].has("ClientReport_getSubSeqNum", "cdecl"):
    ClientReport_getSubSeqNum = _libs["libiec61850.so"].get("ClientReport_getSubSeqNum", "cdecl")
    ClientReport_getSubSeqNum.argtypes = [ClientReport]
    ClientReport_getSubSeqNum.restype = uint16_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1615
if _libs["libiec61850.so"].has("ClientReport_getMoreSeqmentsFollow", "cdecl"):
    ClientReport_getMoreSeqmentsFollow = _libs["libiec61850.so"].get("ClientReport_getMoreSeqmentsFollow", "cdecl")
    ClientReport_getMoreSeqmentsFollow.argtypes = [ClientReport]
    ClientReport_getMoreSeqmentsFollow.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1624
if _libs["libiec61850.so"].has("ReasonForInclusion_getValueAsString", "cdecl"):
    ReasonForInclusion_getValueAsString = _libs["libiec61850.so"].get("ReasonForInclusion_getValueAsString", "cdecl")
    ReasonForInclusion_getValueAsString.argtypes = [ReasonForInclusion]
    if sizeof(c_int) == sizeof(c_void_p):
        ReasonForInclusion_getValueAsString.restype = ReturnString
    else:
        ReasonForInclusion_getValueAsString.restype = String
        ReasonForInclusion_getValueAsString.errcheck = ReturnString

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1632
if _libs["libiec61850.so"].has("ClientReportControlBlock_create", "cdecl"):
    ClientReportControlBlock_create = _libs["libiec61850.so"].get("ClientReportControlBlock_create", "cdecl")
    ClientReportControlBlock_create.argtypes = [String]
    ClientReportControlBlock_create.restype = ClientReportControlBlock

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1635
if _libs["libiec61850.so"].has("ClientReportControlBlock_destroy", "cdecl"):
    ClientReportControlBlock_destroy = _libs["libiec61850.so"].get("ClientReportControlBlock_destroy", "cdecl")
    ClientReportControlBlock_destroy.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_destroy.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1637
if _libs["libiec61850.so"].has("ClientReportControlBlock_getObjectReference", "cdecl"):
    ClientReportControlBlock_getObjectReference = _libs["libiec61850.so"].get("ClientReportControlBlock_getObjectReference", "cdecl")
    ClientReportControlBlock_getObjectReference.argtypes = [ClientReportControlBlock]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientReportControlBlock_getObjectReference.restype = ReturnString
    else:
        ClientReportControlBlock_getObjectReference.restype = String
        ClientReportControlBlock_getObjectReference.errcheck = ReturnString

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1641
if _libs["libiec61850.so"].has("ClientReportControlBlock_isBuffered", "cdecl"):
    ClientReportControlBlock_isBuffered = _libs["libiec61850.so"].get("ClientReportControlBlock_isBuffered", "cdecl")
    ClientReportControlBlock_isBuffered.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_isBuffered.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1643
if _libs["libiec61850.so"].has("ClientReportControlBlock_getRptId", "cdecl"):
    ClientReportControlBlock_getRptId = _libs["libiec61850.so"].get("ClientReportControlBlock_getRptId", "cdecl")
    ClientReportControlBlock_getRptId.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getRptId.restype = c_char_p

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1647
if _libs["libiec61850.so"].has("ClientReportControlBlock_setRptId", "cdecl"):
    ClientReportControlBlock_setRptId = _libs["libiec61850.so"].get("ClientReportControlBlock_setRptId", "cdecl")
    ClientReportControlBlock_setRptId.argtypes = [ClientReportControlBlock, String]
    ClientReportControlBlock_setRptId.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1650
if _libs["libiec61850.so"].has("ClientReportControlBlock_getRptEna", "cdecl"):
    ClientReportControlBlock_getRptEna = _libs["libiec61850.so"].get("ClientReportControlBlock_getRptEna", "cdecl")
    ClientReportControlBlock_getRptEna.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getRptEna.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1653
if _libs["libiec61850.so"].has("ClientReportControlBlock_setRptEna", "cdecl"):
    ClientReportControlBlock_setRptEna = _libs["libiec61850.so"].get("ClientReportControlBlock_setRptEna", "cdecl")
    ClientReportControlBlock_setRptEna.argtypes = [ClientReportControlBlock, c_bool]
    ClientReportControlBlock_setRptEna.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1656
if _libs["libiec61850.so"].has("ClientReportControlBlock_getResv", "cdecl"):
    ClientReportControlBlock_getResv = _libs["libiec61850.so"].get("ClientReportControlBlock_getResv", "cdecl")
    ClientReportControlBlock_getResv.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getResv.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1659
if _libs["libiec61850.so"].has("ClientReportControlBlock_setResv", "cdecl"):
    ClientReportControlBlock_setResv = _libs["libiec61850.so"].get("ClientReportControlBlock_setResv", "cdecl")
    ClientReportControlBlock_setResv.argtypes = [ClientReportControlBlock, c_bool]
    ClientReportControlBlock_setResv.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1661
if _libs["libiec61850.so"].has("ClientReportControlBlock_getDataSetReference", "cdecl"):
    ClientReportControlBlock_getDataSetReference = _libs["libiec61850.so"].get("ClientReportControlBlock_getDataSetReference", "cdecl")
    ClientReportControlBlock_getDataSetReference.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getDataSetReference.restype = c_char_p

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1681
if _libs["libiec61850.so"].has("ClientReportControlBlock_setDataSetReference", "cdecl"):
    ClientReportControlBlock_setDataSetReference = _libs["libiec61850.so"].get("ClientReportControlBlock_setDataSetReference", "cdecl")
    ClientReportControlBlock_setDataSetReference.argtypes = [ClientReportControlBlock, String]
    ClientReportControlBlock_setDataSetReference.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1684
if _libs["libiec61850.so"].has("ClientReportControlBlock_getConfRev", "cdecl"):
    ClientReportControlBlock_getConfRev = _libs["libiec61850.so"].get("ClientReportControlBlock_getConfRev", "cdecl")
    ClientReportControlBlock_getConfRev.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getConfRev.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1694
if _libs["libiec61850.so"].has("ClientReportControlBlock_getOptFlds", "cdecl"):
    ClientReportControlBlock_getOptFlds = _libs["libiec61850.so"].get("ClientReportControlBlock_getOptFlds", "cdecl")
    ClientReportControlBlock_getOptFlds.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getOptFlds.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1703
if _libs["libiec61850.so"].has("ClientReportControlBlock_setOptFlds", "cdecl"):
    ClientReportControlBlock_setOptFlds = _libs["libiec61850.so"].get("ClientReportControlBlock_setOptFlds", "cdecl")
    ClientReportControlBlock_setOptFlds.argtypes = [ClientReportControlBlock, c_int]
    ClientReportControlBlock_setOptFlds.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1714
if _libs["libiec61850.so"].has("ClientReportControlBlock_getBufTm", "cdecl"):
    ClientReportControlBlock_getBufTm = _libs["libiec61850.so"].get("ClientReportControlBlock_getBufTm", "cdecl")
    ClientReportControlBlock_getBufTm.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getBufTm.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1726
if _libs["libiec61850.so"].has("ClientReportControlBlock_setBufTm", "cdecl"):
    ClientReportControlBlock_setBufTm = _libs["libiec61850.so"].get("ClientReportControlBlock_setBufTm", "cdecl")
    ClientReportControlBlock_setBufTm.argtypes = [ClientReportControlBlock, uint32_t]
    ClientReportControlBlock_setBufTm.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1729
if _libs["libiec61850.so"].has("ClientReportControlBlock_getSqNum", "cdecl"):
    ClientReportControlBlock_getSqNum = _libs["libiec61850.so"].get("ClientReportControlBlock_getSqNum", "cdecl")
    ClientReportControlBlock_getSqNum.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getSqNum.restype = uint16_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1732
if _libs["libiec61850.so"].has("ClientReportControlBlock_getTrgOps", "cdecl"):
    ClientReportControlBlock_getTrgOps = _libs["libiec61850.so"].get("ClientReportControlBlock_getTrgOps", "cdecl")
    ClientReportControlBlock_getTrgOps.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getTrgOps.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1735
if _libs["libiec61850.so"].has("ClientReportControlBlock_setTrgOps", "cdecl"):
    ClientReportControlBlock_setTrgOps = _libs["libiec61850.so"].get("ClientReportControlBlock_setTrgOps", "cdecl")
    ClientReportControlBlock_setTrgOps.argtypes = [ClientReportControlBlock, c_int]
    ClientReportControlBlock_setTrgOps.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1738
if _libs["libiec61850.so"].has("ClientReportControlBlock_getIntgPd", "cdecl"):
    ClientReportControlBlock_getIntgPd = _libs["libiec61850.so"].get("ClientReportControlBlock_getIntgPd", "cdecl")
    ClientReportControlBlock_getIntgPd.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getIntgPd.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1741
if _libs["libiec61850.so"].has("ClientReportControlBlock_setIntgPd", "cdecl"):
    ClientReportControlBlock_setIntgPd = _libs["libiec61850.so"].get("ClientReportControlBlock_setIntgPd", "cdecl")
    ClientReportControlBlock_setIntgPd.argtypes = [ClientReportControlBlock, uint32_t]
    ClientReportControlBlock_setIntgPd.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1744
if _libs["libiec61850.so"].has("ClientReportControlBlock_getGI", "cdecl"):
    ClientReportControlBlock_getGI = _libs["libiec61850.so"].get("ClientReportControlBlock_getGI", "cdecl")
    ClientReportControlBlock_getGI.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getGI.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1747
if _libs["libiec61850.so"].has("ClientReportControlBlock_setGI", "cdecl"):
    ClientReportControlBlock_setGI = _libs["libiec61850.so"].get("ClientReportControlBlock_setGI", "cdecl")
    ClientReportControlBlock_setGI.argtypes = [ClientReportControlBlock, c_bool]
    ClientReportControlBlock_setGI.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1750
if _libs["libiec61850.so"].has("ClientReportControlBlock_getPurgeBuf", "cdecl"):
    ClientReportControlBlock_getPurgeBuf = _libs["libiec61850.so"].get("ClientReportControlBlock_getPurgeBuf", "cdecl")
    ClientReportControlBlock_getPurgeBuf.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getPurgeBuf.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1760
if _libs["libiec61850.so"].has("ClientReportControlBlock_setPurgeBuf", "cdecl"):
    ClientReportControlBlock_setPurgeBuf = _libs["libiec61850.so"].get("ClientReportControlBlock_setPurgeBuf", "cdecl")
    ClientReportControlBlock_setPurgeBuf.argtypes = [ClientReportControlBlock, c_bool]
    ClientReportControlBlock_setPurgeBuf.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1768
if _libs["libiec61850.so"].has("ClientReportControlBlock_hasResvTms", "cdecl"):
    ClientReportControlBlock_hasResvTms = _libs["libiec61850.so"].get("ClientReportControlBlock_hasResvTms", "cdecl")
    ClientReportControlBlock_hasResvTms.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_hasResvTms.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1771
if _libs["libiec61850.so"].has("ClientReportControlBlock_getResvTms", "cdecl"):
    ClientReportControlBlock_getResvTms = _libs["libiec61850.so"].get("ClientReportControlBlock_getResvTms", "cdecl")
    ClientReportControlBlock_getResvTms.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getResvTms.restype = c_int16

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1774
if _libs["libiec61850.so"].has("ClientReportControlBlock_setResvTms", "cdecl"):
    ClientReportControlBlock_setResvTms = _libs["libiec61850.so"].get("ClientReportControlBlock_setResvTms", "cdecl")
    ClientReportControlBlock_setResvTms.argtypes = [ClientReportControlBlock, c_int16]
    ClientReportControlBlock_setResvTms.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1776
if _libs["libiec61850.so"].has("ClientReportControlBlock_getEntryId", "cdecl"):
    ClientReportControlBlock_getEntryId = _libs["libiec61850.so"].get("ClientReportControlBlock_getEntryId", "cdecl")
    ClientReportControlBlock_getEntryId.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getEntryId.restype = POINTER(MmsValue)

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1780
if _libs["libiec61850.so"].has("ClientReportControlBlock_setEntryId", "cdecl"):
    ClientReportControlBlock_setEntryId = _libs["libiec61850.so"].get("ClientReportControlBlock_setEntryId", "cdecl")
    ClientReportControlBlock_setEntryId.argtypes = [ClientReportControlBlock, POINTER(MmsValue)]
    ClientReportControlBlock_setEntryId.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1783
if _libs["libiec61850.so"].has("ClientReportControlBlock_getEntryTime", "cdecl"):
    ClientReportControlBlock_getEntryTime = _libs["libiec61850.so"].get("ClientReportControlBlock_getEntryTime", "cdecl")
    ClientReportControlBlock_getEntryTime.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getEntryTime.restype = uint64_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1785
if _libs["libiec61850.so"].has("ClientReportControlBlock_getOwner", "cdecl"):
    ClientReportControlBlock_getOwner = _libs["libiec61850.so"].get("ClientReportControlBlock_getOwner", "cdecl")
    ClientReportControlBlock_getOwner.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getOwner.restype = POINTER(MmsValue)

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1819
if _libs["libiec61850.so"].has("IedConnection_readDataSetValues", "cdecl"):
    IedConnection_readDataSetValues = _libs["libiec61850.so"].get("IedConnection_readDataSetValues", "cdecl")
    IedConnection_readDataSetValues.argtypes = [IedConnection, POINTER(IedClientError), String, ClientDataSet]
    IedConnection_readDataSetValues.restype = ClientDataSet

IedConnection_ReadDataSetHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, ClientDataSet)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1822

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1844
if _libs["libiec61850.so"].has("IedConnection_readDataSetValuesAsync", "cdecl"):
    IedConnection_readDataSetValuesAsync = _libs["libiec61850.so"].get("IedConnection_readDataSetValuesAsync", "cdecl")
    IedConnection_readDataSetValuesAsync.argtypes = [IedConnection, POINTER(IedClientError), String, ClientDataSet, IedConnection_ReadDataSetHandler, POINTER(None)]
    IedConnection_readDataSetValuesAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1865
if _libs["libiec61850.so"].has("IedConnection_createDataSet", "cdecl"):
    IedConnection_createDataSet = _libs["libiec61850.so"].get("IedConnection_createDataSet", "cdecl")
    IedConnection_createDataSet.argtypes = [IedConnection, POINTER(IedClientError), String, LinkedList]
    IedConnection_createDataSet.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1889
if _libs["libiec61850.so"].has("IedConnection_createDataSetAsync", "cdecl"):
    IedConnection_createDataSetAsync = _libs["libiec61850.so"].get("IedConnection_createDataSetAsync", "cdecl")
    IedConnection_createDataSetAsync.argtypes = [IedConnection, POINTER(IedClientError), String, LinkedList, IedConnection_GenericServiceHandler, POINTER(None)]
    IedConnection_createDataSetAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1906
if _libs["libiec61850.so"].has("IedConnection_deleteDataSet", "cdecl"):
    IedConnection_deleteDataSet = _libs["libiec61850.so"].get("IedConnection_deleteDataSet", "cdecl")
    IedConnection_deleteDataSet.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_deleteDataSet.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1926
if _libs["libiec61850.so"].has("IedConnection_deleteDataSetAsync", "cdecl"):
    IedConnection_deleteDataSetAsync = _libs["libiec61850.so"].get("IedConnection_deleteDataSetAsync", "cdecl")
    IedConnection_deleteDataSetAsync.argtypes = [IedConnection, POINTER(IedClientError), String, IedConnection_GenericServiceHandler, POINTER(None)]
    IedConnection_deleteDataSetAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1944
if _libs["libiec61850.so"].has("IedConnection_getDataSetDirectory", "cdecl"):
    IedConnection_getDataSetDirectory = _libs["libiec61850.so"].get("IedConnection_getDataSetDirectory", "cdecl")
    IedConnection_getDataSetDirectory.argtypes = [IedConnection, POINTER(IedClientError), String, POINTER(c_bool)]
    IedConnection_getDataSetDirectory.restype = LinkedList

IedConnection_GetDataSetDirectoryHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, LinkedList, c_bool)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1954

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1971
if _libs["libiec61850.so"].has("IedConnection_getDataSetDirectoryAsync", "cdecl"):
    IedConnection_getDataSetDirectoryAsync = _libs["libiec61850.so"].get("IedConnection_getDataSetDirectoryAsync", "cdecl")
    IedConnection_getDataSetDirectoryAsync.argtypes = [IedConnection, POINTER(IedClientError), String, IedConnection_GetDataSetDirectoryHandler, POINTER(None)]
    IedConnection_getDataSetDirectoryAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1990
if _libs["libiec61850.so"].has("IedConnection_writeDataSetValues", "cdecl"):
    IedConnection_writeDataSetValues = _libs["libiec61850.so"].get("IedConnection_writeDataSetValues", "cdecl")
    IedConnection_writeDataSetValues.argtypes = [IedConnection, POINTER(IedClientError), String, LinkedList, POINTER(LinkedList)]
    IedConnection_writeDataSetValues.restype = None

IedConnection_WriteDataSetHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, LinkedList)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2002

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2026
if _libs["libiec61850.so"].has("IedConnection_writeDataSetValuesAsync", "cdecl"):
    IedConnection_writeDataSetValuesAsync = _libs["libiec61850.so"].get("IedConnection_writeDataSetValuesAsync", "cdecl")
    IedConnection_writeDataSetValuesAsync.argtypes = [IedConnection, POINTER(IedClientError), String, LinkedList, IedConnection_WriteDataSetHandler, POINTER(None)]
    IedConnection_writeDataSetValuesAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2043
if _libs["libiec61850.so"].has("ClientDataSet_destroy", "cdecl"):
    ClientDataSet_destroy = _libs["libiec61850.so"].get("ClientDataSet_destroy", "cdecl")
    ClientDataSet_destroy.argtypes = [ClientDataSet]
    ClientDataSet_destroy.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2059
if _libs["libiec61850.so"].has("ClientDataSet_getValues", "cdecl"):
    ClientDataSet_getValues = _libs["libiec61850.so"].get("ClientDataSet_getValues", "cdecl")
    ClientDataSet_getValues.argtypes = [ClientDataSet]
    ClientDataSet_getValues.restype = POINTER(MmsValue)

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2069
if _libs["libiec61850.so"].has("ClientDataSet_getReference", "cdecl"):
    ClientDataSet_getReference = _libs["libiec61850.so"].get("ClientDataSet_getReference", "cdecl")
    ClientDataSet_getReference.argtypes = [ClientDataSet]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientDataSet_getReference.restype = ReturnString
    else:
        ClientDataSet_getReference.restype = String
        ClientDataSet_getReference.errcheck = ReturnString

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2080
if _libs["libiec61850.so"].has("ClientDataSet_getDataSetSize", "cdecl"):
    ClientDataSet_getDataSetSize = _libs["libiec61850.so"].get("ClientDataSet_getDataSetSize", "cdecl")
    ClientDataSet_getDataSetSize.argtypes = [ClientDataSet]
    ClientDataSet_getDataSetSize.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2094
class struct_sControlObjectClient(Structure):
    pass

ControlObjectClient = POINTER(struct_sControlObjectClient)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2094

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2113
if _libs["libiec61850.so"].has("ControlObjectClient_create", "cdecl"):
    ControlObjectClient_create = _libs["libiec61850.so"].get("ControlObjectClient_create", "cdecl")
    ControlObjectClient_create.argtypes = [String, IedConnection]
    ControlObjectClient_create.restype = ControlObjectClient

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2128
if _libs["libiec61850.so"].has("ControlObjectClient_createEx", "cdecl"):
    ControlObjectClient_createEx = _libs["libiec61850.so"].get("ControlObjectClient_createEx", "cdecl")
    ControlObjectClient_createEx.argtypes = [String, IedConnection, ControlModel, POINTER(MmsVariableSpecification)]
    ControlObjectClient_createEx.restype = ControlObjectClient

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2136
if _libs["libiec61850.so"].has("ControlObjectClient_destroy", "cdecl"):
    ControlObjectClient_destroy = _libs["libiec61850.so"].get("ControlObjectClient_destroy", "cdecl")
    ControlObjectClient_destroy.argtypes = [ControlObjectClient]
    ControlObjectClient_destroy.restype = None

enum_anon_46 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2146

CONTROL_ACTION_TYPE_SELECT = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2146

CONTROL_ACTION_TYPE_OPERATE = 1# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2146

CONTROL_ACTION_TYPE_CANCEL = 2# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2146

ControlActionType = enum_anon_46# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2146

ControlObjectClient_ControlActionHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, ControlActionType, c_bool)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2165

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2174
if _libs["libiec61850.so"].has("ControlObjectClient_getObjectReference", "cdecl"):
    ControlObjectClient_getObjectReference = _libs["libiec61850.so"].get("ControlObjectClient_getObjectReference", "cdecl")
    ControlObjectClient_getObjectReference.argtypes = [ControlObjectClient]
    ControlObjectClient_getObjectReference.restype = c_char_p

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2185
if _libs["libiec61850.so"].has("ControlObjectClient_getControlModel", "cdecl"):
    ControlObjectClient_getControlModel = _libs["libiec61850.so"].get("ControlObjectClient_getControlModel", "cdecl")
    ControlObjectClient_getControlModel.argtypes = [ControlObjectClient]
    ControlObjectClient_getControlModel.restype = ControlModel

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2196
if _libs["libiec61850.so"].has("ControlObjectClient_setControlModel", "cdecl"):
    ControlObjectClient_setControlModel = _libs["libiec61850.so"].get("ControlObjectClient_setControlModel", "cdecl")
    ControlObjectClient_setControlModel.argtypes = [ControlObjectClient, ControlModel]
    ControlObjectClient_setControlModel.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2208
if _libs["libiec61850.so"].has("ControlObjectClient_changeServerControlModel", "cdecl"):
    ControlObjectClient_changeServerControlModel = _libs["libiec61850.so"].get("ControlObjectClient_changeServerControlModel", "cdecl")
    ControlObjectClient_changeServerControlModel.argtypes = [ControlObjectClient, ControlModel]
    ControlObjectClient_changeServerControlModel.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2221
if _libs["libiec61850.so"].has("ControlObjectClient_getCtlValType", "cdecl"):
    ControlObjectClient_getCtlValType = _libs["libiec61850.so"].get("ControlObjectClient_getCtlValType", "cdecl")
    ControlObjectClient_getCtlValType.argtypes = [ControlObjectClient]
    ControlObjectClient_getCtlValType.restype = MmsType

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2231
if _libs["libiec61850.so"].has("ControlObjectClient_getLastError", "cdecl"):
    ControlObjectClient_getLastError = _libs["libiec61850.so"].get("ControlObjectClient_getLastError", "cdecl")
    ControlObjectClient_getLastError.argtypes = [ControlObjectClient]
    ControlObjectClient_getLastError.restype = IedClientError

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2244
if _libs["libiec61850.so"].has("ControlObjectClient_operate", "cdecl"):
    ControlObjectClient_operate = _libs["libiec61850.so"].get("ControlObjectClient_operate", "cdecl")
    ControlObjectClient_operate.argtypes = [ControlObjectClient, POINTER(MmsValue), uint64_t]
    ControlObjectClient_operate.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2257
if _libs["libiec61850.so"].has("ControlObjectClient_select", "cdecl"):
    ControlObjectClient_select = _libs["libiec61850.so"].get("ControlObjectClient_select", "cdecl")
    ControlObjectClient_select.argtypes = [ControlObjectClient]
    ControlObjectClient_select.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2271
if _libs["libiec61850.so"].has("ControlObjectClient_selectWithValue", "cdecl"):
    ControlObjectClient_selectWithValue = _libs["libiec61850.so"].get("ControlObjectClient_selectWithValue", "cdecl")
    ControlObjectClient_selectWithValue.argtypes = [ControlObjectClient, POINTER(MmsValue)]
    ControlObjectClient_selectWithValue.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2284
if _libs["libiec61850.so"].has("ControlObjectClient_cancel", "cdecl"):
    ControlObjectClient_cancel = _libs["libiec61850.so"].get("ControlObjectClient_cancel", "cdecl")
    ControlObjectClient_cancel.argtypes = [ControlObjectClient]
    ControlObjectClient_cancel.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2301
if _libs["libiec61850.so"].has("ControlObjectClient_operateAsync", "cdecl"):
    ControlObjectClient_operateAsync = _libs["libiec61850.so"].get("ControlObjectClient_operateAsync", "cdecl")
    ControlObjectClient_operateAsync.argtypes = [ControlObjectClient, POINTER(IedClientError), POINTER(MmsValue), uint64_t, ControlObjectClient_ControlActionHandler, POINTER(None)]
    ControlObjectClient_operateAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2318
if _libs["libiec61850.so"].has("ControlObjectClient_selectAsync", "cdecl"):
    ControlObjectClient_selectAsync = _libs["libiec61850.so"].get("ControlObjectClient_selectAsync", "cdecl")
    ControlObjectClient_selectAsync.argtypes = [ControlObjectClient, POINTER(IedClientError), ControlObjectClient_ControlActionHandler, POINTER(None)]
    ControlObjectClient_selectAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2335
if _libs["libiec61850.so"].has("ControlObjectClient_selectWithValueAsync", "cdecl"):
    ControlObjectClient_selectWithValueAsync = _libs["libiec61850.so"].get("ControlObjectClient_selectWithValueAsync", "cdecl")
    ControlObjectClient_selectWithValueAsync.argtypes = [ControlObjectClient, POINTER(IedClientError), POINTER(MmsValue), ControlObjectClient_ControlActionHandler, POINTER(None)]
    ControlObjectClient_selectWithValueAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2352
if _libs["libiec61850.so"].has("ControlObjectClient_cancelAsync", "cdecl"):
    ControlObjectClient_cancelAsync = _libs["libiec61850.so"].get("ControlObjectClient_cancelAsync", "cdecl")
    ControlObjectClient_cancelAsync.argtypes = [ControlObjectClient, POINTER(IedClientError), ControlObjectClient_ControlActionHandler, POINTER(None)]
    ControlObjectClient_cancelAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2362
if _libs["libiec61850.so"].has("ControlObjectClient_getLastApplError", "cdecl"):
    ControlObjectClient_getLastApplError = _libs["libiec61850.so"].get("ControlObjectClient_getLastApplError", "cdecl")
    ControlObjectClient_getLastApplError.argtypes = [ControlObjectClient]
    ControlObjectClient_getLastApplError.restype = LastApplError

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2374
if _libs["libiec61850.so"].has("ControlObjectClient_setTestMode", "cdecl"):
    ControlObjectClient_setTestMode = _libs["libiec61850.so"].get("ControlObjectClient_setTestMode", "cdecl")
    ControlObjectClient_setTestMode.argtypes = [ControlObjectClient, c_bool]
    ControlObjectClient_setTestMode.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2387
if _libs["libiec61850.so"].has("ControlObjectClient_setOrigin", "cdecl"):
    ControlObjectClient_setOrigin = _libs["libiec61850.so"].get("ControlObjectClient_setOrigin", "cdecl")
    ControlObjectClient_setOrigin.argtypes = [ControlObjectClient, String, c_int]
    ControlObjectClient_setOrigin.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2398
if _libs["libiec61850.so"].has("ControlObjectClient_useConstantT", "cdecl"):
    ControlObjectClient_useConstantT = _libs["libiec61850.so"].get("ControlObjectClient_useConstantT", "cdecl")
    ControlObjectClient_useConstantT.argtypes = [ControlObjectClient, c_bool]
    ControlObjectClient_useConstantT.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2404
if _libs["libiec61850.so"].has("ControlObjectClient_enableInterlockCheck", "cdecl"):
    ControlObjectClient_enableInterlockCheck = _libs["libiec61850.so"].get("ControlObjectClient_enableInterlockCheck", "cdecl")
    ControlObjectClient_enableInterlockCheck.argtypes = [ControlObjectClient]
    ControlObjectClient_enableInterlockCheck.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2410
if _libs["libiec61850.so"].has("ControlObjectClient_enableSynchroCheck", "cdecl"):
    ControlObjectClient_enableSynchroCheck = _libs["libiec61850.so"].get("ControlObjectClient_enableSynchroCheck", "cdecl")
    ControlObjectClient_enableSynchroCheck.argtypes = [ControlObjectClient]
    ControlObjectClient_enableSynchroCheck.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2416
if _libs["libiec61850.so"].has("ControlObjectClient_setCtlNum", "cdecl"):
    ControlObjectClient_setCtlNum = _libs["libiec61850.so"].get("ControlObjectClient_setCtlNum", "cdecl")
    ControlObjectClient_setCtlNum.argtypes = [ControlObjectClient, uint8_t]
    ControlObjectClient_setCtlNum.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2425
if _libs["libiec61850.so"].has("ControlObjectClient_setInterlockCheck", "cdecl"):
    ControlObjectClient_setInterlockCheck = _libs["libiec61850.so"].get("ControlObjectClient_setInterlockCheck", "cdecl")
    ControlObjectClient_setInterlockCheck.argtypes = [ControlObjectClient, c_bool]
    ControlObjectClient_setInterlockCheck.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2434
if _libs["libiec61850.so"].has("ControlObjectClient_setSynchroCheck", "cdecl"):
    ControlObjectClient_setSynchroCheck = _libs["libiec61850.so"].get("ControlObjectClient_setSynchroCheck", "cdecl")
    ControlObjectClient_setSynchroCheck.argtypes = [ControlObjectClient, c_bool]
    ControlObjectClient_setSynchroCheck.restype = None

CommandTerminationHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), ControlObjectClient)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2454

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2471
if _libs["libiec61850.so"].has("ControlObjectClient_setCommandTerminationHandler", "cdecl"):
    ControlObjectClient_setCommandTerminationHandler = _libs["libiec61850.so"].get("ControlObjectClient_setCommandTerminationHandler", "cdecl")
    ControlObjectClient_setCommandTerminationHandler.argtypes = [ControlObjectClient, CommandTerminationHandler, POINTER(None)]
    ControlObjectClient_setCommandTerminationHandler.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2497
if _libs["libiec61850.so"].has("IedConnection_getDeviceModelFromServer", "cdecl"):
    IedConnection_getDeviceModelFromServer = _libs["libiec61850.so"].get("IedConnection_getDeviceModelFromServer", "cdecl")
    IedConnection_getDeviceModelFromServer.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_getDeviceModelFromServer.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2513
if _libs["libiec61850.so"].has("IedConnection_getLogicalDeviceList", "cdecl"):
    IedConnection_getLogicalDeviceList = _libs["libiec61850.so"].get("IedConnection_getLogicalDeviceList", "cdecl")
    IedConnection_getLogicalDeviceList.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_getLogicalDeviceList.restype = LinkedList

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2532
if _libs["libiec61850.so"].has("IedConnection_getServerDirectory", "cdecl"):
    IedConnection_getServerDirectory = _libs["libiec61850.so"].get("IedConnection_getServerDirectory", "cdecl")
    IedConnection_getServerDirectory.argtypes = [IedConnection, POINTER(IedClientError), c_bool]
    IedConnection_getServerDirectory.restype = LinkedList

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2550
if _libs["libiec61850.so"].has("IedConnection_getLogicalDeviceDirectory", "cdecl"):
    IedConnection_getLogicalDeviceDirectory = _libs["libiec61850.so"].get("IedConnection_getLogicalDeviceDirectory", "cdecl")
    IedConnection_getLogicalDeviceDirectory.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getLogicalDeviceDirectory.restype = LinkedList

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2568
if _libs["libiec61850.so"].has("IedConnection_getLogicalNodeVariables", "cdecl"):
    IedConnection_getLogicalNodeVariables = _libs["libiec61850.so"].get("IedConnection_getLogicalNodeVariables", "cdecl")
    IedConnection_getLogicalNodeVariables.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getLogicalNodeVariables.restype = LinkedList

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2588
if _libs["libiec61850.so"].has("IedConnection_getLogicalNodeDirectory", "cdecl"):
    IedConnection_getLogicalNodeDirectory = _libs["libiec61850.so"].get("IedConnection_getLogicalNodeDirectory", "cdecl")
    IedConnection_getLogicalNodeDirectory.argtypes = [IedConnection, POINTER(IedClientError), String, ACSIClass]
    IedConnection_getLogicalNodeDirectory.restype = LinkedList

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2607
if _libs["libiec61850.so"].has("IedConnection_getDataDirectory", "cdecl"):
    IedConnection_getDataDirectory = _libs["libiec61850.so"].get("IedConnection_getDataDirectory", "cdecl")
    IedConnection_getDataDirectory.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getDataDirectory.restype = LinkedList

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2626
if _libs["libiec61850.so"].has("IedConnection_getDataDirectoryFC", "cdecl"):
    IedConnection_getDataDirectoryFC = _libs["libiec61850.so"].get("IedConnection_getDataDirectoryFC", "cdecl")
    IedConnection_getDataDirectoryFC.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getDataDirectoryFC.restype = LinkedList

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2648
if _libs["libiec61850.so"].has("IedConnection_getDataDirectoryByFC", "cdecl"):
    IedConnection_getDataDirectoryByFC = _libs["libiec61850.so"].get("IedConnection_getDataDirectoryByFC", "cdecl")
    IedConnection_getDataDirectoryByFC.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_getDataDirectoryByFC.restype = LinkedList

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2665
if _libs["libiec61850.so"].has("IedConnection_getVariableSpecification", "cdecl"):
    IedConnection_getVariableSpecification = _libs["libiec61850.so"].get("IedConnection_getVariableSpecification", "cdecl")
    IedConnection_getVariableSpecification.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_getVariableSpecification.restype = POINTER(MmsVariableSpecification)

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2682
if _libs["libiec61850.so"].has("IedConnection_getLogicalDeviceVariables", "cdecl"):
    IedConnection_getLogicalDeviceVariables = _libs["libiec61850.so"].get("IedConnection_getLogicalDeviceVariables", "cdecl")
    IedConnection_getLogicalDeviceVariables.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getLogicalDeviceVariables.restype = LinkedList

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2697
if _libs["libiec61850.so"].has("IedConnection_getLogicalDeviceDataSets", "cdecl"):
    IedConnection_getLogicalDeviceDataSets = _libs["libiec61850.so"].get("IedConnection_getLogicalDeviceDataSets", "cdecl")
    IedConnection_getLogicalDeviceDataSets.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getLogicalDeviceDataSets.restype = LinkedList

IedConnection_GetNameListHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, LinkedList, c_bool)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2704

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2719
if _libs["libiec61850.so"].has("IedConnection_getServerDirectoryAsync", "cdecl"):
    IedConnection_getServerDirectoryAsync = _libs["libiec61850.so"].get("IedConnection_getServerDirectoryAsync", "cdecl")
    IedConnection_getServerDirectoryAsync.argtypes = [IedConnection, POINTER(IedClientError), String, LinkedList, IedConnection_GetNameListHandler, POINTER(None)]
    IedConnection_getServerDirectoryAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2739
if _libs["libiec61850.so"].has("IedConnection_getLogicalDeviceVariablesAsync", "cdecl"):
    IedConnection_getLogicalDeviceVariablesAsync = _libs["libiec61850.so"].get("IedConnection_getLogicalDeviceVariablesAsync", "cdecl")
    IedConnection_getLogicalDeviceVariablesAsync.argtypes = [IedConnection, POINTER(IedClientError), String, String, LinkedList, IedConnection_GetNameListHandler, POINTER(None)]
    IedConnection_getLogicalDeviceVariablesAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2759
if _libs["libiec61850.so"].has("IedConnection_getLogicalDeviceDataSetsAsync", "cdecl"):
    IedConnection_getLogicalDeviceDataSetsAsync = _libs["libiec61850.so"].get("IedConnection_getLogicalDeviceDataSetsAsync", "cdecl")
    IedConnection_getLogicalDeviceDataSetsAsync.argtypes = [IedConnection, POINTER(IedClientError), String, String, LinkedList, IedConnection_GetNameListHandler, POINTER(None)]
    IedConnection_getLogicalDeviceDataSetsAsync.restype = uint32_t

IedConnection_GetVariableSpecificationHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, POINTER(MmsVariableSpecification))# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2764

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2778
if _libs["libiec61850.so"].has("IedConnection_getVariableSpecificationAsync", "cdecl"):
    IedConnection_getVariableSpecificationAsync = _libs["libiec61850.so"].get("IedConnection_getVariableSpecificationAsync", "cdecl")
    IedConnection_getVariableSpecificationAsync.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, IedConnection_GetVariableSpecificationHandler, POINTER(None)]
    IedConnection_getVariableSpecificationAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2807
if _libs["libiec61850.so"].has("IedConnection_queryLogByTime", "cdecl"):
    IedConnection_queryLogByTime = _libs["libiec61850.so"].get("IedConnection_queryLogByTime", "cdecl")
    IedConnection_queryLogByTime.argtypes = [IedConnection, POINTER(IedClientError), String, uint64_t, uint64_t, POINTER(c_bool)]
    IedConnection_queryLogByTime.restype = LinkedList

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2828
if _libs["libiec61850.so"].has("IedConnection_queryLogAfter", "cdecl"):
    IedConnection_queryLogAfter = _libs["libiec61850.so"].get("IedConnection_queryLogAfter", "cdecl")
    IedConnection_queryLogAfter.argtypes = [IedConnection, POINTER(IedClientError), String, POINTER(MmsValue), uint64_t, POINTER(c_bool)]
    IedConnection_queryLogAfter.restype = LinkedList

IedConnection_QueryLogHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, LinkedList, c_bool)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2833

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2836
if _libs["libiec61850.so"].has("IedConnection_queryLogByTimeAsync", "cdecl"):
    IedConnection_queryLogByTimeAsync = _libs["libiec61850.so"].get("IedConnection_queryLogByTimeAsync", "cdecl")
    IedConnection_queryLogByTimeAsync.argtypes = [IedConnection, POINTER(IedClientError), String, uint64_t, uint64_t, IedConnection_QueryLogHandler, POINTER(None)]
    IedConnection_queryLogByTimeAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2840
if _libs["libiec61850.so"].has("IedConnection_queryLogAfterAsync", "cdecl"):
    IedConnection_queryLogAfterAsync = _libs["libiec61850.so"].get("IedConnection_queryLogAfterAsync", "cdecl")
    IedConnection_queryLogAfterAsync.argtypes = [IedConnection, POINTER(IedClientError), String, POINTER(MmsValue), uint64_t, IedConnection_QueryLogHandler, POINTER(None)]
    IedConnection_queryLogAfterAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2851
class struct_sFileDirectoryEntry(Structure):
    pass

FileDirectoryEntry = POINTER(struct_sFileDirectoryEntry)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2851

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2857
if _libs["libiec61850.so"].has("FileDirectoryEntry_create", "cdecl"):
    FileDirectoryEntry_create = _libs["libiec61850.so"].get("FileDirectoryEntry_create", "cdecl")
    FileDirectoryEntry_create.argtypes = [String, uint32_t, uint64_t]
    FileDirectoryEntry_create.restype = FileDirectoryEntry

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2867
if _libs["libiec61850.so"].has("FileDirectoryEntry_destroy", "cdecl"):
    FileDirectoryEntry_destroy = _libs["libiec61850.so"].get("FileDirectoryEntry_destroy", "cdecl")
    FileDirectoryEntry_destroy.argtypes = [FileDirectoryEntry]
    FileDirectoryEntry_destroy.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2876
if _libs["libiec61850.so"].has("FileDirectoryEntry_getFileName", "cdecl"):
    FileDirectoryEntry_getFileName = _libs["libiec61850.so"].get("FileDirectoryEntry_getFileName", "cdecl")
    FileDirectoryEntry_getFileName.argtypes = [FileDirectoryEntry]
    FileDirectoryEntry_getFileName.restype = c_char_p

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2887
if _libs["libiec61850.so"].has("FileDirectoryEntry_getFileSize", "cdecl"):
    FileDirectoryEntry_getFileSize = _libs["libiec61850.so"].get("FileDirectoryEntry_getFileSize", "cdecl")
    FileDirectoryEntry_getFileSize.argtypes = [FileDirectoryEntry]
    FileDirectoryEntry_getFileSize.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2897
if _libs["libiec61850.so"].has("FileDirectoryEntry_getLastModified", "cdecl"):
    FileDirectoryEntry_getLastModified = _libs["libiec61850.so"].get("FileDirectoryEntry_getLastModified", "cdecl")
    FileDirectoryEntry_getLastModified.argtypes = [FileDirectoryEntry]
    FileDirectoryEntry_getLastModified.restype = uint64_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2919
if _libs["libiec61850.so"].has("IedConnection_getFileDirectory", "cdecl"):
    IedConnection_getFileDirectory = _libs["libiec61850.so"].get("IedConnection_getFileDirectory", "cdecl")
    IedConnection_getFileDirectory.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getFileDirectory.restype = LinkedList

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2950
if _libs["libiec61850.so"].has("IedConnection_getFileDirectoryEx", "cdecl"):
    IedConnection_getFileDirectoryEx = _libs["libiec61850.so"].get("IedConnection_getFileDirectoryEx", "cdecl")
    IedConnection_getFileDirectoryEx.argtypes = [IedConnection, POINTER(IedClientError), String, String, POINTER(c_bool)]
    IedConnection_getFileDirectoryEx.restype = LinkedList

IedConnection_FileDirectoryEntryHandler = CFUNCTYPE(UNCHECKED(c_bool), uint32_t, POINTER(None), IedClientError, String, uint32_t, uint64_t, c_bool)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2978

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 3000
if _libs["libiec61850.so"].has("IedConnection_getFileDirectoryAsyncEx", "cdecl"):
    IedConnection_getFileDirectoryAsyncEx = _libs["libiec61850.so"].get("IedConnection_getFileDirectoryAsyncEx", "cdecl")
    IedConnection_getFileDirectoryAsyncEx.argtypes = [IedConnection, POINTER(IedClientError), String, String, IedConnection_FileDirectoryEntryHandler, POINTER(None)]
    IedConnection_getFileDirectoryAsyncEx.restype = uint32_t

IedClientGetFileHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), POINTER(uint8_t), uint32_t)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 3018

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 3032
if _libs["libiec61850.so"].has("IedConnection_getFile", "cdecl"):
    IedConnection_getFile = _libs["libiec61850.so"].get("IedConnection_getFile", "cdecl")
    IedConnection_getFile.argtypes = [IedConnection, POINTER(IedClientError), String, IedClientGetFileHandler, POINTER(None)]
    IedConnection_getFile.restype = uint32_t

IedConnection_GetFileAsyncHandler = CFUNCTYPE(UNCHECKED(c_bool), uint32_t, POINTER(None), IedClientError, uint32_t, POINTER(uint8_t), uint32_t, c_bool)# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 3055

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 3076
if _libs["libiec61850.so"].has("IedConnection_getFileAsync", "cdecl"):
    IedConnection_getFileAsync = _libs["libiec61850.so"].get("IedConnection_getFileAsync", "cdecl")
    IedConnection_getFileAsync.argtypes = [IedConnection, POINTER(IedClientError), String, IedConnection_GetFileAsyncHandler, POINTER(None)]
    IedConnection_getFileAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 3090
if _libs["libiec61850.so"].has("IedConnection_setFilestoreBasepath", "cdecl"):
    IedConnection_setFilestoreBasepath = _libs["libiec61850.so"].get("IedConnection_setFilestoreBasepath", "cdecl")
    IedConnection_setFilestoreBasepath.argtypes = [IedConnection, String]
    IedConnection_setFilestoreBasepath.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 3103
if _libs["libiec61850.so"].has("IedConnection_setFile", "cdecl"):
    IedConnection_setFile = _libs["libiec61850.so"].get("IedConnection_setFile", "cdecl")
    IedConnection_setFile.argtypes = [IedConnection, POINTER(IedClientError), String, String]
    IedConnection_setFile.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 3118
if _libs["libiec61850.so"].has("IedConnection_setFileAsync", "cdecl"):
    IedConnection_setFileAsync = _libs["libiec61850.so"].get("IedConnection_setFileAsync", "cdecl")
    IedConnection_setFileAsync.argtypes = [IedConnection, POINTER(IedClientError), String, String, IedConnection_GenericServiceHandler, POINTER(None)]
    IedConnection_setFileAsync.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 3131
if _libs["libiec61850.so"].has("IedConnection_deleteFile", "cdecl"):
    IedConnection_deleteFile = _libs["libiec61850.so"].get("IedConnection_deleteFile", "cdecl")
    IedConnection_deleteFile.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_deleteFile.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 3145
if _libs["libiec61850.so"].has("IedConnection_deleteFileAsync", "cdecl"):
    IedConnection_deleteFileAsync = _libs["libiec61850.so"].get("IedConnection_deleteFileAsync", "cdecl")
    IedConnection_deleteFileAsync.argtypes = [IedConnection, POINTER(IedClientError), String, IedConnection_GenericServiceHandler, POINTER(None)]
    IedConnection_deleteFileAsync.restype = uint32_t

FileHandle = POINTER(None)# ../libiec61850/hal/inc/hal_filesystem.h: 30

# ../libiec61850/hal/inc/hal_filesystem.h: 31
class struct_sDirectoryHandle(Structure):
    pass

DirectoryHandle = POINTER(struct_sDirectoryHandle)# ../libiec61850/hal/inc/hal_filesystem.h: 31

# ../libiec61850/hal/inc/hal_filesystem.h: 47
if _libs["libiec61850.so"].has("FileSystem_openFile", "cdecl"):
    FileSystem_openFile = _libs["libiec61850.so"].get("FileSystem_openFile", "cdecl")
    FileSystem_openFile.argtypes = [String, c_bool]
    FileSystem_openFile.restype = FileHandle

# ../libiec61850/hal/inc/hal_filesystem.h: 64
if _libs["libiec61850.so"].has("FileSystem_readFile", "cdecl"):
    FileSystem_readFile = _libs["libiec61850.so"].get("FileSystem_readFile", "cdecl")
    FileSystem_readFile.argtypes = [FileHandle, POINTER(uint8_t), c_int]
    FileSystem_readFile.restype = c_int

# ../libiec61850/hal/inc/hal_filesystem.h: 76
if _libs["libiec61850.so"].has("FileSystem_writeFile", "cdecl"):
    FileSystem_writeFile = _libs["libiec61850.so"].get("FileSystem_writeFile", "cdecl")
    FileSystem_writeFile.argtypes = [FileHandle, POINTER(uint8_t), c_int]
    FileSystem_writeFile.restype = c_int

# ../libiec61850/hal/inc/hal_filesystem.h: 84
if _libs["libiec61850.so"].has("FileSystem_closeFile", "cdecl"):
    FileSystem_closeFile = _libs["libiec61850.so"].get("FileSystem_closeFile", "cdecl")
    FileSystem_closeFile.argtypes = [FileHandle]
    FileSystem_closeFile.restype = None

# ../libiec61850/hal/inc/hal_filesystem.h: 100
if _libs["libiec61850.so"].has("FileSystem_getFileInfo", "cdecl"):
    FileSystem_getFileInfo = _libs["libiec61850.so"].get("FileSystem_getFileInfo", "cdecl")
    FileSystem_getFileInfo.argtypes = [String, POINTER(uint32_t), POINTER(uint64_t)]
    FileSystem_getFileInfo.restype = c_bool

# ../libiec61850/hal/inc/hal_filesystem.h: 110
if _libs["libiec61850.so"].has("FileSystem_deleteFile", "cdecl"):
    FileSystem_deleteFile = _libs["libiec61850.so"].get("FileSystem_deleteFile", "cdecl")
    FileSystem_deleteFile.argtypes = [String]
    FileSystem_deleteFile.restype = c_bool

# ../libiec61850/hal/inc/hal_filesystem.h: 121
if _libs["libiec61850.so"].has("FileSystem_renameFile", "cdecl"):
    FileSystem_renameFile = _libs["libiec61850.so"].get("FileSystem_renameFile", "cdecl")
    FileSystem_renameFile.argtypes = [String, String]
    FileSystem_renameFile.restype = c_bool

# ../libiec61850/hal/inc/hal_filesystem.h: 131
if _libs["libiec61850.so"].has("FileSystem_openDirectory", "cdecl"):
    FileSystem_openDirectory = _libs["libiec61850.so"].get("FileSystem_openDirectory", "cdecl")
    FileSystem_openDirectory.argtypes = [String]
    FileSystem_openDirectory.restype = DirectoryHandle

# ../libiec61850/hal/inc/hal_filesystem.h: 145
if _libs["libiec61850.so"].has("FileSystem_readDirectory", "cdecl"):
    FileSystem_readDirectory = _libs["libiec61850.so"].get("FileSystem_readDirectory", "cdecl")
    FileSystem_readDirectory.argtypes = [DirectoryHandle, POINTER(c_bool)]
    if sizeof(c_int) == sizeof(c_void_p):
        FileSystem_readDirectory.restype = ReturnString
    else:
        FileSystem_readDirectory.restype = String
        FileSystem_readDirectory.errcheck = ReturnString

# ../libiec61850/hal/inc/hal_filesystem.h: 155
if _libs["libiec61850.so"].has("FileSystem_closeDirectory", "cdecl"):
    FileSystem_closeDirectory = _libs["libiec61850.so"].get("FileSystem_closeDirectory", "cdecl")
    FileSystem_closeDirectory.argtypes = [DirectoryHandle]
    FileSystem_closeDirectory.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 157
class struct_sModelNode(Structure):
    pass

ModelNode = struct_sModelNode# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 48

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 184
class struct_sDataAttribute(Structure):
    pass

DataAttribute = struct_sDataAttribute# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 53

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 173
class struct_sDataObject(Structure):
    pass

DataObject = struct_sDataObject# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 58

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 165
class struct_sLogicalNode(Structure):
    pass

LogicalNode = struct_sLogicalNode# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 63

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 148
class struct_sLogicalDevice(Structure):
    pass

LogicalDevice = struct_sLogicalDevice# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 68

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 135
class struct_sIedModel(Structure):
    pass

IedModel = struct_sIedModel# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 73

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 214
class struct_sDataSet(Structure):
    pass

DataSet = struct_sDataSet# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 75

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 222
class struct_sReportControlBlock(Structure):
    pass

ReportControlBlock = struct_sReportControlBlock# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 76

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 269
class struct_sSettingGroupControlBlock(Structure):
    pass

SettingGroupControlBlock = struct_sSettingGroupControlBlock# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 81

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 283
class struct_sGSEControlBlock(Structure):
    pass

GSEControlBlock = struct_sGSEControlBlock# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 83

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 296
class struct_sSVControlBlock(Structure):
    pass

SVControlBlock = struct_sSVControlBlock# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 85

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 244
class struct_sLogControlBlock(Structure):
    pass

LogControlBlock = struct_sLogControlBlock# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 87

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 261
class struct_sLog(Structure):
    pass

Log = struct_sLog# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 89

enum_anon_47 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_UNKNOWN_TYPE = (-1)# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_BOOLEAN = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_INT8 = 1# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_INT16 = 2# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_INT32 = 3# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_INT64 = 4# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_INT128 = 5# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_INT8U = 6# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_INT16U = 7# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_INT24U = 8# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_INT32U = 9# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_FLOAT32 = 10# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_FLOAT64 = 11# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_ENUMERATED = 12# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_OCTET_STRING_64 = 13# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_OCTET_STRING_6 = 14# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_OCTET_STRING_8 = 15# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_VISIBLE_STRING_32 = 16# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_VISIBLE_STRING_64 = 17# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_VISIBLE_STRING_65 = 18# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_VISIBLE_STRING_129 = 19# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_VISIBLE_STRING_255 = 20# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_UNICODE_STRING_255 = 21# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_TIMESTAMP = 22# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_QUALITY = 23# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_CHECK = 24# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_CODEDENUM = 25# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_GENERIC_BITSTRING = 26# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_CONSTRUCTED = 27# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_ENTRY_TIME = 28# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_PHYCOMADDR = 29# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_CURRENCY = 30# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_OPTFLDS = 31# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

IEC61850_TRGOPS = 32# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

DataAttributeType = enum_anon_47# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 126

enum_anon_48 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 133

LogicalDeviceModelType = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 133

LogicalNodeModelType = (LogicalDeviceModelType + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 133

DataObjectModelType = (LogicalNodeModelType + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 133

DataAttributeModelType = (DataObjectModelType + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 133

ModelNodeType = enum_anon_48# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 133

struct_sIedModel.__slots__ = [
    'name',
    'firstChild',
    'dataSets',
    'rcbs',
    'gseCBs',
    'svCBs',
    'sgcbs',
    'lcbs',
    'logs',
    'initializer',
]
struct_sIedModel._fields_ = [
    ('name', String),
    ('firstChild', POINTER(LogicalDevice)),
    ('dataSets', POINTER(DataSet)),
    ('rcbs', POINTER(ReportControlBlock)),
    ('gseCBs', POINTER(GSEControlBlock)),
    ('svCBs', POINTER(SVControlBlock)),
    ('sgcbs', POINTER(SettingGroupControlBlock)),
    ('lcbs', POINTER(LogControlBlock)),
    ('logs', POINTER(Log)),
    ('initializer', CFUNCTYPE(UNCHECKED(None), )),
]

struct_sLogicalDevice.__slots__ = [
    'modelType',
    'name',
    'parent',
    'sibling',
    'firstChild',
    'ldName',
]
struct_sLogicalDevice._fields_ = [
    ('modelType', ModelNodeType),
    ('name', String),
    ('parent', POINTER(ModelNode)),
    ('sibling', POINTER(ModelNode)),
    ('firstChild', POINTER(ModelNode)),
    ('ldName', String),
]

struct_sModelNode.__slots__ = [
    'modelType',
    'name',
    'parent',
    'sibling',
    'firstChild',
]
struct_sModelNode._fields_ = [
    ('modelType', ModelNodeType),
    ('name', String),
    ('parent', POINTER(ModelNode)),
    ('sibling', POINTER(ModelNode)),
    ('firstChild', POINTER(ModelNode)),
]

struct_sLogicalNode.__slots__ = [
    'modelType',
    'name',
    'parent',
    'sibling',
    'firstChild',
]
struct_sLogicalNode._fields_ = [
    ('modelType', ModelNodeType),
    ('name', String),
    ('parent', POINTER(ModelNode)),
    ('sibling', POINTER(ModelNode)),
    ('firstChild', POINTER(ModelNode)),
]

struct_sDataObject.__slots__ = [
    'modelType',
    'name',
    'parent',
    'sibling',
    'firstChild',
    'elementCount',
    'arrayIndex',
]
struct_sDataObject._fields_ = [
    ('modelType', ModelNodeType),
    ('name', String),
    ('parent', POINTER(ModelNode)),
    ('sibling', POINTER(ModelNode)),
    ('firstChild', POINTER(ModelNode)),
    ('elementCount', c_int),
    ('arrayIndex', c_int),
]

struct_sDataAttribute.__slots__ = [
    'modelType',
    'name',
    'parent',
    'sibling',
    'firstChild',
    'elementCount',
    'arrayIndex',
    'fc',
    'type',
    'triggerOptions',
    'mmsValue',
    'sAddr',
]
struct_sDataAttribute._fields_ = [
    ('modelType', ModelNodeType),
    ('name', String),
    ('parent', POINTER(ModelNode)),
    ('sibling', POINTER(ModelNode)),
    ('firstChild', POINTER(ModelNode)),
    ('elementCount', c_int),
    ('arrayIndex', c_int),
    ('fc', FunctionalConstraint),
    ('type', DataAttributeType),
    ('triggerOptions', uint8_t),
    ('mmsValue', POINTER(MmsValue)),
    ('sAddr', uint32_t),
]

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 204
class struct_sDataSetEntry(Structure):
    pass

struct_sDataSetEntry.__slots__ = [
    'logicalDeviceName',
    'isLDNameDynamicallyAllocated',
    'variableName',
    'index',
    'componentName',
    'value',
    'sibling',
]
struct_sDataSetEntry._fields_ = [
    ('logicalDeviceName', String),
    ('isLDNameDynamicallyAllocated', c_bool),
    ('variableName', String),
    ('index', c_int),
    ('componentName', String),
    ('value', POINTER(MmsValue)),
    ('sibling', POINTER(struct_sDataSetEntry)),
]

DataSetEntry = struct_sDataSetEntry# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 212

struct_sDataSet.__slots__ = [
    'logicalDeviceName',
    'name',
    'elementCount',
    'fcdas',
    'sibling',
]
struct_sDataSet._fields_ = [
    ('logicalDeviceName', String),
    ('name', String),
    ('elementCount', c_int),
    ('fcdas', POINTER(DataSetEntry)),
    ('sibling', POINTER(DataSet)),
]

struct_sReportControlBlock.__slots__ = [
    'parent',
    'name',
    'rptId',
    'buffered',
    'dataSetName',
    'confRef',
    'trgOps',
    'options',
    'bufferTime',
    'intPeriod',
    'clientReservation',
    'sibling',
]
struct_sReportControlBlock._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('name', String),
    ('rptId', String),
    ('buffered', c_bool),
    ('dataSetName', String),
    ('confRef', uint32_t),
    ('trgOps', uint8_t),
    ('options', uint8_t),
    ('bufferTime', uint32_t),
    ('intPeriod', uint32_t),
    ('clientReservation', uint8_t * int(17)),
    ('sibling', POINTER(ReportControlBlock)),
]

struct_sLogControlBlock.__slots__ = [
    'parent',
    'name',
    'dataSetName',
    'logRef',
    'trgOps',
    'intPeriod',
    'logEna',
    'reasonCode',
    'sibling',
]
struct_sLogControlBlock._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('name', String),
    ('dataSetName', String),
    ('logRef', String),
    ('trgOps', uint8_t),
    ('intPeriod', uint32_t),
    ('logEna', c_bool),
    ('reasonCode', c_bool),
    ('sibling', POINTER(LogControlBlock)),
]

struct_sLog.__slots__ = [
    'parent',
    'name',
    'sibling',
]
struct_sLog._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('name', String),
    ('sibling', POINTER(Log)),
]

struct_sSettingGroupControlBlock.__slots__ = [
    'parent',
    'actSG',
    'numOfSGs',
    'editSG',
    'cnfEdit',
    'timestamp',
    'resvTms',
    'sibling',
]
struct_sSettingGroupControlBlock._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('actSG', uint8_t),
    ('numOfSGs', uint8_t),
    ('editSG', uint8_t),
    ('cnfEdit', c_bool),
    ('timestamp', uint64_t),
    ('resvTms', uint16_t),
    ('sibling', POINTER(SettingGroupControlBlock)),
]

struct_sGSEControlBlock.__slots__ = [
    'parent',
    'name',
    'appId',
    'dataSetName',
    'confRev',
    'fixedOffs',
    'address',
    'minTime',
    'maxTime',
    'sibling',
]
struct_sGSEControlBlock._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('name', String),
    ('appId', String),
    ('dataSetName', String),
    ('confRev', uint32_t),
    ('fixedOffs', c_bool),
    ('address', POINTER(PhyComAddress)),
    ('minTime', c_int),
    ('maxTime', c_int),
    ('sibling', POINTER(GSEControlBlock)),
]

struct_sSVControlBlock.__slots__ = [
    'parent',
    'name',
    'svId',
    'dataSetName',
    'optFlds',
    'smpMod',
    'smpRate',
    'confRev',
    'dstAddress',
    'isUnicast',
    'noASDU',
    'sibling',
]
struct_sSVControlBlock._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('name', String),
    ('svId', String),
    ('dataSetName', String),
    ('optFlds', uint8_t),
    ('smpMod', uint8_t),
    ('smpRate', uint16_t),
    ('confRev', uint32_t),
    ('dstAddress', POINTER(PhyComAddress)),
    ('isUnicast', c_bool),
    ('noASDU', c_int),
    ('sibling', POINTER(SVControlBlock)),
]

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 328
if _libs["libiec61850.so"].has("ModelNode_getChildCount", "cdecl"):
    ModelNode_getChildCount = _libs["libiec61850.so"].get("ModelNode_getChildCount", "cdecl")
    ModelNode_getChildCount.argtypes = [POINTER(ModelNode)]
    ModelNode_getChildCount.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 338
if _libs["libiec61850.so"].has("ModelNode_getChild", "cdecl"):
    ModelNode_getChild = _libs["libiec61850.so"].get("ModelNode_getChild", "cdecl")
    ModelNode_getChild.argtypes = [POINTER(ModelNode), String]
    ModelNode_getChild.restype = POINTER(ModelNode)

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 349
if _libs["libiec61850.so"].has("ModelNode_getChildWithIdx", "cdecl"):
    ModelNode_getChildWithIdx = _libs["libiec61850.so"].get("ModelNode_getChildWithIdx", "cdecl")
    ModelNode_getChildWithIdx.argtypes = [POINTER(ModelNode), c_int]
    ModelNode_getChildWithIdx.restype = POINTER(ModelNode)

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 365
if _libs["libiec61850.so"].has("ModelNode_getChildWithFc", "cdecl"):
    ModelNode_getChildWithFc = _libs["libiec61850.so"].get("ModelNode_getChildWithFc", "cdecl")
    ModelNode_getChildWithFc.argtypes = [POINTER(ModelNode), String, FunctionalConstraint]
    ModelNode_getChildWithFc.restype = POINTER(ModelNode)

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 377
if _libs["libiec61850.so"].has("ModelNode_getObjectReference", "cdecl"):
    ModelNode_getObjectReference = _libs["libiec61850.so"].get("ModelNode_getObjectReference", "cdecl")
    ModelNode_getObjectReference.argtypes = [POINTER(ModelNode), String]
    if sizeof(c_int) == sizeof(c_void_p):
        ModelNode_getObjectReference.restype = ReturnString
    else:
        ModelNode_getObjectReference.restype = String
        ModelNode_getObjectReference.errcheck = ReturnString

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 390
if _libs["libiec61850.so"].has("ModelNode_getObjectReferenceEx", "cdecl"):
    ModelNode_getObjectReferenceEx = _libs["libiec61850.so"].get("ModelNode_getObjectReferenceEx", "cdecl")
    ModelNode_getObjectReferenceEx.argtypes = [POINTER(ModelNode), String, c_bool]
    if sizeof(c_int) == sizeof(c_void_p):
        ModelNode_getObjectReferenceEx.restype = ReturnString
    else:
        ModelNode_getObjectReferenceEx.restype = String
        ModelNode_getObjectReferenceEx.errcheck = ReturnString

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 401
if _libs["libiec61850.so"].has("ModelNode_getType", "cdecl"):
    ModelNode_getType = _libs["libiec61850.so"].get("ModelNode_getType", "cdecl")
    ModelNode_getType.argtypes = [POINTER(ModelNode)]
    ModelNode_getType.restype = ModelNodeType

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 410
if _libs["libiec61850.so"].has("ModelNode_getName", "cdecl"):
    ModelNode_getName = _libs["libiec61850.so"].get("ModelNode_getName", "cdecl")
    ModelNode_getName.argtypes = [POINTER(ModelNode)]
    ModelNode_getName.restype = c_char_p

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 420
if _libs["libiec61850.so"].has("ModelNode_getParent", "cdecl"):
    ModelNode_getParent = _libs["libiec61850.so"].get("ModelNode_getParent", "cdecl")
    ModelNode_getParent.argtypes = [POINTER(ModelNode)]
    ModelNode_getParent.restype = POINTER(ModelNode)

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 431
if _libs["libiec61850.so"].has("ModelNode_getChildren", "cdecl"):
    ModelNode_getChildren = _libs["libiec61850.so"].get("ModelNode_getChildren", "cdecl")
    ModelNode_getChildren.argtypes = [POINTER(ModelNode)]
    ModelNode_getChildren.restype = LinkedList

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 443
if _libs["libiec61850.so"].has("IedModel_setIedName", "cdecl"):
    IedModel_setIedName = _libs["libiec61850.so"].get("IedModel_setIedName", "cdecl")
    IedModel_setIedName.argtypes = [POINTER(IedModel), String]
    IedModel_setIedName.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 459
if _libs["libiec61850.so"].has("IedModel_getModelNodeByObjectReference", "cdecl"):
    IedModel_getModelNodeByObjectReference = _libs["libiec61850.so"].get("IedModel_getModelNodeByObjectReference", "cdecl")
    IedModel_getModelNodeByObjectReference.argtypes = [POINTER(IedModel), String]
    IedModel_getModelNodeByObjectReference.restype = POINTER(ModelNode)

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 462
if _libs["libiec61850.so"].has("IedModel_getSVControlBlock", "cdecl"):
    IedModel_getSVControlBlock = _libs["libiec61850.so"].get("IedModel_getSVControlBlock", "cdecl")
    IedModel_getSVControlBlock.argtypes = [POINTER(IedModel), POINTER(LogicalNode), String]
    IedModel_getSVControlBlock.restype = POINTER(SVControlBlock)

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 479
if _libs["libiec61850.so"].has("IedModel_getModelNodeByShortObjectReference", "cdecl"):
    IedModel_getModelNodeByShortObjectReference = _libs["libiec61850.so"].get("IedModel_getModelNodeByShortObjectReference", "cdecl")
    IedModel_getModelNodeByShortObjectReference.argtypes = [POINTER(IedModel), String]
    IedModel_getModelNodeByShortObjectReference.restype = POINTER(ModelNode)

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 493
if _libs["libiec61850.so"].has("IedModel_getModelNodeByShortAddress", "cdecl"):
    IedModel_getModelNodeByShortAddress = _libs["libiec61850.so"].get("IedModel_getModelNodeByShortAddress", "cdecl")
    IedModel_getModelNodeByShortAddress.argtypes = [POINTER(IedModel), uint32_t]
    IedModel_getModelNodeByShortAddress.restype = POINTER(ModelNode)

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 504
if _libs["libiec61850.so"].has("IedModel_getDeviceByInst", "cdecl"):
    IedModel_getDeviceByInst = _libs["libiec61850.so"].get("IedModel_getDeviceByInst", "cdecl")
    IedModel_getDeviceByInst.argtypes = [POINTER(IedModel), String]
    IedModel_getDeviceByInst.restype = POINTER(LogicalDevice)

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 515
if _libs["libiec61850.so"].has("IedModel_getDeviceByIndex", "cdecl"):
    IedModel_getDeviceByIndex = _libs["libiec61850.so"].get("IedModel_getDeviceByIndex", "cdecl")
    IedModel_getDeviceByIndex.argtypes = [POINTER(IedModel), c_int]
    IedModel_getDeviceByIndex.restype = POINTER(LogicalDevice)

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 527
if _libs["libiec61850.so"].has("LogicalDevice_getLogicalNode", "cdecl"):
    LogicalDevice_getLogicalNode = _libs["libiec61850.so"].get("LogicalDevice_getLogicalNode", "cdecl")
    LogicalDevice_getLogicalNode.argtypes = [POINTER(LogicalDevice), String]
    LogicalDevice_getLogicalNode.restype = POINTER(LogicalNode)

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 537
if _libs["libiec61850.so"].has("LogicalDevice_getSettingGroupControlBlock", "cdecl"):
    LogicalDevice_getSettingGroupControlBlock = _libs["libiec61850.so"].get("LogicalDevice_getSettingGroupControlBlock", "cdecl")
    LogicalDevice_getSettingGroupControlBlock.argtypes = [POINTER(LogicalDevice)]
    LogicalDevice_getSettingGroupControlBlock.restype = POINTER(SettingGroupControlBlock)

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 551
if _libs["libiec61850.so"].has("IedModel_setAttributeValuesToNull", "cdecl"):
    IedModel_setAttributeValuesToNull = _libs["libiec61850.so"].get("IedModel_setAttributeValuesToNull", "cdecl")
    IedModel_setAttributeValuesToNull.argtypes = [POINTER(IedModel)]
    IedModel_setAttributeValuesToNull.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 561
if _libs["libiec61850.so"].has("IedModel_getDevice", "cdecl"):
    IedModel_getDevice = _libs["libiec61850.so"].get("IedModel_getDevice", "cdecl")
    IedModel_getDevice.argtypes = [POINTER(IedModel), String]
    IedModel_getDevice.restype = POINTER(LogicalDevice)

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 572
if _libs["libiec61850.so"].has("IedModel_lookupDataSet", "cdecl"):
    IedModel_lookupDataSet = _libs["libiec61850.so"].get("IedModel_lookupDataSet", "cdecl")
    IedModel_lookupDataSet.argtypes = [POINTER(IedModel), String]
    IedModel_lookupDataSet.restype = POINTER(DataSet)

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 583
if _libs["libiec61850.so"].has("IedModel_lookupDataAttributeByMmsValue", "cdecl"):
    IedModel_lookupDataAttributeByMmsValue = _libs["libiec61850.so"].get("IedModel_lookupDataAttributeByMmsValue", "cdecl")
    IedModel_lookupDataAttributeByMmsValue.argtypes = [POINTER(IedModel), POINTER(MmsValue)]
    IedModel_lookupDataAttributeByMmsValue.restype = POINTER(DataAttribute)

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 595
if _libs["libiec61850.so"].has("IedModel_getLogicalDeviceCount", "cdecl"):
    IedModel_getLogicalDeviceCount = _libs["libiec61850.so"].get("IedModel_getLogicalDeviceCount", "cdecl")
    IedModel_getLogicalDeviceCount.argtypes = [POINTER(IedModel)]
    IedModel_getLogicalDeviceCount.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 598
if _libs["libiec61850.so"].has("LogicalDevice_getLogicalNodeCount", "cdecl"):
    LogicalDevice_getLogicalNodeCount = _libs["libiec61850.so"].get("LogicalDevice_getLogicalNodeCount", "cdecl")
    LogicalDevice_getLogicalNodeCount.argtypes = [POINTER(LogicalDevice)]
    LogicalDevice_getLogicalNodeCount.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 600
if _libs["libiec61850.so"].has("LogicalDevice_getChildByMmsVariableName", "cdecl"):
    LogicalDevice_getChildByMmsVariableName = _libs["libiec61850.so"].get("LogicalDevice_getChildByMmsVariableName", "cdecl")
    LogicalDevice_getChildByMmsVariableName.argtypes = [POINTER(LogicalDevice), String]
    LogicalDevice_getChildByMmsVariableName.restype = POINTER(ModelNode)

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 604
if _libs["libiec61850.so"].has("LogicalNode_hasFCData", "cdecl"):
    LogicalNode_hasFCData = _libs["libiec61850.so"].get("LogicalNode_hasFCData", "cdecl")
    LogicalNode_hasFCData.argtypes = [POINTER(LogicalNode), FunctionalConstraint]
    LogicalNode_hasFCData.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 607
for _lib in _libs.values():
    if not _lib.has("LogicalNode_hasBufferedReports", "cdecl"):
        continue
    LogicalNode_hasBufferedReports = _lib.get("LogicalNode_hasBufferedReports", "cdecl")
    LogicalNode_hasBufferedReports.argtypes = [POINTER(LogicalNode)]
    LogicalNode_hasBufferedReports.restype = c_bool
    break

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 610
for _lib in _libs.values():
    if not _lib.has("LogicalNode_hasUnbufferedReports", "cdecl"):
        continue
    LogicalNode_hasUnbufferedReports = _lib.get("LogicalNode_hasUnbufferedReports", "cdecl")
    LogicalNode_hasUnbufferedReports.argtypes = [POINTER(LogicalNode)]
    LogicalNode_hasUnbufferedReports.restype = c_bool
    break

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 620
if _libs["libiec61850.so"].has("LogicalNode_getDataSet", "cdecl"):
    LogicalNode_getDataSet = _libs["libiec61850.so"].get("LogicalNode_getDataSet", "cdecl")
    LogicalNode_getDataSet.argtypes = [POINTER(LogicalNode), String]
    LogicalNode_getDataSet.restype = POINTER(DataSet)

# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 624
if _libs["libiec61850.so"].has("DataObject_hasFCData", "cdecl"):
    DataObject_hasFCData = _libs["libiec61850.so"].get("DataObject_hasFCData", "cdecl")
    DataObject_hasFCData.argtypes = [POINTER(DataObject), FunctionalConstraint]
    DataObject_hasFCData.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 57
if _libs["libiec61850.so"].has("IedModel_create", "cdecl"):
    IedModel_create = _libs["libiec61850.so"].get("IedModel_create", "cdecl")
    IedModel_create.argtypes = [String]
    IedModel_create.restype = POINTER(IedModel)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 72
if _libs["libiec61850.so"].has("IedModel_setIedNameForDynamicModel", "cdecl"):
    IedModel_setIedNameForDynamicModel = _libs["libiec61850.so"].get("IedModel_setIedNameForDynamicModel", "cdecl")
    IedModel_setIedNameForDynamicModel.argtypes = [POINTER(IedModel), String]
    IedModel_setIedNameForDynamicModel.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 84
if _libs["libiec61850.so"].has("IedModel_destroy", "cdecl"):
    IedModel_destroy = _libs["libiec61850.so"].get("IedModel_destroy", "cdecl")
    IedModel_destroy.argtypes = [POINTER(IedModel)]
    IedModel_destroy.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 94
if _libs["libiec61850.so"].has("LogicalDevice_create", "cdecl"):
    LogicalDevice_create = _libs["libiec61850.so"].get("LogicalDevice_create", "cdecl")
    LogicalDevice_create.argtypes = [String, POINTER(IedModel)]
    LogicalDevice_create.restype = POINTER(LogicalDevice)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 106
if _libs["libiec61850.so"].has("LogicalDevice_createEx", "cdecl"):
    LogicalDevice_createEx = _libs["libiec61850.so"].get("LogicalDevice_createEx", "cdecl")
    LogicalDevice_createEx.argtypes = [String, POINTER(IedModel), String]
    LogicalDevice_createEx.restype = POINTER(LogicalDevice)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 117
if _libs["libiec61850.so"].has("LogicalNode_create", "cdecl"):
    LogicalNode_create = _libs["libiec61850.so"].get("LogicalNode_create", "cdecl")
    LogicalNode_create.argtypes = [String, POINTER(LogicalDevice)]
    LogicalNode_create.restype = POINTER(LogicalNode)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 134
if _libs["libiec61850.so"].has("DataObject_create", "cdecl"):
    DataObject_create = _libs["libiec61850.so"].get("DataObject_create", "cdecl")
    DataObject_create.argtypes = [String, POINTER(ModelNode), c_int]
    DataObject_create.restype = POINTER(DataObject)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 152
if _libs["libiec61850.so"].has("DataAttribute_create", "cdecl"):
    DataAttribute_create = _libs["libiec61850.so"].get("DataAttribute_create", "cdecl")
    DataAttribute_create.argtypes = [String, POINTER(ModelNode), DataAttributeType, FunctionalConstraint, uint8_t, c_int, uint32_t]
    DataAttribute_create.restype = POINTER(DataAttribute)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 164
if _libs["libiec61850.so"].has("DataAttribute_getType", "cdecl"):
    DataAttribute_getType = _libs["libiec61850.so"].get("DataAttribute_getType", "cdecl")
    DataAttribute_getType.argtypes = [POINTER(DataAttribute)]
    DataAttribute_getType.restype = DataAttributeType

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 174
if _libs["libiec61850.so"].has("DataAttribute_getFC", "cdecl"):
    DataAttribute_getFC = _libs["libiec61850.so"].get("DataAttribute_getFC", "cdecl")
    DataAttribute_getFC.argtypes = [POINTER(DataAttribute)]
    DataAttribute_getFC.restype = FunctionalConstraint

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 184
if _libs["libiec61850.so"].has("DataAttribute_getTrgOps", "cdecl"):
    DataAttribute_getTrgOps = _libs["libiec61850.so"].get("DataAttribute_getTrgOps", "cdecl")
    DataAttribute_getTrgOps.argtypes = [POINTER(DataAttribute)]
    DataAttribute_getTrgOps.restype = uint8_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 193
if _libs["libiec61850.so"].has("DataAttribute_setValue", "cdecl"):
    DataAttribute_setValue = _libs["libiec61850.so"].get("DataAttribute_setValue", "cdecl")
    DataAttribute_setValue.argtypes = [POINTER(DataAttribute), POINTER(MmsValue)]
    DataAttribute_setValue.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 214
if _libs["libiec61850.so"].has("ReportControlBlock_create", "cdecl"):
    ReportControlBlock_create = _libs["libiec61850.so"].get("ReportControlBlock_create", "cdecl")
    ReportControlBlock_create.argtypes = [String, POINTER(LogicalNode), String, c_bool, String, uint32_t, uint8_t, uint8_t, uint32_t, uint32_t]
    ReportControlBlock_create.restype = POINTER(ReportControlBlock)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 228
if _libs["libiec61850.so"].has("ReportControlBlock_setPreconfiguredClient", "cdecl"):
    ReportControlBlock_setPreconfiguredClient = _libs["libiec61850.so"].get("ReportControlBlock_setPreconfiguredClient", "cdecl")
    ReportControlBlock_setPreconfiguredClient.argtypes = [POINTER(ReportControlBlock), uint8_t, POINTER(uint8_t)]
    ReportControlBlock_setPreconfiguredClient.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 239
if _libs["libiec61850.so"].has("ReportControlBlock_getName", "cdecl"):
    ReportControlBlock_getName = _libs["libiec61850.so"].get("ReportControlBlock_getName", "cdecl")
    ReportControlBlock_getName.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getName.restype = c_char_p

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 250
if _libs["libiec61850.so"].has("ReportControlBlock_isBuffered", "cdecl"):
    ReportControlBlock_isBuffered = _libs["libiec61850.so"].get("ReportControlBlock_isBuffered", "cdecl")
    ReportControlBlock_isBuffered.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_isBuffered.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 259
if _libs["libiec61850.so"].has("ReportControlBlock_getParent", "cdecl"):
    ReportControlBlock_getParent = _libs["libiec61850.so"].get("ReportControlBlock_getParent", "cdecl")
    ReportControlBlock_getParent.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getParent.restype = POINTER(LogicalNode)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 269
if _libs["libiec61850.so"].has("ReportControlBlock_getRptID", "cdecl"):
    ReportControlBlock_getRptID = _libs["libiec61850.so"].get("ReportControlBlock_getRptID", "cdecl")
    ReportControlBlock_getRptID.argtypes = [POINTER(ReportControlBlock)]
    if sizeof(c_int) == sizeof(c_void_p):
        ReportControlBlock_getRptID.restype = ReturnString
    else:
        ReportControlBlock_getRptID.restype = String
        ReportControlBlock_getRptID.errcheck = ReturnString

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 280
if _libs["libiec61850.so"].has("ReportControlBlock_getRptEna", "cdecl"):
    ReportControlBlock_getRptEna = _libs["libiec61850.so"].get("ReportControlBlock_getRptEna", "cdecl")
    ReportControlBlock_getRptEna.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getRptEna.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 289
if _libs["libiec61850.so"].has("ReportControlBlock_getDataSet", "cdecl"):
    ReportControlBlock_getDataSet = _libs["libiec61850.so"].get("ReportControlBlock_getDataSet", "cdecl")
    ReportControlBlock_getDataSet.argtypes = [POINTER(ReportControlBlock)]
    if sizeof(c_int) == sizeof(c_void_p):
        ReportControlBlock_getDataSet.restype = ReturnString
    else:
        ReportControlBlock_getDataSet.restype = String
        ReportControlBlock_getDataSet.errcheck = ReturnString

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 300
if _libs["libiec61850.so"].has("ReportControlBlock_getConfRev", "cdecl"):
    ReportControlBlock_getConfRev = _libs["libiec61850.so"].get("ReportControlBlock_getConfRev", "cdecl")
    ReportControlBlock_getConfRev.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getConfRev.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 320
if _libs["libiec61850.so"].has("ReportControlBlock_getOptFlds", "cdecl"):
    ReportControlBlock_getOptFlds = _libs["libiec61850.so"].get("ReportControlBlock_getOptFlds", "cdecl")
    ReportControlBlock_getOptFlds.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getOptFlds.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 333
if _libs["libiec61850.so"].has("ReportControlBlock_getBufTm", "cdecl"):
    ReportControlBlock_getBufTm = _libs["libiec61850.so"].get("ReportControlBlock_getBufTm", "cdecl")
    ReportControlBlock_getBufTm.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getBufTm.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 336
if _libs["libiec61850.so"].has("ReportControlBlock_getSqNum", "cdecl"):
    ReportControlBlock_getSqNum = _libs["libiec61850.so"].get("ReportControlBlock_getSqNum", "cdecl")
    ReportControlBlock_getSqNum.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getSqNum.restype = uint16_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 353
if _libs["libiec61850.so"].has("ReportControlBlock_getTrgOps", "cdecl"):
    ReportControlBlock_getTrgOps = _libs["libiec61850.so"].get("ReportControlBlock_getTrgOps", "cdecl")
    ReportControlBlock_getTrgOps.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getTrgOps.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 356
if _libs["libiec61850.so"].has("ReportControlBlock_getIntgPd", "cdecl"):
    ReportControlBlock_getIntgPd = _libs["libiec61850.so"].get("ReportControlBlock_getIntgPd", "cdecl")
    ReportControlBlock_getIntgPd.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getIntgPd.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 359
if _libs["libiec61850.so"].has("ReportControlBlock_getGI", "cdecl"):
    ReportControlBlock_getGI = _libs["libiec61850.so"].get("ReportControlBlock_getGI", "cdecl")
    ReportControlBlock_getGI.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getGI.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 362
if _libs["libiec61850.so"].has("ReportControlBlock_getPurgeBuf", "cdecl"):
    ReportControlBlock_getPurgeBuf = _libs["libiec61850.so"].get("ReportControlBlock_getPurgeBuf", "cdecl")
    ReportControlBlock_getPurgeBuf.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getPurgeBuf.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 364
if _libs["libiec61850.so"].has("ReportControlBlock_getEntryId", "cdecl"):
    ReportControlBlock_getEntryId = _libs["libiec61850.so"].get("ReportControlBlock_getEntryId", "cdecl")
    ReportControlBlock_getEntryId.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getEntryId.restype = POINTER(MmsValue)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 368
if _libs["libiec61850.so"].has("ReportControlBlock_getTimeofEntry", "cdecl"):
    ReportControlBlock_getTimeofEntry = _libs["libiec61850.so"].get("ReportControlBlock_getTimeofEntry", "cdecl")
    ReportControlBlock_getTimeofEntry.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getTimeofEntry.restype = uint64_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 371
if _libs["libiec61850.so"].has("ReportControlBlock_getResvTms", "cdecl"):
    ReportControlBlock_getResvTms = _libs["libiec61850.so"].get("ReportControlBlock_getResvTms", "cdecl")
    ReportControlBlock_getResvTms.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getResvTms.restype = c_int16

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 374
if _libs["libiec61850.so"].has("ReportControlBlock_getResv", "cdecl"):
    ReportControlBlock_getResv = _libs["libiec61850.so"].get("ReportControlBlock_getResv", "cdecl")
    ReportControlBlock_getResv.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getResv.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 376
if _libs["libiec61850.so"].has("ReportControlBlock_getOwner", "cdecl"):
    ReportControlBlock_getOwner = _libs["libiec61850.so"].get("ReportControlBlock_getOwner", "cdecl")
    ReportControlBlock_getOwner.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getOwner.restype = POINTER(MmsValue)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 396
if _libs["libiec61850.so"].has("LogControlBlock_create", "cdecl"):
    LogControlBlock_create = _libs["libiec61850.so"].get("LogControlBlock_create", "cdecl")
    LogControlBlock_create.argtypes = [String, POINTER(LogicalNode), String, String, uint8_t, uint32_t, c_bool, c_bool]
    LogControlBlock_create.restype = POINTER(LogControlBlock)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 400
if _libs["libiec61850.so"].has("LogControlBlock_getName", "cdecl"):
    LogControlBlock_getName = _libs["libiec61850.so"].get("LogControlBlock_getName", "cdecl")
    LogControlBlock_getName.argtypes = [POINTER(LogControlBlock)]
    LogControlBlock_getName.restype = c_char_p

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 403
if _libs["libiec61850.so"].has("LogControlBlock_getParent", "cdecl"):
    LogControlBlock_getParent = _libs["libiec61850.so"].get("LogControlBlock_getParent", "cdecl")
    LogControlBlock_getParent.argtypes = [POINTER(LogControlBlock)]
    LogControlBlock_getParent.restype = POINTER(LogicalNode)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 414
if _libs["libiec61850.so"].has("Log_create", "cdecl"):
    Log_create = _libs["libiec61850.so"].get("Log_create", "cdecl")
    Log_create.argtypes = [String, POINTER(LogicalNode)]
    Log_create.restype = POINTER(Log)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 428
if _libs["libiec61850.so"].has("SettingGroupControlBlock_create", "cdecl"):
    SettingGroupControlBlock_create = _libs["libiec61850.so"].get("SettingGroupControlBlock_create", "cdecl")
    SettingGroupControlBlock_create.argtypes = [POINTER(LogicalNode), uint8_t, uint8_t]
    SettingGroupControlBlock_create.restype = POINTER(SettingGroupControlBlock)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 447
if _libs["libiec61850.so"].has("GSEControlBlock_create", "cdecl"):
    GSEControlBlock_create = _libs["libiec61850.so"].get("GSEControlBlock_create", "cdecl")
    GSEControlBlock_create.argtypes = [String, POINTER(LogicalNode), String, String, uint32_t, c_bool, c_int, c_int]
    GSEControlBlock_create.restype = POINTER(GSEControlBlock)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 467
if _libs["libiec61850.so"].has("SVControlBlock_create", "cdecl"):
    SVControlBlock_create = _libs["libiec61850.so"].get("SVControlBlock_create", "cdecl")
    SVControlBlock_create.argtypes = [String, POINTER(LogicalNode), String, String, uint32_t, uint8_t, uint16_t, uint8_t, c_bool]
    SVControlBlock_create.restype = POINTER(SVControlBlock)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 472
if _libs["libiec61850.so"].has("SVControlBlock_addPhyComAddress", "cdecl"):
    SVControlBlock_addPhyComAddress = _libs["libiec61850.so"].get("SVControlBlock_addPhyComAddress", "cdecl")
    SVControlBlock_addPhyComAddress.argtypes = [POINTER(SVControlBlock), POINTER(PhyComAddress)]
    SVControlBlock_addPhyComAddress.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 475
if _libs["libiec61850.so"].has("GSEControlBlock_addPhyComAddress", "cdecl"):
    GSEControlBlock_addPhyComAddress = _libs["libiec61850.so"].get("GSEControlBlock_addPhyComAddress", "cdecl")
    GSEControlBlock_addPhyComAddress.argtypes = [POINTER(GSEControlBlock), POINTER(PhyComAddress)]
    GSEControlBlock_addPhyComAddress.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 489
if _libs["libiec61850.so"].has("PhyComAddress_create", "cdecl"):
    PhyComAddress_create = _libs["libiec61850.so"].get("PhyComAddress_create", "cdecl")
    PhyComAddress_create.argtypes = [uint8_t, uint16_t, uint16_t, POINTER(uint8_t)]
    PhyComAddress_create.restype = POINTER(PhyComAddress)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 500
if _libs["libiec61850.so"].has("DataSet_create", "cdecl"):
    DataSet_create = _libs["libiec61850.so"].get("DataSet_create", "cdecl")
    DataSet_create.argtypes = [String, POINTER(LogicalNode)]
    DataSet_create.restype = POINTER(DataSet)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 510
if _libs["libiec61850.so"].has("DataSet_getName", "cdecl"):
    DataSet_getName = _libs["libiec61850.so"].get("DataSet_getName", "cdecl")
    DataSet_getName.argtypes = [POINTER(DataSet)]
    DataSet_getName.restype = c_char_p

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 521
if _libs["libiec61850.so"].has("DataSet_getSize", "cdecl"):
    DataSet_getSize = _libs["libiec61850.so"].get("DataSet_getSize", "cdecl")
    DataSet_getSize.argtypes = [POINTER(DataSet)]
    DataSet_getSize.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 523
if _libs["libiec61850.so"].has("DataSet_getFirstEntry", "cdecl"):
    DataSet_getFirstEntry = _libs["libiec61850.so"].get("DataSet_getFirstEntry", "cdecl")
    DataSet_getFirstEntry.argtypes = [POINTER(DataSet)]
    DataSet_getFirstEntry.restype = POINTER(DataSetEntry)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 526
if _libs["libiec61850.so"].has("DataSetEntry_getNext", "cdecl"):
    DataSetEntry_getNext = _libs["libiec61850.so"].get("DataSetEntry_getNext", "cdecl")
    DataSetEntry_getNext.argtypes = [POINTER(DataSetEntry)]
    DataSetEntry_getNext.restype = POINTER(DataSetEntry)

# /home/user/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 549
if _libs["libiec61850.so"].has("DataSetEntry_create", "cdecl"):
    DataSetEntry_create = _libs["libiec61850.so"].get("DataSetEntry_create", "cdecl")
    DataSetEntry_create.argtypes = [POINTER(DataSet), String, c_int, String]
    DataSetEntry_create.restype = POINTER(DataSetEntry)

enum_anon_49 = c_int# ../libiec61850/src/mms/inc/mms_server.h: 42

MMS_SERVER_NEW_CONNECTION = 0# ../libiec61850/src/mms/inc/mms_server.h: 42

MMS_SERVER_CONNECTION_CLOSED = (MMS_SERVER_NEW_CONNECTION + 1)# ../libiec61850/src/mms/inc/mms_server.h: 42

MMS_SERVER_CONNECTION_TICK = (MMS_SERVER_CONNECTION_CLOSED + 1)# ../libiec61850/src/mms/inc/mms_server.h: 42

MmsServerEvent = enum_anon_49# ../libiec61850/src/mms/inc/mms_server.h: 42

# ../libiec61850/src/mms/inc/mms_server.h: 44
class struct_sMmsServer(Structure):
    pass

MmsServer = POINTER(struct_sMmsServer)# ../libiec61850/src/mms/inc/mms_server.h: 44

# ../libiec61850/src/mms/inc/mms_server.h: 46
class struct_sMmsServerConnection(Structure):
    pass

MmsServerConnection = POINTER(struct_sMmsServerConnection)# ../libiec61850/src/mms/inc/mms_server.h: 46

enum_anon_50 = c_int# ../libiec61850/src/mms/inc/mms_server.h: 52

MMS_DOMAIN_SPECIFIC = 0# ../libiec61850/src/mms/inc/mms_server.h: 52

MMS_ASSOCIATION_SPECIFIC = (MMS_DOMAIN_SPECIFIC + 1)# ../libiec61850/src/mms/inc/mms_server.h: 52

MMS_VMD_SPECIFIC = (MMS_ASSOCIATION_SPECIFIC + 1)# ../libiec61850/src/mms/inc/mms_server.h: 52

MmsVariableListType = enum_anon_50# ../libiec61850/src/mms/inc/mms_server.h: 52

# ../libiec61850/src/mms/inc/mms_server.h: 55
for _lib in _libs.values():
    if not _lib.has("MmsServer_setLocalIpAddress", "cdecl"):
        continue
    MmsServer_setLocalIpAddress = _lib.get("MmsServer_setLocalIpAddress", "cdecl")
    MmsServer_setLocalIpAddress.argtypes = [MmsServer, String]
    MmsServer_setLocalIpAddress.restype = None
    break

# ../libiec61850/src/mms/inc/mms_server.h: 58
for _lib in _libs.values():
    if not _lib.has("MmsServer_isRunning", "cdecl"):
        continue
    MmsServer_isRunning = _lib.get("MmsServer_isRunning", "cdecl")
    MmsServer_isRunning.argtypes = [MmsServer]
    MmsServer_isRunning.restype = c_bool
    break

enum_anon_51 = c_int# ../libiec61850/src/mms/inc/mms_server.h: 66

MMS_VARLIST_CREATE = 0# ../libiec61850/src/mms/inc/mms_server.h: 66

MMS_VARLIST_DELETE = (MMS_VARLIST_CREATE + 1)# ../libiec61850/src/mms/inc/mms_server.h: 66

MMS_VARLIST_READ = (MMS_VARLIST_DELETE + 1)# ../libiec61850/src/mms/inc/mms_server.h: 66

MMS_VARLIST_WRITE = (MMS_VARLIST_READ + 1)# ../libiec61850/src/mms/inc/mms_server.h: 66

MMS_VARLIST_GET_DIRECTORY = (MMS_VARLIST_WRITE + 1)# ../libiec61850/src/mms/inc/mms_server.h: 66

MmsVariableListAccessType = enum_anon_51# ../libiec61850/src/mms/inc/mms_server.h: 66

MmsNamedVariableListAccessHandler = CFUNCTYPE(UNCHECKED(MmsError), POINTER(None), MmsVariableListAccessType, MmsVariableListType, POINTER(MmsDomain), String, MmsServerConnection)# ../libiec61850/src/mms/inc/mms_server.h: 80

# ../libiec61850/src/mms/inc/mms_server.h: 91
for _lib in _libs.values():
    if not _lib.has("MmsServer_installVariableListAccessHandler", "cdecl"):
        continue
    MmsServer_installVariableListAccessHandler = _lib.get("MmsServer_installVariableListAccessHandler", "cdecl")
    MmsServer_installVariableListAccessHandler.argtypes = [MmsServer, MmsNamedVariableListAccessHandler, POINTER(None)]
    MmsServer_installVariableListAccessHandler.restype = None
    break

MmsReadJournalHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), POINTER(MmsDomain), String, MmsServerConnection)# ../libiec61850/src/mms/inc/mms_server.h: 101

# ../libiec61850/src/mms/inc/mms_server.h: 111
for _lib in _libs.values():
    if not _lib.has("MmsServer_installReadJournalHandler", "cdecl"):
        continue
    MmsServer_installReadJournalHandler = _lib.get("MmsServer_installReadJournalHandler", "cdecl")
    MmsServer_installReadJournalHandler.argtypes = [MmsServer, MmsReadJournalHandler, POINTER(None)]
    MmsServer_installReadJournalHandler.restype = None
    break

enum_anon_52 = c_int# ../libiec61850/src/mms/inc/mms_server.h: 118

MMS_GETNAMELIST_DOMAINS = 0# ../libiec61850/src/mms/inc/mms_server.h: 118

MMS_GETNAMELIST_JOURNALS = (MMS_GETNAMELIST_DOMAINS + 1)# ../libiec61850/src/mms/inc/mms_server.h: 118

MMS_GETNAMELIST_DATASETS = (MMS_GETNAMELIST_JOURNALS + 1)# ../libiec61850/src/mms/inc/mms_server.h: 118

MMS_GETNAMELIST_DATA = (MMS_GETNAMELIST_DATASETS + 1)# ../libiec61850/src/mms/inc/mms_server.h: 118

MmsGetNameListType = enum_anon_52# ../libiec61850/src/mms/inc/mms_server.h: 118

MmsGetNameListHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), MmsGetNameListType, POINTER(MmsDomain), MmsServerConnection)# ../libiec61850/src/mms/inc/mms_server.h: 120

# ../libiec61850/src/mms/inc/mms_server.h: 123
for _lib in _libs.values():
    if not _lib.has("MmsServer_installGetNameListHandler", "cdecl"):
        continue
    MmsServer_installGetNameListHandler = _lib.get("MmsServer_installGetNameListHandler", "cdecl")
    MmsServer_installGetNameListHandler.argtypes = [MmsServer, MmsGetNameListHandler, POINTER(None)]
    MmsServer_installGetNameListHandler.restype = None
    break

MmsObtainFileHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), MmsServerConnection, String, String)# ../libiec61850/src/mms/inc/mms_server.h: 136

# ../libiec61850/src/mms/inc/mms_server.h: 148
for _lib in _libs.values():
    if not _lib.has("MmsServer_installObtainFileHandler", "cdecl"):
        continue
    MmsServer_installObtainFileHandler = _lib.get("MmsServer_installObtainFileHandler", "cdecl")
    MmsServer_installObtainFileHandler.argtypes = [MmsServer, MmsObtainFileHandler, POINTER(None)]
    MmsServer_installObtainFileHandler.restype = None
    break

MmsGetFileCompleteHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), MmsServerConnection, String)# ../libiec61850/src/mms/inc/mms_server.h: 159

# ../libiec61850/src/mms/inc/mms_server.h: 170
for _lib in _libs.values():
    if not _lib.has("MmsServer_installGetFileCompleteHandler", "cdecl"):
        continue
    MmsServer_installGetFileCompleteHandler = _lib.get("MmsServer_installGetFileCompleteHandler", "cdecl")
    MmsServer_installGetFileCompleteHandler.argtypes = [MmsServer, MmsGetFileCompleteHandler, POINTER(None)]
    MmsServer_installGetFileCompleteHandler.restype = None
    break

enum_anon_53 = c_int# ../libiec61850/src/mms/inc/mms_server.h: 179

MMS_FILE_ACCESS_TYPE_READ_DIRECTORY = 0# ../libiec61850/src/mms/inc/mms_server.h: 179

MMS_FILE_ACCESS_TYPE_OPEN = (MMS_FILE_ACCESS_TYPE_READ_DIRECTORY + 1)# ../libiec61850/src/mms/inc/mms_server.h: 179

MMS_FILE_ACCESS_TYPE_OBTAIN = (MMS_FILE_ACCESS_TYPE_OPEN + 1)# ../libiec61850/src/mms/inc/mms_server.h: 179

MMS_FILE_ACCESS_TYPE_DELETE = (MMS_FILE_ACCESS_TYPE_OBTAIN + 1)# ../libiec61850/src/mms/inc/mms_server.h: 179

MMS_FILE_ACCESS_TYPE_RENAME = (MMS_FILE_ACCESS_TYPE_DELETE + 1)# ../libiec61850/src/mms/inc/mms_server.h: 179

MmsFileServiceType = enum_anon_53# ../libiec61850/src/mms/inc/mms_server.h: 179

MmsFileAccessHandler = CFUNCTYPE(UNCHECKED(MmsError), POINTER(None), MmsServerConnection, MmsFileServiceType, String, String)# ../libiec61850/src/mms/inc/mms_server.h: 192

# ../libiec61850/src/mms/inc/mms_server.h: 205
if _libs["libiec61850.so"].has("MmsServer_installFileAccessHandler", "cdecl"):
    MmsServer_installFileAccessHandler = _libs["libiec61850.so"].get("MmsServer_installFileAccessHandler", "cdecl")
    MmsServer_installFileAccessHandler.argtypes = [MmsServer, MmsFileAccessHandler, POINTER(None)]
    MmsServer_installFileAccessHandler.restype = None

# ../libiec61850/src/mms/inc/mms_server.h: 218
for _lib in _libs.values():
    if not _lib.has("MmsServer_setFilestoreBasepath", "cdecl"):
        continue
    MmsServer_setFilestoreBasepath = _lib.get("MmsServer_setFilestoreBasepath", "cdecl")
    MmsServer_setFilestoreBasepath.argtypes = [MmsServer, String]
    MmsServer_setFilestoreBasepath.restype = None
    break

# ../libiec61850/src/mms/inc/mms_server.h: 226
for _lib in _libs.values():
    if not _lib.has("MmsServer_setMaxConnections", "cdecl"):
        continue
    MmsServer_setMaxConnections = _lib.get("MmsServer_setMaxConnections", "cdecl")
    MmsServer_setMaxConnections.argtypes = [MmsServer, c_int]
    MmsServer_setMaxConnections.restype = None
    break

# ../libiec61850/src/mms/inc/mms_server.h: 237
for _lib in _libs.values():
    if not _lib.has("MmsServer_enableFileService", "cdecl"):
        continue
    MmsServer_enableFileService = _lib.get("MmsServer_enableFileService", "cdecl")
    MmsServer_enableFileService.argtypes = [MmsServer, c_bool]
    MmsServer_enableFileService.restype = None
    break

# ../libiec61850/src/mms/inc/mms_server.h: 248
for _lib in _libs.values():
    if not _lib.has("MmsServer_enableDynamicNamedVariableListService", "cdecl"):
        continue
    MmsServer_enableDynamicNamedVariableListService = _lib.get("MmsServer_enableDynamicNamedVariableListService", "cdecl")
    MmsServer_enableDynamicNamedVariableListService.argtypes = [MmsServer, c_bool]
    MmsServer_enableDynamicNamedVariableListService.restype = None
    break

# ../libiec61850/src/mms/inc/mms_server.h: 257
for _lib in _libs.values():
    if not _lib.has("MmsServer_setMaxAssociationSpecificDataSets", "cdecl"):
        continue
    MmsServer_setMaxAssociationSpecificDataSets = _lib.get("MmsServer_setMaxAssociationSpecificDataSets", "cdecl")
    MmsServer_setMaxAssociationSpecificDataSets.argtypes = [MmsServer, c_int]
    MmsServer_setMaxAssociationSpecificDataSets.restype = None
    break

# ../libiec61850/src/mms/inc/mms_server.h: 266
for _lib in _libs.values():
    if not _lib.has("MmsServer_setMaxDomainSpecificDataSets", "cdecl"):
        continue
    MmsServer_setMaxDomainSpecificDataSets = _lib.get("MmsServer_setMaxDomainSpecificDataSets", "cdecl")
    MmsServer_setMaxDomainSpecificDataSets.argtypes = [MmsServer, c_int]
    MmsServer_setMaxDomainSpecificDataSets.restype = None
    break

# ../libiec61850/src/mms/inc/mms_server.h: 275
for _lib in _libs.values():
    if not _lib.has("MmsServer_setMaxDataSetEntries", "cdecl"):
        continue
    MmsServer_setMaxDataSetEntries = _lib.get("MmsServer_setMaxDataSetEntries", "cdecl")
    MmsServer_setMaxDataSetEntries.argtypes = [MmsServer, c_int]
    MmsServer_setMaxDataSetEntries.restype = None
    break

# ../libiec61850/src/mms/inc/mms_server.h: 286
for _lib in _libs.values():
    if not _lib.has("MmsServer_enableJournalService", "cdecl"):
        continue
    MmsServer_enableJournalService = _lib.get("MmsServer_enableJournalService", "cdecl")
    MmsServer_enableJournalService.argtypes = [MmsServer, c_bool]
    MmsServer_enableJournalService.restype = None
    break

# ../libiec61850/src/mms/inc/mms_server.h: 308
for _lib in _libs.values():
    if not _lib.has("MmsServer_setServerIdentity", "cdecl"):
        continue
    MmsServer_setServerIdentity = _lib.get("MmsServer_setServerIdentity", "cdecl")
    MmsServer_setServerIdentity.argtypes = [MmsServer, String, String, String]
    MmsServer_setServerIdentity.restype = None
    break

# ../libiec61850/src/mms/inc/mms_server.h: 316
for _lib in _libs.values():
    if not _lib.has("MmsServer_getVendorName", "cdecl"):
        continue
    MmsServer_getVendorName = _lib.get("MmsServer_getVendorName", "cdecl")
    MmsServer_getVendorName.argtypes = [MmsServer]
    if sizeof(c_int) == sizeof(c_void_p):
        MmsServer_getVendorName.restype = ReturnString
    else:
        MmsServer_getVendorName.restype = String
        MmsServer_getVendorName.errcheck = ReturnString
    break

# ../libiec61850/src/mms/inc/mms_server.h: 325
for _lib in _libs.values():
    if not _lib.has("MmsServer_getModelName", "cdecl"):
        continue
    MmsServer_getModelName = _lib.get("MmsServer_getModelName", "cdecl")
    MmsServer_getModelName.argtypes = [MmsServer]
    if sizeof(c_int) == sizeof(c_void_p):
        MmsServer_getModelName.restype = ReturnString
    else:
        MmsServer_getModelName.restype = String
        MmsServer_getModelName.errcheck = ReturnString
    break

# ../libiec61850/src/mms/inc/mms_server.h: 334
for _lib in _libs.values():
    if not _lib.has("MmsServer_getRevision", "cdecl"):
        continue
    MmsServer_getRevision = _lib.get("MmsServer_getRevision", "cdecl")
    MmsServer_getRevision.argtypes = [MmsServer]
    if sizeof(c_int) == sizeof(c_void_p):
        MmsServer_getRevision.restype = ReturnString
    else:
        MmsServer_getRevision.restype = String
        MmsServer_getRevision.errcheck = ReturnString
    break

MmsStatusRequestListener = CFUNCTYPE(UNCHECKED(None), POINTER(None), MmsServer, MmsServerConnection, c_bool)# ../libiec61850/src/mms/inc/mms_server.h: 362

# ../libiec61850/src/mms/inc/mms_server.h: 372
for _lib in _libs.values():
    if not _lib.has("MmsServer_setVMDStatus", "cdecl"):
        continue
    MmsServer_setVMDStatus = _lib.get("MmsServer_setVMDStatus", "cdecl")
    MmsServer_setVMDStatus.argtypes = [MmsServer, c_int, c_int]
    MmsServer_setVMDStatus.restype = None
    break

# ../libiec61850/src/mms/inc/mms_server.h: 380
for _lib in _libs.values():
    if not _lib.has("MmsServer_getVMDLogicalStatus", "cdecl"):
        continue
    MmsServer_getVMDLogicalStatus = _lib.get("MmsServer_getVMDLogicalStatus", "cdecl")
    MmsServer_getVMDLogicalStatus.argtypes = [MmsServer]
    MmsServer_getVMDLogicalStatus.restype = c_int
    break

# ../libiec61850/src/mms/inc/mms_server.h: 388
for _lib in _libs.values():
    if not _lib.has("MmsServer_getVMDPhysicalStatus", "cdecl"):
        continue
    MmsServer_getVMDPhysicalStatus = _lib.get("MmsServer_getVMDPhysicalStatus", "cdecl")
    MmsServer_getVMDPhysicalStatus.argtypes = [MmsServer]
    MmsServer_getVMDPhysicalStatus.restype = c_int
    break

# ../libiec61850/src/mms/inc/mms_server.h: 402
for _lib in _libs.values():
    if not _lib.has("MmsServer_setStatusRequestListener", "cdecl"):
        continue
    MmsServer_setStatusRequestListener = _lib.get("MmsServer_setStatusRequestListener", "cdecl")
    MmsServer_setStatusRequestListener.argtypes = [MmsServer, MmsStatusRequestListener, POINTER(None)]
    MmsServer_setStatusRequestListener.restype = None
    break

# ../libiec61850/src/mms/inc/mms_server.h: 404
for _lib in _libs.values():
    if not _lib.has("MmsServerConnection_getClientAddress", "cdecl"):
        continue
    MmsServerConnection_getClientAddress = _lib.get("MmsServerConnection_getClientAddress", "cdecl")
    MmsServerConnection_getClientAddress.argtypes = [MmsServerConnection]
    if sizeof(c_int) == sizeof(c_void_p):
        MmsServerConnection_getClientAddress.restype = ReturnString
    else:
        MmsServerConnection_getClientAddress.restype = String
        MmsServerConnection_getClientAddress.errcheck = ReturnString
    break

# ../libiec61850/src/mms/inc/mms_server.h: 407
for _lib in _libs.values():
    if not _lib.has("MmsServerConnection_getLocalAddress", "cdecl"):
        continue
    MmsServerConnection_getLocalAddress = _lib.get("MmsServerConnection_getLocalAddress", "cdecl")
    MmsServerConnection_getLocalAddress.argtypes = [MmsServerConnection]
    if sizeof(c_int) == sizeof(c_void_p):
        MmsServerConnection_getLocalAddress.restype = ReturnString
    else:
        MmsServerConnection_getLocalAddress.restype = String
        MmsServerConnection_getLocalAddress.errcheck = ReturnString
    break

# ../libiec61850/src/mms/inc/mms_server.h: 410
for _lib in _libs.values():
    if not _lib.has("MmsServerConnection_getSecurityToken", "cdecl"):
        continue
    MmsServerConnection_getSecurityToken = _lib.get("MmsServerConnection_getSecurityToken", "cdecl")
    MmsServerConnection_getSecurityToken.argtypes = [MmsServerConnection]
    MmsServerConnection_getSecurityToken.restype = POINTER(c_ubyte)
    MmsServerConnection_getSecurityToken.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# ../libiec61850/src/mms/inc/mms_server.h: 414
for _lib in _libs.values():
    if not _lib.has("MmsServer_ignoreClientRequests", "cdecl"):
        continue
    MmsServer_ignoreClientRequests = _lib.get("MmsServer_ignoreClientRequests", "cdecl")
    MmsServer_ignoreClientRequests.argtypes = [MmsServer, c_bool]
    MmsServer_ignoreClientRequests.restype = None
    break

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 71
class struct_sIedServerConfig(Structure):
    pass

IedServerConfig = POINTER(struct_sIedServerConfig)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 69

struct_sIedServerConfig.__slots__ = [
    'reportBufferSize',
    'reportBufferSizeURCBs',
    'fileServiceBasepath',
    'enableFileService',
    'enableDynamicDataSetService',
    'maxAssociationSpecificDataSets',
    'maxDomainSpecificDataSets',
    'maxDataSetEntries',
    'enableLogService',
    'useIntegratedGoosePublisher',
    'edition',
    'maxMmsConnections',
    'enableEditSG',
    'enableResvTmsForSGCB',
    'enableResvTmsForBRCB',
    'enableOwnerForRCB',
    'syncIntegrityReportTimes',
    'reportSettingsWritable',
]
struct_sIedServerConfig._fields_ = [
    ('reportBufferSize', c_int),
    ('reportBufferSizeURCBs', c_int),
    ('fileServiceBasepath', String),
    ('enableFileService', c_bool),
    ('enableDynamicDataSetService', c_bool),
    ('maxAssociationSpecificDataSets', c_int),
    ('maxDomainSpecificDataSets', c_int),
    ('maxDataSetEntries', c_int),
    ('enableLogService', c_bool),
    ('useIntegratedGoosePublisher', c_bool),
    ('edition', uint8_t),
    ('maxMmsConnections', c_int),
    ('enableEditSG', c_bool),
    ('enableResvTmsForSGCB', c_bool),
    ('enableResvTmsForBRCB', c_bool),
    ('enableOwnerForRCB', c_bool),
    ('syncIntegrityReportTimes', c_bool),
    ('reportSettingsWritable', uint8_t),
]

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 134
if _libs["libiec61850.so"].has("IedServerConfig_create", "cdecl"):
    IedServerConfig_create = _libs["libiec61850.so"].get("IedServerConfig_create", "cdecl")
    IedServerConfig_create.argtypes = []
    IedServerConfig_create.restype = IedServerConfig

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 140
if _libs["libiec61850.so"].has("IedServerConfig_destroy", "cdecl"):
    IedServerConfig_destroy = _libs["libiec61850.so"].get("IedServerConfig_destroy", "cdecl")
    IedServerConfig_destroy.argtypes = [IedServerConfig]
    IedServerConfig_destroy.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 148
if _libs["libiec61850.so"].has("IedServerConfig_setEdition", "cdecl"):
    IedServerConfig_setEdition = _libs["libiec61850.so"].get("IedServerConfig_setEdition", "cdecl")
    IedServerConfig_setEdition.argtypes = [IedServerConfig, uint8_t]
    IedServerConfig_setEdition.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 156
if _libs["libiec61850.so"].has("IedServerConfig_getEdition", "cdecl"):
    IedServerConfig_getEdition = _libs["libiec61850.so"].get("IedServerConfig_getEdition", "cdecl")
    IedServerConfig_getEdition.argtypes = [IedServerConfig]
    IedServerConfig_getEdition.restype = uint8_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 164
if _libs["libiec61850.so"].has("IedServerConfig_setReportBufferSize", "cdecl"):
    IedServerConfig_setReportBufferSize = _libs["libiec61850.so"].get("IedServerConfig_setReportBufferSize", "cdecl")
    IedServerConfig_setReportBufferSize.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setReportBufferSize.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 172
if _libs["libiec61850.so"].has("IedServerConfig_getReportBufferSize", "cdecl"):
    IedServerConfig_getReportBufferSize = _libs["libiec61850.so"].get("IedServerConfig_getReportBufferSize", "cdecl")
    IedServerConfig_getReportBufferSize.argtypes = [IedServerConfig]
    IedServerConfig_getReportBufferSize.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 180
if _libs["libiec61850.so"].has("IedServerConfig_setReportBufferSizeForURCBs", "cdecl"):
    IedServerConfig_setReportBufferSizeForURCBs = _libs["libiec61850.so"].get("IedServerConfig_setReportBufferSizeForURCBs", "cdecl")
    IedServerConfig_setReportBufferSizeForURCBs.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setReportBufferSizeForURCBs.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 188
if _libs["libiec61850.so"].has("IedServerConfig_getReportBufferSizeForURCBs", "cdecl"):
    IedServerConfig_getReportBufferSizeForURCBs = _libs["libiec61850.so"].get("IedServerConfig_getReportBufferSizeForURCBs", "cdecl")
    IedServerConfig_getReportBufferSizeForURCBs.argtypes = [IedServerConfig]
    IedServerConfig_getReportBufferSizeForURCBs.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 199
if _libs["libiec61850.so"].has("IedServerConfig_setMaxMmsConnections", "cdecl"):
    IedServerConfig_setMaxMmsConnections = _libs["libiec61850.so"].get("IedServerConfig_setMaxMmsConnections", "cdecl")
    IedServerConfig_setMaxMmsConnections.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setMaxMmsConnections.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 207
if _libs["libiec61850.so"].has("IedServerConfig_getMaxMmsConnections", "cdecl"):
    IedServerConfig_getMaxMmsConnections = _libs["libiec61850.so"].get("IedServerConfig_getMaxMmsConnections", "cdecl")
    IedServerConfig_getMaxMmsConnections.argtypes = [IedServerConfig]
    IedServerConfig_getMaxMmsConnections.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 219
if _libs["libiec61850.so"].has("IedServerConfig_setSyncIntegrityReportTimes", "cdecl"):
    IedServerConfig_setSyncIntegrityReportTimes = _libs["libiec61850.so"].get("IedServerConfig_setSyncIntegrityReportTimes", "cdecl")
    IedServerConfig_setSyncIntegrityReportTimes.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_setSyncIntegrityReportTimes.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 231
if _libs["libiec61850.so"].has("IedServerConfig_getSyncIntegrityReportTimes", "cdecl"):
    IedServerConfig_getSyncIntegrityReportTimes = _libs["libiec61850.so"].get("IedServerConfig_getSyncIntegrityReportTimes", "cdecl")
    IedServerConfig_getSyncIntegrityReportTimes.argtypes = [IedServerConfig]
    IedServerConfig_getSyncIntegrityReportTimes.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 241
if _libs["libiec61850.so"].has("IedServerConfig_setFileServiceBasePath", "cdecl"):
    IedServerConfig_setFileServiceBasePath = _libs["libiec61850.so"].get("IedServerConfig_setFileServiceBasePath", "cdecl")
    IedServerConfig_setFileServiceBasePath.argtypes = [IedServerConfig, String]
    IedServerConfig_setFileServiceBasePath.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 246
if _libs["libiec61850.so"].has("IedServerConfig_getFileServiceBasePath", "cdecl"):
    IedServerConfig_getFileServiceBasePath = _libs["libiec61850.so"].get("IedServerConfig_getFileServiceBasePath", "cdecl")
    IedServerConfig_getFileServiceBasePath.argtypes = [IedServerConfig]
    IedServerConfig_getFileServiceBasePath.restype = c_char_p

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 255
if _libs["libiec61850.so"].has("IedServerConfig_enableFileService", "cdecl"):
    IedServerConfig_enableFileService = _libs["libiec61850.so"].get("IedServerConfig_enableFileService", "cdecl")
    IedServerConfig_enableFileService.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_enableFileService.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 263
if _libs["libiec61850.so"].has("IedServerConfig_isFileServiceEnabled", "cdecl"):
    IedServerConfig_isFileServiceEnabled = _libs["libiec61850.so"].get("IedServerConfig_isFileServiceEnabled", "cdecl")
    IedServerConfig_isFileServiceEnabled.argtypes = [IedServerConfig]
    IedServerConfig_isFileServiceEnabled.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 271
if _libs["libiec61850.so"].has("IedServerConfig_enableDynamicDataSetService", "cdecl"):
    IedServerConfig_enableDynamicDataSetService = _libs["libiec61850.so"].get("IedServerConfig_enableDynamicDataSetService", "cdecl")
    IedServerConfig_enableDynamicDataSetService.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_enableDynamicDataSetService.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 279
if _libs["libiec61850.so"].has("IedServerConfig_isDynamicDataSetServiceEnabled", "cdecl"):
    IedServerConfig_isDynamicDataSetServiceEnabled = _libs["libiec61850.so"].get("IedServerConfig_isDynamicDataSetServiceEnabled", "cdecl")
    IedServerConfig_isDynamicDataSetServiceEnabled.argtypes = [IedServerConfig]
    IedServerConfig_isDynamicDataSetServiceEnabled.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 290
if _libs["libiec61850.so"].has("IedServerConfig_setMaxAssociationSpecificDataSets", "cdecl"):
    IedServerConfig_setMaxAssociationSpecificDataSets = _libs["libiec61850.so"].get("IedServerConfig_setMaxAssociationSpecificDataSets", "cdecl")
    IedServerConfig_setMaxAssociationSpecificDataSets.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setMaxAssociationSpecificDataSets.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 298
if _libs["libiec61850.so"].has("IedServerConfig_getMaxAssociationSpecificDataSets", "cdecl"):
    IedServerConfig_getMaxAssociationSpecificDataSets = _libs["libiec61850.so"].get("IedServerConfig_getMaxAssociationSpecificDataSets", "cdecl")
    IedServerConfig_getMaxAssociationSpecificDataSets.argtypes = [IedServerConfig]
    IedServerConfig_getMaxAssociationSpecificDataSets.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 306
if _libs["libiec61850.so"].has("IedServerConfig_setMaxDomainSpecificDataSets", "cdecl"):
    IedServerConfig_setMaxDomainSpecificDataSets = _libs["libiec61850.so"].get("IedServerConfig_setMaxDomainSpecificDataSets", "cdecl")
    IedServerConfig_setMaxDomainSpecificDataSets.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setMaxDomainSpecificDataSets.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 314
if _libs["libiec61850.so"].has("IedServerConfig_getMaxDomainSpecificDataSets", "cdecl"):
    IedServerConfig_getMaxDomainSpecificDataSets = _libs["libiec61850.so"].get("IedServerConfig_getMaxDomainSpecificDataSets", "cdecl")
    IedServerConfig_getMaxDomainSpecificDataSets.argtypes = [IedServerConfig]
    IedServerConfig_getMaxDomainSpecificDataSets.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 326
if _libs["libiec61850.so"].has("IedServerConfig_setMaxDataSetEntries", "cdecl"):
    IedServerConfig_setMaxDataSetEntries = _libs["libiec61850.so"].get("IedServerConfig_setMaxDataSetEntries", "cdecl")
    IedServerConfig_setMaxDataSetEntries.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setMaxDataSetEntries.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 334
if _libs["libiec61850.so"].has("IedServerConfig_getMaxDatasSetEntries", "cdecl"):
    IedServerConfig_getMaxDatasSetEntries = _libs["libiec61850.so"].get("IedServerConfig_getMaxDatasSetEntries", "cdecl")
    IedServerConfig_getMaxDatasSetEntries.argtypes = [IedServerConfig]
    IedServerConfig_getMaxDatasSetEntries.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 342
if _libs["libiec61850.so"].has("IedServerConfig_enableLogService", "cdecl"):
    IedServerConfig_enableLogService = _libs["libiec61850.so"].get("IedServerConfig_enableLogService", "cdecl")
    IedServerConfig_enableLogService.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_enableLogService.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 353
if _libs["libiec61850.so"].has("IedServerConfig_enableEditSG", "cdecl"):
    IedServerConfig_enableEditSG = _libs["libiec61850.so"].get("IedServerConfig_enableEditSG", "cdecl")
    IedServerConfig_enableEditSG.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_enableEditSG.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 363
if _libs["libiec61850.so"].has("IedServerConfig_enableResvTmsForSGCB", "cdecl"):
    IedServerConfig_enableResvTmsForSGCB = _libs["libiec61850.so"].get("IedServerConfig_enableResvTmsForSGCB", "cdecl")
    IedServerConfig_enableResvTmsForSGCB.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_enableResvTmsForSGCB.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 371
if _libs["libiec61850.so"].has("IedServerConfig_enableResvTmsForBRCB", "cdecl"):
    IedServerConfig_enableResvTmsForBRCB = _libs["libiec61850.so"].get("IedServerConfig_enableResvTmsForBRCB", "cdecl")
    IedServerConfig_enableResvTmsForBRCB.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_enableResvTmsForBRCB.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 379
if _libs["libiec61850.so"].has("IedServerConfig_isResvTmsForBRCBEnabled", "cdecl"):
    IedServerConfig_isResvTmsForBRCBEnabled = _libs["libiec61850.so"].get("IedServerConfig_isResvTmsForBRCBEnabled", "cdecl")
    IedServerConfig_isResvTmsForBRCBEnabled.argtypes = [IedServerConfig]
    IedServerConfig_isResvTmsForBRCBEnabled.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 387
if _libs["libiec61850.so"].has("IedServerConfig_enableOwnerForRCB", "cdecl"):
    IedServerConfig_enableOwnerForRCB = _libs["libiec61850.so"].get("IedServerConfig_enableOwnerForRCB", "cdecl")
    IedServerConfig_enableOwnerForRCB.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_enableOwnerForRCB.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 395
if _libs["libiec61850.so"].has("IedServerConfig_isOwnerForRCBEnabled", "cdecl"):
    IedServerConfig_isOwnerForRCBEnabled = _libs["libiec61850.so"].get("IedServerConfig_isOwnerForRCBEnabled", "cdecl")
    IedServerConfig_isOwnerForRCBEnabled.argtypes = [IedServerConfig]
    IedServerConfig_isOwnerForRCBEnabled.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 405
if _libs["libiec61850.so"].has("IedServerConfig_useIntegratedGoosePublisher", "cdecl"):
    IedServerConfig_useIntegratedGoosePublisher = _libs["libiec61850.so"].get("IedServerConfig_useIntegratedGoosePublisher", "cdecl")
    IedServerConfig_useIntegratedGoosePublisher.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_useIntegratedGoosePublisher.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 413
if _libs["libiec61850.so"].has("IedServerConfig_isLogServiceEnabled", "cdecl"):
    IedServerConfig_isLogServiceEnabled = _libs["libiec61850.so"].get("IedServerConfig_isLogServiceEnabled", "cdecl")
    IedServerConfig_isLogServiceEnabled.argtypes = [IedServerConfig]
    IedServerConfig_isLogServiceEnabled.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 424
if _libs["libiec61850.so"].has("IedServerConfig_setReportSetting", "cdecl"):
    IedServerConfig_setReportSetting = _libs["libiec61850.so"].get("IedServerConfig_setReportSetting", "cdecl")
    IedServerConfig_setReportSetting.argtypes = [IedServerConfig, uint8_t, c_bool]
    IedServerConfig_setReportSetting.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 434
if _libs["libiec61850.so"].has("IedServerConfig_getReportSetting", "cdecl"):
    IedServerConfig_getReportSetting = _libs["libiec61850.so"].get("IedServerConfig_getReportSetting", "cdecl")
    IedServerConfig_getReportSetting.argtypes = [IedServerConfig, uint8_t]
    IedServerConfig_getReportSetting.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 449
class struct_sIedServer(Structure):
    pass

IedServer = POINTER(struct_sIedServer)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 449

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 454
class struct_sClientConnection(Structure):
    pass

ClientConnection = POINTER(struct_sClientConnection)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 454

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 464
if _libs["libiec61850.so"].has("IedServer_create", "cdecl"):
    IedServer_create = _libs["libiec61850.so"].get("IedServer_create", "cdecl")
    IedServer_create.argtypes = [POINTER(IedModel)]
    IedServer_create.restype = IedServer

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 475
if _libs["libiec61850.so"].has("IedServer_createWithTlsSupport", "cdecl"):
    IedServer_createWithTlsSupport = _libs["libiec61850.so"].get("IedServer_createWithTlsSupport", "cdecl")
    IedServer_createWithTlsSupport.argtypes = [POINTER(IedModel), TLSConfiguration]
    IedServer_createWithTlsSupport.restype = IedServer

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 485
if _libs["libiec61850.so"].has("IedServer_createWithConfig", "cdecl"):
    IedServer_createWithConfig = _libs["libiec61850.so"].get("IedServer_createWithConfig", "cdecl")
    IedServer_createWithConfig.argtypes = [POINTER(IedModel), TLSConfiguration, IedServerConfig]
    IedServer_createWithConfig.restype = IedServer

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 493
if _libs["libiec61850.so"].has("IedServer_destroy", "cdecl"):
    IedServer_destroy = _libs["libiec61850.so"].get("IedServer_destroy", "cdecl")
    IedServer_destroy.argtypes = [IedServer]
    IedServer_destroy.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 506
if _libs["libiec61850.so"].has("IedServer_addAccessPoint", "cdecl"):
    IedServer_addAccessPoint = _libs["libiec61850.so"].get("IedServer_addAccessPoint", "cdecl")
    IedServer_addAccessPoint.argtypes = [IedServer, String, c_int, TLSConfiguration]
    IedServer_addAccessPoint.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 515
if _libs["libiec61850.so"].has("IedServer_setLocalIpAddress", "cdecl"):
    IedServer_setLocalIpAddress = _libs["libiec61850.so"].get("IedServer_setLocalIpAddress", "cdecl")
    IedServer_setLocalIpAddress.argtypes = [IedServer, String]
    IedServer_setLocalIpAddress.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 528
if _libs["libiec61850.so"].has("IedServer_setServerIdentity", "cdecl"):
    IedServer_setServerIdentity = _libs["libiec61850.so"].get("IedServer_setServerIdentity", "cdecl")
    IedServer_setServerIdentity.argtypes = [IedServer, String, String, String]
    IedServer_setServerIdentity.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 541
if _libs["libiec61850.so"].has("IedServer_setFilestoreBasepath", "cdecl"):
    IedServer_setFilestoreBasepath = _libs["libiec61850.so"].get("IedServer_setFilestoreBasepath", "cdecl")
    IedServer_setFilestoreBasepath.argtypes = [IedServer, String]
    IedServer_setFilestoreBasepath.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 553
if _libs["libiec61850.so"].has("IedServer_setLogStorage", "cdecl"):
    IedServer_setLogStorage = _libs["libiec61850.so"].get("IedServer_setLogStorage", "cdecl")
    IedServer_setLogStorage.argtypes = [IedServer, String, LogStorage]
    IedServer_setLogStorage.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 562
if _libs["libiec61850.so"].has("IedServer_start", "cdecl"):
    IedServer_start = _libs["libiec61850.so"].get("IedServer_start", "cdecl")
    IedServer_start.argtypes = [IedServer, c_int]
    IedServer_start.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 570
if _libs["libiec61850.so"].has("IedServer_stop", "cdecl"):
    IedServer_stop = _libs["libiec61850.so"].get("IedServer_stop", "cdecl")
    IedServer_stop.argtypes = [IedServer]
    IedServer_stop.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 583
if _libs["libiec61850.so"].has("IedServer_startThreadless", "cdecl"):
    IedServer_startThreadless = _libs["libiec61850.so"].get("IedServer_startThreadless", "cdecl")
    IedServer_startThreadless.argtypes = [IedServer, c_int]
    IedServer_startThreadless.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 599
if _libs["libiec61850.so"].has("IedServer_waitReady", "cdecl"):
    IedServer_waitReady = _libs["libiec61850.so"].get("IedServer_waitReady", "cdecl")
    IedServer_waitReady.argtypes = [IedServer, c_uint]
    IedServer_waitReady.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 611
if _libs["libiec61850.so"].has("IedServer_processIncomingData", "cdecl"):
    IedServer_processIncomingData = _libs["libiec61850.so"].get("IedServer_processIncomingData", "cdecl")
    IedServer_processIncomingData.argtypes = [IedServer]
    IedServer_processIncomingData.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 622
if _libs["libiec61850.so"].has("IedServer_performPeriodicTasks", "cdecl"):
    IedServer_performPeriodicTasks = _libs["libiec61850.so"].get("IedServer_performPeriodicTasks", "cdecl")
    IedServer_performPeriodicTasks.argtypes = [IedServer]
    IedServer_performPeriodicTasks.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 630
if _libs["libiec61850.so"].has("IedServer_stopThreadless", "cdecl"):
    IedServer_stopThreadless = _libs["libiec61850.so"].get("IedServer_stopThreadless", "cdecl")
    IedServer_stopThreadless.argtypes = [IedServer]
    IedServer_stopThreadless.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 639
if _libs["libiec61850.so"].has("IedServer_getDataModel", "cdecl"):
    IedServer_getDataModel = _libs["libiec61850.so"].get("IedServer_getDataModel", "cdecl")
    IedServer_getDataModel.argtypes = [IedServer]
    IedServer_getDataModel.restype = POINTER(IedModel)

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 650
if _libs["libiec61850.so"].has("IedServer_isRunning", "cdecl"):
    IedServer_isRunning = _libs["libiec61850.so"].get("IedServer_isRunning", "cdecl")
    IedServer_isRunning.argtypes = [IedServer]
    IedServer_isRunning.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 660
if _libs["libiec61850.so"].has("IedServer_getNumberOfOpenConnections", "cdecl"):
    IedServer_getNumberOfOpenConnections = _libs["libiec61850.so"].get("IedServer_getNumberOfOpenConnections", "cdecl")
    IedServer_getNumberOfOpenConnections.argtypes = [IedServer]
    IedServer_getNumberOfOpenConnections.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 673
if _libs["libiec61850.so"].has("IedServer_getMmsServer", "cdecl"):
    IedServer_getMmsServer = _libs["libiec61850.so"].get("IedServer_getMmsServer", "cdecl")
    IedServer_getMmsServer.argtypes = [IedServer]
    IedServer_getMmsServer.restype = MmsServer

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 688
if _libs["libiec61850.so"].has("IedServer_enableGoosePublishing", "cdecl"):
    IedServer_enableGoosePublishing = _libs["libiec61850.so"].get("IedServer_enableGoosePublishing", "cdecl")
    IedServer_enableGoosePublishing.argtypes = [IedServer]
    IedServer_enableGoosePublishing.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 701
if _libs["libiec61850.so"].has("IedServer_disableGoosePublishing", "cdecl"):
    IedServer_disableGoosePublishing = _libs["libiec61850.so"].get("IedServer_disableGoosePublishing", "cdecl")
    IedServer_disableGoosePublishing.argtypes = [IedServer]
    IedServer_disableGoosePublishing.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 717
if _libs["libiec61850.so"].has("IedServer_setGooseInterfaceId", "cdecl"):
    IedServer_setGooseInterfaceId = _libs["libiec61850.so"].get("IedServer_setGooseInterfaceId", "cdecl")
    IedServer_setGooseInterfaceId.argtypes = [IedServer, String]
    IedServer_setGooseInterfaceId.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 733
if _libs["libiec61850.so"].has("IedServer_setGooseInterfaceIdEx", "cdecl"):
    IedServer_setGooseInterfaceIdEx = _libs["libiec61850.so"].get("IedServer_setGooseInterfaceIdEx", "cdecl")
    IedServer_setGooseInterfaceIdEx.argtypes = [IedServer, POINTER(LogicalNode), String, String]
    IedServer_setGooseInterfaceIdEx.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 749
if _libs["libiec61850.so"].has("IedServer_useGooseVlanTag", "cdecl"):
    IedServer_useGooseVlanTag = _libs["libiec61850.so"].get("IedServer_useGooseVlanTag", "cdecl")
    IedServer_useGooseVlanTag.argtypes = [IedServer, POINTER(LogicalNode), String, c_bool]
    IedServer_useGooseVlanTag.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 764
if _libs["libiec61850.so"].has("IedServer_setTimeQuality", "cdecl"):
    IedServer_setTimeQuality = _libs["libiec61850.so"].get("IedServer_setTimeQuality", "cdecl")
    IedServer_setTimeQuality.argtypes = [IedServer, c_bool, c_bool, c_bool, c_int]
    IedServer_setTimeQuality.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 789
if _libs["libiec61850.so"].has("IedServer_setAuthenticator", "cdecl"):
    IedServer_setAuthenticator = _libs["libiec61850.so"].get("IedServer_setAuthenticator", "cdecl")
    IedServer_setAuthenticator.argtypes = [IedServer, AcseAuthenticator, POINTER(None)]
    IedServer_setAuthenticator.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 800
if _libs["libiec61850.so"].has("ClientConnection_getPeerAddress", "cdecl"):
    ClientConnection_getPeerAddress = _libs["libiec61850.so"].get("ClientConnection_getPeerAddress", "cdecl")
    ClientConnection_getPeerAddress.argtypes = [ClientConnection]
    ClientConnection_getPeerAddress.restype = c_char_p

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 812
if _libs["libiec61850.so"].has("ClientConnection_getLocalAddress", "cdecl"):
    ClientConnection_getLocalAddress = _libs["libiec61850.so"].get("ClientConnection_getLocalAddress", "cdecl")
    ClientConnection_getLocalAddress.argtypes = [ClientConnection]
    ClientConnection_getLocalAddress.restype = c_char_p

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 825
if _libs["libiec61850.so"].has("ClientConnection_getSecurityToken", "cdecl"):
    ClientConnection_getSecurityToken = _libs["libiec61850.so"].get("ClientConnection_getSecurityToken", "cdecl")
    ClientConnection_getSecurityToken.argtypes = [ClientConnection]
    ClientConnection_getSecurityToken.restype = POINTER(c_ubyte)
    ClientConnection_getSecurityToken.errcheck = lambda v,*a : cast(v, c_void_p)

IedConnectionIndicationHandler = CFUNCTYPE(UNCHECKED(None), IedServer, ClientConnection, c_bool, POINTER(None))# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 837

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 847
if _libs["libiec61850.so"].has("IedServer_setConnectionIndicationHandler", "cdecl"):
    IedServer_setConnectionIndicationHandler = _libs["libiec61850.so"].get("IedServer_setConnectionIndicationHandler", "cdecl")
    IedServer_setConnectionIndicationHandler.argtypes = [IedServer, IedConnectionIndicationHandler, POINTER(None)]
    IedServer_setConnectionIndicationHandler.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 858
if _libs["libiec61850.so"].has("IedServer_ignoreClientRequests", "cdecl"):
    IedServer_ignoreClientRequests = _libs["libiec61850.so"].get("IedServer_ignoreClientRequests", "cdecl")
    IedServer_ignoreClientRequests.argtypes = [IedServer, c_bool]
    IedServer_ignoreClientRequests.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 884
if _libs["libiec61850.so"].has("IedServer_lockDataModel", "cdecl"):
    IedServer_lockDataModel = _libs["libiec61850.so"].get("IedServer_lockDataModel", "cdecl")
    IedServer_lockDataModel.argtypes = [IedServer]
    IedServer_lockDataModel.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 895
if _libs["libiec61850.so"].has("IedServer_unlockDataModel", "cdecl"):
    IedServer_unlockDataModel = _libs["libiec61850.so"].get("IedServer_unlockDataModel", "cdecl")
    IedServer_unlockDataModel.argtypes = [IedServer]
    IedServer_unlockDataModel.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 909
if _libs["libiec61850.so"].has("IedServer_getAttributeValue", "cdecl"):
    IedServer_getAttributeValue = _libs["libiec61850.so"].get("IedServer_getAttributeValue", "cdecl")
    IedServer_getAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getAttributeValue.restype = POINTER(MmsValue)

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 924
if _libs["libiec61850.so"].has("IedServer_getBooleanAttributeValue", "cdecl"):
    IedServer_getBooleanAttributeValue = _libs["libiec61850.so"].get("IedServer_getBooleanAttributeValue", "cdecl")
    IedServer_getBooleanAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getBooleanAttributeValue.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 938
if _libs["libiec61850.so"].has("IedServer_getInt32AttributeValue", "cdecl"):
    IedServer_getInt32AttributeValue = _libs["libiec61850.so"].get("IedServer_getInt32AttributeValue", "cdecl")
    IedServer_getInt32AttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getInt32AttributeValue.restype = c_int32

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 952
if _libs["libiec61850.so"].has("IedServer_getInt64AttributeValue", "cdecl"):
    IedServer_getInt64AttributeValue = _libs["libiec61850.so"].get("IedServer_getInt64AttributeValue", "cdecl")
    IedServer_getInt64AttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getInt64AttributeValue.restype = c_int64

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 966
if _libs["libiec61850.so"].has("IedServer_getUInt32AttributeValue", "cdecl"):
    IedServer_getUInt32AttributeValue = _libs["libiec61850.so"].get("IedServer_getUInt32AttributeValue", "cdecl")
    IedServer_getUInt32AttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getUInt32AttributeValue.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 980
if _libs["libiec61850.so"].has("IedServer_getFloatAttributeValue", "cdecl"):
    IedServer_getFloatAttributeValue = _libs["libiec61850.so"].get("IedServer_getFloatAttributeValue", "cdecl")
    IedServer_getFloatAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getFloatAttributeValue.restype = c_float

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 994
if _libs["libiec61850.so"].has("IedServer_getUTCTimeAttributeValue", "cdecl"):
    IedServer_getUTCTimeAttributeValue = _libs["libiec61850.so"].get("IedServer_getUTCTimeAttributeValue", "cdecl")
    IedServer_getUTCTimeAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getUTCTimeAttributeValue.restype = uint64_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1012
if _libs["libiec61850.so"].has("IedServer_getBitStringAttributeValue", "cdecl"):
    IedServer_getBitStringAttributeValue = _libs["libiec61850.so"].get("IedServer_getBitStringAttributeValue", "cdecl")
    IedServer_getBitStringAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getBitStringAttributeValue.restype = uint32_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1025
if _libs["libiec61850.so"].has("IedServer_getStringAttributeValue", "cdecl"):
    IedServer_getStringAttributeValue = _libs["libiec61850.so"].get("IedServer_getStringAttributeValue", "cdecl")
    IedServer_getStringAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getStringAttributeValue.restype = c_char_p

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1043
if _libs["libiec61850.so"].has("IedServer_getFunctionalConstrainedData", "cdecl"):
    IedServer_getFunctionalConstrainedData = _libs["libiec61850.so"].get("IedServer_getFunctionalConstrainedData", "cdecl")
    IedServer_getFunctionalConstrainedData.argtypes = [IedServer, POINTER(DataObject), FunctionalConstraint]
    IedServer_getFunctionalConstrainedData.restype = POINTER(MmsValue)

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1063
if _libs["libiec61850.so"].has("IedServer_updateAttributeValue", "cdecl"):
    IedServer_updateAttributeValue = _libs["libiec61850.so"].get("IedServer_updateAttributeValue", "cdecl")
    IedServer_updateAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), POINTER(MmsValue)]
    IedServer_updateAttributeValue.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1078
if _libs["libiec61850.so"].has("IedServer_updateFloatAttributeValue", "cdecl"):
    IedServer_updateFloatAttributeValue = _libs["libiec61850.so"].get("IedServer_updateFloatAttributeValue", "cdecl")
    IedServer_updateFloatAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), c_float]
    IedServer_updateFloatAttributeValue.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1093
if _libs["libiec61850.so"].has("IedServer_updateInt32AttributeValue", "cdecl"):
    IedServer_updateInt32AttributeValue = _libs["libiec61850.so"].get("IedServer_updateInt32AttributeValue", "cdecl")
    IedServer_updateInt32AttributeValue.argtypes = [IedServer, POINTER(DataAttribute), c_int32]
    IedServer_updateInt32AttributeValue.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1108
if _libs["libiec61850.so"].has("IedServer_updateDbposValue", "cdecl"):
    IedServer_updateDbposValue = _libs["libiec61850.so"].get("IedServer_updateDbposValue", "cdecl")
    IedServer_updateDbposValue.argtypes = [IedServer, POINTER(DataAttribute), Dbpos]
    IedServer_updateDbposValue.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1123
if _libs["libiec61850.so"].has("IedServer_updateInt64AttributeValue", "cdecl"):
    IedServer_updateInt64AttributeValue = _libs["libiec61850.so"].get("IedServer_updateInt64AttributeValue", "cdecl")
    IedServer_updateInt64AttributeValue.argtypes = [IedServer, POINTER(DataAttribute), c_int64]
    IedServer_updateInt64AttributeValue.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1138
if _libs["libiec61850.so"].has("IedServer_updateUnsignedAttributeValue", "cdecl"):
    IedServer_updateUnsignedAttributeValue = _libs["libiec61850.so"].get("IedServer_updateUnsignedAttributeValue", "cdecl")
    IedServer_updateUnsignedAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), uint32_t]
    IedServer_updateUnsignedAttributeValue.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1153
if _libs["libiec61850.so"].has("IedServer_updateBitStringAttributeValue", "cdecl"):
    IedServer_updateBitStringAttributeValue = _libs["libiec61850.so"].get("IedServer_updateBitStringAttributeValue", "cdecl")
    IedServer_updateBitStringAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), uint32_t]
    IedServer_updateBitStringAttributeValue.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1168
if _libs["libiec61850.so"].has("IedServer_updateBooleanAttributeValue", "cdecl"):
    IedServer_updateBooleanAttributeValue = _libs["libiec61850.so"].get("IedServer_updateBooleanAttributeValue", "cdecl")
    IedServer_updateBooleanAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), c_bool]
    IedServer_updateBooleanAttributeValue.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1183
if _libs["libiec61850.so"].has("IedServer_updateVisibleStringAttributeValue", "cdecl"):
    IedServer_updateVisibleStringAttributeValue = _libs["libiec61850.so"].get("IedServer_updateVisibleStringAttributeValue", "cdecl")
    IedServer_updateVisibleStringAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), String]
    IedServer_updateVisibleStringAttributeValue.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1198
if _libs["libiec61850.so"].has("IedServer_updateUTCTimeAttributeValue", "cdecl"):
    IedServer_updateUTCTimeAttributeValue = _libs["libiec61850.so"].get("IedServer_updateUTCTimeAttributeValue", "cdecl")
    IedServer_updateUTCTimeAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), uint64_t]
    IedServer_updateUTCTimeAttributeValue.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1213
if _libs["libiec61850.so"].has("IedServer_updateTimestampAttributeValue", "cdecl"):
    IedServer_updateTimestampAttributeValue = _libs["libiec61850.so"].get("IedServer_updateTimestampAttributeValue", "cdecl")
    IedServer_updateTimestampAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), POINTER(Timestamp)]
    IedServer_updateTimestampAttributeValue.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1230
if _libs["libiec61850.so"].has("IedServer_updateQuality", "cdecl"):
    IedServer_updateQuality = _libs["libiec61850.so"].get("IedServer_updateQuality", "cdecl")
    IedServer_updateQuality.argtypes = [IedServer, POINTER(DataAttribute), Quality]
    IedServer_updateQuality.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1253
if _libs["libiec61850.so"].has("IedServer_changeActiveSettingGroup", "cdecl"):
    IedServer_changeActiveSettingGroup = _libs["libiec61850.so"].get("IedServer_changeActiveSettingGroup", "cdecl")
    IedServer_changeActiveSettingGroup.argtypes = [IedServer, POINTER(SettingGroupControlBlock), uint8_t]
    IedServer_changeActiveSettingGroup.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1264
if _libs["libiec61850.so"].has("IedServer_getActiveSettingGroup", "cdecl"):
    IedServer_getActiveSettingGroup = _libs["libiec61850.so"].get("IedServer_getActiveSettingGroup", "cdecl")
    IedServer_getActiveSettingGroup.argtypes = [IedServer, POINTER(SettingGroupControlBlock)]
    IedServer_getActiveSettingGroup.restype = uint8_t

ActiveSettingGroupChangedHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), POINTER(SettingGroupControlBlock), uint8_t, ClientConnection)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1281

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1293
if _libs["libiec61850.so"].has("IedServer_setActiveSettingGroupChangedHandler", "cdecl"):
    IedServer_setActiveSettingGroupChangedHandler = _libs["libiec61850.so"].get("IedServer_setActiveSettingGroupChangedHandler", "cdecl")
    IedServer_setActiveSettingGroupChangedHandler.argtypes = [IedServer, POINTER(SettingGroupControlBlock), ActiveSettingGroupChangedHandler, POINTER(None)]
    IedServer_setActiveSettingGroupChangedHandler.restype = None

EditSettingGroupChangedHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), POINTER(SettingGroupControlBlock), uint8_t, ClientConnection)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1313

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1325
if _libs["libiec61850.so"].has("IedServer_setEditSettingGroupChangedHandler", "cdecl"):
    IedServer_setEditSettingGroupChangedHandler = _libs["libiec61850.so"].get("IedServer_setEditSettingGroupChangedHandler", "cdecl")
    IedServer_setEditSettingGroupChangedHandler.argtypes = [IedServer, POINTER(SettingGroupControlBlock), EditSettingGroupChangedHandler, POINTER(None)]
    IedServer_setEditSettingGroupChangedHandler.restype = None

EditSettingGroupConfirmationHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(SettingGroupControlBlock), uint8_t)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1337

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1349
if _libs["libiec61850.so"].has("IedServer_setEditSettingGroupConfirmationHandler", "cdecl"):
    IedServer_setEditSettingGroupConfirmationHandler = _libs["libiec61850.so"].get("IedServer_setEditSettingGroupConfirmationHandler", "cdecl")
    IedServer_setEditSettingGroupConfirmationHandler.argtypes = [IedServer, POINTER(SettingGroupControlBlock), EditSettingGroupConfirmationHandler, POINTER(None)]
    IedServer_setEditSettingGroupConfirmationHandler.restype = None

enum_anon_54 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1373

CONTROL_ACCEPTED = (-1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1373

CONTROL_WAITING_FOR_SELECT = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1373

CONTROL_HARDWARE_FAULT = 1# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1373

CONTROL_TEMPORARILY_UNAVAILABLE = 2# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1373

CONTROL_OBJECT_ACCESS_DENIED = 3# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1373

CONTROL_OBJECT_UNDEFINED = 4# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1373

CONTROL_VALUE_INVALID = 11# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1373

CheckHandlerResult = enum_anon_54# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1373

enum_anon_55 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1382

CONTROL_RESULT_FAILED = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1382

CONTROL_RESULT_OK = 1# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1382

CONTROL_RESULT_WAITING = 2# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1382

ControlHandlerResult = enum_anon_55# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1382

ControlAction = POINTER(None)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1384

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1393
if _libs["libiec61850.so"].has("ControlAction_setError", "cdecl"):
    ControlAction_setError = _libs["libiec61850.so"].get("ControlAction_setError", "cdecl")
    ControlAction_setError.argtypes = [ControlAction, ControlLastApplError]
    ControlAction_setError.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1402
if _libs["libiec61850.so"].has("ControlAction_setAddCause", "cdecl"):
    ControlAction_setAddCause = _libs["libiec61850.so"].get("ControlAction_setAddCause", "cdecl")
    ControlAction_setAddCause.argtypes = [ControlAction, ControlAddCause]
    ControlAction_setAddCause.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1412
if _libs["libiec61850.so"].has("ControlAction_getOrCat", "cdecl"):
    ControlAction_getOrCat = _libs["libiec61850.so"].get("ControlAction_getOrCat", "cdecl")
    ControlAction_getOrCat.argtypes = [ControlAction]
    ControlAction_getOrCat.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1421
if _libs["libiec61850.so"].has("ControlAction_getOrIdent", "cdecl"):
    ControlAction_getOrIdent = _libs["libiec61850.so"].get("ControlAction_getOrIdent", "cdecl")
    ControlAction_getOrIdent.argtypes = [ControlAction, POINTER(c_int)]
    ControlAction_getOrIdent.restype = POINTER(uint8_t)

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1432
if _libs["libiec61850.so"].has("ControlAction_getCtlNum", "cdecl"):
    ControlAction_getCtlNum = _libs["libiec61850.so"].get("ControlAction_getCtlNum", "cdecl")
    ControlAction_getCtlNum.argtypes = [ControlAction]
    ControlAction_getCtlNum.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1442
if _libs["libiec61850.so"].has("ControlAction_getSynchroCheck", "cdecl"):
    ControlAction_getSynchroCheck = _libs["libiec61850.so"].get("ControlAction_getSynchroCheck", "cdecl")
    ControlAction_getSynchroCheck.argtypes = [ControlAction]
    ControlAction_getSynchroCheck.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1452
if _libs["libiec61850.so"].has("ControlAction_getInterlockCheck", "cdecl"):
    ControlAction_getInterlockCheck = _libs["libiec61850.so"].get("ControlAction_getInterlockCheck", "cdecl")
    ControlAction_getInterlockCheck.argtypes = [ControlAction]
    ControlAction_getInterlockCheck.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1462
if _libs["libiec61850.so"].has("ControlAction_isSelect", "cdecl"):
    ControlAction_isSelect = _libs["libiec61850.so"].get("ControlAction_isSelect", "cdecl")
    ControlAction_isSelect.argtypes = [ControlAction]
    ControlAction_isSelect.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1472
if _libs["libiec61850.so"].has("ControlAction_getClientConnection", "cdecl"):
    ControlAction_getClientConnection = _libs["libiec61850.so"].get("ControlAction_getClientConnection", "cdecl")
    ControlAction_getClientConnection.argtypes = [ControlAction]
    ControlAction_getClientConnection.restype = ClientConnection

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1481
if _libs["libiec61850.so"].has("ControlAction_getControlObject", "cdecl"):
    ControlAction_getControlObject = _libs["libiec61850.so"].get("ControlAction_getControlObject", "cdecl")
    ControlAction_getControlObject.argtypes = [ControlAction]
    ControlAction_getControlObject.restype = POINTER(DataObject)

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1492
if _libs["libiec61850.so"].has("ControlAction_getControlTime", "cdecl"):
    ControlAction_getControlTime = _libs["libiec61850.so"].get("ControlAction_getControlTime", "cdecl")
    ControlAction_getControlTime.argtypes = [ControlAction]
    ControlAction_getControlTime.restype = uint64_t

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1501
if _libs["libiec61850.so"].has("ControlAction_getT", "cdecl"):
    ControlAction_getT = _libs["libiec61850.so"].get("ControlAction_getT", "cdecl")
    ControlAction_getT.argtypes = [ControlAction]
    ControlAction_getT.restype = POINTER(Timestamp)

ControlPerformCheckHandler = CFUNCTYPE(UNCHECKED(CheckHandlerResult), ControlAction, POINTER(None), POINTER(MmsValue), c_bool, c_bool)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1524

ControlWaitForExecutionHandler = CFUNCTYPE(UNCHECKED(ControlHandlerResult), ControlAction, POINTER(None), POINTER(MmsValue), c_bool, c_bool)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1549

ControlHandler = CFUNCTYPE(UNCHECKED(ControlHandlerResult), ControlAction, POINTER(None), POINTER(MmsValue), c_bool)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1572

enum_anon_56 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1584

SELECT_STATE_REASON_SELECTED = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1584

SELECT_STATE_REASON_CANCELED = (SELECT_STATE_REASON_SELECTED + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1584

SELECT_STATE_REASON_TIMEOUT = (SELECT_STATE_REASON_CANCELED + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1584

SELECT_STATE_REASON_OPERATED = (SELECT_STATE_REASON_TIMEOUT + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1584

SELECT_STATE_REASON_OPERATE_FAILED = (SELECT_STATE_REASON_OPERATED + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1584

SELECT_STATE_REASON_DISCONNECTED = (SELECT_STATE_REASON_OPERATE_FAILED + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1584

SelectStateChangedReason = enum_anon_56# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1584

ControlSelectStateChangedHandler = CFUNCTYPE(UNCHECKED(None), ControlAction, POINTER(None), c_bool, SelectStateChangedReason)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1596

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1612
if _libs["libiec61850.so"].has("IedServer_setControlHandler", "cdecl"):
    IedServer_setControlHandler = _libs["libiec61850.so"].get("IedServer_setControlHandler", "cdecl")
    IedServer_setControlHandler.argtypes = [IedServer, POINTER(DataObject), ControlHandler, POINTER(None)]
    IedServer_setControlHandler.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1629
if _libs["libiec61850.so"].has("IedServer_setPerformCheckHandler", "cdecl"):
    IedServer_setPerformCheckHandler = _libs["libiec61850.so"].get("IedServer_setPerformCheckHandler", "cdecl")
    IedServer_setPerformCheckHandler.argtypes = [IedServer, POINTER(DataObject), ControlPerformCheckHandler, POINTER(None)]
    IedServer_setPerformCheckHandler.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1646
if _libs["libiec61850.so"].has("IedServer_setWaitForExecutionHandler", "cdecl"):
    IedServer_setWaitForExecutionHandler = _libs["libiec61850.so"].get("IedServer_setWaitForExecutionHandler", "cdecl")
    IedServer_setWaitForExecutionHandler.argtypes = [IedServer, POINTER(DataObject), ControlWaitForExecutionHandler, POINTER(None)]
    IedServer_setWaitForExecutionHandler.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1665
if _libs["libiec61850.so"].has("IedServer_setSelectStateChangedHandler", "cdecl"):
    IedServer_setSelectStateChangedHandler = _libs["libiec61850.so"].get("IedServer_setSelectStateChangedHandler", "cdecl")
    IedServer_setSelectStateChangedHandler.argtypes = [IedServer, POINTER(DataObject), ControlSelectStateChangedHandler, POINTER(None)]
    IedServer_setSelectStateChangedHandler.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1678
if _libs["libiec61850.so"].has("IedServer_updateCtlModel", "cdecl"):
    IedServer_updateCtlModel = _libs["libiec61850.so"].get("IedServer_updateCtlModel", "cdecl")
    IedServer_updateCtlModel.argtypes = [IedServer, POINTER(DataObject), ControlModel]
    IedServer_updateCtlModel.restype = None

enum_anon_57 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1701

RCB_EVENT_GET_PARAMETER = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1701

RCB_EVENT_SET_PARAMETER = (RCB_EVENT_GET_PARAMETER + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1701

RCB_EVENT_UNRESERVED = (RCB_EVENT_SET_PARAMETER + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1701

RCB_EVENT_RESERVED = (RCB_EVENT_UNRESERVED + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1701

RCB_EVENT_ENABLE = (RCB_EVENT_RESERVED + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1701

RCB_EVENT_DISABLE = (RCB_EVENT_ENABLE + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1701

RCB_EVENT_GI = (RCB_EVENT_DISABLE + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1701

RCB_EVENT_PURGEBUF = (RCB_EVENT_GI + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1701

RCB_EVENT_OVERFLOW = (RCB_EVENT_PURGEBUF + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1701

RCB_EVENT_REPORT_CREATED = (RCB_EVENT_OVERFLOW + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1701

IedServer_RCBEventType = enum_anon_57# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1701

IedServer_RCBEventHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(ReportControlBlock), ClientConnection, IedServer_RCBEventType, String, MmsDataAccessError)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1713

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1723
if _libs["libiec61850.so"].has("IedServer_setRCBEventHandler", "cdecl"):
    IedServer_setRCBEventHandler = _libs["libiec61850.so"].get("IedServer_setRCBEventHandler", "cdecl")
    IedServer_setRCBEventHandler.argtypes = [IedServer, IedServer_RCBEventHandler, POINTER(None)]
    IedServer_setRCBEventHandler.restype = None

SVCBEventHandler = CFUNCTYPE(UNCHECKED(None), POINTER(SVControlBlock), c_int, POINTER(None))# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1748

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1759
if _libs["libiec61850.so"].has("IedServer_setSVCBHandler", "cdecl"):
    IedServer_setSVCBHandler = _libs["libiec61850.so"].get("IedServer_setSVCBHandler", "cdecl")
    IedServer_setSVCBHandler.argtypes = [IedServer, POINTER(SVControlBlock), SVCBEventHandler, POINTER(None)]
    IedServer_setSVCBHandler.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1771
class struct_sMmsGooseControlBlock(Structure):
    pass

MmsGooseControlBlock = POINTER(struct_sMmsGooseControlBlock)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1771

GoCBEventHandler = CFUNCTYPE(UNCHECKED(None), MmsGooseControlBlock, c_int, POINTER(None))# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1779

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1792
if _libs["libiec61850.so"].has("IedServer_setGoCBHandler", "cdecl"):
    IedServer_setGoCBHandler = _libs["libiec61850.so"].get("IedServer_setGoCBHandler", "cdecl")
    IedServer_setGoCBHandler.argtypes = [IedServer, GoCBEventHandler, POINTER(None)]
    IedServer_setGoCBHandler.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1794
if _libs["libiec61850.so"].has("MmsGooseControlBlock_getName", "cdecl"):
    MmsGooseControlBlock_getName = _libs["libiec61850.so"].get("MmsGooseControlBlock_getName", "cdecl")
    MmsGooseControlBlock_getName.argtypes = [MmsGooseControlBlock]
    if sizeof(c_int) == sizeof(c_void_p):
        MmsGooseControlBlock_getName.restype = ReturnString
    else:
        MmsGooseControlBlock_getName.restype = String
        MmsGooseControlBlock_getName.errcheck = ReturnString

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1797
if _libs["libiec61850.so"].has("MmsGooseControlBlock_getLogicalNode", "cdecl"):
    MmsGooseControlBlock_getLogicalNode = _libs["libiec61850.so"].get("MmsGooseControlBlock_getLogicalNode", "cdecl")
    MmsGooseControlBlock_getLogicalNode.argtypes = [MmsGooseControlBlock]
    MmsGooseControlBlock_getLogicalNode.restype = POINTER(LogicalNode)

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1800
if _libs["libiec61850.so"].has("MmsGooseControlBlock_getDataSet", "cdecl"):
    MmsGooseControlBlock_getDataSet = _libs["libiec61850.so"].get("MmsGooseControlBlock_getDataSet", "cdecl")
    MmsGooseControlBlock_getDataSet.argtypes = [MmsGooseControlBlock]
    MmsGooseControlBlock_getDataSet.restype = POINTER(DataSet)

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1804
if _libs["libiec61850.so"].has("MmsGooseControlBlock_getGoEna", "cdecl"):
    MmsGooseControlBlock_getGoEna = _libs["libiec61850.so"].get("MmsGooseControlBlock_getGoEna", "cdecl")
    MmsGooseControlBlock_getGoEna.argtypes = [MmsGooseControlBlock]
    MmsGooseControlBlock_getGoEna.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1807
if _libs["libiec61850.so"].has("MmsGooseControlBlock_getMinTime", "cdecl"):
    MmsGooseControlBlock_getMinTime = _libs["libiec61850.so"].get("MmsGooseControlBlock_getMinTime", "cdecl")
    MmsGooseControlBlock_getMinTime.argtypes = [MmsGooseControlBlock]
    MmsGooseControlBlock_getMinTime.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1810
if _libs["libiec61850.so"].has("MmsGooseControlBlock_getMaxTime", "cdecl"):
    MmsGooseControlBlock_getMaxTime = _libs["libiec61850.so"].get("MmsGooseControlBlock_getMaxTime", "cdecl")
    MmsGooseControlBlock_getMaxTime.argtypes = [MmsGooseControlBlock]
    MmsGooseControlBlock_getMaxTime.restype = c_int

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1813
if _libs["libiec61850.so"].has("MmsGooseControlBlock_getFixedOffs", "cdecl"):
    MmsGooseControlBlock_getFixedOffs = _libs["libiec61850.so"].get("MmsGooseControlBlock_getFixedOffs", "cdecl")
    MmsGooseControlBlock_getFixedOffs.argtypes = [MmsGooseControlBlock]
    MmsGooseControlBlock_getFixedOffs.restype = c_bool

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1816
if _libs["libiec61850.so"].has("MmsGooseControlBlock_getNdsCom", "cdecl"):
    MmsGooseControlBlock_getNdsCom = _libs["libiec61850.so"].get("MmsGooseControlBlock_getNdsCom", "cdecl")
    MmsGooseControlBlock_getNdsCom.argtypes = [MmsGooseControlBlock]
    MmsGooseControlBlock_getNdsCom.restype = c_bool

WriteAccessHandler = CFUNCTYPE(UNCHECKED(MmsDataAccessError), POINTER(DataAttribute), POINTER(MmsValue), ClientConnection, POINTER(None))# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1859

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1881
if _libs["libiec61850.so"].has("IedServer_handleWriteAccess", "cdecl"):
    IedServer_handleWriteAccess = _libs["libiec61850.so"].get("IedServer_handleWriteAccess", "cdecl")
    IedServer_handleWriteAccess.argtypes = [IedServer, POINTER(DataAttribute), WriteAccessHandler, POINTER(None)]
    IedServer_handleWriteAccess.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1904
if _libs["libiec61850.so"].has("IedServer_handleWriteAccessForComplexAttribute", "cdecl"):
    IedServer_handleWriteAccessForComplexAttribute = _libs["libiec61850.so"].get("IedServer_handleWriteAccessForComplexAttribute", "cdecl")
    IedServer_handleWriteAccessForComplexAttribute.argtypes = [IedServer, POINTER(DataAttribute), WriteAccessHandler, POINTER(None)]
    IedServer_handleWriteAccessForComplexAttribute.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1918
if _libs["libiec61850.so"].has("IedServer_handleWriteAccessForDataObject", "cdecl"):
    IedServer_handleWriteAccessForDataObject = _libs["libiec61850.so"].get("IedServer_handleWriteAccessForDataObject", "cdecl")
    IedServer_handleWriteAccessForDataObject.argtypes = [IedServer, POINTER(DataObject), FunctionalConstraint, WriteAccessHandler, POINTER(None)]
    IedServer_handleWriteAccessForDataObject.restype = None

enum_anon_58 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1923

ACCESS_POLICY_ALLOW = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1923

ACCESS_POLICY_DENY = (ACCESS_POLICY_ALLOW + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1923

AccessPolicy = enum_anon_58# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1923

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1934
if _libs["libiec61850.so"].has("IedServer_setWriteAccessPolicy", "cdecl"):
    IedServer_setWriteAccessPolicy = _libs["libiec61850.so"].get("IedServer_setWriteAccessPolicy", "cdecl")
    IedServer_setWriteAccessPolicy.argtypes = [IedServer, FunctionalConstraint, AccessPolicy]
    IedServer_setWriteAccessPolicy.restype = None

ReadAccessHandler = CFUNCTYPE(UNCHECKED(MmsDataAccessError), POINTER(LogicalDevice), POINTER(LogicalNode), POINTER(DataObject), FunctionalConstraint, ClientConnection, POINTER(None))# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1953

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1965
if _libs["libiec61850.so"].has("IedServer_setReadAccessHandler", "cdecl"):
    IedServer_setReadAccessHandler = _libs["libiec61850.so"].get("IedServer_setReadAccessHandler", "cdecl")
    IedServer_setReadAccessHandler.argtypes = [IedServer, ReadAccessHandler, POINTER(None)]
    IedServer_setReadAccessHandler.restype = None

enum_anon_59 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1973

DATASET_CREATE = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1973

DATASET_DELETE = (DATASET_CREATE + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1973

DATASET_READ = (DATASET_DELETE + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1973

DATASET_WRITE = (DATASET_READ + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1973

DATASET_GET_DIRECTORY = (DATASET_WRITE + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1973

IedServer_DataSetOperation = enum_anon_59# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1973

IedServer_DataSetAccessHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), ClientConnection, IedServer_DataSetOperation, String)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1987

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1996
if _libs["libiec61850.so"].has("IedServer_setDataSetAccessHandler", "cdecl"):
    IedServer_setDataSetAccessHandler = _libs["libiec61850.so"].get("IedServer_setDataSetAccessHandler", "cdecl")
    IedServer_setDataSetAccessHandler.argtypes = [IedServer, IedServer_DataSetAccessHandler, POINTER(None)]
    IedServer_setDataSetAccessHandler.restype = None

enum_anon_60 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 2003

DIRECTORY_CAT_LD_LIST = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 2003

DIRECTORY_CAT_DATA_LIST = (DIRECTORY_CAT_LD_LIST + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 2003

DIRECTORY_CAT_DATASET_LIST = (DIRECTORY_CAT_DATA_LIST + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 2003

DIRECTORY_CAT_LOG_LIST = (DIRECTORY_CAT_DATASET_LIST + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 2003

IedServer_DirectoryCategory = enum_anon_60# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 2003

IedServer_DirectoryAccessHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), ClientConnection, IedServer_DirectoryCategory, POINTER(LogicalDevice))# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 2006

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 2009
if _libs["libiec61850.so"].has("IedServer_setDirectoryAccessHandler", "cdecl"):
    IedServer_setDirectoryAccessHandler = _libs["libiec61850.so"].get("IedServer_setDirectoryAccessHandler", "cdecl")
    IedServer_setDirectoryAccessHandler.argtypes = [IedServer, IedServer_DirectoryAccessHandler, POINTER(None)]
    IedServer_setDirectoryAccessHandler.restype = None

IedServer_ListObjectsAccessHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), ClientConnection, ACSIClass, POINTER(LogicalDevice), POINTER(LogicalNode), String, String, FunctionalConstraint)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 2028

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 2037
if _libs["libiec61850.so"].has("IedServer_setListObjectsAccessHandler", "cdecl"):
    IedServer_setListObjectsAccessHandler = _libs["libiec61850.so"].get("IedServer_setListObjectsAccessHandler", "cdecl")
    IedServer_setListObjectsAccessHandler.argtypes = [IedServer, IedServer_ListObjectsAccessHandler, POINTER(None)]
    IedServer_setListObjectsAccessHandler.restype = None

enum_anon_61 = c_int# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 2042

IEC61850_CB_ACCESS_TYPE_READ = 0# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 2042

IEC61850_CB_ACCESS_TYPE_WRITE = (IEC61850_CB_ACCESS_TYPE_READ + 1)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 2042

IedServer_ControlBlockAccessType = enum_anon_61# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 2042

IedServer_ControlBlockAccessHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), ClientConnection, ACSIClass, POINTER(LogicalDevice), POINTER(LogicalNode), String, String, IedServer_ControlBlockAccessType)# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 2061

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 2070
if _libs["libiec61850.so"].has("IedServer_setControlBlockAccessHandler", "cdecl"):
    IedServer_setControlBlockAccessHandler = _libs["libiec61850.so"].get("IedServer_setControlBlockAccessHandler", "cdecl")
    IedServer_setControlBlockAccessHandler.argtypes = [IedServer, IedServer_ControlBlockAccessHandler, POINTER(None)]
    IedServer_setControlBlockAccessHandler.restype = None

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 2079
if _libs["libiec61850.so"].has("IedServer_ignoreReadAccess", "cdecl"):
    IedServer_ignoreReadAccess = _libs["libiec61850.so"].get("IedServer_ignoreReadAccess", "cdecl")
    IedServer_ignoreReadAccess.argtypes = [IedServer, c_bool]
    IedServer_ignoreReadAccess.restype = None

# /home/user/libiec61850/src/common/inc/string_utilities.h: 34
for _lib in _libs.values():
    if not _lib.has("StringUtils_copyString", "cdecl"):
        continue
    StringUtils_copyString = _lib.get("StringUtils_copyString", "cdecl")
    StringUtils_copyString.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        StringUtils_copyString.restype = ReturnString
    else:
        StringUtils_copyString.restype = String
        StringUtils_copyString.errcheck = ReturnString
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 37
for _lib in _libs.values():
    if not _lib.has("StringUtils_copyStringMax", "cdecl"):
        continue
    StringUtils_copyStringMax = _lib.get("StringUtils_copyStringMax", "cdecl")
    StringUtils_copyStringMax.argtypes = [String, c_int, String]
    if sizeof(c_int) == sizeof(c_void_p):
        StringUtils_copyStringMax.restype = ReturnString
    else:
        StringUtils_copyStringMax.restype = String
        StringUtils_copyStringMax.errcheck = ReturnString
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 40
for _lib in _libs.values():
    if not _lib.has("StringUtils_copyStringToBuffer", "cdecl"):
        continue
    StringUtils_copyStringToBuffer = _lib.get("StringUtils_copyStringToBuffer", "cdecl")
    StringUtils_copyStringToBuffer.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        StringUtils_copyStringToBuffer.restype = ReturnString
    else:
        StringUtils_copyStringToBuffer.restype = String
        StringUtils_copyStringToBuffer.errcheck = ReturnString
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 53
for _lib in _libs.values():
    if not _lib.has("StringUtils_copyStringToBufferAndReplace", "cdecl"):
        continue
    StringUtils_copyStringToBufferAndReplace = _lib.get("StringUtils_copyStringToBufferAndReplace", "cdecl")
    StringUtils_copyStringToBufferAndReplace.argtypes = [String, String, c_char, c_char]
    if sizeof(c_int) == sizeof(c_void_p):
        StringUtils_copyStringToBufferAndReplace.restype = ReturnString
    else:
        StringUtils_copyStringToBufferAndReplace.restype = String
        StringUtils_copyStringToBufferAndReplace.errcheck = ReturnString
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 56
for _lib in _libs.values():
    if not _lib.has("StringUtils_copySubString", "cdecl"):
        continue
    StringUtils_copySubString = _lib.get("StringUtils_copySubString", "cdecl")
    StringUtils_copySubString.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        StringUtils_copySubString.restype = ReturnString
    else:
        StringUtils_copySubString.restype = String
        StringUtils_copySubString.errcheck = ReturnString
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 63
for _lib in _libs.values():
    if _lib.has("StringUtils_createString", "cdecl"):
        _func = _lib.get("StringUtils_createString", "cdecl")
        _restype = String
        _errcheck = None
        _argtypes = [c_int]
        StringUtils_createString = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/user/libiec61850/src/common/inc/string_utilities.h: 70
for _lib in _libs.values():
    if _lib.has("StringUtils_createStringInBuffer", "cdecl"):
        _func = _lib.get("StringUtils_createStringInBuffer", "cdecl")
        _restype = String
        _errcheck = None
        _argtypes = [String, c_int, c_int]
        StringUtils_createStringInBuffer = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/user/libiec61850/src/common/inc/string_utilities.h: 73
for _lib in _libs.values():
    if not _lib.has("StringUtils_createStringFromBuffer", "cdecl"):
        continue
    StringUtils_createStringFromBuffer = _lib.get("StringUtils_createStringFromBuffer", "cdecl")
    StringUtils_createStringFromBuffer.argtypes = [POINTER(uint8_t), c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        StringUtils_createStringFromBuffer.restype = ReturnString
    else:
        StringUtils_createStringFromBuffer.restype = String
        StringUtils_createStringFromBuffer.errcheck = ReturnString
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 76
for _lib in _libs.values():
    if not _lib.has("StringUtils_createStringFromBufferInBuffer", "cdecl"):
        continue
    StringUtils_createStringFromBufferInBuffer = _lib.get("StringUtils_createStringFromBufferInBuffer", "cdecl")
    StringUtils_createStringFromBufferInBuffer.argtypes = [String, POINTER(uint8_t), c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        StringUtils_createStringFromBufferInBuffer.restype = ReturnString
    else:
        StringUtils_createStringFromBufferInBuffer.restype = String
        StringUtils_createStringFromBufferInBuffer.errcheck = ReturnString
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 79
for _lib in _libs.values():
    if not _lib.has("StringUtils_createStringFromBufferInBufferMax", "cdecl"):
        continue
    StringUtils_createStringFromBufferInBufferMax = _lib.get("StringUtils_createStringFromBufferInBufferMax", "cdecl")
    StringUtils_createStringFromBufferInBufferMax.argtypes = [String, POINTER(uint8_t), c_int, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        StringUtils_createStringFromBufferInBufferMax.restype = ReturnString
    else:
        StringUtils_createStringFromBufferInBufferMax.restype = String
        StringUtils_createStringFromBufferInBufferMax.errcheck = ReturnString
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 83
for _lib in _libs.values():
    if not _lib.has("StringUtils_replace", "cdecl"):
        continue
    StringUtils_replace = _lib.get("StringUtils_replace", "cdecl")
    StringUtils_replace.argtypes = [String, c_char, c_char]
    StringUtils_replace.restype = None
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 85
for _lib in _libs.values():
    if not _lib.has("StringUtils_concatString", "cdecl"):
        continue
    StringUtils_concatString = _lib.get("StringUtils_concatString", "cdecl")
    StringUtils_concatString.argtypes = [String, c_int, String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        StringUtils_concatString.restype = ReturnString
    else:
        StringUtils_concatString.restype = String
        StringUtils_concatString.errcheck = ReturnString
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 88
for _lib in _libs.values():
    if not _lib.has("StringUtils_appendString", "cdecl"):
        continue
    StringUtils_appendString = _lib.get("StringUtils_appendString", "cdecl")
    StringUtils_appendString.argtypes = [String, c_int, String]
    if sizeof(c_int) == sizeof(c_void_p):
        StringUtils_appendString.restype = ReturnString
    else:
        StringUtils_appendString.restype = String
        StringUtils_appendString.errcheck = ReturnString
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 92
for _lib in _libs.values():
    if not _lib.has("StringUtils_isDigit", "cdecl"):
        continue
    StringUtils_isDigit = _lib.get("StringUtils_isDigit", "cdecl")
    StringUtils_isDigit.argtypes = [c_char]
    StringUtils_isDigit.restype = c_bool
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 95
for _lib in _libs.values():
    if not _lib.has("StringUtils_digitToInt", "cdecl"):
        continue
    StringUtils_digitToInt = _lib.get("StringUtils_digitToInt", "cdecl")
    StringUtils_digitToInt.argtypes = [c_char]
    StringUtils_digitToInt.restype = c_int
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 98
for _lib in _libs.values():
    if not _lib.has("StringUtils_digitsToInt", "cdecl"):
        continue
    StringUtils_digitsToInt = _lib.get("StringUtils_digitsToInt", "cdecl")
    StringUtils_digitsToInt.argtypes = [String, c_int]
    StringUtils_digitsToInt.restype = c_int
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 101
for _lib in _libs.values():
    if not _lib.has("StringUtils_createBufferFromHexString", "cdecl"):
        continue
    StringUtils_createBufferFromHexString = _lib.get("StringUtils_createBufferFromHexString", "cdecl")
    StringUtils_createBufferFromHexString.argtypes = [String, POINTER(uint8_t)]
    StringUtils_createBufferFromHexString.restype = c_int
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 107
for _lib in _libs.values():
    if not _lib.has("StringUtils_startsWith", "cdecl"):
        continue
    StringUtils_startsWith = _lib.get("StringUtils_startsWith", "cdecl")
    StringUtils_startsWith.argtypes = [String, String]
    StringUtils_startsWith.restype = c_bool
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 110
for _lib in _libs.values():
    if not _lib.has("StringUtils_endsWith", "cdecl"):
        continue
    StringUtils_endsWith = _lib.get("StringUtils_endsWith", "cdecl")
    StringUtils_endsWith.argtypes = [String, String]
    StringUtils_endsWith.restype = c_bool
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 121
for _lib in _libs.values():
    if not _lib.has("StringUtils_compareChars", "cdecl"):
        continue
    StringUtils_compareChars = _lib.get("StringUtils_compareChars", "cdecl")
    StringUtils_compareChars.argtypes = [c_char, c_char]
    StringUtils_compareChars.restype = c_int
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 132
for _lib in _libs.values():
    if not _lib.has("StringUtils_compareStrings", "cdecl"):
        continue
    StringUtils_compareStrings = _lib.get("StringUtils_compareStrings", "cdecl")
    StringUtils_compareStrings.argtypes = [String, String]
    StringUtils_compareStrings.restype = c_int
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 140
for _lib in _libs.values():
    if not _lib.has("StringUtils_sortList", "cdecl"):
        continue
    StringUtils_sortList = _lib.get("StringUtils_sortList", "cdecl")
    StringUtils_sortList.argtypes = [LinkedList]
    StringUtils_sortList.restype = None
    break

# /home/user/libiec61850/src/common/inc/string_utilities.h: 151
for _lib in _libs.values():
    if not _lib.has("StringUtils_convertIPv6AdddressStringToByteArray", "cdecl"):
        continue
    StringUtils_convertIPv6AdddressStringToByteArray = _lib.get("StringUtils_convertIPv6AdddressStringToByteArray", "cdecl")
    StringUtils_convertIPv6AdddressStringToByteArray.argtypes = [String, POINTER(uint8_t)]
    StringUtils_convertIPv6AdddressStringToByteArray.restype = c_bool
    break

MemoryExceptionHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None))# ../libiec61850/hal/inc/lib_memory.h: 32

# ../libiec61850/hal/inc/lib_memory.h: 35
if _libs["libiec61850.so"].has("Memory_installExceptionHandler", "cdecl"):
    Memory_installExceptionHandler = _libs["libiec61850.so"].get("Memory_installExceptionHandler", "cdecl")
    Memory_installExceptionHandler.argtypes = [MemoryExceptionHandler, POINTER(None)]
    Memory_installExceptionHandler.restype = None

# ../libiec61850/hal/inc/lib_memory.h: 37
if _libs["libiec61850.so"].has("Memory_malloc", "cdecl"):
    Memory_malloc = _libs["libiec61850.so"].get("Memory_malloc", "cdecl")
    Memory_malloc.argtypes = [c_size_t]
    Memory_malloc.restype = POINTER(c_ubyte)
    Memory_malloc.errcheck = lambda v,*a : cast(v, c_void_p)

# ../libiec61850/hal/inc/lib_memory.h: 40
if _libs["libiec61850.so"].has("Memory_calloc", "cdecl"):
    Memory_calloc = _libs["libiec61850.so"].get("Memory_calloc", "cdecl")
    Memory_calloc.argtypes = [c_size_t, c_size_t]
    Memory_calloc.restype = POINTER(c_ubyte)
    Memory_calloc.errcheck = lambda v,*a : cast(v, c_void_p)

# ../libiec61850/hal/inc/lib_memory.h: 43
if _libs["libiec61850.so"].has("Memory_realloc", "cdecl"):
    Memory_realloc = _libs["libiec61850.so"].get("Memory_realloc", "cdecl")
    Memory_realloc.argtypes = [POINTER(None), c_size_t]
    Memory_realloc.restype = POINTER(c_ubyte)
    Memory_realloc.errcheck = lambda v,*a : cast(v, c_void_p)

# ../libiec61850/hal/inc/lib_memory.h: 47
if _libs["libiec61850.so"].has("Memory_free", "cdecl"):
    Memory_free = _libs["libiec61850.so"].get("Memory_free", "cdecl")
    Memory_free.argtypes = [POINTER(None)]
    Memory_free.restype = None

# /home/user/libiec61850/src/common/inc/buffer_chain.h: 31
class struct_sBufferChain(Structure):
    pass

BufferChain = POINTER(struct_sBufferChain)# /home/user/libiec61850/src/common/inc/buffer_chain.h: 29

struct_sBufferChain.__slots__ = [
    'length',
    'partLength',
    'partMaxLength',
    'buffer',
    'nextPart',
]
struct_sBufferChain._fields_ = [
    ('length', c_int),
    ('partLength', c_int),
    ('partMaxLength', c_int),
    ('buffer', POINTER(uint8_t)),
    ('nextPart', BufferChain),
]

# /home/user/libiec61850/src/common/inc/buffer_chain.h: 40
for _lib in _libs.values():
    if not _lib.has("BufferChain_init", "cdecl"):
        continue
    BufferChain_init = _lib.get("BufferChain_init", "cdecl")
    BufferChain_init.argtypes = [BufferChain, c_int, c_int, BufferChain, POINTER(uint8_t)]
    BufferChain_init.restype = None
    break

# /home/user/libiec61850/src/common/inc/buffer_chain.h: 46
class struct_anon_64(Structure):
    pass

struct_anon_64.__slots__ = [
    'memory',
    'currentPos',
    'size',
]
struct_anon_64._fields_ = [
    ('memory', POINTER(uint8_t)),
    ('currentPos', c_int),
    ('size', c_int),
]

MemoryArea = struct_anon_64# /home/user/libiec61850/src/common/inc/buffer_chain.h: 46

# /home/user/libiec61850/src/common/inc/buffer_chain.h: 49
for _lib in _libs.values():
    if not _lib.has("MemoryArea_initialize", "cdecl"):
        continue
    MemoryArea_initialize = _lib.get("MemoryArea_initialize", "cdecl")
    MemoryArea_initialize.argtypes = [POINTER(MemoryArea), POINTER(uint8_t), c_int]
    MemoryArea_initialize.restype = None
    break

# /home/user/libiec61850/src/common/inc/buffer_chain.h: 51
for _lib in _libs.values():
    if not _lib.has("MemoryArea_getNextBlock", "cdecl"):
        continue
    MemoryArea_getNextBlock = _lib.get("MemoryArea_getNextBlock", "cdecl")
    MemoryArea_getNextBlock.argtypes = [POINTER(MemoryArea), c_int]
    MemoryArea_getNextBlock.restype = POINTER(uint8_t)
    break

# /home/user/libiec61850/src/common/inc/byte_buffer.h: 37
class struct_anon_65(Structure):
    pass

struct_anon_65.__slots__ = [
    'buffer',
    'maxSize',
    'size',
]
struct_anon_65._fields_ = [
    ('buffer', POINTER(uint8_t)),
    ('maxSize', c_int),
    ('size', c_int),
]

ByteBuffer = struct_anon_65# /home/user/libiec61850/src/common/inc/byte_buffer.h: 37

# /home/user/libiec61850/src/common/inc/byte_buffer.h: 39
for _lib in _libs.values():
    if not _lib.has("ByteBuffer_create", "cdecl"):
        continue
    ByteBuffer_create = _lib.get("ByteBuffer_create", "cdecl")
    ByteBuffer_create.argtypes = [POINTER(ByteBuffer), c_int]
    ByteBuffer_create.restype = POINTER(ByteBuffer)
    break

# /home/user/libiec61850/src/common/inc/byte_buffer.h: 43
for _lib in _libs.values():
    if not _lib.has("ByteBuffer_destroy", "cdecl"):
        continue
    ByteBuffer_destroy = _lib.get("ByteBuffer_destroy", "cdecl")
    ByteBuffer_destroy.argtypes = [POINTER(ByteBuffer)]
    ByteBuffer_destroy.restype = None
    break

# /home/user/libiec61850/src/common/inc/byte_buffer.h: 46
for _lib in _libs.values():
    if not _lib.has("ByteBuffer_wrap", "cdecl"):
        continue
    ByteBuffer_wrap = _lib.get("ByteBuffer_wrap", "cdecl")
    ByteBuffer_wrap.argtypes = [POINTER(ByteBuffer), POINTER(uint8_t), c_int, c_int]
    ByteBuffer_wrap.restype = None
    break

# /home/user/libiec61850/src/common/inc/byte_buffer.h: 49
for _lib in _libs.values():
    if not _lib.has("ByteBuffer_append", "cdecl"):
        continue
    ByteBuffer_append = _lib.get("ByteBuffer_append", "cdecl")
    ByteBuffer_append.argtypes = [POINTER(ByteBuffer), POINTER(uint8_t), c_int]
    ByteBuffer_append.restype = c_int
    break

# /home/user/libiec61850/src/common/inc/byte_buffer.h: 52
for _lib in _libs.values():
    if not _lib.has("ByteBuffer_appendByte", "cdecl"):
        continue
    ByteBuffer_appendByte = _lib.get("ByteBuffer_appendByte", "cdecl")
    ByteBuffer_appendByte.argtypes = [POINTER(ByteBuffer), uint8_t]
    ByteBuffer_appendByte.restype = c_int
    break

# /home/user/libiec61850/src/common/inc/byte_buffer.h: 54
for _lib in _libs.values():
    if not _lib.has("ByteBuffer_getBuffer", "cdecl"):
        continue
    ByteBuffer_getBuffer = _lib.get("ByteBuffer_getBuffer", "cdecl")
    ByteBuffer_getBuffer.argtypes = [POINTER(ByteBuffer)]
    ByteBuffer_getBuffer.restype = POINTER(uint8_t)
    break

# /home/user/libiec61850/src/common/inc/byte_buffer.h: 58
for _lib in _libs.values():
    if not _lib.has("ByteBuffer_getSize", "cdecl"):
        continue
    ByteBuffer_getSize = _lib.get("ByteBuffer_getSize", "cdecl")
    ByteBuffer_getSize.argtypes = [POINTER(ByteBuffer)]
    ByteBuffer_getSize.restype = c_int
    break

# /home/user/libiec61850/src/common/inc/byte_buffer.h: 61
for _lib in _libs.values():
    if not _lib.has("ByteBuffer_getMaxSize", "cdecl"):
        continue
    ByteBuffer_getMaxSize = _lib.get("ByteBuffer_getMaxSize", "cdecl")
    ByteBuffer_getMaxSize.argtypes = [POINTER(ByteBuffer)]
    ByteBuffer_getMaxSize.restype = c_int
    break

# /home/user/libiec61850/src/common/inc/byte_buffer.h: 64
for _lib in _libs.values():
    if not _lib.has("ByteBuffer_setSize", "cdecl"):
        continue
    ByteBuffer_setSize = _lib.get("ByteBuffer_setSize", "cdecl")
    ByteBuffer_setSize.argtypes = [POINTER(ByteBuffer), c_int]
    ByteBuffer_setSize.restype = c_int
    break

# /home/user/libiec61850/src/common/inc/byte_buffer.h: 67
for _lib in _libs.values():
    if not _lib.has("ByteBuffer_print", "cdecl"):
        continue
    ByteBuffer_print = _lib.get("ByteBuffer_print", "cdecl")
    ByteBuffer_print.argtypes = [POINTER(ByteBuffer), String]
    ByteBuffer_print.restype = None
    break

# /home/user/libiec61850/src/common/inc/conversions.h: 32
for _lib in _libs.values():
    if not _lib.has("Conversions_intToStringBuffer", "cdecl"):
        continue
    Conversions_intToStringBuffer = _lib.get("Conversions_intToStringBuffer", "cdecl")
    Conversions_intToStringBuffer.argtypes = [c_int, c_int, POINTER(uint8_t)]
    Conversions_intToStringBuffer.restype = None
    break

# /home/user/libiec61850/src/common/inc/conversions.h: 35
for _lib in _libs.values():
    if not _lib.has("Conversions_msTimeToGeneralizedTime", "cdecl"):
        continue
    Conversions_msTimeToGeneralizedTime = _lib.get("Conversions_msTimeToGeneralizedTime", "cdecl")
    Conversions_msTimeToGeneralizedTime.argtypes = [uint64_t, POINTER(uint8_t)]
    Conversions_msTimeToGeneralizedTime.restype = None
    break

# /home/user/libiec61850/src/common/inc/conversions.h: 38
for _lib in _libs.values():
    if not _lib.has("Conversions_generalizedTimeToMsTime", "cdecl"):
        continue
    Conversions_generalizedTimeToMsTime = _lib.get("Conversions_generalizedTimeToMsTime", "cdecl")
    Conversions_generalizedTimeToMsTime.argtypes = [String]
    Conversions_generalizedTimeToMsTime.restype = uint64_t
    break

# /home/user/libiec61850/src/common/inc/conversions.h: 41
for _lib in _libs.values():
    if not _lib.has("memcpyReverseByteOrder", "cdecl"):
        continue
    memcpyReverseByteOrder = _lib.get("memcpyReverseByteOrder", "cdecl")
    memcpyReverseByteOrder.argtypes = [POINTER(uint8_t), POINTER(uint8_t), c_int]
    memcpyReverseByteOrder.restype = None
    break

# /home/user/libiec61850/src/common/inc/map.h: 32
class struct_sMap(Structure):
    pass

Map = POINTER(struct_sMap)# /home/user/libiec61850/src/common/inc/map.h: 30

struct_sMap.__slots__ = [
    'entries',
    'compareKeys',
]
struct_sMap._fields_ = [
    ('entries', LinkedList),
    ('compareKeys', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))),
]

# /home/user/libiec61850/src/common/inc/map.h: 40
for _lib in _libs.values():
    if not _lib.has("Map_create", "cdecl"):
        continue
    Map_create = _lib.get("Map_create", "cdecl")
    Map_create.argtypes = []
    Map_create.restype = Map
    break

# /home/user/libiec61850/src/common/inc/map.h: 43
for _lib in _libs.values():
    if not _lib.has("Map_size", "cdecl"):
        continue
    Map_size = _lib.get("Map_size", "cdecl")
    Map_size.argtypes = [Map]
    Map_size.restype = c_int
    break

# /home/user/libiec61850/src/common/inc/map.h: 45
for _lib in _libs.values():
    if not _lib.has("Map_addEntry", "cdecl"):
        continue
    Map_addEntry = _lib.get("Map_addEntry", "cdecl")
    Map_addEntry.argtypes = [Map, POINTER(None), POINTER(None)]
    Map_addEntry.restype = POINTER(c_ubyte)
    Map_addEntry.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/user/libiec61850/src/common/inc/map.h: 48
for _lib in _libs.values():
    if not _lib.has("Map_removeEntry", "cdecl"):
        continue
    Map_removeEntry = _lib.get("Map_removeEntry", "cdecl")
    Map_removeEntry.argtypes = [Map, POINTER(None), c_bool]
    Map_removeEntry.restype = POINTER(c_ubyte)
    Map_removeEntry.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/user/libiec61850/src/common/inc/map.h: 51
for _lib in _libs.values():
    if not _lib.has("Map_getEntry", "cdecl"):
        continue
    Map_getEntry = _lib.get("Map_getEntry", "cdecl")
    Map_getEntry.argtypes = [Map, POINTER(None)]
    Map_getEntry.restype = POINTER(c_ubyte)
    Map_getEntry.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/user/libiec61850/src/common/inc/map.h: 55
for _lib in _libs.values():
    if not _lib.has("Map_delete", "cdecl"):
        continue
    Map_delete = _lib.get("Map_delete", "cdecl")
    Map_delete.argtypes = [Map, c_bool]
    Map_delete.restype = None
    break

# /home/user/libiec61850/src/common/inc/map.h: 58
for _lib in _libs.values():
    if not _lib.has("Map_deleteStatic", "cdecl"):
        continue
    Map_deleteStatic = _lib.get("Map_deleteStatic", "cdecl")
    Map_deleteStatic.argtypes = [Map, c_bool]
    Map_deleteStatic.restype = None
    break

# /home/user/libiec61850/src/common/inc/map.h: 61
for _lib in _libs.values():
    if not _lib.has("Map_deleteDeep", "cdecl"):
        continue
    Map_deleteDeep = _lib.get("Map_deleteDeep", "cdecl")
    Map_deleteDeep.argtypes = [Map, c_bool, CFUNCTYPE(UNCHECKED(None), POINTER(None))]
    Map_deleteDeep.restype = None
    break

# /home/user/libiec61850/src/common/inc/simple_allocator.h: 31
class struct_anon_66(Structure):
    pass

struct_anon_66.__slots__ = [
    'memoryBlock',
    'currentPtr',
    'size',
]
struct_anon_66._fields_ = [
    ('memoryBlock', String),
    ('currentPtr', String),
    ('size', c_int),
]

MemoryAllocator = struct_anon_66# /home/user/libiec61850/src/common/inc/simple_allocator.h: 31

# /home/user/libiec61850/src/common/inc/simple_allocator.h: 34
for _lib in _libs.values():
    if not _lib.has("MemoryAllocator_init", "cdecl"):
        continue
    MemoryAllocator_init = _lib.get("MemoryAllocator_init", "cdecl")
    MemoryAllocator_init.argtypes = [POINTER(MemoryAllocator), String, c_int]
    MemoryAllocator_init.restype = None
    break

# /home/user/libiec61850/src/common/inc/simple_allocator.h: 37
for _lib in _libs.values():
    if not _lib.has("MemoryAllocator_getAlignedSize", "cdecl"):
        continue
    MemoryAllocator_getAlignedSize = _lib.get("MemoryAllocator_getAlignedSize", "cdecl")
    MemoryAllocator_getAlignedSize.argtypes = [c_int]
    MemoryAllocator_getAlignedSize.restype = c_int
    break

# /home/user/libiec61850/src/common/inc/simple_allocator.h: 39
for _lib in _libs.values():
    if not _lib.has("MemoryAllocator_allocate", "cdecl"):
        continue
    MemoryAllocator_allocate = _lib.get("MemoryAllocator_allocate", "cdecl")
    MemoryAllocator_allocate.argtypes = [POINTER(MemoryAllocator), c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        MemoryAllocator_allocate.restype = ReturnString
    else:
        MemoryAllocator_allocate.restype = String
        MemoryAllocator_allocate.errcheck = ReturnString
    break

# /home/user/libiec61850/src/common/inc/mem_alloc_linked_list.h: 38
class struct_sMemAllocLinkedList(Structure):
    pass

MemAllocLinkedList = POINTER(struct_sMemAllocLinkedList)# /home/user/libiec61850/src/common/inc/mem_alloc_linked_list.h: 38

# /home/user/libiec61850/src/common/inc/mem_alloc_linked_list.h: 41
for _lib in _libs.values():
    if not _lib.has("MemAllocLinkedList_create", "cdecl"):
        continue
    MemAllocLinkedList_create = _lib.get("MemAllocLinkedList_create", "cdecl")
    MemAllocLinkedList_create.argtypes = [POINTER(MemoryAllocator)]
    MemAllocLinkedList_create.restype = MemAllocLinkedList
    break

# /home/user/libiec61850/src/common/inc/mem_alloc_linked_list.h: 44
for _lib in _libs.values():
    if not _lib.has("MemAllocLinkedList_add", "cdecl"):
        continue
    MemAllocLinkedList_add = _lib.get("MemAllocLinkedList_add", "cdecl")
    MemAllocLinkedList_add.argtypes = [MemAllocLinkedList, POINTER(None)]
    MemAllocLinkedList_add.restype = LinkedList
    break

# ../libiec61850/hal/inc/hal_socket.h: 44
class struct_sServerSocket(Structure):
    pass

ServerSocket = POINTER(struct_sServerSocket)# ../libiec61850/hal/inc/hal_socket.h: 44

# ../libiec61850/hal/inc/hal_socket.h: 46
class struct_sUdpSocket(Structure):
    pass

UdpSocket = POINTER(struct_sUdpSocket)# ../libiec61850/hal/inc/hal_socket.h: 46

# ../libiec61850/hal/inc/hal_socket.h: 49
class struct_sSocket(Structure):
    pass

Socket = POINTER(struct_sSocket)# ../libiec61850/hal/inc/hal_socket.h: 49

# ../libiec61850/hal/inc/hal_socket.h: 52
class struct_sHandleSet(Structure):
    pass

HandleSet = POINTER(struct_sHandleSet)# ../libiec61850/hal/inc/hal_socket.h: 52

enum_anon_67 = c_int# ../libiec61850/hal/inc/hal_socket.h: 60

SOCKET_STATE_CONNECTING = 0# ../libiec61850/hal/inc/hal_socket.h: 60

SOCKET_STATE_FAILED = 1# ../libiec61850/hal/inc/hal_socket.h: 60

SOCKET_STATE_CONNECTED = 2# ../libiec61850/hal/inc/hal_socket.h: 60

SocketState = enum_anon_67# ../libiec61850/hal/inc/hal_socket.h: 60

# ../libiec61850/hal/inc/hal_socket.h: 69
if _libs["libiec61850.so"].has("Handleset_new", "cdecl"):
    Handleset_new = _libs["libiec61850.so"].get("Handleset_new", "cdecl")
    Handleset_new.argtypes = []
    Handleset_new.restype = HandleSet

# ../libiec61850/hal/inc/hal_socket.h: 75
if _libs["libiec61850.so"].has("Handleset_reset", "cdecl"):
    Handleset_reset = _libs["libiec61850.so"].get("Handleset_reset", "cdecl")
    Handleset_reset.argtypes = [HandleSet]
    Handleset_reset.restype = None

# ../libiec61850/hal/inc/hal_socket.h: 84
if _libs["libiec61850.so"].has("Handleset_addSocket", "cdecl"):
    Handleset_addSocket = _libs["libiec61850.so"].get("Handleset_addSocket", "cdecl")
    Handleset_addSocket.argtypes = [HandleSet, Socket]
    Handleset_addSocket.restype = None

# ../libiec61850/hal/inc/hal_socket.h: 90
if _libs["libiec61850.so"].has("Handleset_removeSocket", "cdecl"):
    Handleset_removeSocket = _libs["libiec61850.so"].get("Handleset_removeSocket", "cdecl")
    Handleset_removeSocket.argtypes = [HandleSet, Socket]
    Handleset_removeSocket.restype = None

# ../libiec61850/hal/inc/hal_socket.h: 108
if _libs["libiec61850.so"].has("Handleset_waitReady", "cdecl"):
    Handleset_waitReady = _libs["libiec61850.so"].get("Handleset_waitReady", "cdecl")
    Handleset_waitReady.argtypes = [HandleSet, c_uint]
    Handleset_waitReady.restype = c_int

# ../libiec61850/hal/inc/hal_socket.h: 116
if _libs["libiec61850.so"].has("Handleset_destroy", "cdecl"):
    Handleset_destroy = _libs["libiec61850.so"].get("Handleset_destroy", "cdecl")
    Handleset_destroy.argtypes = [HandleSet]
    Handleset_destroy.restype = None

# ../libiec61850/hal/inc/hal_socket.h: 129
if _libs["libiec61850.so"].has("TcpServerSocket_create", "cdecl"):
    TcpServerSocket_create = _libs["libiec61850.so"].get("TcpServerSocket_create", "cdecl")
    TcpServerSocket_create.argtypes = [String, c_int]
    TcpServerSocket_create.restype = ServerSocket

# ../libiec61850/hal/inc/hal_socket.h: 137
if _libs["libiec61850.so"].has("UdpSocket_create", "cdecl"):
    UdpSocket_create = _libs["libiec61850.so"].get("UdpSocket_create", "cdecl")
    UdpSocket_create.argtypes = []
    UdpSocket_create.restype = UdpSocket

# ../libiec61850/hal/inc/hal_socket.h: 145
if _libs["libiec61850.so"].has("UdpSocket_createIpV6", "cdecl"):
    UdpSocket_createIpV6 = _libs["libiec61850.so"].get("UdpSocket_createIpV6", "cdecl")
    UdpSocket_createIpV6.argtypes = []
    UdpSocket_createIpV6.restype = UdpSocket

# ../libiec61850/hal/inc/hal_socket.h: 156
if _libs["libiec61850.so"].has("UdpSocket_addGroupMembership", "cdecl"):
    UdpSocket_addGroupMembership = _libs["libiec61850.so"].get("UdpSocket_addGroupMembership", "cdecl")
    UdpSocket_addGroupMembership.argtypes = [UdpSocket, String]
    UdpSocket_addGroupMembership.restype = c_bool

# ../libiec61850/hal/inc/hal_socket.h: 167
if _libs["libiec61850.so"].has("UdpSocket_setMulticastTtl", "cdecl"):
    UdpSocket_setMulticastTtl = _libs["libiec61850.so"].get("UdpSocket_setMulticastTtl", "cdecl")
    UdpSocket_setMulticastTtl.argtypes = [UdpSocket, c_int]
    UdpSocket_setMulticastTtl.restype = c_bool

# ../libiec61850/hal/inc/hal_socket.h: 170
if _libs["libiec61850.so"].has("UdpSocket_bind", "cdecl"):
    UdpSocket_bind = _libs["libiec61850.so"].get("UdpSocket_bind", "cdecl")
    UdpSocket_bind.argtypes = [UdpSocket, String, c_int]
    UdpSocket_bind.restype = c_bool

# ../libiec61850/hal/inc/hal_socket.h: 173
if _libs["libiec61850.so"].has("UdpSocket_sendTo", "cdecl"):
    UdpSocket_sendTo = _libs["libiec61850.so"].get("UdpSocket_sendTo", "cdecl")
    UdpSocket_sendTo.argtypes = [UdpSocket, String, c_int, POINTER(uint8_t), c_int]
    UdpSocket_sendTo.restype = c_bool

# ../libiec61850/hal/inc/hal_socket.h: 187
if _libs["libiec61850.so"].has("UdpSocket_receiveFrom", "cdecl"):
    UdpSocket_receiveFrom = _libs["libiec61850.so"].get("UdpSocket_receiveFrom", "cdecl")
    UdpSocket_receiveFrom.argtypes = [UdpSocket, String, c_int, POINTER(uint8_t), c_int]
    UdpSocket_receiveFrom.restype = c_int

# ../libiec61850/hal/inc/hal_socket.h: 191
if _libs["libiec61850.so"].has("ServerSocket_listen", "cdecl"):
    ServerSocket_listen = _libs["libiec61850.so"].get("ServerSocket_listen", "cdecl")
    ServerSocket_listen.argtypes = [ServerSocket]
    ServerSocket_listen.restype = None

# ../libiec61850/hal/inc/hal_socket.h: 208
if _libs["libiec61850.so"].has("ServerSocket_accept", "cdecl"):
    ServerSocket_accept = _libs["libiec61850.so"].get("ServerSocket_accept", "cdecl")
    ServerSocket_accept.argtypes = [ServerSocket]
    ServerSocket_accept.restype = Socket

# ../libiec61850/hal/inc/hal_socket.h: 221
if _libs["libiec61850.so"].has("Socket_activateTcpKeepAlive", "cdecl"):
    Socket_activateTcpKeepAlive = _libs["libiec61850.so"].get("Socket_activateTcpKeepAlive", "cdecl")
    Socket_activateTcpKeepAlive.argtypes = [Socket, c_int, c_int, c_int]
    Socket_activateTcpKeepAlive.restype = None

# ../libiec61850/hal/inc/hal_socket.h: 233
if _libs["libiec61850.so"].has("ServerSocket_setBacklog", "cdecl"):
    ServerSocket_setBacklog = _libs["libiec61850.so"].get("ServerSocket_setBacklog", "cdecl")
    ServerSocket_setBacklog.argtypes = [ServerSocket, c_int]
    ServerSocket_setBacklog.restype = None

# ../libiec61850/hal/inc/hal_socket.h: 245
if _libs["libiec61850.so"].has("ServerSocket_destroy", "cdecl"):
    ServerSocket_destroy = _libs["libiec61850.so"].get("ServerSocket_destroy", "cdecl")
    ServerSocket_destroy.argtypes = [ServerSocket]
    ServerSocket_destroy.restype = None

# ../libiec61850/hal/inc/hal_socket.h: 255
if _libs["libiec61850.so"].has("TcpSocket_create", "cdecl"):
    TcpSocket_create = _libs["libiec61850.so"].get("TcpSocket_create", "cdecl")
    TcpSocket_create.argtypes = []
    TcpSocket_create.restype = Socket

# ../libiec61850/hal/inc/hal_socket.h: 264
if _libs["libiec61850.so"].has("Socket_setConnectTimeout", "cdecl"):
    Socket_setConnectTimeout = _libs["libiec61850.so"].get("Socket_setConnectTimeout", "cdecl")
    Socket_setConnectTimeout.argtypes = [Socket, uint32_t]
    Socket_setConnectTimeout.restype = None

# ../libiec61850/hal/inc/hal_socket.h: 278
if _libs["libiec61850.so"].has("Socket_bind", "cdecl"):
    Socket_bind = _libs["libiec61850.so"].get("Socket_bind", "cdecl")
    Socket_bind.argtypes = [Socket, String, c_int]
    Socket_bind.restype = c_bool

# ../libiec61850/hal/inc/hal_socket.h: 299
if _libs["libiec61850.so"].has("Socket_connect", "cdecl"):
    Socket_connect = _libs["libiec61850.so"].get("Socket_connect", "cdecl")
    Socket_connect.argtypes = [Socket, String, c_int]
    Socket_connect.restype = c_bool

# ../libiec61850/hal/inc/hal_socket.h: 302
if _libs["libiec61850.so"].has("Socket_connectAsync", "cdecl"):
    Socket_connectAsync = _libs["libiec61850.so"].get("Socket_connectAsync", "cdecl")
    Socket_connectAsync.argtypes = [Socket, String, c_int]
    Socket_connectAsync.restype = c_bool

# ../libiec61850/hal/inc/hal_socket.h: 305
if _libs["libiec61850.so"].has("Socket_checkAsyncConnectState", "cdecl"):
    Socket_checkAsyncConnectState = _libs["libiec61850.so"].get("Socket_checkAsyncConnectState", "cdecl")
    Socket_checkAsyncConnectState.argtypes = [Socket]
    Socket_checkAsyncConnectState.restype = SocketState

# ../libiec61850/hal/inc/hal_socket.h: 324
if _libs["libiec61850.so"].has("Socket_read", "cdecl"):
    Socket_read = _libs["libiec61850.so"].get("Socket_read", "cdecl")
    Socket_read.argtypes = [Socket, POINTER(uint8_t), c_int]
    Socket_read.restype = c_int

# ../libiec61850/hal/inc/hal_socket.h: 336
if _libs["libiec61850.so"].has("Socket_write", "cdecl"):
    Socket_write = _libs["libiec61850.so"].get("Socket_write", "cdecl")
    Socket_write.argtypes = [Socket, POINTER(uint8_t), c_int]
    Socket_write.restype = c_int

# ../libiec61850/hal/inc/hal_socket.h: 338
if _libs["libiec61850.so"].has("Socket_getLocalAddress", "cdecl"):
    Socket_getLocalAddress = _libs["libiec61850.so"].get("Socket_getLocalAddress", "cdecl")
    Socket_getLocalAddress.argtypes = [Socket]
    if sizeof(c_int) == sizeof(c_void_p):
        Socket_getLocalAddress.restype = ReturnString
    else:
        Socket_getLocalAddress.restype = String
        Socket_getLocalAddress.errcheck = ReturnString

# ../libiec61850/hal/inc/hal_socket.h: 352
if _libs["libiec61850.so"].has("Socket_getPeerAddress", "cdecl"):
    Socket_getPeerAddress = _libs["libiec61850.so"].get("Socket_getPeerAddress", "cdecl")
    Socket_getPeerAddress.argtypes = [Socket]
    if sizeof(c_int) == sizeof(c_void_p):
        Socket_getPeerAddress.restype = ReturnString
    else:
        Socket_getPeerAddress.restype = String
        Socket_getPeerAddress.errcheck = ReturnString

# ../libiec61850/hal/inc/hal_socket.h: 369
if _libs["libiec61850.so"].has("Socket_getPeerAddressStatic", "cdecl"):
    Socket_getPeerAddressStatic = _libs["libiec61850.so"].get("Socket_getPeerAddressStatic", "cdecl")
    Socket_getPeerAddressStatic.argtypes = [Socket, String]
    if sizeof(c_int) == sizeof(c_void_p):
        Socket_getPeerAddressStatic.restype = ReturnString
    else:
        Socket_getPeerAddressStatic.restype = String
        Socket_getPeerAddressStatic.errcheck = ReturnString

# ../libiec61850/hal/inc/hal_socket.h: 383
if _libs["libiec61850.so"].has("Socket_destroy", "cdecl"):
    Socket_destroy = _libs["libiec61850.so"].get("Socket_destroy", "cdecl")
    Socket_destroy.argtypes = [Socket]
    Socket_destroy.restype = None

# /home/user/libiec61850/src/common/inc/sntp_client.h: 32
class struct_sSNTPClient(Structure):
    pass

SNTPClient = POINTER(struct_sSNTPClient)# /home/user/libiec61850/src/common/inc/sntp_client.h: 32

SNTPClient_UserCallback = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_bool)# /home/user/libiec61850/src/common/inc/sntp_client.h: 34

# /home/user/libiec61850/src/common/inc/sntp_client.h: 37
for _lib in _libs.values():
    if not _lib.has("SNTPClient_create", "cdecl"):
        continue
    SNTPClient_create = _lib.get("SNTPClient_create", "cdecl")
    SNTPClient_create.argtypes = []
    SNTPClient_create.restype = SNTPClient
    break

# /home/user/libiec61850/src/common/inc/sntp_client.h: 40
for _lib in _libs.values():
    if not _lib.has("SNTPClient_setLocalAddress", "cdecl"):
        continue
    SNTPClient_setLocalAddress = _lib.get("SNTPClient_setLocalAddress", "cdecl")
    SNTPClient_setLocalAddress.argtypes = [SNTPClient, String]
    SNTPClient_setLocalAddress.restype = None
    break

# /home/user/libiec61850/src/common/inc/sntp_client.h: 43
for _lib in _libs.values():
    if not _lib.has("SNTPClient_setLocalPort", "cdecl"):
        continue
    SNTPClient_setLocalPort = _lib.get("SNTPClient_setLocalPort", "cdecl")
    SNTPClient_setLocalPort.argtypes = [SNTPClient, c_int]
    SNTPClient_setLocalPort.restype = None
    break

# /home/user/libiec61850/src/common/inc/sntp_client.h: 46
for _lib in _libs.values():
    if not _lib.has("SNTPClient_getHandleSet", "cdecl"):
        continue
    SNTPClient_getHandleSet = _lib.get("SNTPClient_getHandleSet", "cdecl")
    SNTPClient_getHandleSet.argtypes = [SNTPClient]
    SNTPClient_getHandleSet.restype = HandleSet
    break

# /home/user/libiec61850/src/common/inc/sntp_client.h: 49
for _lib in _libs.values():
    if not _lib.has("SNTPClient_addServer", "cdecl"):
        continue
    SNTPClient_addServer = _lib.get("SNTPClient_addServer", "cdecl")
    SNTPClient_addServer.argtypes = [SNTPClient, String, c_int]
    SNTPClient_addServer.restype = None
    break

# /home/user/libiec61850/src/common/inc/sntp_client.h: 52
for _lib in _libs.values():
    if not _lib.has("SNTPClient_setPollInterval", "cdecl"):
        continue
    SNTPClient_setPollInterval = _lib.get("SNTPClient_setPollInterval", "cdecl")
    SNTPClient_setPollInterval.argtypes = [SNTPClient, uint32_t]
    SNTPClient_setPollInterval.restype = None
    break

# /home/user/libiec61850/src/common/inc/sntp_client.h: 55
for _lib in _libs.values():
    if not _lib.has("SNTPClient_setUserCallback", "cdecl"):
        continue
    SNTPClient_setUserCallback = _lib.get("SNTPClient_setUserCallback", "cdecl")
    SNTPClient_setUserCallback.argtypes = [SNTPClient, SNTPClient_UserCallback, POINTER(None)]
    SNTPClient_setUserCallback.restype = None
    break

# /home/user/libiec61850/src/common/inc/sntp_client.h: 58
for _lib in _libs.values():
    if not _lib.has("SNTPClient_isSynchronized", "cdecl"):
        continue
    SNTPClient_isSynchronized = _lib.get("SNTPClient_isSynchronized", "cdecl")
    SNTPClient_isSynchronized.argtypes = [SNTPClient]
    SNTPClient_isSynchronized.restype = c_bool
    break

# /home/user/libiec61850/src/common/inc/sntp_client.h: 61
for _lib in _libs.values():
    if not _lib.has("SNTPClient_start", "cdecl"):
        continue
    SNTPClient_start = _lib.get("SNTPClient_start", "cdecl")
    SNTPClient_start.argtypes = [SNTPClient]
    SNTPClient_start.restype = None
    break

# /home/user/libiec61850/src/common/inc/sntp_client.h: 64
for _lib in _libs.values():
    if not _lib.has("SNTPClient_stop", "cdecl"):
        continue
    SNTPClient_stop = _lib.get("SNTPClient_stop", "cdecl")
    SNTPClient_stop.argtypes = [SNTPClient]
    SNTPClient_stop.restype = None
    break

# /home/user/libiec61850/src/common/inc/sntp_client.h: 67
for _lib in _libs.values():
    if not _lib.has("SNTPClient_destroy", "cdecl"):
        continue
    SNTPClient_destroy = _lib.get("SNTPClient_destroy", "cdecl")
    SNTPClient_destroy.argtypes = [SNTPClient]
    SNTPClient_destroy.restype = None
    break

# /home/user/libiec61850/src/common/inc/string_map.h: 27
for _lib in _libs.values():
    if not _lib.has("StringMap_create", "cdecl"):
        continue
    StringMap_create = _lib.get("StringMap_create", "cdecl")
    StringMap_create.argtypes = []
    StringMap_create.restype = Map
    break

# ../libiec61850/src/r_session/r_session.h: 34
class struct_sRSession(Structure):
    pass

RSession = POINTER(struct_sRSession)# ../libiec61850/src/r_session/r_session.h: 34

enum_anon_68 = c_int# ../libiec61850/src/r_session/r_session.h: 40

R_SESSION_SEC_ALGO_NONE = 0# ../libiec61850/src/r_session/r_session.h: 40

R_SESSION_SEC_ALGO_AES_128_GCM = 1# ../libiec61850/src/r_session/r_session.h: 40

R_SESSION_SEC_ALGO_AES_256_GCM = 2# ../libiec61850/src/r_session/r_session.h: 40

RSecurityAlgorithm = enum_anon_68# ../libiec61850/src/r_session/r_session.h: 40

enum_anon_69 = c_int# ../libiec61850/src/r_session/r_session.h: 52

R_SESSION_SIG_ALGO_NONE = 0# ../libiec61850/src/r_session/r_session.h: 52

R_SESSION_SIG_ALGO_HMAC_SHA256_80 = 1# ../libiec61850/src/r_session/r_session.h: 52

R_SESSION_SIG_ALGO_HMAC_SHA256_128 = 2# ../libiec61850/src/r_session/r_session.h: 52

R_SESSION_SIG_ALGO_HMAC_SHA256_256 = 3# ../libiec61850/src/r_session/r_session.h: 52

R_SESSION_SIG_ALGO_AES_GMAC_64 = 4# ../libiec61850/src/r_session/r_session.h: 52

R_SESSION_SIG_ALGO_AES_GMAC_128 = 5# ../libiec61850/src/r_session/r_session.h: 52

R_SESSION_SIG_ALGO_HMAC_SHA3_80 = 6# ../libiec61850/src/r_session/r_session.h: 52

R_SESSION_SIG_ALGO_HMAC_SHA3_128 = 7# ../libiec61850/src/r_session/r_session.h: 52

R_SESSION_SIG_ALGO_HMAC_SHA3_256 = 8# ../libiec61850/src/r_session/r_session.h: 52

RSignatureAlgorithm = enum_anon_69# ../libiec61850/src/r_session/r_session.h: 52

enum_anon_70 = c_int# ../libiec61850/src/r_session/r_session.h: 64

R_SESSION_ERROR_OK = 0# ../libiec61850/src/r_session/r_session.h: 64

R_SESSION_ERROR_INVALID_KEY = 1# ../libiec61850/src/r_session/r_session.h: 64

R_SESSION_ERROR_KEY_QUEUE_FULL = 2# ../libiec61850/src/r_session/r_session.h: 64

R_SESSION_ERROR_NO_SOCKET = 3# ../libiec61850/src/r_session/r_session.h: 64

R_SESSION_ERROR_OUT_OF_MEMORY = 4# ../libiec61850/src/r_session/r_session.h: 64

R_SESSION_ERROR_FAILED_TO_SEND = 5# ../libiec61850/src/r_session/r_session.h: 64

R_SESSION_ERROR_FAILED_TO_RECEIVE = 6# ../libiec61850/src/r_session/r_session.h: 64

R_SESSION_ERROR_INVALID_MESSAGE = 7# ../libiec61850/src/r_session/r_session.h: 64

R_SESSION_ERROR_SET_FAILED = 8# ../libiec61850/src/r_session/r_session.h: 64

RSessionError = enum_anon_70# ../libiec61850/src/r_session/r_session.h: 64

# ../libiec61850/src/r_session/r_session.h: 68
class struct_sRSessionPayloadElement(Structure):
    pass

RSessionPayloadElement = POINTER(struct_sRSessionPayloadElement)# ../libiec61850/src/r_session/r_session.h: 66

struct_sRSessionPayloadElement.__slots__ = [
    'simulation',
    'appId',
    'payloadType',
    'payload',
    'payloadSize',
    'nextElement',
]
struct_sRSessionPayloadElement._fields_ = [
    ('simulation', c_bool),
    ('appId', uint16_t),
    ('payloadType', uint8_t),
    ('payload', POINTER(uint8_t)),
    ('payloadSize', c_int),
    ('nextElement', RSessionPayloadElement),
]

# ../libiec61850/src/r_session/r_session.h: 84
for _lib in _libs.values():
    if not _lib.has("RSession_create", "cdecl"):
        continue
    RSession_create = _lib.get("RSession_create", "cdecl")
    RSession_create.argtypes = []
    RSession_create.restype = RSession
    break

# ../libiec61850/src/r_session/r_session.h: 93
for _lib in _libs.values():
    if not _lib.has("RSession_setBufferSize", "cdecl"):
        continue
    RSession_setBufferSize = _lib.get("RSession_setBufferSize", "cdecl")
    RSession_setBufferSize.argtypes = [RSession, uint16_t]
    RSession_setBufferSize.restype = None
    break

# ../libiec61850/src/r_session/r_session.h: 106
for _lib in _libs.values():
    if not _lib.has("RSession_setSecurity", "cdecl"):
        continue
    RSession_setSecurity = _lib.get("RSession_setSecurity", "cdecl")
    RSession_setSecurity.argtypes = [RSession, RSecurityAlgorithm, RSignatureAlgorithm]
    RSession_setSecurity.restype = RSessionError
    break

# ../libiec61850/src/r_session/r_session.h: 116
for _lib in _libs.values():
    if not _lib.has("RSession_setLocalAddress", "cdecl"):
        continue
    RSession_setLocalAddress = _lib.get("RSession_setLocalAddress", "cdecl")
    RSession_setLocalAddress.argtypes = [RSession, String, c_int]
    RSession_setLocalAddress.restype = RSessionError
    break

# ../libiec61850/src/r_session/r_session.h: 127
for _lib in _libs.values():
    if not _lib.has("RSession_addMulticastGroup", "cdecl"):
        continue
    RSession_addMulticastGroup = _lib.get("RSession_addMulticastGroup", "cdecl")
    RSession_addMulticastGroup.argtypes = [RSession, String]
    RSession_addMulticastGroup.restype = RSessionError
    break

# ../libiec61850/src/r_session/r_session.h: 138
for _lib in _libs.values():
    if not _lib.has("RSession_setMulticastTtl", "cdecl"):
        continue
    RSession_setMulticastTtl = _lib.get("RSession_setMulticastTtl", "cdecl")
    RSession_setMulticastTtl.argtypes = [RSession, c_int]
    RSession_setMulticastTtl.restype = RSessionError
    break

# ../libiec61850/src/r_session/r_session.h: 150
for _lib in _libs.values():
    if not _lib.has("RSession_setRemoteAddress", "cdecl"):
        continue
    RSession_setRemoteAddress = _lib.get("RSession_setRemoteAddress", "cdecl")
    RSession_setRemoteAddress.argtypes = [RSession, String, c_int]
    RSession_setRemoteAddress.restype = RSessionError
    break

# ../libiec61850/src/r_session/r_session.h: 160
for _lib in _libs.values():
    if not _lib.has("RSession_start", "cdecl"):
        continue
    RSession_start = _lib.get("RSession_start", "cdecl")
    RSession_start.argtypes = [RSession]
    RSession_start.restype = RSessionError
    break

# ../libiec61850/src/r_session/r_session.h: 170
for _lib in _libs.values():
    if not _lib.has("RSession_stop", "cdecl"):
        continue
    RSession_stop = _lib.get("RSession_stop", "cdecl")
    RSession_stop.argtypes = [RSession]
    RSession_stop.restype = RSessionError
    break

# ../libiec61850/src/r_session/r_session.h: 183
for _lib in _libs.values():
    if not _lib.has("RSession_addKey", "cdecl"):
        continue
    RSession_addKey = _lib.get("RSession_addKey", "cdecl")
    RSession_addKey.argtypes = [RSession, uint32_t, POINTER(uint8_t), c_int, RSecurityAlgorithm, RSignatureAlgorithm]
    RSession_addKey.restype = RSessionError
    break

# ../libiec61850/src/r_session/r_session.h: 192
for _lib in _libs.values():
    if not _lib.has("RSession_removeKey", "cdecl"):
        continue
    RSession_removeKey = _lib.get("RSession_removeKey", "cdecl")
    RSession_removeKey.argtypes = [RSession, uint32_t]
    RSession_removeKey.restype = RSessionError
    break

# ../libiec61850/src/r_session/r_session.h: 200
for _lib in _libs.values():
    if not _lib.has("RSession_removeAllKeys", "cdecl"):
        continue
    RSession_removeAllKeys = _lib.get("RSession_removeAllKeys", "cdecl")
    RSession_removeAllKeys.argtypes = [RSession]
    RSession_removeAllKeys.restype = None
    break

enum_anon_71 = c_int# ../libiec61850/src/r_session/r_session.h: 205

RSESSION_KEY_EVENT__NEED_KEY = 1# ../libiec61850/src/r_session/r_session.h: 205

RSessionKeyEvent = enum_anon_71# ../libiec61850/src/r_session/r_session.h: 205

RSession_KeyEventHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), RSession, RSessionKeyEvent, uint32_t)# ../libiec61850/src/r_session/r_session.h: 207

# ../libiec61850/src/r_session/r_session.h: 219
for _lib in _libs.values():
    if not _lib.has("RSession_setKeyEventHandler", "cdecl"):
        continue
    RSession_setKeyEventHandler = _lib.get("RSession_setKeyEventHandler", "cdecl")
    RSession_setKeyEventHandler.argtypes = [RSession, RSession_KeyEventHandler, POINTER(None)]
    RSession_setKeyEventHandler.restype = None
    break

# ../libiec61850/src/r_session/r_session.h: 230
for _lib in _libs.values():
    if not _lib.has("RSession_setActiveKey", "cdecl"):
        continue
    RSession_setActiveKey = _lib.get("RSession_setActiveKey", "cdecl")
    RSession_setActiveKey.argtypes = [RSession, uint32_t]
    RSession_setActiveKey.restype = RSessionError
    break

# ../libiec61850/src/r_session/r_session.h: 238
for _lib in _libs.values():
    if not _lib.has("RSession_destroy", "cdecl"):
        continue
    RSession_destroy = _lib.get("RSession_destroy", "cdecl")
    RSession_destroy.argtypes = [RSession]
    RSession_destroy.restype = None
    break

# /home/user/libiec61850/src/goose/goose_publisher.h: 44
class struct_sCommParameters(Structure):
    pass

struct_sCommParameters.__slots__ = [
    'vlanPriority',
    'vlanId',
    'appId',
    'dstAddress',
]
struct_sCommParameters._fields_ = [
    ('vlanPriority', uint8_t),
    ('vlanId', uint16_t),
    ('appId', uint16_t),
    ('dstAddress', uint8_t * int(6)),
]

CommParameters = struct_sCommParameters# /home/user/libiec61850/src/goose/goose_publisher.h: 44

# /home/user/libiec61850/src/goose/goose_publisher.h: 48
class struct_sGoosePublisher(Structure):
    pass

GoosePublisher = POINTER(struct_sGoosePublisher)# /home/user/libiec61850/src/goose/goose_publisher.h: 48

# /home/user/libiec61850/src/goose/goose_publisher.h: 61
if _libs["libiec61850.so"].has("GoosePublisher_create", "cdecl"):
    GoosePublisher_create = _libs["libiec61850.so"].get("GoosePublisher_create", "cdecl")
    GoosePublisher_create.argtypes = [POINTER(CommParameters), String]
    GoosePublisher_create.restype = GoosePublisher

# /home/user/libiec61850/src/goose/goose_publisher.h: 73
if _libs["libiec61850.so"].has("GoosePublisher_createEx", "cdecl"):
    GoosePublisher_createEx = _libs["libiec61850.so"].get("GoosePublisher_createEx", "cdecl")
    GoosePublisher_createEx.argtypes = [POINTER(CommParameters), String, c_bool]
    GoosePublisher_createEx.restype = GoosePublisher

# /home/user/libiec61850/src/goose/goose_publisher.h: 84
for _lib in _libs.values():
    if not _lib.has("GoosePublisher_createRemote", "cdecl"):
        continue
    GoosePublisher_createRemote = _lib.get("GoosePublisher_createRemote", "cdecl")
    GoosePublisher_createRemote.argtypes = [RSession, uint16_t]
    GoosePublisher_createRemote.restype = GoosePublisher
    break

# /home/user/libiec61850/src/goose/goose_publisher.h: 92
if _libs["libiec61850.so"].has("GoosePublisher_destroy", "cdecl"):
    GoosePublisher_destroy = _libs["libiec61850.so"].get("GoosePublisher_destroy", "cdecl")
    GoosePublisher_destroy.argtypes = [GoosePublisher]
    GoosePublisher_destroy.restype = None

# /home/user/libiec61850/src/goose/goose_publisher.h: 103
if _libs["libiec61850.so"].has("GoosePublisher_publish", "cdecl"):
    GoosePublisher_publish = _libs["libiec61850.so"].get("GoosePublisher_publish", "cdecl")
    GoosePublisher_publish.argtypes = [GoosePublisher, LinkedList]
    GoosePublisher_publish.restype = c_int

# /home/user/libiec61850/src/goose/goose_publisher.h: 115
if _libs["libiec61850.so"].has("GoosePublisher_publishAndDump", "cdecl"):
    GoosePublisher_publishAndDump = _libs["libiec61850.so"].get("GoosePublisher_publishAndDump", "cdecl")
    GoosePublisher_publishAndDump.argtypes = [GoosePublisher, LinkedList, String, POINTER(c_int32), c_int32]
    GoosePublisher_publishAndDump.restype = c_int

# /home/user/libiec61850/src/goose/goose_publisher.h: 124
if _libs["libiec61850.so"].has("GoosePublisher_setGoID", "cdecl"):
    GoosePublisher_setGoID = _libs["libiec61850.so"].get("GoosePublisher_setGoID", "cdecl")
    GoosePublisher_setGoID.argtypes = [GoosePublisher, String]
    GoosePublisher_setGoID.restype = None

# /home/user/libiec61850/src/goose/goose_publisher.h: 133
if _libs["libiec61850.so"].has("GoosePublisher_setGoCbRef", "cdecl"):
    GoosePublisher_setGoCbRef = _libs["libiec61850.so"].get("GoosePublisher_setGoCbRef", "cdecl")
    GoosePublisher_setGoCbRef.argtypes = [GoosePublisher, String]
    GoosePublisher_setGoCbRef.restype = None

# /home/user/libiec61850/src/goose/goose_publisher.h: 142
if _libs["libiec61850.so"].has("GoosePublisher_setTimeAllowedToLive", "cdecl"):
    GoosePublisher_setTimeAllowedToLive = _libs["libiec61850.so"].get("GoosePublisher_setTimeAllowedToLive", "cdecl")
    GoosePublisher_setTimeAllowedToLive.argtypes = [GoosePublisher, uint32_t]
    GoosePublisher_setTimeAllowedToLive.restype = None

# /home/user/libiec61850/src/goose/goose_publisher.h: 151
if _libs["libiec61850.so"].has("GoosePublisher_setDataSetRef", "cdecl"):
    GoosePublisher_setDataSetRef = _libs["libiec61850.so"].get("GoosePublisher_setDataSetRef", "cdecl")
    GoosePublisher_setDataSetRef.argtypes = [GoosePublisher, String]
    GoosePublisher_setDataSetRef.restype = None

# /home/user/libiec61850/src/goose/goose_publisher.h: 160
if _libs["libiec61850.so"].has("GoosePublisher_setConfRev", "cdecl"):
    GoosePublisher_setConfRev = _libs["libiec61850.so"].get("GoosePublisher_setConfRev", "cdecl")
    GoosePublisher_setConfRev.argtypes = [GoosePublisher, uint32_t]
    GoosePublisher_setConfRev.restype = None

# /home/user/libiec61850/src/goose/goose_publisher.h: 169
if _libs["libiec61850.so"].has("GoosePublisher_setSimulation", "cdecl"):
    GoosePublisher_setSimulation = _libs["libiec61850.so"].get("GoosePublisher_setSimulation", "cdecl")
    GoosePublisher_setSimulation.argtypes = [GoosePublisher, c_bool]
    GoosePublisher_setSimulation.restype = None

# /home/user/libiec61850/src/goose/goose_publisher.h: 181
if _libs["libiec61850.so"].has("GoosePublisher_setStNum", "cdecl"):
    GoosePublisher_setStNum = _libs["libiec61850.so"].get("GoosePublisher_setStNum", "cdecl")
    GoosePublisher_setStNum.argtypes = [GoosePublisher, uint32_t]
    GoosePublisher_setStNum.restype = None

# /home/user/libiec61850/src/goose/goose_publisher.h: 192
if _libs["libiec61850.so"].has("GoosePublisher_setSqNum", "cdecl"):
    GoosePublisher_setSqNum = _libs["libiec61850.so"].get("GoosePublisher_setSqNum", "cdecl")
    GoosePublisher_setSqNum.argtypes = [GoosePublisher, uint32_t]
    GoosePublisher_setSqNum.restype = None

# /home/user/libiec61850/src/goose/goose_publisher.h: 201
if _libs["libiec61850.so"].has("GoosePublisher_setNeedsCommission", "cdecl"):
    GoosePublisher_setNeedsCommission = _libs["libiec61850.so"].get("GoosePublisher_setNeedsCommission", "cdecl")
    GoosePublisher_setNeedsCommission.argtypes = [GoosePublisher, c_bool]
    GoosePublisher_setNeedsCommission.restype = None

# /home/user/libiec61850/src/goose/goose_publisher.h: 213
if _libs["libiec61850.so"].has("GoosePublisher_increaseStNum", "cdecl"):
    GoosePublisher_increaseStNum = _libs["libiec61850.so"].get("GoosePublisher_increaseStNum", "cdecl")
    GoosePublisher_increaseStNum.argtypes = [GoosePublisher]
    GoosePublisher_increaseStNum.restype = uint64_t

# /home/user/libiec61850/src/goose/goose_publisher.h: 223
if _libs["libiec61850.so"].has("GoosePublisher_reset", "cdecl"):
    GoosePublisher_reset = _libs["libiec61850.so"].get("GoosePublisher_reset", "cdecl")
    GoosePublisher_reset.argtypes = [GoosePublisher]
    GoosePublisher_reset.restype = None

# ../libiec61850/hal/inc/hal_ethernet.h: 34
class struct_sEthernetSocket(Structure):
    pass

EthernetSocket = POINTER(struct_sEthernetSocket)# ../libiec61850/hal/inc/hal_ethernet.h: 34

# ../libiec61850/hal/inc/hal_ethernet.h: 37
class struct_sEthernetHandleSet(Structure):
    pass

EthernetHandleSet = POINTER(struct_sEthernetHandleSet)# ../libiec61850/hal/inc/hal_ethernet.h: 37

enum_anon_72 = c_int# ../libiec61850/hal/inc/hal_ethernet.h: 44

ETHERNET_SOCKET_MODE_PROMISC = 0# ../libiec61850/hal/inc/hal_ethernet.h: 44

ETHERNET_SOCKET_MODE_ALL_MULTICAST = (ETHERNET_SOCKET_MODE_PROMISC + 1)# ../libiec61850/hal/inc/hal_ethernet.h: 44

ETHERNET_SOCKET_MODE_MULTICAST = (ETHERNET_SOCKET_MODE_ALL_MULTICAST + 1)# ../libiec61850/hal/inc/hal_ethernet.h: 44

ETHERNET_SOCKET_MODE_HOST_ONLY = (ETHERNET_SOCKET_MODE_MULTICAST + 1)# ../libiec61850/hal/inc/hal_ethernet.h: 44

EthernetSocketMode = enum_anon_72# ../libiec61850/hal/inc/hal_ethernet.h: 44

# ../libiec61850/hal/inc/hal_ethernet.h: 52
if _libs["libiec61850.so"].has("EthernetHandleSet_new", "cdecl"):
    EthernetHandleSet_new = _libs["libiec61850.so"].get("EthernetHandleSet_new", "cdecl")
    EthernetHandleSet_new.argtypes = []
    EthernetHandleSet_new.restype = EthernetHandleSet

# ../libiec61850/hal/inc/hal_ethernet.h: 61
if _libs["libiec61850.so"].has("EthernetHandleSet_addSocket", "cdecl"):
    EthernetHandleSet_addSocket = _libs["libiec61850.so"].get("EthernetHandleSet_addSocket", "cdecl")
    EthernetHandleSet_addSocket.argtypes = [EthernetHandleSet, EthernetSocket]
    EthernetHandleSet_addSocket.restype = None

# ../libiec61850/hal/inc/hal_ethernet.h: 70
if _libs["libiec61850.so"].has("EthernetHandleSet_removeSocket", "cdecl"):
    EthernetHandleSet_removeSocket = _libs["libiec61850.so"].get("EthernetHandleSet_removeSocket", "cdecl")
    EthernetHandleSet_removeSocket.argtypes = [EthernetHandleSet, EthernetSocket]
    EthernetHandleSet_removeSocket.restype = None

# ../libiec61850/hal/inc/hal_ethernet.h: 85
if _libs["libiec61850.so"].has("EthernetHandleSet_waitReady", "cdecl"):
    EthernetHandleSet_waitReady = _libs["libiec61850.so"].get("EthernetHandleSet_waitReady", "cdecl")
    EthernetHandleSet_waitReady.argtypes = [EthernetHandleSet, c_uint]
    EthernetHandleSet_waitReady.restype = c_int

# ../libiec61850/hal/inc/hal_ethernet.h: 93
if _libs["libiec61850.so"].has("EthernetHandleSet_destroy", "cdecl"):
    EthernetHandleSet_destroy = _libs["libiec61850.so"].get("EthernetHandleSet_destroy", "cdecl")
    EthernetHandleSet_destroy.argtypes = [EthernetHandleSet]
    EthernetHandleSet_destroy.restype = None

# ../libiec61850/hal/inc/hal_ethernet.h: 104
if _libs["libiec61850.so"].has("Ethernet_getInterfaceMACAddress", "cdecl"):
    Ethernet_getInterfaceMACAddress = _libs["libiec61850.so"].get("Ethernet_getInterfaceMACAddress", "cdecl")
    Ethernet_getInterfaceMACAddress.argtypes = [String, POINTER(uint8_t)]
    Ethernet_getInterfaceMACAddress.restype = None

# ../libiec61850/hal/inc/hal_ethernet.h: 114
if _libs["libiec61850.so"].has("Ethernet_createSocket", "cdecl"):
    Ethernet_createSocket = _libs["libiec61850.so"].get("Ethernet_createSocket", "cdecl")
    Ethernet_createSocket.argtypes = [String, POINTER(uint8_t)]
    Ethernet_createSocket.restype = EthernetSocket

# ../libiec61850/hal/inc/hal_ethernet.h: 122
if _libs["libiec61850.so"].has("Ethernet_destroySocket", "cdecl"):
    Ethernet_destroySocket = _libs["libiec61850.so"].get("Ethernet_destroySocket", "cdecl")
    Ethernet_destroySocket.argtypes = [EthernetSocket]
    Ethernet_destroySocket.restype = None

# ../libiec61850/hal/inc/hal_ethernet.h: 125
if _libs["libiec61850.so"].has("Ethernet_sendPacket", "cdecl"):
    Ethernet_sendPacket = _libs["libiec61850.so"].get("Ethernet_sendPacket", "cdecl")
    Ethernet_sendPacket.argtypes = [EthernetSocket, POINTER(uint8_t), c_int]
    Ethernet_sendPacket.restype = None

# ../libiec61850/hal/inc/hal_ethernet.h: 137
if _libs["libiec61850.so"].has("Ethernet_setMode", "cdecl"):
    Ethernet_setMode = _libs["libiec61850.so"].get("Ethernet_setMode", "cdecl")
    Ethernet_setMode.argtypes = [EthernetSocket, EthernetSocketMode]
    Ethernet_setMode.restype = None

# ../libiec61850/hal/inc/hal_ethernet.h: 148
if _libs["libiec61850.so"].has("Ethernet_addMulticastAddress", "cdecl"):
    Ethernet_addMulticastAddress = _libs["libiec61850.so"].get("Ethernet_addMulticastAddress", "cdecl")
    Ethernet_addMulticastAddress.argtypes = [EthernetSocket, POINTER(uint8_t)]
    Ethernet_addMulticastAddress.restype = None

# ../libiec61850/hal/inc/hal_ethernet.h: 160
if _libs["libiec61850.so"].has("Ethernet_setProtocolFilter", "cdecl"):
    Ethernet_setProtocolFilter = _libs["libiec61850.so"].get("Ethernet_setProtocolFilter", "cdecl")
    Ethernet_setProtocolFilter.argtypes = [EthernetSocket, uint16_t]
    Ethernet_setProtocolFilter.restype = None

# ../libiec61850/hal/inc/hal_ethernet.h: 172
if _libs["libiec61850.so"].has("Ethernet_receivePacket", "cdecl"):
    Ethernet_receivePacket = _libs["libiec61850.so"].get("Ethernet_receivePacket", "cdecl")
    Ethernet_receivePacket.argtypes = [EthernetSocket, POINTER(uint8_t), c_int]
    Ethernet_receivePacket.restype = c_int

# ../libiec61850/hal/inc/hal_ethernet.h: 180
if _libs["libiec61850.so"].has("Ethernet_isSupported", "cdecl"):
    Ethernet_isSupported = _libs["libiec61850.so"].get("Ethernet_isSupported", "cdecl")
    Ethernet_isSupported.argtypes = []
    Ethernet_isSupported.restype = c_bool

enum_anon_73 = c_int# /home/user/libiec61850/src/goose/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_NO_ERROR = 0# /home/user/libiec61850/src/goose/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_UNKNOWN_TAG = (GOOSE_PARSE_ERROR_NO_ERROR + 1)# /home/user/libiec61850/src/goose/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_TAGDECODE = (GOOSE_PARSE_ERROR_UNKNOWN_TAG + 1)# /home/user/libiec61850/src/goose/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_SUBLEVEL = (GOOSE_PARSE_ERROR_TAGDECODE + 1)# /home/user/libiec61850/src/goose/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_OVERFLOW = (GOOSE_PARSE_ERROR_SUBLEVEL + 1)# /home/user/libiec61850/src/goose/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_UNDERFLOW = (GOOSE_PARSE_ERROR_OVERFLOW + 1)# /home/user/libiec61850/src/goose/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_TYPE_MISMATCH = (GOOSE_PARSE_ERROR_UNDERFLOW + 1)# /home/user/libiec61850/src/goose/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_LENGTH_MISMATCH = (GOOSE_PARSE_ERROR_TYPE_MISMATCH + 1)# /home/user/libiec61850/src/goose/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_INVALID_PADDING = (GOOSE_PARSE_ERROR_LENGTH_MISMATCH + 1)# /home/user/libiec61850/src/goose/goose_subscriber.h: 51

GooseParseError = enum_anon_73# /home/user/libiec61850/src/goose/goose_subscriber.h: 51

# /home/user/libiec61850/src/goose/goose_receiver_internal.h: 37
class struct_sGooseSubscriber(Structure):
    pass

GooseSubscriber = POINTER(struct_sGooseSubscriber)# /home/user/libiec61850/src/goose/goose_subscriber.h: 53

GooseListener = CFUNCTYPE(UNCHECKED(None), GooseSubscriber, POINTER(None))# /home/user/libiec61850/src/goose/goose_subscriber.h: 61

# /home/user/libiec61850/src/goose/goose_subscriber.h: 84
if _libs["libiec61850.so"].has("GooseSubscriber_create", "cdecl"):
    GooseSubscriber_create = _libs["libiec61850.so"].get("GooseSubscriber_create", "cdecl")
    GooseSubscriber_create.argtypes = [String, POINTER(MmsValue)]
    GooseSubscriber_create.restype = GooseSubscriber

# /home/user/libiec61850/src/goose/goose_subscriber.h: 91
if _libs["libiec61850.so"].has("GooseSubscriber_getGoId", "cdecl"):
    GooseSubscriber_getGoId = _libs["libiec61850.so"].get("GooseSubscriber_getGoId", "cdecl")
    GooseSubscriber_getGoId.argtypes = [GooseSubscriber]
    if sizeof(c_int) == sizeof(c_void_p):
        GooseSubscriber_getGoId.restype = ReturnString
    else:
        GooseSubscriber_getGoId.restype = String
        GooseSubscriber_getGoId.errcheck = ReturnString

# /home/user/libiec61850/src/goose/goose_subscriber.h: 99
if _libs["libiec61850.so"].has("GooseSubscriber_getGoCbRef", "cdecl"):
    GooseSubscriber_getGoCbRef = _libs["libiec61850.so"].get("GooseSubscriber_getGoCbRef", "cdecl")
    GooseSubscriber_getGoCbRef.argtypes = [GooseSubscriber]
    if sizeof(c_int) == sizeof(c_void_p):
        GooseSubscriber_getGoCbRef.restype = ReturnString
    else:
        GooseSubscriber_getGoCbRef.restype = String
        GooseSubscriber_getGoCbRef.errcheck = ReturnString

# /home/user/libiec61850/src/goose/goose_subscriber.h: 107
if _libs["libiec61850.so"].has("GooseSubscriber_getDataSet", "cdecl"):
    GooseSubscriber_getDataSet = _libs["libiec61850.so"].get("GooseSubscriber_getDataSet", "cdecl")
    GooseSubscriber_getDataSet.argtypes = [GooseSubscriber]
    if sizeof(c_int) == sizeof(c_void_p):
        GooseSubscriber_getDataSet.restype = ReturnString
    else:
        GooseSubscriber_getDataSet.restype = String
        GooseSubscriber_getDataSet.errcheck = ReturnString

# /home/user/libiec61850/src/goose/goose_subscriber.h: 119
if _libs["libiec61850.so"].has("GooseSubscriber_setDstMac", "cdecl"):
    GooseSubscriber_setDstMac = _libs["libiec61850.so"].get("GooseSubscriber_setDstMac", "cdecl")
    GooseSubscriber_setDstMac.argtypes = [GooseSubscriber, uint8_t * int(6)]
    GooseSubscriber_setDstMac.restype = None

# /home/user/libiec61850/src/goose/goose_subscriber.h: 130
if _libs["libiec61850.so"].has("GooseSubscriber_setAppId", "cdecl"):
    GooseSubscriber_setAppId = _libs["libiec61850.so"].get("GooseSubscriber_setAppId", "cdecl")
    GooseSubscriber_setAppId.argtypes = [GooseSubscriber, uint16_t]
    GooseSubscriber_setAppId.restype = None

# /home/user/libiec61850/src/goose/goose_subscriber.h: 140
if _libs["libiec61850.so"].has("GooseSubscriber_isValid", "cdecl"):
    GooseSubscriber_isValid = _libs["libiec61850.so"].get("GooseSubscriber_isValid", "cdecl")
    GooseSubscriber_isValid.argtypes = [GooseSubscriber]
    GooseSubscriber_isValid.restype = c_bool

# /home/user/libiec61850/src/goose/goose_subscriber.h: 150
if _libs["libiec61850.so"].has("GooseSubscriber_getParseError", "cdecl"):
    GooseSubscriber_getParseError = _libs["libiec61850.so"].get("GooseSubscriber_getParseError", "cdecl")
    GooseSubscriber_getParseError.argtypes = [GooseSubscriber]
    GooseSubscriber_getParseError.restype = GooseParseError

# /home/user/libiec61850/src/goose/goose_subscriber.h: 161
if _libs["libiec61850.so"].has("GooseSubscriber_destroy", "cdecl"):
    GooseSubscriber_destroy = _libs["libiec61850.so"].get("GooseSubscriber_destroy", "cdecl")
    GooseSubscriber_destroy.argtypes = [GooseSubscriber]
    GooseSubscriber_destroy.restype = None

# /home/user/libiec61850/src/goose/goose_subscriber.h: 171
if _libs["libiec61850.so"].has("GooseSubscriber_setListener", "cdecl"):
    GooseSubscriber_setListener = _libs["libiec61850.so"].get("GooseSubscriber_setListener", "cdecl")
    GooseSubscriber_setListener.argtypes = [GooseSubscriber, GooseListener, POINTER(None)]
    GooseSubscriber_setListener.restype = None

# /home/user/libiec61850/src/goose/goose_subscriber.h: 179
if _libs["libiec61850.so"].has("GooseSubscriber_getAppId", "cdecl"):
    GooseSubscriber_getAppId = _libs["libiec61850.so"].get("GooseSubscriber_getAppId", "cdecl")
    GooseSubscriber_getAppId.argtypes = [GooseSubscriber]
    GooseSubscriber_getAppId.restype = c_int32

# /home/user/libiec61850/src/goose/goose_subscriber.h: 188
if _libs["libiec61850.so"].has("GooseSubscriber_getSrcMac", "cdecl"):
    GooseSubscriber_getSrcMac = _libs["libiec61850.so"].get("GooseSubscriber_getSrcMac", "cdecl")
    GooseSubscriber_getSrcMac.argtypes = [GooseSubscriber, POINTER(uint8_t)]
    GooseSubscriber_getSrcMac.restype = None

# /home/user/libiec61850/src/goose/goose_subscriber.h: 197
if _libs["libiec61850.so"].has("GooseSubscriber_getDstMac", "cdecl"):
    GooseSubscriber_getDstMac = _libs["libiec61850.so"].get("GooseSubscriber_getDstMac", "cdecl")
    GooseSubscriber_getDstMac.argtypes = [GooseSubscriber, POINTER(uint8_t)]
    GooseSubscriber_getDstMac.restype = None

# /home/user/libiec61850/src/goose/goose_subscriber.h: 209
if _libs["libiec61850.so"].has("GooseSubscriber_getStNum", "cdecl"):
    GooseSubscriber_getStNum = _libs["libiec61850.so"].get("GooseSubscriber_getStNum", "cdecl")
    GooseSubscriber_getStNum.argtypes = [GooseSubscriber]
    GooseSubscriber_getStNum.restype = uint32_t

# /home/user/libiec61850/src/goose/goose_subscriber.h: 222
if _libs["libiec61850.so"].has("GooseSubscriber_getSqNum", "cdecl"):
    GooseSubscriber_getSqNum = _libs["libiec61850.so"].get("GooseSubscriber_getSqNum", "cdecl")
    GooseSubscriber_getSqNum.argtypes = [GooseSubscriber]
    GooseSubscriber_getSqNum.restype = uint32_t

# /home/user/libiec61850/src/goose/goose_subscriber.h: 234
if _libs["libiec61850.so"].has("GooseSubscriber_isTest", "cdecl"):
    GooseSubscriber_isTest = _libs["libiec61850.so"].get("GooseSubscriber_isTest", "cdecl")
    GooseSubscriber_isTest.argtypes = [GooseSubscriber]
    GooseSubscriber_isTest.restype = c_bool

# /home/user/libiec61850/src/goose/goose_subscriber.h: 245
if _libs["libiec61850.so"].has("GooseSubscriber_getConfRev", "cdecl"):
    GooseSubscriber_getConfRev = _libs["libiec61850.so"].get("GooseSubscriber_getConfRev", "cdecl")
    GooseSubscriber_getConfRev.argtypes = [GooseSubscriber]
    GooseSubscriber_getConfRev.restype = uint32_t

# /home/user/libiec61850/src/goose/goose_subscriber.h: 258
if _libs["libiec61850.so"].has("GooseSubscriber_needsCommission", "cdecl"):
    GooseSubscriber_needsCommission = _libs["libiec61850.so"].get("GooseSubscriber_needsCommission", "cdecl")
    GooseSubscriber_needsCommission.argtypes = [GooseSubscriber]
    GooseSubscriber_needsCommission.restype = c_bool

# /home/user/libiec61850/src/goose/goose_subscriber.h: 268
if _libs["libiec61850.so"].has("GooseSubscriber_getTimeAllowedToLive", "cdecl"):
    GooseSubscriber_getTimeAllowedToLive = _libs["libiec61850.so"].get("GooseSubscriber_getTimeAllowedToLive", "cdecl")
    GooseSubscriber_getTimeAllowedToLive.argtypes = [GooseSubscriber]
    GooseSubscriber_getTimeAllowedToLive.restype = uint32_t

# /home/user/libiec61850/src/goose/goose_subscriber.h: 278
if _libs["libiec61850.so"].has("GooseSubscriber_getTimestamp", "cdecl"):
    GooseSubscriber_getTimestamp = _libs["libiec61850.so"].get("GooseSubscriber_getTimestamp", "cdecl")
    GooseSubscriber_getTimestamp.argtypes = [GooseSubscriber]
    GooseSubscriber_getTimestamp.restype = uint64_t

# /home/user/libiec61850/src/goose/goose_subscriber.h: 291
if _libs["libiec61850.so"].has("GooseSubscriber_getDataSetValues", "cdecl"):
    GooseSubscriber_getDataSetValues = _libs["libiec61850.so"].get("GooseSubscriber_getDataSetValues", "cdecl")
    GooseSubscriber_getDataSetValues.argtypes = [GooseSubscriber]
    GooseSubscriber_getDataSetValues.restype = POINTER(MmsValue)

# /home/user/libiec61850/src/goose/goose_subscriber.h: 295
if _libs["libiec61850.so"].has("GooseSubscriber_isVlanSet", "cdecl"):
    GooseSubscriber_isVlanSet = _libs["libiec61850.so"].get("GooseSubscriber_isVlanSet", "cdecl")
    GooseSubscriber_isVlanSet.argtypes = [GooseSubscriber]
    GooseSubscriber_isVlanSet.restype = c_bool

# /home/user/libiec61850/src/goose/goose_subscriber.h: 298
if _libs["libiec61850.so"].has("GooseSubscriber_getVlanId", "cdecl"):
    GooseSubscriber_getVlanId = _libs["libiec61850.so"].get("GooseSubscriber_getVlanId", "cdecl")
    GooseSubscriber_getVlanId.argtypes = [GooseSubscriber]
    GooseSubscriber_getVlanId.restype = uint16_t

# /home/user/libiec61850/src/goose/goose_subscriber.h: 301
if _libs["libiec61850.so"].has("GooseSubscriber_getVlanPrio", "cdecl"):
    GooseSubscriber_getVlanPrio = _libs["libiec61850.so"].get("GooseSubscriber_getVlanPrio", "cdecl")
    GooseSubscriber_getVlanPrio.argtypes = [GooseSubscriber]
    GooseSubscriber_getVlanPrio.restype = uint8_t

# /home/user/libiec61850/src/goose/goose_subscriber.h: 310
if _libs["libiec61850.so"].has("GooseSubscriber_setObserver", "cdecl"):
    GooseSubscriber_setObserver = _libs["libiec61850.so"].get("GooseSubscriber_setObserver", "cdecl")
    GooseSubscriber_setObserver.argtypes = [GooseSubscriber]
    GooseSubscriber_setObserver.restype = None

# /home/user/libiec61850/src/goose/goose_receiver.h: 42
class struct_sGooseReceiver(Structure):
    pass

GooseReceiver = POINTER(struct_sGooseReceiver)# /home/user/libiec61850/src/goose/goose_receiver.h: 42

# /home/user/libiec61850/src/goose/goose_receiver.h: 53
if _libs["libiec61850.so"].has("GooseReceiver_create", "cdecl"):
    GooseReceiver_create = _libs["libiec61850.so"].get("GooseReceiver_create", "cdecl")
    GooseReceiver_create.argtypes = []
    GooseReceiver_create.restype = GooseReceiver

# /home/user/libiec61850/src/goose/goose_receiver.h: 66
if _libs["libiec61850.so"].has("GooseReceiver_createEx", "cdecl"):
    GooseReceiver_createEx = _libs["libiec61850.so"].get("GooseReceiver_createEx", "cdecl")
    GooseReceiver_createEx.argtypes = [POINTER(uint8_t)]
    GooseReceiver_createEx.restype = GooseReceiver

# /home/user/libiec61850/src/goose/goose_receiver.h: 76
for _lib in _libs.values():
    if not _lib.has("GooseReceiver_createRemote", "cdecl"):
        continue
    GooseReceiver_createRemote = _lib.get("GooseReceiver_createRemote", "cdecl")
    GooseReceiver_createRemote.argtypes = [RSession]
    GooseReceiver_createRemote.restype = GooseReceiver
    break

# /home/user/libiec61850/src/goose/goose_receiver.h: 85
if _libs["libiec61850.so"].has("GooseReceiver_setInterfaceId", "cdecl"):
    GooseReceiver_setInterfaceId = _libs["libiec61850.so"].get("GooseReceiver_setInterfaceId", "cdecl")
    GooseReceiver_setInterfaceId.argtypes = [GooseReceiver, String]
    GooseReceiver_setInterfaceId.restype = None

# /home/user/libiec61850/src/goose/goose_receiver.h: 94
if _libs["libiec61850.so"].has("GooseReceiver_getInterfaceId", "cdecl"):
    GooseReceiver_getInterfaceId = _libs["libiec61850.so"].get("GooseReceiver_getInterfaceId", "cdecl")
    GooseReceiver_getInterfaceId.argtypes = [GooseReceiver]
    GooseReceiver_getInterfaceId.restype = c_char_p

# /home/user/libiec61850/src/goose/goose_receiver.h: 107
if _libs["libiec61850.so"].has("GooseReceiver_addSubscriber", "cdecl"):
    GooseReceiver_addSubscriber = _libs["libiec61850.so"].get("GooseReceiver_addSubscriber", "cdecl")
    GooseReceiver_addSubscriber.argtypes = [GooseReceiver, GooseSubscriber]
    GooseReceiver_addSubscriber.restype = None

# /home/user/libiec61850/src/goose/goose_receiver.h: 119
if _libs["libiec61850.so"].has("GooseReceiver_removeSubscriber", "cdecl"):
    GooseReceiver_removeSubscriber = _libs["libiec61850.so"].get("GooseReceiver_removeSubscriber", "cdecl")
    GooseReceiver_removeSubscriber.argtypes = [GooseReceiver, GooseSubscriber]
    GooseReceiver_removeSubscriber.restype = None

# /home/user/libiec61850/src/goose/goose_receiver.h: 127
if _libs["libiec61850.so"].has("GooseReceiver_start", "cdecl"):
    GooseReceiver_start = _libs["libiec61850.so"].get("GooseReceiver_start", "cdecl")
    GooseReceiver_start.argtypes = [GooseReceiver]
    GooseReceiver_start.restype = None

# /home/user/libiec61850/src/goose/goose_receiver.h: 137
if _libs["libiec61850.so"].has("GooseReceiver_stop", "cdecl"):
    GooseReceiver_stop = _libs["libiec61850.so"].get("GooseReceiver_stop", "cdecl")
    GooseReceiver_stop.argtypes = [GooseReceiver]
    GooseReceiver_stop.restype = None

# /home/user/libiec61850/src/goose/goose_receiver.h: 149
if _libs["libiec61850.so"].has("GooseReceiver_isRunning", "cdecl"):
    GooseReceiver_isRunning = _libs["libiec61850.so"].get("GooseReceiver_isRunning", "cdecl")
    GooseReceiver_isRunning.argtypes = [GooseReceiver]
    GooseReceiver_isRunning.restype = c_bool

# /home/user/libiec61850/src/goose/goose_receiver.h: 157
if _libs["libiec61850.so"].has("GooseReceiver_destroy", "cdecl"):
    GooseReceiver_destroy = _libs["libiec61850.so"].get("GooseReceiver_destroy", "cdecl")
    GooseReceiver_destroy.argtypes = [GooseReceiver]
    GooseReceiver_destroy.restype = None

# /home/user/libiec61850/src/goose/goose_receiver.h: 163
if _libs["libiec61850.so"].has("GooseReceiver_startThreadless", "cdecl"):
    GooseReceiver_startThreadless = _libs["libiec61850.so"].get("GooseReceiver_startThreadless", "cdecl")
    GooseReceiver_startThreadless.argtypes = [GooseReceiver]
    GooseReceiver_startThreadless.restype = EthernetSocket

# /home/user/libiec61850/src/goose/goose_receiver.h: 166
if _libs["libiec61850.so"].has("GooseReceiver_stopThreadless", "cdecl"):
    GooseReceiver_stopThreadless = _libs["libiec61850.so"].get("GooseReceiver_stopThreadless", "cdecl")
    GooseReceiver_stopThreadless.argtypes = [GooseReceiver]
    GooseReceiver_stopThreadless.restype = None

# /home/user/libiec61850/src/goose/goose_receiver.h: 178
if _libs["libiec61850.so"].has("GooseReceiver_tick", "cdecl"):
    GooseReceiver_tick = _libs["libiec61850.so"].get("GooseReceiver_tick", "cdecl")
    GooseReceiver_tick.argtypes = [GooseReceiver]
    GooseReceiver_tick.restype = c_bool

# /home/user/libiec61850/src/goose/goose_receiver.h: 191
if _libs["libiec61850.so"].has("GooseReceiver_handleMessage", "cdecl"):
    GooseReceiver_handleMessage = _libs["libiec61850.so"].get("GooseReceiver_handleMessage", "cdecl")
    GooseReceiver_handleMessage.argtypes = [GooseReceiver, POINTER(uint8_t), c_int]
    GooseReceiver_handleMessage.restype = None

struct_sGooseSubscriber.__slots__ = [
    'goCBRef',
    'datSet',
    'goId',
    'goCBRefLen',
    'timeAllowedToLive',
    'stNum',
    'sqNum',
    'confRev',
    'timestamp',
    'simulation',
    'ndsCom',
    'invalidityTime',
    'stateValid',
    'parseError',
    'srcMac',
    'dstMac',
    'appId',
    'dataSetValues',
    'dataSetValuesSelfAllocated',
    'dstMacSet',
    'isObserver',
    'vlanSet',
    'vlanId',
    'vlanPrio',
    'listener',
    'listenerParameter',
]
struct_sGooseSubscriber._fields_ = [
    ('goCBRef', c_char * int(130)),
    ('datSet', c_char * int(130)),
    ('goId', c_char * int(130)),
    ('goCBRefLen', c_int),
    ('timeAllowedToLive', uint32_t),
    ('stNum', uint32_t),
    ('sqNum', uint32_t),
    ('confRev', uint32_t),
    ('timestamp', POINTER(MmsValue)),
    ('simulation', c_bool),
    ('ndsCom', c_bool),
    ('invalidityTime', uint64_t),
    ('stateValid', c_bool),
    ('parseError', GooseParseError),
    ('srcMac', uint8_t * int(6)),
    ('dstMac', uint8_t * int(6)),
    ('appId', c_int32),
    ('dataSetValues', POINTER(MmsValue)),
    ('dataSetValuesSelfAllocated', c_bool),
    ('dstMacSet', c_bool),
    ('isObserver', c_bool),
    ('vlanSet', c_bool),
    ('vlanId', uint16_t),
    ('vlanPrio', uint8_t),
    ('listener', GooseListener),
    ('listenerParameter', POINTER(None)),
]

# /home/user/libiec61850/src/r_session/r_session_crypto.h: 33
for _lib in _libs.values():
    if not _lib.has("RSessionCrypto_createHMAC", "cdecl"):
        continue
    RSessionCrypto_createHMAC = _lib.get("RSessionCrypto_createHMAC", "cdecl")
    RSessionCrypto_createHMAC.argtypes = [POINTER(uint8_t), c_int, POINTER(uint8_t), c_int, POINTER(uint8_t), c_int]
    RSessionCrypto_createHMAC.restype = c_bool
    break

# /home/user/libiec61850/src/r_session/r_session_crypto.h: 36
for _lib in _libs.values():
    if not _lib.has("RSessionCrypto_gcmEncryptAndTag", "cdecl"):
        continue
    RSessionCrypto_gcmEncryptAndTag = _lib.get("RSessionCrypto_gcmEncryptAndTag", "cdecl")
    RSessionCrypto_gcmEncryptAndTag.argtypes = [POINTER(uint8_t), c_int, POINTER(uint8_t), c_int, POINTER(uint8_t), c_int, POINTER(uint8_t), c_int, POINTER(uint8_t), c_int]
    RSessionCrypto_gcmEncryptAndTag.restype = c_bool
    break

# /home/user/libiec61850/src/r_session/r_session_crypto.h: 39
for _lib in _libs.values():
    if not _lib.has("RSessionCrypto_gcmAuthAndDecrypt", "cdecl"):
        continue
    RSessionCrypto_gcmAuthAndDecrypt = _lib.get("RSessionCrypto_gcmAuthAndDecrypt", "cdecl")
    RSessionCrypto_gcmAuthAndDecrypt.argtypes = [POINTER(uint8_t), c_int, POINTER(uint8_t), c_int, POINTER(uint8_t), c_int, POINTER(uint8_t), c_int, POINTER(uint8_t), POINTER(uint8_t), c_int]
    RSessionCrypto_gcmAuthAndDecrypt.restype = c_bool
    break

# /home/user/libiec61850/src/r_session/r_session_crypto.h: 42
for _lib in _libs.values():
    if not _lib.has("RSessionCrypto_createRandomData", "cdecl"):
        continue
    RSessionCrypto_createRandomData = _lib.get("RSessionCrypto_createRandomData", "cdecl")
    RSessionCrypto_createRandomData.argtypes = [POINTER(uint8_t), c_int]
    RSessionCrypto_createRandomData.restype = c_bool
    break

# /home/user/libiec61850/src/r_session/r_session_internal.h: 30
for _lib in _libs.values():
    if not _lib.has("RSession_getSocket", "cdecl"):
        continue
    RSession_getSocket = _lib.get("RSession_getSocket", "cdecl")
    RSession_getSocket.argtypes = [RSession]
    RSession_getSocket.restype = Socket
    break

enum_anon_74 = c_int# /home/user/libiec61850/src/r_session/r_session_internal.h: 37

RSESSION_SPDU_ID_TUNNELED = 0xa0# /home/user/libiec61850/src/r_session/r_session_internal.h: 37

RSESSION_SPDU_ID_GOOSE = 0xa1# /home/user/libiec61850/src/r_session/r_session_internal.h: 37

RSESSION_SPDU_ID_SV = 0xa2# /home/user/libiec61850/src/r_session/r_session_internal.h: 37

RSESSION_SPDU_ID_MGMT = 0xa3# /home/user/libiec61850/src/r_session/r_session_internal.h: 37

RSessionProtocol_SPDU_ID = enum_anon_74# /home/user/libiec61850/src/r_session/r_session_internal.h: 37

# /home/user/libiec61850/src/r_session/r_session_internal.h: 45
for _lib in _libs.values():
    if not _lib.has("RSession_sendMessage", "cdecl"):
        continue
    RSession_sendMessage = _lib.get("RSession_sendMessage", "cdecl")
    RSession_sendMessage.argtypes = [RSession, RSessionProtocol_SPDU_ID, c_bool, uint16_t, POINTER(uint8_t), c_int]
    RSession_sendMessage.restype = RSessionError
    break

RSessionPayloadElementHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), uint16_t, POINTER(uint8_t), c_int)# /home/user/libiec61850/src/r_session/r_session_internal.h: 50

# /home/user/libiec61850/src/r_session/r_session_internal.h: 53
for _lib in _libs.values():
    if not _lib.has("RSession_receiveMessage", "cdecl"):
        continue
    RSession_receiveMessage = _lib.get("RSession_receiveMessage", "cdecl")
    RSession_receiveMessage.argtypes = [RSession, RSessionPayloadElementHandler, POINTER(None)]
    RSession_receiveMessage.restype = RSessionError
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 63
class struct_sSVPublisher(Structure):
    pass

SVPublisher = POINTER(struct_sSVPublisher)# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 63

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 68
class struct_sSVPublisher_ASDU(Structure):
    pass

SVPublisher_ASDU = POINTER(struct_sSVPublisher_ASDU)# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 68

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 81
if _libs["libiec61850.so"].has("SVPublisher_create", "cdecl"):
    SVPublisher_create = _libs["libiec61850.so"].get("SVPublisher_create", "cdecl")
    SVPublisher_create.argtypes = [POINTER(CommParameters), String]
    SVPublisher_create.restype = SVPublisher

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 92
if _libs["libiec61850.so"].has("SVPublisher_createEx", "cdecl"):
    SVPublisher_createEx = _libs["libiec61850.so"].get("SVPublisher_createEx", "cdecl")
    SVPublisher_createEx.argtypes = [POINTER(CommParameters), String, c_bool]
    SVPublisher_createEx.restype = SVPublisher

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 103
for _lib in _libs.values():
    if not _lib.has("SVPublisher_createRemote", "cdecl"):
        continue
    SVPublisher_createRemote = _lib.get("SVPublisher_createRemote", "cdecl")
    SVPublisher_createRemote.argtypes = [RSession, uint16_t]
    SVPublisher_createRemote.restype = SVPublisher
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 114
if _libs["libiec61850.so"].has("SVPublisher_addASDU", "cdecl"):
    SVPublisher_addASDU = _libs["libiec61850.so"].get("SVPublisher_addASDU", "cdecl")
    SVPublisher_addASDU.argtypes = [SVPublisher, String, String, uint32_t]
    SVPublisher_addASDU.restype = SVPublisher_ASDU

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 124
if _libs["libiec61850.so"].has("SVPublisher_setupComplete", "cdecl"):
    SVPublisher_setupComplete = _libs["libiec61850.so"].get("SVPublisher_setupComplete", "cdecl")
    SVPublisher_setupComplete.argtypes = [SVPublisher]
    SVPublisher_setupComplete.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 132
if _libs["libiec61850.so"].has("SVPublisher_publish", "cdecl"):
    SVPublisher_publish = _libs["libiec61850.so"].get("SVPublisher_publish", "cdecl")
    SVPublisher_publish.argtypes = [SVPublisher]
    SVPublisher_publish.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 140
if _libs["libiec61850.so"].has("SVPublisher_destroy", "cdecl"):
    SVPublisher_destroy = _libs["libiec61850.so"].get("SVPublisher_destroy", "cdecl")
    SVPublisher_destroy.argtypes = [SVPublisher]
    SVPublisher_destroy.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 156
if _libs["libiec61850.so"].has("SVPublisher_ASDU_resetBuffer", "cdecl"):
    SVPublisher_ASDU_resetBuffer = _libs["libiec61850.so"].get("SVPublisher_ASDU_resetBuffer", "cdecl")
    SVPublisher_ASDU_resetBuffer.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_resetBuffer.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 165
if _libs["libiec61850.so"].has("SVPublisher_ASDU_addINT8", "cdecl"):
    SVPublisher_ASDU_addINT8 = _libs["libiec61850.so"].get("SVPublisher_ASDU_addINT8", "cdecl")
    SVPublisher_ASDU_addINT8.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_addINT8.restype = c_int

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 175
if _libs["libiec61850.so"].has("SVPublisher_ASDU_setINT8", "cdecl"):
    SVPublisher_ASDU_setINT8 = _libs["libiec61850.so"].get("SVPublisher_ASDU_setINT8", "cdecl")
    SVPublisher_ASDU_setINT8.argtypes = [SVPublisher_ASDU, c_int, c_int8]
    SVPublisher_ASDU_setINT8.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 184
if _libs["libiec61850.so"].has("SVPublisher_ASDU_addINT32", "cdecl"):
    SVPublisher_ASDU_addINT32 = _libs["libiec61850.so"].get("SVPublisher_ASDU_addINT32", "cdecl")
    SVPublisher_ASDU_addINT32.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_addINT32.restype = c_int

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 194
if _libs["libiec61850.so"].has("SVPublisher_ASDU_setINT32", "cdecl"):
    SVPublisher_ASDU_setINT32 = _libs["libiec61850.so"].get("SVPublisher_ASDU_setINT32", "cdecl")
    SVPublisher_ASDU_setINT32.argtypes = [SVPublisher_ASDU, c_int, c_int32]
    SVPublisher_ASDU_setINT32.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 203
if _libs["libiec61850.so"].has("SVPublisher_ASDU_addINT64", "cdecl"):
    SVPublisher_ASDU_addINT64 = _libs["libiec61850.so"].get("SVPublisher_ASDU_addINT64", "cdecl")
    SVPublisher_ASDU_addINT64.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_addINT64.restype = c_int

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 213
if _libs["libiec61850.so"].has("SVPublisher_ASDU_setINT64", "cdecl"):
    SVPublisher_ASDU_setINT64 = _libs["libiec61850.so"].get("SVPublisher_ASDU_setINT64", "cdecl")
    SVPublisher_ASDU_setINT64.argtypes = [SVPublisher_ASDU, c_int, c_int64]
    SVPublisher_ASDU_setINT64.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 222
if _libs["libiec61850.so"].has("SVPublisher_ASDU_addFLOAT", "cdecl"):
    SVPublisher_ASDU_addFLOAT = _libs["libiec61850.so"].get("SVPublisher_ASDU_addFLOAT", "cdecl")
    SVPublisher_ASDU_addFLOAT.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_addFLOAT.restype = c_int

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 232
if _libs["libiec61850.so"].has("SVPublisher_ASDU_setFLOAT", "cdecl"):
    SVPublisher_ASDU_setFLOAT = _libs["libiec61850.so"].get("SVPublisher_ASDU_setFLOAT", "cdecl")
    SVPublisher_ASDU_setFLOAT.argtypes = [SVPublisher_ASDU, c_int, c_float]
    SVPublisher_ASDU_setFLOAT.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 241
if _libs["libiec61850.so"].has("SVPublisher_ASDU_addFLOAT64", "cdecl"):
    SVPublisher_ASDU_addFLOAT64 = _libs["libiec61850.so"].get("SVPublisher_ASDU_addFLOAT64", "cdecl")
    SVPublisher_ASDU_addFLOAT64.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_addFLOAT64.restype = c_int

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 251
if _libs["libiec61850.so"].has("SVPublisher_ASDU_setFLOAT64", "cdecl"):
    SVPublisher_ASDU_setFLOAT64 = _libs["libiec61850.so"].get("SVPublisher_ASDU_setFLOAT64", "cdecl")
    SVPublisher_ASDU_setFLOAT64.argtypes = [SVPublisher_ASDU, c_int, c_double]
    SVPublisher_ASDU_setFLOAT64.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 260
if _libs["libiec61850.so"].has("SVPublisher_ASDU_addTimestamp", "cdecl"):
    SVPublisher_ASDU_addTimestamp = _libs["libiec61850.so"].get("SVPublisher_ASDU_addTimestamp", "cdecl")
    SVPublisher_ASDU_addTimestamp.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_addTimestamp.restype = c_int

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 270
if _libs["libiec61850.so"].has("SVPublisher_ASDU_setTimestamp", "cdecl"):
    SVPublisher_ASDU_setTimestamp = _libs["libiec61850.so"].get("SVPublisher_ASDU_setTimestamp", "cdecl")
    SVPublisher_ASDU_setTimestamp.argtypes = [SVPublisher_ASDU, c_int, Timestamp]
    SVPublisher_ASDU_setTimestamp.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 281
if _libs["libiec61850.so"].has("SVPublisher_ASDU_addQuality", "cdecl"):
    SVPublisher_ASDU_addQuality = _libs["libiec61850.so"].get("SVPublisher_ASDU_addQuality", "cdecl")
    SVPublisher_ASDU_addQuality.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_addQuality.restype = c_int

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 291
if _libs["libiec61850.so"].has("SVPublisher_ASDU_setQuality", "cdecl"):
    SVPublisher_ASDU_setQuality = _libs["libiec61850.so"].get("SVPublisher_ASDU_setQuality", "cdecl")
    SVPublisher_ASDU_setQuality.argtypes = [SVPublisher_ASDU, c_int, Quality]
    SVPublisher_ASDU_setQuality.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 300
if _libs["libiec61850.so"].has("SVPublisher_ASDU_setSmpCnt", "cdecl"):
    SVPublisher_ASDU_setSmpCnt = _libs["libiec61850.so"].get("SVPublisher_ASDU_setSmpCnt", "cdecl")
    SVPublisher_ASDU_setSmpCnt.argtypes = [SVPublisher_ASDU, uint16_t]
    SVPublisher_ASDU_setSmpCnt.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 308
if _libs["libiec61850.so"].has("SVPublisher_ASDU_getSmpCnt", "cdecl"):
    SVPublisher_ASDU_getSmpCnt = _libs["libiec61850.so"].get("SVPublisher_ASDU_getSmpCnt", "cdecl")
    SVPublisher_ASDU_getSmpCnt.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_getSmpCnt.restype = uint16_t

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 320
if _libs["libiec61850.so"].has("SVPublisher_ASDU_increaseSmpCnt", "cdecl"):
    SVPublisher_ASDU_increaseSmpCnt = _libs["libiec61850.so"].get("SVPublisher_ASDU_increaseSmpCnt", "cdecl")
    SVPublisher_ASDU_increaseSmpCnt.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_increaseSmpCnt.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 330
if _libs["libiec61850.so"].has("SVPublisher_ASDU_setSmpCntWrap", "cdecl"):
    SVPublisher_ASDU_setSmpCntWrap = _libs["libiec61850.so"].get("SVPublisher_ASDU_setSmpCntWrap", "cdecl")
    SVPublisher_ASDU_setSmpCntWrap.argtypes = [SVPublisher_ASDU, uint16_t]
    SVPublisher_ASDU_setSmpCntWrap.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 340
if _libs["libiec61850.so"].has("SVPublisher_ASDU_enableRefrTm", "cdecl"):
    SVPublisher_ASDU_enableRefrTm = _libs["libiec61850.so"].get("SVPublisher_ASDU_enableRefrTm", "cdecl")
    SVPublisher_ASDU_enableRefrTm.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_enableRefrTm.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 349
if _libs["libiec61850.so"].has("SVPublisher_ASDU_setRefrTmNs", "cdecl"):
    SVPublisher_ASDU_setRefrTmNs = _libs["libiec61850.so"].get("SVPublisher_ASDU_setRefrTmNs", "cdecl")
    SVPublisher_ASDU_setRefrTmNs.argtypes = [SVPublisher_ASDU, nsSinceEpoch]
    SVPublisher_ASDU_setRefrTmNs.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 358
if _libs["libiec61850.so"].has("SVPublisher_ASDU_setRefrTm", "cdecl"):
    SVPublisher_ASDU_setRefrTm = _libs["libiec61850.so"].get("SVPublisher_ASDU_setRefrTm", "cdecl")
    SVPublisher_ASDU_setRefrTm.argtypes = [SVPublisher_ASDU, msSinceEpoch]
    SVPublisher_ASDU_setRefrTm.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 370
if _libs["libiec61850.so"].has("SVPublisher_ASDU_setRefrTmByTimestamp", "cdecl"):
    SVPublisher_ASDU_setRefrTmByTimestamp = _libs["libiec61850.so"].get("SVPublisher_ASDU_setRefrTmByTimestamp", "cdecl")
    SVPublisher_ASDU_setRefrTmByTimestamp.argtypes = [SVPublisher_ASDU, POINTER(Timestamp)]
    SVPublisher_ASDU_setRefrTmByTimestamp.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 384
if _libs["libiec61850.so"].has("SVPublisher_ASDU_setSmpMod", "cdecl"):
    SVPublisher_ASDU_setSmpMod = _libs["libiec61850.so"].get("SVPublisher_ASDU_setSmpMod", "cdecl")
    SVPublisher_ASDU_setSmpMod.argtypes = [SVPublisher_ASDU, uint8_t]
    SVPublisher_ASDU_setSmpMod.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 398
if _libs["libiec61850.so"].has("SVPublisher_ASDU_setSmpRate", "cdecl"):
    SVPublisher_ASDU_setSmpRate = _libs["libiec61850.so"].get("SVPublisher_ASDU_setSmpRate", "cdecl")
    SVPublisher_ASDU_setSmpRate.argtypes = [SVPublisher_ASDU, uint16_t]
    SVPublisher_ASDU_setSmpRate.restype = None

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 415
if _libs["libiec61850.so"].has("SVPublisher_ASDU_setSmpSynch", "cdecl"):
    SVPublisher_ASDU_setSmpSynch = _libs["libiec61850.so"].get("SVPublisher_ASDU_setSmpSynch", "cdecl")
    SVPublisher_ASDU_setSmpSynch.argtypes = [SVPublisher_ASDU, uint16_t]
    SVPublisher_ASDU_setSmpSynch.restype = None

SampledValuesPublisher = POINTER(struct_sSVPublisher)# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 434

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 436
class struct_sSV_ASDU(Structure):
    pass

SV_ASDU = POINTER(struct_sSV_ASDU)# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 436

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 439
for _lib in _libs.values():
    if not _lib.has("SampledValuesPublisher_create", "cdecl"):
        continue
    SampledValuesPublisher_create = _lib.get("SampledValuesPublisher_create", "cdecl")
    SampledValuesPublisher_create.argtypes = [POINTER(CommParameters), String]
    SampledValuesPublisher_create.restype = SVPublisher
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 442
for _lib in _libs.values():
    if not _lib.has("SampledValuesPublisher_addASDU", "cdecl"):
        continue
    SampledValuesPublisher_addASDU = _lib.get("SampledValuesPublisher_addASDU", "cdecl")
    SampledValuesPublisher_addASDU.argtypes = [SVPublisher, String, String, uint32_t]
    SampledValuesPublisher_addASDU.restype = SVPublisher_ASDU
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 445
for _lib in _libs.values():
    if not _lib.has("SampledValuesPublisher_setupComplete", "cdecl"):
        continue
    SampledValuesPublisher_setupComplete = _lib.get("SampledValuesPublisher_setupComplete", "cdecl")
    SampledValuesPublisher_setupComplete.argtypes = [SVPublisher]
    SampledValuesPublisher_setupComplete.restype = None
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 448
for _lib in _libs.values():
    if not _lib.has("SampledValuesPublisher_publish", "cdecl"):
        continue
    SampledValuesPublisher_publish = _lib.get("SampledValuesPublisher_publish", "cdecl")
    SampledValuesPublisher_publish.argtypes = [SVPublisher]
    SampledValuesPublisher_publish.restype = None
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 451
for _lib in _libs.values():
    if not _lib.has("SampledValuesPublisher_destroy", "cdecl"):
        continue
    SampledValuesPublisher_destroy = _lib.get("SampledValuesPublisher_destroy", "cdecl")
    SampledValuesPublisher_destroy.argtypes = [SVPublisher]
    SampledValuesPublisher_destroy.restype = None
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 454
for _lib in _libs.values():
    if not _lib.has("SV_ASDU_resetBuffer", "cdecl"):
        continue
    SV_ASDU_resetBuffer = _lib.get("SV_ASDU_resetBuffer", "cdecl")
    SV_ASDU_resetBuffer.argtypes = [SVPublisher_ASDU]
    SV_ASDU_resetBuffer.restype = None
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 457
for _lib in _libs.values():
    if not _lib.has("SV_ASDU_addINT8", "cdecl"):
        continue
    SV_ASDU_addINT8 = _lib.get("SV_ASDU_addINT8", "cdecl")
    SV_ASDU_addINT8.argtypes = [SVPublisher_ASDU]
    SV_ASDU_addINT8.restype = c_int
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 460
for _lib in _libs.values():
    if not _lib.has("SV_ASDU_setINT8", "cdecl"):
        continue
    SV_ASDU_setINT8 = _lib.get("SV_ASDU_setINT8", "cdecl")
    SV_ASDU_setINT8.argtypes = [SVPublisher_ASDU, c_int, c_int8]
    SV_ASDU_setINT8.restype = None
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 463
for _lib in _libs.values():
    if not _lib.has("SV_ASDU_addINT32", "cdecl"):
        continue
    SV_ASDU_addINT32 = _lib.get("SV_ASDU_addINT32", "cdecl")
    SV_ASDU_addINT32.argtypes = [SVPublisher_ASDU]
    SV_ASDU_addINT32.restype = c_int
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 466
for _lib in _libs.values():
    if not _lib.has("SV_ASDU_setINT32", "cdecl"):
        continue
    SV_ASDU_setINT32 = _lib.get("SV_ASDU_setINT32", "cdecl")
    SV_ASDU_setINT32.argtypes = [SVPublisher_ASDU, c_int, c_int32]
    SV_ASDU_setINT32.restype = None
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 469
for _lib in _libs.values():
    if not _lib.has("SV_ASDU_addINT64", "cdecl"):
        continue
    SV_ASDU_addINT64 = _lib.get("SV_ASDU_addINT64", "cdecl")
    SV_ASDU_addINT64.argtypes = [SVPublisher_ASDU]
    SV_ASDU_addINT64.restype = c_int
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 472
for _lib in _libs.values():
    if not _lib.has("SV_ASDU_setINT64", "cdecl"):
        continue
    SV_ASDU_setINT64 = _lib.get("SV_ASDU_setINT64", "cdecl")
    SV_ASDU_setINT64.argtypes = [SVPublisher_ASDU, c_int, c_int64]
    SV_ASDU_setINT64.restype = None
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 475
for _lib in _libs.values():
    if not _lib.has("SV_ASDU_addFLOAT", "cdecl"):
        continue
    SV_ASDU_addFLOAT = _lib.get("SV_ASDU_addFLOAT", "cdecl")
    SV_ASDU_addFLOAT.argtypes = [SVPublisher_ASDU]
    SV_ASDU_addFLOAT.restype = c_int
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 478
for _lib in _libs.values():
    if not _lib.has("SV_ASDU_setFLOAT", "cdecl"):
        continue
    SV_ASDU_setFLOAT = _lib.get("SV_ASDU_setFLOAT", "cdecl")
    SV_ASDU_setFLOAT.argtypes = [SVPublisher_ASDU, c_int, c_float]
    SV_ASDU_setFLOAT.restype = None
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 481
for _lib in _libs.values():
    if not _lib.has("SV_ASDU_addFLOAT64", "cdecl"):
        continue
    SV_ASDU_addFLOAT64 = _lib.get("SV_ASDU_addFLOAT64", "cdecl")
    SV_ASDU_addFLOAT64.argtypes = [SVPublisher_ASDU]
    SV_ASDU_addFLOAT64.restype = c_int
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 484
for _lib in _libs.values():
    if not _lib.has("SV_ASDU_setFLOAT64", "cdecl"):
        continue
    SV_ASDU_setFLOAT64 = _lib.get("SV_ASDU_setFLOAT64", "cdecl")
    SV_ASDU_setFLOAT64.argtypes = [SVPublisher_ASDU, c_int, c_double]
    SV_ASDU_setFLOAT64.restype = None
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 487
for _lib in _libs.values():
    if not _lib.has("SV_ASDU_setSmpCnt", "cdecl"):
        continue
    SV_ASDU_setSmpCnt = _lib.get("SV_ASDU_setSmpCnt", "cdecl")
    SV_ASDU_setSmpCnt.argtypes = [SVPublisher_ASDU, uint16_t]
    SV_ASDU_setSmpCnt.restype = None
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 490
for _lib in _libs.values():
    if not _lib.has("SV_ASDU_getSmpCnt", "cdecl"):
        continue
    SV_ASDU_getSmpCnt = _lib.get("SV_ASDU_getSmpCnt", "cdecl")
    SV_ASDU_getSmpCnt.argtypes = [SVPublisher_ASDU]
    SV_ASDU_getSmpCnt.restype = uint16_t
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 493
for _lib in _libs.values():
    if not _lib.has("SV_ASDU_increaseSmpCnt", "cdecl"):
        continue
    SV_ASDU_increaseSmpCnt = _lib.get("SV_ASDU_increaseSmpCnt", "cdecl")
    SV_ASDU_increaseSmpCnt.argtypes = [SVPublisher_ASDU]
    SV_ASDU_increaseSmpCnt.restype = None
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 496
for _lib in _libs.values():
    if not _lib.has("SV_ASDU_setRefrTm", "cdecl"):
        continue
    SV_ASDU_setRefrTm = _lib.get("SV_ASDU_setRefrTm", "cdecl")
    SV_ASDU_setRefrTm.argtypes = [SVPublisher_ASDU, uint64_t]
    SV_ASDU_setRefrTm.restype = None
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 499
for _lib in _libs.values():
    if not _lib.has("SV_ASDU_setSmpMod", "cdecl"):
        continue
    SV_ASDU_setSmpMod = _lib.get("SV_ASDU_setSmpMod", "cdecl")
    SV_ASDU_setSmpMod.argtypes = [SVPublisher_ASDU, uint8_t]
    SV_ASDU_setSmpMod.restype = None
    break

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 502
for _lib in _libs.values():
    if not _lib.has("SV_ASDU_setSmpRate", "cdecl"):
        continue
    SV_ASDU_setSmpRate = _lib.get("SV_ASDU_setSmpRate", "cdecl")
    SV_ASDU_setSmpRate.argtypes = [SVPublisher_ASDU, uint16_t]
    SV_ASDU_setSmpRate.restype = None
    break

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 97
class struct_sSVSubscriber_ASDU(Structure):
    pass

SVSubscriber_ASDU = POINTER(struct_sSVSubscriber_ASDU)# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 97

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 106
class struct_sSVSubscriber(Structure):
    pass

SVSubscriber = POINTER(struct_sSVSubscriber)# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 106

SVUpdateListener = CFUNCTYPE(UNCHECKED(None), SVSubscriber, POINTER(None), SVSubscriber_ASDU)# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 117

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 122
class struct_sSVReceiver(Structure):
    pass

SVReceiver = POINTER(struct_sSVReceiver)# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 122

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 134
if _libs["libiec61850.so"].has("SVReceiver_create", "cdecl"):
    SVReceiver_create = _libs["libiec61850.so"].get("SVReceiver_create", "cdecl")
    SVReceiver_create.argtypes = []
    SVReceiver_create.restype = SVReceiver

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 144
for _lib in _libs.values():
    if not _lib.has("SVReceiver_createRemote", "cdecl"):
        continue
    SVReceiver_createRemote = _lib.get("SVReceiver_createRemote", "cdecl")
    SVReceiver_createRemote.argtypes = [RSession]
    SVReceiver_createRemote.restype = SVReceiver
    break

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 152
if _libs["libiec61850.so"].has("SVReceiver_disableDestAddrCheck", "cdecl"):
    SVReceiver_disableDestAddrCheck = _libs["libiec61850.so"].get("SVReceiver_disableDestAddrCheck", "cdecl")
    SVReceiver_disableDestAddrCheck.argtypes = [SVReceiver]
    SVReceiver_disableDestAddrCheck.restype = None

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 165
if _libs["libiec61850.so"].has("SVReceiver_enableDestAddrCheck", "cdecl"):
    SVReceiver_enableDestAddrCheck = _libs["libiec61850.so"].get("SVReceiver_enableDestAddrCheck", "cdecl")
    SVReceiver_enableDestAddrCheck.argtypes = [SVReceiver]
    SVReceiver_enableDestAddrCheck.restype = None

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 178
if _libs["libiec61850.so"].has("SVReceiver_setInterfaceId", "cdecl"):
    SVReceiver_setInterfaceId = _libs["libiec61850.so"].get("SVReceiver_setInterfaceId", "cdecl")
    SVReceiver_setInterfaceId.argtypes = [SVReceiver, String]
    SVReceiver_setInterfaceId.restype = None

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 189
if _libs["libiec61850.so"].has("SVReceiver_addSubscriber", "cdecl"):
    SVReceiver_addSubscriber = _libs["libiec61850.so"].get("SVReceiver_addSubscriber", "cdecl")
    SVReceiver_addSubscriber.argtypes = [SVReceiver, SVSubscriber]
    SVReceiver_addSubscriber.restype = None

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 198
if _libs["libiec61850.so"].has("SVReceiver_removeSubscriber", "cdecl"):
    SVReceiver_removeSubscriber = _libs["libiec61850.so"].get("SVReceiver_removeSubscriber", "cdecl")
    SVReceiver_removeSubscriber.argtypes = [SVReceiver, SVSubscriber]
    SVReceiver_removeSubscriber.restype = None

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 208
if _libs["libiec61850.so"].has("SVReceiver_start", "cdecl"):
    SVReceiver_start = _libs["libiec61850.so"].get("SVReceiver_start", "cdecl")
    SVReceiver_start.argtypes = [SVReceiver]
    SVReceiver_start.restype = None

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 216
if _libs["libiec61850.so"].has("SVReceiver_stop", "cdecl"):
    SVReceiver_stop = _libs["libiec61850.so"].get("SVReceiver_stop", "cdecl")
    SVReceiver_stop.argtypes = [SVReceiver]
    SVReceiver_stop.restype = None

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 228
if _libs["libiec61850.so"].has("SVReceiver_isRunning", "cdecl"):
    SVReceiver_isRunning = _libs["libiec61850.so"].get("SVReceiver_isRunning", "cdecl")
    SVReceiver_isRunning.argtypes = [SVReceiver]
    SVReceiver_isRunning.restype = c_bool

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 236
if _libs["libiec61850.so"].has("SVReceiver_destroy", "cdecl"):
    SVReceiver_destroy = _libs["libiec61850.so"].get("SVReceiver_destroy", "cdecl")
    SVReceiver_destroy.argtypes = [SVReceiver]
    SVReceiver_destroy.restype = None

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 243
if _libs["libiec61850.so"].has("SVReceiver_startThreadless", "cdecl"):
    SVReceiver_startThreadless = _libs["libiec61850.so"].get("SVReceiver_startThreadless", "cdecl")
    SVReceiver_startThreadless.argtypes = [SVReceiver]
    SVReceiver_startThreadless.restype = c_bool

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 246
if _libs["libiec61850.so"].has("SVReceiver_stopThreadless", "cdecl"):
    SVReceiver_stopThreadless = _libs["libiec61850.so"].get("SVReceiver_stopThreadless", "cdecl")
    SVReceiver_stopThreadless.argtypes = [SVReceiver]
    SVReceiver_stopThreadless.restype = None

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 258
if _libs["libiec61850.so"].has("SVReceiver_tick", "cdecl"):
    SVReceiver_tick = _libs["libiec61850.so"].get("SVReceiver_tick", "cdecl")
    SVReceiver_tick.argtypes = [SVReceiver]
    SVReceiver_tick.restype = c_bool

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 270
if _libs["libiec61850.so"].has("SVSubscriber_create", "cdecl"):
    SVSubscriber_create = _libs["libiec61850.so"].get("SVSubscriber_create", "cdecl")
    SVSubscriber_create.argtypes = [POINTER(uint8_t), uint16_t]
    SVSubscriber_create.restype = SVSubscriber

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 284
if _libs["libiec61850.so"].has("SVSubscriber_setListener", "cdecl"):
    SVSubscriber_setListener = _libs["libiec61850.so"].get("SVSubscriber_setListener", "cdecl")
    SVSubscriber_setListener.argtypes = [SVSubscriber, SVUpdateListener, POINTER(None)]
    SVSubscriber_setListener.restype = None

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 287
if _libs["libiec61850.so"].has("SVSubscriber_destroy", "cdecl"):
    SVSubscriber_destroy = _libs["libiec61850.so"].get("SVSubscriber_destroy", "cdecl")
    SVSubscriber_destroy.argtypes = [SVSubscriber]
    SVSubscriber_destroy.restype = None

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 307
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getSmpCnt", "cdecl"):
    SVSubscriber_ASDU_getSmpCnt = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getSmpCnt", "cdecl")
    SVSubscriber_ASDU_getSmpCnt.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getSmpCnt.restype = uint16_t

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 314
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getSvId", "cdecl"):
    SVSubscriber_ASDU_getSvId = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getSvId", "cdecl")
    SVSubscriber_ASDU_getSvId.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getSvId.restype = c_char_p

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 322
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getDatSet", "cdecl"):
    SVSubscriber_ASDU_getDatSet = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getDatSet", "cdecl")
    SVSubscriber_ASDU_getDatSet.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getDatSet.restype = c_char_p

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 331
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getConfRev", "cdecl"):
    SVSubscriber_ASDU_getConfRev = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getConfRev", "cdecl")
    SVSubscriber_ASDU_getConfRev.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getConfRev.restype = uint32_t

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 339
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getSmpMod", "cdecl"):
    SVSubscriber_ASDU_getSmpMod = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getSmpMod", "cdecl")
    SVSubscriber_ASDU_getSmpMod.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getSmpMod.restype = uint8_t

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 347
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getSmpRate", "cdecl"):
    SVSubscriber_ASDU_getSmpRate = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getSmpRate", "cdecl")
    SVSubscriber_ASDU_getSmpRate.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getSmpRate.restype = uint16_t

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 357
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_hasDatSet", "cdecl"):
    SVSubscriber_ASDU_hasDatSet = _libs["libiec61850.so"].get("SVSubscriber_ASDU_hasDatSet", "cdecl")
    SVSubscriber_ASDU_hasDatSet.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_hasDatSet.restype = c_bool

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 367
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_hasRefrTm", "cdecl"):
    SVSubscriber_ASDU_hasRefrTm = _libs["libiec61850.so"].get("SVSubscriber_ASDU_hasRefrTm", "cdecl")
    SVSubscriber_ASDU_hasRefrTm.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_hasRefrTm.restype = c_bool

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 377
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_hasSmpMod", "cdecl"):
    SVSubscriber_ASDU_hasSmpMod = _libs["libiec61850.so"].get("SVSubscriber_ASDU_hasSmpMod", "cdecl")
    SVSubscriber_ASDU_hasSmpMod.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_hasSmpMod.restype = c_bool

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 387
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_hasSmpRate", "cdecl"):
    SVSubscriber_ASDU_hasSmpRate = _libs["libiec61850.so"].get("SVSubscriber_ASDU_hasSmpRate", "cdecl")
    SVSubscriber_ASDU_hasSmpRate.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_hasSmpRate.restype = c_bool

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 397
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getRefrTmAsMs", "cdecl"):
    SVSubscriber_ASDU_getRefrTmAsMs = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getRefrTmAsMs", "cdecl")
    SVSubscriber_ASDU_getRefrTmAsMs.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getRefrTmAsMs.restype = uint64_t

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 407
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getRefrTmAsNs", "cdecl"):
    SVSubscriber_ASDU_getRefrTmAsNs = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getRefrTmAsNs", "cdecl")
    SVSubscriber_ASDU_getRefrTmAsNs.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getRefrTmAsNs.restype = nsSinceEpoch

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 418
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getINT8", "cdecl"):
    SVSubscriber_ASDU_getINT8 = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getINT8", "cdecl")
    SVSubscriber_ASDU_getINT8.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getINT8.restype = c_int8

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 429
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getINT16", "cdecl"):
    SVSubscriber_ASDU_getINT16 = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getINT16", "cdecl")
    SVSubscriber_ASDU_getINT16.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getINT16.restype = c_int16

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 440
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getINT32", "cdecl"):
    SVSubscriber_ASDU_getINT32 = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getINT32", "cdecl")
    SVSubscriber_ASDU_getINT32.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getINT32.restype = c_int32

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 451
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getINT64", "cdecl"):
    SVSubscriber_ASDU_getINT64 = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getINT64", "cdecl")
    SVSubscriber_ASDU_getINT64.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getINT64.restype = c_int64

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 462
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getINT8U", "cdecl"):
    SVSubscriber_ASDU_getINT8U = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getINT8U", "cdecl")
    SVSubscriber_ASDU_getINT8U.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getINT8U.restype = uint8_t

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 473
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getINT16U", "cdecl"):
    SVSubscriber_ASDU_getINT16U = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getINT16U", "cdecl")
    SVSubscriber_ASDU_getINT16U.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getINT16U.restype = uint16_t

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 484
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getINT32U", "cdecl"):
    SVSubscriber_ASDU_getINT32U = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getINT32U", "cdecl")
    SVSubscriber_ASDU_getINT32U.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getINT32U.restype = uint32_t

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 495
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getINT64U", "cdecl"):
    SVSubscriber_ASDU_getINT64U = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getINT64U", "cdecl")
    SVSubscriber_ASDU_getINT64U.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getINT64U.restype = uint64_t

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 506
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getFLOAT32", "cdecl"):
    SVSubscriber_ASDU_getFLOAT32 = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getFLOAT32", "cdecl")
    SVSubscriber_ASDU_getFLOAT32.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getFLOAT32.restype = c_float

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 517
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getFLOAT64", "cdecl"):
    SVSubscriber_ASDU_getFLOAT64 = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getFLOAT64", "cdecl")
    SVSubscriber_ASDU_getFLOAT64.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getFLOAT64.restype = c_double

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 528
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getTimestamp", "cdecl"):
    SVSubscriber_ASDU_getTimestamp = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getTimestamp", "cdecl")
    SVSubscriber_ASDU_getTimestamp.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getTimestamp.restype = Timestamp

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 541
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getQuality", "cdecl"):
    SVSubscriber_ASDU_getQuality = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getQuality", "cdecl")
    SVSubscriber_ASDU_getQuality.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getQuality.restype = Quality

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 551
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getDataSize", "cdecl"):
    SVSubscriber_ASDU_getDataSize = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getDataSize", "cdecl")
    SVSubscriber_ASDU_getDataSize.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getDataSize.restype = c_int

# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 561
if _libs["libiec61850.so"].has("SVSubscriber_ASDU_getSmpSynch", "cdecl"):
    SVSubscriber_ASDU_getSmpSynch = _libs["libiec61850.so"].get("SVSubscriber_ASDU_getSmpSynch", "cdecl")
    SVSubscriber_ASDU_getSmpSynch.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getSmpSynch.restype = uint8_t

# /home/user/libiec61850/hal/inc/hal_serial.h: 39
class struct_sSerialPort(Structure):
    pass

SerialPort = POINTER(struct_sSerialPort)# /home/user/libiec61850/hal/inc/hal_serial.h: 39

enum_anon_75 = c_int# /home/user/libiec61850/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_NONE = 0# /home/user/libiec61850/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_INVALID_ARGUMENT = 1# /home/user/libiec61850/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_INVALID_BAUDRATE = 2# /home/user/libiec61850/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_OPEN_FAILED = 3# /home/user/libiec61850/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_UNKNOWN = 99# /home/user/libiec61850/hal/inc/hal_serial.h: 47

SerialPortError = enum_anon_75# /home/user/libiec61850/hal/inc/hal_serial.h: 47

# /home/user/libiec61850/hal/inc/hal_serial.h: 61
if _libs["libiec61850.so"].has("SerialPort_create", "cdecl"):
    SerialPort_create = _libs["libiec61850.so"].get("SerialPort_create", "cdecl")
    SerialPort_create.argtypes = [String, c_int, uint8_t, c_char, uint8_t]
    SerialPort_create.restype = SerialPort

# /home/user/libiec61850/hal/inc/hal_serial.h: 67
if _libs["libiec61850.so"].has("SerialPort_destroy", "cdecl"):
    SerialPort_destroy = _libs["libiec61850.so"].get("SerialPort_destroy", "cdecl")
    SerialPort_destroy.argtypes = [SerialPort]
    SerialPort_destroy.restype = None

# /home/user/libiec61850/hal/inc/hal_serial.h: 75
if _libs["libiec61850.so"].has("SerialPort_open", "cdecl"):
    SerialPort_open = _libs["libiec61850.so"].get("SerialPort_open", "cdecl")
    SerialPort_open.argtypes = [SerialPort]
    SerialPort_open.restype = c_bool

# /home/user/libiec61850/hal/inc/hal_serial.h: 81
if _libs["libiec61850.so"].has("SerialPort_close", "cdecl"):
    SerialPort_close = _libs["libiec61850.so"].get("SerialPort_close", "cdecl")
    SerialPort_close.argtypes = [SerialPort]
    SerialPort_close.restype = None

# /home/user/libiec61850/hal/inc/hal_serial.h: 89
if _libs["libiec61850.so"].has("SerialPort_getBaudRate", "cdecl"):
    SerialPort_getBaudRate = _libs["libiec61850.so"].get("SerialPort_getBaudRate", "cdecl")
    SerialPort_getBaudRate.argtypes = [SerialPort]
    SerialPort_getBaudRate.restype = c_int

# /home/user/libiec61850/hal/inc/hal_serial.h: 97
if _libs["libiec61850.so"].has("SerialPort_setTimeout", "cdecl"):
    SerialPort_setTimeout = _libs["libiec61850.so"].get("SerialPort_setTimeout", "cdecl")
    SerialPort_setTimeout.argtypes = [SerialPort, c_int]
    SerialPort_setTimeout.restype = None

# /home/user/libiec61850/hal/inc/hal_serial.h: 103
if _libs["libiec61850.so"].has("SerialPort_discardInBuffer", "cdecl"):
    SerialPort_discardInBuffer = _libs["libiec61850.so"].get("SerialPort_discardInBuffer", "cdecl")
    SerialPort_discardInBuffer.argtypes = [SerialPort]
    SerialPort_discardInBuffer.restype = None

# /home/user/libiec61850/hal/inc/hal_serial.h: 111
if _libs["libiec61850.so"].has("SerialPort_readByte", "cdecl"):
    SerialPort_readByte = _libs["libiec61850.so"].get("SerialPort_readByte", "cdecl")
    SerialPort_readByte.argtypes = [SerialPort]
    SerialPort_readByte.restype = c_int

# /home/user/libiec61850/hal/inc/hal_serial.h: 123
if _libs["libiec61850.so"].has("SerialPort_write", "cdecl"):
    SerialPort_write = _libs["libiec61850.so"].get("SerialPort_write", "cdecl")
    SerialPort_write.argtypes = [SerialPort, POINTER(uint8_t), c_int, c_int]
    SerialPort_write.restype = c_int

# /home/user/libiec61850/hal/inc/hal_serial.h: 129
if _libs["libiec61850.so"].has("SerialPort_getLastError", "cdecl"):
    SerialPort_getLastError = _libs["libiec61850.so"].get("SerialPort_getLastError", "cdecl")
    SerialPort_getLastError.argtypes = [SerialPort]
    SerialPort_getLastError.restype = SerialPortError

# /home/user/libiec61850/hal/inc/hal_thread.h: 38
class struct_sThread(Structure):
    pass

Thread = POINTER(struct_sThread)# /home/user/libiec61850/hal/inc/hal_thread.h: 38

Semaphore = POINTER(None)# /home/user/libiec61850/hal/inc/hal_thread.h: 41

ThreadExecutionFunction = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(None))# /home/user/libiec61850/hal/inc/hal_thread.h: 44

# /home/user/libiec61850/hal/inc/hal_thread.h: 56
if _libs["libiec61850.so"].has("Thread_create", "cdecl"):
    Thread_create = _libs["libiec61850.so"].get("Thread_create", "cdecl")
    Thread_create.argtypes = [ThreadExecutionFunction, POINTER(None), c_bool]
    Thread_create.restype = Thread

# /home/user/libiec61850/hal/inc/hal_thread.h: 67
if _libs["libiec61850.so"].has("Thread_start", "cdecl"):
    Thread_start = _libs["libiec61850.so"].get("Thread_start", "cdecl")
    Thread_start.argtypes = [Thread]
    Thread_start.restype = None

# /home/user/libiec61850/hal/inc/hal_thread.h: 75
if _libs["libiec61850.so"].has("Thread_destroy", "cdecl"):
    Thread_destroy = _libs["libiec61850.so"].get("Thread_destroy", "cdecl")
    Thread_destroy.argtypes = [Thread]
    Thread_destroy.restype = None

# /home/user/libiec61850/hal/inc/hal_thread.h: 81
if _libs["libiec61850.so"].has("Thread_sleep", "cdecl"):
    Thread_sleep = _libs["libiec61850.so"].get("Thread_sleep", "cdecl")
    Thread_sleep.argtypes = [c_int]
    Thread_sleep.restype = None

# /home/user/libiec61850/hal/inc/hal_thread.h: 84
if _libs["libiec61850.so"].has("Semaphore_create", "cdecl"):
    Semaphore_create = _libs["libiec61850.so"].get("Semaphore_create", "cdecl")
    Semaphore_create.argtypes = [c_int]
    Semaphore_create.restype = Semaphore

# /home/user/libiec61850/hal/inc/hal_thread.h: 88
if _libs["libiec61850.so"].has("Semaphore_wait", "cdecl"):
    Semaphore_wait = _libs["libiec61850.so"].get("Semaphore_wait", "cdecl")
    Semaphore_wait.argtypes = [Semaphore]
    Semaphore_wait.restype = None

# /home/user/libiec61850/hal/inc/hal_thread.h: 91
if _libs["libiec61850.so"].has("Semaphore_post", "cdecl"):
    Semaphore_post = _libs["libiec61850.so"].get("Semaphore_post", "cdecl")
    Semaphore_post.argtypes = [Semaphore]
    Semaphore_post.restype = None

# /home/user/libiec61850/hal/inc/hal_thread.h: 94
if _libs["libiec61850.so"].has("Semaphore_destroy", "cdecl"):
    Semaphore_destroy = _libs["libiec61850.so"].get("Semaphore_destroy", "cdecl")
    Semaphore_destroy.argtypes = [Semaphore]
    Semaphore_destroy.restype = None

# /home/user/libiec61850/hal/inc/tls_socket.h: 48
class struct_sTLSSocket(Structure):
    pass

TLSSocket = POINTER(struct_sTLSSocket)# /home/user/libiec61850/hal/inc/tls_socket.h: 48

# /home/user/libiec61850/hal/inc/tls_socket.h: 63
for _lib in _libs.values():
    if not _lib.has("TLSSocket_create", "cdecl"):
        continue
    TLSSocket_create = _lib.get("TLSSocket_create", "cdecl")
    TLSSocket_create.argtypes = [Socket, TLSConfiguration, c_bool]
    TLSSocket_create.restype = TLSSocket
    break

# /home/user/libiec61850/hal/inc/tls_socket.h: 69
for _lib in _libs.values():
    if not _lib.has("TLSSocket_performHandshake", "cdecl"):
        continue
    TLSSocket_performHandshake = _lib.get("TLSSocket_performHandshake", "cdecl")
    TLSSocket_performHandshake.argtypes = [TLSSocket]
    TLSSocket_performHandshake.restype = c_bool
    break

# /home/user/libiec61850/hal/inc/tls_socket.h: 78
for _lib in _libs.values():
    if not _lib.has("TLSSocket_getPeerCertificate", "cdecl"):
        continue
    TLSSocket_getPeerCertificate = _lib.get("TLSSocket_getPeerCertificate", "cdecl")
    TLSSocket_getPeerCertificate.argtypes = [TLSSocket, POINTER(c_int)]
    TLSSocket_getPeerCertificate.restype = POINTER(uint8_t)
    break

# /home/user/libiec61850/hal/inc/tls_socket.h: 94
for _lib in _libs.values():
    if not _lib.has("TLSSocket_read", "cdecl"):
        continue
    TLSSocket_read = _lib.get("TLSSocket_read", "cdecl")
    TLSSocket_read.argtypes = [TLSSocket, POINTER(uint8_t), c_int]
    TLSSocket_read.restype = c_int
    break

# /home/user/libiec61850/hal/inc/tls_socket.h: 106
for _lib in _libs.values():
    if not _lib.has("TLSSocket_write", "cdecl"):
        continue
    TLSSocket_write = _lib.get("TLSSocket_write", "cdecl")
    TLSSocket_write.argtypes = [TLSSocket, POINTER(uint8_t), c_int]
    TLSSocket_write.restype = c_int
    break

# /home/user/libiec61850/hal/inc/tls_socket.h: 112
for _lib in _libs.values():
    if not _lib.has("TLSSocket_close", "cdecl"):
        continue
    TLSSocket_close = _lib.get("TLSSocket_close", "cdecl")
    TLSSocket_close.argtypes = [TLSSocket]
    TLSSocket_close.restype = None
    break

# /home/user/libiec61850/config/stack_config.h: 13
try:
    DEBUG = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 16
try:
    DEBUG_SOCKET = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 17
try:
    DEBUG_COTP = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 18
try:
    DEBUG_ISO_SERVER = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 19
try:
    DEBUG_ISO_CLIENT = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 20
try:
    DEBUG_IED_SERVER = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 21
try:
    DEBUG_IED_CLIENT = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 22
try:
    DEBUG_MMS_CLIENT = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 23
try:
    DEBUG_MMS_SERVER = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 24
try:
    DEBUG_GOOSE_SUBSCRIBER = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 25
try:
    DEBUG_GOOSE_PUBLISHER = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 26
try:
    DEBUG_SV_SUBSCRIBER = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 27
try:
    DEBUG_SV_PUBLISHER = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 28
try:
    DEBUG_HAL_ETHERNET = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 31
try:
    CONFIG_MMS_MAXIMUM_PDU_SIZE = 65000
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 40
try:
    CONFIG_MMS_SINGLE_THREADED = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 51
try:
    CONFIG_MMS_THREADLESS_STACK = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 54
try:
    CONFIG_MAXIMUM_TCP_CLIENT_CONNECTIONS = 100
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 57
try:
    CONFIG_ACTIVATE_TCP_KEEPALIVE = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 60
try:
    CONFIG_TCP_KEEPALIVE_IDLE = 5
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 63
try:
    CONFIG_TCP_KEEPALIVE_INTERVAL = 2
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 66
try:
    CONFIG_TCP_KEEPALIVE_CNT = 2
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 69
try:
    CONFIG_COTP_MAX_TPDU_SIZE = 8192
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 72
try:
    CONFIG_ETHERNET_INTERFACE_ID = 'eth0'
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 77
try:
    CONFIG_INCLUDE_GOOSE_SUPPORT = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 80
try:
    CONFIG_IEC61850_SAMPLED_VALUES_SUPPORT = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 83
try:
    CONFIG_IEC61850_EDITION_1 = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 86
try:
    CONFIG_GOOSE_STABLE_STATE_TRANSMISSION_INTERVAL = 5000
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 89
try:
    CONFIG_GOOSE_EVENT_RETRANSMISSION_INTERVAL = 500
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 92
try:
    CONFIG_GOOSE_EVENT_RETRANSMISSION_COUNT = 2
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 100
try:
    CONFIG_GOOSE_GOID_WRITABLE = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 101
try:
    CONFIG_GOOSE_DATSET_WRITABLE = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 102
try:
    CONFIG_GOOSE_CONFREV_WRITABLE = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 103
try:
    CONFIG_GOOSE_NDSCOM_WRITABLE = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 104
try:
    CONFIG_GOOSE_DSTADDRESS_WRITABLE = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 105
try:
    CONFIG_GOOSE_MINTIME_WRITABLE = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 106
try:
    CONFIG_GOOSE_MAXTIME_WRITABLE = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 107
try:
    CONFIG_GOOSE_FIXEDOFFS_WRITABLE = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 110
try:
    CONFIG_GOOSE_DEFAULT_PRIORITY = 4
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 113
try:
    CONFIG_GOOSE_DEFAULT_VLAN_ID = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 116
try:
    CONFIG_GOOSE_DEFAULT_APPID = 0x1000
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 122
try:
    CONFIG_IEC61850_CONTROL_SERVICE = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 125
try:
    CONFIG_CONTROL_DEFAULT_SBO_TIMEOUT = 15000
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 128
try:
    CONFIG_IEC61850_REPORT_SERVICE = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 131
try:
    CONFIG_IEC61850_BRCB_WITH_RESVTMS = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 134
try:
    CONFIG_IEC61850_RCB_ALLOW_ONLY_PRECONFIGURED_CLIENT = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 137
try:
    CONFIG_REPORTING_DEFAULT_REPORT_BUFFER_SIZE = 65536
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 140
try:
    CONFIG_IEC61850_SETTING_GROUPS = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 143
try:
    CONFIG_IEC61850_SG_RESVTMS = 300
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 146
try:
    CONFIG_IEC61850_LOG_SERVICE = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 149
try:
    CONFIG_IEC61850_SERVICE_TRACKING = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 152
try:
    CONFIG_IEC61850_SUPPORT_USER_READ_ACCESS_CONTROL = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 155
try:
    CONFIG_IEC61850_SUPPORT_SERVER_IDENTITY = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 158
try:
    CONFIG_IEC61850_FORCE_MEMORY_ALIGNMENT = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 161
try:
    CONFIG_IEC61850_R_GOOSE = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 164
try:
    CONFIG_IEC61850_R_SMV = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 167
try:
    CONFIG_IEC61850_L2_GOOSE = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 170
try:
    CONFIG_IEC61850_L2_SMV = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 173
try:
    CONFIG_IEC61850_SNTP_CLIENT = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 202
try:
    CONFIG_VIRTUAL_FILESTORE_BASEPATH = './vmd-filestore/'
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 205
try:
    CONFIG_MMS_MAX_NUMBER_OF_OPEN_FILES_PER_CONNECTION = 5
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 208
try:
    CONFIG_MMS_MAX_NUMBER_OF_DOMAIN_SPECIFIC_DATA_SETS = 10
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 211
try:
    CONFIG_MMS_MAX_NUMBER_OF_ASSOCIATION_SPECIFIC_DATA_SETS = 10
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 214
try:
    CONFIG_MMS_MAX_NUMBER_OF_VMD_SPECIFIC_DATA_SETS = 10
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 217
try:
    CONFIG_MMS_MAX_NUMBER_OF_DATA_SET_MEMBERS = 100
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 220
try:
    CONFIG_MMS_SERVER_MAX_GET_FILE_TASKS = 5
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 223
try:
    MMS_DEFAULT_PROFILE = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 226
try:
    MMS_READ_SERVICE = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 227
try:
    MMS_WRITE_SERVICE = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 228
try:
    MMS_GET_NAME_LIST = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 229
try:
    MMS_JOURNAL_SERVICE = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 230
try:
    MMS_GET_VARIABLE_ACCESS_ATTRIBUTES = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 231
try:
    MMS_DATA_SET_SERVICE = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 232
try:
    MMS_DYNAMIC_DATA_SETS = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 233
try:
    MMS_GET_DATA_SET_ATTRIBUTES = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 234
try:
    MMS_STATUS_SERVICE = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 235
try:
    MMS_IDENTIFY_SERVICE = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 236
try:
    MMS_FILE_SERVICE = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 237
try:
    MMS_OBTAIN_FILE_SERVICE = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 238
try:
    MMS_DELETE_FILE_SERVICE = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 239
try:
    MMS_RENAME_FILE_SERVICE = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 244
try:
    CONFIG_MMS_SUPPORT_FLATTED_NAME_SPACE = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 248
try:
    CONFIG_MMS_SORT_NAME_LIST = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 250
try:
    CONFIG_INCLUDE_PLATFORM_SPECIFIC_HEADERS = 0
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 253
try:
    CONFIG_MMS_RAW_MESSAGE_LOGGING = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 258
try:
    CONFIG_SET_FILESTORE_BASEPATH_AT_RUNTIME = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 261
try:
    CONFIG_MMS_SERVER_CONFIG_SERVICES_AT_RUNTIME = 1
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 264
try:
    CONFIG_DEFAULT_MAX_SERV_OUTSTANDING_CALLING = 5
except:
    pass

# /home/user/libiec61850/config/stack_config.h: 267
try:
    CONFIG_DEFAULT_MAX_SERV_OUTSTANDING_CALLED = 5
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 49
try:
    CDC_OPTION_PICS_SUBST = (1 << 0)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 50
try:
    CDC_OPTION_BLK_ENA = (1 << 1)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 53
try:
    CDC_OPTION_DESC = (1 << 2)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 56
try:
    CDC_OPTION_DESC_UNICODE = (1 << 3)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 59
try:
    CDC_OPTION_AC_DLNDA = (1 << 4)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 62
try:
    CDC_OPTION_AC_DLN = (1 << 5)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 65
try:
    CDC_OPTION_UNIT = (1 << 6)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 67
try:
    CDC_OPTION_FROZEN_VALUE = (1 << 7)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 69
try:
    CDC_OPTION_ADDR = (1 << 8)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 70
try:
    CDC_OPTION_ADDINFO = (1 << 9)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 72
try:
    CDC_OPTION_INST_MAG = (1 << 10)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 73
try:
    CDC_OPTION_RANGE = (1 << 11)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 75
try:
    CDC_OPTION_UNIT_MULTIPLIER = (1 << 12)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 77
try:
    CDC_OPTION_AC_SCAV = (1 << 13)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 79
try:
    CDC_OPTION_MIN = (1 << 14)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 80
try:
    CDC_OPTION_MAX = (1 << 15)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 82
try:
    CDC_OPTION_AC_CLC_O = (1 << 16)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 84
try:
    CDC_OPTION_RANGE_ANG = (1 << 17)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 86
try:
    CDC_OPTION_PHASE_A = (1 << 18)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 87
try:
    CDC_OPTION_PHASE_B = (1 << 19)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 88
try:
    CDC_OPTION_PHASE_C = (1 << 20)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 90
try:
    CDC_OPTION_PHASE_NEUT = (1 << 21)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 92
try:
    CDC_OPTION_PHASES_ABC = ((CDC_OPTION_PHASE_A | CDC_OPTION_PHASE_B) | CDC_OPTION_PHASE_C)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 94
try:
    CDC_OPTION_PHASES_ALL = (((CDC_OPTION_PHASE_A | CDC_OPTION_PHASE_B) | CDC_OPTION_PHASE_C) | CDC_OPTION_PHASE_NEUT)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 96
try:
    CDC_OPTION_STEP_SIZE = (1 << 22)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 98
try:
    CDC_OPTION_ANGLE_REF = (1 << 23)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 101
try:
    CDC_OPTION_DPL_HWREV = (1 << 17)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 102
try:
    CDC_OPTION_DPL_SWREV = (1 << 18)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 103
try:
    CDC_OPTION_DPL_SERNUM = (1 << 19)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 104
try:
    CDC_OPTION_DPL_MODEL = (1 << 20)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 105
try:
    CDC_OPTION_DPL_LOCATION = (1 << 21)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 108
try:
    CDC_OPTION_AC_LN0_M = (1 << 24)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 109
try:
    CDC_OPTION_AC_LN0_EX = (1 << 25)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 110
try:
    CDC_OPTION_AC_DLD_M = (1 << 26)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 115
try:
    CDC_CTL_MODEL_NONE = 0
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 116
try:
    CDC_CTL_MODEL_DIRECT_NORMAL = 1
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 117
try:
    CDC_CTL_MODEL_SBO_NORMAL = 2
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 118
try:
    CDC_CTL_MODEL_DIRECT_ENHANCED = 3
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 119
try:
    CDC_CTL_MODEL_SBO_ENHANCED = 4
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 121
try:
    CDC_CTL_MODEL_HAS_CANCEL = (1 << 4)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 122
try:
    CDC_CTL_MODEL_IS_TIME_ACTIVATED = (1 << 5)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 124
try:
    CDC_CTL_OPTION_ORIGIN = (1 << 6)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 125
try:
    CDC_CTL_OPTION_CTL_NUM = (1 << 7)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 126
try:
    CDC_CTL_OPTION_ST_SELD = (1 << 8)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 127
try:
    CDC_CTL_OPTION_OP_RCVD = (1 << 9)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 128
try:
    CDC_CTL_OPTION_OP_OK = (1 << 10)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 129
try:
    CDC_CTL_OPTION_T_OP_OK = (1 << 11)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 130
try:
    CDC_CTL_OPTION_SBO_TIMEOUT = (1 << 12)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 131
try:
    CDC_CTL_OPTION_SBO_CLASS = (1 << 13)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 132
try:
    CDC_CTL_OPTION_OPER_TIMEOUT = (1 << 14)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 564
try:
    CDC_OPTION_61400_MIN_MX_VAL = (1 << 10)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 567
try:
    CDC_OPTION_61400_MAX_MX_VAL = (1 << 11)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 570
try:
    CDC_OPTION_61400_TOT_AV_VAL = (1 << 12)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 573
try:
    CDC_OPTION_61400_SDV_VAL = (1 << 13)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 576
try:
    CDC_OPTION_61400_INC_RATE = (1 << 14)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 579
try:
    CDC_OPTION_61400_DEC_RATE = (1 << 15)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 582
try:
    CDC_OPTION_61400_SP_ACS = (1 << 16)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 585
try:
    CDC_OPTION_61400_CHA_PER_RS = (1 << 17)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 588
try:
    CDC_OPTION_61400_CM_ACS = (1 << 18)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 591
try:
    CDC_OPTION_61400_TM_TOT = (1 << 19)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 594
try:
    CDC_OPTION_61400_COUNTING_DAILY = (1 << 20)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 597
try:
    CDC_OPTION_61400_COUNTING_MONTHLY = (1 << 21)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 600
try:
    CDC_OPTION_61400_COUNTING_YEARLY = (1 << 22)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 603
try:
    CDC_OPTION_61400_COUNTING_TOTAL = (1 << 23)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_cdc.h: 606
try:
    CDC_OPTION_61400_COUNTING_ALL = (((CDC_OPTION_61400_COUNTING_DAILY | CDC_OPTION_61400_COUNTING_MONTHLY) | CDC_OPTION_61400_COUNTING_YEARLY) | CDC_OPTION_61400_COUNTING_TOTAL)
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 42
try:
    IEC_61850_EDITION_1 = 0
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 45
try:
    IEC_61850_EDITION_2 = 1
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 48
try:
    IEC_61850_EDITION_2_1 = 2
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 112
try:
    TRG_OPT_DATA_CHANGED = 1
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 115
try:
    TRG_OPT_QUALITY_CHANGED = 2
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 118
try:
    TRG_OPT_DATA_UPDATE = 4
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 121
try:
    TRG_OPT_INTEGRITY = 8
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 124
try:
    TRG_OPT_GI = 16
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 127
try:
    TRG_OPT_TRANSIENT = 128
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 139
try:
    RPT_OPT_SEQ_NUM = 1
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 142
try:
    RPT_OPT_TIME_STAMP = 2
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 145
try:
    RPT_OPT_REASON_FOR_INCLUSION = 4
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 148
try:
    RPT_OPT_DATA_SET = 8
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 151
try:
    RPT_OPT_DATA_REFERENCE = 16
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 154
try:
    RPT_OPT_BUFFER_OVERFLOW = 32
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 157
try:
    RPT_OPT_ENTRY_ID = 64
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 160
try:
    RPT_OPT_CONF_REV = 128
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 170
try:
    CONTROL_ORCAT_NOT_SUPPORTED = 0
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 173
try:
    CONTROL_ORCAT_BAY_CONTROL = 1
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 176
try:
    CONTROL_ORCAT_STATION_CONTROL = 2
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 179
try:
    CONTROL_ORCAT_REMOTE_CONTROL = 3
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 182
try:
    CONTROL_ORCAT_AUTOMATIC_BAY = 4
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 185
try:
    CONTROL_ORCAT_AUTOMATIC_STATION = 5
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 188
try:
    CONTROL_ORCAT_AUTOMATIC_REMOTE = 6
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 191
try:
    CONTROL_ORCAT_MAINTENANCE = 7
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 194
try:
    CONTROL_ORCAT_PROCESS = 8
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 329
try:
    QUALITY_VALIDITY_GOOD = 0
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 330
try:
    QUALITY_VALIDITY_INVALID = 2
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 331
try:
    QUALITY_VALIDITY_RESERVED = 1
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 332
try:
    QUALITY_VALIDITY_QUESTIONABLE = 3
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 334
try:
    QUALITY_DETAIL_OVERFLOW = 4
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 335
try:
    QUALITY_DETAIL_OUT_OF_RANGE = 8
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 336
try:
    QUALITY_DETAIL_BAD_REFERENCE = 16
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 337
try:
    QUALITY_DETAIL_OSCILLATORY = 32
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 338
try:
    QUALITY_DETAIL_FAILURE = 64
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 339
try:
    QUALITY_DETAIL_OLD_DATA = 128
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 340
try:
    QUALITY_DETAIL_INCONSISTENT = 256
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 341
try:
    QUALITY_DETAIL_INACCURATE = 512
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 343
try:
    QUALITY_SOURCE_SUBSTITUTED = 1024
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 345
try:
    QUALITY_TEST = 2048
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 347
try:
    QUALITY_OPERATOR_BLOCKED = 4096
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_common.h: 349
try:
    QUALITY_DERIVED = 8192
except:
    pass

# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 28
try:
    CONFIG_MMS_SUPPORT_TLS = 0
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 8
try:
    TLS_NULL_WITH_NULL_NULL = 0x0000
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 9
try:
    TLS_RSA_WITH_NULL_MD5 = 0x0001
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 10
try:
    TLS_RSA_WITH_NULL_SHA = 0x0002
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 11
try:
    TLS_RSA_EXPORT_WITH_RC4_40_MD5 = 0x0003
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 12
try:
    TLS_RSA_WITH_RC4_128_MD5 = 0x0004
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 13
try:
    TLS_RSA_WITH_RC4_128_SHA = 0x0005
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 14
try:
    TLS_RSA_EXPORT_WITH_RC2_CBC_40_MD5 = 0x0006
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 15
try:
    TLS_RSA_WITH_IDEA_CBC_SHA = 0x0007
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 16
try:
    TLS_RSA_EXPORT_WITH_DES40_CBC_SHA = 0x0008
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 17
try:
    TLS_RSA_WITH_DES_CBC_SHA = 0x0009
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 18
try:
    TLS_RSA_WITH_3DES_EDE_CBC_SHA = 0x000A
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 19
try:
    TLS_DH_DSS_EXPORT_WITH_DES40_CBC_SHA = 0x000B
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 20
try:
    TLS_DH_DSS_WITH_DES_CBC_SHA = 0x000C
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 21
try:
    TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA = 0x000D
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 22
try:
    TLS_DH_RSA_EXPORT_WITH_DES40_CBC_SHA = 0x000E
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 23
try:
    TLS_DH_RSA_WITH_DES_CBC_SHA = 0x000F
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 24
try:
    TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA = 0x0010
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 25
try:
    TLS_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA = 0x0011
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 26
try:
    TLS_DHE_DSS_WITH_DES_CBC_SHA = 0x0012
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 27
try:
    TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA = 0x0013
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 28
try:
    TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA = 0x0014
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 29
try:
    TLS_DHE_RSA_WITH_DES_CBC_SHA = 0x0015
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 30
try:
    TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA = 0x0016
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 31
try:
    TLS_DH_anon_EXPORT_WITH_RC4_40_MD5 = 0x0017
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 32
try:
    TLS_DH_anon_WITH_RC4_128_MD5 = 0x0018
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 33
try:
    TLS_DH_anon_EXPORT_WITH_DES40_CBC_SHA = 0x0019
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 34
try:
    TLS_DH_anon_WITH_DES_CBC_SHA = 0x001A
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 35
try:
    TLS_DH_anon_WITH_3DES_EDE_CBC_SHA = 0x001B
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 36
try:
    TLS_RSA_WITH_AES_128_CBC_SHA = 0x002F
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 37
try:
    TLS_DH_DSS_WITH_AES_128_CBC_SHA = 0x0030
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 38
try:
    TLS_DH_RSA_WITH_AES_128_CBC_SHA = 0x0031
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 39
try:
    TLS_DHE_DSS_WITH_AES_128_CBC_SHA = 0x0032
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 40
try:
    TLS_DHE_RSA_WITH_AES_128_CBC_SHA = 0x0033
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 41
try:
    TLS_DH_anon_WITH_AES_128_CBC_SHA = 0x0034
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 42
try:
    TLS_RSA_WITH_AES_256_CBC_SHA = 0x0035
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 43
try:
    TLS_DH_DSS_WITH_AES_256_CBC_SHA = 0x0036
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 44
try:
    TLS_DH_RSA_WITH_AES_256_CBC_SHA = 0x0037
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 45
try:
    TLS_DHE_DSS_WITH_AES_256_CBC_SHA = 0x0038
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 46
try:
    TLS_DHE_RSA_WITH_AES_256_CBC_SHA = 0x0039
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 47
try:
    TLS_DH_anon_WITH_AES_256_CBC_SHA = 0x003A
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 48
try:
    TLS_RSA_WITH_NULL_SHA256 = 0x003B
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 49
try:
    TLS_RSA_WITH_AES_128_CBC_SHA256 = 0x003C
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 50
try:
    TLS_RSA_WITH_AES_256_CBC_SHA256 = 0x003D
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 51
try:
    TLS_DH_DSS_WITH_AES_128_CBC_SHA256 = 0x003E
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 52
try:
    TLS_DH_RSA_WITH_AES_128_CBC_SHA256 = 0x003F
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 53
try:
    TLS_DHE_DSS_WITH_AES_128_CBC_SHA256 = 0x0040
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 54
try:
    TLS_RSA_WITH_CAMELLIA_128_CBC_SHA = 0x0041
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 55
try:
    TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA = 0x0042
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 56
try:
    TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA = 0x0043
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 57
try:
    TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA = 0x0044
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 58
try:
    TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA = 0x0045
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 59
try:
    TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA = 0x0046
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 60
try:
    TLS_DHE_RSA_WITH_AES_128_CBC_SHA256 = 0x0067
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 61
try:
    TLS_DH_DSS_WITH_AES_256_CBC_SHA256 = 0x0068
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 62
try:
    TLS_DH_RSA_WITH_AES_256_CBC_SHA256 = 0x0069
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 63
try:
    TLS_DHE_DSS_WITH_AES_256_CBC_SHA256 = 0x006A
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 64
try:
    TLS_DHE_RSA_WITH_AES_256_CBC_SHA256 = 0x006B
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 65
try:
    TLS_DH_anon_WITH_AES_128_CBC_SHA256 = 0x006C
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 66
try:
    TLS_DH_anon_WITH_AES_256_CBC_SHA256 = 0x006D
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 67
try:
    TLS_RSA_WITH_CAMELLIA_256_CBC_SHA = 0x0084
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 68
try:
    TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA = 0x0085
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 69
try:
    TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA = 0x0086
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 70
try:
    TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA = 0x0087
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 71
try:
    TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA = 0x0088
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 72
try:
    TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA = 0x0089
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 73
try:
    TLS_RSA_WITH_SEED_CBC_SHA = 0x0096
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 74
try:
    TLS_DH_DSS_WITH_SEED_CBC_SHA = 0x0097
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 75
try:
    TLS_DH_RSA_WITH_SEED_CBC_SHA = 0x0098
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 76
try:
    TLS_DHE_DSS_WITH_SEED_CBC_SHA = 0x0099
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 77
try:
    TLS_DHE_RSA_WITH_SEED_CBC_SHA = 0x009A
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 78
try:
    TLS_DH_anon_WITH_SEED_CBC_SHA = 0x009B
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 79
try:
    TLS_RSA_WITH_AES_128_GCM_SHA256 = 0x009C
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 80
try:
    TLS_RSA_WITH_AES_256_GCM_SHA384 = 0x009D
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 81
try:
    TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 = 0x009E
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 82
try:
    TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 = 0x009F
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 83
try:
    TLS_DH_RSA_WITH_AES_128_GCM_SHA256 = 0x00A0
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 84
try:
    TLS_DH_RSA_WITH_AES_256_GCM_SHA384 = 0x00A1
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 85
try:
    TLS_DHE_DSS_WITH_AES_128_GCM_SHA256 = 0x00A2
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 86
try:
    TLS_DHE_DSS_WITH_AES_256_GCM_SHA384 = 0x00A3
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 87
try:
    TLS_DH_DSS_WITH_AES_128_GCM_SHA256 = 0x00A4
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 88
try:
    TLS_DH_DSS_WITH_AES_256_GCM_SHA384 = 0x00A5
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 89
try:
    TLS_DH_anon_WITH_AES_128_GCM_SHA256 = 0x00A6
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 90
try:
    TLS_DH_anon_WITH_AES_256_GCM_SHA384 = 0x00A7
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 91
try:
    TLS_PSK_WITH_AES_128_CBC_SHA = 0x008C
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 92
try:
    TLS_PSK_WITH_AES_256_CBC_SHA = 0x008D
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 93
try:
    TLS_DHE_PSK_WITH_AES_128_CBC_SHA = 0x008E
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 94
try:
    TLS_DHE_PSK_WITH_AES_256_CBC_SHA = 0x008F
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 95
try:
    TLS_RSA_PSK_WITH_AES_128_CBC_SHA = 0x0090
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 96
try:
    TLS_RSA_PSK_WITH_AES_256_CBC_SHA = 0x0091
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 97
try:
    TLS_PSK_WITH_AES_128_CBC_SHA256 = 0x00AE
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 98
try:
    TLS_PSK_WITH_AES_256_CBC_SHA384 = 0x00AF
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 99
try:
    TLS_DHE_PSK_WITH_AES_128_CBC_SHA256 = 0x00B0
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 100
try:
    TLS_DHE_PSK_WITH_AES_256_CBC_SHA384 = 0x00B1
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 101
try:
    TLS_RSA_PSK_WITH_AES_128_CBC_SHA256 = 0x00B2
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 102
try:
    TLS_RSA_PSK_WITH_AES_256_CBC_SHA384 = 0x00B3
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 103
try:
    TLS_PSK_WITH_NULL_SHA = 0x002C
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 104
try:
    TLS_DHE_PSK_WITH_NULL_SHA = 0x002D
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 105
try:
    TLS_RSA_PSK_WITH_NULL_SHA = 0x002E
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 106
try:
    TLS_PSK_WITH_NULL_SHA256 = 0x00B4
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 107
try:
    TLS_PSK_WITH_NULL_SHA384 = 0x00B5
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 108
try:
    TLS_DHE_PSK_WITH_NULL_SHA256 = 0x00B6
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 109
try:
    TLS_DHE_PSK_WITH_NULL_SHA384 = 0x00B7
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 110
try:
    TLS_RSA_PSK_WITH_NULL_SHA256 = 0x00B8
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 111
try:
    TLS_RSA_PSK_WITH_NULL_SHA384 = 0x00B9
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 112
try:
    TLS_ECDH_ECDSA_WITH_NULL_SHA = 0xC001
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 113
try:
    TLS_ECDH_ECDSA_WITH_RC4_128_SHA = 0xC002
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 114
try:
    TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA = 0xC003
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 115
try:
    TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA = 0xC004
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 116
try:
    TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA = 0xC005
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 117
try:
    TLS_ECDHE_ECDSA_WITH_NULL_SHA = 0xC006
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 118
try:
    TLS_ECDHE_ECDSA_WITH_RC4_128_SHA = 0xC007
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 119
try:
    TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA = 0xC008
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 120
try:
    TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA = 0xC009
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 121
try:
    TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA = 0xC00A
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 122
try:
    TLS_ECDH_RSA_WITH_NULL_SHA = 0xC00B
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 123
try:
    TLS_ECDH_RSA_WITH_RC4_128_SHA = 0xC00C
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 124
try:
    TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA = 0xC00D
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 125
try:
    TLS_ECDH_RSA_WITH_AES_128_CBC_SHA = 0xC00E
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 126
try:
    TLS_ECDH_RSA_WITH_AES_256_CBC_SHA = 0xC00F
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 127
try:
    TLS_ECDHE_RSA_WITH_NULL_SHA = 0xC010
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 128
try:
    TLS_ECDHE_RSA_WITH_RC4_128_SHA = 0xC011
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 129
try:
    TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA = 0xC012
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 130
try:
    TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA = 0xC013
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 131
try:
    TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA = 0xC014
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 132
try:
    TLS_ECDH_anon_WITH_NULL_SHA = 0xC015
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 133
try:
    TLS_ECDH_anon_WITH_RC4_128_SHA = 0xC016
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 134
try:
    TLS_ECDH_anon_WITH_3DES_EDE_CBC_SHA = 0xC017
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 135
try:
    TLS_ECDH_anon_WITH_AES_128_CBC_SHA = 0xC018
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 136
try:
    TLS_ECDH_anon_WITH_AES_256_CBC_SHA = 0xC019
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 137
try:
    TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 = 0xC023
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 138
try:
    TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384 = 0xC024
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 139
try:
    TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256 = 0xC025
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 140
try:
    TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384 = 0xC026
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 141
try:
    TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 = 0xC027
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 142
try:
    TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 = 0xC028
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 143
try:
    TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256 = 0xC029
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 144
try:
    TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384 = 0xC02A
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 145
try:
    TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 = 0xC02B
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 146
try:
    TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 = 0xC02C
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 147
try:
    TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256 = 0xC02D
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 148
try:
    TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384 = 0xC02E
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 149
try:
    TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 = 0xC02F
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 150
try:
    TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 = 0xC030
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 151
try:
    TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256 = 0xC031
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 152
try:
    TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384 = 0xC032
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 153
try:
    TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA = 0xC035
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 154
try:
    TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA = 0xC036
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 155
try:
    TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA256 = 0xC037
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 156
try:
    TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384 = 0xC038
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 157
try:
    TLS_ECDHE_PSK_WITH_NULL_SHA = 0xC039
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 158
try:
    TLS_ECDHE_PSK_WITH_NULL_SHA256 = 0xC03A
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 159
try:
    TLS_ECDHE_PSK_WITH_NULL_SHA384 = 0xC03B
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 160
try:
    TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_CBC_SHA256 = 0xC072
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 161
try:
    TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_CBC_SHA384 = 0xC073
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 162
try:
    TLS_ECDH_ECDSA_WITH_CAMELLIA_128_CBC_SHA256 = 0xC074
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 163
try:
    TLS_ECDH_ECDSA_WITH_CAMELLIA_256_CBC_SHA384 = 0xC075
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 164
try:
    TLS_ECDHE_RSA_WITH_CAMELLIA_128_CBC_SHA256 = 0xC076
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 165
try:
    TLS_ECDHE_RSA_WITH_CAMELLIA_256_CBC_SHA384 = 0xC077
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 166
try:
    TLS_ECDH_RSA_WITH_CAMELLIA_128_CBC_SHA256 = 0xC078
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 167
try:
    TLS_ECDH_RSA_WITH_CAMELLIA_256_CBC_SHA384 = 0xC079
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 168
try:
    TLS_RSA_WITH_ARIA_128_CBC_SHA256 = 0xC03C
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 169
try:
    TLS_RSA_WITH_ARIA_256_CBC_SHA384 = 0xC03D
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 170
try:
    TLS_DH_DSS_WITH_ARIA_128_CBC_SHA256 = 0xC03E
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 171
try:
    TLS_DH_DSS_WITH_ARIA_256_CBC_SHA384 = 0xC03F
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 172
try:
    TLS_DH_RSA_WITH_ARIA_128_CBC_SHA256 = 0xC040
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 173
try:
    TLS_DH_RSA_WITH_ARIA_256_CBC_SHA384 = 0xC041
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 174
try:
    TLS_DHE_DSS_WITH_ARIA_128_CBC_SHA256 = 0xC042
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 175
try:
    TLS_DHE_DSS_WITH_ARIA_256_CBC_SHA384 = 0xC043
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 176
try:
    TLS_DHE_RSA_WITH_ARIA_128_CBC_SHA256 = 0xC044
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 177
try:
    TLS_DHE_RSA_WITH_ARIA_256_CBC_SHA384 = 0xC045
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 178
try:
    TLS_DH_anon_WITH_ARIA_128_CBC_SHA256 = 0xC046
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 179
try:
    TLS_DH_anon_WITH_ARIA_256_CBC_SHA384 = 0xC047
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 180
try:
    TLS_ECDHE_ECDSA_WITH_ARIA_128_CBC_SHA256 = 0xC048
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 181
try:
    TLS_ECDHE_ECDSA_WITH_ARIA_256_CBC_SHA384 = 0xC049
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 182
try:
    TLS_ECDH_ECDSA_WITH_ARIA_128_CBC_SHA256 = 0xC04A
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 183
try:
    TLS_ECDH_ECDSA_WITH_ARIA_256_CBC_SHA384 = 0xC04B
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 184
try:
    TLS_ECDHE_RSA_WITH_ARIA_128_CBC_SHA256 = 0xC04C
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 185
try:
    TLS_ECDHE_RSA_WITH_ARIA_256_CBC_SHA384 = 0xC04D
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 186
try:
    TLS_ECDH_RSA_WITH_ARIA_128_CBC_SHA256 = 0xC04E
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 187
try:
    TLS_ECDH_RSA_WITH_ARIA_256_CBC_SHA384 = 0xC04F
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 188
try:
    TLS_RSA_WITH_ARIA_128_GCM_SHA256 = 0xC050
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 189
try:
    TLS_RSA_WITH_ARIA_256_GCM_SHA384 = 0xC051
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 190
try:
    TLS_DHE_RSA_WITH_ARIA_128_GCM_SHA256 = 0xC052
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 191
try:
    TLS_DHE_RSA_WITH_ARIA_256_GCM_SHA384 = 0xC053
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 192
try:
    TLS_DH_RSA_WITH_ARIA_128_GCM_SHA256 = 0xC054
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 193
try:
    TLS_DH_RSA_WITH_ARIA_256_GCM_SHA384 = 0xC055
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 194
try:
    TLS_DHE_DSS_WITH_ARIA_128_GCM_SHA256 = 0xC056
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 195
try:
    TLS_DHE_DSS_WITH_ARIA_256_GCM_SHA384 = 0xC057
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 196
try:
    TLS_DH_DSS_WITH_ARIA_128_GCM_SHA256 = 0xC058
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 197
try:
    TLS_DH_DSS_WITH_ARIA_256_GCM_SHA384 = 0xC059
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 198
try:
    TLS_DH_anon_WITH_ARIA_128_GCM_SHA256 = 0xC05A
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 199
try:
    TLS_DH_anon_WITH_ARIA_256_GCM_SHA384 = 0xC05B
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 200
try:
    TLS_ECDHE_ECDSA_WITH_ARIA_128_GCM_SHA256 = 0xC05C
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 201
try:
    TLS_ECDHE_ECDSA_WITH_ARIA_256_GCM_SHA384 = 0xC05D
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 202
try:
    TLS_ECDH_ECDSA_WITH_ARIA_128_GCM_SHA256 = 0xC05E
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 203
try:
    TLS_ECDH_ECDSA_WITH_ARIA_256_GCM_SHA384 = 0xC05F
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 204
try:
    TLS_ECDHE_RSA_WITH_ARIA_128_GCM_SHA256 = 0xC060
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 205
try:
    TLS_ECDHE_RSA_WITH_ARIA_256_GCM_SHA384 = 0xC061
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 206
try:
    TLS_ECDH_RSA_WITH_ARIA_128_GCM_SHA256 = 0xC062
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 207
try:
    TLS_ECDH_RSA_WITH_ARIA_256_GCM_SHA384 = 0xC063
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 208
try:
    TLS_PSK_WITH_ARIA_128_CBC_SHA256 = 0xC064
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 209
try:
    TLS_PSK_WITH_ARIA_256_CBC_SHA384 = 0xC065
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 210
try:
    TLS_DHE_PSK_WITH_ARIA_128_CBC_SHA256 = 0xC066
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 211
try:
    TLS_DHE_PSK_WITH_ARIA_256_CBC_SHA384 = 0xC067
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 212
try:
    TLS_RSA_PSK_WITH_ARIA_128_CBC_SHA256 = 0xC068
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 213
try:
    TLS_RSA_PSK_WITH_ARIA_256_CBC_SHA384 = 0xC069
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 214
try:
    TLS_PSK_WITH_ARIA_128_GCM_SHA256 = 0xC06A
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 215
try:
    TLS_PSK_WITH_ARIA_256_GCM_SHA384 = 0xC06B
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 216
try:
    TLS_DHE_PSK_WITH_ARIA_128_GCM_SHA256 = 0xC06C
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 217
try:
    TLS_DHE_PSK_WITH_ARIA_256_GCM_SHA384 = 0xC06D
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 218
try:
    TLS_RSA_PSK_WITH_ARIA_128_GCM_SHA256 = 0xC06E
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 219
try:
    TLS_RSA_PSK_WITH_ARIA_256_GCM_SHA384 = 0xC06F
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 220
try:
    TLS_ECDHE_PSK_WITH_ARIA_128_CBC_SHA256 = 0xC070
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 221
try:
    TLS_ECDHE_PSK_WITH_ARIA_256_CBC_SHA384 = 0xC071
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 222
try:
    TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_GCM_SHA256 = 0xC076
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 223
try:
    TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_GCM_SHA384 = 0xC077
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 224
try:
    TLS_ECDH_ECDSA_WITH_CAMELLIA_128_GCM_SHA256 = 0xC078
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 225
try:
    TLS_ECDH_ECDSA_WITH_CAMELLIA_256_GCM_SHA384 = 0xC079
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 226
try:
    TLS_ECDHE_RSA_WITH_CAMELLIA_128_GCM_SHA256 = 0xC07A
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 227
try:
    TLS_ECDHE_RSA_WITH_CAMELLIA_256_GCM_SHA384 = 0xC07B
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 228
try:
    TLS_ECDH_RSA_WITH_CAMELLIA_128_GCM_SHA256 = 0xC07C
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 229
try:
    TLS_ECDH_RSA_WITH_CAMELLIA_256_GCM_SHA384 = 0xC07D
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 230
try:
    TLS_PSK_WITH_CAMELLIA_128_GCM_SHA256 = 0xC07E
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 231
try:
    TLS_PSK_WITH_CAMELLIA_256_GCM_SHA384 = 0xC07F
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 232
try:
    TLS_DHE_PSK_WITH_CAMELLIA_128_GCM_SHA256 = 0xC080
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 233
try:
    TLS_DHE_PSK_WITH_CAMELLIA_256_GCM_SHA384 = 0xC081
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 234
try:
    TLS_RSA_PSK_WITH_CAMELLIA_128_GCM_SHA256 = 0xC082
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 235
try:
    TLS_RSA_PSK_WITH_CAMELLIA_256_GCM_SHA384 = 0xC083
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 236
try:
    TLS_ECDHE_PSK_WITH_CAMELLIA_128_GCM_SHA256 = 0xC084
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 237
try:
    TLS_ECDHE_PSK_WITH_CAMELLIA_256_GCM_SHA384 = 0xC085
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 238
try:
    TLS_RSA_WITH_AES_128_CCM = 0xC09C
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 239
try:
    TLS_RSA_WITH_AES_256_CCM = 0xC09D
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 240
try:
    TLS_DHE_RSA_WITH_AES_128_CCM = 0xC09E
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 241
try:
    TLS_DHE_RSA_WITH_AES_256_CCM = 0xC09F
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 242
try:
    TLS_RSA_WITH_AES_128_CCM_8 = 0xC0A0
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 243
try:
    TLS_RSA_WITH_AES_256_CCM_8 = 0xC0A1
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 244
try:
    TLS_DHE_RSA_WITH_AES_128_CCM_8 = 0xC0A2
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 245
try:
    TLS_DHE_RSA_WITH_AES_256_CCM_8 = 0xC0A3
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 246
try:
    TLS_PSK_WITH_AES_128_CCM = 0xC0A4
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 247
try:
    TLS_PSK_WITH_AES_256_CCM = 0xC0A5
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 248
try:
    TLS_DHE_PSK_WITH_AES_128_CCM = 0xC0A6
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 249
try:
    TLS_DHE_PSK_WITH_AES_256_CCM = 0xC0A7
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 250
try:
    TLS_PSK_WITH_AES_128_CCM_8 = 0xC0A8
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 251
try:
    TLS_PSK_WITH_AES_256_CCM_8 = 0xC0A9
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 252
try:
    TLS_PSK_DHE_WITH_AES_128_CCM_8 = 0xC0AA
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 253
try:
    TLS_PSK_DHE_WITH_AES_256_CCM_8 = 0xC0AB
except:
    pass

# ../libiec61850/hal/inc/tls_ciphers.h: 254
try:
    TLS_ECDHE_ECDSA_WITH_AES_128_CCM = 0xC0AC
except:
    pass

# ../libiec61850/hal/inc/tls_config.h: 79
try:
    TLS_EVENT_CODE_ALM_ALGO_NOT_SUPPORTED = 1
except:
    pass

# ../libiec61850/hal/inc/tls_config.h: 80
try:
    TLS_EVENT_CODE_ALM_UNSECURE_COMMUNICATION = 2
except:
    pass

# ../libiec61850/hal/inc/tls_config.h: 81
try:
    TLS_EVENT_CODE_ALM_CERT_UNAVAILABLE = 3
except:
    pass

# ../libiec61850/hal/inc/tls_config.h: 82
try:
    TLS_EVENT_CODE_ALM_BAD_CERT = 4
except:
    pass

# ../libiec61850/hal/inc/tls_config.h: 83
try:
    TLS_EVENT_CODE_ALM_CERT_SIZE_EXCEEDED = 5
except:
    pass

# ../libiec61850/hal/inc/tls_config.h: 84
try:
    TLS_EVENT_CODE_ALM_CERT_VALIDATION_FAILED = 6
except:
    pass

# ../libiec61850/hal/inc/tls_config.h: 85
try:
    TLS_EVENT_CODE_ALM_CERT_REQUIRED = 7
except:
    pass

# ../libiec61850/hal/inc/tls_config.h: 86
try:
    TLS_EVENT_CODE_ALM_HANDSHAKE_FAILED_UNKNOWN_REASON = 8
except:
    pass

# ../libiec61850/hal/inc/tls_config.h: 87
try:
    TLS_EVENT_CODE_WRN_INSECURE_TLS_VERSION = 9
except:
    pass

# ../libiec61850/hal/inc/tls_config.h: 88
try:
    TLS_EVENT_CODE_INF_SESSION_RENEGOTIATION = 10
except:
    pass

# ../libiec61850/hal/inc/tls_config.h: 89
try:
    TLS_EVENT_CODE_ALM_CERT_EXPIRED = 11
except:
    pass

# ../libiec61850/hal/inc/tls_config.h: 90
try:
    TLS_EVENT_CODE_ALM_CERT_REVOKED = 12
except:
    pass

# ../libiec61850/hal/inc/tls_config.h: 91
try:
    TLS_EVENT_CODE_ALM_CERT_NOT_CONFIGURED = 13
except:
    pass

# ../libiec61850/hal/inc/tls_config.h: 92
try:
    TLS_EVENT_CODE_ALM_CERT_NOT_TRUSTED = 14
except:
    pass

# ../libiec61850/hal/inc/tls_config.h: 93
try:
    TLS_EVENT_CODE_ALM_NO_CIPHER = 15
except:
    pass

# ../libiec61850/hal/inc/tls_config.h: 94
try:
    TLS_EVENT_CODE_INF_SESSION_ESTABLISHED = 16
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 533
try:
    IEC61850_SV_OPT_REFRESH_TIME = 1
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 536
try:
    IEC61850_SV_OPT_SAMPLE_SYNC = 2
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 539
try:
    IEC61850_SV_OPT_SAMPLE_RATE = 4
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 542
try:
    IEC61850_SV_OPT_DATA_SET = 8
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 545
try:
    IEC61850_SV_OPT_SECURITY = 16
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 547
try:
    IEC61850_SV_SMPMOD_SAMPLES_PER_PERIOD = 0
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 549
try:
    IEC61850_SV_SMPMOD_SAMPLES_PER_SECOND = 1
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 551
try:
    IEC61850_SV_SMPMOD_SECONDS_PER_SAMPLE = 2
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 689
try:
    GOCB_ELEMENT_GO_ENA = 1
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 692
try:
    GOCB_ELEMENT_GO_ID = 2
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 695
try:
    GOCB_ELEMENT_DATSET = 4
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 698
try:
    GOCB_ELEMENT_CONF_REV = 8
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 701
try:
    GOCB_ELEMENT_NDS_COMM = 16
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 704
try:
    GOCB_ELEMENT_DST_ADDRESS = 32
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 707
try:
    GOCB_ELEMENT_MIN_TIME = 64
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 710
try:
    GOCB_ELEMENT_MAX_TIME = 128
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 713
try:
    GOCB_ELEMENT_FIXED_OFFS = 256
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 716
try:
    GOCB_ELEMENT_ALL = 511
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1221
try:
    IEC61850_REASON_NOT_INCLUDED = 0
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1224
try:
    IEC61850_REASON_DATA_CHANGE = 1
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1227
try:
    IEC61850_REASON_QUALITY_CHANGE = 2
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1230
try:
    IEC61850_REASON_DATA_UPDATE = 4
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1233
try:
    IEC61850_REASON_INTEGRITY = 8
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1236
try:
    IEC61850_REASON_GI = 16
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1239
try:
    IEC61850_REASON_UNKNOWN = 32
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1244
try:
    RCB_ELEMENT_RPT_ID = 1
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1247
try:
    RCB_ELEMENT_RPT_ENA = 2
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1250
try:
    RCB_ELEMENT_RESV = 4
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1253
try:
    RCB_ELEMENT_DATSET = 8
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1256
try:
    RCB_ELEMENT_CONF_REV = 16
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1259
try:
    RCB_ELEMENT_OPT_FLDS = 32
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1262
try:
    RCB_ELEMENT_BUF_TM = 64
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1265
try:
    RCB_ELEMENT_SQ_NUM = 128
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1268
try:
    RCB_ELEMENT_TRG_OPS = 256
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1271
try:
    RCB_ELEMENT_INTG_PD = 512
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1274
try:
    RCB_ELEMENT_GI = 1024
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1277
try:
    RCB_ELEMENT_PURGE_BUF = 2048
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1280
try:
    RCB_ELEMENT_ENTRY_ID = 4096
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1283
try:
    RCB_ELEMENT_TIME_OF_ENTRY = 8192
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1286
try:
    RCB_ELEMENT_RESV_TMS = 16384
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 1289
try:
    RCB_ELEMENT_OWNER = 32768
except:
    pass

# ../libiec61850/hal/inc/hal_filesystem.h: 34
try:
    CONFIG_SYSTEM_FILE_SEPARATOR = '/'
except:
    pass

# ../libiec61850/src/mms/inc/mms_server.h: 341
try:
    MMS_LOGICAL_STATE_STATE_CHANGES_ALLOWED = 0
except:
    pass

# ../libiec61850/src/mms/inc/mms_server.h: 342
try:
    MMS_LOGICAL_STATE_NO_STATE_CHANGES_ALLOWED = 1
except:
    pass

# ../libiec61850/src/mms/inc/mms_server.h: 343
try:
    MMS_LOGICAL_STATE_LIMITED_SERVICES_PERMITTED = 2
except:
    pass

# ../libiec61850/src/mms/inc/mms_server.h: 344
try:
    MMS_LOGICAL_STATE_SUPPORT_SERVICES_ALLOWED = 3
except:
    pass

# ../libiec61850/src/mms/inc/mms_server.h: 346
try:
    MMS_PHYSICAL_STATE_OPERATIONAL = 0
except:
    pass

# ../libiec61850/src/mms/inc/mms_server.h: 347
try:
    MMS_PHYSICAL_STATE_PARTIALLY_OPERATIONAL = 1
except:
    pass

# ../libiec61850/src/mms/inc/mms_server.h: 348
try:
    MMS_PHYSICAL_STATE_INOPERATIONAL = 2
except:
    pass

# ../libiec61850/src/mms/inc/mms_server.h: 349
try:
    MMS_PHYSICAL_STATE_NEEDS_COMMISSIONING = 3
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 59
try:
    IEC61850_REPORTSETTINGS_RPT_ID = 1
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 60
try:
    IEC61850_REPORTSETTINGS_BUF_TIME = 2
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 61
try:
    IEC61850_REPORTSETTINGS_DATSET = 4
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 62
try:
    IEC61850_REPORTSETTINGS_TRG_OPS = 8
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 63
try:
    IEC61850_REPORTSETTINGS_OPT_FIELDS = 16
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 64
try:
    IEC61850_REPORTSETTINGS_INTG_PD = 32
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1736
try:
    IEC61850_SVCB_EVENT_ENABLE = 1
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1739
try:
    IEC61850_SVCB_EVENT_DISABLE = 0
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1774
try:
    IEC61850_GOCB_EVENT_ENABLE = 1
except:
    pass

# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1777
try:
    IEC61850_GOCB_EVENT_DISABLE = 0
except:
    pass

# ../libiec61850/hal/inc/platform_endian.h: 34
try:
    ORDER_LITTLE_ENDIAN = 1
except:
    pass

# /home/user/libiec61850/src/common/inc/libiec61850_platform_includes.h: 20
try:
    LIBIEC61850_VERSION = '1.6.0'
except:
    pass

# /home/user/libiec61850/src/common/inc/libiec61850_platform_includes.h: 23
try:
    CONFIG_DEFAULT_MMS_VENDOR_NAME = 'libiec61850.com'
except:
    pass

# /home/user/libiec61850/src/common/inc/libiec61850_platform_includes.h: 27
try:
    CONFIG_DEFAULT_MMS_MODEL_NAME = 'LIBIEC61850'
except:
    pass

# /home/user/libiec61850/src/common/inc/libiec61850_platform_includes.h: 31
try:
    CONFIG_DEFAULT_MMS_REVISION = LIBIEC61850_VERSION
except:
    pass

# /home/user/libiec61850/src/common/inc/libiec61850_platform_includes.h: 39
try:
    NDEBUG = 1
except:
    pass

# ../libiec61850/hal/inc/lib_memory.h: 15
def CALLOC(nmemb, size):
    return (Memory_calloc (nmemb, size))

# ../libiec61850/hal/inc/lib_memory.h: 16
def MALLOC(size):
    return (Memory_malloc (size))

# ../libiec61850/hal/inc/lib_memory.h: 17
def REALLOC(oldptr, size):
    return (Memory_realloc (oldptr, size))

# ../libiec61850/hal/inc/lib_memory.h: 18
def FREEMEM(ptr):
    return (Memory_free (ptr))

# ../libiec61850/hal/inc/lib_memory.h: 20
def GLOBAL_CALLOC(nmemb, size):
    return (Memory_calloc (nmemb, size))

# ../libiec61850/hal/inc/lib_memory.h: 21
def GLOBAL_MALLOC(size):
    return (Memory_malloc (size))

# ../libiec61850/hal/inc/lib_memory.h: 22
def GLOBAL_REALLOC(oldptr, size):
    return (Memory_realloc (oldptr, size))

# ../libiec61850/hal/inc/lib_memory.h: 23
def GLOBAL_FREEMEM(ptr):
    return (Memory_free (ptr))

# /home/user/libiec61850/src/goose/goose_receiver_internal.h: 28
try:
    ETH_BUFFER_LENGTH = 1518
except:
    pass

# /home/user/libiec61850/src/goose/goose_receiver_internal.h: 30
try:
    ETH_P_GOOSE = 0x88b8
except:
    pass

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 52
try:
    IEC61850_SV_SMPSYNC_NOT_SYNCHRONIZED = 0
except:
    pass

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 53
try:
    IEC61850_SV_SMPSYNC_SYNCED_UNSPEC_LOCAL_CLOCK = 1
except:
    pass

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 54
try:
    IEC61850_SV_SMPSYNC_SYNCED_GLOBAL_CLOCK = 2
except:
    pass

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 56
try:
    IEC61850_SV_SMPMOD_PER_NOMINAL_PERIOD = 0
except:
    pass

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 57
try:
    IEC61850_SV_SMPMOD_SAMPLES_PER_SECOND = 1
except:
    pass

# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 58
try:
    IEC61850_SV_SMPMOD_SECONDS_PER_SAMPLE = 2
except:
    pass

sMmsDomain = struct_sMmsDomain# ../libiec61850/src/mms/inc/mms_common.h: 137

sMmsAccessSpecifier = struct_sMmsAccessSpecifier# ../libiec61850/src/mms/inc/mms_common.h: 145

sMmsNamedVariableList = struct_sMmsNamedVariableList# ../libiec61850/src/mms/inc/mms_common.h: 155

sMmsVariableSpecification = struct_sMmsVariableSpecification# ../libiec61850/src/mms/inc/mms_types.h: 50

sMmsArray = struct_sMmsArray# ../libiec61850/src/mms/inc/mms_types.h: 55

sMmsStructure = struct_sMmsStructure# ../libiec61850/src/mms/inc/mms_types.h: 59

sMmsFloat = struct_sMmsFloat# ../libiec61850/src/mms/inc/mms_types.h: 66

uMmsTypeSpecification = union_uMmsTypeSpecification# ../libiec61850/src/mms/inc/mms_types.h: 53

sMmsValue = struct_sMmsValue# ../libiec61850/src/mms/inc/mms_value.h: 68

sLogStorage = struct_sLogStorage# ../libiec61850/src/logging/logging_api.h: 78

sLinkedList = struct_sLinkedList# ../libiec61850/src/common/inc/linked_list.h: 44

sTLSConfiguration = struct_sTLSConfiguration# ../libiec61850/hal/inc/tls_config.h: 38

sTLSConnection = struct_sTLSConnection# ../libiec61850/hal/inc/tls_config.h: 96

sAcseAuthenticationParameter = struct_sAcseAuthenticationParameter# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 64

sIsoConnectionParameters = struct_sIsoConnectionParameters# ../libiec61850/src/mms/inc/iso_connection_parameters.h: 141

sMmsConnectionParameters = struct_sMmsConnectionParameters# ../libiec61850/src/mms/inc/mms_client_connection.h: 54

sMmsConnection = struct_sMmsConnection# ../libiec61850/src/mms/inc/mms_client_connection.h: 75

sMmsJournalEntry = struct_sMmsJournalEntry# ../libiec61850/src/mms/inc/mms_client_connection.h: 1265

sMmsJournalVariable = struct_sMmsJournalVariable# ../libiec61850/src/mms/inc/mms_client_connection.h: 1271

sClientDataSet = struct_sClientDataSet# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 43

sClientReport = struct_sClientReport# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 46

sClientReportControlBlock = struct_sClientReportControlBlock# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 49

sClientGooseControlBlock = struct_sClientGooseControlBlock# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 52

sIedConnection = struct_sIedConnection# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 61

sClientSVControlBlock = struct_sClientSVControlBlock# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 555

sControlObjectClient = struct_sControlObjectClient# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2094

sFileDirectoryEntry = struct_sFileDirectoryEntry# /home/user/libiec61850/src/iec61850/inc/iec61850_client.h: 2851

sDirectoryHandle = struct_sDirectoryHandle# ../libiec61850/hal/inc/hal_filesystem.h: 31

sModelNode = struct_sModelNode# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 157

sDataAttribute = struct_sDataAttribute# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 184

sDataObject = struct_sDataObject# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 173

sLogicalNode = struct_sLogicalNode# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 165

sLogicalDevice = struct_sLogicalDevice# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 148

sIedModel = struct_sIedModel# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 135

sDataSet = struct_sDataSet# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 214

sReportControlBlock = struct_sReportControlBlock# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 222

sSettingGroupControlBlock = struct_sSettingGroupControlBlock# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 269

sGSEControlBlock = struct_sGSEControlBlock# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 283

sSVControlBlock = struct_sSVControlBlock# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 296

sLogControlBlock = struct_sLogControlBlock# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 244

sLog = struct_sLog# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 261

sDataSetEntry = struct_sDataSetEntry# /home/user/libiec61850/src/iec61850/inc/iec61850_model.h: 204

sMmsServer = struct_sMmsServer# ../libiec61850/src/mms/inc/mms_server.h: 44

sMmsServerConnection = struct_sMmsServerConnection# ../libiec61850/src/mms/inc/mms_server.h: 46

sIedServerConfig = struct_sIedServerConfig# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 71

sIedServer = struct_sIedServer# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 449

sClientConnection = struct_sClientConnection# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 454

sMmsGooseControlBlock = struct_sMmsGooseControlBlock# /home/user/libiec61850/src/iec61850/inc/iec61850_server.h: 1771

sBufferChain = struct_sBufferChain# /home/user/libiec61850/src/common/inc/buffer_chain.h: 31

sMap = struct_sMap# /home/user/libiec61850/src/common/inc/map.h: 32

sMemAllocLinkedList = struct_sMemAllocLinkedList# /home/user/libiec61850/src/common/inc/mem_alloc_linked_list.h: 38

sServerSocket = struct_sServerSocket# ../libiec61850/hal/inc/hal_socket.h: 44

sUdpSocket = struct_sUdpSocket# ../libiec61850/hal/inc/hal_socket.h: 46

sSocket = struct_sSocket# ../libiec61850/hal/inc/hal_socket.h: 49

sHandleSet = struct_sHandleSet# ../libiec61850/hal/inc/hal_socket.h: 52

sSNTPClient = struct_sSNTPClient# /home/user/libiec61850/src/common/inc/sntp_client.h: 32

sRSession = struct_sRSession# ../libiec61850/src/r_session/r_session.h: 34

sRSessionPayloadElement = struct_sRSessionPayloadElement# ../libiec61850/src/r_session/r_session.h: 68

sCommParameters = struct_sCommParameters# /home/user/libiec61850/src/goose/goose_publisher.h: 44

sGoosePublisher = struct_sGoosePublisher# /home/user/libiec61850/src/goose/goose_publisher.h: 48

sEthernetSocket = struct_sEthernetSocket# ../libiec61850/hal/inc/hal_ethernet.h: 34

sEthernetHandleSet = struct_sEthernetHandleSet# ../libiec61850/hal/inc/hal_ethernet.h: 37

sGooseSubscriber = struct_sGooseSubscriber# /home/user/libiec61850/src/goose/goose_receiver_internal.h: 37

sGooseReceiver = struct_sGooseReceiver# /home/user/libiec61850/src/goose/goose_receiver.h: 42

sSVPublisher = struct_sSVPublisher# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 63

sSVPublisher_ASDU = struct_sSVPublisher_ASDU# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 68

sSV_ASDU = struct_sSV_ASDU# /home/user/libiec61850/src/sampled_values/sv_publisher.h: 436

sSVSubscriber_ASDU = struct_sSVSubscriber_ASDU# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 97

sSVSubscriber = struct_sSVSubscriber# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 106

sSVReceiver = struct_sSVReceiver# /home/user/libiec61850/src/sampled_values/sv_subscriber.h: 122

sSerialPort = struct_sSerialPort# /home/user/libiec61850/hal/inc/hal_serial.h: 39

sThread = struct_sThread# /home/user/libiec61850/hal/inc/hal_thread.h: 38

sTLSSocket = struct_sTLSSocket# /home/user/libiec61850/hal/inc/tls_socket.h: 48

# No inserted files

# No prefix-stripping

