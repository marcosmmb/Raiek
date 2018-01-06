import requests
import json
import random
from configparser import SafeConfigParser

MAX_INDEX = 18446744073709551615
MIN_INDEX = -18446744073709551615

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

    def validateAccountNumber(self, account):
        #Check whether account is a valid account number
        action = "validate_account_number"

        request = '''{ "action":"%s", "account":"%s" }''' % (action, account)

        return self.sendRpcRequest(request)
    #end validateAccountNumber

    def blockCount(self):
        #Reports the number of blocks in the ledger and unchecked synchronizing blocks
        action = "block_count"

        request = '''{ "action":"%s"}''' % (action)

        return self.sendRpcRequest(request)
    #end blockCount

    def walletBalances(self, wallet):
        #Returns how many rai is owned and how many have not yet been received by all accounts in wallet
        action = "wallet_balances"

        request = '''{ "action":"%s", "wallet":"%s" }''' % (action, wallet)

        return self.sendRpcRequest(request)
    #end walletBalances




class NodeParser:

    def returnMraiFromRaw(self, amount):
        if(not amount.isnumeric()):
            return {"message":"Amount must be numeric"}
        elif(int(amount) < 0):
            return {"message":"Amount mustn't be negative"}
        r = node.mraiFromRaw(amount)
        return {"result":r["amount"]}

    def returnMraiToRaw(self, amount):
        if(not amount.isnumeric()):
            return {"message":"Amount must be numeric"}
        elif(int(amount) < 0):
            return {"message":"Amount mustn't be negative"}
        r = node.mraiToRaw(amount)
        return {"result":r["amount"]}

    def returnKraiFromRaw(self, amount):
        if(not amount.isnumeric()):
            return {"message":"Amount must be numeric"}
        elif(int(amount) < 0):
            return {"message":"Amount mustn't be negative"}
        r = node.kraiFromRaw(amount)
        return {"result":r["amount"]}

    def returnKraiToRaw(self, amount):
        if(not amount.isnumeric()):
            return {"message":"Amount must be numeric"}
        elif(int(amount) < 0):
            return {"message":"Amount mustn't be negative"}
        r = node.kraiToRaw(amount)
        return {"result":r["amount"]}

    def returnRaiFromRaw(self, amount):
        if(not amount.isnumeric()):
            return {"message":"Amount must be numeric"}
        elif(int(amount) < 0):
            return {"message":"Amount mustn't be negative"}
        r = node.raiFromRaw(amount)
        return {"result":r["amount"]}

    def returnRaiToRaw(self, amount):
        if(not amount.isnumeric()):
            return {"message":"Amount must be numeric"}
        elif(int(amount) < 0):
            return {"message":"Amount mustn't be negative"}
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
        return {"seed":seed}

    def returnNewWallet(self):
        wallet = node.walletCreate()
        return wallet

    def createWalletSet(self, seed, wallet_number, index):
        #Creates a wallet set with 5 important tokens, must be saved
        #if(index.isnumeric() == False and index > MAX_INDEX):
    
        if(index.isnumeric() and int(index) > MAX_INDEX and int(index) < MIN_INDEX):
            return {"message":"The index is invalid"}

        try:
            dk = node.deterministicKey(seed, index)
            account = dk["account"]
        except:
            return {"message":"The seed is invalid"}

        private = dk["private"]
        public = dk["public"]
        account = dk["account"]
        
        try:
            r = self.insertAccountInWallet(wallet_number, private)
            key = r["key"]
        except:
            return {"message":"The wallet number is invalid"}
        
        wset = { "seed":seed, "wallet":wallet_number, "private":private, "public":public, "account":account }

        return wset
    #end createWalletSet

    def insertAccountInWallet(self, wallet, private):
        try:
            json = node.walletAdd(wallet, private)
            try:
                key = json["account"]
                if(private == "" or private.isnumeric()):
                    return {"message":"The private key is invalid"}
                else:
                    return {"key":key}
            except:
                key = json["error"]
                return {"message":"The wallet number is invalid"}
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

    def returnBlockCount(self):
        #Returns a tuple with blocks and pending blocks
        t = node.blockCount()
        count = t["count"]
        unchecked = t["unchecked"]
        return {"count":count, "unchecked":unchecked}
    #end returnBlockCount

    def returnWalletBalances(self, wallet):
        #Returns the wallet accounts balances
        r = node.walletBalances(wallet)
        try:
            balances = r["balances"]
            return r
        except:
            return {"message":"The wallet number is invalid"}
    #end returnWalletBalances

#------------------------------------------------------#

config_parser = SafeConfigParser()
config_files = config_parser.read('config.ini')
uri = config_parser.get("rai_node","uri")

node = RaiNode(uri)
node_parser = NodeParser()
