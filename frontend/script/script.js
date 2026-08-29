// Fetch sensor data periodically
setInterval(() => {
    fetch('/sensor_data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('temperature').innerText = data.temperature;
            document.getElementById('gas').innerText = data.gas;
            document.getElementById('sound').innerText = data.sound;
        });
}, 1000);

// Send movement commands
function sendCommand(command) {
    fetch('/control', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ command: command })
    }).then(response => response.json())
      .then(data => console.log(data));
}
