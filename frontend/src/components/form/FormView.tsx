import {ApiForm} from '../../dto';

type Properties = {
  goToTable: () => void,
  goToEdit: (arg0: ApiForm) => void,
  formToBeViewed: ApiForm | null
}

export default function FormView({ goToTable, goToEdit, formToBeViewed }: Properties) {
  return (
    <></>
  );
}