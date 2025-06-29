def Caas(type):
    if type == "1":
        file.write("CitmInstance1: bindAddress\n")
        file.write("CitmInstance3: bindAddress\n")
        file.write("CitmInstance4: bindAddress\n")
        file.write("global: multus_nodeselector\n")
        file.write("global: nonmultus_nodeselector\n")
        file.write("global: multus_tolerations\n")
        file.write("global: nonmultus_tolerations\n")
    elif type == "2":
        file.write("CITM_Instance1_MetalLB_IP_citmSPML\n")
        file.write("CITM_Instance3_MetalLB_IP_citmBULK\n")
        file.write("CITM_Instance4_MetalLB_IP_citmService\n")
        file.write("global: nonmultus_nodeselector\n")
        file.write("global: nonmultus_tolerations\n")
    elif type == "3":
        file.write("POOL_IP_CITM1\n")
        file.write("POOL_IP_CITM3\n")
        file.write("POOL_IP_CITM4\n")
    elif type == "4":
        file.write("SUBNET_IP_CITM1\n")
        file.write("SUBNET_IP_CITM3\n")
        file.write("SUBNET_IP_CITM4\n")
    else:
        print("Invalid CaaS type")

def JSON(type):
    file.write("global: json_provisioning\n")
    if type == "1":
        file.write("CitmInstance2: bindAddress\n")
    elif type == "2":
        file.write("CITM_Instance2_MetalLB_IP_citmJSON\n")
    elif type == "3": 
        file.write("POOL_IP_CITM2\n")
    elif type == "4":
        file.write("SUBNET_IP_CITM2\n")

def notmandatory(str1):
    if str1 == "LI enabled":
        
        file.write("common: lienabled\n")
    elif str1 == "self signed secret creation":
        #print("self signed secret creation is Enabled")
        file.write("common: selfsigned_ca.crt\n")
        file.write("commoon: selfsigned_ca.ckey\n")
    else:
        print("Invalid parameter name")

def mandatory(str1):
    if str1 == "CaaS_Type":
        print("CaaS_Type is Enabled")
        #ls1=["NCS","NCP","TCP","AWS"]
        type1=input("Enter the type of CaaS (NCS-1/NCP-2/TCP-3/AWS-4): ")
        Caas(type1)
        print("Is JSON provisioning Enabled? (y/n):", end="")
        str= input()
        if(str=="y" or str=="Y"):
            print("JSON provisioning is Enabled")
            JSON(type1)
    elif str1 == "IPcreation & NAD creation":
        print("IPcreation & NAD creation is Enabled")
        #ls3=["IPv4","IPv6","DualStack"]
        type3=input("Enter the type of IP creation (IPv4-1/IPv6-2/DualStack-3): ")
        file.write("global.networks.networkType_APP:\n")
        file.write("global.networks.networkType_OAM\n")
        file.write("global.networks.networkType_PROV\n")
        multus=input("Enter if MultusEgress is Enabled? (y/n): ")
        if(multus=="y" or multus=="Y"):
            file.write("global.networks.whereaboutsMultusNetwork.ext_app_network_nad [Host_device / subnet / start / end / gateway / destination]\n")
            file.write("global.networks.whereaboutsMultusNetwork.ext_oam_network_nad [Host_device / subnet / start / end / gateway / destination]\n")
            file.write("global.networks.whereaboutsMultusNetwork.fp_network [Host_device / subnet / start / end / gateway / destination]\n")
            #file.write("M.APP_LAN\n")
        elif(multus=="n" or multus=="N"):
            file.write("global.networks.whereaboutsMultusNetwork.fp_network [Host_device / subnet / start / end / gateway / destination]\n")
    # elif str1 == "self signed secret creation":
    #     print("self signed secret creation is Enabled")
    #     file.write("CA.crt\n")
    #     file.write("CA.key\n")
    else:
        print("Invalid parameter name")

with open("chartname_parametername_pgw.txt", "w") as file:
    print("you can let this machine know what parameters to be filled in the chartname_parametername.txt")
    list1=["CaaS_Type","IPcreation & NAD creation"]
    file.write("bssc-ifd: citm_ckey_ip\n")
    file.write("bssc-ifd: logging_ip\n")
    file.write("global: confd_citm_ip\n")
    file.write("global: isMultusNadPrecreated\n")
    file.write("global: certFramework\n")
    file.write("global: cnfName\n")
    file.write("global: registry\n")
    file.write("global: storageClassRwo\n")
    file.write("global: storageClassRwx\n")
    file.write("common: hostnameprefix\n")
    file.write("common: colocated_SDLInstances\n")
    file.write("common: pgwadminuser\n")
    file.write("common: common_um_password\n")
    file.write("common: autoProvision\n")
    file.write("common: locality\n")
    file.write("common: pgw_instance\n")
    file.write("common: globalSettings_preferredSiteOrder\n")
    file.write("common: globalSettings_sdlDiscoveryIPs\n")
    file.write("common: globalSettings_enableSecurity\n")
    file.write("common: keycloakIp\n")
    for i in list1:
        mandatory(i)
    list2=["LI enabled","self signed secret creation"]
    for i in list2:
        print("Is ",i," Enabled? (y/n):", end="")
        str= input()
        if(str=="y" or str=="Y"):
            print(i," is Enabled")
            notmandatory(i)
        else:
            print(i," is Disabled")
    print("ENDED.\n")