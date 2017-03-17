#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xcb35df31

# Compiled with Coconut version 1.2.0-post_dev25 [Colonel]

# Coconut Header: --------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
if _coconut_sys.version_info < (3,):
    py_chr, py_filter, py_hex, py_input, py_int, py_map, py_oct, py_open, py_print, py_range, py_str, py_zip = chr, filter, hex, input, int, map, oct, open, print, range, str, zip
    py_raw_input, py_xrange = raw_input, xrange
    _coconut_raw_input, _coconut_xrange, _coconut_int, _coconut_long, _coconut_print, _coconut_str, _coconut_unicode, _coconut_repr = raw_input, xrange, int, long, print, str, unicode, repr
    from future_builtins import *
    chr, str = unichr, unicode
    from io import open
    class range(object):
        __slots__ = ("_xrange",)
        if hasattr(_coconut_xrange, "__doc__"):
            __doc__ = _coconut_xrange.__doc__
        def __init__(self, *args):
            self._xrange = _coconut_xrange(*args)
        def __iter__(self):
            return _coconut.iter(self._xrange)
        def __reversed__(self):
            return _coconut.reversed(self._xrange)
        def __len__(self):
            return _coconut.len(self._xrange)
        def __contains__(self, elem):
            return elem in self._xrange
        def __getitem__(self, index):
            if _coconut.isinstance(index, _coconut.slice):
                start, stop, step = index.start, index.stop, index.step
                if start is None:
                    start = 0
                elif start < 0:
                    start += _coconut.len(self._xrange)
                if stop is None:
                    stop = _coconut.len(self._xrange)
                elif stop is not None and stop < 0:
                    stop += _coconut.len(self._xrange)
                if step is None:
                    step = 1
                return _coconut_map(self._xrange.__getitem__, self.__class__(start, stop, step))
            else:
                return self._xrange[index]
        def count(self, elem):
            """Count the number of times elem appears in the range."""
            return int(elem in self._xrange)
        def index(self, elem):
            """Find the index of elem in the range."""
            if elem not in self._xrange: raise _coconut.ValueError(_coconut.repr(elem) + " is not in range")
            start, _, step = self._xrange.__reduce_ex__(2)[1]
            return (elem - start) // step
        def __repr__(self):
            return _coconut.repr(self._xrange)[1:]
        def __reduce_ex__(self, protocol):
            return (self.__class__, self._xrange.__reduce_ex__(protocol)[1])
        def __reduce__(self):
            return self.__reduce_ex__(_coconut.pickle.HIGHEST_PROTOCOL)
        def __hash__(self):
            return _coconut.hash(self._xrange.__reduce__()[1])
        def __copy__(self):
            return self.__class__(*self._xrange.__reduce__()[1])
        def __eq__(self, other):
            reduction = self.__reduce__()
            return _coconut.isinstance(other, reduction[0]) and reduction[1] == other.__reduce__()[1]
    from collections import Sequence as _coconut_Sequence
    _coconut_Sequence.register(range)
    class int(_coconut_int):
        __slots__ = ()
        if hasattr(_coconut_int, "__doc__"):
            __doc__ = _coconut_int.__doc__
        class __metaclass__(type):
            def __instancecheck__(cls, inst):
                return _coconut.isinstance(inst, (_coconut_int, _coconut_long))
    from functools import wraps as _coconut_wraps
    @_coconut_wraps(_coconut_print)
    def print(*args, **kwargs):
        if _coconut.hasattr(_coconut_sys.stdout, "encoding") and _coconut_sys.stdout.encoding is not None:
            return _coconut_print(*(_coconut_unicode(x).encode(_coconut_sys.stdout.encoding) for x in args), **kwargs)
        else:
            return _coconut_print(*(_coconut_unicode(x).encode() for x in args), **kwargs)
    @_coconut_wraps(_coconut_raw_input)
    def input(*args, **kwargs):
        if _coconut.hasattr(_coconut_sys.stdout, "encoding") and _coconut_sys.stdout.encoding is not None:
            return _coconut_raw_input(*args, **kwargs).decode(_coconut_sys.stdout.encoding)
        else:
            return _coconut_raw_input(*args, **kwargs).decode()
    @_coconut_wraps(_coconut_repr)
    def repr(obj):
        if isinstance(obj, _coconut_unicode):
            return _coconut_repr(obj)[1:]
        else:
            return _coconut_repr(obj)
    ascii = repr
    def raw_input(*args):
        """Coconut uses Python 3 "input" instead of Python 2 "raw_input"."""
        raise _coconut.NameError('Coconut uses Python 3 "input" instead of Python 2 "raw_input"')
    def xrange(*args):
        """Coconut uses Python 3 "range" instead of Python 2 "xrange"."""
        raise _coconut.NameError('Coconut uses Python 3 "range" instead of Python 2 "xrange"')
    if _coconut_sys.version_info < (2, 7):
        import functools as _coconut_functools, copy_reg as _coconut_copy_reg
        def _coconut_new_partial(func, args, keywords):
            return _coconut_functools.partial(func, *(args if args is not None else ()), **(keywords if keywords is not None else {}))
        _coconut_copy_reg.constructor(_coconut_new_partial)
        def _coconut_reduce_partial(self):
            return (_coconut_new_partial, (self.func, self.args, self.keywords))
        _coconut_copy_reg.pickle(_coconut_functools.partial, _coconut_reduce_partial)
