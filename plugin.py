#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  E Custom quick signal level
#
#  Copyright (C) Evg77734, 2025-2026
#

from enigma import eServiceCenter, eServiceReference, iServiceInformation, eTimer, getDesktop, gRGB, ePoint
from Components.config import config, getConfigListEntry, ConfigSelection, ConfigSubsection, configfile
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
from Components.Sources.StaticText import StaticText
from Components.ConfigList import ConfigListScreen
from Components.ProgressBar import ProgressBar
from Plugins.Plugin import PluginDescriptor
from Components.ActionMap import ActionMap
from Screens.MessageBox import MessageBox
from Components.Language import language
from Components.Pixmap import Pixmap
from .lock_table_dvbs import *
from Components.Label import Label
from Screens.Screen import Screen
from threading import Thread
from skin import parseColor
from .myboxinfo import *
from time import sleep
from os import environ
from .my_skin import *
import xml.etree.ElementTree as ET
import subprocess
import gettext
import random
import time
import json
import sys
import six
import os

lang = language.getLanguage()
environ["LANGUAGE"] = lang[:2]
gettext.bindtextdomain("enigma2", resolveFilename(SCOPE_LANGUAGE))
gettext.textdomain("enigma2")
gettext.bindtextdomain("ECustom_quick_signal_level", "%s%s" % (resolveFilename(SCOPE_PLUGINS), "Extensions/ECustom_quick_signal_level/locale"))

def _(txt):
	t = gettext.dgettext("ECustom_quick_signal_level", txt)
	if t == txt:
		t = gettext.gettext(txt)
	return t

config.plugins.ecqslevel = ConfigSubsection()
config.plugins.ecqslevel.mindb = ConfigSelection(default="yes", choices = [
	("no", _("no")),
	("yes", _("yes"))])
config.plugins.ecqslevel.extinfo = ConfigSelection(default="yes", choices = [
	("no", _("no")),
	("yes", _("yes"))])

version = '2.2'

path1 = '/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/cpu.sh'
path2 = '/tmp/cu35787.txt'

global newdb, newdeltadb, my_dict_newdb, my_dict_newdeltadb, view_type, MyBoxType, MyBoxTuner
newdb = 16.0
newdeltadb = 0.0
my_dict_newdb = {"default": 16.0}
my_dict_newdeltadb = {"default": 0.0}
view_type = 'accepted'
MyBoxType = ''
MyBoxTuner = ''

