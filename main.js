async function refresh() {
  const res = await fetch('/api/status');
  const j = await res.json();
  const a = j.angle ?? 90;
  document.getElementById('angle').value = a;
  document.getElementById('angleVal').textContent = a;
  document.getElementById('fanState').textContent = j.fan_on ? " (ON)" : " (OFF)";
}

document.getElementById('angle').addEventListener('input', (e) => {
  document.getElementById('angleVal').textContent = e.target.value;
});

document.getElementById('setBtn').addEventListener('click', async () => {
  const angle = parseFloat(document.getElementById('angle').value);
  const res = await fetch('/api/angle', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({angle})
  });
  if (!res.ok) {
    const j = await res.json();
    alert('Error: ' + (j.error || res.status));
  } else {
    alert('Angle set to ' + angle + '°');
  }
  refresh();
});

document.getElementById('stopBtn').addEventListener('click', async () => {
  alert('To release servo, call servo.off() in code or restart pigpiod without setting angle.');
});

document.getElementById('fanOn').addEventListener('click', async () => {
  await fetch('/api/fan', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({on: true})
  });
  refresh();
});

document.getElementById('fanOff').addEventListener('click', async () => {
  await fetch('/api/fan', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({on: false})
  });
  refresh();
});

refresh();
setInterval(refresh, 3000);

