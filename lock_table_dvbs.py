#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Minimum db values ​​for DVBS signal capture
# Source vitalik--19
# Evg77734 2026 (c)
#

lock_table = {
    # DVB-S QPSK
    ("DVB-S", "QPSK", "1/2"): 2.7,
    ("DVB-S", "QPSK", "2/3"): 4.4,
    ("DVB-S", "QPSK", "3/4"): 5.5,
    ("DVB-S", "QPSK", "5/6"): 6.5,
    ("DVB-S", "QPSK", "7/8"): 7.2,

    # DVB-S2 QPSK
    ("DVB-S2", "QPSK", "1/4"): -2.4,
    ("DVB-S2", "QPSK", "1/3"): -1.2,
    ("DVB-S2", "QPSK", "2/5"): 0.0,
    ("DVB-S2", "QPSK", "1/2"): 1.0,
    ("DVB-S2", "QPSK", "3/5"): 2.2,
    ("DVB-S2", "QPSK", "2/3"): 3.1,
    ("DVB-S2", "QPSK", "3/4"): 4.0,
    ("DVB-S2", "QPSK", "4/5"): 4.6,
    ("DVB-S2", "QPSK", "5/6"): 5.2,
    ("DVB-S2", "QPSK", "8/9"): 6.2,
    ("DVB-S2", "QPSK", "9/10"): 6.5,

    # DVB-S2 8PSK
    ("DVB-S2", "8PSK", "3/5"): 5.5,
    ("DVB-S2", "8PSK", "2/3"): 6.6,
    ("DVB-S2", "8PSK", "3/4"): 7.9,
    ("DVB-S2", "8PSK", "5/6"): 9.4,
    ("DVB-S2", "8PSK", "8/9"): 10.6,
    ("DVB-S2", "8PSK", "9/10"): 11.0,

    # DVB-S2 16APSK
    ("DVB-S2", "16PSK", "2/3"): 9.0,
    ("DVB-S2", "16PSK", "3/4"): 10.2,
    ("DVB-S2", "16PSK", "4/5"): 11.0,
    ("DVB-S2", "16PSK", "5/6"): 11.6,
    ("DVB-S2", "16PSK", "8/9"): 12.9,
    ("DVB-S2", "16PSK", "9/10"): 13.1,

    # DVB-S2 32APSK
    ("DVB-S2", "32PSK", "3/4"): 12.6,
    ("DVB-S2", "32PSK", "4/5"): 13.6,
    ("DVB-S2", "32PSK", "5/6"): 14.3,
    ("DVB-S2", "32PSK", "8/9"): 15.7,
    ("DVB-S2", "32PSK", "9/10"): 16.1,
}

def minimum_db(standard, modulation, fec):
	minimum = 0.0
	minimum = lock_table.get((standard, modulation, fec), 0.0)
	return 	minimum

def initial_data(indata):
	std = ""
	mod = ""
	fec = ""
	std = indata.split(" ")[6]
	mod = indata.split(" ")[5]
	fec = indata.split(" ")[4]

	return std, mod, fec

#print(minimum_db("DVB-S2", "QPSK", "4/5"))
#print(initial_data("11606 Mhz H 44948 4/5 QPSK DVB-S2"))
#a, b, c = initial_data("11606 Mhz H 44948 4/5 QPSK DVB-S2")
#print(minimum_db(a, b, c))
