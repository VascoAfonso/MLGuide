import './MainContainer.css'
import Item from './Item.js'
import lazyLearning from '../images/LazyLearning.png';
import decisionTree from '../images/DecisionTree.png';
import regression from '../images/Regression.png';
import clustering from '../images/Clustering.png';
const MainContainer = () => {
    return (
        <div className="MainContainer">
            <div className="MainContainer-row">
                <Item text='Decision Tree' image={decisionTree} alt={'DecisionTree'} />
                <Item text='Bayesian Learning' />
                <Item text={'Lazy Learning'} image={lazyLearning} alt={'LazyLearning'} />
            </div>
            <div className="MainContainer-row">
                <Item text="Regression" image={regression} alt={'regression'} />
                <Item text='Perceptron' />
                <Item text='MultiLayer Perceptron' />
            </div>
            <div className="MainContainer-row">
                <Item text='Clustering' image={clustering} alt={'clustering'} />
            </div>
        </div>
    );
}
export default MainContainer;