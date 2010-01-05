# -*- coding: utf-8 -*-
import string


def generate_pdu(params_dict):
    s = SMS()
    s.sms_data = params_dict
    s.generate_pdu()
    PDU = ""

    for part in s.pdu:
        PDU = PDU + part
    return PDU


class SMS:
    def __init__(self):
        # GSM7 default aplhabet - letter and corresponding hex value
        self.default = {
            '@': 0x00,
            '£': 0x01,
            '$': 0x02,
            '¥': 0x03,
            'è': 0x04,
            'é': 0x05,
            'ù': 0x06,
            'ì': 0x07,
            'ò': 0x08,
            'Ç': 0x09,
            '\n': 0x0a,
            'Ø': 0x0b,
            'ø': 0x0c,
            '\
': 0x0d,
            'Å': 0x0e,
            'å': 0x0f,
            '\u0394': 0x10,
            '_': 0x11,
            '\u03a6': 0x12,
            '\u0393': 0x13,
            '\u039b': 0x14,
            '\u03a9': 0x15,
            '\u03a0': 0x16,
            '\u03a8': 0x17,
            '\u03a3': 0x18,
            '\u0398': 0x19,
            '\u039e': 0x1a,
            '€': 0x1b,
            'Æ': 0x1c,
            'æ': 0x1d,
            'ß': 0x1e,
            'É': 0x1f,
            ' ': 0x20,
            '!': 0x21,
            '"': 0x22,
            '#': 0x23,
            '¤': 0x24,
            '%': 0x25,
            '&': 0x26,
            '\'': 0x27,
            '(': 0x28,
            ')': 0x29,
            '*': 0x2a,
            '+': 0x2b,
            ',': 0x2c,
            '-': 0x2d,
            '.': 0x2e,
            '/': 0x2f,
            '0': 0x30,
            '1': 0x31,
            '2': 0x32,
            '3': 0x33,
            '4': 0x34,
            '5': 0x35,
            '6': 0x36,
            '7': 0x37,
            '8': 0x38,
            '9': 0x39,
            ':': 0x3a,
            ';': 0x3b,
            '<': 0x3c,
            '=': 0x3d,
            '>': 0x3e,
            '?': 0x3f,
            '¡': 0x40,
            'A': 0x41,
            'B': 0x42,
            'C': 0x43,
            'D': 0x44,
            'E': 0x45,
            'F': 0x46,
            'G': 0x47,
            'H': 0x48,
            'I': 0x49,
            'J': 0x4a,
            'K': 0x4b,
            'L': 0x4c,
            'M': 0x4d,
            'N': 0x4e,
            'O': 0x4f,
            'P': 0x50,
            'Q': 0x51,
            'R': 0x52,
            'S': 0x53,
            'T': 0x54,
            'U': 0x55,
            'V': 0x56,
            'W': 0x57,
            'X': 0x58,
            'Y': 0x59,
            'Z': 0x5a,
            'Ä': 0x5b,
            'Ö': 0x5c,
            'Ñ': 0x5d,
            'Ü': 0x5e,
            '§': 0x5f,
            '¿': 0x60,
            'a': 0x61,
            'b': 0x62,
            'c': 0x63,
            'd': 0x64,
            'e': 0x65,
            'f': 0x66,
            'g': 0x67,
            'h': 0x68,
            'i': 0x69,
            'j': 0x6a,
            'k': 0x6b,
            'l': 0x6c,
            'm': 0x6d,
            'n': 0x6e,
            'o': 0x6f,
            'p': 0x70,
            'q': 0x71,
            'r': 0x72,
            's': 0x73,
            't': 0x74,
            'u': 0x75,
            'v': 0x76,
            'w': 0x77,
            'x': 0x78,
            'y': 0x79,
            'z': 0x7a,
            'ä': 0x7b,
            'ö': 0x7c,
            'ñ': 0x7d,
            'ü': 0x7e,
            'à': 0x7f,
            }

        # initialize list
        self.pdu = []
        self.pdulen = 0
        self.sms_data = dict()


    def binary2other(self, thebinary, transform=str):
        """
        Transforms binary number (represented as string) to hex format
        for example '00101010' = 2A
        if returned value is only one char for example D then leading 0 is added 
        and final result is 0D
        """
        result = str(transform(string.atoi(thebinary,2))[2:])
        #add leading 0 if hex value is only 1 char
        if len(result) == 1:
            result = "0" + result
        return result.upper()

    #method used to transfrom decimal value to 8 signed (default value) binary
    #for example 23 = 00100011
    def dec2bin(self,dec,count=8):
        dec = int(dec)
        return "".join([str((dec >> y) & 1) for y in range(count-1, -1, -1)])
    #method used to transfrom integer value to septets 
    #integer represents letter defined in GSM7 alphabet
    def int2bin(self, n, count=7):
        return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

    #method used to prepare UD bytes
    #takes as arguments: user text and UDH (if present)
    #UD is packed in septets and then returned as bytes
    #Option 1
    def du2bin1(self,text,udh=""):
        chars_reversed = ""
        result = []
        udh_preparred = ""
        #check if UDH (User Data Header) is present
        if len(udh) != 0:
            #if so - count number of full octets in UDH
            no_of_octets = len(udh) / 8 
            #prepare UDH
            # UDH octet 0
            # UDH octet 1
            # UDH octet 3
            # udh_preparred = UDH octet 3 + UDH octet 2 + UDH octet 1
            for i in range (0,no_of_octets):
                udh_preparred = udh_preparred + udh[len(udh)-8-i*8:len(udh)-i*8]
            #count number of fill bits needed
            #udh modulo 7 gives rest which substractet from septes gives number of fill bots
            no_of_fill_bits = 7 - (len(udh) % 7)
            #check if there is a need to add fill bits
            if no_of_fill_bits != 0:
                #add fill bits (zeros)
                udh_preparred = udh_preparred.zfill(7*(len(udh)/7)+7)
        #read chars in text in revere order
        #each char is converted to septet according to GSM7 coding table
        for c in reversed(text):            
            chars_reversed = chars_reversed + str(self.int2bin(self.default[c]))                      
                #final string of bits is ready
        final = chars_reversed + udh_preparred
        #form UD to bytes, the most important bytes are first
        #UD
        # octet 0, octet 1, etc.
        for i in range (0, len(final) / 8):
            result.append(final[len(final)-8-i*8:(len(final)-i*8)])        
        #last octet creation
        tmp = final[0:(len(final) % 8)]
        #fill with zeros
        result.append(tmp.zfill(8))
        #return UD and length in septets
        return result, self.dec2bin(len(final)/7)

    def du2bin2(self,text,datatype="septets"):
        every_second_index = 0
        result = []
        databyte = ""

        for hex_char in text:
            if every_second_index == 1:
                databyte = databyte + hex_char
                result.append(databyte)
                every_second_index = 0
                databyte = ""
            else:
                every_second_index += 1
                databyte = databyte + hex_char

        if datatype == "septets":
            length = (len(text) * 4) / 7
        else:
            length = (len(text) * 4) / 8
        return result, self.dec2bin(length)
                
    def hex2bin4(self,hex_txt):
        return self.dec2bin(int(hex_txt,16),4)

    def udh2bin(self,udh):
        result = ""
        for hex_char in udh:
            result = result + self.hex2bin4(hex_char)
        return result

    #generates whole PDU
    def generate_pdu(self):
        # add SMSC number first
        self.insert_smsc_number()
        #RP(1)|UDHI(1)|SRR(1)|VPF(2)|RD(1)|MTI(2)
        char1 = str(self.sms_data["RP"]) + str(self.sms_data["UDHI"]) + str(self.sms_data["SRR"]) + str(self.sms_data["VPF1"])
        char0 = str(self.sms_data["VPF2"]) + str(self.sms_data["RD"]) + str(self.sms_data["MTI1"]) + str(self.sms_data["MTI2"])
        octet = char1 + char0
        self.pdu.append(self.binary2other(octet,hex))
        #MR - Message Reference
        self.pdu.append(self.binary2other(self.dec2bin(self.sms_data["MR"]),hex))
        #DA - Destination Address
        self.insert_da_number()
        #PID - Protocol Identifier
        self.pdu.append(self.binary2other(self.dec2bin(self.sms_data["PID"]),hex))
        #HC(2)|TC(1)|CM(1)|ALPH(2)|CL(2)        
        char1 = str(self.sms_data["HCDCS1"]) + str(self.sms_data["HCDCS2"])+ str(self.sms_data["TC"]) + str(self.sms_data["CM"])
        char0 = str(self.sms_data["ALPH1"]) + str(self.sms_data["ALPH2"]) + str(self.sms_data["CL1"]) + str(self.sms_data["CL2"])
        octet = char1 + char0
        self.pdu.append(self.binary2other(octet,hex))
                #UDH + UD - User Data Header + User Data 
        #Option 1 - UDH in hex and UD in GSM7
        if int(self.sms_data["UDFormat"]) == 1:
            if self.sms_data["UDHI"] == 1:            
                user_data, ud_length = self.du2bin1(self.sms_data["UD"],self.udh2bin(self.sms_data["UDH"]))
            else:
                user_data, ud_length = self.du2bin1(self.sms_data["UD"])
                #UDL - user data length (in septets)
            self.pdu.append(self.binary2other(ud_length,hex))
            for i in range(0,len(user_data)):
                self.pdu.append(self.binary2other(user_data[i],hex))
        #UDH + UD - User Data Header + User Data
        #Option 2 - UDH and UD in hex - coding depends on alphabet settings (not done yet)
        else:
            if self.sms_data["ALPH1"] == 0 and self.sms_data["ALPH2"] == 0:
                user_data, ud_length = self.du2bin2(self.sms_data["UDH"])
            else:
                user_data, ud_length = self.du2bin2(self.sms_data["UDH"],"octets")
        #UDL - user data length (in septets - for GSM7 or octets for other cases)
            self.pdu.append(self.binary2other(ud_length,hex))
        #UD - append user data
            for i in range(0,len(user_data)):
                self.pdu.append(user_data[i])
        #self.pdu.append(user_data)
        return

    def insert_smsc_number(self):
        
        #octet 0 - SMSC number length - hardcoded - 7 octets
        self.pdu.append(hex(0)[2:]+hex(7)[2:])
        #octet 1 - type of number and numbering plan - hardcoded
        self.pdu.append(hex(9)[2:]+hex(1)[2:])
        #octet 3-8 - smsc number
        index2 = 0
        smsc = str(self.sms_data["SMSC"])
        for index in range (len(smsc) / 2):
            self.pdu.append(smsc[index2+1] + smsc[index2])
            index2+=2    
        return

    def insert_da_number(self):
        
        #octet 0 - DA number length - hardcoded - 13 octets
        self.pdu.append(hex(0)[2:]+hex(13)[2:])
        #octet 1 - type of number and numbering plan - hardcoded
        self.pdu.append(hex(9)[2:]+hex(1)[2:])
        #octet 3-9 - da number
        index2 = 0
        da = str(self.sms_data["DA"])
        for index in range (len(da) / 2):
            self.pdu.append(da[index2+1] + da[index2])
            index2+=2    
        self.pdu.append("F"+da[-1:])    