else:
    py_chr, py_filter, py_hex, py_input, py_int, py_map, py_oct, py_open, py_print, py_range, py_str, py_zip = chr, filter, hex, input, int, map, oct, open, print, range, str, zip

class _coconut(object):
    import collections, functools, imp, itertools, operator, types, copy, pickle
    if _coconut_sys.version_info < (3, 3):
        abc = collections
    else:
        import collections.abc as abc
    IndexError, NameError, ValueError, map, zip, dict, filter, frozenset, getattr, hasattr, hash, isinstance, iter, len, list, min, max, next, object, range, reversed, set, slice, str, sum, super, tuple, bytearray, repr = IndexError, NameError, ValueError, map, zip, dict, filter, frozenset, getattr, hasattr, hash, isinstance, iter, len, list, min, max, next, object, range, reversed, set, slice, str, sum, super, tuple, bytearray, staticmethod(repr)
class MatchError(Exception):
    """Pattern-matching error."""
    __slots__ = ("pattern", "value")
class _coconut_tail_call(Exception):
    __slots__ = ("func", "args", "kwargs")
    def __init__(self, func, *args, **kwargs):
        self.func, self.args, self.kwargs = func, args, kwargs
def _coconut_tco(func):
    @_coconut.functools.wraps(func)
    def tail_call_optimized_func(*args, **kwargs):
        call_func = func
        while True:
            if "_coconut_inside_tco" in kwargs:
                del kwargs["_coconut_inside_tco"]
                return call_func(*args, **kwargs)
            if hasattr(call_func, "_coconut_is_tco"):
                kwargs["_coconut_inside_tco"] = call_func._coconut_is_tco
            try:
                return call_func(*args, **kwargs)
            except _coconut_tail_call as tail_call:
                call_func, args, kwargs = tail_call.func, tail_call.args, tail_call.kwargs
    tail_call_optimized_func._coconut_is_tco = True
    return tail_call_optimized_func
def _coconut_igetitem(iterable, index):
    if isinstance(iterable, _coconut.range) or _coconut.hasattr(iterable, "__getitem__"):
        return iterable[index]
    elif not _coconut.isinstance(index, _coconut.slice):
        if index < 0:
            return _coconut.collections.deque(iterable, maxlen=-index)[0]
        else:
            return _coconut.next(_coconut.itertools.islice(iterable, index, index + 1))
    elif index.start is not None and index.start < 0 and (index.stop is None or index.stop < 0) and index.step is None:
        queue = _coconut.collections.deque(iterable, maxlen=-index.start)
        if index.stop is not None:
            queue = _coconut.tuple(queue)[:index.stop - index.start]
        return queue
    elif (index.start is not None and index.start < 0) or (index.stop is not None and index.stop < 0) or (index.step is not None and index.step < 0):
        return _coconut.tuple(iterable)[index]
    else:
        return _coconut.itertools.islice(iterable, index.start, index.stop, index.step)
