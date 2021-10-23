import binascii
from struct import pack, unpack

flagSwapped = binascii.unhexlify('84f7180b84f837084f83906f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e6263376365616336ffae007d')
flag = pack('<10I', *unpack('>10I', flagSwapped[11:]))
print(flag[:-3])
