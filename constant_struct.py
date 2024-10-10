
from ctypes import memmove, memset, addressof, sizeof
import ctypes

from enum import Enum



from ctypes import memmove, memset, addressof, sizeof
import ctypes

from enum import Enum

#### Receive from others
DMM_NSA_CMD_TO_TEXT_MSG_ID	= 17
DMM_NSA_SELF_TEST_REPORT_MSG_ID	= 13 # Instead we can use DMM_NSA_CMD_TO_TEXT_MSG_ID
LDA_NSA_INIT_DRONE_DATA_MSG_ID	= 16
LDA_NSA_INIT_RA_DA_DATA_MSG_ID	= 12
MFD_NSA_TEXT_TO_CMD_MSG_ID  = 19
MFD_NSA_LOAD_MISSION_PLAN_MSG_ID = 20

#### FROM NSA send to
NSA_LDA_INIT_DATA_REQ_MSG_ID	= 3
NSA_MFD_CONFIG_NLP_ENGINE_MSG_ID	= 1
NSA_MFD_DECODE_VOICE_IN_COMMAND_RESP_MSG_ID	= 4
NSA_MFD_STRING_MSG_ID = 1
NSA_MFD_RECOGNIZED_CMD_ID =2 
MFD_ASR_START_STOP_COMMAND_MSG_ID = 20
ASR_MFD_VOICE_TO_TEXT_COMMAND_MSG_ID = 1


# IRS enums and constants

INT_8 = ctypes.c_char
INT_16 = ctypes.c_short
INT_32 = ctypes.c_int 
REAL_32 = ctypes.c_float

CSCI_ID = ctypes.c_uint8
MESSAGE_ID = ctypes.c_uint16
MESSAGE_LENGTH = ctypes.c_uint16
STRING_100 = ctypes.c_uint8 * 100
STRING_151 = ctypes.c_uint8 * 151
STRING_251 = ctypes.c_uint8 * 251
CWP_INDEX = ctypes.c_uint8
DRONE_HEALTH_STATUS = ctypes.c_uint8
STRING_6 = ctypes.c_uint8 * 6
STRING_11 = ctypes.c_uint8 * 11
STRING_21 = ctypes.c_uint8 * 21
IP_ADDRESS = ctypes.c_uint8 * 16
ACTION_ID = ctypes.c_uint8
UNIT_ID = ctypes.c_uint8
SYSTEM_STATUS = ctypes.c_uint8
ARMED_STATUS = ctypes.c_uint8
MAVLINK_VERSION = ctypes.c_uint8
START_STOP_FLAG = ctypes.c_uint8


CAMERA_TYPE = ctypes.c_uint8 #0- PTZ
DRONE_TYPE = ctypes.c_uint8	#0- SURVEILLANCE, 1- LOGISTIC
ENTITY_TYPE = ctypes.c_uint8  # legalcheck, 0-1: 0- RESTRICTED_AREA, 1- DANGER_AREA
NATURAL_DIALOG_ENABLED_DISABLED_FLAG = ctypes.c_bool
NLP_COMMAND = ctypes.c_uint8 
SHAPE_TYPE = ctypes.c_uint8 
MISSION_OBJECTIVE = ctypes.c_uint8
OBJECT_TYPE  = ctypes.c_uint8
TIME_IN_MINUTES = ctypes.c_uint8
VERTICAL_HORIZONTAL_SEPARATION = ctypes.c_uint8

MAX_NO_OF_POINTS_IN_POLYGON = 40
MAX_NO_OF_DRONES_IN_A_MISSION = 10

class CSCI_ID_ENUM(Enum):
    MFD = 1
    LDA = 2
    DMM = 3
    NSA = 4
    VPA = 5
    ADSS = 6
    ANAV = 7
    NDA = 8
    GFC = 9
    ALL = 10
 
class ENTITY_TYPE_ENUM(Enum):
    RESTRICTED_AREA = 0
    DANGER_AREA = 1 
    
class SHAPE_TYPE_ENUM(Enum):
    POLYGON = 0
    CIRCLE = 1 
    
class DRONE_TYPE_ENUM(Enum):
    SURVEILLANCE = 0
    LOGISTIC = 1 

