import requests
import json

def fetch_blockchain_stats():
    url = "https://api.blockchain.info/stats"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
        return None

def main():
    blockchain_stats = fetch_blockchain_stats()

    if blockchain_stats:
        print("Blockchain Statistics:")
        print("Market Price (USD):", blockchain_stats["market_price_usd"])
        print("Hash Rate:", blockchain_stats["hash_rate"])
        print("Total Fees (BTC):", blockchain_stats["total_fees_btc"])
        print("Total BTC Mined:", blockchain_stats["n_btc_mined"])
        print("Total Transactions:", blockchain_stats["n_tx"])
        # Add more metrics as needed

if __name__ == "__main__":
    main()
