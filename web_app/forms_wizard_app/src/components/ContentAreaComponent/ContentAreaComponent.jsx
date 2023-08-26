import { useContext } from "react"
import { FormWizardContext } from "../../App"
import NewFormMetadataComponent from "../NewFormMetadataComponent/NewFormMetadataComponent";
import LoadFormComponent from "../LoadFormComponent/LoadFormComponent";

export default function ContentAreaComponent() {
    const { state, dispatch } = useContext(FormWizardContext);

    const handleNewForm = (metadata) => {
        const formDefinition = {
            name: metadata.name,
            description: metadata.description,
            version: 1,
            pages: [
                {
                    order: 1,
                    fields: [],
                    dependencies: []
                }
            ]
        };
        dispatch({ type: "EDIT_NEW_FORM", payload: formDefinition });
    };

    const handleLoadForm = (formData) =>{
        
    }

    if (state.showNewFormMetadata) {
        return (
            <div className="container-fluid">
                <NewFormMetadataComponent handle={handleNewForm} />
            </div>);
    }
    if (state.showLoadForm) {
        return (
            <div className="container-fluid">
                <LoadFormComponent handle={handleLoadForm} />
            </div>
            );
    }
    return <div>Content Area</div>
}