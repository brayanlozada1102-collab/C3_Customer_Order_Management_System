# Sales Registration System

A Python-based command-line application designed to manage customer registrations, product inventory, and sales orders. This system provides a simple way to track daily income and generate consolidated sales reports.

## Features

- **Customer Management**: Register new customers with email validation (minimum 10 characters, requiring '@' and '.').
- **Product Management**: Add new products to the inventory with automated ID assignment.
- **Order Creation**: Process sales by linking registered customers with available products and specifying quantities.
- **Order Consultation**: View a detailed list of all current orders, including customer names and product details.
- **Financial Tracking**: 
  - View real-time daily income totals.
  - Generate a final consolidated report including total orders, total income, spending grouped by customer, and total units sold per product.

## Project Structure

The project is modularized into several Python files:

- `main.py`: The entry point of the application containing the main menu logic.
- `customer_registration.py`: Functions for validating and creating customer profiles.
- `products_register.py`: Logic for adding new items to the product database.
- `order_creation.py`: Handles the process of creating and saving new sales.
- `consult_order.py`: Contains functions to format and display order history.
- `dailyincome.py`: Calculates and displays the current total of sales.
- `final_report_generation.py`: Generates a comprehensive summary of all activities before closing.

## Requirements

- Python 3.x

## How to Run

1. Clone or download all the `.py` files into the same directory.
2. Open your terminal or command prompt.
3. Run the application using the following command:
   ```bash
   python main.py