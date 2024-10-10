import socket
import os
import IndianEnglishModel
import subprocess
from subprocess import call, PIPE, Popen
from logger import DailyMessageLogger
from ctypes import memset, memmove
from constant_struct import *
from json_handler import users_dict
HOST ="192.168.1.126"  # Listen on all interfaces
PORT = 5051
logger = DailyMessageLogger()
# with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#     s.bind((HOST, PORT))
# with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#     s.bind((HOST, PORT))
mission_id_name_list ={}
users_dict.items()
def receive_message():
  """
  Receives a message over UDP.
  """
  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
  #data, addr = s.recvfrom(1024)
    buffer, addr = s.recvfrom(1024)
    print("buffer: ", buffer)
    processData(buffer)
    logger.log_message(f"BY RECEIVER Received message: {buffer}")
    print(f"inside recived message Received message: {buffer}")
  #return buffer.decode()

def processData(buffer):
     msg_header = STRUCT_MESSAGE_HEADER()
     memset(addressof(msg_header), 0, sizeof(msg_header))
     memmove(addressof(msg_header), buffer, sizeof(msg_header))
     print("src dest ",msg_header.src_csci_id, msg_header.dest_csci_id)
     msg_id_rcvd = msg_header.msg_id
     dest_id_rcvd = msg_header.dest_csci_id
     print ("msg id: ",msg_id_rcvd ,"dst_id: ",dest_id_rcvd)
     if(dest_id_rcvd == CSCI_ID_ENUM.NSA.value):
         if (msg_id_rcvd == NSA_MFD_CONFIG_NLP_ENGINE_MSG_ID):
             print("msg identified: MFD_NSA_CONFIG_NLP_ENGINE_MSG_ID")
            #  os.popen(["bash", "home/crl/Desktop/drone/stop.sh"])
            #  stt = subprocess.Popen(["IndianEnglishModel.py"]+cmd, stdout=subprocess.PIPE, text=True)
            #  print(stt)
             call(["python","IndianEnglishModel.py"])
            #  print("modiiiii",aman)
            #  IndianEnglishModel.py.kill()
            #  file_path='IndianEnglishModel.py'
            #  def execndianEnglishModel.py'
            #  def execute_python_file(file_path):
            #     try:
            #          os.system(f'python{file_path}')
            #     except FileNotFoundError:
            #         print("file path does not exists ")
         
         
                 
             
         elif (msg_id_rcvd == LDA_NSA_INIT_RA_DA_DATA_MSG_ID):
             print("msg identified: LDA_NSA_INIT_RA_DA_DATA_MSG_ID")
             print("INIT RADA DATA RECEIVED")
             processInitRADA(buffer)
             #processTestAppState(buffer)
             
         elif (msg_id_rcvd == LDA_NSA_INIT_DRONE_DATA_MSG_ID):
             print("msg identified: LDA_NSA_INIT_DRONE_DATA_MSG_ID: ")
             print("INIT DRONE DATA RECEIVED")
             os.popen('sh/home/crl/Desktop/drone/stop.sh')
             
            # processInitDroneData(buffer)
             
         elif (msg_id_rcvd == DMM_NSA_CMD_TO_TEXT_MSG_ID):
             print("msg identified: DMM_NSA_CMD_TO_TEXT_MSG_ID")
             processCommandToText(buffer)
             
         elif (msg_id_rcvd == DMM_NSA_SELF_TEST_REPORT_MSG_ID):
             print("msg identified: DMM_NSA_SELF_TEST_REPORT_MSG_ID")
             
         elif (msg_id_rcvd == MFD_NSA_TEXT_TO_CMD_MSG_ID):
             print("msg identified: MFD_NSA_TEXT_TO_CMD_MSG_ID")     
                  
         elif (msg_id_rcvd == MFD_NSA_LOAD_MISSION_PLAN_MSG_ID):
             print("msg identified: MFD_NSA_LOAD_MISSION_PLAN_MSG_ID")
             processMissionPlan(buffer)
             
         else:
             print("Unidentified message for NSA module")
     else:
         print("Message not destined for NSA module")