class _coconut_compose(object):
    __slots__ = ("funcs")
    def __init__(self, *funcs):
        self.funcs = funcs
    def __call__(self, *args, **kwargs):
        arg = self.funcs[-1](*args, **kwargs)
        for f in self.funcs[-2::-1]:
            arg = f(arg)
        return arg
    def __repr__(self):
        return "..".join(_coconut.repr(f) for f in self.funcs)
    def __reduce__(self):
        return (_coconut_compose, self.funcs)
def _coconut_pipe(x, f): return f(x)
def _coconut_starpipe(xs, f): return f(*xs)
def _coconut_backpipe(f, x): return f(x)
def _coconut_backstarpipe(f, xs): return f(*xs)
def _coconut_bool_and(a, b): return a and b
def _coconut_bool_or(a, b): return a or b
def _coconut_minus(*args): return _coconut.operator.neg(*args) if len(args) < 2 else _coconut.operator.sub(*args)
@_coconut.functools.wraps(_coconut.itertools.tee)
def _coconut_tee(iterable, n=2):
    if n >= 0 and _coconut.isinstance(iterable, (_coconut.tuple, _coconut.frozenset)):
        return (iterable,)*n
    elif n > 0 and (_coconut.hasattr(iterable, "__copy__") or _coconut.isinstance(iterable, _coconut.abc.Sequence)):
        return (iterable,) + _coconut.tuple(_coconut.copy.copy(iterable) for i in range(n - 1))
    else:
        return _coconut.itertools.tee(iterable, n)
class _coconut_map(_coconut.map):
    __slots__ = ("_func", "_iters")
    if hasattr(_coconut.map, "__doc__"):
        __doc__ = _coconut.map.__doc__
    def __new__(cls, function, *iterables):
        new_map = _coconut.map.__new__(cls, function, *iterables)
        new_map._func, new_map._iters = function, iterables
        return new_map
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(self._func, *(_coconut_igetitem(i, index) for i in self._iters))
        else:
            return self._func(*(_coconut_igetitem(i, index) for i in self._iters))
    def __reversed__(self):
        return self.__class__(self._func, *(_coconut.reversed(i) for i in self._iters))
    def __len__(self):
        return _coconut.min(_coconut.len(i) for i in self._iters)
    def __repr__(self):
        return "map(" + _coconut.repr(self._func) + ", " + ", ".join((_coconut.repr(i) for i in self._iters)) + ")"
    def __reduce__(self):
        return (self.__class__, (self._func,) + self._iters)
    def __reduce_ex__(self, _):
        return self.__reduce__()
    def __copy__(self):
        return self.__class__(self._func, *_coconut_map(_coconut.copy.copy, self._iters))
class parallel_map(_coconut_map):
    """Multiprocessing implementation of map using concurrent.futures.
    Requires arguments to be pickleable."""
    __slots__ = ()
    def __iter__(self):
        from concurrent.futures import ProcessPoolExecutor
        with ProcessPoolExecutor() as executor:
            return _coconut.iter(_coconut.tuple(executor.map(self._func, *self._iters)))
    def __repr__(self):
        return "parallel_" + _coconut_map.__repr__(self)
class concurrent_map(_coconut_map):
    """Multithreading implementation of map using concurrent.futures."""
    __slots__ = ()
    def __iter__(self):
        from concurrent.futures import ThreadPoolExecutor
        from multiprocessing import cpu_count  # cpu_count() * 5 is the default Python 3 thread count
        with ThreadPoolExecutor(cpu_count() * 5) as executor:
            return _coconut.iter(_coconut.tuple(executor.map(self._func, *self._iters)))
    def __repr__(self):
        return "concurrent_" + _coconut_map.__repr__(self)
class filter(_coconut.filter):
    __slots__ = ("_func", "_iter")
    if hasattr(_coconut.filter, "__doc__"):
        __doc__ = _coconut.filter.__doc__
    def __new__(cls, function, iterable):
        new_filter = _coconut.filter.__new__(cls, function, iterable)
        new_filter._func = function
        new_filter._iter = iterable
        return new_filter
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(self._func, self._iter[index])
        else:
            raise _coconut.IndexError("filter does not support single indexing")
    def __reversed__(self):
        return self.__class__(self._func, _coconut.reversed(self._iter))
    def __repr__(self):
        return "filter(" + _coconut.repr(self._func) + ", " + _coconut.repr(self._iter) + ")"
    def __reduce__(self):
        return (self.__class__, (self._func, self_iter))
    def __reduce_ex__(self, _):
        return self.__reduce__()
    def __copy__(self):
        return self.__class__(self._func, _coconut.copy.copy(self._iter))
