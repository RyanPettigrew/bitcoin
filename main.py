import matplotlib.pyplot as plt

def process_data(filename):
    unique_addresses = {}
    
    with open(filename, 'r') as file:
        for line in file:
            data = line.split(" ")
            try:
                block_number, transaction_type, input_count, output_count = map(int, data[:4])

                for i in range(4 + input_count, 4 + input_count + output_count):
                    value = int(float(data[i]) * 100000000)
                    if value > 0:
                        address = data[i + output_count][-16:]
                        unique_addresses[address] = (block_number, value)

                for i in range(4, 4 + input_count):
                    address = data[i][-16:]
                    unique_addresses.pop(address, None)
            except ValueError as e:
                print(f"Error: {e} | Line: {line}")

    return unique_addresses


def create_line_chart(block_data):
    block_numbers = list(block_data.keys())
    transaction_counts = [block_data[block]['transaction_count'] for block in block_numbers]

    plt.figure(figsize=(10, 6))
    plt.plot(block_numbers, transaction_counts, marker='o')
    plt.xlabel('Block Number')
    plt.ylabel('Number of Transactions')
    plt.title('Bitcoin Transactions Over Time')
    plt.grid(True)
    plt.show()

def create_bar_chart(block_data):
    block_numbers = list(block_data.keys())
    total_transaction_values = [block_data[block]['total_transaction_value'] for block in block_numbers]

    plt.figure(figsize=(10, 6))
    plt.bar(block_numbers, total_transaction_values)
    plt.xlabel('Block Number')
    plt.ylabel('Total Transaction Value (in satoshis)')
    plt.title('Total Transaction Value for Each Block')
    plt.grid(axis='y')
    plt.show()

def main():
    filename = 'data_test'
    block_data = process_data(filename)
    
    create_line_chart(block_data)
    create_bar_chart(block_data)

if __name__ == "__main__":
    main()
