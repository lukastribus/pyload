#
# Autogenerated by Thrift Compiler (0.9.0-dev)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:slots,dynamic
#

from thrift.Thrift import TType, TMessageType, TException

from thrift.protocol.TBase import TBase, TExceptionBase


class DownloadStatus(TBase):
  NA = 0
  Offline = 1
  Online = 2
  Queued = 3
  Paused = 4
  Finished = 5
  Skipped = 6
  Failed = 7
  Starting = 8
  Waiting = 9
  Downloading = 10
  TempOffline = 11
  Aborted = 12
  Decrypting = 13
  Processing = 14
  Custom = 15
  Unknown = 16

  _VALUES_TO_NAMES = {
    0: "NA",
    1: "Offline",
    2: "Online",
    3: "Queued",
    4: "Paused",
    5: "Finished",
    6: "Skipped",
    7: "Failed",
    8: "Starting",
    9: "Waiting",
    10: "Downloading",
    11: "TempOffline",
    12: "Aborted",
    13: "Decrypting",
    14: "Processing",
    15: "Custom",
    16: "Unknown",
  }

  _NAMES_TO_VALUES = {
    "NA": 0,
    "Offline": 1,
    "Online": 2,
    "Queued": 3,
    "Paused": 4,
    "Finished": 5,
    "Skipped": 6,
    "Failed": 7,
    "Starting": 8,
    "Waiting": 9,
    "Downloading": 10,
    "TempOffline": 11,
    "Aborted": 12,
    "Decrypting": 13,
    "Processing": 14,
    "Custom": 15,
    "Unknown": 16,
  }

class MediaType(TBase):
  All = 0
  Other = 1
  Audio = 2
  Image = 4
  Video = 8
  Document = 16
  Archive = 32

  _VALUES_TO_NAMES = {
    0: "All",
    1: "Other",
    2: "Audio",
    4: "Image",
    8: "Video",
    16: "Document",
    32: "Archive",
  }

  _NAMES_TO_VALUES = {
    "All": 0,
    "Other": 1,
    "Audio": 2,
    "Image": 4,
    "Video": 8,
    "Document": 16,
    "Archive": 32,
  }

class FileStatus(TBase):
  Ok = 0
  Missing = 1
  Remote = 2

  _VALUES_TO_NAMES = {
    0: "Ok",
    1: "Missing",
    2: "Remote",
  }

  _NAMES_TO_VALUES = {
    "Ok": 0,
    "Missing": 1,
    "Remote": 2,
  }

class PackageStatus(TBase):
  Ok = 0
  Paused = 1
  Remote = 2

  _VALUES_TO_NAMES = {
    0: "Ok",
    1: "Paused",
    2: "Remote",
  }

  _NAMES_TO_VALUES = {
    "Ok": 0,
    "Paused": 1,
    "Remote": 2,
  }

class Input(TBase):
  NA = 0
  Text = 1
  TextBox = 2
  Password = 3
  Bool = 4
  Click = 5
  Choice = 6
  Multiple = 7
  List = 8
  Table = 9

  _VALUES_TO_NAMES = {
    0: "NA",
    1: "Text",
    2: "TextBox",
    3: "Password",
    4: "Bool",
    5: "Click",
    6: "Choice",
    7: "Multiple",
    8: "List",
    9: "Table",
  }

  _NAMES_TO_VALUES = {
    "NA": 0,
    "Text": 1,
    "TextBox": 2,
    "Password": 3,
    "Bool": 4,
    "Click": 5,
    "Choice": 6,
    "Multiple": 7,
    "List": 8,
    "Table": 9,
  }

class Output(TBase):
  All = 0
  Notification = 1
  Captcha = 2
  Query = 4

  _VALUES_TO_NAMES = {
    0: "All",
    1: "Notification",
    2: "Captcha",
    4: "Query",
  }

  _NAMES_TO_VALUES = {
    "All": 0,
    "Notification": 1,
    "Captcha": 2,
    "Query": 4,
  }


