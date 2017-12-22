import requests
import json
import random
from configparser import SafeConfigParser

class RaiNode():

    def __init__(self, uri):
        self.uri = uri

    def generateSeed(self):
        #Generates a seed randomly

        full_wallet_seed = hex(random.SystemRandom().getrandbits(256))
        wallet_seed = full_wallet_seed[2:].upper()

        return wallet_seed
    #end generateSeed

    def sendRpcRequest(self, data):
        #Sends off POST request to rai_node, returns dict result.
        
        response = requests.post(self.uri, data=data)
        if not response.ok:
            return None
        resp_dict = json.loads(response.text)
        return resp_dict
    #end sendRpcRequest

    def blockCount(self):
        #Reports the number of blocks in the ledger and unchecked synchronizing blocks
        action = "block_count"

        request = '''{ "action":"%s" }''' % (action)

        return self.sendRpcRequest(request)
    #end blockCount

    def deterministicKey(self, seed, index):
        #Derive deterministic keypair from seed based on index
        action = "deterministic_key"

        request = '''{ "action":"%s", "seed":"%s", "index":"%s" }''' % (action, seed, index)

        return self.sendRpcRequest(request)
    #end deterministicKey

    def walletCreate(self):
        #Creates a new random wallet id
        action = "wallet_create"

        request = '''{ "action":"%s" }''' % (action)

        return self.sendRpcRequest(request)
    #end walletCreate

    def walletAdd(self, wallet, key):
        #Add an adhoc private key key to wallet
        action = "wallet_add"

        request = '''{ "action":"%s", "wallet":"%s", "key":"%s" }''' % (action, wallet, key)

        return self.sendRpcRequest(request)
    #end walletAdd

    def walletBalances(self, wallet):
        #Returns how many rai is owned and how many have not yet been received by all accounts in wallet
        action = "wallet_balances"

        request = '''{ "action":"%s", "wallet":"%s" }''' % (action, wallet )

        return self.sendRpcRequest(request)
    #end walletBalances

    def accountList(self, wallet):
        #Lists all the accounts inside wallet
        action = "account_list"

        request = '''{ "action":"%s", "wallet":"%s" }''' % (action, wallet )

        return self.sendRpcRequest(request)
    #end accountList

    def accountGet(self, key):
        #Get account number for the public key
        action = "account_get"

        request = '''{ "action":"%s", "key":"%s" }''' % (action, key )

        return self.sendRpcRequest(request)
    #end accountGet

    def accountBalance(self, account):
        #Returns how many RAW is owned and how many have not yet been received by account
        action = "account_balance"

        request = '''{ "action":"%s", "account":"%s" }''' % (action, account )

        return self.sendRpcRequest(request)
    #end accountBalance

    def searchPending(self, wallet):
        #Tells the node to look for pending blocks for any account in wallet
        action = "search_pending"

        request = '''{ "action":"%s", "wallet":"%s" }''' % (action, wallet )

        return self.sendRpcRequest(request)
    #end searchPending

    def walletPending(self, wallet, count = 100):
        #Returns a list of block hashes which have not yet been received by accounts in this wallet
        action = "wallet_pending"

        request = '''{ "action":"%s", "wallet":"%s", "count":"%s" }''' % (action, wallet, count)

        return self.sendRpcRequest(request)
    #end walletPending

    def receive(self, wallet, account, block):
        #Receive pending block for account in wallet
        action = "receive"

        request = '''{ "action":"%s", "wallet":"%s", "account":"%s", "block":"%s" }''' % (action, wallet, account, block)

        return self.sendRpcRequest(request)
    #end receive

    def send(self, wallet, source, destination, amount):
        #Send amount from source in wallet to destination
        action = "send"

        request = '''{ "action":"%s", "wallet":"%s", "source":"%s", "destination":"%s", "amount":"%s" }''' % (action, wallet, source, destination, amount)

        return self.sendRpcRequest(request)
    #end receive

    def mraiFromRaw(self, amount):
        #Divide a raw amount down by the Mrai ratio.
        action = "mrai_from_raw"

        request = '''{ "action":"%s", "amount":"%s" }''' % (action, amount)

        return self.sendRpcRequest(request)
    #end mraiFromRaw

    def mraiToRaw(self, amount):
        #Multiply an Mrai amount by the Mrai ratio.
        action = "mrai_to_raw"

        request = '''{ "action":"%s", "amount":"%s" }''' % (action, amount)

        return self.sendRpcRequest(request)
    #end mraiToRaw

    def kraiFromRaw(self, amount):
        #Divide a raw amount down by the Krai ratio.
        action = "krai_from_raw"

        request = '''{ "action":"%s", "amount":"%s" }''' % (action, amount)

        return self.sendRpcRequest(request)
    #end kraiFromRaw

    def kraiToRaw(self, amount):
        #Multiply an Krai amount by the Krai ratio.
        action = "krai_to_raw"

        request = '''{ "action":"%s", "amount":"%s" }''' % (action, amount)

        return self.sendRpcRequest(request)
    #end kraiToRaw

    def raiFromRaw(self, amount):
        #Divide a raw amount down by the rai ratio.
        action = "rai_from_raw"

        request = '''{ "action":"%s", "amount":"%s" }''' % (action, amount)

        return self.sendRpcRequest(request)
    #end raiFromRaw

    def raiToRaw(self, amount):
        #Multiply an rai amount by the rai ratio.
        action = "rai_to_raw"

        request = '''{ "action":"%s", "amount":"%s" }''' % (action, amount)

        return self.sendRpcRequest(request)
    #end raiToRaw

    def walletRepresentative(self, wallet):
        #Returns the default representative for wallet
        action = "wallet_representative"

        request = '''{ "action":"%s", "wallet":"%s" }''' % (action, wallet)

        return self.sendRpcRequest(request)
    #end walletRepresentative

    def walletRepresentativeSet(self, wallet, representative):
        #Sets the default representative for wallet
        action = "wallet_representative_set"

        request = '''{ "action":"%s", "wallet":"%s", "representative":"%s" }''' % (action, wallet, representative)

        return self.sendRpcRequest(request)
    #end walletRepresentativeSet

    def history(self, hash, count = 1):
        #Reports send/receive information for a chain of blocks
        action = "history"

        request = '''{ "action":"%s", "hash":"%s", "count":"%s" }''' % (action, hash, count)

        return self.sendRpcRequest(request)
    #end history



