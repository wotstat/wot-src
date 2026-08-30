__all__ = [
 b'ValueError', b'pad', b'unpad']
from Crypto.Util.py3compat import *

def pad(data_to_pad, block_size, style=b'pkcs7'):
    padding_len = block_size - len(data_to_pad) % block_size
    if style == b'pkcs7':
        padding = bchr(padding_len) * padding_len
    elif style == b'x923':
        padding = bchr(0) * (padding_len - 1) + bchr(padding_len)
    elif style == b'iso7816':
        padding = bchr(128) + bchr(0) * (padding_len - 1)
    else:
        raise ValueError(b'Unknown padding style')
    return data_to_pad + padding


def unpad(padded_data, block_size, style=b'pkcs7'):
    pdata_len = len(padded_data)
    if pdata_len % block_size:
        raise ValueError(b'Input data is not padded')
    if style in (b'pkcs7', b'x923'):
        padding_len = bord(padded_data[-1])
        if padding_len < 1 or padding_len > min(block_size, pdata_len):
            raise ValueError(b'Padding is incorrect.')
        if style == b'pkcs7':
            if padded_data[-padding_len:] != bchr(padding_len) * padding_len:
                raise ValueError(b'PKCS#7 padding is incorrect.')
        elif padded_data[-padding_len:-1] != bchr(0) * (padding_len - 1):
            raise ValueError(b'ANSI X.923 padding is incorrect.')
    elif style == b'iso7816':
        padding_len = pdata_len - padded_data.rfind(bchr(128))
        if padding_len < 1 or padding_len > min(block_size, pdata_len):
            raise ValueError(b'Padding is incorrect.')
        if padding_len > 1 and padded_data[1 - padding_len:] != bchr(0) * (padding_len - 1):
            raise ValueError(b'ISO 7816-4 padding is incorrect.')
    else:
        raise ValueError(b'Unknown padding style')
    return padded_data[:-padding_len]
