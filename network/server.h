#ifndef __NWAY_GATEWAY_XML_OP_NETWORK_SERVER_H__
#define __NWAY_GATEWAY_XML_OP_NETWORK_SERVER_H__
#include "../libs/libiop/inc/iop.h"
#include "../libs/libiop/inc/iop_log_service.h"
#include "../libs/libiop/inc/iop_server.h"

void set_fs_conf_path(const char* fs_path);
int push_server(short port); //���ڽ���Ϣ���͸����ӵķ�����

int exch_server(short port); //����Զ�˿ͻ������������������ݽ��� 

#endif