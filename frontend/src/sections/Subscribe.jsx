import { useState } from 'react';
import AddProductForm from "../components/AddProductForm"; // Import the AddProductForm

const Subscribe = () => {
  const [products, setProducts] = useState([]);

  // Callback function to handle product addition
  const handleProductAdded = (newProduct) => {
    setProducts([...products, newProduct]);  // Add the new product to the product list
  };

  return (
    <section
      id="contact-us"
      className="max-container flex justify-between items-center max-lg:flex-col gap-10"
    >
      {/* Header Section */}
      <h3 className="text-4xl leading-[68px] lg:max-w-md font-palanquin font-bold">
        Add a new 
        <span className="text-coral-red"> Product </span>
      </h3>
      
      {/* Section to Add a New Product */}
      <section className="add-product-form w-full">
        <AddProductForm onProductAdded={handleProductAdded} />  {/* Use AddProductForm component */}
      </section>
    </section>
  );
};

export default Subscribe;
