import socket
from logger import DailyMessageLogger
from constant_struct import *

#DEST="192.168.111.46"      #IP Arohan
#DEST = "10.10.40.42"  # Change to target IP if needed
#DEST = "192.168.171.42"
#DEST = "192.168.111.95"
#DEST = "192.168.111.46"  #VLCC
#DEST="192.168.171.42"'
DEST="192.168.171.201"
PORT = 5100
logger = DailyMessageLogger()


def send_message(message,DEST,PORT):
  """
  Sends a message over UDP.;
  """
  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    print(message)
    s.sendto(message.encode(), (DEST, PORT))
    logger.log_message(f"Sent message inside send for logg message: {message}")

# Example usage
#
#message = "Hello from sender!"
#send_message(message)
#print(f"Sent message: {message}")

# def sendMsg(HOST,PORT):
# 	valuesrc = 0b0010 #4
# 	valuedst = 0b0100  #4
  

# 	app_state_hdr = STRUCT_MESSAGE_HEADER(valuesrc,valuedst, 20, 6, 1,1)
  
# 	print(app_state_hdr, sizeof(app_state_hdr))

# 	str_name =('a','b')
# 	# Define a byte string (e.g., b'Hello')
# 	# byte_string = b'Hello'

# 	# Convert the byte string to a ctypes array
# 	# arr = (ctypes.c_uint8 * 100)(*byte_string)

# 	pp_state = STRUCT_ASR_MFD_VOICE_TEXT_COMMAND_MSG(app_state_hdr,4,5,6,arr)
  
# 	header_bytes = bytes(app_state_hdr)
# 	pp_state_bytes = bytes(pp_state)
    
# 	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#           s.sendto(pp_state_bytes,(HOST, PORT))
#           print("bytes sent: ",pp_state_bytes)


# Hardcoded IP and Port
IP_LOCAL = "127.0.0.1"
PORT_LOCAL= 12345

# Send text over UDP
def send_udp_tts_message(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode('utf-8'), (IP_LOCAL, PORT_LOCAL))
    sock.close()



def sendMsg(DEST,PORT,temp):
    
  print("in the function")
  print("val third ", temp)
  # valuesrc = 0b0010 #4
  # valuedst = 0b0100  #4
  valuesrc = 10
  valuedst = 1
  asr_text_msg = STRUCT_ASR_MFD_VOICE_TEXT_COMMAND_MSG()#asr_text_header, asr_text_data
  asr_text_msg.struct_msg_header.src_csci_id=10
  asr_text_msg.struct_msg_header.dest_csci_id=1
  asr_text_msg.struct_msg_header.msg_id=1
  asr_text_msg.struct_msg_header.msg_len=6
  asr_text_msg.struct_msg_header.src_unit_id=1
  asr_text_msg.struct_msg_header.dest_unit_id=1
  #asr_text_header = STRUCT_MESSAGE_HEADER(valuesrc,valuedst,1, 6, 1,1)
 
  bytes_object = bytes(temp, 'utf-8')
  arr = (ctypes.c_uint8 * 251)(*bytes_object)
  # arr = ctypes.c_uint8(temp)
  #asr_text_data = STRUCT_VOICE_TO_TEXT_COMMAND(arr)
  textMsg=STRUCT_VOICE_TO_TEXT_COMMAND(arr)
  asr_text_msg.text_msg = textMsg
     
  
  # header_bytes = bytes(asr_text_header)
  # asr_text_bytes = bytes(asr_text_msg)

  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
          #s.sendto(asr_text_msg,("192.168.110.102", 5007))
          s.sendto(asr_text_msg,(DEST, PORT))
          print("bytes sent: ",asr_text_msg)

def sendInit(HOST,PORT):
    print("send initial message")
    valuesrc = 0b0010 #4
    valuedst = 0b0100  #4
    init_msg = STRUCT_MESSAGE_HEADER(valuesrc,valuedst, 12, 6, 1,1)
    init_msg_bytes = bytes(init_msg)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
          s.sendto(init_msg_bytes,(DEST, 5007))
          print("bytes sent: ",init_msg_bytes)