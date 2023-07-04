import { Component,Inject, OnInit } from '@angular/core';
import { FormBuilder, FormGroup,FormControl, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { EmpdataserviceService } from '../empdataservice.service';
import {FloatLabelType, MatFormFieldModule} from '@angular/material/form-field';
import {MatIconModule} from '@angular/material/icon';
import {MatSelectModule} from '@angular/material/select';
import {MatInputModule} from '@angular/material/input';
import {MatRadioModule} from '@angular/material/radio';
import {MatCheckboxModule} from '@angular/material/checkbox';
import {MatDatepickerModule} from '@angular/material/datepicker';
import { formatDate } from '@angular/common';

@Component({
  selector: 'app-popup',
  templateUrl: './popup.component.html',
  styleUrls: ['./popup.component.scss']
})
export class PopupComponent implements OnInit {
  // form!: FormGroup;
  description!: string;
  email = new FormControl('', [Validators.required, Validators.email]);
  hide = true;
  inputdata:any;
  emp_add!: FormGroup; // Rename 'form' to 'emp_add'
  constructor(
    @Inject(MAT_DIALOG_DATA) public data:any,
  private ref:MatDialogRef<PopupComponent>, 
  private fb: FormBuilder, 
  private service:EmpdataserviceService){}

  ngOnInit(): void {
    this.inputdata=this.data;
    // emp_add = this.fb.group({
    //   name:this.fb.control(''),
    //   address:this.fb.control(''),
    
    // })

    this.emp_add = this.fb.group({
      username: ['', Validators.required],
      first_name: ['', Validators.required],
      last_name: ['', Validators.required],
      password: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      gender: ['', Validators.required],
      mobile_no: ['', Validators.required],
      designation: ['', Validators.required],
      department: ['', Validators.required],
      address: ['', Validators.required],
      date_of_birth: ['', Validators.required],
      education: ['', Validators.required],
      profile_pic: ['', Validators.required],
      document: ['', Validators.required],

    });

  }
  

  getErrorMessage() {
    if (this.email.hasError('required')) {
      return 'You must enter a value';
    }

    return this.email.hasError('email') ? 'Not a valid email' : '';
  }
  closepopup()
  {
    this.ref.close('Closed using Function')
  }
  save() {
    this.ref.close(this.emp_add.value);
}

Save_employee()
{
    // Format the date_of_birth value before sending it to the API
    const formattedDateOfBirth = formatDate(this.emp_add.value.date_of_birth, 'yyyy-MM-dd', 'en-US');
  
    // Update the date_of_birth value in the form group
    this.emp_add.patchValue({ date_of_birth: formattedDateOfBirth });
  
  const formData = new FormData();

  // Append form values
  Object.keys(this.emp_add.value).forEach(key => {
    if (key === 'profile_pic' || key === 'document' || key === 'date_of_birth' ) {
      // Append files separately
      formData.append(key, this.emp_add.value[key]);
    } else {
      formData.append(key, this.emp_add.value[key]);
    }
  });

  console.log(formData);

  console.log(this.emp_add.value);

  this.service.addEmployee(formData).subscribe(res=>{
  console.log('New employee added:', res);
  this.closepopup()
  });
}
onProfilePicSelected(event: any) {
  if (event.target.files && event.target.files.length > 0) {
    const file = event.target.files[0];
    console.log(file)
    this.emp_add.patchValue({ profile_pic: file });
  }
}

onDocumentSelected(event: any) {
  if (event.target.files && event.target.files.length > 0) {
    const file = event.target.files[0];
    console.log(file)
    this.emp_add.patchValue({ document: file });
  }
}

}