class NodeParser:

    def returnMraiFromRaw(self, amount):
        if(not amount.isnumeric()):
            return {"message":"ERROR"}
        elif(int(amount) < 0):
            return {"message":"ERROR"}
        r = node.mraiFromRaw(amount)
        return {"result":r["amount"]}

    def returnMraiToRaw(self, amount):
        if(not amount.isnumeric()):
            return {"message":"ERROR"}
        elif(int(amount) < 0):
            return {"message":"ERROR"}
        r = node.mraiToRaw(amount)
        return {"result":r["amount"]}

    def returnKraiFromRaw(self, amount):
        if(not amount.isnumeric()):
            return {"message":"ERROR"}
        elif(int(amount) < 0):
            return {"message":"ERROR"}
        r = node.kraiFromRaw(amount)
        return {"result":r["amount"]}

    def returnKraiToRaw(self, amount):
        if(not amount.isnumeric()):
            return {"message":"ERROR"}
        elif(int(amount) < 0):
            return {"message":"ERROR"}
        r = node.kraiToRaw(amount)
        return {"result":r["amount"]}

    def returnRaiFromRaw(self, amount):
        if(not amount.isnumeric()):
            return {"message":"ERROR"}
        elif(int(amount) < 0):
            return {"message":"ERROR"}
        r = node.raiFromRaw(amount)
        return {"result":r["amount"]}

    def returnRaiToRaw(self, amount):
        if(not amount.isnumeric()):
            return {"message":"ERROR"}
        elif(int(amount) < 0):
            return {"message":"ERROR"}
        r = node.raiToRaw(amount)
        return {"result":r["amount"]}

    def returnAccountBalance(self, account):
        #Returns an account balance as a string
        balance = node.accountBalance(account)
        try:
            ab = str(node.raiFromRaw(balance["balance"])["amount"])
            ab = list(ab)
            if(len(ab) > 6):
                ab.insert(-6, ".")
            ab = "".join(ab)
            return {"balance":ab}
        except:
            return balance
    #end returnAccountBalance

    def returnNewSeed(self):
        seed = node.generateSeed()
        return seed

    def returnNewWallet(self):
        wallet = node.walletCreate()
        return wallet

    def createWalletSet(self, seed, wallet_number, index):
        #Creates a wallet set with 5 important tokens, must be saved
        try:
            dk = node.deterministicKey(seed, index)
            private = dk["private"]
            public = dk["public"]
            account = dk["account"]
            self.insertAccountInWallet(wallet_number, private)
        except:
            return {"message":"ERROR"}
        
        wset = { "seed":seed, "wallet":wallet_number, "private":private, "public":public, "account":account }

        return wset
    #end createWalletSet

    def insertAccountInWallet(self, wallet, private):
        try:
            json = node.walletAdd(wallet, private)
            try:
                key = json["account"]
                return {"message":"OK"}
            except:
                key = json["error"]
                return {"message":"ERROR"}
        except:
            return {"message":"ERROR"}

    def createNewAccount(self, seed, wallet, index):
        dk = node.deterministicKey(seed, index)

        try: 
            private = dk["private"]
            public = dk["public"]
            account = dk["account"]
            self.insertAccountInWallet(wallet, private)
        except:
            return dk

        wset = {"private":private, "public":public, "account":account }

        return wset
    #end createNewAccount

    def receiveAllXrb(self, wallet):
        #Routine to start a receive on every pending block, and returns a log with the received blocks
        node.searchPending(wallet)
        pending = node.walletPending(wallet)

        try:
            blocks = pending["blocks"]
        except:
            return pending

        log = {}

        for acc in blocks:
            log[acc] = []
            for b in blocks[acc]:
                node.receive(wallet,acc, b)
                log[acc].append( {"block":b, "amount":node_parser.checkBlockHistory(b)["history"][0]["amount"]} )

        return log
    #end receiveAllXrb

    def sendXrb(self, wallet, source, destination, amount):
        #Sends a value from a source to a destination, returns the block, the amount and the accounts as a log
        block = node.send(wallet, source, destination, amount)
        try: 
            block = block["block"]
            log = { "block":block, "amount":amount, "source":source, "destination":destination }
        except:
            log = block
        return log
    #end sendXrb

    def returnRepresentative(self, wallet):
        #Returns the representative account of a wallet
        return node.walletRepresentative(wallet)
    #end getRepresentative

    def changeRepresentative(self, wallet, representative):
        #Sets the presentative account of a wallet
        s = node.walletRepresentativeSet(wallet, representative)
        try:
            s = s["set"]
            rep = { "set":s, "representative":representative }
        except:
            rep = s
        return rep
    #end setRepresentative

    def checkBlockHistory(self, block):
        #Returns a block history
        return node.history(block)
    #end checkBlockHistory