def processMissionPlan(buffer):
    missionPlan = STRUCT_MISSION_PLAN()
    memset(addressof(missionPlan), 0, sizeof(missionPlan))
    memmove(addressof(missionPlan), buffer, sizeof(missionPlan))
       
    print("mission_id: ", missionPlan.mission_id),
    #print("mission_area", STRUCT_AREA),
    
    byte_string = bytes(missionPlan.mission_name)
    # Decode the byte string into a regular string using the desired encoding (e.g., UTF-8)
    decoded_string = byte_string.decode('utf-8')
    print("mission_name: ", decoded_string),
    # added to id string list
    if missionPlan.mission_id in mission_id_name_list:
        mission_id_name_list.update({missionPlan.mission_id,decoded_string})
    else:
        mission_id_name_list['missionPlan.mission_id']=decoded_string 
    #print("struct_min_max_height", STRUCT_MISSION_AREA_MIN_MAX_HEIGHT),
    
    print("mission_description: ", missionPlan.mission_description),
    print("mission_objective: ",missionPlan.mission_objective),
    print("object_type: ", OBJECT_TYPE),
    
    print ("no_of_drones: ", missionPlan.no_of_drones),
    #print("struct_drone", STRUCT_DRONE),#array: no of drones
    #print("safe_distance_btwn_drones", ctypes.c_uint8),
    #print("collision_parameters", STRUCT_COLLISION_PARAMETERS),
    print("look_ahead_time_in_mins: ", missionPlan.look_ahead_time_in_mins),
    print("warning_time_in_mins: ", missionPlan.warning_time_in_mins),
    #print("gcs_loc", STRUCT_LATITUDE_LONGITUDE)

def processInitRADA(buffer):
    initRaDaData = STRUCT_INIT_RA_DA_DATA
    memset(addressof(initRaDaData), 0, sizeof(initRaDaData))
    memmove(addressof(initRaDaData), buffer, sizeof(initRaDaData))
    print("ra_da_data: ")
    print("entity_type ", initRaDaData.ra_da_data.entity_type)
    print("entity_id ",initRaDaData.ra_da_data.entity_id)

    byte_string = bytes(initRaDaData.ra_da_data.entity_name)
    decoded_string = byte_string.decode('utf-8')
    print ("entity_name ", decoded_string)
    print("struct_entity_area ")
    print("colour ", initRaDaData.ra_da_data.colour)
    print("look_ahead_time ", initRaDaData.ra_da_data.look_ahead_time)
    print("max_height ", initRaDaData.ra_da_data.max_height)
    print("min_height ",initRaDaData.ra_da_data.min_height)    
    print("action_id: ", initRaDaData.action_id)

def processInitDroneData(buffer):
    initDroneData = STRUCT_INIT_DRONE_DATA
    memset(addressof(initDroneData), 0, sizeof(initDroneData))
    memmove(addressof(initDroneData), buffer, sizeof(initDroneData))
    
    #make list for each drone: no array, drone data received seperately
    print("drone_data: ")
    print("drone_unit_id ", initDroneData.drone_data.drone_unit_id)

def processCommandToText(buffer):
    CommndToTxt=STRUCT_COMMAND_TO_TEXT_ID()
    memset(addressof(CommndToTxt), 0, sizeof(CommndToTxt))
    memmove(addressof(CommndToTxt), buffer, sizeof(CommndToTxt))

    print("number of missions :",CommndToTxt.no_of_missions)
    print("mission id:",CommndToTxt.mission_ids)
    print("no of drones:",CommndToTxt.no_of_drones)
    print("drone id:",CommndToTxt.drone_ids)
    print("no of areas:",CommndToTxt.no_of_areas)
    print("area id:",CommndToTxt.area_ids)

def processTestAppState(buffer):
    missionPlan = STRUCT_APPLICATION_STATE()
    memset(addressof(missionPlan), 0, sizeof(missionPlan))
    memmove(addressof(missionPlan), buffer, sizeof(missionPlan))
    
    print("hardware_id: ",missionPlan.hardware_id)
    byte_string = bytes(missionPlan.csci_name)
    # Decode the byte string into a regular string using the desired encoding (e.g., UTF-8)
    decoded_string = byte_string.decode('utf-8')
    print("app_state: ", decoded_string)




# def processASR(buffer):


# Example usage

#message = receive_message()
#print(f"Received message: {message}")