class ECustomquicksignallevel(Screen):
	sz_w = getDesktop(0).size().width()
	if sz_w == 1920:
		skin = ECustomsignallevel_FHD
	else:
		skin = ECustomsignallevel_HD

	def __init__(self, session):
		Screen.__init__(self, session)
		self.setTitle(_(" "))
		self["snr_label"] = Label(" SNR")
		self["snr_bar"] = ProgressBar()
		self["agc_label"] = Label(" AGC")
		self["agc_bar"] = ProgressBar()
		self["snr_data"] = Label(" N/A")
		self["snrdb_data"] = Label(" N/A")
		self["agc1_data"] = Label(" N/A")
		self["agc_data"] = Label(" N/A")
		self["ber_data"] = Label(" N/A")
		self["lock_data"] = Label(" N/A")
		self["sat_chname"] = Label(" N/A")
		self["sat_prov"] = Label(" N/A")
		self["sat_name"] = Label(" N/A")
		self["sat_trdatas"] = Label(" N/A")
		self["db_default1"] = Label(" N/A")
		self["db_default2"] = Label(" N/A")
		self["db_custom1"] = Label(" N/A")
		self["db_custom2"] = Label(" N/A")
		self["right_arrow"] = Label(" ")
		self["left_arrow"] = Label(" ")
		self["up_arrow"] = Label(" ")
		self["down_arrow"] = Label(" ")
		self["my_box"] = Label(" N/A")
		self["my_tuner"] = Label(" N/A")
		self["test_label"] = Label(" ")
		self.n = 0
		self.m = 0
		self.deltat = 25
		self.counter = 0
		self["remote"] = Pixmap()
		self["circle"] = Pixmap()
		self["min_db"] = Pixmap()
		self["shortcuts"] = ActionMap(["ShortcutActions", "WizardActions", "ColorActions", "DirectionActions", "HelpActions", "EPGSelectActions", "MenuActions"],
		{
			"cancel": self.cancel,
			"back": self.cancel,
			"red": self.cancel,
			"ok": self.action,
			"green": self.greenbutton,
			"right": self.right_key,
			"left": self.left_key,
			"up": self.up_key,
			"down": self.down_key,
			"info": self.about,
			"menu": self.config,
			})

		self.snr_db, self.snr_percent, self.ber, self.agc, self.lock = self.getSignalFromFrontend_def()

		Thread0 = Thread(target=self.mylevel0)
		Thread0.start()

		Thread1 = Thread(target=self.mylevel1)
		Thread1.start()

		Thread2 = Thread(target=self.clear_dadas)
		Thread2.start()

		self.onShow.append(self.Setfirstdatas)

	def config (self):
		self.session.open(ConfigECQSL)

	def clear_dadas(self):
		self.moveTimer2 = eTimer()
		self.moveTimer2.callback.append(self.clear_exe)
		self.moveTimer2.start(10000, 1)

	def clear_exe(self):
		self.moveTimer2.start(5000, 1)
		self["up_arrow"].setText(str(' '))
		self["down_arrow"].setText(str(' '))
		self["right_arrow"].setText(str(' '))
		self["left_arrow"].setText(str(' '))

	def Setfirstdatas(self):
		global newdb, newdeltadb, my_dict_newdb, my_dict_newdeltadb
		c2, p2, n2, t2 = self.getBasicInfo()
		path1 = "/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/my_data1.json"
		path2 = "/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/my_data2.json"
		mykey = str(t2) + '*' + str(n2)
		with open(path1, "r", encoding="utf-8") as f:
			my_dict_newdb = json.load(f)
		with open(path2, "r", encoding="utf-8") as f:
			my_dict_newdeltadb = json.load(f)
		try:
			newdb = my_dict_newdb[mykey]
		except:
			newdb = my_dict_newdb.get("default")
		try:
			newdeltadb = my_dict_newdeltadb[mykey]
		except:
			newdeltadb = my_dict_newdeltadb.get("default")

		self["snr_bar"].setValue(int(0))
		self["agc_bar"].setValue(int(0))
		sz_w = getDesktop(0).size().width()
		if sz_w == 1920:
			self["remote"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/images/150x150.png")
			self["remote"].instance.show()
			self["circle"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/images/circle.png")
			self["circle"].instance.show()
			if config.plugins.ecqslevel.mindb.value == 'yes':
				self["min_db"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/images/min_level.png")
				self["min_db"].instance.show()
				self["min_db"].move(ePoint(25, 70))
				a, b, c = initial_data(str(t2))
				if "DVB-S" in str(a):
					mdb = minimum_db(a, b, c)
					mpercent = int(float(float(mdb) * 100 / 16))
					posx = int(float(1850 * float(mdb) / 16)) + 25
					self["test_label"].setText(str(mdb)+ " dB" + " / " + str(mpercent) + " %")
					self["min_db"].move(ePoint(posx, 70))
					self["test_label"].move(ePoint((posx + 35), 70))
		else:
			self["remote"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/images/150x150_1.png")
			self["remote"].instance.show()
			self["circle"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/images/circle_1.png")
			self["circle"].instance.show()
			if config.plugins.ecqslevel.mindb.value == 'yes':
				self["min_db"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/images/min_level_1.png")
				self["min_db"].instance.show()
				self["min_db"].move(ePoint(16, 47))
				a, b, c = initial_data(str(t2))
				if "DVB-S" in str(a):
					mdb = minimum_db(a, b, c)
					mpercent = int(float(float(mdb) * 100 / 16))
					posx = int(float(1233 * float(mdb) / 16)) + 16
					self["test_label"].setText(str(mdb)+ " dB" + " / " + str(mpercent) + " %")
					self["min_db"].move(ePoint(posx, 47))
					self["test_label"].move(ePoint((posx + 25), 47))

	def setmydatas(self):
		global newdb, newdeltadb
		try:
			self["db_custom1"].setText(str('SNR 100% = ' + "%.1f" % (newdb) + ' dB.'))
		except:
			self["db_custom1"].setText(str('SNR 100% = N/A dB.'))
		try:
			if newdeltadb > 0:
				self["db_custom2"].setText(str('Correction: +' + str(newdeltadb) + ' dB.'))
			elif newdeltadb == 0:
				self["db_custom2"].setText(str('Correction: ' + str(newdeltadb) + ' dB.'))
			else:
				self["db_custom2"].setText(str('Correction: ' + str(newdeltadb) + ' dB.'))
		except:
			self["db_custom2"].setText(str('Correction: - N/A dB.'))

	def up_key(self):
		global newdb, newdeltadb
		self["up_arrow"].setText(str('+1'))
		self["down_arrow"].setText(str(' '))
		self["right_arrow"].setText(str(' '))
		self["left_arrow"].setText(str(' '))
		newdeltadb = float("%.1f" % (newdeltadb + 0.1))
		self.setmydatas()

	def down_key(self):
		global newdb, newdeltadb
		self["down_arrow"].setText(str('-1'))
		self["right_arrow"].setText(str(' '))
		self["left_arrow"].setText(str(' '))
		self["up_arrow"].setText(str(' '))
		newdeltadb = float("%.1f" % (newdeltadb - 0.1))
		self.setmydatas()

	def right_key(self):
		global newdb, newdeltadb
		self["right_arrow"].setText(str('+1'))
		self["down_arrow"].setText(str(' '))
		self["left_arrow"].setText(str(' '))
		self["up_arrow"].setText(str(' '))
		newdb = newdb + 0.1
		self.setmydatas()

	def left_key(self):
		global newdb, newdeltadb
		self["left_arrow"].setText(str('-1'))
		self["down_arrow"].setText(str(' '))
		self["right_arrow"].setText(str(' '))
		self["up_arrow"].setText(str(' '))
		newdb = newdb - 0.1
		self.setmydatas()

	def Setdatas(self):
		global newdb, newdeltadb, MyBoxType, MyBoxTuner
		c1, p1, n1, t1 = self.getBasicInfo()
		self["sat_chname"].instance.clearForegroundColor()
		self["sat_chname"].instance.setForegroundColor(parseColor('green'))
		self["sat_chname"].setText(str(c1))
		self["sat_prov"].instance.clearForegroundColor()
		self["sat_prov"].instance.setForegroundColor(parseColor('green'))
		self["sat_prov"].setText(str(p1))
		self["sat_trdatas"].instance.clearForegroundColor()
		self["sat_trdatas"].instance.setForegroundColor(parseColor('yellow'))
		self["sat_trdatas"].setText(str(t1))
		self["sat_name"].instance.clearForegroundColor()
		self["sat_name"].instance.setForegroundColor(parseColor('yellow'))
		self["sat_name"].setText(str(n1))
		self["my_box"].setText(str(MyBoxType))
		self["my_tuner"].setText(str(MyBoxTuner.split('Tuner: ')[1]))
		try:
			self["db_default1"].setText(str('SNR 100% = ' + "%.1f" % (self.snr_db / self.snr_percent * 100) + ' dB.'))
		except:
			self["db_default1"].setText(str('SNR 100% = N/A dB.'))
		self["db_default2"].setText(str('Correction: 0.00 dB.'))

		try:
			self["db_custom1"].setText(str('SNR 100% = ' + "%.1f" % (newdb) + ' dB.'))
		except:
			self["db_custom1"].setText(str('SNR 100% = N/A dB.'))
		try:
			if newdeltadb > 0:
				self["db_custom2"].setText(str('Correction: +' + str(newdeltadb) + ' dB.'))
			elif newdeltadb == 0:
				self["db_custom2"].setText(str('Correction: ' + str(newdeltadb) + ' dB.'))
			else:
				self["db_custom2"].setText(str('Correction: ' + str(newdeltadb) + ' dB.'))				
		except:
			self["db_custom2"].setText(str('Correction: - N/A dB.'))

	def mylevel0(self):
		self.moveTimer0 = eTimer()
		self.moveTimer0.callback.append(self.levelshow0)
		self.moveTimer0.start(100, 1)

	def levelshow0(self):
		global newdb
		self.moveTimer0.start(self.deltat, 1)
		self["snr_bar"].setValue(int(self.n))
		self["snr_data"].setText(str(self.n) + ' %')
		bd = self.snr_percent - self.n
		if bd < 0:
			bd = 0
		self["ber_data"].setText(str(bd) + ' %')
		try:
			rez = (self.snr_db / self.snr_percent) * self.n
		except:
			rez = 0
		self["snrdb_data"].setText(str("%.1f" % rez) + ' dB')
		self.n = self.n + 1
		if self.n >= (round(self.snr_db / newdb * 100)):
			Threadx = Thread(target=self.mylevelx)
			Threadx.start()
			self.Setdatas()
			self.moveTimer0.stop()

	def mylevel1(self):
		self.moveTimer1 = eTimer()
		self.moveTimer1.callback.append(self.levelshow1)
		self.moveTimer1.start(100, 1)

	def levelshow1(self):
		self.moveTimer1.start(self.deltat, 1)
		self["agc_bar"].setValue(int(self.m))
		self["agc_data"].setText(str(self.m) + ' %')
		self["agc1_data"].setText(str(self.m) + ' %')
		self.m = self.m + 1
		if self.m >= self.agc:
			self.moveTimer1.stop()

	def mylevelx(self):
		self.moveTimerx = eTimer()
		self.moveTimerx.callback.append(self.levelshowx)
		self.moveTimerx.start(100, 1)

	def levelshowx(self):
		self.moveTimerx.start(1000, 1)
		self.datashow()

	def datashow(self):
		global view_type
		if view_type == 'accepted':
			snr_db, snr_percent, ber, agc, lock = self.getSignalFromFrontend()
		else:
			snr_db, snr_percent, ber, agc, lock = self.getSignalFromFrontend_def()
		self["snr_bar"].setValue(int(snr_percent))
		self["agc_bar"].setValue(int(agc))
		self["snr_data"].setText(str(snr_percent) + ' %')
		self["agc_data"].setText(str(agc) + ' %')
		self["agc1_data"].setText(str(agc) + ' %')
		self["snrdb_data"].setText(str("%.1f" % snr_db) + ' dB')
		self["ber_data"].setText(str(ber) + ' %')
		if lock == True:
			self["lock_data"].instance.clearForegroundColor()
			self["lock_data"].instance.setForegroundColor(parseColor('green'))
			self["lock_data"].setText(str('LOCK'))
		else:
			self["lock_data"].instance.clearForegroundColor()
			self["lock_data"].instance.setForegroundColor(parseColor('red'))
			self["lock_data"].setText(str('LOCK'))

	def getSignalFromFrontend(self):
		global newdb, newdeltadb
		service = self.session.nav.getCurrentService()
		if service:
			frontendInfo = service.frontendInfo()
			if frontendInfo:
				try:
					frontendData = frontendInfo.getAll(True)
					print(f"[ECustomquicksignallevel] Raw interface data: {frontendData}")
					quality = frontendData.get("tuner_signal_quality", 0)
#					snr_percent = min(100, quality // 655)
					snr_db = (frontendData.get("tuner_signal_quality_db", 0) / 100.0) + newdeltadb
					snr_percent = (round(snr_db / newdb * 100))
					ber = frontendData.get("tuner_bit_error_rate", 0)
					agc = min(100, frontendData.get("tuner_signal_power", 0) // 655)
					lock = frontendData.get("tuner_locked", 0)
					return snr_db, snr_percent, ber, agc, lock
				except Exception as e:
					print(f"[ECustomquicksignallevel] Error getting signal from frontend: {e}")
		return 0.0, 0, 0, 0, False

	def getSignalFromFrontend_def(self):
		service = self.session.nav.getCurrentService()
		if service:
			frontendInfo = service.frontendInfo()
			if frontendInfo:
				try:
					frontendData = frontendInfo.getAll(True)
					print(f"[ECustomquicksignallevel] Raw interface data: {frontendData}")
					quality = frontendData.get("tuner_signal_quality", 0)
					snr_percent = min(100, quality // 655)
					snr_db = frontendData.get("tuner_signal_quality_db", 0) / 100.0
					ber = frontendData.get("tuner_bit_error_rate", 0)
					agc = min(100, frontendData.get("tuner_signal_power", 0) // 655)
					lock = frontendData.get("tuner_locked", 0)
					return snr_db, snr_percent, ber, agc, lock
				except Exception as e:
					print(f"[ECustomquicksignallevel] Error getting signal from frontend: {e}")
		return 0.0, 0, 0, 0, False

	def getFec(self, fec):
		return {0:"Auto",1:"1/2",2:"2/3",3:"3/4",4:"5/6",5:"7/8",6:"8/9",7:"3/5",8:"4/5",9:"9/10"}.get(fec, "N/A")

	def getModulation(self, mod):
		return {0:"Auto",1:"QPSK",2:"8PSK",3:"64QAM",4:"16APSK",5:"32APSK"}.get(mod, "N/A")

	def getSystem(self, tuner_type, sys):
		if tuner_type == "DVB-S":
			return {0: "DVB-S", 1: "DVB-S2"}.get(sys, "N/A")
		elif tuner_type == "DVB-T":
			return {0: "DVB-T", 1: "DVB-T2"}.get(sys, "N/A")
		elif tuner_type == "DVB-C":
			return {0: "DVB-C", 1: "DVB-C2"}.get(sys, "N/A")
		else:
			return "N/A"

	def getPolarization(self, pol):
		return {0:"H",1:"V",2:"L",3:"R"}.get(pol, "N/A")

    # New methods for DVB-T specific parameters
	def getBandwidth(self, bw):
		return {6000000: "6 MHz", 7000000: "7 MHz", 8000000: "8 MHz"}.get(bw, f"{bw/1000000} MHz")

	def getConstellation(self, constellation):
		return {0: "QPSK", 1: "16QAM", 2: "64QAM", 3: "256QAM"}.get(constellation, "N/A")

	def getTransmissionMode(self, mode):
		return {0: "Auto", 1: "2K", 2: "8K", 3: "4K"}.get(mode, "N/A")

	def getGuardInterval(self, gi):
		return {0: "Auto", 1: "1/32", 2: "1/16", 3: "1/8", 4: "1/4"}.get(gi, "N/A")

	def getHierarchy(self, hi):
		return {0: "None", 1: "1", 2: "2", 3: "4", 4: "Auto"}.get(hi, "N/A")

	def getSatelliteNameFromXML(self, orbital_position):
		satellites_file = "/etc/tuxbox/satellites.xml"
		if not os.path.exists(satellites_file):
			return self.formatOrbitalPos(orbital_position)

		try:
			tree = ET.parse(satellites_file)
			root = tree.getroot()
			sat_pos = self.convertOrbitalPos(orbital_position)
			for sat in root.findall("sat"):
				pos = int(sat.get("position", "0"))
				if pos == sat_pos:
					return sat.get("name", self.formatOrbitalPos(orbital_position))
			return self.formatOrbitalPos(orbital_position)
		except:
			return self.formatOrbitalPos(orbital_position)

	def convertOrbitalPos(self, pos):
		if pos > 1800:
			return pos - 3600
		else:
			return pos

	def formatOrbitalPos(self, pos):
		pos = self.convertOrbitalPos(pos)
		if pos < 0:
			return f"{abs(pos) / 10.0:.1f}W"
		else:
			return f"{pos / 10.0:.1f}E"

	def getBasicInfo(self):
		service = self.session.nav.getCurrentService()
		if not service:
			return "No active service"
		info = service.info()
		if not info:
			return "I can't get information about the object."

		try:
			name = info.getName() or "N/A"
		except:
			name = "N/A"
		try:
			provider = info.getInfoString(iServiceInformation.sProvider) or "N/A"
		except:
			provider = "N/A"

		frontendInfo = service.frontendInfo()
		frontendData = frontendInfo and frontendInfo.getAll(True)
		if not frontendData:
			return "Can't get interface data."

		try:
			freq = frontendData.get("frequency", 0) // 1000
		except:
			freq = 0
		try:
			sr = frontendData.get("symbol_rate", 0) // 1000
		except:
			sr = 0
		try:
			fec_inner = frontendData.get("fec_inner", 0)
			fec_str = self.getFec(fec_inner)
		except:
			fec_str = "N/A"
		try:
			pol = frontendData.get("polarization", 0)
			pol_str = self.getPolarization(pol)
		except:
			pol_str = "N/A"
		try:
			orbital_pos = frontendData.get("orbital_position", 0)
			sat_name = self.getSatelliteNameFromXML(orbital_pos)
		except:
			sat_name = "Unknown satellite"

		try:
			mod = frontendData.get("modulation", 0)
			mod_str = self.getModulation(mod)
		except:
			mod_str = "N/A"
		try:
			tuner_type = frontendData.get("tuner_type", "")
			system_val = frontendData.get("system", 0)
			system_str = self.getSystem(tuner_type, system_val)
		except:
			system_str = "N/A"
		try:
			pls_mode = frontendData.get("pls_mode", -1)
			pls_mode_str = {0:"Root",1:"Gold",2:"Combo"}.get(pls_mode, str(pls_mode))
		except:
			pls_mode_str = "N/A"
		try:
			pls_code = frontendData.get("pls_code", -1)
			pls_code_str = str(pls_code) if pls_code >= 0 else "N/A"
		except:
			pls_code_str = "N/A"
		try:
			t2mi_plp_id = frontendData.get("t2mi_plp_id", -1)
			t2mi_plp_str = str(t2mi_plp_id) if t2mi_plp_id >= 0 else "N/A"
		except:
			t2mi_plp_str = "N/A"
		try:
			t2mi_pid = frontendData.get("t2mi_pid", -1)
			t2mi_pid_str = f"0x{t2mi_pid:X}" if t2mi_pid >= 0 else "N/A"
		except:
			t2mi_pid_str = "N/A"

		try:
			vpid = info.getInfo(iServiceInformation.sVideoPID)
			vpid_str = f"0x{vpid:X}" if vpid != -1 else "No"
		except:
			vpid_str = "No"
		try:
			apid = info.getInfo(iServiceInformation.sAudioPID)
			apid_str = f"0x{apid:X}" if apid != -1 else "No"
		except:
			apid_str = "No"
		try:
			pcrpid = info.getInfo(iServiceInformation.sPCRPID)
			pcr_str = f"0x{pcrpid:X}" if pcrpid != -1 else "No"
		except:
			pcr_str = "No"
		try:
			pmtpid = info.getInfo(iServiceInformation.sPMTPID)
			pmt_str = f"0x{pmtpid:X}" if pmtpid != -1 else "No"
		except:
			pmt_str = "No"
		try:
			txt_pid = info.getInfo(iServiceInformation.sTXTPID)
			txt_str = f"0x{txt_pid:X}" if txt_pid != -1 else "No"
		except:
			txt_str = "No"

        # DVB-T specific parameters
		dvbt_params = ""
		if tuner_type in ["DVB-T", "DVB-T2"]:
			try:
				bandwidth = frontendData.get("bandwidth", 0)
				bandwidth_str = self.getBandwidth(bandwidth)
			except:
				bandwidth_str = "N/A"
			try:
				code_rate_hp = frontendData.get("code_rate_hp", 0)
				code_rate_hp_str = self.getFec(code_rate_hp)
			except:
				code_rate_hp_str = "N/A"
			try:
				code_rate_lp = frontendData.get("code_rate_lp", 0)
				code_rate_lp_str = self.getFec(code_rate_lp)
			except:
				code_rate_lp_str = "N/A"
			try:
				constellation = frontendData.get("constellation", 0)
				constellation_str = self.getConstellation(constellation)
			except:
				constellation_str = "N/A"
			try:
				transmission_mode = frontendData.get("transmission_mode", 0)
				transmission_mode_str = self.getTransmissionMode(transmission_mode)
			except:
				transmission_mode_str = "N/A"
			try:
				guard_interval = frontendData.get("guard_interval", 0)
				guard_interval_str = self.getGuardInterval(guard_interval)
			except:
				guard_interval_str = "N/A"
			try:
				hierarchy = frontendData.get("hierarchy_information", 0)
				hierarchy_str = self.getHierarchy(hierarchy)
			except:
				hierarchy_str = "N/A"

			dvbt_params = f"""
   Bandwidth: {bandwidth_str}
   Code Rate HP: {code_rate_hp_str}
   Code Rate LP: {code_rate_lp_str}
   Constellation: {constellation_str}
   Transmission Mode: {transmission_mode_str}
   Guard Interval: {guard_interval_str}
   Hierarchy: {hierarchy_str}
            """

		text = f"""
   Channel: {name}
   Provider: {provider}
   Satellite: {sat_name}
   Frequency: {freq} MHz
   Polarization: {pol_str}
   Symbol Rate: {sr}k
   FEC: {fec_str}
   Modulation: {mod_str}
   SYSTEM: {system_str}
   PLS MODE: {pls_mode_str}
   PLS CODE: {pls_code_str}
   T2MI PLP ID: {t2mi_plp_str}
   T2MI PID: {t2mi_pid_str}
{dvbt_params}
   VIDEO PID: {vpid_str}
   AUDIO PID: {apid_str}
   PCR PID: {pcr_str}
   PMT PID: {pmt_str}
   TELETEXT PID: {txt_str}
        """.strip()
		mytrdata = str(freq) + ' MHz ' + str(pol_str) + ' ' + str(sr) + ' ' + str(fec_str) + ' ' + str(mod_str) + ' ' + str(system_str)
		return name, provider, sat_name, mytrdata

	def action(self):
		global view_type
		self.counter = self.counter + 1
		if self.counter % 2 == 0:
			view_type = 'accepted'
			sz_w = getDesktop(0).size().width()
			if sz_w == 1920:
				self["circle"].instance.show()
			else:
				self["circle"].instance.show()
		else:
			view_type = 'default'
			sz_w = getDesktop(0).size().width()
			if sz_w == 1920:
				self["circle"].instance.hide()
			else:
				self["circle"].instance.hide()

	def greenbutton(self):
		global newdb, newdeltadb, my_dict_newdb, my_dict_newdeltadb
		c2, p2, n2, t2 = self.getBasicInfo()
		path1 = "/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/my_data1.json"
		path2 = "/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/my_data2.json"
		mykey = str(t2) + '*' + str(n2)
		my_dict_newdb[mykey] = float("%.1f" % (newdb))
		my_dict_newdeltadb[mykey] = newdeltadb
		with open(path1, "w", encoding="utf-8") as f:
			json.dump(my_dict_newdb, f, ensure_ascii=False)
		with open(path2, "w", encoding="utf-8") as f:
			json.dump(my_dict_newdeltadb, f, ensure_ascii=False)

	def about(self):
		if config.plugins.ecqslevel.extinfo.value == 'yes':
			self.session.open(ECQSLBox)
		else:
			self.session.open(ECQSLInfo)

	def cancel(self):
		self.greenbutton()
		self.close()

class ECQSLBox(Screen):
	sz_w = getDesktop(0).size().width()
	if sz_w == 1920:
		skin = ECQSLBox_FHD
	else:
		skin = ECQSLBox_HD

	def __init__(self, session, args = 0):
		self.session = session
		Screen.__init__(self, session)

		self["info_00"] = Label(" ")
		self["info_01"] = Label(" ")
		self["info_02"] = Label(" ")
		self["info_03"] = Label(" ")
		self["info_04"] = Label(" ")
		self["info_05"] = Label(" ")
		self["info_06"] = Label(" ")
		self["info_07"] = Label(" ")
		self["info_08"] = Label(" ")
		self["info_09"] = Label(" ")
		self["info_10"] = Label(" ")
		self["cpu_info"] = Label(" ")
		self["cpu_pic"] = Pixmap()

		self["ver"] = StaticText(_("E Custom Quick Signal level. ver. ") + str(version))
		self["copyright"] = StaticText("(C) Evg77734, 2026, https://gisclub.tv")

		self["actions"] = ActionMap(["OkCancelActions", "DirectionActions", "HelpActions", "EPGSelectActions"],
		{
			"cancel": self.Exit,
		}, -1)

		self.ch755()

		Thread4 = Thread(target=self.mys)
		Thread4.start()

		Thread5 = Thread(target=self.myrd)
		Thread5.start()

		self.onShow.append(self.Setfirstdatas)

	def ch755(self):
		if os.path.exists(path1):
			script = path1
			os.chmod(script, 755)

	def mysub(self):
		process = subprocess.Popen(['bash', '-c', path1],
								   stdout=subprocess.PIPE,
								   stderr=subprocess.PIPE)
		stdout, stderr = process.communicate()
		print("STDOUT:", stdout.decode())
		print("STDERR:", stderr.decode())

	def myreaddata(self):
		color = gRGB(255, 255, 255)
		if os.path.exists(path2):
			with open(path2, 'r') as f:
				for line in f:
					if 'CPU: ' in line:
						rez = line.strip('\n').split('CPU: ')[1].split(' %')[0]
						if float(rez) <= 40.0:
							color = gRGB(0, 128, 0)
						elif float(rez) > 40.0 and float(rez) < 60.0:
							color = gRGB(255, 255, 0)
						elif float(rez) >= 60.0:
							color = gRGB(255, 0, 0)
						else:
							color = gRGB(255, 255, 255)
						self["cpu_info"].instance.setForegroundColor(color)
						self["cpu_info"].setText(line.strip('\n'))

	def mys(self):
		self.mysub()

	def myrd(self):
		while 1:
			sleep(1)
			self.myreaddata()

	def Setfirstdatas(self):
		global MyBoxType, MyBoxTuner
		self["info_00"].setText(str(MyBoxType))
		self["info_01"].setText(str(MyBoxTuner))
		self["info_02"].setText(str(getMyBoxSoftware()))
		self["info_03"].setText(str(getMyBoxLinuxVersion()))
		self["info_04"].setText(str(getMyBoxPythonVersion()))
		self["info_05"].setText(str(getMyBoxCpuInfo().split('CPU: ')[1]))
		self["info_06"].setText(str(getMyBoxCpuSpeed()))
		sz_w = getDesktop(0).size().width()
		sz_h = getDesktop(0).size().height()
		self["info_09"].setText(str(getMyBoxSkin()) + ' (' + str(sz_w) + 'x' + str(sz_h) + ')')
		sz_w = getDesktop(0).size().width()
		if sz_w == 1920:
			self["cpu_pic"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/images/cpu_hi.png")
		else:
			self["cpu_pic"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/images/cpu_hi_1.png")

		Thread3 = Thread(target=self.sh_dadas)
		Thread3.start()

	def sh_dadas(self):
		self.moveTimer3 = eTimer()
		self.moveTimer3.callback.append(self.sh_exe)
		self.moveTimer3.start(100, 1)

	def sh_exe(self):
		global MyBoxType
		color = gRGB(255, 255, 255)
		self.moveTimer3.start(5000, 1)

		try:
			rezcpuload = getMyBoxCpuLoad().split('CPU Load: ')[1]
			rezcpuload = rezcpuload.split(' ')[0]

			if str(MyBoxType) == 'AX 4K-BOX HD61':
				if float(rezcpuload) <= 13.3:
					color = gRGB(0, 128, 0)
				elif float(rezcpuload) > 13.3 and float(rezcpuload) < 13.55:
					color = gRGB(255, 255, 0)
				elif float(rezcpuload) >= 13.55:
					color = gRGB(255, 0, 0)
				else:
					color = gRGB(255, 255, 255)
			if str(MyBoxType) == 'GI ET11000 4K':
				if float(rezcpuload) <= 0.5:
					color = gRGB(0, 128, 0)
				elif float(rezcpuload) > 0.5 and float(rezcpuload) < 0.95:
					color = gRGB(255, 255, 0)
				elif float(rezcpuload) >= 13.55:
					color = gRGB(255, 0, 0)
				else:
					color = gRGB(255, 255, 255)
		except:
			color = gRGB(255, 255, 255)

		self["info_07"].instance.setForegroundColor(color)
		self["info_07"].setText(str(getMyBoxCpuLoad()))

		color = gRGB(244, 164, 96)
		self["info_10"].instance.setForegroundColor(color)
		self["info_10"].setText(str(getMyBoxTimeWorking()))

		try:
			reztemp = getMyBoxCpuTemp().split('CPU: ')[1]
			reztemp = reztemp.split(' ')[0]

			if float(reztemp) < 50.0:
				color = gRGB(0, 128, 0)
			elif float(reztemp) >= 50.0 and float(reztemp) < 75.0:
				color = gRGB(255, 255, 0)
			elif float(reztemp) >= 75.0:
				color = gRGB(255, 0, 0)
			else:
				color = gRGB(255, 255, 255)
		except:
			color = gRGB(255, 255, 255)

		self["info_08"].instance.setForegroundColor(color)
		self["info_08"].setText(str(getMyBoxCpuTemp()))

	def Exit(self):
		try:
			os.system('killall cpu.sh')
		except:
			pass
		self.close()

class ConfigECQSL(ConfigListScreen, Screen):
	sz_w = getDesktop(0).size().width()
	if sz_w == 1920:
		skin = ConfigECustomsignallevel_FHD
	else:
		skin = ConfigECustomsignallevel_HD

	def __init__(self, session):
		self.session = session
		Screen.__init__(self, session)

		self["mytitle"] = StaticText(_("Configuration of the E Custom quick signal level plugin"))

		list = []
		list.append(getConfigListEntry(_("Show minimum dB level values:"), config.plugins.ecqslevel.mindb))
		list.append(getConfigListEntry(_("Show extended information about the receiver:"), config.plugins.ecqslevel.extinfo))
		ConfigListScreen.__init__(self, list)

		self["setupActions"] = ActionMap(["DirectionActions", "SetupActions", "ColorActions"],
		{ "red": self.cancel,
		"cancel": self.cancel,
		"green": self.save,
		"ok": self.save
		}, -2)
		self["key_red"] = StaticText(_("Close"))
		self["key_green"] = StaticText(_("Save"))

	def cancel(self):
		for x in self["config"].list:
			x[1].cancel()
		self.close(False)

	def save(self):
		for x in self["config"].list:
			x[1].save()
		configfile.save()
		self.mbox = self.session.open(MessageBox,(_("Configuration is saved")), MessageBox.TYPE_INFO, timeout = 3 )
		self.close()

class ECQSLInfo(Screen):
	sz_w = getDesktop(0).size().width()
	if sz_w == 1920:
		skin = ECQSLInfo_FHD
	else:
		skin = ECQSLInfo_HD

	def __init__(self, session, args = 0):
		self.session = session
		Screen.__init__(self, session)

		self["ver"] = StaticText(_("E Custom Quick Signal level. ver. ") + str(version))

		self["actions"] = ActionMap(["OkCancelActions", "DirectionActions", "HelpActions", "EPGSelectActions"],
		{
			"cancel": self.Exit,
		}, -1)

	def Exit(self):
		self.close()

class ECustomquicksignallevelError(Screen):
	sz_w = getDesktop(0).size().width()
	if sz_w == 1920:
		skin = ECQSLError_FHD
	else:
		skin = ECQSLError_HD

	def __init__(self, session, args = 0):
		self.session = session
		Screen.__init__(self, session)

		self["ver"] = StaticText(_("E Custom Quick Signal level. ver. ") + str(version))
		self["err1"] = StaticText(_("Error."))
		self["err2"] = StaticText(_("No services found from DVB-S, DVB-T, or DVB-C tuners."))

		self["actions"] = ActionMap(["OkCancelActions", "DirectionActions", "HelpActions", "EPGSelectActions"],
		{
			"cancel": self.Exit,
		}, -1)

	def Exit(self):
		self.close()

def onstart0(session):
	global MyBoxType, MyBoxTuner
	service = session.nav.getCurrentService()
	info = service and service.info()
	tunertype = " "
	if info is not None:
		feinfo = (service and service.frontendInfo())
		if (feinfo is not None):
			frontendData = (feinfo and feinfo.getAll(True))
			if (frontendData is not None):
				if (frontendData.get("tuner_type") == "DVB-S"):
					tunertype = frontendData.get("tuner_type")
				if (frontendData.get("tuner_type") == "DVB-T"):
					tunertype = frontendData.get("tuner_type")
				if (frontendData.get("tuner_type") == "DVB-C"):
					tunertype = frontendData.get("tuner_type")
	if tunertype == "DVB-S":
		MyBoxType = getMyBoxType()
		MyBoxTuner = getMyBoxTuner(tunertype)
		session.open(ECustomquicksignallevel)
	elif tunertype == "DVB-T":
		MyBoxType = getMyBoxType()
		MyBoxTuner = getMyBoxTuner(tunertype)
		session.open(ECustomquicksignallevel)
	elif tunertype == "DVB-C":
		MyBoxType = getMyBoxType()
		MyBoxTuner = getMyBoxTuner(tunertype)
		session.open(ECustomquicksignallevel)
	else:
		if config.plugins.ecqslevel.extinfo.value == 'yes':
			MyBoxTuner = _('DVB-S, DVB-T, or DVB-C tuners are not used.')
			session.open(ECQSLBox)
		else:
			session.open(ECustomquicksignallevelError)

def main(session, **kwargs):
	onstart0(session)

def Plugins(path, **kwargs):
	return PluginDescriptor(name = _("E Custom quick signal level. ver. ") + str(version), where = [PluginDescriptor.WHERE_PLUGINMENU], description = _("Signal level with display settings"), icon = 'ecqsignal.png', fnc = main)
