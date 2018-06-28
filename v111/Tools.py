#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
import hashlib
import os
import json
__all__ = ["md5"]
def md5(strs):
    m2 = hashlib.md5()
    m2.update(strs.encode("utf-8"))
    return m2.hexdigest()

def read_cache():
    if not os.path.exists("option.json"):
        j={
            "usrid":"",
            "usrpsd":"",
            "kch":"",
            "jsm":"",
            "kxh":""
        }
        with open("option.json","w")as f:
            f.write(json.dumps(j))
    with open("option.json")as f:
        js=f.read()
    js=json.loads(js)
    return js
def save_cache(a,b,c,d,e):
    j = {
        "usrid": a,
        "usrpsd": b,
        "kch": c,
        "jsm": d,
        "kxh": e
    }
    with open("option.json","w")as f:
        f.write(json.dumps(j))



if __name__=="__main__":
    save_cache("2","","","","")