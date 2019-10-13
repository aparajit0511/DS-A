class Solution:
    # Time On
    # space O1
    def validIPAddress(self, IP: str) -> str:
        # only num & no leading zeros & in range(256)
        def isIPv4(string):
            return string.isnumeric() and str(int(string)) == string and 0 <= int(string) <=255
        
        # only num + (a,b,c,d,e,f) & length in range(5)
        def isIPv6(string):                      
            try:return string.isalnum() and int(string,16) >= 0 and len(string) <= 4 
            except: return False
        
        
        if IP.count(".") == 3 and all(isIPv4(string) for string in IP.split(".") ):
            return "IPv4"
        if IP.count(":") == 7 and all(isIPv6(string) for string in IP.split(":")):
            return "IPv6"
        return "Neither"


Alternate old solution

class Solution(object):
    def validIPAddress(self, IP):
        def is_hex(s):
            hex_digits = set("0123456789abcdefABCDEF")
            for char in s:
                if not (char in hex_digits):
                    return False
            return True
        ary = IP.split('.')
        if len(ary) == 4:
            for i in xrange(len(ary)):
                if not ary[i].isdigit() or not 0 <= int(ary[i]) < 256 or (ary[i][0] == '0' and len(ary[i]) > 1):
                    return "Neither"
            return "IPv4"
        ary = IP.split(':')
        if len(ary) == 8:
            for i in xrange(len(ary)):
                tmp = ary[i]
                if len(tmp) == 0 or not len(tmp) <= 4 or not is_hex(tmp):    
                    return "Neither"
            return "IPv6"
        return "Neither"