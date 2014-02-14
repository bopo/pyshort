# -*- coding: utf-8 -*-
def shortByHex(url):
    '''url缩短'''
    import hashlib
    
    _seed = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _hex  = hashlib.md5(url).hexdigest()
    
    _output = []
    _hexLen = len(_hex)
    _subHexLen = _hexLen / 8
    
    for i in xrange(0, _subHexLen):
        _subHex = _hex[i*8:i*8+8]
        _subHex = 0x3FFFFFFF&int(1*('0x%s'%_subHex), 16)
        _o = []
        
        for n in xrange(0, 6):
            _index = 0x0000003D & _subHex
            _o.append(_seed[int(_index)])
            _subHex = _subHex >> 5

        _output.append(''.join(_o))
    
    return _output

print shortByHex("password")