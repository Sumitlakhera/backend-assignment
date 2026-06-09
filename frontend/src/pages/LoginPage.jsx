import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";
import { getErrorMessage } from "../utils/errorHandler";
import { Link } from "react-router-dom";

function LoginPage() {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const navigate = useNavigate();

  const [error, setError] = useState("");

  const handleChange = (event) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value,
    });
  };

const handleSubmit = async (event) => {
  event.preventDefault();

  setError("");

  try {
    const formPayload = new URLSearchParams();

    formPayload.append(
      "username",
      formData.email
    );

    formPayload.append(
      "password",
      formData.password
    );

    const response = await api.post(
      "/auth/login",
      formPayload,
      {
        headers: {
          "Content-Type":
            "application/x-www-form-urlencoded",
        },
      }
    );

    localStorage.setItem(
      "token",
      response.data.access_token
    );

    navigate("/dashboard");
  } catch (error) {
    console.error(error);

setError(getErrorMessage(error));
  }
};

  return (
    <div>
      <h2>Login</h2>

      {error && <p>{error}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>Email</label>
          <br />
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
          />
        </div>

        <br />

        <div>
          <label>Password</label>
          <br />
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
          />
        </div>

        <br />

        <p>
  Don't have an account?{" "}
  <Link to="/register">
    Register
  </Link>
</p>

        <button type="submit">
          Login
        </button>
      </form>
    </div>
  );
}

export default LoginPage;