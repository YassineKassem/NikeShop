import React, { useState } from 'react';
import { addProduct } from '../services/api';  // Import the addProduct service

const AddProductForm = ({ onProductAdded }) => {
    const [newProduct, setNewProduct] = useState({
        nom: '',
        reference: '',
        description: '',
        image: '',
        stock: 0,
    });
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [error, setError] = useState(null);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setNewProduct({
            ...newProduct,
            [name]: name === 'stock' ? parseInt(value, 10) : value,  // Ensure stock is a number
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsSubmitting(true);
        setError(null);
    
        console.log("Product being sent:", newProduct);  // Log the product data to check its structure
    
        try {
            const addedProduct = await addProduct(newProduct);  // Call the addProduct service
            onProductAdded(addedProduct);  // Callback to update the product list in the parent component
            setNewProduct({ nom: '', reference: '', description: '', image: '', stock: 0 });  // Reset form
        } catch (error) {
            setError('Failed to add product. Please try again.');
            console.error('Error adding product:', error);
        } finally {
            setIsSubmitting(false);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="w-full max-w-lg mx-auto bg-white p-8 rounded-lg shadow-md">
            <h2 className="text-2xl font-bold text-center text-coral-red mb-6">Add New Product</h2>
            
            <div className="mb-4">
                <label className="block text-slate-gray text-sm font-bold mb-2" htmlFor="nom">
                    Product Name:
                </label>
                <input
                    type="text"
                    name="nom"
                    value={newProduct.nom}
                    onChange={handleChange}
                    className="w-full px-3 py-2 border rounded-lg text-slate-gray focus:outline-none focus:ring-2 focus:ring-coral-red"
                    placeholder="Enter product name"
                    required
                />
            </div>

            <div className="mb-4">
                <label className="block text-slate-gray text-sm font-bold mb-2" htmlFor="reference">
                    Reference:
                </label>
                <input
                    type="text"
                    name="reference"
                    value={newProduct.reference}
                    onChange={handleChange}
                    className="w-full px-3 py-2 border rounded-lg text-slate-gray focus:outline-none focus:ring-2 focus:ring-coral-red"
                    placeholder="Enter reference"
                    required
                />
            </div>

            <div className="mb-4">
                <label className="block text-slate-gray text-sm font-bold mb-2" htmlFor="description">
                    Description:
                </label>
                <textarea
                    name="description"
                    value={newProduct.description}
                    onChange={handleChange}
                    className="w-full px-3 py-2 border rounded-lg text-slate-gray focus:outline-none focus:ring-2 focus:ring-coral-red"
                    placeholder="Enter description"
                    required
                />
            </div>

            <div className="mb-4">
                <label className="block text-slate-gray text-sm font-bold mb-2" htmlFor="image">
                    Image URL:
                </label>
                <input
                    type="text"
                    name="image"
                    value={newProduct.image}
                    onChange={handleChange}
                    className="w-full px-3 py-2 border rounded-lg text-slate-gray focus:outline-none focus:ring-2 focus:ring-coral-red"
                    placeholder="Enter image URL"
                    required
                />
            </div>

            <div className="mb-4">
                <label className="block text-slate-gray text-sm font-bold mb-2" htmlFor="stock">
                    Stock:
                </label>
                <input
                    type="number"
                    name="stock"
                    value={newProduct.stock}
                    onChange={handleChange}
                    className="w-full px-3 py-2 border rounded-lg text-slate-gray focus:outline-none focus:ring-2 focus:ring-coral-red"
                    placeholder="Enter stock quantity"
                    required
                />
            </div>

            <button
                type="submit"
                disabled={isSubmitting}
                className="w-full bg-coral-red text-white font-bold py-2 px-4 rounded-lg hover:bg-red-500 transition-colors duration-300"
            >
                {isSubmitting ? 'Adding Product...' : 'Add Product'}
            </button>

            {error && <p className="text-red-500 mt-4">{error}</p>}
        </form>
    );
};

export default AddProductForm;
