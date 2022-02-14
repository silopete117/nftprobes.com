import os

from dotenv import dotenv_values

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = dotenv_values(f"{ROOT_DIR}/.env")

ABI_ENDPOINT = "https://api.etherscan.io/api?module=contract&action=getabi&address="
ARBITRUM_ABI_ENDPOINT = (
    "https://api.arbiscan.io/api?module=contract&action=getabi&address="
)
AVALANCHE_ABI_ENDPOINT = (
    "https://api.snowtrace.io/api?module=contract&action=getabi&address="
)
FANTOM_ABI_ENDPOINT = (
    "https://api.ftmscan.com/api?module=contract&action=getabi&address="
)
OPTIMISM_ABI_ENDPOINT = (
    "https://api-optimistic.etherscan.io/api?module=contract&action=getabi&address="
)
POLYGON_ABI_ENDPOINT = (
    "https://api.polygonscan.com/api?module=contract&action=getabi&address="
)
ENDPOINT = config.get("web3_provider")
ARBITRUM_ENDPOINT = config.get("arbitrum_web3_provider")
AVALANCHE_ENDPOINT = config.get("avalanche_web3_provider")
FANTOM_ENDPOINT = config.get("fantom_web3_provider")
OPTIMISM_ENDPOINT = config.get("optimism_web3_provider")
POLYGON_ENDPOINT = config.get("polygon_web3_provider")
IMPLEMENTATION_SLOT = (
    "0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc"
)

# Data folders
ATTRIBUTES_FOLDER = f"{ROOT_DIR}/metadata/raw_attributes"
RARITY_FOLDER = f"{ROOT_DIR}/metadata/rarity_data"
MINTING_FOLDER = f"{ROOT_DIR}/minting_data"

# API keys
IPFS_GATEWAY = config.get("ipfs_gateway")
OPENSEA_API_KEY = config.get("opensea_api_key")
MORALIS_API_KEY = config.get("moralis_api_key")
