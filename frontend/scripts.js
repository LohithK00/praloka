
const BASE_URL = 'https://praloka-backend.onrender.com';

document.getElementById("signupForm")?.addEventListener("submit", async function(event) {
  event.preventDefault();
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    const res = await fetch(`${BASE_URL}/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email, password })
    });
    const data = await res.json();
    alert(data.message || data.error);
  } catch (error) {
    alert("Signup failed");
  }
});

document.getElementById("loginForm")?.addEventListener("submit", async function(event) {
  event.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    const res = await fetch(`${BASE_URL}/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });
    const data = await res.json();
    if (data.token) {
      alert("Login successful!");
      localStorage.setItem("token", data.token);
    } else {
      alert(data.error);
    }
  } catch (error) {
    alert("Login failed");
  }
});