class zip(_coconut.zip):
    __slots__ = ("_iters",)
    if hasattr(_coconut.zip, "__doc__"):
        __doc__ = _coconut.zip.__doc__
    def __new__(cls, *iterables):
        new_zip = _coconut.zip.__new__(cls, *iterables)
        new_zip._iters = iterables
        return new_zip
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(*(_coconut_igetitem(i, index) for i in self._iters))
        else:
            return _coconut.tuple(_coconut_igetitem(i, index) for i in self._iters)
    def __reversed__(self):
        return self.__class__(*(_coconut.reversed(i) for i in self._iters))
    def __len__(self):
        return _coconut.min(_coconut.len(i) for i in self._iters)
    def __repr__(self):
        return "zip(" + ", ".join((_coconut.repr(i) for i in self._iters)) + ")"
    def __reduce__(self):
        return (self.__class__, self._iters)
    def __reduce_ex__(self, _):
        return self.__reduce__()
    def __copy__(self):
        return self.__class__(*_coconut_map(_coconut.copy.copy, self._iters))
class count(object):
    """count(start, step) returns an infinite iterator starting at start and increasing by step."""
    __slots__ = ("_start", "_step")
    def __init__(self, start=0, step=1):
        self._start, self._step = start, step
    def __iter__(self):
        while True:
            yield self._start
            self._start += self._step
    def __contains__(self, elem):
        return elem >= self._start and (elem - self._start) % self._step == 0
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice) and (index.start is None or index.start >= 0) and (index.stop is not None and index.stop >= 0):
            return _coconut_map(lambda x: self._start + x * self._step, _coconut.range(index.start if index.start is not None else 0, index.stop, index.step if index.step is not None else 1))
        elif index >= 0:
            return self._start + index * self._step
        else:
            raise _coconut.IndexError("count indices must be positive")
    def count(self, elem):
        """Count the number of times elem appears in the count."""
        return int(elem in self)
    def index(self, elem):
        """Find the index of elem in the count."""
        if elem not in self:
            raise _coconut.ValueError(_coconut.repr(elem) + " is not in count")
        return (elem - self._start) // self._step
    def __repr__(self):
        return "count(" + _coconut.str(self._start) + ", " + _coconut.str(self._step) + ")"
    def __hash__(self):
        return _coconut.hash((self._start, self._step))
    def __reduce__(self):
        return (self.__class__, (self._start, self._step))
    def __copy__(self):
        return self.__class__(self._start, self._step)
    def __eq__(self, other):
        reduction = self.__reduce__()
        return _coconut.isinstance(other, reduction[0]) and reduction[1] == other.__reduce__()[1]
def recursive_iterator(func):
    """Decorates a function by optimizing it for iterator recursion.
    Requires function arguments to be pickleable."""
    tee_store = {}
    @_coconut.functools.wraps(func)
    def recursive_iterator_func(*args, **kwargs):
        hashable_args_kwargs = _coconut.pickle.dumps((args, kwargs), _coconut.pickle.HIGHEST_PROTOCOL)
        if hashable_args_kwargs in tee_store:
            to_tee = tee_store[hashable_args_kwargs]
        else:
            to_tee = func(*args, **kwargs)
        tee_store[hashable_args_kwargs], to_return = _coconut_tee(to_tee)
        return to_return
    return recursive_iterator_func
def addpattern(base_func):
    """Decorator to add a new case to a pattern-matching function, where the new case is checked last."""
    def pattern_adder(func):
        @_coconut.functools.wraps(func)
        @_coconut_tco
        def add_pattern_func(*args, **kwargs):
            try:
                return base_func(*args, **kwargs)
            except _coconut_MatchError:
                raise _coconut_tail_call(func, *args, **kwargs)
        return add_pattern_func
    return pattern_adder
def prepattern(base_func):
    """Decorator to add a new case to a pattern-matching function, where the new case is checked first."""
    def pattern_prepender(func):
        return addpattern(func)(base_func)
    return pattern_prepender
