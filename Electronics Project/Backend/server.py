# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/control', methods=['POST'])
# def control():
#     # Get the JSON payload from the request
#     data = request.get_json()

#     if not data or 'command' not in data:
#         return jsonify({'error': 'Invalid request, command not found'}), 400

#     # Extract the command
#     command = data['command']
#     print(f"Received command: {command}")

#     # Add your robot control logic here
#     # Example: 
#     if command == 'forward':
#         print("Moving forward")
#     elif command == 'backward':
#         print("Moving backward")
#     elif command == 'left':
#         print("Turning left")
#     elif command == 'right':
#         print("Turning right")
#     elif command == 'stop':
#         print("Stopping")
#     else:
#         print(f"Unknown command: {command}")
#         return jsonify({'error': 'Unknown command'}), 400

#     # Respond with a success message
#     return jsonify({'message': f'Command {command} executed successfully'}), 200

# if __name__ == '__main__':
#     # Run the Flask server
#     app.run(host='0.0.0.0', port=5000, debug=True)



from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Define the paths
FRONTEND_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'frontend')
CSS_FOLDER = os.path.join(FRONTEND_FOLDER, 'css')
SCRIPT_FOLDER = os.path.join(FRONTEND_FOLDER, 'script')

@app.route('/')
def serve_index():
    # Serve the index.html file
    return send_from_directory(FRONTEND_FOLDER, 'index.html')

@app.route('/css/<path:filename>')
def serve_css(filename):
    # Serve CSS files
    return send_from_directory(CSS_FOLDER, filename)

@app.route('/script/<path:filename>')
def serve_js(filename):
    # Serve JS files
    return send_from_directory(SCRIPT_FOLDER, filename)

@app.route('/control', methods=['POST'])
def control():
    # Get the JSON payload from the request
    data = request.get_json()

    if not data or 'command' not in data:
        return jsonify({'error': 'Invalid request, command not found'}), 400

    # Extract the command
    command = data['command']
    print(f"Received command: {command}")

    # Add your robot control logic here
    if command == 'forward':
        print("Moving forward")
    elif command == 'backward':
        print("Moving backward")
    elif command == 'left':
        print("Turning left")
    elif command == 'right':
        print("Turning right")
    elif command == 'stop':
        print("Stopping")
    else:
        print(f"Unknown command: {command}")
        return jsonify({'error': 'Unknown command'}), 400

    # Respond with a success message
    return jsonify({'message': f'Command {command} executed successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
