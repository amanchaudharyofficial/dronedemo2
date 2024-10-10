# messageHandler
from ctypes import memset,memmove

def processMessage(buffer):
    # process initialbuffer and get msg_id, dest_id
    # if dest_id = ours, process further; else no action
    print("In message handler: processMessage")
    msg_id_rcvd, dest_id_rcvd, src_id_rcvd = processMsgHeader(buffer)
    print("Received MessageId DestinationCSCI SourceCSCI: ",
          msg_id_rcvd, dest_id_rcvd, src_id_rcvd)

    if(dest_id_rcvd == CSCI_ID_ENUM.NSA.value):
    	if (msg_id_rcvd == MFD_NSA_CONFIG_NLP_ENGINE_MSG_ID):
    		print("msg identified: MFD_NSA_CONFIG_NLP_ENGINE_MSG_ID")
    	elif (msg_id_rcvd == LDA_NSA_INIT_RA_DA_DATA_MSG_ID):
			print("msg identified: LDA_NSA_INIT_RA_DA_DATA_MSG_ID")
	     	struct_init_rada = STRUCT_APPLICATION_STATE()
	     	memset(addressof(app_state), 0, sizeof(struct_init_rada))
	     	memmove(addressof(app_state), buffer, sizeof(struct_init_rada))
	     	processMsg_Init_RADA(struct_init_rada)
	    else if (msg_id_rcvd == LDA_NSA_INIT_DRONE_DATA_MSG_ID):
	     	print("msg identified: LDA_NSA_INIT_DRONE_DATA_MSG_ID: ")

	    else if (msg_id_rcvd == DMM_NSA_CMD_TO_TEXT_MSG_ID):
	     	print("msg identified: DMM_NSA_CMD_TO_TEXT_MSG_ID")

	    else if (msg_id_rcvd == DMM_NSA_SELF_TEST_REPORT_MSG_ID):
	     	print("msg identified: DMM_NSA_SELF_TEST_REPORT_MSG_ID")

	    else if (msg_id_rcvd == MFD_NSA_TEXT_TO_CMD_MSG_ID):
	     	print("msg identified: MFD_NSA_TEXT_TO_CMD_MSG_ID")

	    else
	     	print("Unidentified message for NSA module")
    else
	print("Message not destined for NSA module")
     	
    
    
    
# process Message Header   
def processMsgHeader(buffer):
    # process msg header, return msg_id, dest_id, src_id
   msg_header = STRUCT_MESSAGE_HEADER()
   memset(addressof(msg_header), 0, sizeof(msg_header))
   memmove(addressof(msg_header), buffer, sizeof(msg_header))
   msgId = msg_header.msg_id
   dstId = msg_header.dest_csci_id
   srcId = msg_header.src_csci_id
   
   return msgId, dstId, srcId
   

# init RA_DA
def processMsg_Init_RADA(STRUCT_APPLICATION_STATE msg):
    print("in function processMsg_Init_RADA")
    # process individual, get reqd fields and return the values
    # Convert the ctypes array to a byte string
    
    byte_string = bytes(msg.csci_name)
    # Decode the byte string into a regular string using the desired encoding (e.g., UTF-8)
    decoded_string = byte_string.decode('utf-8')
    print("app_state: ",decoded_string)
 
 
# init drone msg   
   
# enable_disable state
    
# command_to_text
   
# self test report
    
# configNLPEngine
    
# text_to_command
