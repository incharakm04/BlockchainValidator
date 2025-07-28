# 🧱 Blockchain Simulator

A simple web-based blockchain simulator built with Flask (Python) and Bootstrap. This project demonstrates the core concepts of blockchain, including block creation, tampering, and validation, with an interactive UI.

## Features

- **Add Block:** Add new blocks with custom data to the blockchain.
- **Tamper Block:** Modify the data of any block to simulate tampering.
- **Validate Blockchain:** Check if the blockchain is valid or has been tampered with.
- **Visual Feedback:** Tampered blocks are highlighted for easy identification.
- **Responsive UI:** Clean and modern interface using Bootstrap.

## Project Structure

```
/blockchain_simulator
    /templates
     /index.html
    app.py
    README.md
```

- **/templates:** Contains HTML templates for rendering the web pages.
- **app.py:** The main Flask application file.
- **README.md:** This documentation file.

## Technologies Used

- **Flask:** A micro web framework for Python.
- **Bootstrap:** A front-end framework for developing responsive websites.
- **JavaScript:** A programming language for web development.
- **HTML/CSS:** Markup and style sheet languages for creating web pages.

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/blockchain-simulator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd blockchain-simulator
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- **Adding a Block:**
  1. Enter the data for the new block in the input field.
  2. Click the "Add Block" button.
  3. The new block will be added to the blockchain and displayed on the screen.

- **Tampering with a Block:**
  1. Click the "Tamper" button on any block.
  2. Modify the data in the block.
  3. Click the "Validate Blockchain" button to check the blockchain's integrity.

- **Validating the Blockchain:**
  1. Click the "Validate Blockchain" button.
  2. A message will be displayed indicating whether the blockchain is valid or has been tampered with.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes.
4. Commit your changes: `git commit -m 'Add new feature'`
5. Push to the branch: `git push origin feature-branch`
6. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need to understand blockchain technology better.
- Thanks to the Flask and Bootstrap communities for their excellent documentation and support.

---

**Note:** This is a simplified blockchain simulator for educational purposes. It does not represent a production-ready blockchain solution.


