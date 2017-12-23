Raiek
=====

**Raiek is an open source RaiBlocks wallet, designed to be fast and free of fees.**

-----

**How does a wallet works?**

There are few things that aren't that clear when you try to create your own wallet software. The most confusing is how a wallet is designed. 

First of all, we need to establish 6 main structures that are important to understand the real design of a wallet:

 1. WALLET
 2. SEED
 3. ACCOUNT NUMBER
 4. PRIVATE KEY
 5. PUBLIC KEY
 6. ACCOUNT SET

The WALLET is a *local*  storage of what I like to call ACCOUNT SET, an ACCOUNT SET contains the ACCOUNT NUMBER, the PRIVATE KEY and the PUBLIC KEY. Each account set is unique, it means that a ACCOUNT NUMBER is always together with its PRIVATE KEY and its PUBLIC KEY, and those can never be with another ACCOUNT NUMBER. This is guaranteed by a deterministic algorithm. 

The SEED generates deterministically a infinity number of ACCOUNT SETS, the SEED will always generate the same ACCOUNT SETS, it just depends on the index.

For instance, when you generate an ACCOUNT SET using your SEED with index 0, this will generate the ACCOUNT SET "x", when you generate a new one with the index 1, the ACCOUNT SET "y" is generated. If you generate again using index 0, the ACCOUNT SET "x" will reappear. So the SEED can be thought as a infinity list of ACCOUNT SETS.

Since the WALLET is a *local* storage of ACCOUNT SETS, when you generate a new ACCOUNT SET using your SEED, you must add this ACCOUNT SET to your local WALLET.

The ACCOUNT NUMBER is that "xrb_" address that we usually use to receive or transfer coins from a person to another, or between wallets. The ACCOUNT NUMBER pretty much makes a PUBLIC KEY sort of useless, so we don't need to worry about it.

Finally, the PRIVATE KEY is, just like in Bitcoin system, used to sign transactions. Also, when we have to add a ACCOUNT SET into a WALLET, we don't need to insert every piece of the ACCOUNT SET, we just need to insert the PRIVATE KEY. 

----

**Setting up:**

First of all, you must clone the project in your computer or server:

    $ git clone https://github.com/marcosmmb/Raiek.git
    $ cd Raiek

In order to use the API functions you must setup some configurations. Edit the /RaiekProject/config.ini file:

    [rai_node]
    uri = http://127.0.0.1:7076

The "uri" field is the default IP that you should change if you want to run it in a separated node or to connect to a third party node (the port 7076 is default for rai_node).

If you don't have a node yet, you can check how to setup your own node [here](https://github.com/clemahieu/raiblocks/wiki/Build-rai_node-samples) and launch it as a service [here](https://github.com/clemahieu/raiblocks/wiki/Running-rai_node-as-a-service).

To run the service locally, you must run the following command inside the main folder:

    $ cd RaiekProject && python3 api.py

----

**Python:**

The API is made using [python 3](https://www.python.org/) and [flask](http://flask.pocoo.org/),  so you must have both installed on your computer or in your web service server. Also, you have to install some python packages to run the code. The easiest way to do that is via [pip](https://pip.pypa.io/en/stable/) commands. 

These are the packages that you need to install before running the application:

    $ python3 -m pip install update
    $ python3 -m pip install requests configparser flask flask_restful flask_jsonpify

----

 **API:**

These are the endpoints and the keys that you must use in your POST request form: 

Note: the http://127.0.0.1:5000/ default url may be changed depending on where your node is running (this is default for a local node).

>  - http://127.0.0.1:5000/get_new_seed

*Used for generate a new seed, this is the only function that doesn't connect to the blockchain. Instead, it uses an algorithm to generate a 64 characters hexa string.* 

----

>  - http://127.0.0.1:5000/get_new_wallet

*Just like the /get_new_seed endpoint, this one generates a new wallet number to locally store account sets. This one connects to the blockchain though.*

----
 
>  - http://127.0.0.1:5000/get_new_account_set
> 	 - seed_value
> 	 - wallet_value
> 	 - index_value

*Using the seed and the index, it generates the account set and then stores it in the local wallet.*

----

>  - http://127.0.0.1:5000/get_new_account
> 	 - seed_value
> 	 - wallet_value
> 	 - index_value

*Similar to above, usually used to create a new account for a existing user, since it doesn't returns the seed nor the wallet number.*

----

>  - http://127.0.0.1:5000/set_account_in_wallet
> 	 - wallet_value
> 	 - private_value

*Locally stores an account set into a wallet.*s

----

>  - http://127.0.0.1:5000/set_receive_all_blocks
> 	 - wallet_value

*Usually used to receive every pending block. You must want to create a routine to use this one.*

----
 

> - http://127.0.0.1:5000/set_send_block
> 	 - wallet_value
> 	 - source_value
> 	 - destination_value
> 	 - amount_value

*Sets a send block.*

----

>  - http://127.0.0.1:5000/get_representative
> 	 - wallet_value

*Get the current representative of a wallet. Note that the representative is set per wallet, not per account. It means that the blockchain will count only the last defined representative of an account (through its wallet).*

----

>  - http://127.0.0.1:5000/set_representative
> 	 - wallet_value
> 	 - representative_value

*Sets a new representative to the wallet, every account in it will be affected.*

----

>  - http://127.0.0.1:5000/get_account_balance
> 	 - account_value

*Checks an account balance. Doesn't need any permission.*

----

>  - http://127.0.0.1:5000/get_mrai_from_raw
> 	 - amount_value

*Translates Mrai from raw.*

----

>  - http://127.0.0.1:5000/get_mrai_to_raw
> 	 - amount_value

*Translates Mrai to raw.*


----

>  - http://127.0.0.1:5000/get_krai_from_raw
> 	 - amount_value

*Translates Krai from raw.*

----

>  - http://127.0.0.1:5000/get_krai_to_raw
> 	 - amount_value

*Translates Krai to raw.*

----

>  - http://127.0.0.1:5000/get_rai_from_raw
> 	 - amount_value

*Translates Rai from raw.*

----

>  - http://127.0.0.1:5000/get_rai_to_raw
> 	 - amount_value

*Translates Rai to raw.*

 

