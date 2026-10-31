# Created (C) Evg77734, 2025-2026

ECustomsignallevel_FHD = """
<screen name="ECustomsignallevel_FHD" position="0,0" size="1920,1080" backgroundColor="transparent" flags="wfNoBorder">
  <eLabel zPosition="1" size="1900,230" position="center,835" backgroundColor="#000050ef" cornerRadius="50"/>
  <eLabel size="1880,210" zPosition="2" position="center,845" backgroundColor="#50000000" cornerRadius="50"/>
  <eLabel size="1900,470" zPosition="1" position="10,10" backgroundColor="#000050ef" cornerRadius="50"/>
  <eLabel size="1880,450" zPosition="2" position="20,20" backgroundColor="#50000000" cornerRadius="50"/>
  <eLabel size="270,270" zPosition="1" position="center,523" backgroundColor="#000050ef" cornerRadius="150"/>
  <eLabel size="450,150" zPosition="1" position="182,583" backgroundColor="#000050ef" cornerRadius="50"/>
  <eLabel size="450,150" zPosition="1" position="1277,583" backgroundColor="#000050ef" cornerRadius="50"/>
  <eLabel size="250,250" zPosition="2" position="center,533" backgroundColor="#50000000" cornerRadius="150"/>
  <eLabel size="430,130" zPosition="2" position="192,593" backgroundColor="#50000000" cornerRadius="50"/>
  <eLabel size="430,130" zPosition="2" position="1287,593" backgroundColor="#50000000" cornerRadius="50"/>
  <widget name="snr_label" position="35,70" size="150,75" font="Regular;52" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1"/>
  <widget name="agc_data" position="1715,170" size="150,75" font="Regular;52" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="right"/>
  <widget name="snrdb_data" position="150,300" size="400,118" font="Regular;108" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" text=" N/A"/>
  <widget name="agc1_data" position="685,300" size="350,118" font="Regular;108" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" text=" N/A"/>
  <widget name="ber_data" position="1180,300" size="250,118" font="Regular;108" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" text=" N/A"/>
  <widget name="lock_data" position="1450,300" size="430,118" font="Console;72" valign="bottom" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" text=" N/A"/>
  <widget name="snr_data" position="1715,70" size="150,75" font="Regular;52" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="right"/>
  <widget name="snr_bar" position="center,70" size="1850,75" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/images/icon_snr.png" borderWidth="1" borderColor="#000050ef" zPosition="3" backgroundColor="#50000000" cornerRadius="15"/>
  <widget name="agc_label" position="35,170" size="150,75" font="Regular;52" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1"/>
  <widget name="sat_chname" position="35,860" size="905,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="sat_trdatas" position="35,925" size="905,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="my_box" position="35,990" size="905,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="db_default1" position="205,605" size="400,48" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="db_custom1" position="1303,605" size="400,48" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="right_arrow" position="1038,634" size="45,48" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="down_arrow" position="center,734" size="48,48" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="up_arrow" position="center,534" size="48,48" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="left_arrow" position="838,634" size="45,48" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="db_default2" position="205,665" size="400,48" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="db_custom2" position="1303,665" size="400,48" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="sat_prov" position="975,860" size="905,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="sat_name" position="975,925" size="905,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="my_tuner" position="975,990" size="905,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="agc_bar" position="center,170" size="1850,75" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/images/icon_agc.png" borderWidth="1" borderColor="#000050ef" zPosition="3" backgroundColor="#50000000" cornerRadius="15"/>
  <eLabel text="SNR:" position="35,334" size="100,50" transparent="1" zPosition="5" font="Regular;35" valign="center"/>
  <eLabel text="AGC:" position="575,334" size="100,50" transparent="1" zPosition="5" font="Regular;35" valign="center"/>
  <eLabel text="BER:" position="1060,334" size="100,50" transparent="1" zPosition="5" font="Regular;35" valign="center"/>
  <widget name="remote" position="center,583" size="150,150" zPosition="3" alphatest="on" transparent="1" backgroundColor="#50000000"/>
  <widget name="circle" position="center,508" size="300,300" zPosition="0" alphatest="on" transparent="1" backgroundColor="#50000000"/>
  <widget name="min_db" position="2100,70" zPosition="4" size="20,75" transparent="1" alphatest="on"/>
  <widget name="test_label" position="590,70" size="200,75" font="Regular;28" valign="center" foregroundColor="#00000000" zPosition="4" transparent="1"/>
</screen>"""

