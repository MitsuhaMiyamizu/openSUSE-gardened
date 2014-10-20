#!/usr/bin/python

# This plugin refreshes system-wide PaX flags after update finishes.

from sys import stderr
from zypp_plugin import Plugin
import json
import subprocess

DEBUG=True
LOGFILE='/var/log/YaST2/pax-plugin.log'

def dbg(args):
    if not DEBUG: return
    f=open(LOGFILE, "a+")
    f.write(args)
    f.write("\n")
    f.close()

class MyPlugin(Plugin):
  def PLUGINBEGIN(self, headers, body):
    self.actions = []
    self.commit_hook_supported = False
    dbg('--- Plugin begin')
    self.ack()

  def COMMITBEGIN(self, headers, body):
    self.commit_hook_supported = True
    dbg('commitbegin: %s\n%s\n' % (str(headers), str(body)))
    bs=json.loads(body)
    tsl=bs['TransactionStepList']
    for step in tsl:
        name=step['solvable']['n']
        stype=step['type']
        if stype == '+' or stype == 'M':
            dbg("Action %s: pax on %s" % (stype, name))
            self.actions.append(name)
    self.ack()

  def COMMITEND(self, headers, body):
    self.commit_hook_supported = True
    dbg('commitend: %s %s\n' % (str(headers), str(body)))
    bs=json.loads(body)
    tsl=bs['TransactionStepList']
    for step in tsl:
        name=step['solvable']['n']
        stype=step['type']
        if stype == '+' or stype == 'M':
            dbg("Action %s: pax on %s" % (stype, name))
            self.actions.append(name)
    self.ack()

  def PLUGINEND(self, headers, body):
    dbg('pluginend: %s %s\n' % (str(headers), str(body)))
    if self.commit_hook_supported:
        act=sorted(set(self.actions))
        dbg('actions: ' + str(act))
        # TODO: can do more fine-grained settings
    else:
        pass
    # unconditionally run pax flags update
    out=subprocess.Popen('/usr/sbin/linux-pax-flags --yes --xattr', shell=True, stdout=subprocess.PIPE).stdout
    dbg("".join(out.readlines()))
    out.close()
    self.ack()

plugin = MyPlugin()
plugin.main()
