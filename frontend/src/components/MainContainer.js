import './MainContainer.css'
import Item from './Item.js'
const MainContainer = () => {
    return (
        <div className="MainContainer">
            <div className="MainContainer-row">
                <Item text='Decision Tree' />
                <Item text='Bayesian Learning' />
                <Item text={'Lazy Learning'} />
            </div>
            <div className="MainContainer-row">
                <Item text="Regression" />
                <Item text='Perceptron' />
                <Item text='MultiLayer Perceptron' />
            </div>
            <div className="MainContainer-row">
                <Item text='Clustering' />
            </div>
        </div>
    );
}
export default MainContainer;