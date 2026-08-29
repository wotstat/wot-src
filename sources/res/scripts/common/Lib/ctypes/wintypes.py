from ctypes import *
BYTE = c_byte
WORD = c_ushort
DWORD = c_ulong
WCHAR = c_wchar
UINT = c_uint
INT = c_int
DOUBLE = c_double
FLOAT = c_float
BOOLEAN = BYTE
BOOL = c_long
from ctypes import _SimpleCData

class VARIANT_BOOL(_SimpleCData):
    _type_ = b'v'

    def __repr__(self):
        return b'%s(%r)' % (self.__class__.__name__, self.value)


ULONG = c_ulong
LONG = c_long
USHORT = c_ushort
SHORT = c_short
_LARGE_INTEGER = LARGE_INTEGER = c_longlong
_ULARGE_INTEGER = ULARGE_INTEGER = c_ulonglong
LPCOLESTR = LPOLESTR = OLESTR = c_wchar_p
LPCWSTR = LPWSTR = c_wchar_p
LPCSTR = LPSTR = c_char_p
LPCVOID = LPVOID = c_void_p
if sizeof(c_long) == sizeof(c_void_p):
    WPARAM = c_ulong
    LPARAM = c_long
elif sizeof(c_longlong) == sizeof(c_void_p):
    WPARAM = c_ulonglong
    LPARAM = c_longlong
ATOM = WORD
LANGID = WORD
COLORREF = DWORD
LGRPID = DWORD
LCTYPE = DWORD
LCID = DWORD
HANDLE = c_void_p
HACCEL = HANDLE
HBITMAP = HANDLE
HBRUSH = HANDLE
HCOLORSPACE = HANDLE
HDC = HANDLE
HDESK = HANDLE
HDWP = HANDLE
HENHMETAFILE = HANDLE
HFONT = HANDLE
HGDIOBJ = HANDLE
HGLOBAL = HANDLE
HHOOK = HANDLE
HICON = HANDLE
HINSTANCE = HANDLE
HKEY = HANDLE
HKL = HANDLE
HLOCAL = HANDLE
HMENU = HANDLE
HMETAFILE = HANDLE
HMODULE = HANDLE
HMONITOR = HANDLE
HPALETTE = HANDLE
HPEN = HANDLE
HRGN = HANDLE
HRSRC = HANDLE
HSTR = HANDLE
HTASK = HANDLE
HWINSTA = HANDLE
HWND = HANDLE
SC_HANDLE = HANDLE
SERVICE_STATUS_HANDLE = HANDLE

class RECT(Structure):
    _fields_ = [
     (
      b'left', c_long),
     (
      b'top', c_long),
     (
      b'right', c_long),
     (
      b'bottom', c_long)]


tagRECT = _RECTL = RECTL = RECT

class _SMALL_RECT(Structure):
    _fields_ = [
     (
      b'Left', c_short),
     (
      b'Top', c_short),
     (
      b'Right', c_short),
     (
      b'Bottom', c_short)]


SMALL_RECT = _SMALL_RECT

class _COORD(Structure):
    _fields_ = [
     (
      b'X', c_short),
     (
      b'Y', c_short)]


class POINT(Structure):
    _fields_ = [
     (
      b'x', c_long),
     (
      b'y', c_long)]


tagPOINT = _POINTL = POINTL = POINT

class SIZE(Structure):
    _fields_ = [
     (
      b'cx', c_long),
     (
      b'cy', c_long)]


tagSIZE = SIZEL = SIZE

def RGB(red, green, blue):
    return red + (green << 8) + (blue << 16)


class FILETIME(Structure):
    _fields_ = [
     (
      b'dwLowDateTime', DWORD),
     (
      b'dwHighDateTime', DWORD)]


_FILETIME = FILETIME

class MSG(Structure):
    _fields_ = [
     (
      b'hWnd', HWND),
     (
      b'message', c_uint),
     (
      b'wParam', WPARAM),
     (
      b'lParam', LPARAM),
     (
      b'time', DWORD),
     (
      b'pt', POINT)]


tagMSG = MSG
MAX_PATH = 260

class WIN32_FIND_DATAA(Structure):
    _fields_ = [
     (
      b'dwFileAttributes', DWORD),
     (
      b'ftCreationTime', FILETIME),
     (
      b'ftLastAccessTime', FILETIME),
     (
      b'ftLastWriteTime', FILETIME),
     (
      b'nFileSizeHigh', DWORD),
     (
      b'nFileSizeLow', DWORD),
     (
      b'dwReserved0', DWORD),
     (
      b'dwReserved1', DWORD),
     (
      b'cFileName', c_char * MAX_PATH),
     (
      b'cAlternateFileName', c_char * 14)]


class WIN32_FIND_DATAW(Structure):
    _fields_ = [
     (
      b'dwFileAttributes', DWORD),
     (
      b'ftCreationTime', FILETIME),
     (
      b'ftLastAccessTime', FILETIME),
     (
      b'ftLastWriteTime', FILETIME),
     (
      b'nFileSizeHigh', DWORD),
     (
      b'nFileSizeLow', DWORD),
     (
      b'dwReserved0', DWORD),
     (
      b'dwReserved1', DWORD),
     (
      b'cFileName', c_wchar * MAX_PATH),
     (
      b'cAlternateFileName', c_wchar * 14)]


__all__ = [
 25, 26, 27, 28, 29, 30, 31, 
 16, 32, 33, 34, 35, 36, 
 37, 38, 
 39, 40, 41, 42, 
 43, 44, 45, 46, 47, 48, 
 49, 50, 51, 52, 53, 
 54, 
 55, 56, 57, 58, 59, 60, 61, 
 62, 63, 64, 65, 66, 67, 
 68, 
 69, 70, 71, 72, 73, 
 74, 75, 76, 77, 78, 79, 
 18, 80, 11, 81, 
 5, 82, 83, 
 84, 85, 86, 13, 87, 
 88, 89, 90, 91, 92, 
 3, 93, 
 21, 23, 
 94, 95, 9, 96, 97, 
 98, 99, 7, 100, 101, 
 102, 103, 
 104]
