<!DOCTYPE html>
<html>

<body>

  <h1>TextEncryptorDecryptor</h1>

  <p>TextEncryptorDecryptor is a Python-based application designed to encrypt and decrypt messages using multiple cipher algorithms. It offers several classical encryption techniques to securely transform sensitive information and allows users to choose between different encryption methods based on their needs.</p>

  <h2>Features</h2>
  <ul>
    <li>Supports multiple cipher algorithms: Caesar Cipher, Vigenère Cipher, Railfence Cipher, Playfair Cipher, Beaufort Cipher, and Autokey Cipher</li>
    <li>Provides encryption and decryption options for each cipher</li>
    <li>Encrypts and decrypts messages using user-defined secret keys</li>
    <li>Uses a simple and intuitive graphical user interface built with Tkinter</li>
    <li>Secret keys are displayed as asterisks for security (*****)</li>
  </ul>

  <h2>Getting Started</h2>

  <p>To get started with the EncryDecryApp, follow these steps:</p>
  <ol>
    <li>Clone the repository:</li>
  </ol>
  <pre><code>git clone https://github.com/your-username/EncryDecryApp.git</code></pre>

  <ol start="2">
    <li>Navigate to the project directory:</li>
  </ol>
  <pre><code>cd EncryDecryApp</code></pre>

  <ol start="3">
    <li>Create a virtual environment (optional but recommended):</li>
  </ol>
  <pre><code>python -m venv .venv</code></pre>

  <ol start="4">
    <li>Activate the virtual environment:</li>
  </ol>
  <pre><code>.venv\Scripts\activate  # On Windows</code></pre>
  <pre><code>source .venv/bin/activate  # On macOS/Linux</code></pre>

  <ol start="5">
    <li>Install the required dependencies:</li>
  </ol>
  <pre><code>pip install tkinter</code></pre>

  <ol start="6">
    <li>Run the EncryDecryApp script:</li>
  </ol>
  <pre><code>python main.py</code></pre>

  <h2>Usage</h2>
  <ol>
    <li>Run the EncryDecryApp script using <code>python main.py</code>.</li>
    <li>The app will open a graphical interface for encryption and decryption.</li>
    <li>Enter the message you want to encrypt or decrypt.</li>
    <li>Choose a cipher algorithm from the available options: Caesar, Vigenère, Railfence, Playfair, Beaufort, or Autokey.</li>
    <li>Enter a secret key (the key will be displayed as *****).</li>
    <li>Click on either "Encrypt" or "Decrypt" based on your need.</li>
    <li>The result will be displayed in a new window.</li>
  </ol>

  <h2>Contributing</h2>

  <p>Contributions are welcome! If you want to improve the code or add more features, follow these steps:</p>
  <ol>
    <li>Fork the repository.</li>
    <li>Create a new branch for your feature or fix.</li>
    <li>Make your changes and commit them.</li>
    <li>Push your branch to your forked repository.</li>
    <li>Submit a pull request with a detailed description of your changes.</li>
  </ol>

  <h2>Acknowledgments</h2>
  <ul>
    <li>Special thanks to the developers of the <a href="https://docs.python.org/3/library/tkinter.html">Tkinter</a> library for building the graphical user interface.</li>
    <li>Thank you to the cryptographic algorithm resources for providing clear descriptions of the cipher techniques used in this project.</li>
  </ul>

</body>

</html>
