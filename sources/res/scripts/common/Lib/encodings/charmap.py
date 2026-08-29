import codecs

class Codec(codecs.Codec):
    encode = codecs.charmap_encode
    decode = codecs.charmap_decode


class IncrementalEncoder(codecs.IncrementalEncoder):

    def __init__(self, errors=b'strict', mapping=None):
        codecs.IncrementalEncoder.__init__(self, errors)
        self.mapping = mapping
        return

    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, self.mapping)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):

    def __init__(self, errors=b'strict', mapping=None):
        codecs.IncrementalDecoder.__init__(self, errors)
        self.mapping = mapping
        return

    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, self.mapping)[0]


class StreamWriter(Codec, codecs.StreamWriter):

    def __init__(self, stream, errors=b'strict', mapping=None):
        codecs.StreamWriter.__init__(self, stream, errors)
        self.mapping = mapping
        return

    def encode(self, input, errors=b'strict'):
        return Codec.encode(input, errors, self.mapping)


class StreamReader(Codec, codecs.StreamReader):

    def __init__(self, stream, errors=b'strict', mapping=None):
        codecs.StreamReader.__init__(self, stream, errors)
        self.mapping = mapping
        return

    def decode(self, input, errors=b'strict'):
        return Codec.decode(input, errors, self.mapping)


def getregentry():
    return codecs.CodecInfo(name=b'charmap', encode=Codec.encode, decode=Codec.decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamwriter=StreamWriter, streamreader=StreamReader)
