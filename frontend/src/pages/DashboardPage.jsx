import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function DashboardPage() {
  const [user, setUser] = useState(null);
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

    try {
      const payload = {
        ...productData,
        price: Number(productData.price),
      };

      if (editingProductId) {
        await api.put(`/products/${editingProductId}`, payload);
      } else {
        await api.post("/products", payload);
      }

      setProductData({
        name: "",
        description: "",
        price: "",
      });

      setEditingProductId(null);

      fetchProducts();
    } catch (error) {
      console.error(error);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("token");

    navigate("/");
  };

  return (
    <div>
      <h2>Dashboard</h2>

      {error && <p>{error}</p>}

      {user && (
        <div>
          <p>Name: {user.name}</p>
          <p>Email: {user.email}</p>
          <p>Role: {user.role}</p>
        </div>
      )}

      <h3>{editingProductId ? "Updating Product" : "Create Product"}</h3>

      <form onSubmit={handleCreateProduct}>
        <div>
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

        <div>
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

        <div>
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

        <button type="submit">
          {editingProductId ? "Update Product" : "Create Product"}
        </button>
      </form>

      <hr />

      <h3>Products</h3>

      <ul>
        {products.map((product) => (
          <li key={product.id}>
            <p>
              Name : <strong>{product.name}</strong>
            </p>
            <p>Description : {product.description}</p>
            <p>Price : ₹{product.price}</p>

            <button
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
          </li>
        ))}
      </ul>

      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}

export default DashboardPage;
