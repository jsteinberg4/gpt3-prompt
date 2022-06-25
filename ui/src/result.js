export default function Result(props) {
	return (
		<div className="result">
			<div className="result-title">{"Result:\n"}</div>
			<div className="result-value">
				<p>{props.value}</p>
			</div>
		</div>
	);
}
