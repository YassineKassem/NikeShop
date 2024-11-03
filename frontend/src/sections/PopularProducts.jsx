import React, { useState, useEffect } from 'react';
import { PopularProductCard } from "../components";  // Import the product card component
import { fetchProducts, deleteProductById } from '../services/api';  // Import the fetch and delete services
import AddProductForm from '../components/AddProductForm';  // Import the AddProductForm

const PopularProducts = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        async function loadProducts() {
            try {
                const data = await fetchProducts();
                setProducts(data);
            } catch (error) {
                console.error('Error loading products:', error);
            }
        }
        loadProducts();
    }, []);

    const handleProductAdded = (newProduct) => {
        setProducts((prevProducts) => [...prevProducts, newProduct]);
    };

    const handleProductDelete = async (productId) => {
        try {
            await deleteProductById(productId);
            setProducts((prevProducts) => prevProducts.filter(product => product.id !== productId));
        } catch (error) {
            console.error('Error deleting product:', error);
        }
    };

    return (
        <div>
            <section id="products" className="max-container max-sm:mt-12">
                <div className="flex flex-col justify-start gap-5">
                    <h2 className="text-4xl font-palanquin font-bold">
                        Our <span className="text-coral-red"> Popular </span> Products
                    </h2>
                    <p className="lg:max-w-lg mt-2 font-montserrat text-slate-gray">
                        Experience top-notch quality and style with our sought-after selections.
                        Discover a world of comfort, design, and value.
                    </p>
                </div>

                <div className="mt-16 grid lg:grid-cols-4 md:grid-cols-3 sm:grid-cols-2 grid-cols-1 sm:gap-6 gap-14">
                    {products.length > 0 ? (
                        products.map((product) => (
                            <PopularProductCard
                                key={product.id}  // Ensure 'id' is unique
                                name={product.nom}
                                imgURL={product.image}
                                description={product.description}
                                stock={product.stock}
                                onDelete={() => handleProductDelete(product.id)}  // Replace with actual delete function
                                />
                        ))
                    ) : (
                        <p>Loading products...</p>
                    )}
                </div>
            </section>

            <section className="add-product-form">
                <h3>Add a New Product</h3>
                <AddProductForm onProductAdded={handleProductAdded} />
            </section>
        </div>
    );
};

export default PopularProducts;
