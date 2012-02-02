# -*- coding: utf-8 -*-

"""
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License,
    or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, see <http://www.gnu.org/licenses/>.

    @author: zoidberg
"""
from urlparse import urlparse
import re
from time import time

from module.plugins.Hoster import Hoster
from module.utils import html_unescape, fixup, parseFileSize
from module.network.RequestFactory import getURL

def reSub(string, ruleslist):
    for r in ruleslist:
        rf, rt = r
        string = re.sub(rf, rt, string)
        #self.logDebug(rf, rt, string)
    return string
    
def parseHtmlTagAttrValue(attr_name, tag):
        m = re.search(r"%s\s*=\s*([\"']?)((?<=\")[^\"]+|(?<=')[^']+|[^\s\"'][^>\s]+)\1" % attr_name, tag)   
        return m.group(2) if m else ''

def parseFileInfo(self, url = '', html = '', infomode = False):    
    info = {"name" : url, "size" : 0, "status" : 3}

    if hasattr(self, "req") and self.req.http.code == '404':
        info['status'] = 1
    else:
        if not html and hasattr(self, "html"): html = self.html
        if isinstance(self.SH_BROKEN_ENCODING, (str, unicode)): 
            html = unicode(html, self.SH_BROKEN_ENCODING)
            if hasattr(self, "html"): self.html = html
        
        if hasattr(self, "FILE_OFFLINE_PATTERN") and re.search(self.FILE_OFFLINE_PATTERN, html):
            # File offline
            info['status'] = 1
        else:
            online = False
            for pattern in ("FILE_INFO_PATTERN", "FILE_NAME_PATTERN", "FILE_SIZE_PATTERN"):
                try:
                    info = dict(info, **re.search(getattr(self, pattern), html).groupdict())
                    online = True
                except AttributeError:
                    continue

            if online:
                # File online, return name and size
                info['status'] = 2
                if 'N' in info:
                    info['name'] = reSub(info['N'], self.FILE_NAME_REPLACEMENTS)
                if 'S' in info:
                    size = reSub(info['S'] + info['U'] if 'U' in info else info['S'], self.FILE_SIZE_REPLACEMENTS)
                    info['size'] = parseFileSize(size)
                elif isinstance(info['size'], (str, unicode)):
                    if 'units' in info: info['size'] += info['units']
                    info['size'] = parseFileSize(info['size'])

    if infomode:
        if hasattr(self, "pyfile"): 
            info = dict(info, **re.match(self.__pattern__, self.pyfile.url).groupdict())
        return info
    else:
        return info['name'], info['size'], info['status'], url

def create_getInfo(plugin):
    def getInfo(urls):
        for url in urls:
            file_info = parseFileInfo(plugin, url, getURL(reSub(url, plugin.FILE_URL_REPLACEMENTS), \
                decode = not plugin.SH_BROKEN_ENCODING))
            yield file_info
    return getInfo

def timestamp():
    return int(time()*1000)

class PluginParseError(Exception):
    def __init__(self, msg):
        Exception.__init__(self)
        self.value = 'Parse error (%s) - plugin may be out of date' % msg
    def __str__(self):
        return repr(self.value)

class SimpleHoster(Hoster):
    __name__ = "SimpleHoster"
    __version__ = "0.18"
    __pattern__ = None
    __type__ = "hoster"
    __description__ = """Base hoster plugin"""
    __author_name__ = ("zoidberg")
    __author_mail__ = ("zoidberg@mujmail.cz")
    """
    These patterns should be defined by each hoster:
    FILE_INFO_PATTERN = r'(?P<N>file_name) (?P<S>file_size) (?P<U>units)'
    or FILE_NAME_INFO = r'(?P<N>file_name)'
    and FILE_SIZE_INFO = r'(?P<S>file_size) (?P<U>units)'
    FILE_OFFLINE_PATTERN = r'File (deleted|not found)'
    TEMP_OFFLINE_PATTERN = r'Server maintainance'
    """

    FILE_SIZE_REPLACEMENTS = []
    FILE_NAME_REPLACEMENTS = [("&#?\w+;", fixup)]
    FILE_URL_REPLACEMENTS = []
    
    SH_BROKEN_ENCODING = False # Set to True or encoding name if encoding in http header is not correct
    SH_COOKIES = True
    SH_CHECK_TRAFFIC = False

    def setup(self):
        self.resumeDownload = self.multiDL = True if self.premium else False

    def process(self, pyfile):
        pyfile.url = reSub(pyfile.url, self.FILE_URL_REPLACEMENTS)
        self.html = self.load(pyfile.url, decode = not self.SH_BROKEN_ENCODING, cookies = self.SH_COOKIES)
        self.file_info = self.getFileInfo()
        if self.premium and (not self.SH_CHECK_TRAFFIC or self.checkTrafficLeft()):
            self.handlePremium()
        else:
            self.handleFree()

    def getFileInfo(self):
        self.logDebug("URL: %s" % self.pyfile.url)
        if hasattr(self, "TEMP_OFFLINE_PATTERN") and re.search(self.TEMP_OFFLINE_PATTERN, self.html):
            self.tempOffline()

        file_info = parseFileInfo(self, infomode = True)
        if file_info['status'] == 1:
            self.offline()
        elif file_info['status'] != 2:
            self.logDebug(file_info)
            self.parseError('File info')

        if file_info['name']:
            self.pyfile.name = file_info['name']
        else:
            self.pyfile.name = html_unescape(urlparse(self.pyfile.url).path.split("/")[-1])

        if file_info['size']:
            self.pyfile.size = file_info['size']
        else:
            self.logError("File size not parsed")

        self.logDebug("FILE NAME: %s FILE SIZE: %s" % (self.pyfile.name, self.pyfile.size))
        return file_info

    def handleFree(self):
        self.fail("Free download not implemented")

    def handlePremium(self):
        self.fail("Premium download not implemented")

    def parseError(self, msg):
        raise PluginParseError(msg)   

    def parseHtmlForm(self, attr_str):
        inputs = {}
        action = None 
        form = re.search(r"(?P<tag><form[^>]*%s[^>]*>)(?P<content>.*?)</form[^>]*>" % attr_str, self.html, re.S)
        if form:
            action = parseHtmlTagAttrValue("action", form.group('tag'))
            for input in re.finditer(r'(<(?:input|textarea)[^>]*>)', form.group('content')):
                name = parseHtmlTagAttrValue("name", input.group(1))
                if name:
                    inputs[name] = parseHtmlTagAttrValue("value", input.group(1)) 
        return action, inputs
    
    def checkTrafficLeft(self):                   
        traffic = self.account.getAccountInfo(self.user, True)["trafficleft"]
        size = self.pyfile.size / 1024
        self.logInfo("Filesize: %i KiB, Traffic left for user %s: %i KiB" % (size, self.user, traffic))               
        return  size <= traffic