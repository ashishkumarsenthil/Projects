def Caas(type):
    if type == "1":
        file.write("citm-ingress.citm_oam: bindaddress\n")
        file.write("citm-ingress.citm_app: bindaddress\n")
        file.write("citm-ingress.citm_db: bindaddress\n")
    elif type == "2":
        file.write("citm-ingress.citm_oam: metalLB IP\n")
        file.write("citm-ingress.citm_app: metalLB IP\n")
        file.write("citm-ingress.citm_db: metalLB IP\n")
    elif type == "3":
        file.write("POOL_IP_OAM\n")
        file.write("POOL_IP_APP\n")
        file.write("POOL_IP_DB\n")
    elif type == "4":
        file.write("SUBNET_IP_OAM\n")
        file.write("SUBNET_IP_APP\n")
        file.write("SUBNET_IP_DB\n")
    else:
        print("Invalid CaaS type")

def CKEY(type):
    file.write("global.userMgmt.deployckey\n")
    if type == "1":
        file.write("citm-ingress.citm_ckey: bindaddress\n")
    elif type == "2":
        file.write("citm-ingress.citm_ckey: metalLB IP\n")
    elif type == "3": 
        file.write("POOL_IP_CKEY\n")
    elif type == "4":
        file.write("SUBNET_IP\n")
    file.write("global:userMgmt.umBackup\n")
    # file.write("Avamar_Sensor\n")
    # file.write("Client_name\n")
    # file.write("enable_avamar\n")
    # file.write("Include_Namespace\n")  

def notmandatory(str1,str2):
    if (str1 == "primary CNF" and (str2 == "N" or str2 == "n")):
        #print("HealthCheckEnable is Enabled")
        file.write("multi-cnf.active_peer_vnf_sdl_instance\n")
        file.write("multi-cnf.ops_ha_vip\n")
        file.write("multi-cnf.primary_sdl_instance\n")
    elif str1 == "self signed secret creation":
        #print("self signed secret creation is Enabled")2
        file.write("logicalSDL: selfSignedCA.CA.crt\n")
        file.write("logicalSDL: selfSignedCA.CA.key\n")

