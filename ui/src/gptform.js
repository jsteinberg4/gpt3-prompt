import React from 'react';

export default class GptForm extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			value: 'Hello, GPT-3!',
			isNew: true,
		};

		this.handleChange = this.handleChange.bind(this);
		this.handleSubmit = this.props.handleSubmit;
	}

	handleChange(event) {
		this.setState({
			value: event.target.value
		});
	}

	// Unclear if need the <label>
	render() {
		return(
			<form onSubmit={this.handleSubmit}>
				<label>
					<textarea type="text" value={this.state.value} 
						onChange={this.handleChange}
						onClick={() => {
							if (this.state.isNew) {
								this.setState({
									value: '',
									isNew: false,
								});
							}
						}}
					/>
				</label>
				<input type="submit" value="Submit" />
			</form>
		);
	}
}
