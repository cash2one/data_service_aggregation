

def statistic_data_service(userdatas):
    userdatas.wait_approve_counts = 0
    userdatas.approving_counts = 0
    userdatas.approved_counts = 0
    for userdata in userdatas :
        if userdata.status == 0 :
            userdatas.wait_approve_counts += 1 
        elif userdata.status == 1 :
            userdatas.approving_counts += 1 
        elif userdata.status == 2 :
            userdatas.approved_counts += 1 
        else :
            continue