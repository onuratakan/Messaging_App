from wallet.wallet import Wallet_Import

def messaging_app_main_tx(tx):
    tx_pubkey = tx.toUser
    tx_pubkey_fromUser = tx.fromUser
    my_pubkey = "".join([
            l.strip() for l in Wallet_Import(0,0).splitlines()
            if l and not l.startswith("-----")
        ])  
    
    print("\n")
    print("\n\n"+tx_pubkey)
    print(my_pubkey+"\n\n")
    print(tx_pubkey == my_pubkey or tx_pubkey in my_pubkey or my_pubkey in tx_pubkey)
    print(tx.__dict__)
    print(tx.data)
    print(type(tx.data))
    print("\n")

    control = False
    to_User = False
    from_User = False
    if tx_pubkey == my_pubkey or tx_pubkey in my_pubkey or my_pubkey in tx_pubkey:
        control = True
        to_User = True
    elif tx_pubkey_fromUser == my_pubkey or tx_pubkey_fromUser in my_pubkey or my_pubkey in tx_pubkey_fromUser:
        control = True
        from_User = True

    if control:
     if tx.data != None:
      print("\n not none \n")
      if "app" in tx.data:
        print("\n app in data \n")
        if tx.data["app"] == "messagingapp":
            print("""\n tx.data["app"] == "messagingapp" \n""")
            if tx.data["command"] == "addnewuser" and to_User:
                print("""\n tx.data["command"] == "addnewuser" \n""")
                from app.Messaging_App.func.create_new_user import create_new_user
                create_new_user("unknow", tx.fromUser, tx.data["n"],tx.data["e"])
            elif tx.data["command"] == "newmessage" and to_User:
                from app.Messaging_App.func.decrypt import decrypt_text
                decrypt_text(tx.data["message"],tx_pubkey_fromUser)




def messaging_app_main_run(port=79):

    from app.Messaging_App.web.chat import start_messaging_app
    start_messaging_app(port=port)

