import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/produits';
//const API_URL = import.meta.env.VITE_API_URL;

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

// Function to delete a product by ID
export const deleteProductById = async (productId) => {
    try {
        await axios.delete(`${API_URL}/${productId}`);
    } catch (error) {
        console.error('Error deleting product:', error);
        throw error;
    }
};

export const updateProduct = async (productId, updatedProduct) => {
    try {
        const response = await axios.put(`${API_URL}/${productId}`, updatedProduct);
        return response.data;
    } catch (error) {
        console.error('Error updating product:', error);
        throw error;
    }
};