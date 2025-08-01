const BASE_URL = 'https://praloka-backend.onrender.com';

async function sendOTP() {
  const email = document.getElementById("email").value;
  if (!email) return alert("Please enter your email first.");
  const res = await fetch(`${BASE_URL}/send-otp`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email })
  });
  const data = await res.json();
  alert(data.message || data.error);
}

async function registerUser(event) {
  event.preventDefault();
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const otp = document.getElementById("otp").value;
  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("confirmPassword").value;

  if (password !== confirmPassword) {
    return alert("Passwords do not match");
  }

  const res = await fetch(`${BASE_URL}/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, email, otp, password })
  });
  const data = await res.json();
  alert(data.message || data.error);
}