class ProgressInfo(TBase):
  """
  Attributes:
   - fid
   - name
   - speed
   - eta
   - format_eta
   - bleft
   - size
   - format_size
   - percent
   - status
   - statusmsg
   - format_wait
   - wait_until
   - packageID
   - packageName
   - plugin
  """

  __slots__ = [ 
    'fid',
    'name',
    'speed',
    'eta',
    'format_eta',
    'bleft',
    'size',
    'format_size',
    'percent',
    'status',
    'statusmsg',
    'format_wait',
    'wait_until',
    'packageID',
    'packageName',
    'plugin',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'fid', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.I64, 'speed', None, None, ), # 3
    (4, TType.I32, 'eta', None, None, ), # 4
    (5, TType.STRING, 'format_eta', None, None, ), # 5
    (6, TType.I64, 'bleft', None, None, ), # 6
    (7, TType.I64, 'size', None, None, ), # 7
    (8, TType.STRING, 'format_size', None, None, ), # 8
    (9, TType.I16, 'percent', None, None, ), # 9
    (10, TType.I32, 'status', None, None, ), # 10
    (11, TType.STRING, 'statusmsg', None, None, ), # 11
    (12, TType.STRING, 'format_wait', None, None, ), # 12
    (13, TType.I64, 'wait_until', None, None, ), # 13
    (14, TType.I32, 'packageID', None, None, ), # 14
    (15, TType.STRING, 'packageName', None, None, ), # 15
    (16, TType.STRING, 'plugin', None, None, ), # 16
  )

  def __init__(self, fid=None, name=None, speed=None, eta=None, format_eta=None, bleft=None, size=None, format_size=None, percent=None, status=None, statusmsg=None, format_wait=None, wait_until=None, packageID=None, packageName=None, plugin=None,):
    self.fid = fid
    self.name = name
    self.speed = speed
    self.eta = eta
    self.format_eta = format_eta
    self.bleft = bleft
    self.size = size
    self.format_size = format_size
    self.percent = percent
    self.status = status
    self.statusmsg = statusmsg
    self.format_wait = format_wait
    self.wait_until = wait_until
    self.packageID = packageID
    self.packageName = packageName
    self.plugin = plugin


class ServerStatus(TBase):
  """
  Attributes:
   - pause
   - active
   - queue
   - total
   - speed
   - download
   - reconnect
  """

  __slots__ = [ 
    'pause',
    'active',
    'queue',
    'total',
    'speed',
    'download',
    'reconnect',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'pause', None, None, ), # 1
    (2, TType.I16, 'active', None, None, ), # 2
    (3, TType.I16, 'queue', None, None, ), # 3
    (4, TType.I16, 'total', None, None, ), # 4
    (5, TType.I64, 'speed', None, None, ), # 5
    (6, TType.BOOL, 'download', None, None, ), # 6
    (7, TType.BOOL, 'reconnect', None, None, ), # 7
  )

  def __init__(self, pause=None, active=None, queue=None, total=None, speed=None, download=None, reconnect=None,):
    self.pause = pause
    self.active = active
    self.queue = queue
    self.total = total
    self.speed = speed
    self.download = download
    self.reconnect = reconnect


class DownloadInfo(TBase):
  """
  Attributes:
   - url
   - plugin
   - hash
   - status
   - statusmsg
   - error
  """

  __slots__ = [ 
    'url',
    'plugin',
    'hash',
    'status',
    'statusmsg',
    'error',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'url', None, None, ), # 1
    (2, TType.STRING, 'plugin', None, None, ), # 2
    (3, TType.STRING, 'hash', None, None, ), # 3
    (4, TType.I32, 'status', None, None, ), # 4
    (5, TType.STRING, 'statusmsg', None, None, ), # 5
    (6, TType.STRING, 'error', None, None, ), # 6
  )

  def __init__(self, url=None, plugin=None, hash=None, status=None, statusmsg=None, error=None,):
    self.url = url
    self.plugin = plugin
    self.hash = hash
    self.status = status
    self.statusmsg = statusmsg
    self.error = error


class FileInfo(TBase):
  """
  Attributes:
   - fid
   - name
   - package
   - size
   - status
   - media
   - added
   - fileorder
   - download
  """

  __slots__ = [ 
    'fid',
    'name',
    'package',
    'size',
    'status',
    'media',
    'added',
    'fileorder',
    'download',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'fid', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.I32, 'package', None, None, ), # 3
    (4, TType.I64, 'size', None, None, ), # 4
    (5, TType.I32, 'status', None, None, ), # 5
    (6, TType.I32, 'media', None, None, ), # 6
    (7, TType.I64, 'added', None, None, ), # 7
    (8, TType.I16, 'fileorder', None, None, ), # 8
    (9, TType.STRUCT, 'download', (DownloadInfo, DownloadInfo.thrift_spec), None, ), # 9
  )

  def __init__(self, fid=None, name=None, package=None, size=None, status=None, media=None, added=None, fileorder=None, download=None,):
    self.fid = fid
    self.name = name
    self.package = package
    self.size = size
    self.status = status
    self.media = media
    self.added = added
    self.fileorder = fileorder
    self.download = download


