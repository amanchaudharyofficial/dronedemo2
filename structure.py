import ctypes

class STRUCT_MSG_HEADER(ctypes.Structure):
    _pack_ = 1 #packing of bytes
    _fields_ = [
        ("src_csci_id",ctypes.c_uint8,4),
        ("dest_csci_id",ctypes.c_uint8,4),
        ("msg_id",ctypes.c_uint8),
        ("msg_len",ctypes.c_uint16),
        ("src_unit_id",ctypes.c_uint8),
        ("dest_unit_id",ctypes.c_uint8)
    ]


print("header size")
struct_msg_header=STRUCT_MSG_HEADER()
print(ctypes.sizeof(struct_msg_header)) #size of header

value = 0b1010
struct_msg_header.src_csci_id = value
print(struct_msg_header.src_csci_id)


