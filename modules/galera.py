# Galera cluster check module for monitorViaHttp

# version 0.1
# 2014 Dec 22 - Kenny Gryp - <gryp@dakin.be>


import urlparse
import os
import json
import urllib2
import datetime


def parse(s):
    parsed_url = urlparse.urlparse(s.path)
    params_url = urlparse.parse_qs(parsed_url.query)
    (server_name, module_name) = parsed_url.path[1:].split('/',1)
    port = params_url['port'][0]
    clustercheck_url = "http://%s:%s/" % (server_name, port, )
    print clustercheck_url
    doCall(s, clustercheck_url)

def doCall(s, url):
    try:
        content = urllib2.urlopen(url).read()
    except:
        s.do_BAD_HEAD()
        s.wfile.write("ERROR: Node Cluster Check is BAD\n")
        return False
    s.wfile.write("OK: Cluster node is Synced\n")
    return True;