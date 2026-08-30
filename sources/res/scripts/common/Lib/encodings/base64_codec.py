import codecs, base64

def base64_encode(input, errors=b'strict'):
    output = base64.encodestring(input)
    return (output, len(input))


def base64_decode(input, errors=b'strict'):
    output = base64.decodestring(input)
    return (output, len(input))


class Codec(codecs.Codec):

    def encode(self, input, errors=b'strict'):
        return base64_encode(input, errors)

    def decode(self, input, errors=b'strict'):
        return base64_decode(input, errors)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        return base64.encodestring(input)


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final=False):
        return base64.decodestring(input)


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(name=b'base64', encode=base64_encode, decode=base64_decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamwriter=StreamWriter, streamreader=StreamReader, _is_text_encoding=False)
