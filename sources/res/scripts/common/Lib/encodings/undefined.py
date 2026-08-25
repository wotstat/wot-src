import codecs

class Codec(codecs.Codec):

    def encode(self, input, errors=b'strict'):
        raise UnicodeError(b'undefined encoding')
        return

    def decode(self, input, errors=b'strict'):
        raise UnicodeError(b'undefined encoding')
        return


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        raise UnicodeError(b'undefined encoding')
        return


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final=False):
        raise UnicodeError(b'undefined encoding')
        return


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(name=b'undefined', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamwriter=StreamWriter, streamreader=StreamReader)
