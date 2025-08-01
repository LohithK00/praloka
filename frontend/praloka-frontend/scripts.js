const BASE_URL = 'https://praloka-backend.onrender.com';

async function registerUser(event) {
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

    if (res.ok) window.location.href = "login.html";
  } catch (error) {
    alert("Error connecting to backend");
  }
}

async function loginUser(event) {
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
    alert("Error connecting to backend");
  }
}