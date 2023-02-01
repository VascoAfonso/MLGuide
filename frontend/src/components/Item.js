//Item to select in Home
import './Item.css'
const Item = ({ text, image, value }) => {
    return (
        <button className='Item'>
            <img className="Item-img" src={image} alt={value} />
            <div className="Item-text">{text}</div>
        </button>
    );
}
export default Item;
