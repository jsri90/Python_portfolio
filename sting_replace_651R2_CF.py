def replace_string( *args):
    old_text = args[0][0]
    argLen = len(args[0])
    new_text = old_text
    i = 1
    while( i < argLen):
        new_text = new_text.replace(args[0][i], args[0][i + 1])
        i +=2

    return new_text


print('-----------------------------------------------------------------------------------------------------/n/n')



##old_str1 = "SEL_651R2_5362_DNP"
##new_str1 = "SEL_651R2_5361_5362_DNP"
##
##old_str2 = ".BI_"
##new_str2 = "._5362_BI_"
##
##old_str3 = ".AI_", "._5362_AI_"
##
##old_str4 = ".BO_", "._5362_BO_"
##
##new_string = replace_string(string1, old_str1, new_str1, old_str2, new_str2, old_str3, new_str3, old_str4, new_str4)
##print(new_string)



print('----------------------------------------------------------------------------------------------------/n/n')


""" "SEL_651R2_5745_DNP", "SEL_651R2_5744_5745_DNP", ".BI_", "._5745_BI_", ".AI_", "._5745_AI_", ".BO_", "._5745_BO_" """

print('----------------------------------------------------------------------------------------------------/n/n')

list_strings = [[""" pFieldFirst_Bi	:=	ADR(SEL_651R2_5361_DNP.BI_00000_Recloser_Status)	,
	pFieldFirst_Ai	:=	ADR(SEL_651R2_5361_DNP.AI_00000_IA)	,
	pFieldFirst_Bo	:=	ADR(SEL_651R2_5361_DNP.BO_00000_SS1)	,
	pFieldFirst_Ao	:=	0	,
	pFieldFirst_Cnt	:=	0	,
	pDeviceOffline	:=	ADR(SEL_651R2_5361_DNP_POU.Offline)	,
	pPoll	:=	ADR(SEL_651R2_5361_DNP_POU.Poll_Integrity_Obj_60_Cls_1230)	,
	pMessageReceivedCount	:=	ADR(SEL_651R2_5361_DNP_POU.Message_Received_Count)	);""", "SEL_651R2_5361_DNP", "SEL_651R2_5361_5362_DNP", ".BI_", "._5361_BI_", ".AI_", "._5361_AI_", ".BO_", "._5361_BO_"],
                     [""" 	pFieldFirst_Bi	:=	ADR(SEL_651R2_5362_DNP.BI_00000_Recloser_Status)	,
	pFieldFirst_Ai	:=	ADR(SEL_651R2_5362_DNP.AI_00000_IA)	,
	pFieldFirst_Bo	:=	ADR(SEL_651R2_5362_DNP.BO_00000_SS1)	,
	pFieldFirst_Ao	:=	0	,
	pFieldFirst_Cnt	:=	0	,
	pDeviceOffline	:=	ADR(SEL_651R2_5362_DNP_POU.Offline)	,
	pPoll	:=	ADR(SEL_651R2_5362_DNP_POU.Poll_Integrity_Obj_60_Cls_1230)	,
	pMessageReceivedCount	:=	ADR(SEL_651R2_5362_DNP_POU.Message_Received_Count)	);""", "SEL_651R2_5362_DNP", "SEL_651R2_5361_5362_DNP", ".BI_", "._5362_BI_", ".AI_", "._5362_AI_", ".BO_", "._5362_BO_"],
                     [""" 	pFieldFirst_Bi	:=	ADR(SEL_651R2_5405_DNP.BI_00000_Recloser_Status)	,
	pFieldFirst_Ai	:=	ADR(SEL_651R2_5405_DNP.AI_00000_IA)	,
	pFieldFirst_Bo	:=	ADR(SEL_651R2_5405_DNP.BO_00000_SS1)	,
	pFieldFirst_Ao	:=	0	,
	pFieldFirst_Cnt	:=	0	,
	pDeviceOffline	:=	ADR(SEL_651R2_5405_DNP_POU.Offline)	,
	pPoll	:=	ADR(SEL_651R2_5405_DNP_POU.Poll_Integrity_Obj_60_Cls_1230)	,
	pMessageReceivedCount	:=	ADR(SEL_651R2_5405_DNP_POU.Message_Received_Count)	);""", "SEL_651R2_5405_DNP", "SEL_651R2_5405_5460_DNP", ".BI_", "._5405_BI_", ".AI_", "._5405_AI_", ".BO_", "._5405_BO_"],
                     [""" 	pFieldFirst_Bi	:=	ADR(SEL_651R2_5414_DNP.BI_00000_Recloser_Status)	,
	pFieldFirst_Ai	:=	ADR(SEL_651R2_5414_DNP.AI_00000_IA)	,
	pFieldFirst_Bo	:=	ADR(SEL_651R2_5414_DNP.BO_00000_SS1)	,
	pFieldFirst_Ao	:=	0	,
	pFieldFirst_Cnt	:=	0	,
	pDeviceOffline	:=	ADR(SEL_651R2_5414_DNP_POU.Offline)	,
	pPoll	:=	ADR(SEL_651R2_5414_DNP_POU.Poll_Integrity_Obj_60_Cls_1230)	,
	pMessageReceivedCount	:=	ADR(SEL_651R2_5414_DNP_POU.Message_Received_Count)	); """, "SEL_651R2_5414_DNP", "SEL_651R2_5414_5416_DNP", ".BI_", "._5414_BI_", ".AI_", "._5414_AI_", ".BO_", "._5414_BO_"],
                     ["""	pFieldFirst_Bi	:=	ADR(SEL_651R2_5416_DNP.BI_00000_Recloser_Status)	,
	pFieldFirst_Ai	:=	ADR(SEL_651R2_5416_DNP.AI_00000_IA)	,
	pFieldFirst_Bo	:=	ADR(SEL_651R2_5416_DNP.BO_00000_SS1)	,
	pFieldFirst_Ao	:=	0	,
	pFieldFirst_Cnt	:=	0	,
	pDeviceOffline	:=	ADR(SEL_651R2_5416_DNP_POU.Offline)	,
	pPoll	:=	ADR(SEL_651R2_5416_DNP_POU.Poll_Integrity_Obj_60_Cls_1230)	,
	pMessageReceivedCount	:=	ADR(SEL_651R2_5416_DNP_POU.Message_Received_Count)	); """, "SEL_651R2_5416_DNP", "SEL_651R2_5414_5416_DNP", ".BI_", "._5416_BI_", ".AI_", "._5416_AI_", ".BO_", "._5416_BO_"],
                     [""" 	pFieldFirst_Bi	:=	ADR(SEL_651R2_5440_DNP.BI_00000_Recloser_Status)	,
	pFieldFirst_Ai	:=	ADR(SEL_651R2_5440_DNP.AI_00000_IA)	,
	pFieldFirst_Bo	:=	ADR(SEL_651R2_5440_DNP.BO_00000_SS1)	,
	pFieldFirst_Ao	:=	0	,
	pFieldFirst_Cnt	:=	0	,
	pDeviceOffline	:=	ADR(SEL_651R2_5440_DNP_POU.Offline)	,
	pPoll	:=	ADR(SEL_651R2_5440_DNP_POU.Poll_Integrity_Obj_60_Cls_1230)	,
	pMessageReceivedCount	:=	ADR(SEL_651R2_5440_DNP_POU.Message_Received_Count)	);""", "SEL_651R2_5440_DNP", "SEL_651R2_5440_5442_DNP", ".BI_", "._5440_BI_", ".AI_", "._5440_AI_", ".BO_", "._5440_BO_"],
                     [""" 	pFieldFirst_Bi	:=	ADR(SEL_651R2_5442_DNP.BI_00000_Recloser_Status)	,
	pFieldFirst_Ai	:=	ADR(SEL_651R2_5442_DNP.AI_00000_IA)	,
	pFieldFirst_Bo	:=	ADR(SEL_651R2_5442_DNP.BO_00000_SS1)	,
	pFieldFirst_Ao	:=	0	,
	pFieldFirst_Cnt	:=	0	,
	pDeviceOffline	:=	ADR(SEL_651R2_5442_DNP_POU.Offline)	,
	pPoll	:=	ADR(SEL_651R2_5442_DNP_POU.Poll_Integrity_Obj_60_Cls_1230)	,
	pMessageReceivedCount	:=	ADR(SEL_651R2_5442_DNP_POU.Message_Received_Count)	);""", "SEL_651R2_5442_DNP", "SEL_651R2_5440_5442_DNP", ".BI_", "._5442_BI_", ".AI_", "._5442_AI_", ".BO_", "._5442_BO_"],
                     [""" 	pFieldFirst_Bi	:=	ADR(SEL_651R2_5454_DNP.BI_00000_Recloser_Status)	,
	pFieldFirst_Ai	:=	ADR(SEL_651R2_5454_DNP.AI_00000_IA)	,
	pFieldFirst_Bo	:=	ADR(SEL_651R2_5454_DNP.BO_00000_SS1)	,
	pFieldFirst_Ao	:=	0	,
	pFieldFirst_Cnt	:=	0	,
	pDeviceOffline	:=	ADR(SEL_651R2_5454_DNP_POU.Offline)	,
	pPoll	:=	ADR(SEL_651R2_5454_DNP_POU.Poll_Integrity_Obj_60_Cls_1230)	,
	pMessageReceivedCount	:=	ADR(SEL_651R2_5454_DNP_POU.Message_Received_Count)	);""", "SEL_651R2_5454_DNP", "SEL_651R2_5454_5456_DNP", ".BI_", "._5454_BI_", ".AI_", "._5454_AI_", ".BO_", "._5454_BO_" ],
                     [""" 	pFieldFirst_Bi	:=	ADR(SEL_651R2_5456_DNP.BI_00000_Recloser_Status)	,
	pFieldFirst_Ai	:=	ADR(SEL_651R2_5456_DNP.AI_00000_IA)	,
	pFieldFirst_Bo	:=	ADR(SEL_651R2_5456_DNP.BO_00000_SS1)	,
	pFieldFirst_Ao	:=	0	,
	pFieldFirst_Cnt	:=	0	,
	pDeviceOffline	:=	ADR(SEL_651R2_5456_DNP_POU.Offline)	,
	pPoll	:=	ADR(SEL_651R2_5456_DNP_POU.Poll_Integrity_Obj_60_Cls_1230)	,
	pMessageReceivedCount	:=	ADR(SEL_651R2_5456_DNP_POU.Message_Received_Count)	);""", "SEL_651R2_5456_DNP", "SEL_651R2_5454_5456_DNP", ".BI_", "._5456_BI_", ".AI_", "._5456_AI_", ".BO_", "._5456_BO_"],
                     [""" 	pFieldFirst_Bi	:=	ADR(SEL_651R2_5460_DNP.BI_00000_Recloser_Status)	,
	pFieldFirst_Ai	:=	ADR(SEL_651R2_5460_DNP.AI_00000_IA)	,
	pFieldFirst_Bo	:=	ADR(SEL_651R2_5460_DNP.BO_00000_SS1)	,
	pFieldFirst_Ao	:=	0	,
	pFieldFirst_Cnt	:=	0	,
	pDeviceOffline	:=	ADR(SEL_651R2_5460_DNP_POU.Offline)	,
	pPoll	:=	ADR(SEL_651R2_5460_DNP_POU.Poll_Integrity_Obj_60_Cls_1230)	,
	pMessageReceivedCount	:=	ADR(SEL_651R2_5460_DNP_POU.Message_Received_Count)	);""", "SEL_651R2_5460_DNP", "SEL_651R2_5405_5460_DNP", ".BI_", "._5460_BI_", ".AI_", "._5460_AI_", ".BO_", "._5460_BO_" ],
                     [""" 	pFieldFirst_Bi	:=	ADR(SEL_651R2_5506_DNP.BI_00000_Recloser_Status)	,
	pFieldFirst_Ai	:=	ADR(SEL_651R2_5506_DNP.AI_00000_IA)	,
	pFieldFirst_Bo	:=	ADR(SEL_651R2_5506_DNP.BO_00000_SS1)	,
	pFieldFirst_Ao	:=	0	,
	pFieldFirst_Cnt	:=	0	,
	pDeviceOffline	:=	ADR(SEL_651R2_5506_DNP_POU.Offline)	,
	pPoll	:=	ADR(SEL_651R2_5506_DNP_POU.Poll_Integrity_Obj_60_Cls_1230)	,
	pMessageReceivedCount	:=	ADR(SEL_651R2_5506_DNP_POU.Message_Received_Count)	);""", "SEL_651R2_5506_DNP", "SEL_651R2_5506_5508_DNP", ".BI_", "._5506_BI_", ".AI_", "._5506_AI_", ".BO_", "._5506_BO_" ],
                     [""" 	pFieldFirst_Bi	:=	ADR(SEL_651R2_5508_DNP.BI_00000_Recloser_Status)	,
	pFieldFirst_Ai	:=	ADR(SEL_651R2_5508_DNP.AI_00000_IA)	,
	pFieldFirst_Bo	:=	ADR(SEL_651R2_5508_DNP.BO_00000_SS1)	,
	pFieldFirst_Ao	:=	0	,
	pFieldFirst_Cnt	:=	0	,
	pDeviceOffline	:=	ADR(SEL_651R2_5508_DNP_POU.Offline)	,
	pPoll	:=	ADR(SEL_651R2_5508_DNP_POU.Poll_Integrity_Obj_60_Cls_1230)	,
	pMessageReceivedCount	:=	ADR(SEL_651R2_5508_DNP_POU.Message_Received_Count)	);""", "SEL_651R2_5508_DNP", "SEL_651R2_5506_5508_DNP", ".BI_", "._5508_BI_", ".AI_", "._5508_AI_", ".BO_", "._5508_BO_" ],
                     [""" 	pFieldFirst_Bi	:=	ADR(SEL_651R2_5744_DNP.BI_00000_Recloser_Status)	,
	pFieldFirst_Ai	:=	ADR(SEL_651R2_5744_DNP.AI_00000_IA)	,
	pFieldFirst_Bo	:=	ADR(SEL_651R2_5744_DNP.BO_00000_SS1)	,
	pFieldFirst_Ao	:=	0	,
	pFieldFirst_Cnt	:=	0	,
	pDeviceOffline	:=	ADR(SEL_651R2_5744_DNP_POU.Offline)	,
	pPoll	:=	ADR(SEL_651R2_5744_DNP_POU.Poll_Integrity_Obj_60_Cls_1230)	,
	pMessageReceivedCount	:=	ADR(SEL_651R2_5744_DNP_POU.Message_Received_Count)	);""", "SEL_651R2_5744_DNP", "SEL_651R2_5744_5745_DNP", ".BI_", "._5744_BI_", ".AI_", "._5744_AI_", ".BO_", "._5744_BO_"],
                     [""" 	pFieldFirst_Bi	:=	ADR(SEL_651R2_5745_DNP.BI_00000_Recloser_Status)	,
	pFieldFirst_Ai	:=	ADR(SEL_651R2_5745_DNP.AI_00000_IA)	,
	pFieldFirst_Bo	:=	ADR(SEL_651R2_5745_DNP.BO_00000_SS1)	,
	pFieldFirst_Ao	:=	0	,
	pFieldFirst_Cnt	:=	0	,
	pDeviceOffline	:=	ADR(SEL_651R2_5745_DNP_POU.Offline)	,
	pPoll	:=	ADR(SEL_651R2_5745_DNP_POU.Poll_Integrity_Obj_60_Cls_1230)	,
	pMessageReceivedCount	:=	ADR(SEL_651R2_5745_DNP_POU.Message_Received_Count)	);""", "SEL_651R2_5745_DNP", "SEL_651R2_5744_5745_DNP", ".BI_", "._5745_BI_", ".AI_", "._5745_AI_", ".BO_", "._5745_BO_" ]]



l1 = len(list_strings)
print(l1)

for string in list_strings:
    new_string = replace_string([text for text in string] )
    print(new_string)
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')

    

