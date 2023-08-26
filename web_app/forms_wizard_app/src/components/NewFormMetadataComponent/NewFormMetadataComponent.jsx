import { useState } from "react";
export default function NewFormMetadataComponent({ handle }) {
    const [state, setState] = useState({
        name:'',
        description: '',
    });
    const handleSubmit = e => {
        e.preventDefault();
        handle(e.target);
    }
    const handleTextareaKeyDown = (event) => {
        if ((event.ctrlKey || event.metaKey) && event.key === 'Enter') {
            event.preventDefault(); // Prevents a new line in the textarea
            handleSubmit(event);
        }
    };
    const handleChange = e => {
        setState({ ...state, [e.target.name]: e.target.value });
    }
    return (
        <div className="d-flex justify-content-center align-items-center vh-100 bg-dark text-light">
            <div className="card text-center bg-secondary text-light">
                <div className="card-header">
                    <h3 className="card-title">New Form</h3>
                </div>
                <div className="card-body">
                    <form onSubmit={handleSubmit} onKeyDown={handleTextareaKeyDown}>
                        <div className="mb-3">
                            <label className="form-label">Name:</label>
                            <input autoComplete="off" placeholder="Name your form so it's easier to find later" type="text" name="name" className="form-control" value={state.name} onChange={handleChange} />
                        </div>
                        <div className="mb-3">
                            <label className="form-label">Description:</label>
                            <textarea autoComplete="off" placeholder="Describe the form in a few words" name="description" cols="30" rows="4" className="form-control" value={state.description} onChange={handleChange} ></textarea>
                        </div>
                        <div className="mb-3">
                            <input tabIndex={0} className="btn btn-success override-customs text-white" type="submit" value="Begin Creating" />
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );

}