ECQSLBox_FHD = """
<screen name="ECQSLBox_FHD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="950,980">
  <widget position="center,887" size="850,56" zPosition="3" font="Regular;36" source="copyright" render="Label" transparent="1" valign="center" halign="center" foregroundColor="#00e4b500"/>
  <widget position="center,35" size="850,56" zPosition="3" font="Regular;36" source="ver" render="Label" transparent="1" valign="center" halign="center" foregroundColor="#00e4b500"/>
  <eLabel size="920,950" zPosition="2" position="15,15" backgroundColor="#50000000" cornerRadius="80"/>
  <eLabel size="950,980" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="80"/>
  <widget name="info_00" position="center,107" size="850,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="info_02" position="center,249" size="850,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="info_03" position="center,320" size="850,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="info_04" position="center,391" size="850,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="info_06" position="center,533" size="850,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="info_07" position="center,604" size="850,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="cpu_info" position="475,675" size="425,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="info_08" position="50,675" size="425,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="info_09" position="center,746" size="850,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="info_10" position="center,817" size="850,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="info_05" position="center,462" size="850,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="info_01" position="center,178" size="850,56" font="Regular;36" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center"/>
  <widget name="cpu_pic" position="center,675" size="56,56" zPosition="4" alphatest="on" transparent="1" backgroundColor="#50000000" scale="1"/>
</screen>"""

ConfigECustomsignallevel_FHD = """
<screen name="ConfigECustomsignallevel_FHD" position="center,center" size="1125,540" title=" " flags="wfNoBorder" backgroundColor="transparent">
  <eLabel size="1105,520" zPosition="-2" position="10,10" backgroundColor="#000050ef" cornerRadius="40"/>
  <eLabel size="1095,510" zPosition="-1" position="15,15" backgroundColor="#50000000" cornerRadius="40"/>
  <eLabel position="55,433" size="1020,5" backgroundColor="#000050ef" zPosition="3"/>
  <widget name="config" position="55,105" size="1020,300" scrollbarMode="showOnDemand" itemHeight="35" transparent="1" font="Regular;30" zPosition="2"/>
  <widget source="key_red" render="Label" position="140,455" size="248,45" font="Regular;33" valign="center" foregroundColor="#00f4f4f4" backgroundColor="background" transparent="1" zPosition="2"/>
  <widget source="mytitle" render="Label" position="55,35" size="1020,45" font="Regular;33" valign="center" foregroundColor="#00f4f4f4" backgroundColor="background" transparent="1" zPosition="2"/>
  <widget source="key_green" render="Label" position="485,455" size="248,45" font="Regular;33" valign="center" foregroundColor="#00f4f4f4" backgroundColor="background" transparent="1" zPosition="2"/>
  <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/images/key_red.png" position="65,463" size="60,30" alphatest="on" zPosition="2" scale="1"/>
  <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/images/key_green.png" position="410,463" size="60,30" alphatest="on" zPosition="2" scale="1"/>
</screen>"""

ECQSLInfo_FHD = """
<screen name="ECQSLInfo_FHD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="960,400">
  <widget position="center,100" size="750,42" zPosition="3" font="Regular;32" source="ver" render="Label" transparent="1" valign="center" halign="center"/>
  <eLabel position="center,180" size="400,42" zPosition="3" font="Regular;32" text="(C) Evg77734, 2026" transparent="1" halign="center" valign="center"/>
  <eLabel name="" position="center,260" size="400,42" zPosition="3" font="Regular;32" text="https://gisclub.tv" transparent="1" halign="center" valign="center"/>
  <eLabel size="930,370" zPosition="2" position="15,15" backgroundColor="#50000000" cornerRadius="80"/>
  <eLabel size="960,400" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="80"/>
</screen>"""

ECQSLError_FHD = """
<screen name="ECQSLError_FHD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="960,400">
  <widget position="center,85" size="750,42" zPosition="3" font="Regular;32" source="ver" render="Label" transparent="1" valign="center" halign="center"/>
  <widget position="center,170" size="750,42" zPosition="3" font="Regular;32" source="err1" render="Label" transparent="1" valign="center" halign="center"/>
  <widget position="center,250" size="900,42" zPosition="3" font="Regular;32" source="err2" render="Label" transparent="1" valign="center" halign="center"/>
  <eLabel size="930,370" zPosition="2" position="15,15" backgroundColor="#50000000" cornerRadius="80"/>
  <eLabel size="960,400" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="80"/>
</screen>"""

#-----------------------------------------------------------------------

