import { useContext } from "react"
import { Button, Modal } from 'react-bootstrap';
import { FormWizardContext } from '../../App'

export default function TopBarComponent() {
    const { state, dispatch } = useContext(FormWizardContext);
    return (
        <>
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container-fluid flex-row-reverse justify-content-center">
                    <div className="d-flex">
                        {state.isEditing ? (
                            <>
                                <button className="btn btn-primary me-2" onClick={() => dispatch({ type: 'NEW_FORM' })}>New</button>
                                <button className="btn btn-warning me-2" onClick={() => dispatch({ type: 'LOAD_FORM' })}>Load</button>
                                <button className="btn btn-success me-2" onClick={() => dispatch({ type: 'SAVE_FORM' })}>Save</button>
                            </>
                        ) : (
                            <>
                                <button className="btn btn-primary me-2" onClick={() => dispatch({ type: 'NEW_FORM' })}>New Form</button>
                                <button className="btn btn-warning me-2" onClick={() => dispatch({ type: 'LOAD_FORM' })}>Load Form</button>
                            </>
                        )}
                    </div>
                </div>
            </nav>

            <Modal show={state.showChangesPopup} onHide={() => { dispatch({ type: 'CANCEL_ACTION' }) }} className="bg-dark border border-5 border-warning">
                <Modal.Header className="bg-dark border border-white">
                    <Modal.Title>Unsaved Changes</Modal.Title>
                </Modal.Header>
                <Modal.Body className="bg-dark border border-white">
                    <p>You have unsaved changes. What would you like to do?</p>
                </Modal.Body>
                <Modal.Footer className="bg-dark border border-white">
                    <Button variant="success" className="button" onClick={() => dispatch({ type: 'SAVE_CHANGES' })}>Save</Button>
                    <Button variant="danger" className="button" onClick={() => dispatch({ type: 'DISCARD_CHANGES' })}>Discard</Button>
                    <Button variant="secondary" className="button" onClick={() => dispatch({ type: 'CANCEL_ACTION' })}>Cancel</Button>
                </Modal.Footer>
            </Modal>

        </>
    );
}