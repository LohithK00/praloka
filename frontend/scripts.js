const BASE_URL = 'https://praloka-backend.onrender.com'; // Change to your Render backend later

async function sendOTP() {
  const email = document.getElementById('email').value;
  const res = await fetch(`${BASE_URL}/send-otp`, {
    method: "POST",
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email })
  });

  const data = await res.json();
  alert(data.message || data.error);
}

document.getElementById("signupForm").addEventListener("submit", async function(event) {
  event.preventDefault();

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const otp = document.getElementById("otp").value;
  const password = document.getElementById("password").value;
  const confirm_password = document.getElementById("confirm_password").value;

  const res = await fetch(`${BASE_URL}/register`, {
    method: "POST",
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, email, otp, password, confirm_password })
  });

  const data = await res.json();
  alert(data.message || data.error);
});
