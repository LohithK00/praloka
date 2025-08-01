const sendOTP = async () => {
  const email = document.getElementById("email").value;
  if (!email) return alert("Please enter your email!");

  const response = await fetch("https://praloka-backend.onrender.com/send-otp", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email })
  });

  const result = await response.json();
  alert(result.message || result.error);
};

document.getElementById("signupForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const data = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    otp: document.getElementById("otp").value,
    password: document.getElementById("password").value,
    confirm_password: document.getElementById("confirm_password").value,
  };

  const response = await fetch("https://praloka-backend.onrender.com/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  alert(result.message || result.error);
});