class PackageStats(TBase):
  """
  Attributes:
   - linkstotal
   - linksdone
   - sizetotal
   - sizedone
  """

  __slots__ = [ 
    'linkstotal',
    'linksdone',
    'sizetotal',
    'sizedone',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I16, 'linkstotal', None, None, ), # 1
    (2, TType.I16, 'linksdone', None, None, ), # 2
    (3, TType.I64, 'sizetotal', None, None, ), # 3
    (4, TType.I64, 'sizedone', None, None, ), # 4
  )

  def __init__(self, linkstotal=None, linksdone=None, sizetotal=None, sizedone=None,):
    self.linkstotal = linkstotal
    self.linksdone = linksdone
    self.sizetotal = sizetotal
    self.sizedone = sizedone


class PackageInfo(TBase):
  """
  Attributes:
   - pid
   - name
   - folder
   - root
   - site
   - comment
   - password
   - added
   - status
   - packageorder
   - stats
   - fids
   - pids
  """

  __slots__ = [ 
    'pid',
    'name',
    'folder',
    'root',
    'site',
    'comment',
    'password',
    'added',
    'status',
    'packageorder',
    'stats',
    'fids',
    'pids',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'pid', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.STRING, 'folder', None, None, ), # 3
    (4, TType.I32, 'root', None, None, ), # 4
    (5, TType.STRING, 'site', None, None, ), # 5
    (6, TType.STRING, 'comment', None, None, ), # 6
    (7, TType.STRING, 'password', None, None, ), # 7
    (8, TType.I64, 'added', None, None, ), # 8
    (9, TType.I32, 'status', None, None, ), # 9
    (10, TType.I16, 'packageorder', None, None, ), # 10
    (11, TType.STRUCT, 'stats', (PackageStats, PackageStats.thrift_spec), None, ), # 11
    (12, TType.LIST, 'fids', (TType.I32,None), None, ), # 12
    (13, TType.LIST, 'pids', (TType.I32,None), None, ), # 13
  )

  def __init__(self, pid=None, name=None, folder=None, root=None, site=None, comment=None, password=None, added=None, status=None, packageorder=None, stats=None, fids=None, pids=None,):
    self.pid = pid
    self.name = name
    self.folder = folder
    self.root = root
    self.site = site
    self.comment = comment
    self.password = password
    self.added = added
    self.status = status
    self.packageorder = packageorder
    self.stats = stats
    self.fids = fids
    self.pids = pids


class PackageView(TBase):
  """
  Attributes:
   - root
   - files
   - packages
  """

  __slots__ = [ 
    'root',
    'files',
    'packages',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'root', (PackageInfo, PackageInfo.thrift_spec), None, ), # 1
    (2, TType.MAP, 'files', (TType.I32,None,TType.STRUCT,(FileInfo, FileInfo.thrift_spec)), None, ), # 2
    (3, TType.MAP, 'packages', (TType.I32,None,TType.STRUCT,(PackageInfo, PackageInfo.thrift_spec)), None, ), # 3
  )

  def __init__(self, root=None, files=None, packages=None,):
    self.root = root
    self.files = files
    self.packages = packages


class LinkStatus(TBase):
  """
  Attributes:
   - url
   - name
   - plugin
   - size
   - status
   - packagename
  """

  __slots__ = [ 
    'url',
    'name',
    'plugin',
    'size',
    'status',
    'packagename',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'url', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.STRING, 'plugin', None, None, ), # 3
    (4, TType.I64, 'size', None, None, ), # 4
    (5, TType.I32, 'status', None, None, ), # 5
    (6, TType.STRING, 'packagename', None, None, ), # 6
  )

  def __init__(self, url=None, name=None, plugin=None, size=None, status=None, packagename=None,):
    self.url = url
    self.name = name
    self.plugin = plugin
    self.size = size
    self.status = status
    self.packagename = packagename


