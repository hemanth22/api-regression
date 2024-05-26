#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import requests
import datetime
import uuid
import xml.etree.ElementTree as ET

## Generate ISO timestamp

iso_timestamp = datetime.datetime.utcnow().isoformat()

## Generate random UUID

random_uuid = str(uuid.uuid4())

endpoint_calculator = "http://www.dneonline.com/calculator.asmx"

def getdata_dneonline(newurl, newfname, outputfilename):
    try:
        #url = "http://www.dneonline.com/calculator.asmx"
        #f = open("addHelper.xml", "rt")
        f = open(newfname, "rt")
        payload = f.read()  
        f.close()
        headers = {
            'Content-Type': 'text/xml'
        }
        response = requests.request("POST", newurl, headers=headers, data=payload, verify=False)
        tree = ET.fromstring(response.text)
        with open(outputfilename, 'w') as OutWritefile:
            OutWritefile.write(response.text)
        for xmlresponse in tree.findall('.//{*}AddResult'):
            return xmlresponse.text
        for xmlresponse in tree.findall('.//{*}SubtractResult'):
            return xmlresponse.text
        for xmlresponse in tree.findall('.//{*}MultiplyResult'):
            return xmlresponse.text
        for xmlresponse in tree.findall('.//{*}DivideResult'):
            return xmlresponse.text
#        return response.text
    except Exception as e:
        print("Err: ", e)

print("TC01",'|',"Basic Test Case",'|',getdata_dneonline(endpoint_calculator, "Add_TC01.xml", "Response_Add_TC01.xml"),'|',getdata_dneonline(endpoint_calculator, "Sub_TC01.xml", "Response_Sub_TC01.xml"),'|',getdata_dneonline(endpoint_calculator, "Mul_TC01.xml","Response_Mul_TC01.xml"),'|',getdata_dneonline(endpoint_calculator, "Div_TC01.xml","Response_Div_TC01.xml"))
print("TC02",'|',"Basic Test Case",'|',getdata_dneonline(endpoint_calculator, "Add_TC02.xml", "Response_Add_TC02.xml"),'|',"N/A",'|',getdata_dneonline(endpoint_calculator, "Mul_TC02.xml","Response_Mul_TC02.xml"),'|',"N/A")
print("TC03",'|',"Basic Test Case",'|',"N/A",'|',"N/A",'|',"N/A",'|',getdata_dneonline(endpoint_calculator, "Div_TC03.xml","Response_Div_TC03.xml"))
print("TC04",'|',"Basic Test Case",'|',getdata_dneonline(endpoint_calculator, "Add_TC04.xml", "Response_Add_TC04.xml"),'|',"N/A",'|',"N/A",'|',getdata_dneonline(endpoint_calculator, "Div_TC04.xml","Response_Div_TC04.xml"))
print("TC05",'|',"Basic Test Case",'|',getdata_dneonline(endpoint_calculator, "Add_TC05.xml", "Response_Add_TC05.xml"),'|',getdata_dneonline(endpoint_calculator, "Sub_TC05.xml", "Response_Sub_TC05.xml"),'|',getdata_dneonline(endpoint_calculator, "Mul_TC05.xml","Response_Mul_TC05.xml"),'|',getdata_dneonline(endpoint_calculator, "Div_TC05.xml","Response_Div_TC05.xml"))
