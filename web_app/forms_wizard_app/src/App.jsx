import { createContext, useEffect, useReducer } from 'react';
import ContentAreaComponent from './components/ContentAreaComponent/ContentAreaComponent';
import TopBarComponent from './components/TopBarComponent/TopBarComponent';
import { deepEquals } from './utils/utils';
import './App.css';


const FormWizardContext = createContext();

const initialState = {
  isEditing: false,
  currentForm: {
    formDefinition: null,
    selectedField: null,
    version: 1,
  },
  cachedForm: {
    formDefinition: null,
    version: null
  },
  availableFieldTypes: [],
  fieldSettings: {},
  topBarActions: [],
  showChangesPopup: false,
  pendingAction: null,
  setPendingAction:null,
  showNewFormMetadata:false,
  diff:false,
};

const formWizardReducer = (state = initialState, action) => {
  const pendingAction = state.setPendingAction ? state.setPendingAction : null;
  const diff = state.currentForm.formDefinition && !deepEquals(state.currentForm.formDefinition, state.cachedForm.formDefinition);
  switch (action.type) {
    case 'TOGGLE_EDITING':
      return { ...state, isEditing: !state.isEditing };
    case 'LOAD_FORM':
      return { ...state, currentForm: action.payload, isEditing: true };
    case 'NEW_FORM':
      if (state.currentForm.formDefinition && !deepEquals(state.currentForm.formDefinition, state.cachedForm.formDefinition)) {
        // there are changes on the current form. Ask to save or discard them with a pop up using reactjs-popup. Save and discard should both have eventhandlers with state logic, therefore we'll set pendingAction and useEffect within the provider body
        return { ...state, showChangesPopup: true, setPendingAction: 'NEW_FORM', diff:true};
      }
      return { ...state, showNewFormMetadata: true, pendingAction: null,diff:false};
    case 'EDIT_NEW_FORM':
      return {...state, currentForm: {version:1,formDefinition:action.payload}, cachedForm: {...initialState.cachedForm}, isEditing:true, showNewFormMetadata:false, diff:true}
    case 'UPDATE_FORM':
      return { ...state, currentForm: { ...state.currentForm, formDefinition: action.payload } };
    case 'SELECT_FIELD':
      return { ...state, currentForm: { ...state.currentForm, selectedField: action.payload } };
    case 'UPDATE_FIELD':
      return { ...state, currentForm: { ...state.currentForm, formDefinition: state.currentForm.formDefinition.map(field => field.id === action.payload.id ? action.payload : field) } };
    case 'LOAD_FIELD_TYPES':
      return { ...state, availableFieldTypes: action.payload };
    case 'LOAD_FIELD_SETTINGS':
      return { ...state, fieldSettings: { ...state.fieldSettings, ...action.payload } };
    case 'SAVE_CHANGES':
      // use forms api to try to save the changed form
      
      return state;
    case 'DISCARD_CHANGES':
      return {...state, cachedForm: {...initialState.cachedForm}, currentForm: {...initialState.currentForm}, pendingAction: pendingAction, setPendingAction: null, showChangesPopup:false, diff:false};
    case 'CANCEL_ACTION':
    return {...state,showChangesPopup:false,pendingAction:null,setPendingAction:null,diff:diff}
    default:
      return state;
  }
}

export const FormWizardProvider = ({ children }) => {
  const [state, dispatch] = useReducer(formWizardReducer, initialState);
  useEffect(()=>{
    if(state.pendingAction){
      dispatch({type: state.pendingAction});
    }
    const handleBeforeUnload = (event) => {
      if (state.diff) {
        event.preventDefault();
        event.returnValue = 'You have unsaved changes. Do you really want to leave?';
      }
    };
    window.addEventListener('beforeunload', handleBeforeUnload);
    return () => {
      window.removeEventListener('beforeunload', handleBeforeUnload);
    };
  },[state.pendingAction,state.diff]);

  return (
    <FormWizardContext.Provider value={{ state, dispatch }}>
      {children}
    </FormWizardContext.Provider>
  );
};


export default function App() {

  return (
    <div className="App">
      <FormWizardProvider>
        <TopBarComponent />
        <ContentAreaComponent />
      </FormWizardProvider>
    </div>
  );
}

export { FormWizardContext };
