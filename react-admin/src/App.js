import React, {Component} from 'react'

/*
应用的根组件
 */
export default class App extends Component {

    state = {
        count: 0
    }

    constructor(props) {
        super(props)


        this.numberRef = React.createRef()
    }

    increment = () => {
        const number = this.numberRef.current.value * 1
        this.setState(state => ({
            count: state.count + number
        }))
    }
    decrement = () => {
        const number = this.numberRef.current.value * 1
        this.setState(state => ({
            count: state.count - number
        }))
    }

    incrementIfOdd = () => {
        const number = this.numberRef.current.value * 1
        if (this.state.count % 2 === 1) {
            this.setState(state => ({
                count: state.count + number
            }))
        }

    }

    incrementAsync = () => {
        const number = this.numberRef.current.value * 1

        setTimeout(() => {
            this.setState(state => ({
                count: state.count + number
            }))
        }, 1000)

    }


    render() {
        const count = this.state.count
        return (
            <div>
                <p>click {count} times</p>
                <div>
                    <section ref={this.numberRef}>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                    </section>
                    <button onClick={this.increment}>+</button>
                    <button onClick={this.decrement}>-</button>
                    <button onClick={this.incrementIfOdd}>increment if odd</button>
                    <button onClick={this.incrementAsync}>increment</button>

                </div>
            </div>
        )
    }
}