ECustomsignallevel_HD = """
<screen name="ECustomsignallevel_HD" position="0,0" size="1280,720" backgroundColor="transparent" flags="wfNoBorder" >
  <eLabel zPosition="1" size="1267,153" position="center,557" backgroundColor="#000050ef" cornerRadius="50" />
  <eLabel size="1253,140" zPosition="2" position="center,563" backgroundColor="#50000000" cornerRadius="50" />
  <eLabel size="1267,313" zPosition="1" position="7,7" backgroundColor="#000050ef" cornerRadius="50" />
  <eLabel size="1253,300" zPosition="2" position="13,13" backgroundColor="#50000000" cornerRadius="50" />
  <eLabel size="180,180" zPosition="1" position="center,349" backgroundColor="#000050ef" cornerRadius="150" />
  <eLabel size="300,100" zPosition="1" position="121,389" backgroundColor="#000050ef" cornerRadius="50" />
  <eLabel size="300,100" zPosition="1" position="851,389" backgroundColor="#000050ef" cornerRadius="50" />
  <eLabel size="167,167" zPosition="2" position="center,355" backgroundColor="#50000000" cornerRadius="150" />
  <eLabel size="287,87" zPosition="2" position="128,395" backgroundColor="#50000000" cornerRadius="50" />
  <eLabel size="287,87" zPosition="2" position="858,395" backgroundColor="#50000000" cornerRadius="50" />
  <widget name="snr_label" position="23,47" size="100,50" font="Regular;35" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" />
  <widget name="agc_data" position="1143,113" size="100,50" font="Regular;35" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="right" />
  <widget name="snrdb_data" position="100,200" size="267,79" font="Regular;72" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" text=" N/A" />
  <widget name="agc1_data" position="457,200" size="233,79" font="Regular;72" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" text=" N/A" />
  <widget name="ber_data" position="787,200" size="167,79" font="Regular;72" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" text=" N/A" />
  <widget name="lock_data" position="967,200" size="287,79" font="Console;48" valign="bottom" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" text=" N/A" />
  <widget name="snr_data" position="1143,47" size="100,50" font="Regular;35" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="right" />
  <widget name="snr_bar" position="center,47" size="1233,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/images/icon_snr.png" borderWidth="1" borderColor="#000050ef" zPosition="3" backgroundColor="#50000000" cornerRadius="15" />
  <widget name="agc_label" position="23,113" size="100,50" font="Regular;35" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" />
  <widget name="sat_chname" position="23,573" size="603,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="sat_trdatas" position="23,617" size="603,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="my_box" position="23,660" size="603,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="db_default1" position="137,403" size="267,32" font="Regular;16" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="db_custom1" position="869,403" size="267,32" font="Regular;16" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="right_arrow" position="692,423" size="30,32" font="Regular;16" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="down_arrow" position="center,489" size="32,32" font="Regular;16" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="up_arrow" position="center,356" size="32,32" font="Regular;16" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="left_arrow" position="559,423" size="30,32" font="Regular;16" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="db_default2" position="137,443" size="267,32" font="Regular;16" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="db_custom2" position="869,443" size="267,32" font="Regular;16" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="sat_prov" position="650,573" size="603,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="sat_name" position="650,617" size="603,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="my_tuner" position="650,660" size="603,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="agc_bar" position="center,113" size="1233,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/images/icon_agc.png" borderWidth="1" borderColor="#000050ef" zPosition="3" backgroundColor="#50000000" cornerRadius="15" />
  <eLabel text="SNR:" position="23,223" size="67,33" transparent="1" zPosition="5" font="Regular;23" valign="center" />
  <eLabel text="AGC:" position="383,223" size="67,33" transparent="1" zPosition="5" font="Regular;23" valign="center" />
  <eLabel text="BER:" position="707,223" size="67,33" transparent="1" zPosition="5" font="Regular;23" valign="center" />
  <widget name="remote" position="center,389" size="100,100" zPosition="3" alphatest="on" transparent="1" backgroundColor="#50000000" />
  <widget name="circle" position="center,339" size="200,200" zPosition="0" alphatest="on" transparent="1" backgroundColor="#50000000" />
  <widget name="min_db" position="1400,47" zPosition="4" size="13,50" transparent="1" alphatest="on"/>
  <widget name="test_label" position="393,47" size="133,50" font="Regular;18" valign="center" foregroundColor="#00000000" zPosition="4" transparent="1"/>
</screen>"""

