from flask import Flask, abort, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from rpc import NodeParser

class getNewSeed(Resource):
    def post(self):
        seed = parser.returnNewSeed()
        return jsonify(seed)

class getNewWallet(Resource):
    def post(self):
        wallet = parser.returnNewWallet()
        return jsonify(wallet)

class getNewAccountSet(Resource):
    def post(self):
        seed = request.form["seed_value"]
        wallet = request.form["wallet_value"]
        index = request.form["index_value"]
        accountSet = parser.createWalletSet(seed, wallet, index)
        return jsonify(accountSet)

class getNewAccount(Resource):
    def post(self):
        seed = request.form["seed_value"]
        wallet = request.form["wallet_value"]
        index = request.form["index_value"]
        newAccount = parser.createNewAccount(seed, wallet, index)
        return jsonify(newAccount)

class setAccountInWallet(Resource):
    def post(self):
        wallet = request.form["wallet_value"]
        private = request.form["private_value"]
        r = parser.insertAccountInWallet(wallet, private)
        return jsonify(r)

class setReceiveAllBlocks(Resource):
    def post(self):
        wallet = request.form["wallet_value"]
        r = parser.receiveAllXrb(wallet)
        return jsonify(r)

class setSendBlock(Resource):
    def post(self):
        wallet = request.form["wallet_value"]
        source = request.form["source_value"]
        destination = request.form["destination_value"]
        amount = request.form["amount_value"]
        log = parser.sendXrb(wallet, source, destination, amount)
        return jsonify(log)

class getRepresentative(Resource):
    def post(self):
        wallet = request.form["wallet_value"]
        r = parser.returnRepresentative(wallet)
        return jsonify(r)

class setRepresentative(Resource):
    def post(self):
        wallet = request.form["wallet_value"]
        representative = request.form["representative_value"]
        r = parser.changeRepresentative(wallet, representative)
        return jsonify(r)

class getAccountBalance(Resource):
    def post(self):
        account = request.form["account_value"]
        r = parser.returnAccountBalance(account)
        return jsonify(r)

class getMraiFromRaw(Resource):
    def post(self):
        amount = request.form["amount_value"]
        r = parser.returnMraiFromRaw(amount)
        return jsonify(r)

class getMraiToRaw(Resource):
    def post(self):
        amount = request.form["amount_value"]
        r = parser.returnMraiToRaw(amount)
        return jsonify(r)

class getKraiFromRaw(Resource):
    def post(self):
        amount = request.form["amount_value"]
        r = parser.returnKraiFromRaw(amount)
        return jsonify(r)

class getKraiToRaw(Resource):
    def post(self):
        amount = request.form["amount_value"]
        r = parser.returnKraiToRaw(amount)
        return jsonify(r)

class getRaiFromRaw(Resource):
    def post(self):
        amount = request.form["amount_value"]
        r = parser.returnRaiFromRaw(amount)
        return jsonify(r)

class getRaiToRaw(Resource):
    def post(self):
        amount = request.form["amount_value"]
        r = parser.returnRaiToRaw(amount)
        return jsonify(r)

#------------------------------------------------------#

app = Flask(__name__)
api = Api(app)

parser = NodeParser()

api.add_resource(getNewSeed, "/get_new_seed")
api.add_resource(getNewWallet, "/get_new_wallet")
api.add_resource(getNewAccountSet, "/get_new_account_set")
api.add_resource(getNewAccount, "/get_new_account")
api.add_resource(setAccountInWallet, "/set_account_in_wallet")
api.add_resource(setReceiveAllBlocks, "/set_receive_all_blocks")
api.add_resource(setSendBlock, "/set_send_block")
api.add_resource(getRepresentative, "/get_representative")
api.add_resource(setRepresentative, "/set_representative")
api.add_resource(getAccountBalance, "/get_account_balance")
api.add_resource(getMraiFromRaw, "/get_mrai_from_raw")
api.add_resource(getMraiToRaw, "/get_mrai_to_raw")
api.add_resource(getKraiFromRaw, "/get_krai_from_raw")
api.add_resource(getKraiToRaw, "/get_krai_to_raw")
api.add_resource(getRaiFromRaw, "/get_rai_from_raw")
api.add_resource(getRaiToRaw, "/get_rai_to_raw")

if __name__ == "__main__":
    app.run()
