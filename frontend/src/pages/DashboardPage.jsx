import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";
import { getErrorMessage } from "../utils/errorHandler";

function DashboardPage() {
  const [user, setUser] = useState(null);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();
  const [products, setProducts] = useState([]);
  const [productData, setProductData] = useState({
    name: "",
    description: "",
    price: "",
  });
  const [editingProductId, setEditingProductId] = useState(null);

  useEffect(() => {
    fetchCurrentUser();
    fetchProducts();
  }, []);

  const fetchCurrentUser = async () => {
    try {
      const response = await api.get("/auth/me");

      setUser(response.data);
    } catch (error) {
      console.error(error);
      setError("Failed to load user");
    }
  };

  const fetchProducts = async () => {
    try {
      const response = await api.get("/products");

      setProducts(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleProductChange = (event) => {
    setProductData({
      ...productData,
      [event.target.name]: event.target.value,
    });
  };

  const handleCreateProduct = async (event) => {
    event.preventDefault();

    setMessage("");
    setError("");

    try {
      const payload = {
        ...productData,
        price: Number(productData.price),
      };

      if (editingProductId) {
        await api.put(`/products/${editingProductId}`, payload);
        setMessage("Product updated successfully");
      } else {
        await api.post("/products", payload);
        setMessage("Product created successfully");
      }

      resetProductForm();

      fetchProducts();
    } catch (error) {
      setError(getErrorMessage(error));
    }
  };

  const handleDeleteProduct = async (productId) => {
    setMessage("");
    setError("");

    try {
      await api.delete(`/products/${productId}`);
      setMessage("Product deleted successfully");

      fetchProducts();
    } catch (error) {
      setError(getErrorMessage(error));
    }
  };

  const resetProductForm = () => {
    setProductData({
      name: "",
      description: "",
      price: "",
    });

    setEditingProductId(null);

    setMessage("");
    setError("");
  };

  const handleLogout = () => {
    localStorage.removeItem("token");

    navigate("/");
  };

  return (
    <div className="dashboard-container">
      <h2>Dashboard</h2>

      {message && <p className="message success-message">{message}</p>}
      {error && <p className="message error-message">{error}</p>}

      {user && (
        <div className="dashboard-section">
          <p>Name: {user.name}</p>
          <p>Email: {user.email}</p>
          <p>Role: {user.role}</p>
        </div>
      )}

      <div className="dashboard-section">
        <h3>{editingProductId ? "Updating Product" : "Create Product"}</h3>

        <form className="dashboard-form" onSubmit={handleCreateProduct}>
          <div className="form-group">
            <label>Name</label>
            <br />
            <input
              type="text"
              name="name"
              value={productData.name}
              onChange={handleProductChange}
            />
          </div>

          <br />

          <div className="form-group">
            <label>Description</label>
            <br />
            <input
              type="text"
              name="description"
              value={productData.description}
              onChange={handleProductChange}
            />
          </div>

          <br />

          <div className="form-group">
            <label>Price</label>
            <br />
            <input
              type="number"
              name="price"
              value={productData.price}
              onChange={handleProductChange}
            />
          </div>
        
        

        <br />

        <div className="action-buttons">
          <button className="btn" type="submit">
            {editingProductId ? "Update Product" : "Create Product"}
          </button>

          <button type="button" className="btn" onClick={resetProductForm}>
            Reset
          </button>
        </div>
        </form>
      </div>

      <hr />

      <div className="dashboard-section">
        <h3>Products</h3>

        <ul>
          {products.map((product) => (
            <li key={product.id} className="product-item">
              <p>
                Name : <strong>{product.name}</strong>
              </p>
              <p>Description : {product.description}</p>
              <p>Price : ₹{product.price}</p>

              <div className="action-buttons">
                <button
                  className="action-button"
                  onClick={() => {
                    setEditingProductId(product.id);

                    setProductData({
                      name: product.name,
                      description: product.description,
                      price: product.price,
                    });
                  }}
                >
                  Edit
                </button>
                <> </>
                <button
                  className="action-button"
                  onClick={() => handleDeleteProduct(product.id)}
                >
                  Delete
                </button>
              </div>
            </li>
          ))}
        </ul>
      </div>

      <button className="logout-button" onClick={handleLogout}>
        Logout
      </button>
    </div>
  );
}

export default DashboardPage;
