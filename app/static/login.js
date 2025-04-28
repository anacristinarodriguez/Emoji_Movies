document.addEventListener('DOMContentLoaded', function(){


    document.getElementById("login-btn").addEventListener("click", async function () {
        const username = document.getElementById("username").value.trim();
        const password = document.getElementById("password").value.trim();
        const loginStatus = document.getElementById("login-status");

        if (!username || !password){
            loginStatus.textContent = "Please enter both username and password.";
            loginStatus.style.color="red";
            return;
        }

    try {
        const response = await fetch("http://localhost:8000/auth/login", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({username, password})
        });

        const data = await response.json();

        if (response.ok) {
            localStorage.setItem("token", data.access_token);
            loginStatus.textContent = "Logged in!";
            loginStatus.style.color = "green";
            window.location.href = "watch.html";
        } else {
            loginStatus.textContent = (data.detail || "Login failed");
            loginStatus.style.color = "red";
            }
        } catch (error) {
            console.error("Login error:", error);
            loginStatus.textContent = "Could not log in.";
            loginStatus.style.color = "red";
        }
    });

});