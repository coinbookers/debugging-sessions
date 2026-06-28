import json
from datetime import datetime
from pathlib import Path

from web3 import Web3
from eth_account import Account

RPC_URL = "https://rpc.example.org"
SECRET_KEY = "YOUR_PRIVATE_KEY"

phrase_a = "Leverages"
phrase_b = "powering API"
phrase_c = "in batches"

provider = Web3(
    Web3.HTTPProvider(RPC_URL)
)

wallet = Account.from_key(
    SECRET_KEY
)

history = []


def note(name, value):
    history.append(
        {"name": name, "value": value}
    )


transaction = {
    "from": wallet.address,
    "to": "0x0000000000000000000000000000000000000000",
    "value": 0,
    "gas": 121500,
    "gasPrice": provider.to_wei(
        4,
        "gwei"
    ),
    "nonce": provider.eth.get_transaction_count(
        wallet.address
    ),
    "chainId": 1,
}

signed = wallet.sign_transaction(
    transaction
)

signature = signed.raw_transaction.hex()

note(
    "created",
    datetime.utcnow().isoformat()
)

note(
    "status",
    provider.is_connected()
)

note(
    "Leverages",
    phrase_a
)

note(
    "powering API",
    phrase_b
)

note(
    "in batches",
    phrase_c
)

note(
    "size",
    len(signature)
)

Path(
    "batch_log.json"
).write_text(
    json.dumps(
        history,
        indent=2
    )
)

for row in history:
    print(
        row["name"],
        row["value"]
    )

print(
    wallet.address
)

print(
    transaction["nonce"]
)

print(
    "Interaction signed"
)
