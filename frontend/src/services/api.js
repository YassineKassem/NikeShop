import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/produits/';  // FastAPI backend URL

// Function to fetch products
export const fetchProducts = async () => {
    try {
        const response = await axios.get(API_URL);
        return response.data;
    } catch (error) {
        console.error('Error fetching products:', error);
        throw error;
    }
};

// Function to add a product to the backend
export const addProduct = async (newProduct) => {
    try {
        // Ensure you're sending the data as JSON
        const response = await axios.post(API_URL, newProduct, {
            headers: {
                'Content-Type': 'application/json',  // Ensure correct header
            }
        });
        return response.data;  // Return the newly created product
    } catch (error) {
        console.error('Error adding product:', error);
        throw error;
    }
};
