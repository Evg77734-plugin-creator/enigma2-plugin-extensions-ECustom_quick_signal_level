#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Receiver information functions
#
#  Copyright (C) Evg77734, 2025
#

from os import path
from pathlib import Path
import glob
import sys
import six
import os
import re

mymess = 'Oops, no data.'

def getMyBoxType():
	try:
		box = ''
		if os.path.isfile('/proc/stb/info/boxtype'):
			box = open('/proc/stb/info/boxtype').read().strip().upper()
			if box.startswith('HD51'):
				box = 'AX 4K-BOX HD51'
			elif box.startswith('SF8008'):
				box = 'Octagon SF8008'
			elif box.startswith('h9combo'):
				box = 'Zgemma h9combo'
			elif box.startswith('HD61'):
				box = 'AX 4K-BOX HD61'
			elif box.startswith('ET11000'):
				box = 'GI ET11000 4K'
		elif os.path.isfile('/proc/stb/info/vumodel'):
			box = 'Vu+ ' + open('/proc/stb/info/vumodel').read().strip().capitalize()
		elif os.path.isfile('/proc/stb/info/model'):
			box = open('/proc/stb/info/model').read().strip().upper()
			if box.startswith('HD61'):
				box = 'AX 4K-BOX HD61'
		return box
	except:
		return mymess

def getMyBoxSoftware():
	try:
		software = ''
		if os.path.isfile('/etc/issue'):
			for line in open('/etc/issue'):
				software += line.capitalize().replace('Open vision enigma2 image for', '').replace('More information : https://openvision.tech', '').replace('%d, %t - (%s %r %m)', '').replace('release', 'r').replace('Welcome to openatv', '').replace('Welcome to opendroid', '').replace('Welcome to OpenHDF', '').replace('Welcome to openvix', '').replace('\n', '').replace('\l', '').replace('\\', '').strip()[:-1].capitalize()
			software = software.strip()
		if os.path.isfile('/etc/vtiversion.info'):
			for line in open('/etc/vtiversion.info'):
				software += line.split()[0].split('-')[0] + ' ' + line.split()[-1].replace('\n', '')
			software = software.strip()
		return software
	except:
		return mymess

def getMyBoxLinuxVersion():
	try:
		if os.path.isfile('/proc/version'):
			enigma = open('/proc/version').read().split(' (')[0]
		return enigma
	except:
		return mymess

def getMyBoxPythonVersion():
	try:
		return 'Python version ' + str(sys.version.split(' (')[0])
	except:
		return mymess

def getMyBoxCpuTemp():
	try:
		info = 'N/A'
		try:
			if os.path.exists('/proc/stb/sensors/temp0/value') and os.path.exists('/proc/stb/sensors/temp0/unit'):
				info = '%s%s' % (open('/proc/stb/sensors/temp0/value').read().strip('\n'), open('/proc/stb/sensors/temp0/unit').read().strip('\n'))
			elif os.path.exists('/proc/stb/fp/temp_sensor_avs'):
				info = '%s' % (open('/proc/stb/fp/temp_sensor_avs').read().strip('\n'))
			elif os.path.exists('/proc/stb/fp/temp_sensor'):
				info = '%s' % (open('/proc/stb/fp/temp_sensor').read().strip('\n'))
			elif os.path.exists('/sys/devices/virtual/thermal/thermal_zone0/temp'):
				info = '%s' % (open('/sys/devices/virtual/thermal/thermal_zone0/temp').read()[:2].strip('\n'))
			elif os.path.exists('/proc/hisi/msp/pm_cpu'):
				try:
					info = '%s%s' % (re.search('temperature = (\d+) degree', open('/proc/hisi/msp/pm_cpu').read()).group(1))
				except:
					pass
		except:
			info = 'N/A'
		info = '%s%s%s%s%s' % ('CPU: ', str(info), ' ', six.ensure_str(six.unichr(176)), 'C')
		return info
	except:
		return mymess

