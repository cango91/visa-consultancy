import { useContext } from "react"
import { Button, Modal } from 'react-bootstrap';
import { FormWizardContext } from '../../App'

export default function TopBarComponent() {
    const { state, dispatch } = useContext(FormWizardContext);
    return (
        <>
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container-fluid">
                    <button className="navbar-toggler" type="button">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse">
                        {state.isEditing ? (
                            <>
                                <button className="btn btn-primary me-2" onClick={() => dispatch({ type: 'LOAD_FORM' })}>Load</button>
                                <button className="btn btn-success btn-success me-2" onClick={() => { /* Save logic here */ }}>Save</button>
                                <button className="btn btn-danger" onClick={() => dispatch({ type: 'NEW_FORM' })}>New Form</button>
                            </>
                        ) : (
                            <>
                                <button className="btn btn-primary me-2" onClick={() => dispatch({ type: 'NEW_FORM' })}>New Form</button>
                                <button className="btn btn-success me-2" onClick={() => dispatch({ type: 'LOAD_FORM' })}>Load Form</button>
                            </>
                        )}
                    </div>
                </div>
            </nav>

            <Modal show={state.showChangesPopup} onHide={() => {dispatch({type: 'CANCEL_ACTION'}) }} className="bg-dark border border-5 border-warning">
                <Modal.Header className="bg-dark border border-white">
                    <Modal.Title>Unsaved Changes</Modal.Title>
                </Modal.Header>
                <Modal.Body className="bg-dark border border-white">
                    <p>You have unsaved changes. What would you like to do?</p>
                </Modal.Body>
                <Modal.Footer className="bg-dark border border-white">
                    <Button variant="success" className="button" onClick={() => dispatch({ type: 'SAVE_CHANGES' })}>Save</Button>
                    <Button variant="danger" className="button" onClick={() => dispatch({ type: 'DISCARD_CHANGES' })}>Discard</Button>
                    <Button variant="secondary" className="button" onClick={()=>dispatch({type: 'CANCEL_ACTION'})}>Cancel</Button>
                </Modal.Footer>
            </Modal>

        </>
    );
}