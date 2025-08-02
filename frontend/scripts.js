
document.getElementById("send-otp").addEventListener("click", () => {
  const email = document.querySelector('input[name="email"]').value;
  fetch("https://praloka-backend.onrender.com/send-otp", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email }),
  })
    .then((res) => res.json())
    .then((data) => alert(data.message || data.error))
    .catch((err) => alert("Failed to send OTP"));
});

document.getElementById("signup-form").addEventListener("submit", function (e) {
  e.preventDefault();
  const formData = new FormData(this);
  const jsonData = {};
  formData.forEach((value, key) => {
    jsonData[key] = value;
  });

  fetch("https://praloka-backend.onrender.com/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(jsonData),
  })
    .then((res) => res.json())
    .then((data) => alert(data.message || data.error))
    .catch(() => alert("Something went wrong"));
});