def getMyBoxTimeWorking():
	try:
		mtw = 'N/A'
		try:
			with open('/proc/uptime', 'r') as file:
				uptime_info = file.read().split()
		except:
			uptime_info = None
			mtw = 'N/A'
		if uptime_info is not None:
			total_seconds = float(uptime_info[0])
			MINUTE = 60
			HOUR = MINUTE * 60
			DAY = HOUR * 24
			days = int( total_seconds / DAY )
			hours = int( ( total_seconds % DAY ) / HOUR )
			minutes = int( ( total_seconds % HOUR ) / MINUTE )
			seconds = int( total_seconds % MINUTE )
			uptime = ''
			if days > 0:
				uptime += str(days) + ' ' + (days == 1 and 'day' or 'days' ) + ' '
			if len(uptime) > 0 or hours > 0:
				uptime += str(hours) + ' ' + (hours == 1 and 'hour' or 'hours' ) + ' '
			if len(uptime) > 0 or minutes > 0:
				uptime += str(minutes) + ' ' + (minutes == 1 and 'minute' or 'minutes' )
			mtw = 'Time working: %s' % uptime
		return mtw
	except:
		return mymess

def getMyBoxCpuInfo():
	try:
		cpu_count = 0
		info = cpu_speed = cpu_info = core = ''
		core = 'core'
		cores = 'cores'
		if os.path.isfile('/proc/cpuinfo'):
			for line in open('/proc/cpuinfo'):
				if 'system type' in line:
					info = line.split(':')[-1].split()[0].strip().strip('\n')
				elif 'cpu MHz' in line:
					cpu_speed =  line.split(':')[-1].strip().strip('\n')
				elif 'cpu type' in line:
					info = line.split(':')[-1].strip().strip('\n')
				elif 'model name' in line or 'Processor' in line:
					info = line.split(':')[-1].strip().strip('\n').replace('Processor ', '')
				elif line.startswith('processor'):
					cpu_count += 1
			if info.startswith('ARM') and os.path.isfile('/proc/stb/info/chipset'):
				for line in open('/proc/cpuinfo'):
					if 'model name' in line or 'Processor' in line:
						info = line.split(':')[-1].split()[0].strip().strip('\n')
						info = '%s (%s)' % (open('/proc/stb/info/chipset').readline().strip().lower().replace('hi3798mv200', 'Hi3798MV200').replace('bcm', 'BCM').replace('brcm', 'BCM').replace('7444', 'BCM7444').replace('7278', 'BCM7278'), info)
			if not cpu_speed:
				try:
					cpu_speed = int(open('/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq').read()) / 1000
				except:
					try:
						import binascii
						f = open('/sys/firmware/devicetree/base/cpus/cpu@0/clock-frequency', 'rb')
						clockfrequency = f.read()
						f.close()
						cpu_speed = "%s" % str(int(binascii.hexlify(clockfrequency), 16)/1000000)
					except:
						cpu_speed = '-'
			if cpu_info == '': 
				return 'CPU: ' + ('%s, %s MHz (%d %s)' % (info, cpu_speed, cpu_count, cpu_count > 1 and cores or core))
		else:
			return 'No info'
	except:
		return mymess

def getMyBoxCpuSpeed():
	try:
		info = 0
		try:
			for line in open('/proc/cpuinfo').readlines():
				line = [ x.strip() for x in line.strip().split(':') ]
				if line[0] == 'cpu MHz':
					info = '%1.0f' % float(line[1])
			if not info:
				try:
					info = int(open('/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq').read()) / 1000
				except:
					try:
						import binascii
						info = int(int(binascii.hexlify(open('/sys/firmware/devicetree/base/cpus/cpu@0/clock-frequency', 'rb').read()), 16) / 100000000) * 100
					except:
						info = '-'
			return ('CPU Speed: %s MHz' % info)
		except:
			return ('No info')
	except:
		return mymess

def getMyBoxCpuLoad():
	try:
		info = 'No info'
		try:
			if os.path.exists('/proc/loadavg'):
				l = open('/proc/loadavg', 'r')
				load = l.readline(18)
				l.close()
			info = load.replace('\n', '')
			info = info.split(' ')[0] + ' ' + info.split(' ')[1] + ' ' + info.split(' ')[2]
		except:
			load = 'No info'
		return ('CPU Load: %s' % info)
	except:
		return mymess

