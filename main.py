from flask import Flask
import clamav


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'
    # Example: Scan a file for viruses
    #result = clamav.scan_file('/path/to/file')
    # if result['infected']:
    #     return 'Virus detected!'
    # else:
    #     return 'File is clean.'

if __name__ == '__main__':
    app.run(debug=True)