#Testing
#------------------------------------------------------#

config_parser = SafeConfigParser()
config_files = config_parser.read('config.ini')
uri = config_parser.get("rai_node","uri")

node = RaiNode(uri)
node_parser = NodeParser()

#log = node_parser.returnAccountBalance("xrb_14tw7j4jj4t5kedatqh5z9k8wiu1tcsamagkqcjyboroa3wramipbphya5d4")

#log = node_parser.sendXrb("0C83BE48EA530E1E7823BEE419CA6A79DEC3F2AF636EFE483866D2CE9BF744AF", "xrb_3gaywkgws7n847h8k1413583jqhqsxdd94kowc646zhr5psqey44t3rsu6kq", "xrb_1k5a4p8xq4ohy1aobouaait5ztxy3i5whcd5g51kbuc7tpqd9jq1m3zkub8i", "100")

#log = node_parser.receiveAllXrb("0C83BE48EA530E1E7823BEE419CA6A79DEC3F2AF636EFE483866D2CE9BF744AF")

#log = node_parser.getRepresentative("0C83BE48EA530E1E7823BEE419CA6A79DEC3F2AF636EFE483866D2CE9BF744AF")

#log = node_parser.setRepresentative("0C83BE48EA530E1E7823BEE419CA6A79DEC3F2AF636EFE483866D2CE9BF744AF", "xrb_1hza3f7wiiqa7ig3jczyxj5yo86yegcmqk3criaz838j91sxcckpfhbhhra1")

#log = node_parser.checkBlockHistory("2730BDAFDE7276AA29425CD2D37717132A9C9C481EA2341E11144C7E392AB0EE")["history"][0]["amount"]

#log = node_parser.createNewAccount("D5042EABC1F8D3F084F2CCC0C5E1F221F875DB05E3267AF833C40BB13D4C0BE1", "0C83BE48EA530E1E7823BEE419CA6A79DEC3F2AF636EFE483866D2CE9BF744AF", 10)

#print(log)