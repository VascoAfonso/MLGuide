import './MainContainer.css'
import Item from './Item.js'
const MainContainer = () => {
    return (
        <div className='MainContainer'>
            <Item text='Decision Tree'/>
            <Item text='Bayesian Learning'/>
            <Item text='Lazy Learning'/>
            <Item text='Regression'/>
            <Item text='Perceptron'/>
            <Item text='MultiLayer Perceptron'/>
            <Item text='Clustering'/>
        </div>
    );
} 
export default MainContainer;