class _coconut_partial(object):
    __slots__ = ("func", "_argdict", "_arglen", "_stargs", "keywords")
    if hasattr(_coconut.functools.partial, "__doc__"):
        __doc__ = _coconut.functools.partial.__doc__
    def __init__(self, func, argdict, arglen, *args, **kwargs):
        self.func, self._argdict, self._arglen, self._stargs, self.keywords = func, argdict, arglen, args, kwargs
    def __reduce__(self):
        return (self.__class__, (self.func, self._argdict, self._arglen) + self._stargs, self.keywords)
    def __setstate__(self, keywords):
        self.keywords = keywords
    @property
    def args(self):
        return _coconut.tuple(self._argdict.get(i) for i in _coconut.range(self._arglen)) + self._stargs
    def __call__(self, *args, **kwargs):
        callargs = []
        argind = 0
        for i in _coconut.range(self._arglen):
            if i in self._argdict:
                callargs.append(self._argdict[i])
            elif argind >= _coconut.len(args):
                raise TypeError("expected at least " + _coconut.str(self._arglen - _coconut.len(self._argdict)) + " argument(s) to " + _coconut.repr(self))
            else:
                callargs.append(args[argind])
                argind += 1
        callargs += self._stargs
        callargs += args[argind:]
        kwargs.update(self.keywords)
        return self.func(*callargs, **kwargs)
    def __repr__(self):
        args = []
        for i in _coconut.range(self._arglen):
            if i in self._argdict:
                args.append(_coconut.repr(self._argdict[i]))
            else:
                args.append("?")
        for arg in self._stargs:
            args.append(_coconut.repr(arg))
        return _coconut.repr(self.func) + "$(" + ", ".join(args) + ")"
def datamaker(data_type):
    """Returns base data constructor of passed data type."""
    return _coconut.functools.partial(_coconut.super(data_type, data_type).__new__, data_type)
def consume(iterable, keep_last=0):
    """Fully exhaust iterable and return the last keep_last elements."""
    return _coconut.collections.deque(iterable, maxlen=keep_last)  # fastest way to exhaust an iterator
_coconut_MatchError, map, reduce, takewhile, dropwhile, tee = MatchError, _coconut_map, _coconut.functools.reduce, _coconut.itertools.takewhile, _coconut.itertools.dropwhile, _coconut_tee

# Compiled Coconut: ------------------------------------------------------

moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}  # line 1

def parse_map(name):  # line 8
    with open(name, "r") as f :  # line 9
        map_text = f.read()  # line 10
    lines = map_text.splitlines()  # line 11
    empty_line = ['#'] * int((len(lines[0]) + 1) / 2 + 2)  # line 12
    lines = (_coconut.functools.partial(map, lambda x: ['#'] + x.split(' ') + ['#']))(lines)  # line 13
    return [empty_line] + list(lines) + [empty_line]  # line 14

def perform_char(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # line 15
    _coconut_match_check = False  # line 15
    if (1 <= _coconut.len(_coconut_match_to_args) <= 3) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "keypad" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 2, "pos" in _coconut_match_to_kwargs)) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) == 0):  # line 15
        _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("keypad")  # line 15
        _coconut_match_temp_1 = _coconut_match_to_args[2] if _coconut.len(_coconut_match_to_args) > 2 else _coconut_match_to_kwargs.pop("pos")  # line 15
        if (not _coconut_match_to_kwargs):  # line 15
            keypad = _coconut_match_temp_0  # line 15
            pos = _coconut_match_temp_1  # line 15
            _coconut_match_check = True  # line 15
    if not _coconut_match_check:  # line 15
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def perform_char([], keypad, pos) = pos'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))  # line 15
        _coconut_match_err.pattern = 'def perform_char([], keypad, pos) = pos'  # line 15
        _coconut_match_err.value = _coconut_match_to_args  # line 15
        raise _coconut_match_err  # line 15

    return pos  # line 16