def myactiveskin():
	try:
		strtarget = 'Unknown skin'
		try:
			pathfolder = Path('/home/root/logs')
			onlyfreshfile = max(pathfolder.iterdir(), key=lambda x: x.stat().st_mtime)
		except:
			return 'Unknown skin'
		try:
			if os.path.exists(onlyfreshfile):
				with open(onlyfreshfile, "r") as file:
					contents = file.readlines()
				file.close()

			newstr = []

			for i in contents:
				newstr.append(i.rstrip())
				if '[StartEnigma]  Initialisation of Skins complete.' in i.rstrip():
					break
			maxlen = len(newstr)
			strtarget = newstr[maxlen-2]
			strtarget = strtarget.split('/usr/share/enigma2/')[1]
			strtarget = strtarget.split('/skin.xml')[0]
			strtarget = strtarget.replace('_', ' ')
		except:
			return 'Unknown skin'
		return 'Skin: ' + strtarget
	except:
		return mymess

def getMyBoxSkin():
	try:
		info = 'Unknown skin'
		if os.path.exists('/etc/enigma2/settings'):
			try:
				for line in open('/etc/enigma2/settings'):
					if 'config.skin.primary_skin' in line:
						info = ('Skin: ' + line.replace('/skin.xml', '').replace('\n', '').split('=')[1])
						return info
				return myactiveskin()
			except:
				info = 'Unknown skin'
		return info
	except:
		return mymess

def getMyBoxTuner(indata):
	try:
		my_dict = {}
		nimfile = ''
		line0 = '1'
		line1 = '2'
		try:
			nimfile = open("/proc/bus/nim_sockets")
		except IOError:
			return
		for line in nimfile:
			if not line:
				break
			line = line.strip()
			if 'Type:' in line:
				line0 = line.split('Type: ')[1]
			if 'Name:' in line:
				line1 = line.split('Name: ')[1]
			my_dict[line0] = line1
		my_dict.pop('1')
#		{'DVB-S2X': 'Si2166D', 'DVB-T2': 'Si2168'}
		mykey = my_dict.keys()
		for n in mykey:
			if n == ('DVB-S'):
				k = 'DVB-S'
			elif n == ('DVB-S2'):
				k = 'DVB-S2'
			elif n == ('DVB-S2X'):
				k = 'DVB-S2X'
			elif n == ('DVB-T'):
				k1 = 'DVB-T'
			elif n == ('DVB-T2'):
				k1 = 'DVB-T2'
			elif n == ('DVB-C'):
				k2 = 'DVB-C'
			elif n == ('DVB-C2'):
				k2 = 'DVB-C2'

		if indata.startswith('DVB-S'):
			indata = k
		elif indata.startswith('DVB-T'):
			indata = k1
		elif indata.startswith('DVB-C'):
			indata = k1

		rez = 'Tuner: ' + my_dict.get(str(indata)) + ' (' + str(indata) + ')'

		return rez
	except:
		return mymess

def mymainboxinfo(indata):
	rez = []
	rez.append(getMyBoxType())          #0
	rez.append(getMyBoxSoftware())      #1
	rez.append(getMyBoxLinuxVersion())  #2
	rez.append(getMyBoxPythonVersion()) #3
	rez.append(getMyBoxCpuTemp())       #4
	rez.append(getMyBoxTimeWorking())   #5
	rez.append(getMyBoxCpuInfo())       #6
	rez.append(getMyBoxCpuSpeed())      #7
	rez.append(getMyBoxCpuLoad())       #8
	rez.append(getMyBoxSkin())          #9
	rez.append(getMyBoxTuner(indata))   #10
	return rez

def printmymainboxinfo(indata):
	print(getMyBoxType())
	print(getMyBoxSoftware())
	print(getMyBoxLinuxVersion())
	print(getMyBoxPythonVersion())
	print(getMyBoxCpuTemp())
	print(getMyBoxTimeWorking())
	print(getMyBoxCpuInfo())
	print(getMyBoxCpuSpeed())
	print(getMyBoxCpuLoad())
	print(getMyBoxSkin())
	print(getMyBoxTuner(indata))
