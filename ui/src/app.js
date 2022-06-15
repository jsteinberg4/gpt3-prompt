import React from 'react';

import GptForm, { Result } from './index.js';


class Page extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			lastResult: "",
		}
	}

	async handleSubmit(event) {
		event.preventDefault();
		console.log(event.target[0].value);

		await fetch(`http://localhost:5000/prompt?q=${event.target[0].value}`)
			.then(response => {
				const json = response.json();
				console.log(json);
				return json;
			}).then(json => {
				const choices = json.choices.map(choice => choice.text);
				console.log(choices);
				return choices;
			}).then(choiceText => {
				console.log("Updating state");
				console.log("State before:", this.state);
				this.setState({
					lastResult: choiceText,
				});

				console.log("Updated state:", this.state);
			}).catch(error => console.error(error));

	}

	renderResult() {
		console.log("Current state: ", this.state);
		return (
			<Result value={this.state.lastResult} />
		);
	}

	render() {
		return (
			<div className='GptApp'>
				<div className="container prompt">
					<GptForm handleSubmit={(e) => this.handleSubmit(e)} />
				</div>
				<div className="separator"><h1></h1></div>
				<div className="container result">
					{ this.renderResult() }
				</div>
			</div>
		);
	}
}

function App() {
	return <Page />
}

export default App;