#IDD and IDD Structs
class STRUCT_MESSAGE_HEADER(ctypes.Structure):  
    _pack_ = 1 #packing of bytes
    _fields_ = [
        ("src_csci_id",ctypes.c_uint8),
        ("dest_csci_id",ctypes.c_uint8),
        ("msg_id",ctypes.c_uint8),
        ("msg_len",ctypes.c_uint16),
        ("src_unit_id",ctypes.c_uint8),
        ("dest_unit_id",ctypes.c_uint8)
    ]

class STRUCT_LATITUDE_LONGITUDE(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("latitude", REAL_32),
        ("longitude", REAL_32)
     ] 
    
class STRUCT_COMMAND_TO_TEXT_ID(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("no_of_missions", ctypes.c_uint8),
        ("mission_ids", ctypes.c_uint8), #array num of missions no_of_missions
        ("no_of_drones", ctypes.c_uint8),
        ("drone_ids", ctypes.c_uint8), #array no_of_drones
        ("no_of_areas", ctypes.c_uint8),
        ("area_ids", ctypes.c_uint8) #array no_of_areas
    ]

class STRUCT_CMD_TO_TEXT(ctypes.Structure):   #msg1  DMM_NSA_CMD_TO_TEXT_MSG_ID = 17  DMM_NSA_SELF_TEST_REPORT_MSG_ID = 18
    _pack_ = 1
    _fields_ = [
        ("struct_msg_header", STRUCT_MESSAGE_HEADER),
        ("command_to_text_data", STRUCT_COMMAND_TO_TEXT_ID), 
        ]

class SELF_TEST_OF_DRONE_PARAM(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("motor_test", DRONE_HEALTH_STATUS),
        ("arm_disarm_status", DRONE_HEALTH_STATUS),
        ("hdop", DRONE_HEALTH_STATUS),
        ("sats", DRONE_HEALTH_STATUS),
        ("battery_status", DRONE_HEALTH_STATUS),
        ("arm_movement", DRONE_HEALTH_STATUS),
    ]


class STRUCT_SELF_TEST_REPORT_OF_DRONE(ctypes.Structure): #msg2 DMM_NSA_SELF_TEST_REPORT_MSG_ID= 18 Instead we can use DMM_NSA_CMD_TO_TEXT_MSG_ID     _pack_ = 1
    _fields_ = [
        ("struct_msg_header", STRUCT_MESSAGE_HEADER),
        ("struct_self_test_of_drone", SELF_TEST_OF_DRONE_PARAM)
    ]

class STRUCT_DRONE_REG_ID(ctypes.Structure): 
    _pack_ = 1
    _fields_ = [
        ("drone_unit_id", UNIT_ID),
        ("callsign", STRING_11),
        ("camera_ip_address", IP_ADDRESS),
        ("camera_port_no", INT_32),
        ("flight_controller_ip_address", IP_ADDRESS),
        ("flight_controller_port_no", INT_32),
        ("jetson_ip_address", IP_ADDRESS),
        ("jetson_port_no", INT_32),
        ("drone_type", DRONE_TYPE),
        ("camera_type", CAMERA_TYPE),
        ("camera_url", STRING_151)             
    ]

class STRUCT_INIT_DRONE_DATA(ctypes.Structure):  #msg3 LDA_NSA_INIT_DRONE_DATA_MSG_ID = 16
    _pack_ = 1
    _fields_ = [
        ("struct_msg_header", STRUCT_MESSAGE_HEADER),
        ("drone_data", STRUCT_DRONE_REG_ID)
        ]


class AREA(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("drone_unit_id", UNIT_ID),
        ("system_status", SYSTEM_STATUS),
        ("armed_status_flag", ARMED_STATUS),
        ("remaining_battery", ctypes.c_uint8),
        ("mavlink_version", MAVLINK_VERSION),
        ("radius", ctypes.c_int16),
        ("centre_lat_long", STRUCT_LATITUDE_LONGITUDE)
    ]


class STRUCT_CIRCLE(ctypes.Structure):  
    _pack_ = 1
    _fields_ = [
        ("radius", INT_16),
        ("centre_lat_long", STRUCT_LATITUDE_LONGITUDE)
    ]

class STRUCT_POLYGON(ctypes.Structure):  
    _pack_ = 1
    _fields_ = [
        ("no_of_points", INT_16),
       # ("polygon_lat_long",STRUCT_LATITUDE_LONGITUDE)
        ("polygon_lat_long", STRUCT_LATITUDE_LONGITUDE*MAX_NO_OF_POINTS_IN_POLYGON) #array of no_of_points
    ]
