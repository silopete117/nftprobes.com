# NFTProbes
https://www.nftprobes.com/

Powered by code from the HonestNFT repository (https://github.com/Convex-Labs/honestnft-shenanigans).

## Table of Contents
  - [Motivation](#motivation)
  - [Process](#process)
  - [Installation](#installation)
  - [Simple Tutorial](#simple-tutorial)
  - [Video Tutorial](#video-tutorial)
  - [API Endpoints](#api-references)
  - [Contact / Social Media](#contact--social-media)
  - [Contributing](#contributing)
  - [Acknowledgements](#acknowledgements)

## Motivation
To create a website around the HonestNFT Repo displaying data analysis of NFT collections. More Coming Soon!

## Process

A. main.py:
  1. process_jobs_metadata()
    a. pull_metadata(): download collection metadata and generate initial JSON file with name, slug, address, upper_id, lower_id, max_supply.
  2. process_jobs_collection_data_new()
    a. pulls and uploads collection links.

## Installation

## Simple Tutorial

## Video Tutorial

## API Endpoints
Web3 Provider: https://www.alchemy.com/ (Recommended)

Basic IPFS Endpoints: https://ipfs.github.io/public-gateway-checker/
<details>
  <summary>Note</summary>
  
  When you click one the gateways, you might be redirected to a long URL. Please note that only the hostname + /ipfs/ part is necessary.  
  E.g.  
  
  ```
  Correct: gateway.ipfs.io/ipfs/  
  Wrong: gateway.ipfs.io/ipfs/bafybeifx7yeb55armcsxwwitkymga5xf53dxiarykms3ygqic223w5sk3m#x-ipfs-companion-no-redirect  
  ```
  
  </details>
Pinata IPFS Endpoints: https://www.pinata.cloud/ (IPFS_GATEWAY in pulling.py is 
set to a public endpoint; can pull faster w Pinata)

## Contact / Social Media
[@Silopete117](https://twitter.com/silopete117)

## Contributing

## Acknowledgements
Many thanks to the team at HonestNFT and ConvexLabs for opening up their code repository. Donate thru GitCoin Grants to see a more fair and open Web3.
https://gitcoin.co/grants/6137/honestnft-shenanigan-scanning-tools

The Etherscan team for providing the free API keys for:
* [ArbiScan](https://arbiscan.io/)
* [BscScan](https://www.bscscan.com/)
* [Etherscan](https://etherscan.io)
* [FtmScan](https://ftmscan.com/)
* [PolygonScan](https://polygonscan.com/)
* [SnowTrace](https://snowtrace.io/)
