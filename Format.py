COMMAND_SIZE = 8
VERSION_SIZE = 8
MUST_BE_ZERO_16_SIZE = 16
MUST_BE_ZERO_32_SIZE = 32
ADDR_FAMILY_ID_SIZE = 16
IP_SIZE = 32
METRIC_SIZE = 32

'''Format integer values to bits in string. Use "Format" class before concatenating a 32 bit line for "bytes()" representation.'''
class Format:
    
    #Return command as 8 bits
    def formatCommand(self, myCommand):
        command_bit = bin(myCommand)[2:]
        command_bit = self.bitSizeCorrection(command_bit, COMMAND_SIZE)
        
        return command_bit
        
    
    
    #Return version as 8 bits
    def formatVersion(self, myVersion):
        version_bit = bin(myVersion)[2:]
        version_bit = self.bitSizeCorrection(version_bit, VERSION_SIZE)
        
        return version_bit
    
    
    #Return must be zero as 8 bit int list
    def formatMustBeZero16(self, myMustZero):
        must_zero_bit = bin(myMustZero)[2:]
        must_zero_bit = self.bitSizeCorrection(must_zero_bit, MUST_BE_ZERO_16_SIZE)
        
        must_zero_list = []
        
        must_zero_list.append(int(must_zero_bit[:8], 2))
        must_zero_list.append(int(must_zero_bit[8:], 2))
        
        return must_zero_list
    
    
    #Return address family identifier as 8 bit int list
    def formatAddrFamilyID(self, myAddrFamilyID):
        addr_fimily_id_bit = bin(myAddrFamilyID)[2:]
        addr_fimily_id_bit = self.bitSizeCorrection(addr_fimily_id_bit, ADDR_FAMILY_ID_SIZE)
        
        addr_fimily_id_list = []
        
        addr_fimily_id_list.append(int(addr_fimily_id_bit[:8], 2))
        addr_fimily_id_list.append(int(addr_fimily_id_bit[8:], 2))
        
        return addr_fimily_id_list
    
    
    #Return ip address as 8 bit int list
    def formatIP(self, myIp):
        ip_bit = bin(myIp)[2:]
        ip_bit = self.bitSizeCorrection(ip_bit, IP_SIZE)
        
        ip_list = []
        
        ip_list.append(int(ip_bit[:8], 2))
        ip_list.append(int(ip_bit[8:16], 2))
        ip_list.append(int(ip_bit[16:24], 2))
        ip_list.append(int(ip_bit[24:], 2))
        
        return ip_list
    
    
    #Return must be zero as 8 bit int list
    def formatMustBeZero32(self, myMustZero):
        must_zero_bit = bin(myMustZero)[2:]
        must_zero_bit = self.bitSizeCorrection(must_zero_bit, MUST_BE_ZERO_32_SIZE)
        
        must_zero_list = []
        
        must_zero_list.append(int(must_zero_bit[:8], 2))
        must_zero_list.append(int(must_zero_bit[8:16], 2))
        must_zero_list.append(int(must_zero_bit[16:24], 2))
        must_zero_list.append(int(must_zero_bit[24:], 2))
        
        return must_zero_list
    
    
    #Return metric as 8 bit int list
    def formatMetric(self, myMetric):
        metric_bit = bin(myMetric)[2:]
        metric_bit = self.bitSizeCorrection(metric_bit, METRIC_SIZE)
        
        metric_list = []
        
        metric_list.append(int(metric_bit[:8], 2))
        metric_list.append(int(metric_bit[8:16], 2))
        metric_list.append(int(metric_bit[16:24], 2))
        metric_list.append(int(metric_bit[24:], 2))
        
        return metric_list
    
    
    
    
    
    
    def format_recev_addr_family_id(self, byte_list):
        addr_family_id = ''
        
        addr_family_id += self.bitSizeCorrection(bin(byte_list[0])[2:], 8)
        addr_family_id += self.bitSizeCorrection(bin(byte_list[1])[2:], 8)
        
        return int(addr_family_id, 2)
    
    
    def format_recev_ip_addr(self, byte_list):
        ip_addr = '{}.{}.{}.{}'.format(byte_list[0], byte_list[1], byte_list[2], byte_list[3])
        
        return ip_addr    
    
    
    def format_recev_metric(self, byte_list):
        metric = ''
                
        metric += self.bitSizeCorrection(bin(byte_list[0])[2:], 8)
        metric += self.bitSizeCorrection(bin(byte_list[1])[2:], 8)
        metric += self.bitSizeCorrection(bin(byte_list[2])[2:], 8)
        metric += self.bitSizeCorrection(bin(byte_list[3])[2:], 8)
        
        return int(metric, 2)    
    
    
    
    def bitSizeCorrection(self, myBits, size):
        myBits = myBits
        
        #maybe make a check it 'myBits' is larger than wanted 'size'
        # don't think it is needed
        
        i = 0
        
        while len(myBits) < size:
            myBits = '0' + myBits
        
        
        
        #this returns '0011' not '0b0011'
        return myBits
    
    
    
    
    

#f = Format()

#command = 2
#print(f.formatAddrFamilyID(2))
