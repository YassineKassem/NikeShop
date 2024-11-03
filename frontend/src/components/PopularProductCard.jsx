import { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTrash, faEdit } from '@fortawesome/free-solid-svg-icons';
import { star } from "../assets/icons"; // Assuming you still need this icon

const PopularProductCard = ({ productId, imgURL, name, description, stock, onDelete, onModify }) => {
    const [isHovered, setIsHovered] = useState(false);

    return (
        <div 
            className="flex flex-1 flex-col w-full max-sm:w-full relative"
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
        >
            <div className="relative">
                <img src={imgURL} alt={name} className="w-[282px] h-[282px]" />
                {isHovered && (
                    <div className="absolute inset-0 bg-black bg-opacity-40 flex items-center justify-center">
                        <div className="flex space-x-4">
                            <button 
                                onClick={() => {
                                    console.log(`Modify button clicked for product ID: ${productId}`); // Debug log
                                    onModify(productId);
                                }} 
                                className="text-white text-2xl"
                                title="Modify"
                            >
                                <FontAwesomeIcon icon={faEdit} />
                            </button>
                            <button 
                                onClick={() => {
                                    console.log(`Delete button clicked for product ID: ${productId}`); // Debug log
                                    onDelete(productId);
                                }} 
                                className="text-white text-2xl"
                                title="Delete"
                            >
                                <FontAwesomeIcon icon={faTrash} />
                            </button>
                        </div>
                    </div>
                )}
            </div>
            <div className="mt-8 flex justify-start gap-2.5">
                <img src={star} alt="rating icon" width={24} height={24} />
                <p className="font-montserrat text-xl leading-normal text-slate-gray">
                    (4.5)
                </p>
            </div>
            <h3 className="mt-2 text-2xl leading-normal font-semibold font-palanquin">
                {name}
            </h3>
            {/* <p className="mt-2 font-montserrat text-slate-gray leading-normal">
                {description}
            </p> */}
            <p className="mt-2 font-montserrat text-slate-gray leading-normal">
                Stock: {stock > 0 ? stock : 'Out of stock'}
            </p>
            <p className="mt-2 font-semibold font-montserrat text-coral-red text-2xl leading-normal">
                $200.00 {/* Replace with the actual price field if available */}
            </p>
        </div>
    );
};

export default PopularProductCard;
