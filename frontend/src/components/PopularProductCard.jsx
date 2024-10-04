import { star } from "../assets/icons";  // Assuming you still need this icon

const PopularProductCard = ({ imgURL, name, description, stock }) => {
    return (
        <div className="flex flex-1 flex-col w-full max-sm:w-full">
            <img src={imgURL} alt={name} className="w-[282px] h-[282px]" />
            <div className="mt-8 flex justify-start gap-2.5">
                <img src={star} alt="rating icon" width={24} height={24} />
                <p className="font-montserrat text-xl leading-normal text-slate-gray">
                    (4.5)
                </p>
            </div>
            <h3 className="mt-2 text-2xl leading-normal font-semibold font-palanquin">
                {name}
            </h3>
            <p className="mt-2 font-montserrat text-slate-gray leading-normal">
                {description}
            </p>
            <p className="mt-2 font-montserrat text-slate-gray leading-normal">
                Stock: {stock > 0 ? stock : 'Out of stock'}
            </p>
            <p className="mt-2 font-semibold font-montserrat text-coral-red text-2xl leading-normal">
                $200.00  {/* You can update this with the actual price field if available */}
            </p>
        </div>
    );
};

export default PopularProductCard;
