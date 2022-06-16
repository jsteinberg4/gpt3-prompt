export function Result(props) {
	return (
		<div className="result">
			<div className="title">{"Result:\n"}</div>
			<div className="result-value">
				<p>{props.value}</p>
			</div>
		</div>
	);
}
