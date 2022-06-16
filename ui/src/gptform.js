import React from 'react';

export default class GptForm extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			value: 'Hello, GPT-3!',
			isNew: true,
		};

		this.handleChange = this.handleChange.bind(this);
	}

	handleChange(event) {
		this.setState({
			value: event.target.value
		});
	}

	render() {
		return(
			<form onSubmit={this.props.handleSubmit}>
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
