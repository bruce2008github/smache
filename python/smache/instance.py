#!/usr/bin/env python

import native
from chunks import *
from exceptions import *

#
# The base entrace to the service.
#

class Smache(native.Smache):
    def create(self, fd, offset, length):
        # h = self.dcreate(fd, offset, length)
        pass
    
    def append(self):
        # h = self.dappend(fd, length)
        pass
    
    def read(self):
        # b = self.dread(h, fd, offset, length)
        pass
    
    def write(self):
        # h = self.dwrite(h, fd, offset, length)
        pass
    
    def remove(self, h):
        # h = self.dremove(h, offset, length)
        pass
    
    def truncate(self, h, length):
        # h = self.dtruncate(h, length)
        pass
    
    def map(self, n, h):
        # b = self.imap(n, h)
        pass

    def remap(self, n, h):
        # b = self.iremap(n, h)
        pass

    def unmap(self, n):
        # b = self.iunmap(n)
        pass