class InteractionTask(TBase):
  """
  Attributes:
   - iid
   - input
   - data
   - output
   - default_value
   - title
   - description
   - plugin
  """

  __slots__ = [ 
    'iid',
    'input',
    'data',
    'output',
    'default_value',
    'title',
    'description',
    'plugin',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'iid', None, None, ), # 1
    (2, TType.I32, 'input', None, None, ), # 2
    (3, TType.LIST, 'data', (TType.STRING,None), None, ), # 3
    (4, TType.I32, 'output', None, None, ), # 4
    (5, TType.STRING, 'default_value', None, None, ), # 5
    (6, TType.STRING, 'title', None, None, ), # 6
    (7, TType.STRING, 'description', None, None, ), # 7
    (8, TType.STRING, 'plugin', None, None, ), # 8
  )

  def __init__(self, iid=None, input=None, data=None, output=None, default_value=None, title=None, description=None, plugin=None,):
    self.iid = iid
    self.input = input
    self.data = data
    self.output = output
    self.default_value = default_value
    self.title = title
    self.description = description
    self.plugin = plugin


class AddonInfo(TBase):
  """
  Attributes:
   - func_name
   - description
   - value
  """

  __slots__ = [ 
    'func_name',
    'description',
    'value',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'func_name', None, None, ), # 1
    (2, TType.STRING, 'description', None, None, ), # 2
    (3, TType.STRING, 'value', None, None, ), # 3
  )

  def __init__(self, func_name=None, description=None, value=None,):
    self.func_name = func_name
    self.description = description
    self.value = value


class ConfigItem(TBase):
  """
  Attributes:
   - name
   - display_name
   - description
   - type
   - default_value
   - value
  """

  __slots__ = [ 
    'name',
    'display_name',
    'description',
    'type',
    'default_value',
    'value',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRING, 'display_name', None, None, ), # 2
    (3, TType.STRING, 'description', None, None, ), # 3
    (4, TType.STRING, 'type', None, None, ), # 4
    (5, TType.STRING, 'default_value', None, None, ), # 5
    (6, TType.STRING, 'value', None, None, ), # 6
  )

  def __init__(self, name=None, display_name=None, description=None, type=None, default_value=None, value=None,):
    self.name = name
    self.display_name = display_name
    self.description = description
    self.type = type
    self.default_value = default_value
    self.value = value


class ConfigSection(TBase):
  """
  Attributes:
   - name
   - display_name
   - description
   - long_description
   - items
   - info
   - handler
  """

  __slots__ = [ 
    'name',
    'display_name',
    'description',
    'long_description',
    'items',
    'info',
    'handler',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRING, 'display_name', None, None, ), # 2
    (3, TType.STRING, 'description', None, None, ), # 3
    (4, TType.STRING, 'long_description', None, None, ), # 4
    (5, TType.LIST, 'items', (TType.STRUCT,(ConfigItem, ConfigItem.thrift_spec)), None, ), # 5
    (6, TType.LIST, 'info', (TType.STRUCT,(AddonInfo, AddonInfo.thrift_spec)), None, ), # 6
    (7, TType.LIST, 'handler', (TType.STRUCT,(InteractionTask, InteractionTask.thrift_spec)), None, ), # 7
  )

  def __init__(self, name=None, display_name=None, description=None, long_description=None, items=None, info=None, handler=None,):
    self.name = name
    self.display_name = display_name
    self.description = description
    self.long_description = long_description
    self.items = items
    self.info = info
    self.handler = handler


class EventInfo(TBase):
  """
  Attributes:
   - eventname
   - event_args
  """

  __slots__ = [ 
    'eventname',
    'event_args',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'eventname', None, None, ), # 1
    (2, TType.LIST, 'event_args', (TType.STRING,None), None, ), # 2
  )

  def __init__(self, eventname=None, event_args=None,):
    self.eventname = eventname
    self.event_args = event_args


class UserData(TBase):
  """
  Attributes:
   - name
   - email
   - role
   - permission
   - templateName
  """

  __slots__ = [ 
    'name',
    'email',
    'role',
    'permission',
    'templateName',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRING, 'email', None, None, ), # 2
    (3, TType.I32, 'role', None, None, ), # 3
    (4, TType.I32, 'permission', None, None, ), # 4
    (5, TType.STRING, 'templateName', None, None, ), # 5
  )

  def __init__(self, name=None, email=None, role=None, permission=None, templateName=None,):
    self.name = name
    self.email = email
    self.role = role
    self.permission = permission
    self.templateName = templateName