def mandatory(str1):
    if str1 == "CaaS_Type":
        print("CaaS_Type is Enabled")
        #ls1=["NCS","NCP","TCP","AWS"]
        type1=input("Enter the type of CaaS (NCS-1/NCP-2/TCP-3/AWS-4): ")
        Caas(type1)
        if(type1=="2"):
            print("CBUR is Enabled")
            #ls2=["NCS","NCP"]
            type2=input("Enter if Journal/umBack is enabled? (y/n): ")
            if(type2=="y" or type2=="Y"):
                file.write("cburBackupConfig.cbur.avamar.server\n")
                file.write("cburBackupConfig.cbur.avamar.clientName\n")
                file.write("cburBackupConfig.cbur.clusterName\n")
                file.write("cburBackupConfig.cbur.avamar.enabled\n")
                file.write("cburBackupConfig.cbur.includeNamespaces\n")
        type3=input("Enter if CKEY is enabled? (y/n): ")
        if(type3=="y" or type3=="Y"):
            print("CKEY is Enabled")
            CKEY(type1)
            type4=input("Enter if Auto provisioning is enabled? (y/n): "  )
            if(type4=="y" or type4=="Y"):
                file.write("logicalSDL: passwdMgmt.autoProvision\n")
                file.write("logicalSDL: passwdMgmt.common_um_password\n")
            elif(type4=="n" or type4=="N"):
                file.write("Mannul provisiong to be done\n")
    elif str1 == "IPcreation & NAD creation":
        print("IPcreation & NAD creation is Enabled")
        #ls3=["IPv4","IPv6","DualStack"]
        type3=input("Enter the type of IP creation (IPv4-1/IPv6-2): ")
        if(type3=="1"):
            file.write("global.networks.ingressEndpoint.app.ipv4\n")
            file.write("global.networks.ingressEndpoint.oam.ipv4\n")
            file.write("global.networks.ingressEndpoint.db.ipv4\n")
            file.write("global.networks.ingressEndpoint.bnr.ipv4\n")
        elif(type3=="2"):
            file.write("global.networks.ingressEndpoint.db.ipv6\n")
            file.write("global.networks.ingressEndpoint.app.ipv6\n")
            file.write("global.networks.ingressEndpoint.oam.ipv6\n")
            file.write("global.networks.ingressEndpoint.bnr.ipv6\n")
            # file.write("CITM_IP_Family_IPv6\n")
            # file.write("Policy_single/dual\n")
        else:
            print("Invalid IP\n")
        multus=input("Enter if MultusEgress is Enabled? (y/n): ")
        if(multus=="y" or multus=="Y"):
            file.write("global.networks.whereaboutsMultusNetwork.ext_oam_network_nad(host_device,name,subnet,start,end,routes,gateway)\n")
            file.write("global.networks.whereaboutsMultusNetwork.ext_app_network_nad(host_device,name,subnet,start,end,routes,gateway)\n")
            file.write("global.networks.staticmultusnetworks.ext_app_network(host_device,name,subnet,start,end,routes)\n")
            file.write("global.networks.staticmultusnetworks.ext_db_network(host_device,name,subnet,start,end,routes)\n")
            file.write("global.networks.whereaboutsMultusNetwork.fp_network(host_device,name,subnet,start,end,routes,gateway)\n")
            
        elif(multus=="n" or multus=="N"):
            file.write("global.networks.staticmultusnetworks.ext_app_network(host_device,name,subnet,start,end,routes)\n")
            file.write("global.networks.staticmultusnetworks.ext_db_network(host_device,name,subnet,start,end,routes)\n")
            file.write("global.networks.whereaboutsMultusNetwork.fp_network(host_device,name,subnet,start,end,routes,gateway)\n")
            #file.write("FP_LAN\n")
    elif str1 == "OPT_pods/SYNC_pods/Both":
        type6=input("Enter which one is enabled? (OPT_pods-1/SYNC_pods-2/Both-3): ")
        if(type6=="1"):
            file.write("global.ntfdefault_kafka_releasename\n")
        elif(type6=="2"):
            file.write("global.ntfsync_kafka_releasename\n")
        elif(type6=="3"):
            file.write("global.ntfdefault_kafka_releasename\n")
            file.write("global.ntfsync_kafka_releasename\n") 
        type5=input("Enter if BQR are enabled? (y/n): ")
        if(type5=="y" or type5=="Y"):
            file.write("global.ntfbqr_kafka_releasename\n")
    else:
        print("Invalid parameter name")

with open("chartname_parametername_SDL.txt", "w") as file:
    print("you can let this machine know what parameters to be filled in the chartname_parametername.txt")
    #Common_Parameters
    file.write("global.registry\n")
    file.write("global.cnfName\n")
    file.write("global.hostnameprefix\n")
    file.write("global:userMgmt.keycloakPassword\n")
    file.write("global:userMgmt.keycloakIP\n")
    file.write("global.certMgmt.certFramework\n")
    file.write("CustomNodeSelectors.global_multus_nodeSelector (Key / value)\n")
    file.write("CustomNodeSelectors.global_nonmultus_nodeSelector (key / value)\n")
    file.write("customToleration.global_multus_toleration (key / value / match / action)\n")
    file.write("customToleration.global_nonmultus_toleration (key / value / match / action)\n")
    file.write("logicalSDL: config.multi-cnf\n")
    file.write("logicalSDL: config.storageClassRwx\n")
    file.write("logicalSDL: config.storageClassRwo\n")
    file.write("logicalSDL: config.revenueAssurance\n")
    file.write("multi-cnf.localities\n")
    file.write("multi-cnf.localities\n")
    file.write("multi-cnf.sdl_instance\n")
    list1=["CaaS_Type","IPcreation & NAD creation","OPT_pods/SYNC_pods/Both"]
    for i in list1:
        mandatory(i)
    list2=["primary CNF","self signed secret creation"]
    for i in list2:
        print("Is ",i," Enabled? (y/n):", end="")
        str= input()
        if(str=="y" or str=="Y"):
            print(i," is Enabled")
            notmandatory(i,str)
        elif(str=="n" or str=="N"):
            if(i=="CNF"):
                notmandatory(i,str)
                continue
            print(i," is Disabled")
    print("ENDED.\n")