# 

class STRUCT_AREA(ctypes.Structure):  
    _pack_ = 1
    _fields_ = [
        ("area_shape_type", SHAPE_TYPE),
        ("struct_circle", STRUCT_CIRCLE),
        ("struct_polygon", STRUCT_POLYGON)        
    ]


class STRUCT_ENTITY_DATA(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("entity_type", ENTITY_TYPE),
        ("entity_id", ctypes.c_uint16),
        ("entity_name", STRING_21),
        ("struct_entity_area", STRUCT_AREA),
        ("colour", ctypes.c_uint8),
        ("look_ahead_time", ctypes.c_uint8),
        ("max_height", ctypes.c_uint16),
        ("min_height", ctypes.c_uint16)
    ]


class STRUCT_INIT_RA_DA_DATA(ctypes.Structure):  #msg4 LDA_NSA_INIT_RA_DA_DATA_MSG_ID = 12
    _pack_ = 1
    _fields_ = [
        ("struct_msg_header", STRUCT_MESSAGE_HEADER),
        ("ra_da_data", STRUCT_ENTITY_DATA),
        ("action_id", ACTION_ID)        
    ]






## Msg id NSA_LDA_INIT_DATA_REQ_MSG_ID  has only STRUCT_MESSAGE_HEADER   #msg5 NSA_LDA_INIT_DATA_REQ_MSG_ID  = 3


class STRUCT_CONFIG_NLP_ENGINE(ctypes.Structure):  #msg6  NSA_MFD_CONFIG_NLP_ENGINE_MSG_ID = 1
    _pack_ = 1
    _fields_ = [
        ("struct_msg_header", STRUCT_MESSAGE_HEADER),
        ("natural_dialog_enabled_disabled_flag", NATURAL_DIALOG_ENABLED_DISABLED_FLAG)              
    ]


class STRUCT_NLP_COMMAND(ctypes.Structure):  #NSA_MFD_DECODE_VOICE_IN_COMMAND_RESP_MSG_ID = 4 Instead we can use NSA_MFD_RECOGNIZED_CMD_ID = 2
    _pack_ = 1
    _fields_ = [
        ("struct_msg_header", STRUCT_MESSAGE_HEADER),
        ("nlp_command", NLP_COMMAND)              
    ]


class STRUCT_RECOGNIZED_COMMAND(ctypes.Structure):  #msg7 NSA_MFD_RECOGNIZED_CMD_ID = 2
    _pack_ = 1
    _fields_ = [
        ("struct_msg_header", STRUCT_MESSAGE_HEADER),
        ("nlp_command", NLP_COMMAND),
        ("cmd_arg_id", ctypes.c_uint8) 
    ]


class STRUCT_STRING_MSG(ctypes.Structure):  #msg8 NSA_MFD_STRING_MSG_ID = 1
    _pack_ = 1
    _fields_ = [
        ("struct_msg_header", STRUCT_MESSAGE_HEADER),
        ("string151", STRING_151)              
    ]


class STRUCT_TEXT_TO_CMD_MSG(ctypes.Structure):  #msg9 MFD_NSA_TEXT_TO_CMD_MSG_ID  = 19
    _pack_ = 1
    _fields_ = [
        ("struct_msg_header", STRUCT_MESSAGE_HEADER),
        ("string151", STRING_251)              
    ]

class STRUCT_VOICE_TO_TEXT_COMMAND(ctypes.Structure):  #msg9 ASR_MFD_VOICE_TO_TEXT_COMMAND_MSG_ID  = 19
    _pack_ = 1
    _fields_ = [
               ("string151", STRING_251)              
    ]

class STRUCT_ASR_MFD_VOICE_TEXT_COMMAND_MSG(ctypes.Structure):  #msg9 ASR_MFD_VOICE_TO_TEXT_COMMAND_MSG_ID = 20
    _pack_ = 1
    _fields_ = [
        ("struct_msg_header", STRUCT_MESSAGE_HEADER),
        ("text_msg", STRUCT_VOICE_TO_TEXT_COMMAND)
    ]