class AccountInfo(TBase):
  """
  Attributes:
   - plugin
   - loginname
   - valid
   - validuntil
   - trafficleft
   - maxtraffic
   - premium
   - activated
   - options
  """

  __slots__ = [ 
    'plugin',
    'loginname',
    'valid',
    'validuntil',
    'trafficleft',
    'maxtraffic',
    'premium',
    'activated',
    'options',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'plugin', None, None, ), # 1
    (2, TType.STRING, 'loginname', None, None, ), # 2
    (3, TType.BOOL, 'valid', None, None, ), # 3
    (4, TType.I64, 'validuntil', None, None, ), # 4
    (5, TType.I64, 'trafficleft', None, None, ), # 5
    (6, TType.I64, 'maxtraffic', None, None, ), # 6
    (7, TType.BOOL, 'premium', None, None, ), # 7
    (8, TType.BOOL, 'activated', None, None, ), # 8
    (9, TType.MAP, 'options', (TType.STRING,None,TType.STRING,None), None, ), # 9
  )

  def __init__(self, plugin=None, loginname=None, valid=None, validuntil=None, trafficleft=None, maxtraffic=None, premium=None, activated=None, options=None,):
    self.plugin = plugin
    self.loginname = loginname
    self.valid = valid
    self.validuntil = validuntil
    self.trafficleft = trafficleft
    self.maxtraffic = maxtraffic
    self.premium = premium
    self.activated = activated
    self.options = options


class AddonService(TBase):
  """
  Attributes:
   - func_name
   - description
   - media
   - package
  """

  __slots__ = [ 
    'func_name',
    'description',
    'media',
    'package',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'func_name', None, None, ), # 1
    (2, TType.STRING, 'description', None, None, ), # 2
    (3, TType.I16, 'media', None, None, ), # 3
    (4, TType.BOOL, 'package', None, None, ), # 4
  )

  def __init__(self, func_name=None, description=None, media=None, package=None,):
    self.func_name = func_name
    self.description = description
    self.media = media
    self.package = package


class OnlineCheck(TBase):
  """
  Attributes:
   - rid
   - data
  """

  __slots__ = [ 
    'rid',
    'data',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'rid', None, None, ), # 1
    (2, TType.MAP, 'data', (TType.STRING,None,TType.STRUCT,(LinkStatus, LinkStatus.thrift_spec)), None, ), # 2
  )

  def __init__(self, rid=None, data=None,):
    self.rid = rid
    self.data = data


class PackageDoesNotExists(TExceptionBase):
  """
  Attributes:
   - pid
  """

  __slots__ = [ 
    'pid',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'pid', None, None, ), # 1
  )

  def __init__(self, pid=None,):
    self.pid = pid

  def __str__(self):
    return repr(self)


class FileDoesNotExists(TExceptionBase):
  """
  Attributes:
   - fid
  """

  __slots__ = [ 
    'fid',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'fid', None, None, ), # 1
  )

  def __init__(self, fid=None,):
    self.fid = fid

  def __str__(self):
    return repr(self)


class UserDoesNotExists(TExceptionBase):
  """
  Attributes:
   - user
  """

  __slots__ = [ 
    'user',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'user', None, None, ), # 1
  )

  def __init__(self, user=None,):
    self.user = user

  def __str__(self):
    return repr(self)


class ServiceDoesNotExists(TExceptionBase):
  """
  Attributes:
   - plugin
   - func
  """

  __slots__ = [ 
    'plugin',
    'func',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'plugin', None, None, ), # 1
    (2, TType.STRING, 'func', None, None, ), # 2
  )

  def __init__(self, plugin=None, func=None,):
    self.plugin = plugin
    self.func = func

  def __str__(self):
    return repr(self)


class ServiceException(TExceptionBase):
  """
  Attributes:
   - msg
  """

  __slots__ = [ 
    'msg',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'msg', None, None, ), # 1
  )

  def __init__(self, msg=None,):
    self.msg = msg

  def __str__(self):
    return repr(self)

