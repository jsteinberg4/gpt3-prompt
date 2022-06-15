import React from 'react';
import ReactDOM from 'react-dom/client';

function Result(props) {
	return (
		<div className="result">
			<div className="title">{"Result:\n"}</div>
			<div className="result-value">{props.value}</div>
		</div>
	);
}

class GptForm extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			value: 'Hello, GPT-3!',
			isNew: true,
		};

		this.handleChange = this.handleChange.bind(this);
		// this.handleSubmit = this.handleSubmit.bind(this);
		this.handleSubmit = this.props.handleSubmit.bind(this);
	}

	handleChange(event) {
		this.setState({
			value: event.target.value
		});
	}

	/*handleSubmit(event) {
		alert('A prompt was submitted: ' + this.state.value);
		event.preventDefault();
	}*/

	render() {
		return(
			<form onSubmit={this.handleSubmit}>
				<label>
					{"Say something to GPT-3: "}
					<textarea type="text" value={this.state.value} 
						onChange={this.handleChange}
						onClick={() => {
							if (this.state.isNew) {
								this.state.value = '';
								this.setState({isNew: false});
							}
						}}
					/>
				</label>
				<input type="submit" value="Submit" />
			</form>
		);
	}
}

class Page extends React.Component {

	constructor(props) {
		super(props);
		this.state = {
			lastResult: "",
		};
	}

	async handleSubmit(event) {
		event.preventDefault();
		console.log(event.target[0].value);
		fetch("http://localhost:5000/post/" + event.target[0].value)
			.then(response => {
				console.log(response.json());
			});

		/* this.setState({
			lastResult: value,
		}); */
	};

	render() {
		return (
				<div className="page">
					<GptForm handleSubmit={this.handleSubmit}/>
					<div><h1></h1></div>
					<Result value={this.state.lastResult}/>
				</div>
		)
	}
}

// ====================
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Page />)
