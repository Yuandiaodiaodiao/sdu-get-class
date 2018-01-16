#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
import hashlib
import re

def md5(strs):
    m2 = hashlib.md5()
    m2.update(strs.encode("utf-8"))
    return m2.hexdigest()