@addpattern(perform_char)  # line 17
@_coconut_tco  # line 17
def perform_char(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # line 17
    _coconut_match_check = False  # line 17
    if (_coconut.len(_coconut_match_to_args) == 3) and ("keypad" not in _coconut_match_to_kwargs) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) >= 1) and (_coconut.isinstance(_coconut_match_to_args[2], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[2]) == 2):  # line 17
        _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("keypad")  # line 17
        rest = _coconut.list(_coconut_match_to_args[0][1:])  # line 17
        char = _coconut_match_to_args[0][0]  # line 17
        i = _coconut_match_to_args[2][0]  # line 17
        j = _coconut_match_to_args[2][1]  # line 17
        if (not _coconut_match_to_kwargs):  # line 17
            keypad = _coconut_match_temp_0  # line 17
            _coconut_match_check = True  # line 17
    if not _coconut_match_check:  # line 17
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def perform_char([char] + rest, keypad, (i, j)):'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))  # line 17
        _coconut_match_err.pattern = 'def perform_char([char] + rest, keypad, (i, j)):'  # line 17
        _coconut_match_err.value = _coconut_match_to_args  # line 17
        raise _coconut_match_err  # line 17

    delta_i, delta_j = moves[char]  # line 20
    if keypad[delta_i + i][delta_j + j] != "#":  # line 21
        raise _coconut_tail_call(perform_char, rest, keypad, (i + delta_i, j + delta_j))  # line 22
    else:  # line 23
        raise _coconut_tail_call(perform_char, rest, keypad, (i, j))  # line 24

def perform_line(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # line 25
    _coconut_match_check = False  # line 25
    if (1 <= _coconut.len(_coconut_match_to_args) <= 3) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "keypad" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 2, "pos" in _coconut_match_to_kwargs)) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) == 0):  # line 25
        _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("keypad")  # line 25
        _coconut_match_temp_1 = _coconut_match_to_args[2] if _coconut.len(_coconut_match_to_args) > 2 else _coconut_match_to_kwargs.pop("pos")  # line 25
        if (not _coconut_match_to_kwargs):  # line 25
            keypad = _coconut_match_temp_0  # line 25
            pos = _coconut_match_temp_1  # line 25
            _coconut_match_check = True  # line 25
    if not _coconut_match_check:  # line 25
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'def perform_line([], keypad, pos) = ""\'' " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))  # line 25
        _coconut_match_err.pattern = 'def perform_line([], keypad, pos) = ""'  # line 25
        _coconut_match_err.value = _coconut_match_to_args  # line 25
        raise _coconut_match_err  # line 25

    return ""  # line 26

@addpattern(perform_line)  # line 27
def perform_line(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # line 27
    _coconut_match_check = False  # line 27
    if (1 <= _coconut.len(_coconut_match_to_args) <= 3) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "keypad" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 2, "pos" in _coconut_match_to_kwargs)) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) >= 1):  # line 27
        _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("keypad")  # line 27
        _coconut_match_temp_1 = _coconut_match_to_args[2] if _coconut.len(_coconut_match_to_args) > 2 else _coconut_match_to_kwargs.pop("pos")  # line 27
        rest = _coconut.list(_coconut_match_to_args[0][1:])  # line 27
        line = _coconut_match_to_args[0][0]  # line 27
        if (not _coconut_match_to_kwargs):  # line 27
            keypad = _coconut_match_temp_0  # line 27
            pos = _coconut_match_temp_1  # line 27
            _coconut_match_check = True  # line 27
    if not _coconut_match_check:  # line 27
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def perform_line([line] + rest, keypad, pos):'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))  # line 27
        _coconut_match_err.pattern = 'def perform_line([line] + rest, keypad, pos):'  # line 27
        _coconut_match_err.value = _coconut_match_to_args  # line 27
        raise _coconut_match_err  # line 27

    i, j = perform_char(list(line), keypad, pos)  # line 30
    return keypad[i][j] + perform_line(rest, keypad, (i, j))  # line 31

@_coconut_tco  # line 32
def find_code(instructs, keypad, pos):  # line 32
    raise _coconut_tail_call(perform_line, instructs.splitlines(), keypad, pos)  # line 33

with open("slepice.txt", "r") as f :  # line 35
    instructs = f.read()  # line 36

(print)((_coconut_partial(find_code, {0: instructs, 2: (1, 1)}, 3))(parse_map('map1.txt')))  # line 38
(print)((_coconut_partial(find_code, {0: instructs, 2: (2, 1)}, 3))(parse_map('map2.txt')))  # line 39