ECQSLBox_HD = """
<screen name="ECQSLBox_HD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="633,653" >
  <widget position="center,591" size="567,37" zPosition="3" font="Regular;24" source="copyright" render="Label" transparent="1" valign="center" halign="center" foregroundColor="#00e4b500" />
  <widget position="center,23" size="567,37" zPosition="3" font="Regular;24" source="ver" render="Label" transparent="1" valign="center" halign="center" foregroundColor="#00e4b500" />
  <eLabel size="613,633" zPosition="2" position="10,10" backgroundColor="#50000000" cornerRadius="80" />
  <eLabel size="633,653" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="80" />
  <widget name="info_00" position="center,71" size="567,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="info_02" position="center,166" size="567,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="info_03" position="center,213" size="567,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="info_04" position="center,261" size="567,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="info_06" position="center,355" size="567,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="info_07" position="center,403" size="567,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="cpu_info" position="317,450" size="283,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="info_08" position="33,450" size="283,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="info_09" position="center,497" size="567,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="info_10" position="center,545" size="567,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="info_05" position="center,308" size="567,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="info_01" position="center,119" size="567,37" font="Regular;24" valign="center" foregroundColor="#00ffffff" zPosition="4" transparent="1" halign="center" />
  <widget name="cpu_pic" position="center,450" size="37,37" zPosition="4" alphatest="on" transparent="1" backgroundColor="#50000000" scale="1" />
</screen>"""

ConfigECustomsignallevel_HD = """
<screen name="ConfigECustomsignallevel_HD" position="center,center" size="750,360" title=" " flags="wfNoBorder" backgroundColor="transparent" >
  <eLabel size="737,347" zPosition="-2" position="7,7" backgroundColor="#000050ef" cornerRadius="40" />
  <eLabel size="730,340" zPosition="-1" position="10,10" backgroundColor="#50000000" cornerRadius="40" />
  <eLabel position="37,289" size="680,3" backgroundColor="#000050ef" zPosition="3" />
  <widget name="config" position="37,70" size="680,200" scrollbarMode="showOnDemand" itemHeight="30" transparent="1" font="Regular;20" zPosition="2" />
  <widget source="key_red" render="Label" position="93,303" size="165,30" font="Regular;22" valign="center" foregroundColor="#00f4f4f4" backgroundColor="background" transparent="1" zPosition="2" />
  <widget source="mytitle" render="Label" position="37,23" size="680,30" font="Regular;22" valign="center" foregroundColor="#00f4f4f4" backgroundColor="background" transparent="1" zPosition="2" />
  <widget source="key_green" render="Label" position="323,303" size="165,30" font="Regular;22" valign="center" foregroundColor="#00f4f4f4" backgroundColor="background" transparent="1" zPosition="2" />
  <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/images/key_red.png" position="43,309" size="40,20" alphatest="on" zPosition="2" scale="1" />
  <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ECustom_quick_signal_level/images/key_green.png" position="273,309" size="40,20" alphatest="on" zPosition="2" scale="1" />
</screen>"""

ECQSLInfo_HD = """
<screen name="ECQSLInfo_FHD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="640,267" >
  <widget position="center,67" size="500,28" zPosition="3" font="Regular;21" source="ver" render="Label" transparent="1" valign="center" halign="center" />
  <eLabel position="center,120" size="267,28" zPosition="3" font="Regular;21" text="(C) Evg77734,2026" transparent="1" halign="center" valign="center" />
  <eLabel name="" position="center,173" size="267,28" zPosition="3" font="Regular;21" text="https://gisclub.tv" transparent="1" halign="center" valign="center" />
  <eLabel size="620,247" zPosition="2" position="10,10" backgroundColor="#50000000" cornerRadius="53" />
  <eLabel size="640,267" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="53" />
</screen>"""

ECQSLError_HD = """
<screen name="ECQSLError_FHD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="640,267" >
  <widget position="center,57" size="500,28" zPosition="3" font="Regular;21" source="ver" render="Label" transparent="1" valign="center" halign="center" />
  <widget position="center,113" size="500,28" zPosition="3" font="Regular;21" source="err1" render="Label" transparent="1" valign="center" halign="center" />
  <widget position="center,167" size="600,28" zPosition="3" font="Regular;21" source="err2" render="Label" transparent="1" valign="center" halign="center" />
  <eLabel size="620,247" zPosition="2" position="10,10" backgroundColor="#50000000" cornerRadius="53" />
  <eLabel size="640,267" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="53" />
</screen>"""
