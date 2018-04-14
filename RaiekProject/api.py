from flask import Flask, abort, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from rpc import NodeParser


class restartDocker(Resource):
    def post(self):
        message = parser.restartDocker()
        return jsonify(message)

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
        abort_bool = False
        try:
            message = accountSet["message"]
            abort_bool = True
        except:
            return jsonify(accountSet)
        if(abort_bool):
            abort(400, message)

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
        abort_bool = False
        try:
            message = r["message"]
            abort_bool = True
        except:
            return jsonify(r)
        if(abort_bool):
            abort(400, message)

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
        abort_bool = False
        try:
            message = r["message"]
            abort_bool = True
        except:
            return jsonify(r)
        if(abort_bool):
            abort(400, message)

class getMraiToRaw(Resource):
    def post(self):
        amount = request.form["amount_value"]
        r = parser.returnMraiToRaw(amount)
        abort_bool = False
        try:
            message = r["message"]
            abort_bool = True
        except:
            return jsonify(r)
        if(abort_bool):
            abort(400, message)

class getKraiFromRaw(Resource):
    def post(self):
        amount = request.form["amount_value"]
        r = parser.returnKraiFromRaw(amount)
        abort_bool = False
        try:
            message = r["message"]
            abort_bool = True
        except:
            return jsonify(r)
        if(abort_bool):
            abort(400, message)

class getKraiToRaw(Resource):
    def post(self):
        amount = request.form["amount_value"]
        r = parser.returnKraiToRaw(amount)
        abort_bool = False
        try:
            message = r["message"]
            abort_bool = True
        except:
            return jsonify(r)
        if(abort_bool):
            abort(400, message)

class getRaiFromRaw(Resource):
    def post(self):
        amount = request.form["amount_value"]
        r = parser.returnRaiFromRaw(amount)
        abort_bool = False
        try:
            message = r["message"]
            abort_bool = True
        except:
            return jsonify(r)
        if(abort_bool):
            abort(400, message)

class getRaiToRaw(Resource):
    def post(self):
        amount = request.form["amount_value"]
        r = parser.returnRaiToRaw(amount)
        abort_bool = False
        try:
            message = r["message"]
            abort_bool = True
        except:
            return jsonify(r)
        if(abort_bool):
            abort(400, message)

class getBlockCount(Resource):
    def post(self):
        blocks = parser.returnBlockCount()
        return jsonify(blocks)

class getNodeVersion(Resource):
    def post(self):
        version = parser.returnNodeVersion()
        return jsonify(version)

class getWalletBalances(Resource):
    def post(self):
        wallet = request.form["wallet_value"]
        r = parser.returnWalletBalances(wallet)
        abort_bool = False
        try:
            message = r["message"]
            abort_bool = True
        except:
            return jsonify(r)
        if(abort_bool):
            abort(400, message)

class getAccountHistory(Resource):
    def post(self):
        account = request.form["account_value"]
        count = request.form["count_value"]
        r = parser.returnAccountHistory(account, count)
        abort_bool = False
        try:
            message = r["message"]
            abort_bool = True
        except:
            return jsonify(r)
        if(abort_bool):
            abort(400, message)

class getAccountInformation(Resource):
    def post(self):
        account = request.form["account_value"]
        r = parser.returnAccountInformation(account)
        abort_bool = False
        try:
            message = r["message"]
            abort_bool = True
        except:
            return jsonify(r)
        if(abort_bool):
            abort(400, message)

class getWorkGenerate(Resource):
    def post(self):
        _hash = request.form["hash_value"]
        r = parser.returnWorkGenerate(_hash)
        abort_bool = False
        try:
            message = r["message"]
            abort_bool = True
        except:
            return jsonify(r)
        if(abort_bool):
            abort(400, message)

class getWorkGenerateThreading(Resource):
    def post(self):
        _hash = request.form["hash_value"]
        r = parser.returnWorkGenerateThreading(_hash)
        abort_bool = False
        try:
            message = r["message"]
            abort_bool = True
        except:
            return jsonify(r)
        if(abort_bool):
            abort(400, message)

class getWorkValidate(Resource):
    def post(self):
        work = request.form["work_value"]
        _hash = request.form["hash_value"]
        r = parser.returnWorkValidate(work, _hash)
        abort_bool = False
        try:
            message = r["message"]
            abort_bool = True
        except:
            return jsonify(r)
        if(abort_bool):
            abort(400, message)

class setSendBlockWithWork(Resource):
    def post(self):
        wallet = request.form["wallet_value"]
        source = request.form["source_value"]
        destination = request.form["destination_value"]
        amount = request.form["amount_value"]
        work = request.form["work_value"]
        log = parser.sendXrbWithWork(wallet, source, destination, amount, work)
        return jsonify(log)

class getOnlineRepresentatives(Resource):
    def post(self):
        representatives = parser.returnsOnlineRepresentatives()
        return jsonify(representatives)
        

#------------------------------------------------------#

app = Flask(__name__)
api = Api(app)

parser = NodeParser()

api.add_resource(restartDocker, "/restart_docker")

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
api.add_resource(getBlockCount, "/get_block_count")
api.add_resource(getNodeVersion, "/get_node_version")
api.add_resource(getWalletBalances, "/get_wallet_balances")
api.add_resource(getAccountHistory, "/get_account_history")
api.add_resource(getAccountInformation, "/get_account_information")
api.add_resource(setSendBlockWithWork, "/set_send_block_with_work")
api.add_resource(getWorkGenerate, "/get_work_generate")
api.add_resource(getWorkGenerateThreading, "/get_work_generate_threading")
api.add_resource(getWorkValidate, "/get_work_validate")
api.add_resource(getOnlineRepresentatives, "/get_online_representatives")





if __name__ == "__main__":
    app.run()
