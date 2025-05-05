document.addEventListener('DOMContentLoaded', function () {
    const loginTab = document.getElementById('login-tab');
    const registerTab = document.getElementById('register-tab');
    const formContent = document.getElementById('form-content');

    // Render login form
    function renderLoginForm() {
        formContent.innerHTML = `
            <div class="form-body">
                <input id="username" type="text" placeholder="Username" class="input"/>
                <input id="password" type="password" placeholder="Password" class="input"/>
                <button id="login-btn" class="login-btn">LOGIN</button>
                <p id="login-status"></p>
            </div>
        `;
        attachLoginButton();
    }

    // Render register form
    function renderRegisterForm() {
        formContent.innerHTML = `
            <div class="form-body">
                <input id="username" type="text" placeholder="Username" class="input"/>
                <input id="email" type="email" placeholder="Email" class="input"/>
                <input id="password" type="password" placeholder="Password" class="input"/>
                <button id="register-btn" class="login-btn">REGISTER</button>
                <p id="login-status"></p>
            </div>
        `;
        attachRegisterButton();
    }

    // Attach login handler
    function attachLoginButton() {
        const loginBtn = document.getElementById("login-btn");
        if (!loginBtn) return;

        loginBtn.addEventListener("click", async function () {
            const username = document.getElementById("username").value.trim();
            const password = document.getElementById("password").value.trim();
            const loginStatus = document.getElementById("login-status");

            if (!username || !password) {
                loginStatus.textContent = "Please enter both username and password.";
                loginStatus.style.color = "red";
                return;
            }

            try {
                const response = await fetch("http://localhost:8000/auth/login", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ username, password })
                });

                const data = await response.json();

                if (response.ok) {
                    localStorage.setItem("token", data.access_token);
                    loginStatus.textContent = "Logged in!";
                    loginStatus.style.color = "green";
                    window.location.href = "watch.html";
                } else {
                    loginStatus.textContent = data.detail || "Login failed";
                    loginStatus.style.color = "red";
                }
            } catch (error) {
                console.error("Login error:", error);
                loginStatus.textContent = "Could not log in.";
                loginStatus.style.color = "red";
            }
        });
    }

    // Attach register handler
    function attachRegisterButton() {
        const registerBtn = document.getElementById("register-btn");
        if (!registerBtn) return;

        registerBtn.addEventListener("click", async function () {
            const username = document.getElementById("username").value.trim();
            const email = document.getElementById("email").value.trim();
            const password = document.getElementById("password").value.trim();
            const loginStatus = document.getElementById("login-status");

            if (!username || !email || !password) {
                loginStatus.textContent = "Please fill in all the fields.";
                loginStatus.style.color = "red";
                return;
            }

            try {
                const response = await fetch("http://localhost:8000/auth/register", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ username, email, password })
                });

                const data = await response.json();

                if (response.ok) {
                    loginStatus.textContent = "Registered successfully! Please log in.";
                    loginStatus.style.color = "green";
                } else {
                    loginStatus.textContent = data.detail || "Registration failed";
                    loginStatus.style.color = "red";
                }
            } catch (error) {
                console.error("Registration error:", error);
                loginStatus.textContent = "Could not register.";
                loginStatus.style.color = "red";
            }
        });
    }

    // Handle tab clicks
    loginTab.addEventListener('click', () => {
        loginTab.classList.add('active');
        registerTab.classList.remove('active');
        renderLoginForm();
    });

    registerTab.addEventListener('click', () => {
        registerTab.classList.add('active');
        loginTab.classList.remove('active');
        renderRegisterForm();
    });

    // Initial load: show login form
    renderLoginForm();
});