class STRUCT_START_STOP_VOICE_COMMAND(ctypes.Structure):  #msg9 ASR_MFD_VOICE_TO_TEXT_COMMAND_MSG_ID  = 19
    _pack_ = 1
    _fields_ = [
               ("start_stop_flag", START_STOP_FLAG)              
    ]

class STRUCT_MFD_ASR_START_STOP_VOICE_COMMAND(ctypes.Structure):  #msg4 MFD_ASR_START_STOP_COMMAND_MSG_ID = 1
    _pack_ = 1
    _fields_ = [
        ("struct_msg_header", STRUCT_MESSAGE_HEADER),
        
        ("start_stop_command", STRUCT_START_STOP_VOICE_COMMAND)        
    ]


class STRUCT_MISSION_AREA_MIN_MAX_HEIGHT(ctypes.Structure):  
    _pack_ = 1
    _fields_ = [
        ("min_height", ctypes.c_uint16),
        ("max_height", ctypes.c_uint16)
    ]


class STRUCT_DRONE_REG_ID(ctypes.Structure):  
    _pack_ = 1
    _fields_ = [
        ("struct_msg_header", STRUCT_MESSAGE_HEADER),
        ("drone_unit_id", STRING_6),
        ("drone_ip_address", IP_ADDRESS),
        ("drop_loc", STRUCT_LATITUDE_LONGITUDE)              
    ]



class STRUCT_COLLISION_PARAMETERS(ctypes.Structure):  
    _pack_ = 1
    _fields_ = [
        ("vertical_separation_in_mtrs", VERTICAL_HORIZONTAL_SEPARATION),
        ("horizontal_separation_in_mtrs", VERTICAL_HORIZONTAL_SEPARATION)
    ]

class STRUCT_DRONE(ctypes.Structure):  
    _pack_ = 1
    _fields_ = [
        ("drone_unit_id", UNIT_ID),
        ("drone_ip_address", IP_ADDRESS),
        ("drop_loc", STRUCT_LATITUDE_LONGITUDE)              
    ]


class STRUCT_MISSION_PLAN(ctypes.Structure):  
    _pack_ = 1
    _fields_ = [
    ("mission_id", ctypes.c_uint8),
    ("mission_area", STRUCT_AREA),
    ("mission_name", STRING_21),
    ("struct_min_max_height", STRUCT_MISSION_AREA_MIN_MAX_HEIGHT),
    ("mission_description", STRING_151),
    ("mission_objective", MISSION_OBJECTIVE),
    ("object_type", OBJECT_TYPE),
    ("no_of_drones", ctypes.c_uint8),
    ("struct_drone", STRUCT_DRONE*MAX_NO_OF_DRONES_IN_A_MISSION), #array: no of drones
    ("safe_distance_btwn_drones", ctypes.c_uint8),
    ("collision_parameters", STRUCT_COLLISION_PARAMETERS),
    ("look_ahead_time_in_mins", TIME_IN_MINUTES),
    ("warning_time_in_mins", TIME_IN_MINUTES),
    ("gcs_loc", STRUCT_LATITUDE_LONGITUDE)
    ]

class STRUCT_LOAD_MISSION_PLAN_MSG(ctypes.Structure):  #msg9 MFD_NSA_LOAD_MISSION_PLAN_MSG_ID = 20
    _pack_ = 1
    _fields_ = [
        ("struct_msg_header", STRUCT_MESSAGE_HEADER),
        ("mission_plan", STRUCT_MISSION_PLAN)
    ]




#### commands for exe
# pyinstaller --onefile text.py
# pyinstaller --onefile text.spec
class STRUCT_APPLICATION_STATE(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("struct_msg_header", STRUCT_MESSAGE_HEADER),
        ("hardware_id", CSCI_ID),
        ("csci_id", CSCI_ID),
        ("csci_state", CSCI_ID),
        ("csci_name", STRING_100)
    ]
    
class MyStructure(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_uint8, 4)
    ]

# Create an instance of the structure
my_instance = MyStructure()

# Enter a 4-bit value into the "id" field
value = 0b1010  # Example value
my_instance.id |= (value & 0b1111)  # Set the least significant 4 bits of "id" with the value

# Print the value of the "id" field
print("ID:", my_instance.id)



#### commands for exe
# pyinstaller --onefile text.py
# pyinstaller --onefile text.spec
